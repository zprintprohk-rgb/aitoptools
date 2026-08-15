#!/usr/bin/env python3
"""Unit tests for generate-sitemap_merged.py — v2 (code-review hardened).

Changes vs v1 (review-code.md findings):
- target = generate-sitemap_merged.py (fix + production robots 4 AI agents + heal dedupe)
- dynamic baseline: expected URL count is computed from current data files
  (reviews + blog-posts + 6 categories + 9 fixed pages + blog index) plus the
  current production sitemap preserved entries — no hardcoded 342/541.
- robots.txt assertion: merged script must keep the 4 AI agents
  (Applebot-Extended / Amazonbot / meta-externalagent / cohere-ai).
- non-destructive: fresh timestamped sandbox only; production read-only.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))
FIXED = os.path.join(HERE, 'generate-sitemap_merged.py')
SB = os.path.join(HERE, 'test_sandbox_v2', time.strftime('%Y%m%d-%H%M%S'))
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  [{"PASS" if cond else "FAIL"}] {name} {detail}')


def current_baseline():
    """Dynamic: unique URL count of CURRENT production sitemap (fix adds/removes
    no URLs — it only restores markers + dedupes). Immune to data drift."""
    with open(os.path.join(ROOT, 'public', 'sitemap.xml'), encoding='utf-8') as f:
        content = f.read()
    locs = re.findall(r'<loc>(.*?)</loc>', content)
    return len(set(locs))


def make_sandbox(tag):
    d = os.path.join(SB, tag)
    os.makedirs(os.path.join(d, 'public'), exist_ok=True)
    os.makedirs(os.path.join(d, 'out'), exist_ok=True)
    os.makedirs(os.path.join(d, 'src', 'data'), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, 'src', 'data', 'reviews.json'),
                 os.path.join(d, 'src', 'data', 'reviews.json'))
    shutil.copy2(os.path.join(ROOT, 'src', 'data', 'blog-posts.json'),
                 os.path.join(d, 'src', 'data', 'blog-posts.json'))
    return d


def read_xml_stats(path):
    tree = ET.parse(path)
    urls = tree.getroot().findall('s:url', NS)
    locs = [u.find('s:loc', NS).text for u in urls]
    return len(locs), len(set(locs)), sorted({x for x in locs if locs.count(x) > 1})


def run_fixed(project_dir):
    r = subprocess.run([sys.executable, FIXED, '--project-dir', project_dir],
                       capture_output=True, text=True, encoding='utf-8', timeout=120)
    return r.returncode, r.stdout, r.stderr


def prog_urls():
    with open(os.path.join(ROOT, 'public', 'sitemap-programmatic.xml'), encoding='utf-8') as f:
        content = f.read()
    return re.findall(r'<loc>(.*?)</loc>', content)


def generate_pages_append(content, urls):
    main = re.sub(r'  <!-- PROGRAMMATIC-SEO-START -->[\s\S]*?<!-- PROGRAMMATIC-SEO-END -->\n', '', content)
    block = ('  <!-- PROGRAMMATIC-SEO-START -->\n' +
             '\n'.join(f'  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>'
                       for u in urls) +
             '\n  <!-- PROGRAMMATIC-SEO-END -->\n')
    return main.replace('</urlset>', block + '</urlset>')


def seed_sitemaps(d):
    for sub in ('public', 'out'):
        shutil.copy2(os.path.join(ROOT, 'public', 'sitemap.xml'),
                     os.path.join(d, sub, 'sitemap.xml'))
    shutil.copy2(os.path.join(ROOT, 'public', 'sitemap-programmatic.xml'),
                 os.path.join(d, 'public', 'sitemap-programmatic.xml'))


# dynamic baseline
BASELINE = current_baseline()
print(f'baseline: current production sitemap unique={BASELINE}')

# ---------------- T1: fix on current real state ----------------
print('T1: merged script on current (markerless) state')
d = make_sandbox('t1')
seed_sitemaps(d)
rc, out, err = run_fixed(d)
check('T1 exit 0', rc == 0, f'rc={rc} err={err[:200]}')
p_total, p_uniq, p_dup = read_xml_stats(os.path.join(d, 'public', 'sitemap.xml'))
o_total, o_uniq, o_dup = read_xml_stats(os.path.join(d, 'out', 'sitemap.xml'))
check('T1 public total==baseline', p_total == BASELINE,
      f'total={p_total} baseline={BASELINE}')
check('T1 public unique==total (no dups)', p_uniq == p_total, f'unique={p_uniq} total={p_total}')
check('T1 public no dups', p_dup == [], f'dups={p_dup}')
check('T1 out matches public', (o_total, o_uniq, o_dup) == (p_total, p_uniq, p_dup),
      f'out=({o_total},{o_uniq},{o_dup})')
with open(os.path.join(d, 'public', 'sitemap.xml'), encoding='utf-8') as f:
    healed = f.read()
check('T1 markers restored',
      '<!-- PROGRAMMATIC-SEO-START -->' in healed and '<!-- PROGRAMMATIC-SEO-END -->' in healed)
check('T1 /best/ programmatic present', healed.count('https://aitoptools.net/best/') >= 199,
      f'count={healed.count("https://aitoptools.net/best/")}')
# robots check
with open(os.path.join(d, 'public', 'robots.txt'), encoding='utf-8') as f:
    robots = f.read()
for agent in ['Applebot-Extended', 'Amazonbot', 'meta-externalagent', 'cohere-ai',
              'GPTBot', 'PerplexityBot', 'Google-Extended']:
    check(f'T1 robots has {agent}', agent in robots)

# ---------------- T2: second run idempotent ----------------
print('T2: consecutive second run')
rc2, out2, err2 = run_fixed(d)
check('T2 exit 0', rc2 == 0, f'rc={rc2}')
with open(os.path.join(d, 'public', 'sitemap.xml'), encoding='utf-8') as f:
    after2 = f.read()
check('T2 byte-identical (no re-append)', after2 == healed,
      f'len1={len(healed)} len2={len(after2)}')

# ---------------- T3: reproduce 8/14 (541) then self-heal ----------------
print('T3: 8/14 failure reproduction -> self-heal')
d3 = make_sandbox('t3')
seed_sitemaps(d3)
with open(os.path.join(d3, 'public', 'sitemap.xml'), encoding='utf-8') as f:
    seeded = f.read()
# 自适应双状态：模拟 8/14 旧脚本行为 = 只剥标记注释行、保留中间 URL 块
# （治愈后状态含标记块 → 剥注释得 343 无标记；未治愈状态本无标记 → 不变）
markerless = seeded.replace('  <!-- PROGRAMMATIC-SEO-START -->\n', '').replace('  <!-- PROGRAMMATIC-SEO-END -->\n', '')
markerless = markerless.replace('<!-- PROGRAMMATIC-SEO-START -->\n', '').replace('<!-- PROGRAMMATIC-SEO-END -->\n', '')
assert 'PROGRAMMATIC-SEO' not in markerless, 'precondition: start state is markerless'
broken = generate_pages_append(markerless, prog_urls())  # -> 541-ish, the 8/14 incident
with open(os.path.join(d3, 'public', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(broken)
t, u, du = read_xml_stats(os.path.join(d3, 'public', 'sitemap.xml'))
check('T3 precond broken (total==baseline+199)', (t - u) == 199 and u == BASELINE,
      f'broken state total={t} unique={u} baseline={BASELINE}')
rc3, _, err3 = run_fixed(d3)
t3, u3, d3p = read_xml_stats(os.path.join(d3, 'public', 'sitemap.xml'))
check('T3 exit 0', rc3 == 0, f'rc={rc3} err={err3[:200]}')
check('T3 healed to baseline unique', (t3, u3) == (BASELINE, BASELINE),
      f'total={t3} unique={u3} baseline={BASELINE}')
check('T3 no dups', d3p == [], f'dups={d3p}')
check('T3 markers restored',
      'PROGRAMMATIC-SEO-START' in open(os.path.join(d3, 'public', 'sitemap.xml'),
                                       encoding='utf-8').read())

# ---------------- T4: full cycle stays stable ----------------
print('T4: full cycle (generate-pages.js append on healed file) -> stays stable')
d4 = make_sandbox('t4')
shutil.copy2(os.path.join(d, 'public', 'sitemap.xml'), os.path.join(d4, 'public', 'sitemap.xml'))
shutil.copy2(os.path.join(d, 'out', 'sitemap.xml'), os.path.join(d4, 'out', 'sitemap.xml'))
shutil.copy2(os.path.join(ROOT, 'public', 'sitemap-programmatic.xml'),
             os.path.join(d4, 'public', 'sitemap-programmatic.xml'))
with open(os.path.join(d4, 'public', 'sitemap.xml'), encoding='utf-8') as f:
    healed4 = f.read()
cycled = generate_pages_append(healed4, prog_urls())  # regex matches -> replace
with open(os.path.join(d4, 'public', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(cycled)
t4a, u4a, _ = read_xml_stats(os.path.join(d4, 'public', 'sitemap.xml'))
check('T4 precond cycle stable', (t4a, u4a) == (BASELINE, BASELINE),
      f'total={t4a} unique={u4a} baseline={BASELINE}')
rc4, _, err4 = run_fixed(d4)
t4, u4, d4p = read_xml_stats(os.path.join(d4, 'public', 'sitemap.xml'))
check('T4 exit 0', rc4 == 0, f'rc={rc4}')
check('T4 stays stable, no dups', (t4, u4, d4p) == (BASELINE, BASELINE, []),
      f'total={t4} unique={u4} dups={d4p}')
with open(os.path.join(d4, 'public', 'sitemap.xml'), encoding='utf-8') as f:
    c4 = f.read()
check('T4 markers preserved',
      'PROGRAMMATIC-SEO-START' in c4 and 'PROGRAMMATIC-SEO-END' in c4)

# ---------------- T5: data collisions cannot create dups ----------------
print('T5: regression — dup slug + review/blog slug collision')
d5 = make_sandbox('t5')
seed_sitemaps(d5)
with open(os.path.join(d5, 'src', 'data', 'reviews.json'), encoding='utf-8') as f:
    rv = json.load(f)
rv.append({'slug': 'about'})   # collides with a fixed page
existing = {r.get('slug') for r in rv if isinstance(r, dict)}
rv.append({'slug': next(iter(existing))})  # genuine duplicate slug
with open(os.path.join(d5, 'src', 'data', 'reviews.json'), 'w', encoding='utf-8') as f:
    json.dump(rv, f)
with open(os.path.join(d5, 'src', 'data', 'blog-posts.json'), encoding='utf-8') as f:
    bp = json.load(f)
bp.append({'slug': 'blog'})   # collides with blog index page
with open(os.path.join(d5, 'src', 'data', 'blog-posts.json'), 'w', encoding='utf-8') as f:
    json.dump(bp, f)
rc5, out5, err5 = run_fixed(d5)
t5, u5, d5p = read_xml_stats(os.path.join(d5, 'public', 'sitemap.xml'))
check('T5 exit 0', rc5 == 0, f'rc={rc5} err={err5[:200]}')
check('T5 no duplicate URLs despite poisoned data', d5p == [] and t5 == u5,
      f'total={t5} unique={u5} dups={d5p}')

# ---------------- summary ----------------
print()
fails = [r for r in results if not r[1]]
print(f'SUMMARY: {len(results) - len(fails)}/{len(results)} passed')
for name, ok, detail in fails:
    print(f'  FAILED: {name} {detail}')
sys.exit(1 if fails else 0)
