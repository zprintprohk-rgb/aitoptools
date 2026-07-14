#!/usr/bin/env python3
import json, urllib.request, sys

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"error": str(e)}

queries = [
    "AI+print+design+tool+2026",
    "AI+packaging+design+print",
    "AI+ecommerce+product+photography+tool",
    "AI+print+on+demand+tool",
    "AI+label+sticker+design",
    "AI+catalog+brochure+maker",
]

all_hits = []
for q in queries:
    url = f"https://hn.algolia.com/api/v1/search?query={q}&tags=story&hitsPerPage=10"
    data = fetch_json(url)
    if "error" not in data:
        for h in data.get("hits", []):
            all_hits.append({
                "title": h.get("title", ""),
                "url": h.get("url", ""),
                "points": h.get("points", 0),
                "created_at": h.get("created_at", ""),
            })

seen = set()
unique = []
for h in all_hits:
    key = h["title"][:60]
    if key not in seen:
        seen.add(key)
        unique.append(h)

unique.sort(key=lambda x: -x["points"])

output = {"hn_results": unique[:30], "total_found": len(unique)}
with open("/mnt/f/aitoptools/.hermes/logs/2026-07-07-hn_results.json", "w") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Found {len(unique)} unique HN results, saved")
