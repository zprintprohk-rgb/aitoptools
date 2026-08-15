#!/usr/bin/env python3
"""Enumerate preserved (non-script) entries in current sitemap.xml: loc + tag shape."""
import json
import os
import re

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

reviews = load('src/data/reviews.json')
blog = load('src/data/blog-posts.json')
slugs = [r.get('slug') for r in reviews if isinstance(r, dict)]
blog_slugs = [p.get('slug') for p in blog if isinstance(p, dict) and p.get('slug')]

cats = ['ai-print-design', 'ai-ecommerce', 'ai-writing', 'ai-image', 'ai-video', 'ai-voice']
fixed = ['', 'about', 'contact', 'disclaimer', 'affiliate-disclosure', 'privacy', 'terms',
         'submit-tool', 'sponsorships']
pages = fixed + [f'category/{c}' for c in cats] + slugs + ['blog'] + [f'blog/{s}' for s in blog_slugs]
new_urls = [(f'https://aitoptools.net/{p}/' if p else 'https://aitoptools.net/') for p in pages]

with open('public/sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

existing = []
for block in content.split('<url>')[1:]:
    block = '<url>' + block.split('</url>')[0] + '</url>'
    m = re.search(r'<loc>(.*?)</loc>', block)
    if m:
        existing.append((m.group(1), block))

newset = set(new_urls)
preserved = [(loc, b) for loc, b in existing if loc not in newset]
print(f'new_urls={len(new_urls)} (unique {len(newset)}) | existing={len(existing)} | preserved={len(preserved)}')

best = [(loc, b) for loc, b in preserved if '/best/' in loc]
other = [(loc, b) for loc, b in preserved if '/best/' not in loc]
print(f'preserved /best/: {len(best)} | other: {len(other)}')

print('\n--- other (non-/best/) preserved entries ---')
for loc, b in other:
    print(f'  {loc}')
    print(f'    {b}')

print('\n--- tag shapes ---')
from collections import Counter
shapes = Counter()
for loc, b in preserved:
    inner = b[len('<url>'):-len('</url>')]
    tags = re.findall(r'<(\w+)', inner)
    shapes[tuple(tags)] += 1
for k, v in shapes.items():
    print(f'  {v}x tags={k}')

# sample best blocks
print('\n--- sample best block ---')
for loc, b in best[:3]:
    print(f'  {b}')
