import json, os, re

slugs = set()

# From reviews.json
d = json.load(open('/mnt/f/aitoptools/src/data/reviews.json'))
for x in d:
    slugs.add(x['slug'])

logdir = '/mnt/f/aitoptools/.hermes/logs'

# From TSX files
for f in os.listdir(logdir):
    if f.endswith('.tsx'):
        m = re.search(r'长尾-(.+?)\.tsx', f)
        if m:
            slugs.add(m.group(1))

# From JSON tool imports
for fn in os.listdir(logdir):
    if '新工具入库' in fn:
        try:
            nd = json.load(open(os.path.join(logdir, fn)))
            for t in nd.get('tools', []):
                slugs.add(t.get('slug', ''))
        except: pass

print(f"Total unique slugs: {len(slugs)}")
for s in sorted(slugs):
    print(s)
