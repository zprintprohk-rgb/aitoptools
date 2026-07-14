import json

# Verify the new tools file
with open(r'F:\aitoptools\.hermes\logs\2026-07-01-new-tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Date: {data['date']}")
print(f"Phase: {data['phase']}")
print(f"Total: {data['total_new']} tools")
print()

existing_slugs = set([
    'jasper-ai-review', 'writesonic-review', 'heygen-review', 'elevenlabs-review',
    'hostinger-review', 'copy-ai-review', 'rytr-review', 'midjourney-review',
    'leonardo-ai-review', 'runway-ml-review', 'claid-ai-review', 'synthesia-review',
    'cursor-review', 'notion-ai-review', 'perplexity-pro-review', 'suno-ai-review',
    'gamma-ai-review', 'canva-ai-review', 'descript-review', 'pika-labs-review',
    'chatgpt-review', 'best-ai-writing-tools-comparison', 'nordvpn-review'
])

new_slugs = set()
for t in data['tools']:
    assert t['slug'] not in existing_slugs, f"DUPLICATE: {t['slug']}"
    assert len(t['pros']) >= 3, f"Too few pros: {t['slug']}"
    assert len(t['cons']) >= 3, f"Too few cons: {t['slug']}"
    assert t['content'] and len(t['content']) > 200, f"Content too short: {t['slug']}"
    assert t['affiliateUrl'] and t['visitUrl'], f"Missing URLs: {t['slug']}"
    new_slugs.add(t['slug'])
    print(f"✓ {t['slug']:40s} | {t['category']:25s} | {t['price']:20s} | {t['rating']}/5")

assert len(new_slugs) == 10, f"Expected 10 unique tools, got {len(new_slugs)}"
print()
print("✅ All 10 tools verified — no duplicates, complete data")
