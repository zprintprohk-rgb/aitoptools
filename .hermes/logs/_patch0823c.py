# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
EM = '\u2014'

# 1. fix literal " + EM + " in [slug]/page.js
p = r'src\app\[slug]\page.js'
s = open(p, encoding='utf-8').read()
n = s.count('" + EM + "')
if n:
    s = s.replace('" + EM + "', EM)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('fixed', n, 'EM literals in', p)
else:
    print('no EM literals in', p)

# 2. compare page: insert More Head-to-Head before WhyTrustUs (regex anchor, ASCII)
p = r'src\app\compare\[slug]\page.js'
s = open(p, encoding='utf-8').read()
if 'More Head-to-Head Comparisons' not in s:
    m = re.search(r'\n        <WhyTrustUs />', s)
    assert m, 'WhyTrustUs anchor not found in compare'
    block = '''
        {/* W2-0823 four-layer internal links: compare -> compare/list */}
        <div className="related-links" style={{ marginTop: 40 }}>
          <h2 id="more-comparisons" style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--k-deep)' }}>More Head-to-Head Comparisons</h2>
          <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
            {comparisons.filter(c => c.slug !== comp.slug).map(c => (
              <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link></li>
            ))}
          </ul>
        </div>
'''
    s = s[:m.start()] + block + s[m.start():]
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('OK compare: More Head-to-Head inserted')
else:
    print('SKIP compare: already inserted')

# 3. best page: insert Related Comparisons & Roundups before WhyTrustUs + import comparisons
p = r'src\app\best\[slug]\page.js'
s = open(p, encoding='utf-8').read()
if "import comparisons from '@/data/comparisons.json'" not in s:
    s = s.replace("import reviews from '@/data/reviews'\n", "import reviews from '@/data/reviews'\nimport comparisons from '@/data/comparisons.json'\n")
if 'Related Comparisons' not in s:
    m = re.search(r'\n        <WhyTrustUs />', s)
    assert m, 'WhyTrustUs anchor not found in best'
    block = '''
        {/* W2-0823 four-layer internal links: list -> tool/compare (hub cross-links) */}
        {(() => {
          const names = l.items.map(it => it.name)
          const relComp = comparisons.filter(c => names.some(n => (c.toolA && c.toolA.name === n) || (c.toolB && c.toolB.name === n)))
          const otherHubs = listicles.filter(x => x.slug !== l.slug)
          return (
            <div className="related-links" style={{ marginTop: 40 }}>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--k-deep)' }}>Related Comparisons ' + EM + ' Roundups</h2>
              <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
                {relComp.map(c => (
                  <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link> ' + EM + ' head-to-head pricing, quality, and shipping comparison.</li>
                ))}
                {otherHubs.map(x => (
                  <li key={x.slug}><Link href={`/best/${x.slug}/`}>{x.title}</Link></li>
                ))}
              </ul>
            </div>
          )
        })()}
'''
    s = s[:m.start()] + block + s[m.start():]
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('OK best: Related section inserted')
else:
    print('SKIP best: already inserted')

# 4. llms.txt: +2 halloween blog links
p = r'public\llms.txt'
s = open(p, encoding='utf-8').read()
old = "## Blog (long-form guides with tested data)\n"
if 'halloween-pod-ideas-2026' not in s:
    assert s.count(old) == 1
    add = old + "- [25 Halloween POD Ideas for 2026: What Actually Sells (With Real Margins)](https://aitoptools.net/blog/halloween-pod-ideas-2026/): 25 seasonal POD product ideas with real margin math, tested catalog picks, and the free asset pool we track.\n- [Printful vs Printify for Halloween 2026: Catalog, Margins & What I Would Sell](https://aitoptools.net/blog/printful-vs-printify-halloween-2026/): Halloween catalog and margin comparison between the two biggest POD platforms.\n"
    open(p, 'w', encoding='utf-8', newline='\n').write(s.replace(old, add))
    print('OK llms.txt +2 halloween')
else:
    print('SKIP llms.txt already patched')

print('DONE')
