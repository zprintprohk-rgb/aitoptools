import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
b = json.load(open(r'src\data\blog-posts.json', encoding='utf-8'))
print('total blog posts:', len(b))
for p in b:
    if 'halloween' in p.get('slug','').lower():
        print(p['slug'], '|', p.get('title','')[:80])
