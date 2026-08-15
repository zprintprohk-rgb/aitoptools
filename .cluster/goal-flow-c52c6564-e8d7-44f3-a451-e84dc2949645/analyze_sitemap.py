#!/usr/bin/env python3
"""Read-only audit helper: stats for public/ and out/ sitemap.xml + blog-posts.json count."""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

def analyze(path):
    print(f'=== {path} ===')
    if not os.path.exists(path):
        print('  (not found)')
        return None
    tree = ET.parse(path)
    root = tree.getroot()
    urls = root.findall('s:url', NS)
    locs = [u.find('s:loc', NS).text for u in urls]
    total = len(locs)
    uniq = len(set(locs))
    dup_locs = sorted({x for x in locs if locs.count(x) > 1})
    lms = [u.find('s:lastmod', NS).text for u in urls if u.find('s:lastmod', NS) is not None]
    print(f'  total  : {total}')
    print(f'  unique : {uniq}')
    print(f'  dup_entries_count : {len(dup_locs)}')
    for x in dup_locs:
        print(f'    DUP: {x}')
    if lms:
        print(f'  lastmod min: {min(lms)}  max: {max(lms)}')
    # Blog entries
    blog = [x for x in locs if '/blog/' in x]
    print(f'  /blog/ entries: {len(blog)}')
    return {'path': path, 'total': total, 'unique': uniq, 'dups': dup_locs}

def main():
    results = []
    for p in (os.path.join('public', 'sitemap.xml'), os.path.join('out', 'sitemap.xml')):
        results.append(analyze(os.path.join(os.getcwd(), p)))
    # blog-posts.json count
    bp = os.path.join(os.getcwd(), 'src', 'data', 'blog-posts.json')
    if os.path.exists(bp):
        with open(bp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        n = len(d) if isinstance(d, list) else f'NOT LIST ({type(d).__name__})'
        print(f'=== src/data/blog-posts.json ===')
        print(f'  array length: {n}')
        if isinstance(d, list):
            slugs = [p.get('slug') for p in d if isinstance(p, dict)]
            print(f'  slugs with value: {len([s for s in slugs if s])}')
    else:
        print('blog-posts.json NOT FOUND')

if __name__ == '__main__':
    main()
