import json

with open('/mnt/f/aitoptools/src/data/reviews.json') as f:
    d = json.load(f)
print(f"{len(d)} tools in reviews.json")

# Show existing slugs
slugs = set(r['slug'] for r in d)
print("Existing slugs:")
for s in sorted(slugs):
    print(f"  {s}")
