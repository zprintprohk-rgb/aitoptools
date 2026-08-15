# -*- coding: utf-8 -*-
"""T2 验证：sitemap 343/343/0 + 标记恢复 + /best/ 202 + robots 无损 + git status"""
import os, re, sys, subprocess
sys.stdout.reconfigure(errors='replace')
ROOT = r'F:\aitoptools'

print('=== sitemap 验证 ===')
for sub in ['public', 'out']:
    p = os.path.join(ROOT, sub, 'sitemap.xml')
    c = open(p, encoding='utf-8').read()
    locs = re.findall(r'<loc>(.*?)</loc>', c)
    total, uniq = len(locs), len(set(locs))
    dups = [x for x in set(locs) if locs.count(x) > 1]
    has_start = '<!-- PROGRAMMATIC-SEO-START -->' in c
    has_end = '<!-- PROGRAMMATIC-SEO-END -->' in c
    best = c.count('https://aitoptools.net/best/')
    print(f'{sub}: total={total} unique={uniq} dups={len(dups)} markers=({has_start},{has_end}) /best/={best}')
    if dups:
        print('  DUPS:', dups[:5])
    # 标记块缩进检查（generate-pages.js 依赖两空格）
    m = re.search(r'\n( *)<!-- PROGRAMMATIC-SEO-START -->', c)
    print(f'  marker indent: {len(m.group(1))} spaces' if m else '  marker indent: NOT FOUND')

print()
print('=== robots 无损验证（7 代理 + sitemap 行）===')
for sub in ['public', 'out']:
    p = os.path.join(ROOT, sub, 'robots.txt')
    c = open(p, encoding='utf-8').read()
    agents = [a for a in ['Applebot-Extended', 'Amazonbot', 'meta-externalagent', 'cohere-ai',
                          'GPTBot', 'ClaudeBot', 'PerplexityBot', 'Google-Extended'] if a in c]
    ok_sitemap = 'Sitemap: https://aitoptools.net/sitemap.xml' in c
    print(f'{sub}/robots.txt: agents={len(agents)} {agents} sitemap_line={ok_sitemap}')

print()
print('=== 单测回归 ===')
r = subprocess.run(['python', r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\sitemap_fix_test_v2.py'],
                   capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=300)
tail = (r.stdout or '')[-300:]
print('rc =', r.returncode)
print(tail)

print()
print('=== git status（改动清单）===')
r = subprocess.run(['git', '-C', ROOT, 'status', '--short'], capture_output=True, text=True, encoding='utf-8', errors='replace')
for line in (r.stdout or '').splitlines():
    if 'generate-sitemap' in line or 'sitemap.xml' in line or 'robots.txt' in line:
        print(' ', line)
