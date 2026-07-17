# -*- coding: utf-8 -*-
"""Audit outbound merchant links in out/ for affiliate tracking coverage."""
import re, sys, io
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(r"F:\aitoptools\out")

MERCHANTS = {
    'photoroom.com': 'Photoroom', 'claid.ai': 'Claid', 'kittl.com': 'Kittl',
    'placeit.net': 'Placeit', 'envato.com': 'Envato/Placeit', 'printful.com': 'Printful',
    'printify.com': 'Printify', 'gelato.com': 'Gelato', 'creativefabrica.com': 'CreativeFabrica',
    'canva.com': 'Canva', 'shopify.com': 'Shopify', 'looka.com': 'Looka',
    'vistacreate.com': 'VistaCreate', 'create.vista.com': 'VistaCreate', 'vista.com': 'VistaCreate',
    'nordpass.com': 'NordPass', 'nordvpn.com': 'NordVPN',
}

AFF_PARAMS = {'fpr','ref','aff','aff_id','affid','partner','via','tap_a','irclickid','cjevent',
              'clickid','subid','pid','offer','promo','coupon','invite','referral','deal',
              'discount','affiliate','ref_','irgwc','utm_medium'}
NETWORK_HINTS = ('awin','partnerstack','impact.','firstpromoter','shareasale','flexoffers',
                 'tapfiliate','refersion','rewardful','tolt.io','growsumo','anrdoezrs',
                 'dpbolvw','jdoqocy','tkqlhce','linksynergy')

SKIP_HOSTS = ('aitoptools.net','schema.org','google.','gstatic','w3.org','github.com',
              'wikipedia','creativecommons','fonts.','cloudflare','facebook.com','twitter.com',
              'x.com','linkedin.com','youtube.com','instagram.com','reddit.com','pinterest',
              'medium.com','producthunt.com','trustpilot.com','g2.com','capterra')

link_re = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"[^>]*>', re.S | re.I)

def merchant_of(host):
    for k, v in MERCHANTS.items():
        if host == k or host.endswith('.' + k):
            return v
    return None

per_merchant = defaultdict(lambda: {'pages': set(), 'links': 0, 'tracked': 0,
                                    'untracked_pages': set(), 'samples': []})
other_links = []
total_pages = 0

for p in sorted(ROOT.rglob('*.html')):
    rel = str(p.relative_to(ROOT).parent)
    if rel == '.':
        rel = '(home)'
    html = p.read_text(encoding='utf-8', errors='ignore')
    total_pages += 1
    for m in link_re.finditer(html):
        url = m.group(1)
        parsed = urlparse(url)
        host = parsed.netloc.lower().replace('www.', '')
        if any(s in host for s in SKIP_HOSTS):
            continue
        mer = merchant_of(host)
        qs = set(parse_qs(parsed.query))
        tracked = bool(AFF_PARAMS & qs) or any(n in url.lower() for n in NETWORK_HINTS)
        if mer:
            d = per_merchant[mer]
            d['links'] += 1
            d['pages'].add(rel)
            if tracked:
                d['tracked'] += 1
            else:
                d['untracked_pages'].add(rel)
                if len(d['samples']) < 2:
                    d['samples'].append((rel, url))
        else:
            other_links.append((rel, host, url, tracked))

print(f"total html pages scanned: {total_pages}\n")
print("=== MERCHANT SUMMARY (links / pages / tracked) ===")
for mer, d in sorted(per_merchant.items(), key=lambda x: -x[1]['links']):
    pct = round(100 * d['tracked'] / d['links']) if d['links'] else 0
    print(f"{mer}: {d['links']} links on {len(d['pages'])} pages | tracked {d['tracked']} ({pct}%) | pages w/o tracking: {len(d['untracked_pages'])}")
    for s in d['samples']:
        print(f"    untracked sample: {s[0]} -> {s[1]}")
print("\n=== OTHER OUTBOUND (not in merchant map) ===")
seen = set()
for rel, host, url, tracked in other_links:
    key = (rel, host)
    if key in seen:
        continue
    seen.add(key)
    print(f"{'T' if tracked else '-'} {rel} -> {host}  {url[:110]}")
print(f"\nother unique (page,host): {len(seen)}")
