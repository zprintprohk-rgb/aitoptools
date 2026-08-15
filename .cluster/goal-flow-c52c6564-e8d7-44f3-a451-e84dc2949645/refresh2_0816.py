# -*- coding: utf-8 -*-
import json, os, re, time

import sys
sys.stdout.reconfigure(errors='replace')

print('=== RESULT-2026-08-15.md (20:46 version) key lines ===')
p = r'F:\aitoptools\handoff\results\RESULT-2026-08-15.md'
lines = open(p, encoding='utf-8').read().splitlines()
for i, l in enumerate(lines, 1):
    if any(k in l for k in ['NORTH-STAR', 'push', 'Boost', '外链', '扩写', 'halloween', 'IndexNow',
                            'Kittl', 'W-8', 'D6', 'D7', '哨兵', '快修']):
        print(i, '|', l[:150])

print()
print('=== blog test article live status ===')
slug = 'kittl-halloween-template-test-2026'
for f in [r'F:\aitoptools\public\sitemap.xml', r'F:\aitoptools\out\sitemap.xml']:
    if os.path.exists(f):
        c = open(f, encoding='utf-8').read()
        print(os.path.basename(f), '| contains slug:', slug in c, '| blog entries:', c.count('/blog/'))
out_html = os.path.join(r'F:\aitoptools\out\blog', slug)
print('out/blog html exists:', os.path.isdir(out_html) and len(os.listdir(out_html)) > 0)
if os.path.isdir(out_html):
    import datetime
    mt = datetime.datetime.fromtimestamp(os.path.getmtime(out_html)).strftime('%m-%d %H:%M')
    print('out/blog html mtime:', mt)

print()
print('=== blog-posts.json entry #11 ===')
bp = json.load(open(r'F:\aitoptools\src\data\blog-posts.json', encoding='utf-8'))
for x in bp:
    if x.get('slug') == slug:
        print(json.dumps({k: x.get(k) for k in ['slug', 'title', 'publishedAt', 'wordCount', 'status', 'blocks']},
                         ensure_ascii=False, default=str)[:400])
        break

print()
print('=== public/tool-screenshots/blog ===')
bd = r'F:\aitoptools\public\tool-screenshots\blog'
print('dir exists:', os.path.isdir(bd), '| files:', os.listdir(bd) if os.path.isdir(bd) else 'N/A')
