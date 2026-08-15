import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
l = json.load(open(r'src\data\listicles.json', encoding='utf-8'))
print('total listicles:', len(l))
for x in l:
    print(x['slug'], '|', x.get('category'), '| items:', len(x.get('items',[])))
