import json

# ---------- comparisons.json: picks / features / pricing ----------
comp_adds = {
  'printful-vs-printify': {
    'picks': [
      {'type': 'top', 'name': 'Printify', 'tagline': 'Best margins and largest catalog for most sellers', 'rating': 4.3, 'anchor': '#at-a-glance'},
      {'type': 'also', 'name': 'Printful', 'tagline': 'Premium print quality and branding options', 'rating': 4.5, 'anchor': '#full-reviews'},
      {'type': 'budget', 'name': 'Printify Free plan', 'tagline': 'Zero monthly cost — pay per order only', 'rating': 4.3, 'anchor': '#pricing'},
    ],
    'features': [
      {'feature': 'Free plan with no monthly fee', 'a': 'yes', 'b': 'yes'},
      {'feature': 'In-house production facilities', 'a': 'yes', 'b': 'no'},
      {'feature': '1,000+ product catalog', 'a': 'no', 'b': 'yes'},
      {'feature': 'Custom labels & pack-ins', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Print quality consistency controls', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Membership discounts (paid plan)', 'a': 'yes', 'b': 'yes'},
      {'feature': 'Marketplace & store integrations', 'a': 'yes', 'b': 'yes'},
    ],
    'pricing': {
      'betterValue': 'b',
      'rows': [
        {'label': 'Free plan', 'a': '$0 — full platform access', 'b': '$0 — full platform access'},
        {'label': 'Paid plan', 'a': 'Growth $24.99/mo (free after $12K/yr in sales)', 'b': 'Premium $39/mo or $24.99/mo billed yearly'},
        {'label': 'Product discount', 'a': 'Up to 33% off products', 'b': 'Up to 20% off products'},
      ],
    },
  },
  'printify-vs-gelato': {
    'picks': [
      {'type': 'top', 'name': 'Printify', 'tagline': 'Largest catalog, deepest discounts, provider control', 'rating': 4.3, 'anchor': '#at-a-glance'},
      {'type': 'also', 'name': 'Gelato', 'tagline': 'Local production in 32 countries for international sales', 'rating': 4.4, 'anchor': '#full-reviews'},
      {'type': 'budget', 'name': 'Printify Free plan', 'tagline': 'Zero monthly cost — pay per order only', 'rating': 4.3, 'anchor': '#pricing'},
    ],
    'features': [
      {'feature': 'Free plan with no monthly fee', 'a': 'yes', 'b': 'yes'},
      {'feature': '1,000+ product catalog', 'a': 'yes', 'b': 'no'},
      {'feature': 'Choice of print providers', 'a': 'yes', 'b': 'no'},
      {'feature': 'Local production in 30+ countries', 'a': 'no', 'b': 'yes'},
      {'feature': 'Membership discounts (paid plan)', 'a': 'yes', 'b': 'yes'},
      {'feature': 'Custom branding (labels, pack-ins)', 'a': 'partial', 'b': 'partial'},
      {'feature': 'Fast EU delivery options', 'a': 'partial', 'b': 'yes'},
    ],
    'pricing': {
      'betterValue': 'b',
      'rows': [
        {'label': 'Free plan', 'a': '$0 — full platform access', 'b': '$0 — full platform access'},
        {'label': 'Paid plan', 'a': 'Premium $39/mo or $24.99/mo billed yearly', 'b': 'Gelato+ $23.99/mo or $19.99/mo billed yearly'},
        {'label': 'Product discount', 'a': 'Up to 33% off products', 'b': 'Up to 25% off products'},
      ],
    },
  },
  'printful-vs-gelato': {
    'picks': [
      {'type': 'top', 'name': 'Printful', 'tagline': 'Premium branding and print consistency for serious brands', 'rating': 4.5, 'anchor': '#at-a-glance'},
      {'type': 'also', 'name': 'Gelato', 'tagline': 'Lower base costs and global local production', 'rating': 4.4, 'anchor': '#full-reviews'},
      {'type': 'budget', 'name': 'Gelato Free plan', 'tagline': 'Free plan with lower base product costs', 'rating': 4.4, 'anchor': '#pricing'},
    ],
    'features': [
      {'feature': 'Free plan with no monthly fee', 'a': 'yes', 'b': 'yes'},
      {'feature': 'In-house production facilities', 'a': 'yes', 'b': 'no'},
      {'feature': 'Custom labels & pack-ins', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Local production in 30+ countries', 'a': 'partial', 'b': 'yes'},
      {'feature': 'Embroidery options', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Lower base product costs', 'a': 'no', 'b': 'yes'},
      {'feature': 'Membership discounts (paid plan)', 'a': 'yes', 'b': 'yes'},
    ],
    'pricing': {
      'betterValue': 'b',
      'rows': [
        {'label': 'Free plan', 'a': '$0 — full platform access', 'b': '$0 — full platform access'},
        {'label': 'Paid plan', 'a': 'Growth $24.99/mo (free after $12K/yr in sales)', 'b': 'Gelato+ $23.99/mo or $19.99/mo billed yearly'},
        {'label': 'Base product costs', 'a': '15–35% higher', 'b': 'Lower'},
      ],
    },
  },
  'kittl-vs-placeit': {
    'picks': [
      {'type': 'top', 'name': 'Kittl', 'tagline': 'Design creation: typography, vectors, AI generation', 'rating': 4.5, 'anchor': '#at-a-glance'},
      {'type': 'also', 'name': 'Placeit', 'tagline': '40,000+ mockups for product presentation', 'rating': 4.0, 'anchor': '#full-reviews'},
      {'type': 'budget', 'name': 'Placeit Annual', 'tagline': '~$7.47/mo billed annually — unlimited downloads', 'rating': 4.0, 'anchor': '#pricing'},
    ],
    'features': [
      {'feature': 'Free plan', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Vector design editing', 'a': 'yes', 'b': 'no'},
      {'feature': 'Advanced typography effects', 'a': 'yes', 'b': 'no'},
      {'feature': 'AI design generation', 'a': 'yes', 'b': 'partial'},
      {'feature': 'Apparel mockup library (10,000+)', 'a': 'no', 'b': 'yes'},
      {'feature': 'Video mockups', 'a': 'no', 'b': 'yes'},
      {'feature': 'Print-ready file export', 'a': 'yes', 'b': 'partial'},
    ],
    'pricing': {
      'betterValue': 'b',
      'rows': [
        {'label': 'Free tier', 'a': 'Yes — personal use only', 'b': 'No full free plan (free assets available)'},
        {'label': 'Entry paid plan', 'a': 'Pro $15/mo or $120/yr', 'b': '$14.95/mo or ~$7.47/mo billed annually'},
        {'label': 'Top tier', 'a': 'Expert $30/mo or $288/yr', 'b': 'Same plan — everything included'},
      ],
    },
  },
  'kittl-vs-canva': {
    'picks': [
      {'type': 'top', 'name': 'Kittl', 'tagline': 'Purpose-built for merch: typography, vectors, print-ready exports', 'rating': 4.5, 'anchor': '#at-a-glance'},
      {'type': 'also', 'name': 'Canva', 'tagline': 'General-purpose design and marketing content', 'rating': 4.5, 'anchor': '#full-reviews'},
      {'type': 'budget', 'name': 'Canva Free', 'tagline': 'Genuinely usable free tier for most commercial work', 'rating': 4.5, 'anchor': '#pricing'},
    ],
    'features': [
      {'feature': 'Free plan (commercial use)', 'a': 'no', 'b': 'yes'},
      {'feature': 'Vector editing', 'a': 'yes', 'b': 'no'},
      {'feature': 'Advanced typography effects', 'a': 'yes', 'b': 'partial'},
      {'feature': 'AI image generation', 'a': 'yes', 'b': 'yes'},
      {'feature': 'AI raster-to-vector conversion', 'a': 'yes', 'b': 'no'},
      {'feature': 'Team collaboration & brand controls', 'a': 'partial', 'b': 'yes'},
      {'feature': 'Print-ready POD export presets', 'a': 'yes', 'b': 'no'},
      {'feature': 'Presentation & document formats', 'a': 'no', 'b': 'yes'},
    ],
    'pricing': {
      'betterValue': 'b',
      'rows': [
        {'label': 'Free tier', 'a': '$0 — personal use only', 'b': '$0 — most commercial use OK'},
        {'label': 'Paid plan', 'a': 'Pro $15/mo or $120/yr', 'b': 'Pro $15/mo or $120/yr'},
        {'label': 'Higher tier', 'a': 'Expert $30/mo or $288/yr', 'b': 'Business $20/user/mo ($10 annual)'},
      ],
    },
  },
}

p = 'F:/aitoptools/src/data/comparisons.json'
d = json.load(open(p, encoding='utf-8'))
for c in d:
    c.update(comp_adds[c['slug']])
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('comparisons updated:', [c['slug'] for c in d])

# ---------- listicles.json: pickType + features ----------
list_adds = {
  'printful-alternatives': {
    'pickTypes': {'Printify': 'top', 'Gelato': 'also', 'CustomCat': 'budget'},
    'featureCols': ['Printify', 'Gelato', 'CustomCat'],
    'features': [
      {'feature': 'Free plan', 'values': ['yes', 'yes', 'yes']},
      {'feature': '1,000+ product catalog', 'values': ['yes', 'no', 'no']},
      {'feature': 'Local production network', 'values': ['partial', 'yes', 'partial']},
      {'feature': 'Custom branding options', 'values': ['partial', 'partial', 'no']},
      {'feature': 'Volume / membership discounts', 'values': ['yes', 'yes', 'partial']},
      {'feature': 'US production speed', 'values': ['partial', 'partial', 'yes']},
    ],
  },
  'printify-alternatives': {
    'pickTypes': {'Printful': 'top', 'Gelato': 'also', 'Teelaunch': 'budget'},
    'featureCols': ['Printful', 'Gelato', 'CustomCat'],
    'features': [
      {'feature': 'Free plan', 'values': ['yes', 'yes', 'yes']},
      {'feature': 'In-house production facilities', 'values': ['yes', 'no', 'yes']},
      {'feature': 'Local production in 30+ countries', 'values': ['partial', 'yes', 'no']},
      {'feature': 'Custom labels & pack-ins', 'values': ['yes', 'partial', 'no']},
      {'feature': 'Embroidery options', 'values': ['yes', 'partial', 'no']},
      {'feature': 'Paid plan optional (not required)', 'values': ['yes', 'yes', 'yes']},
    ],
  },
}

lp = 'F:/aitoptools/src/data/listicles.json'
ld = json.load(open(lp, encoding='utf-8'))
for x in ld:
    add = list_adds[x['slug']]
    for it in x['items']:
        if it['name'] in add['pickTypes']:
            it['pickType'] = add['pickTypes'][it['name']]
    x['featureCols'] = add['featureCols']
    x['features'] = add['features']
json.dump(ld, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('listicles updated:', [(x['slug'], [ (i['name'], i.get('pickType')) for i in x['items'] if i.get('pickType')]) for x in ld])

# 落盘后立刻校验 — 数据不合格不允许构建 (与 CI/本地共用同一脚本)
import os, subprocess, sys as _sys
r = subprocess.run([_sys.executable, os.path.join(os.path.dirname(__file__), 'validate_content_data.py')], capture_output=True, text=True)
print(r.stdout)
if r.returncode != 0:
    print(r.stderr, file=_sys.stderr)
    raise SystemExit(r.returncode)
