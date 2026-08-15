# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
EM = '\u2014'  # em dash
MID = '\u00b7' # middle dot

def patch(path, old, new):
    s = open(path, encoding='utf-8').read()
    if new in s:
        print('SKIP', path, '-> already applied')
        return
    n = s.count(old)
    assert n == 1, f"{path}: expected 1 match, got {n} for: {old[:60]!r}"
    open(path, 'w', encoding='utf-8', newline='\n').write(s.replace(old, new))
    print('OK', path)

# ============ 1. reviews [slug]/page.js ============
p = r'src\app\[slug]\page.js'
patch(p, "import reviews from '@/data/reviews'\n",
      "import reviews from '@/data/reviews'\nimport comparisons from '@/data/comparisons.json'\n")

patch(p, """      author: { '@type': 'Organization', name: 'Print AI Tools' },
      datePublished: review.datePublished || '2026-06-25',""",
"""      author: { '@type': 'Person', name: 'Jerome Tang', jobTitle: 'Print Industry Expert', worksFor: { '@type': 'Organization', name: 'Shenzhen Cai Long Printing', address: { '@type': 'PostalAddress', addressLocality: 'Shenzhen', addressCountry: 'CN' } } },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },
      datePublished: review.datePublished || '2026-06-25',""")

# byline: regex replace the whole byline <p> block (handles dash/middot variants)
s = open(p, encoding='utf-8').read()
if 'How we tested:' not in s:
    m = re.search(r'<p className="byline"[^>]*>\s*By <strong>Jerome Tang</strong>.*?</p>', s, re.S)
    assert m, 'byline block not found'
    byline = m.group(0)
    new_byline = byline + "\n        <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', margin: '4px 0 0' }}>\n          <strong>How we tested:</strong> Tested by Jerome Tang, Shenzhen Cai Long Printing " + EM + " hands-on account testing, live pricing verification, and real print-order checks. See our <Link href=\"/methodology/\">full testing methodology</Link>.\n        </p>"
    s = s.replace(byline, new_byline)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    print('OK', p, 'byline+methodology')
else:
    print('SKIP', p, 'byline already patched')

patch(p, """function getCategoryDisplay(review) {""",
"""const HUB_ROUNDUPS = [
  { cats: ['ai-print-design'], href: '/best/best-ai-tshirt-design-generators/', label: 'Best AI T-Shirt Design Generators (2026)', desc: 'our ranked roundup of 7 design tools for print-on-demand sellers' },
  { cats: ['ai-ecommerce'], href: '/best/printful-alternatives/', label: 'Best Printful Alternatives (2026)', desc: 'cheaper and faster POD platform options, ranked' },
  { cats: ['ai-writing'], href: '/best-ai-writing-tools-comparison/', label: 'Best AI Writing Tools Comparison', desc: 'Jasper vs Writesonic vs Copy.ai vs Rytr vs ChatGPT, side by side' },
  { cats: ['ai-image'], href: '/best-ai-background-removers-2026/', label: 'Best AI Background Removers for POD', desc: '7 tools tested on real print mockups' },
  { cats: ['ai-video', 'ai-voice'], href: '/category/ai-video/', label: 'AI Video & Voice category', desc: 'every video and voice tool review in one place' },
]
const POD_ROUNDUPS = [
  { slug: 'printful-review', href: '/best/printful-alternatives/', label: 'Best Printful Alternatives (2026)', desc: 'cheaper and faster POD platform options, ranked' },
  { slug: 'printify-review', href: '/best/printify-alternatives/', label: 'Best Printify Alternatives (2026)', desc: 'top picks after the Premium price hike' },
  { slug: 'gelato-review', href: '/best/best-print-on-demand-companies/', label: 'Best Print-on-Demand Companies (2026)', desc: '8 POD platforms compared for Etsy and Shopify sellers' },
]
function getHubLinks(review) {
  const pod = POD_ROUNDUPS.find(p => p.slug === review.slug)
  if (pod) return [pod]
  return HUB_ROUNDUPS.filter(h => h.cats.includes(review.categorySlug)).map(h => ({ href: h.href, label: h.label, desc: h.desc }))
}

function getCategoryDisplay(review) {""")

patch(p, """        {/* Similar tools */}
        <div className="section-header" style={{ marginTop: 36 }}>""",
"""        {/* W2-0823 four-layer internal links: tool -> compare -> list (hub cross-links) */}
        {(() => {
          const relatedComp = comparisons.filter(c => (c.toolA && c.toolA.reviewSlug === review.slug) || (c.toolB && c.toolB.reviewSlug === review.slug))
          const hubs = getHubLinks(review)
          if (!relatedComp.length && !hubs.length) return null
          return (
            <div className="related-links" style={{ marginTop: 36 }}>
              <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>Deeper Reads: Comparisons &amp; Roundups</h2>
              <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
                {relatedComp.map(c => (
                  <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link> " + EM + " side-by-side pricing, catalog, and print-quality notes.</li>
                ))}
                {hubs.map(h => (
                  <li key={h.href}><Link href={h.href}>{h.label}</Link> " + EM + " {h.desc}.</li>
                ))}
              </ul>
            </div>
          )
        })()}

        {/* Similar tools */}
        <div className="section-header" style={{ marginTop: 36 }}>""")

# ============ 2. compare/[slug]/page.js ============
p = r'src\app\compare\[slug]\page.js'
patch(p, """      author: { '@type': 'Organization', name: 'Print AI Tools' },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },""",
"""      author: { '@type': 'Person', name: 'Jerome Tang', jobTitle: 'Print Industry Expert', worksFor: { '@type': 'Organization', name: 'Shenzhen Cai Long Printing' } },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },""")

patch(p, """        {/* Why trust us ? shared editorial module */}
        <WhyTrustUs />""",
"""        {/* W2-0823 four-layer internal links: compare -> compare/list */}
        <div className="related-links" style={{ marginTop: 40 }}>
          <h2 id="more-comparisons" style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--k-deep)' }}>More Head-to-Head Comparisons</h2>
          <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
            {comparisons.filter(c => c.slug !== comp.slug).map(c => (
              <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link></li>
            ))}
          </ul>
        </div>

        {/* Why trust us ? shared editorial module */}
        <WhyTrustUs />""")

# ============ 3. best/[slug]/page.js ============
p = r'src\app\best\[slug]\page.js'
patch(p, "import reviews from '@/data/reviews'\n",
      "import reviews from '@/data/reviews'\nimport comparisons from '@/data/comparisons.json'\n")
patch(p, """      author: { '@type': 'Organization', name: 'Print AI Tools' },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },""",
"""      author: { '@type': 'Person', name: 'Jerome Tang', jobTitle: 'Print Industry Expert', worksFor: { '@type': 'Organization', name: 'Shenzhen Cai Long Printing' } },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },""")

patch(p, """        {/* Why trust us ? shared editorial module */}
        <WhyTrustUs />""",
"""        {/* W2-0823 four-layer internal links: list -> tool/compare (hub cross-links) */}
        {(() => {
          const names = l.items.map(it => it.name)
          const relComp = comparisons.filter(c => names.some(n => (c.toolA && c.toolA.name === n) || (c.toolB && c.toolB.name === n)))
          const otherHubs = listicles.filter(x => x.slug !== l.slug)
          return (
            <div className="related-links" style={{ marginTop: 40 }}>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--k-deep)' }}>Related Comparisons &amp; Roundups</h2>
              <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
                {relComp.map(c => (
                  <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link> " + EM + " head-to-head pricing, quality, and shipping comparison.</li>
                ))}
                {otherHubs.map(x => (
                  <li key={x.slug}><Link href={`/best/${x.slug}/`}>{x.title}</Link></li>
                ))}
              </ul>
            </div>
          )
        })()}

        {/* Why trust us ? shared editorial module */}
        <WhyTrustUs />""")

# ============ 4. llms.txt: +2 halloween blog links (8/18 PARTIAL gap P2-5) ============
p = r'public\llms.txt'
s = open(p, encoding='utf-8').read()
old = "## Blog (long-form guides with tested data)\n"
if 'halloween-pod-ideas-2026' not in s:
    assert s.count(old) == 1
    add = old + "- [25 Halloween POD Ideas for 2026: What Actually Sells (With Real Margins)](https://aitoptools.net/blog/halloween-pod-ideas-2026/): 25 seasonal POD product ideas with real margin math, tested catalog picks, and the free asset pool we track.\n- [Printful vs Printify for Halloween 2026: Catalog, Margins & What I Would Sell](https://aitoptools.net/blog/printful-vs-printify-halloween-2026/): Halloween catalog and margin comparison between the two biggest POD platforms.\n"
    open(p, 'w', encoding='utf-8', newline='\n').write(s.replace(old, add))
    print('OK llms.txt +2 halloween')
else:
    print('SKIP llms.txt already has halloween')

print('ALL PATCHES APPLIED')
