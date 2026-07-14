import json, os
from collections import Counter

# Read reviews.json
with open('/mnt/f/aitoptools/src/data/reviews.json') as f:
    reviews = json.load(f)

# Count categories
cats = Counter(r.get('category', 'Unknown') for r in reviews)
print(f"=== Category Distribution ({len(reviews)} total tools) ===")
for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}")

# List all slugs
print(f"\n=== All Slugs ===")
for r in reviews:
    print(f"  {r.get('slug','?')}  [{r.get('category','?')}]")

# Also check logs for pending inventories
log_dir = '/mnt/f/aitoptools/.hermes/logs'
pending_slugs = set()
for fn in sorted(os.listdir(log_dir)):
    if fn.endswith('-新工具入库.json'):
        print(f"\n=== Pending inventory: {fn} ===")
        try:
            with open(os.path.join(log_dir, fn)) as f:
                data = json.load(f)
            tools = data.get('tools', data) if isinstance(data, dict) else data
            for t in tools:
                slug = t.get('slug', t.get('name','?')).lower().replace(' ','-')
                print(f"  {slug}  [{t.get('category','?')}]")
                pending_slugs.add(slug)
        except:
            pass

print(f"\n{pending_slugs}")
