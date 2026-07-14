import json

with open("F:/aitoptools/src/data/reviews.json", "r") as f:
    data = json.load(f)

print(f"Total reviews: {len(data)}")
cats = {}
for r in data:
    cat = r["category"]
    cats[cat] = cats.get(cat, 0) + 1
for k, v in sorted(cats.items()):
    print(f"  {k}: {v}")

# Update generation log
log_path = "F:/aitoptools/content-generation-log.json"
try:
    with open(log_path, "r") as f:
        log = json.load(f)
except:
    log = []

new_entries = []
for r in data:
    if r["slug"] not in [e["slug"] for e in log]:
        new_entries.append({
            "slug": r["slug"],
            "title": r["title"],
            "timestamp": "2026-06-27T13:30:00Z",
            "model": "deepseek-v4-flash",
            "template_type": "single-review",
            "category": r["category"],
            "verified": False
        })

log.extend(new_entries)
with open(log_path, "w") as f:
    json.dump(log, f, indent=2)

print(f"\nLog updated: {len(log)} total entries (+{len(new_entries)} new)")
