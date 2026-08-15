#!/usr/bin/env python3
"""Root-cause probe: check data sources for dup slugs / collisions that break dedup."""
import json
import os
import re

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

reviews = load('src/data/reviews.json')
blog = load('src/data/blog-posts.json')

slugs = [r.get('slug') for r in reviews if isinstance(r, dict)]
print(f'reviews.json: {len(reviews)} items, {len(slugs)} slugs')
dups = sorted({s for s in slugs if slugs.count(s) > 1})
print(f'  dup review slugs: {len(dups)} {dups}')

blog_slugs = [p.get('slug') for p in blog if isinstance(p, dict) and p.get('slug')]
print(f'blog-posts.json: {len(blog)} items, {len(blog_slugs)} slugs')
bdups = sorted({s for s in blog_slugs if blog_slugs.count(s) > 1})
print(f'  dup blog slugs: {len(bdups)} {bdups}')

fixed = ['', 'about', 'contact', 'disclaimer', 'affiliate-disclosure', 'privacy', 'terms',
         'submit-tool', 'sponsorships', 'blog']
cats = ['ai-print-design', 'ai-ecommerce', 'ai-writing', 'ai-image', 'ai-video', 'ai-voice']
cat_pages = [f'category/{c}' for c in cats]

all_pages = fixed + cat_pages + slugs + ['blog'] + [f'blog/{s}' for s in blog_slugs]
n = len(all_pages)
u = len(set(all_pages))
print(f'\npages list (script logic): total={n} unique={u} dup_in_list={n-u}')

dups_in_list = sorted({x for x in all_pages if all_pages.count(x) > 1})
for x in dups_in_list:
    print(f'  DUP PAGE: {x!r} x{all_pages.count(x)}')

# collisions between review slugs and fixed/category/blog namespaces
fixed_set = set(fixed) | set(cat_pages) | {'blog/' + s for s in blog_slugs}
collisions = [s for s in slugs if s in fixed_set]
print(f'\nreview-slug collisions with fixed/cat/blog namespaces: {collisions}')

# how many pages would the CURRENT script write fresh (no existing merge)?
fresh = [('https://aitoptools.net/' if not p else f'https://aitoptools.net/{p}/') for p in all_pages]
print(f'fresh URL list: total={len(fresh)} unique={len(set(fresh))}')

# existing file: what would merge keep?
for sub in ('public', 'out'):
    path = os.path.join(sub, 'sitemap.xml')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    existing = []
    for block in content.split('<url>')[1:]:
        block = '<url>' + block.split('</url>')[0] + '</url>'
        m = re.search(r'<loc>(.*?)</loc>', block)
        if m:
            existing.append((m.group(1), block))
    ex_locs = [l for l, _ in existing]
    print(f'\n{path}: existing blocks={len(existing)} unique locs={len(set(ex_locs))}')
    ex_dups = sorted({x for x in ex_locs if ex_locs.count(x) > 1})
    print(f'  dup locs inside existing file: {len(ex_dups)}')
    for x in ex_dups[:20]:
        print(f'    {x} x{ex_locs.count(x)}')
    # merge simulation
    seen = set(fresh)
    merged = list(fresh)
    preserved = 0
    for loc, block in existing:
        if loc not in seen:
            merged.append(loc)
            seen.add(loc)
            preserved += 1
    print(f'  merge sim: merged_total={len(merged)} unique={len(set(merged))} preserved={preserved}')
