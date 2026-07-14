#!/usr/bin/env python3
"""
Generate sitemap.xml for aitoptools.net from reviews.json.
Also updates robots.txt with correct sitemap URL.

Usage: python scripts/generate-sitemap.py
Run after adding new articles to reviews.json.
"""

import json
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = 'https://aitoptools.net'

def main():
    # Load reviews
    reviews_path = os.path.join(PROJECT_DIR, 'src', 'data', 'reviews.json')
    with open(reviews_path, 'r', encoding='utf-8') as f:
        reviews = json.load(f)

    slugs = [r['slug'] for r in reviews]
    cats = set(r['category'] for r in reviews)
    cat_slugs = sorted(cat.lower().replace(' ', '-').replace('&', 'and') for cat in cats)

    # Build page list
    pages = [
        '',                          # homepage
        'about',
        'disclaimer',
        'affiliate-disclosure',
        'privacy',
        'submit-tool',
        'sponsorships',
    ]
    for cs in cat_slugs:
        pages.append(f'category/{cs}')
    pages.extend(slugs)

    # Generate sitemap XML
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for page in pages:
        if page:
            url = f'{DOMAIN}/{page}/'
        else:
            url = f'{DOMAIN}/'
        lines.append(f'  <url><loc>{url}</loc><changefreq>weekly</changefreq></url>')
    lines.append('</urlset>')

    # Write sitemap.xml to both public/ (source) and out/ (deployed)
    for subdir in ('public', 'out'):
        sitemap_path = os.path.join(PROJECT_DIR, subdir, 'sitemap.xml')
        os.makedirs(os.path.dirname(sitemap_path), exist_ok=True)
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        print(f'  ✓ {sitemap_path} ({len(pages)} URLs)')

    # Write robots.txt
    robots = f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n'
    for subdir in ('public', 'out'):
        robots_path = os.path.join(PROJECT_DIR, subdir, 'robots.txt')
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(robots)
        print(f'  ✓ {robots_path}')

    print(f'\nDone. {len(pages)} URLs in sitemap.')


if __name__ == '__main__':
    main()
