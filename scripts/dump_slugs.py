import json

d = json.load(open('/mnt/f/aitoptools/src/data/reviews.json'))
print('Count:', len(d))
for x in d:
    print(x.get('slug','?'), x.get('category','?'), x.get('name','?')[:40])
