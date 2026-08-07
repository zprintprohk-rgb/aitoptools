#!/usr/bin/env python3
"""
Generate sitemap.xml for aitoptools.net from reviews.json.
Also updates robots.txt with correct sitemap URL.

Usage: python scripts/generate-sitemap.py
Run after adding new articles to reviews.json.
"""

import json
import os
import re
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = 'https://aitoptools.net'

def main():
    # Load reviews
    reviews_path = os.path.join(PROJECT_DIR, 'src', 'data', 'reviews.json')
    with open(reviews_path, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    slugs = [r['slug'] for r in reviews]

    # Load blog posts (2026-08-04: Blog 加入 sitemap)
    blog_slugs = []
    blog_path = os.path.join(PROJECT_DIR, 'src', 'data', 'blog-posts.json')
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

    # Generate sitemap XML
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    new_urls = []
    for page in pages:
        if page:
            url = f'{DOMAIN}/{page}/'
        else:
            url = f'{DOMAIN}/'
        new_urls.append(url)
        lines.append(f'  <url><loc>{url}</loc><changefreq>weekly</changefreq></url>')
    lines.append('</urlset>')

    # Write sitemap.xml to both public/ (source) and out/ (deployed)
    # 2026-08-04: 合并保底 — 现有 sitemap 含 compare//best//程序化页(PROGRAMMATIC-SEO 块)等
    # 本脚本不认识的 URL, 整体覆盖会丢数据。改为: 新生成 URL ∪ 已有 URL（去重保序）。
    for subdir in ('public', 'out'):
        sitemap_path = os.path.join(PROJECT_DIR, subdir, 'sitemap.xml')
        os.makedirs(os.path.dirname(sitemap_path), exist_ok=True)
        existing = []  # 完整 <url>...</url> 块（保留原有 priority/changefreq）
        if os.path.exists(sitemap_path):
            with open(sitemap_path, 'r', encoding='utf-8') as f:
                content = f.read()
            for block in content.split('<url>')[1:]:
                block = '<url>' + block.split('</url>')[0] + '</url>'
                loc_m = re.search(r'<loc>(.*?)</loc>', block)
                if loc_m:
                    existing.append((loc_m.group(1), block))
        merged_blocks = [f'  <url><loc>{u}</loc><changefreq>weekly</changefreq></url>' for u in new_urls]
        seen = set(new_urls)
        for loc, block in existing:
            if loc not in seen:
                merged_blocks.append('  ' + block)
                seen.add(loc)
        merged_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        ]
        merged_lines.extend(merged_blocks)
        merged_lines.append('</urlset>')
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(merged_lines) + '\n')
        print(f'  ✓ {sitemap_path} ({len(merged_blocks)} URLs, +{len(merged_blocks) - len(new_urls)} preserved)')

    # Write robots.txt
    robots = (
        '# Explicitly welcome AI crawlers — this site's content is meant to be cited.\n'
        'User-agent: GPTBot\nAllow: /\n\n'
        'User-agent: ClaudeBot\nAllow: /\n\n'
        'User-agent: PerplexityBot\nAllow: /\n\n'
        'User-agent: Google-Extended\nAllow: /\n\n'
        f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n'
    )
    for subdir in ('public', 'out'):
        robots_path = os.path.join(PROJECT_DIR, subdir, 'robots.txt')
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots)
        print(f'  ✓ {robots_path}')

    print(f'\nDone. {len(pages)} URLs in sitemap.')


if __name__ == '__main__':
    main()
