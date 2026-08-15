# -*- coding: utf-8 -*-
import subprocess, json, os

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip() + ('\n' + r.stderr.strip() if r.stderr.strip() else '')

print('=== git log origin/main (8) ===')
print(run('git -C F:\\aitoptools log --oneline -8 origin/main --date=format:%m-%d\\ %H:%M --pretty=format:%h\\ %ad\\ %s'))
print()
print('=== git status short ===')
print(run('git -C F:\\aitoptools status --short')[:2000])
print()
print('=== handoff newest files ===')
for base in ['strategy', 'results']:
    p = os.path.join(r'F:\aitoptools\handoff', base)
    files = sorted(os.listdir(p), key=lambda f: os.path.getmtime(os.path.join(p, f)), reverse=True)[:4]
    for f in files:
        fp = os.path.join(p, f)
        import time
        print(base, '|', f, '|', time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(fp))))
print()
print('=== copy-ai-review current state ===')
rv = json.load(open(r'F:\aitoptools\src\data\reviews.json', encoding='utf-8'))
r = [x for x in rv if x.get('slug') == 'copy-ai-review']
if r:
    x = r[0]
    print('title:', x.get('title'), '| len:', len(x.get('title', '')))
    print('metaDesc:', (x.get('metaDesc') or '')[:90], '| len:', len(x.get('metaDesc') or ''))
    print('dateModified:', x.get('dateModified'))
else:
    print('NOT FOUND')
print()
print('=== blog-posts count ===')
bp = json.load(open(r'F:\aitoptools\src\data\blog-posts.json', encoding='utf-8'))
print('posts:', len(bp), [p.get('slug') for p in bp][-4:])
