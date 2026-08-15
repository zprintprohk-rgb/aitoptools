#!/usr/bin/env python3
"""
Generate sitemap.xml for aitoptools.net from reviews.json.
Also updates robots.txt with correct sitemap URL.

Usage: python scripts/generate-sitemap.py [--project-dir DIR]
Run after adding new articles to reviews.json.

FIX 2026-08-16 v2 (tech-debt audit + code review, see review-code.md):
- v2 = 修复版 + 生产 robots 4 AI 代理(Applebot-Extended/Amazonbot/meta-externalagent/cohere-ai) 合并
- v2 = heal 路径 prog_blocks 内部按 loc 去重（542-markerless 边缘）
- Root cause of the 8/14 duplication (541 entries): the "合并保底" merge split the
  existing file on '<url>' and discarded everything between <url> blocks — including
  the `<!-- PROGRAMMATIC-SEO-START/END -->` markers that scripts/generate-pages.js
  uses to make its append idempotent. Once the markers were stripped, the next
  generate-pages.js run could not find/remove its old block and appended the 199
  /best/ URLs again (342 + 199 = 541).
- Fix: preserve (and heal) the PROGRAMMATIC-SEO marker block, dedupe by normalized
  <loc> across new + existing + programmatic URLs, and dedupe new_urls themselves
  (defensive against future slug collisions in data files).
"""

import argparse
import json
import os
import re
import sys

DOMAIN = 'https://aitoptools.net'

# Matches the marker block written by scripts/generate-pages.js (it removes this
# exact block before re-appending, so we must never lose these markers).
PROGRAMMATIC_RE = re.compile(
    r'\s*<!-- PROGRAMMATIC-SEO-START -->[\s\S]*?<!-- PROGRAMMATIC-SEO-END -->\s*'
)


def _norm_loc(loc):
    """Normalize a <loc> for dedup: trim, unescape &amp;, enforce single trailing slash."""
    loc = (loc or '').strip().replace('&amp;', '&')
    if loc and not loc.endswith('/'):
        loc += '/'
    return loc


def _parse_blocks(content):
    """Split sitemap XML into complete '<url>...</url>' blocks (raw string level)."""
    blocks = []
    for part in content.split('<url>')[1:]:
        part = part.split('</url>')[0]
        if '<loc>' not in part:
            continue
        blocks.append('<url>' + part + '</url>')
    return blocks


def _load_programmatic_locs(root):
    """Loc set of sitemap-programmatic.xml (199 /best/ URLs owned by generate-pages.js)."""
    prog_path = os.path.join(root, 'public', 'sitemap-programmatic.xml')
    locs = set()
    if os.path.exists(prog_path):
        try:
            with open(prog_path, 'r', encoding='utf-8') as f:
                for m in re.finditer(r'<loc>(.*?)</loc>', f.read()):
                    locs.add(_norm_loc(m.group(1)))
        except OSError:
            locs = set()
    return locs


def _extract_programmatic_block(content):
    """Return (block_with_markers_or_None, normalized_locs_inside, remainder)."""
    m = PROGRAMMATIC_RE.search(content)
    if not m:
        return None, set(), content
    block = m.group(0).strip('\n')  # keep leading two-space indent (generate-pages.js regex depends on it)
    locs = {_norm_loc(x) for x in re.findall(r'<loc>(.*?)</loc>', block)}
    remainder = content[:m.start()] + content[m.end():]
    return block, locs, remainder


def _is_programmatic_block(block, prog_locs):
    """True if block belongs to the generate-pages.js programmatic set (loc-based)."""
    m = re.search(r'<loc>(.*?)</loc>', block)
    if not m:
        return False
    loc = _norm_loc(m.group(1))
    if prog_locs:
        return loc in prog_locs
    # Fallback signature (prog file missing): /best/ + priority 0.7 as written by
    # scripts/generate-pages.js.
    return '/best/' in loc and 'priority>0.7' in block


def build_sitemap_content(new_urls, existing_content, prog_locs):
    """Merge new URLs with existing sitemap content.

    Idempotent: preserves the PROGRAMMATIC-SEO marker block (healing it if the
    previous run stripped the markers) and dedupes by normalized <loc>.
    Returns (merged_lines_list, stats_dict).
    """
    # 1. new URLs — dedupe among themselves (defensive vs data slug collisions)
    seen_new = set()
    deduped_new = []
    for u in new_urls:
        n = _norm_loc(u)
        if n in seen_new:
            continue
        seen_new.add(n)
        deduped_new.append(u)

    # 2. extract marker block + remaining plain blocks
    prog_block, prog_locs_inside, rest = _extract_programmatic_block(existing_content)
    existing = []
    for b in _parse_blocks(rest):
        m = re.search(r'<loc>(.*?)</loc>', b)
        if m:
            existing.append((_norm_loc(m.group(1)), b))

    # 3. split preserved blocks into programmatic vs other
    prog_blocks = []
    other_blocks = []
    for loc, block in existing:
        if loc in prog_locs_inside or _is_programmatic_block(block, prog_locs):
            prog_blocks.append((loc, block))
        else:
            other_blocks.append((loc, block))

    # 4. merge (new first, then other preserved, programmatic block last)
    merged = [f'  <url><loc>{u}</loc><changefreq>weekly</changefreq></url>' for u in deduped_new]
    seen = set(seen_new)
    for loc, block in other_blocks:
        if loc not in seen:
            merged.append('  ' + block)
            seen.add(loc)
    stats = {'new': len(deduped_new), 'preserved': len(other_blocks) + len(prog_blocks),
             'programmatic': len(prog_blocks)}
    if prog_block is not None:
        merged.append(prog_block)  # keep original verbatim (markers intact)
    elif prog_blocks:
        # Heal: previous run(s) stripped the markers — re-wrap the programmatic
        # entries so generate-pages.js's idempotent replace keeps working.
        healed = ['  <!-- PROGRAMMATIC-SEO-START -->']
        healed_locs = set(seen_new)
        for loc, b in prog_blocks:
            if loc not in healed_locs:  # dedupe inside prog_blocks too (edge: 542-markerless)
                healed.append('  ' + b)
                healed_locs.add(loc)
        healed.append('  <!-- PROGRAMMATIC-SEO-END -->')
        merged.append('\n'.join(healed))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    lines.extend(merged)
    lines.append('</urlset>')
    return lines, stats


def main():
    parser = argparse.ArgumentParser(description='Generate sitemap.xml (merge-safe)')
    parser.add_argument('--project-dir', default=None,
                        help='Override project root (used by tests/sandbox)')
    args = parser.parse_args()

    if hasattr(sys.stdout, 'reconfigure'):
        # Windows GBK console cannot encode '✓' — avoid UnicodeEncodeError crashes.
        sys.stdout.reconfigure(errors='replace')

    if args.project_dir:
        root = os.path.abspath(args.project_dir)
    else:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Load reviews
    reviews_path = os.path.join(root, 'src', 'data', 'reviews.json')
    with open(reviews_path, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    slugs = [r['slug'] for r in reviews]

    # Load blog posts (2026-08-04: Blog 加入 sitemap)
    blog_slugs = []
    blog_path = os.path.join(root, 'src', 'data', 'blog-posts.json')
    if os.path.exists(blog_path):
        try:
            with open(blog_path, 'r', encoding='utf-8') as f:
                blog_posts = json.load(f)
            blog_slugs = [p['slug'] for p in blog_posts if p.get('slug')]
        except (json.JSONDecodeError, TypeError):
            blog_slugs = []

    # Canonical categories — MUST match CATEGORY_MAP in src/app/category/[slug]/page.js.
    # Do NOT derive from reviews.json: its category labels are messy (21 variants)
    # and produce category URLs that don't exist (404), poisoning the sitemap.
    cat_slugs = [
        'ai-print-design',
        'ai-ecommerce',
        'ai-writing',
        'ai-image',
        'ai-video',
        'ai-voice',
    ]

    # Build page list
    pages = [
        '',                          # homepage
        'about',
        'contact',
        'disclaimer',
        'affiliate-disclosure',
        'privacy',
        'terms',
        'submit-tool',
        'sponsorships',
    ]
    for cs in cat_slugs:
        pages.append(f'category/{cs}')
    pages.extend(slugs)
    pages.append('blog')             # blog index
    pages.extend(f'blog/{s}' for s in blog_slugs)

    new_urls = [(f'{DOMAIN}/{p}/' if p else f'{DOMAIN}/') for p in pages]

    # Generate sitemap XML (merge-safe) and write to public/ and out/
    # 2026-08-04: 合并保底 — 现有 sitemap 含 compare//best//程序化页(PROGRAMMATIC-SEO 块)等
    # 本脚本不认识的 URL, 整体覆盖会丢数据。改为: 新生成 URL ∪ 已有 URL（去重保序）。
    # 2026-08-16: 修复 — 保留/修复 PROGRAMMATIC-SEO 标记块, 按规范化 loc 去重。
    prog_locs = _load_programmatic_locs(root)
    for subdir in ('public', 'out'):
        sitemap_path = os.path.join(root, subdir, 'sitemap.xml')
        os.makedirs(os.path.dirname(sitemap_path), exist_ok=True)
        existing_content = ''
        if os.path.exists(sitemap_path):
            with open(sitemap_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        merged_lines, stats = build_sitemap_content(new_urls, existing_content, prog_locs)
        text = '\n'.join(merged_lines)
        url_count = text.count('<url>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(text + '\n')
        print(f'  OK {sitemap_path} ({url_count} URLs, '
              f'+{stats["preserved"]} preserved, {stats["programmatic"]} programmatic)')

    # Write robots.txt
    robots = (
        "# Explicitly welcome AI crawlers — this site's content is meant to be cited.\n"
        'User-agent: GPTBot\n'
        'Allow: /\n'
        '\n'
        'User-agent: ClaudeBot\n'
        'Allow: /\n'
        '\n'
        'User-agent: PerplexityBot\n'
        'Allow: /\n'
        '\n'
        'User-agent: Google-Extended\n'
        'Allow: /\n'
        '\n'
        'User-agent: Applebot-Extended\n'
        'Allow: /\n'
        '\n'
        'User-agent: Amazonbot\n'
        'Allow: /\n'
        '\n'
        'User-agent: meta-externalagent\n'
        'Allow: /\n'
        '\n'
        'User-agent: cohere-ai\n'
        'Allow: /\n'
        '\n'
        'User-agent: *\n'
        'Allow: /\n'
        'Sitemap: https://aitoptools.net/sitemap.xml\n'
    )
    for subdir in ('public', 'out'):
        robots_path = os.path.join(root, subdir, 'robots.txt')
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots)
        print(f'  ✓ {robots_path}')

    print(f'\nDone. {len(pages)} base URLs in sitemap.')


if __name__ == '__main__':
    main()
