import json, os

D = chr(36)

# Load existing reviews
with open('/mnt/f/aitoptools/src/data/reviews.json', 'r') as f:
    existing = json.load(f)
existing_slugs = {r['slug'] for r in existing}

# Load today's new tools
with open('/mnt/f/aitoptools/.hermes/logs/2026-07-16-new-tools.json', 'r') as f:
    new_data = json.load(f)
new_tools = new_data.get('tools', new_data) if isinstance(new_data, dict) else new_data

print(f"Loaded {len(new_tools)} new tools, {len(existing)} existing tools")
print(f"Slugs already in reviews: {[t['slug'] for t in new_tools if t['slug'] in existing_slugs]}")
