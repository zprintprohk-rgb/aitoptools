import urllib.request, json, time, os, ssl

logdir = '/mnt/f/aitoptools/.hermes/logs'
ctx = ssl.create_default_context()

# Try fetching Reddit r/artificial hot posts
try:
    url = "https://www.reddit.com/r/artificial/hot.json?limit=15"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=15, context=ctx)
    data = json.loads(resp.read())
    posts = []
    for child in data['data']['children']:
        d = child['data']
        posts.append({'title': d.get('title',''), 'url': d.get('url',''), 'score': d.get('score',0)})
    
    outpath = os.path.join(logdir, 'reddit_trends.json')
    with open(outpath, 'w') as f:
        json.dump(posts, f, indent=2)
    print(f"OK: Fetched {len(posts)} posts from Reddit r/artificial")
except Exception as e:
    print(f"Reddit fetch failed: {e}")
    # Try alternative: r/MachineLearning
    try:
        url = "https://www.reddit.com/r/MachineLearning/hot.json?limit=15"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=15, context=ctx)
        data = json.loads(resp.read())
        posts = []
        for child in data['data']['children']:
            d = child['data']
            posts.append({'title': d.get('title',''), 'url': d.get('url',''), 'score': d.get('score',0)})
        
        outpath = os.path.join(logdir, 'reddit_trends.json')
        with open(outpath, 'w') as f:
            json.dump(posts, f, indent=2)
        print(f"OK: Fetched {len(posts)} posts from Reddit r/MachineLearning")
    except Exception as e2:
        print(f"Reddit alternate failed: {e2}")
