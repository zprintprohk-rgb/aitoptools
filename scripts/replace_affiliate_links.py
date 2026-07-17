# -*- coding: utf-8 -*-
"""Replace fake/stale affiliate URLs in src/data/reviews.json with real ones.

Reads AFFILIATE_LINKS.json (merchant domain -> real affiliate URL).
- Merchant HAS a configured real URL: every link to it (affiliateUrl field
  and any href inside content) is replaced with the real URL.
- Merchant NOT configured: cosmetic fake params (?fpr=partner) are stripped,
  leaving an honest naked link. Never fabricate tracking params.

Usage:
  python scripts/replace_affiliate_links.py          # dry-run, prints counts
  python scripts/replace_affiliate_links.py --apply  # writes reviews.json
Then: npm run build && git add -A && git commit -m "..." && git push
"""
import json, re, sys, io
from pathlib import Path
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / 'AFFILIATE_LINKS.json'
DATA = ROOT / 'src' / 'data' / 'reviews.json'
FAKE = re.compile(r'\?fpr=partner')
URL_RE = re.compile(r"https?://[^\s'\"<>]+")

def fix_url(url, links):
    host = urlparse(url).netloc.lower().replace('www.', '')
    real = links.get(host, '').strip()
    if real:
        return real, 'REPLACED'
    if FAKE.search(url):
        return url.split('?')[0], 'STRIPPED'
    return url, None

def main():
    apply = '--apply' in sys.argv
    links = {k: v for k, v in json.loads(CFG.read_text(encoding='utf-8')).items()
             if not k.startswith('_')}
    reviews = json.loads(DATA.read_text(encoding='utf-8'))
    stats = {'REPLACED': 0, 'STRIPPED': 0}

    def repl(m):
        new, tag = fix_url(m.group(0), links)
        if tag:
            stats[tag] += 1
        return new

    for r in reviews:
        for field in ('affiliateUrl', 'content'):
            if r.get(field):
                r[field] = URL_RE.sub(repl, r[field])

    print(f"REPLACED with real links: {stats['REPLACED']}")
    print(f"STRIPPED fake ?fpr=partner: {stats['STRIPPED']}")
    if apply:
        DATA.write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + '\n',
                        encoding='utf-8')
        print('reviews.json written. Next: npm run build && git add -A && git commit && git push')
    else:
        print('dry-run only. Re-run with --apply to write changes.')

if __name__ == '__main__':
    main()
