"""Build src/data/affiliates.json + src/data/tools/*.json for the programmatic SEO pipeline.

Sources (no fabrication):
- AFFILIATE_LINKS.json (root) — approved affiliate URLs
- reviews.json (src/data) — real rating/price/pros/cons for 7 tools
- docs/SEO_ARCHITECTURE.md — 9-tool pool, commission/best_for facts from M3
- picjam/greenonion: affiliate URL PENDING (no fabrication) -> pending flag, CTA skipped
"""
import json
from pathlib import Path

ROOT = Path(r'F:\aitoptools')
SRC_DATA = ROOT / 'src' / 'data'

# --- Load sources ---
aff_links = json.load(open(ROOT / 'AFFILIATE_LINKS.json', encoding='utf-8'))
reviews = json.load(open(SRC_DATA / 'reviews.json', encoding='utf-8'))
review_map = {r['slug']: r for r in reviews}

# --- 9-tool pool (M3 SEO_ARCHITECTURE.md) ---
TOOLS = {
    'printify': {
        'name': 'Printify', 'category': 'POD', 'applicationCategory': 'BusinessApplication',
        'best_for': 'Catalog size (1,300+ items) + low prices',
        'commission': '5% × 12 months', 'free_trial': 'Free to sign up', 'rating': 'A-',
    },
    'printful': {
        'name': 'Printful', 'category': 'POD', 'applicationCategory': 'BusinessApplication',
        'best_for': 'Quality, branding, embroidery depth',
        'commission': '10% × 12 months + $25 bonus', 'free_trial': 'Free to sign up', 'rating': 'A',
    },
    'gelato': {
        'name': 'Gelato', 'category': 'POD', 'applicationCategory': 'BusinessApplication',
        'best_for': 'International shipping (140+ hubs in 32 countries)',
        'commission': 'TBD (est. 15-20% sales cycle)', 'free_trial': 'Free to sign up', 'rating': 'A-',
    },
    'kittl': {
        'name': 'Kittl', 'category': 'Design', 'applicationCategory': 'DesignApplication',
        'best_for': 'Print-ready vector AI designs, SVG output',
        'commission': '20% paid subscription × 30-day referral', 'free_trial': 'Free tier available', 'rating': 'A',
    },
    'creative-fabrica': {
        'name': 'Creative Fabrica', 'category': 'Design', 'applicationCategory': 'DesignApplication',
        'best_for': 'Templates library, fonts, design assets',
        'commission': '25% + 20% subscription renewal (cycle)', 'free_trial': 'Free tier available', 'rating': 'A',
    },
    'claid': {
        'name': 'Claid', 'category': 'Photo', 'applicationCategory': 'ImageApplication',
        'best_for': 'AI product photo enhancement, background removal',
        'commission': '20% lifetime recurring, $20 minimum', 'free_trial': '50 free credits', 'rating': 'A',
    },
    'mockey': {
        'name': 'Mockey', 'category': 'Mockup', 'applicationCategory': 'DesignApplication',
        'best_for': '5,000+ free mockups, AI background remover',
        'commission': '30% recurring, 90-day cookie', 'free_trial': 'Free tier available', 'rating': 'A',
    },
    'picjam': {
        'name': 'Picjam', 'category': 'Listing', 'applicationCategory': 'BusinessApplication',
        'best_for': 'Listing Score 0-100 optimization, A+ Content',
        'commission': '[PENDING-Picjam-commission-rate]', 'free_trial': 'Free trial available', 'rating': 'A (claimed by user)',
    },
    'greenonion': {
        'name': 'GreenOnion', 'category': 'Listing', 'applicationCategory': 'BusinessApplication',
        'best_for': '60-second compliance listing generation',
        'commission': '[PENDING-GreenOnion-commission-rate]', 'free_trial': 'Free trial available', 'rating': 'A (claimed by user)',
    },
}

# --- Affiliate URL resolution (approved values only; pending = skip CTA) ---
# Priority: reviews.json affiliateUrl > AFFILIATE_LINKS.json (explicit domain keys)
URL_SOURCES = {
    'printify': ['https://try.printify.com/4fs863rfz2yc'],
    'printful': ['https://www.printful.com/a/15297661:***'],
    'gelato': ['https://try.gelato.com/upftmv48rtcl'],
    'kittl': ['https://kittl.pxf.io/qWNvPn'],
    'creative-fabrica': ['https://www.creativefabrica.com/ref/27832838/'],
    'claid': ['https://claid.ai?via=jerome94'],
    'mockey': ['https://mockey.ai?via=jerome796'],
    'picjam': [],
    'greenonion': [],
}
VISIT_URLS = {
    'printify': 'https://printify.com', 'printful': 'https://printful.com', 'gelato': 'https://gelato.com',
    'kittl': 'https://kittl.com', 'creative-fabrica': 'https://www.creativefabrica.com',
    'claid': 'https://claid.ai', 'mockey': 'https://mockey.ai',
    'picjam': 'https://picjam.ai', 'greenonion': 'https://greenonion.ai',
}

# --- Build affiliates.json (SSoT for the pipeline) ---
affiliates = {}
for slug, meta in TOOLS.items():
    aff_urls = URL_SOURCES[slug]
    pending = len(aff_urls) == 0
    affiliates[slug] = {
        'tool': slug,
        'name': meta['name'],
        'affiliate_url': aff_urls[0] if aff_urls else '',
        'visit_url': VISIT_URLS[slug],
        'pending': pending,
        'rel': 'nofollow sponsored',
        'utm_source': 'aitoptools',
        'utm_medium': 'affiliate',
        'utm_campaign': slug,
    }

# --- Build src/data/tools/{slug}.json (one JSON per tool) ---
tools_dir = SRC_DATA / 'tools'
tools_dir.mkdir(exist_ok=True)
review_slug_map = {
    'printify': 'printify-review', 'printful': 'printful-review', 'gelato': 'gelato-review',
    'kittl': 'kittl-review', 'creative-fabrica': 'creative-fabrica-review',
    'claid': 'claid-ai-review', 'mockey': 'mockey-review',
}
written = []
for slug, meta in TOOLS.items():
    rv = review_map.get(review_slug_map.get(slug, ''))
    tool = {
        'slug': slug,
        'name': meta['name'],
        'category': meta['category'],
        'applicationCategory': meta['applicationCategory'],
        'best_for': meta['best_for'],
        'commission': meta['commission'],
        'free_trial': meta['free_trial'],
        'rating_letter': meta['rating'],
        'rating': rv['rating'] if rv else None,
        'price': rv['price'] if rv else None,
        'affiliate_url': affiliates[slug]['affiliate_url'],
        'visit_url': affiliates[slug]['visit_url'],
        'affiliate_pending': affiliates[slug]['pending'],
        'pros': rv['pros'] if rv else [],
        'cons': rv['cons'] if rv else [],
        'review_slug': review_slug_map.get(slug, ''),
        'has_review': rv is not None,
    }
    (tools_dir / f'{slug}.json').write_text(
        json.dumps(tool, ensure_ascii=False, indent=2), encoding='utf-8')
    written.append(slug)

# --- Write affiliates.json ---
(SRC_DATA / 'affiliates.json').write_text(
    json.dumps(affiliates, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'affiliates.json: {len(affiliates)} tools')
print(f'src/data/tools/: {len(written)} tool files: {", ".join(written)}')
print('pending (CTA skipped, no fabricated URL):', [s for s, a in affiliates.items() if a['pending']])
