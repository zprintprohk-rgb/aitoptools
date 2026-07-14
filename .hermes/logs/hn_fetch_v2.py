#!/usr/bin/env python3
"""Fetch HackerNews best stories to source new AI tools."""
import sys, json, urllib.request, time, os

logdir = '/f/aitoptools/.hermes/logs'

try:
    resp = urllib.request.urlopen(
        "https://hacker-news.firebaseio.com/v0/beststories.json",
        timeout=15
    )
    ids = json.loads(resp.read())[:30]
except Exception as e:
    print(f"FETCH_ERROR: {e}")
    sys.exit(1)

tools = []
for sid in ids:
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

outpath = os.path.join(logdir, 'hn_trending.json')
with open(outpath, 'w') as f:
    json.dump(tools, f, indent=2)

print(f"OK: {len(tools)} stories saved to {outpath}")
for t in tools[:10]:
    print(f"  - {t['title'][:80]}")
