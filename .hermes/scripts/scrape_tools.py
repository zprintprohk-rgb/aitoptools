"""Scrape ProductHunt + HackerNews for AI tools"""
import json, requests, re, os, subprocess
from datetime import datetime

# Unset proxy that may block connections
for var in ['http_proxy','https_proxy','HTTP_PROXY','HTTPS_PROXY','all_proxy','ALL_PROXY']:
    os.environ.pop(var, None)

today = datetime.now().strftime("%Y-%m-%d")
results = []
log_dir = "/mnt/f/aitoptools/.hermes/logs"

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_json(url, method='GET', json_data=None, timeout=20):
    try:
        if method == 'GET':
            resp = requests.get(url, headers=HEADERS, verify=False, timeout=timeout)
            return resp.json() if resp.status_code == 200 else None
        else:
            resp = requests.post(url, json=json_data, headers={**HEADERS, 'Content-Type': 'application/json'}, verify=False, timeout=timeout)
            return resp.json() if resp.status_code == 200 else None
    except Exception as e:
        try:
            if json_data:
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                    json.dump(json_data, f)
                    tmpfile = f.name
                r = subprocess.run(['curl','-sk','--noproxy','*','-X','POST','-H','Content-Type: application/json','-d',f'@{tmpfile}',url], capture_output=True, text=True, timeout=timeout)
                os.unlink(tmpfile)
            else:
                r = subprocess.run(['curl','-sk','--noproxy','*',url], capture_output=True, text=True, timeout=timeout)
            return json.loads(r.stdout) if r.stdout else None
        except:
            return None

print("=== Scraping ProductHunt ===")
ph_query = {"query": "{ posts(first: 40, order: NEWEST) { edges { node { id name tagline description url website slug topics { edges { node { name } } } } } } }"}
data = fetch_json("https://api.producthunt.com/v2/api/graphql", method='POST', json_data=ph_query)
if data:
    posts = data.get('data',{}).get('posts',{}).get('edges',[])
    kw = ['ai','artificial intelligence','design','print','image','photo','video','writing','content','marketing','ecommerce','shopify','saas','productivity','logo','mockup','label','package','barcode','label','3d','render']
    for edge in posts[:25]:
        node = edge['node']
        topics = [t['node']['name'] for t in node.get('topics',{}).get('edges',[])]
        tagline = (node.get('tagline','') or '').lower()
        topic_str = ' '.join(topics).lower()
        name = node.get('name','')
        if any(k in tagline or k in topic_str for k in kw):
            results.append({
                'name': name, 'tagline': node.get('tagline',''), 'description': node.get('description',''),
                'website': node.get('website',''), 'url': f"https://www.producthunt.com/posts/{node.get('slug','')}",
                'source': 'ProductHunt', 'topics': topics, 'collected_date': today
            })
    print(f"  PH: {len(posts)} posts processed, {len(results)} relevant")
else:
    print("  PH: no data returned")

print("\n=== Scraping HackerNews ===")
data = fetch_json("https://hacker-news.firebaseio.com/v0/newstories.json")
if data:
    story_ids = data[:40]
    hn_count = 0
    for sid in story_ids:
        item = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
        if item:
            title = item.get('title','')
            ai_kw = ['ai','artificial intelligence','ml','machine learning','llm','gpt','diffusion','neural','deep learning','transformer','agent','rag','automation','image gen','text to image','stable diffusion']
            if any(k in title.lower() for k in ai_kw):
                results.append({
                    'name': title[:80], 'tagline': title, 'url': item.get('url','') or f"https://news.ycombinator.com/item?id={sid}",
                    'source': 'HackerNews', 'collected_date': today
                })
                hn_count += 1
    print(f"  HN: {hn_count} relevant stories")
else:
    print("  HN: no data")

# Deduplicate
seen = set()
unique = []
for r in results:
    key = r['name'].lower().strip()
    if key not in seen:
        seen.add(key)
        unique.append(r)

print(f"\nTotal unique: {len(unique)}")
for r in unique:
    print(f"  [{r['source']}] {r['name']}")

outpath = f"{log_dir}/{today}-raw-scrape.json"
with open(outpath, 'w') as f:
    json.dump(unique, f, indent=2, ensure_ascii=False)
print(f"Saved: {outpath}")
