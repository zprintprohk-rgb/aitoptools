#!/usr/bin/env python3
import sys, json, urllib.request, time

# Fetch best stories from HN
try:
    resp = urllib.request.urlopen("https://hacker-news.firebaseio.com/v0/beststories.json", timeout=15)
    ids = json.loads(resp.read())[:30]
except Exception as e:
    print(f"ERROR fetching best stories: {e}", file=sys.stderr)
    sys.exit(1)

tools = []
for i, sid in enumerate(ids):
    try:
        url = f'https://hacker-news.firebaseio.com/v0/item/{sid}.json'
        data = json.loads(urllib.request.urlopen(url, timeout=10).read())
        title = data.get('title', '')
        url_field = data.get('url', '')
        if url_field and not url_field.startswith('item?'):
            tools.append({'id': sid, 'title': title, 'url': url_field})
    except Exception as e:
        pass
    time.sleep(0.1)

with open('/f/aitoptools/.hermes/logs/hn_trends.json', 'w') as f:
    json.dump(tools, f, indent=2)

print(f"OK: Fetched {len(tools)} stories from HN")
