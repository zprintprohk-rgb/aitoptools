import { notFound } from 'next/navigation'
import Link from 'next/link'
import comparisons from '@/data/comparisons.json'
import reviews from '@/data/reviews'
import RatingBar from '@/components/RatingBar'
import PicksCards from '@/components/PicksCards'
import WhyTrustUs from '@/components/WhyTrustUs'
import FeatureMatrix from '@/components/FeatureMatrix'
import PricingTable from '@/components/PricingTable'
import { buildAffLinkAttrs } from '@/lib/affiliate'

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export function generateStaticParams() {
  return comparisons.map(c => ({ slug: c.slug }))
}

export function generateMetadata({ params }) {
  const comp = comparisons.find(c => c.slug === params.slug)
  if (!comp) return { title: 'Not Found' }
  return {
    title: comp.title,
    description: comp.metaDesc,
    alternates: {
      canonical: `https://aitoptools.net/compare/${params.slug}/`,
    },
    openGraph: {
      title: comp.title,
      description: comp.metaDesc,
      url: `https://aitoptools.net/compare/${params.slug}/`,
      type: 'article',
    },
    twitter: {
      card: 'summary_large_image',
      title: comp.title,
      description: comp.metaDesc,
    },
  }
}

function winnerClass(winner, side) {
  if (winner === 'Tie') return 'compare-cell tie'
  return winner.toLowerCase() === side ? 'compare-cell win' : 'compare-cell'
}

function generateJsonLd(comp) {
  const schemas = [
    {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: comp.title,
      description: comp.metaDesc,
      author: { '@type': 'Organization', name: 'Print AI Tools' },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },
      datePublished: comp.datePublished,
      dateModified: comp.dateModified || comp.datePublished,
      mainEntityOfPage: `https://aitoptools.net/compare/${comp.slug}/`,
    },
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
        { '@type': 'ListItem', position: 2, name: 'Comparisons', item: `https://aitoptools.net/compare/${comp.slug}/` },
        { '@type': 'ListItem', position: 3, name: comp.title, item: `https://aitoptools.net/compare/${comp.slug}/` },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: comp.faqs.map(f => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    },
  ]
  return schemas.map(s => JSON.stringify(s))
}

export default function ComparisonPage({ params }) {
  const comp = comparisons.find(c => c.slug === params.slug)
  if (!comp) notFound()

  const { toolA, toolB } = comp
  const reviewA = reviews.find(r => r.slug === toolA.reviewSlug)
  const reviewB = reviews.find(r => r.slug === toolB.reviewSlug)
  const jsonLd = generateJsonLd(comp)

  return (
    <>
      {jsonLd.map((s, i) => (
        <script key={i} type="application/ld+json" dangerouslySetInnerHTML={{ __html: s }} />
      ))}

      <div className="review-page container">
        {/* Breadcrumb */}
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <span>Comparisons</span>
          <span className="sep">›</span>
          <span className="current">{toolA.name} vs {toolB.name}</span>
        </nav>

        <h1>{comp.title}</h1>
        <div className="meta-bar">
          <span className="card-cat">POD Platform Comparison</span>
          <span className="meta-rating">{toolA.name} <RatingBar rating={toolA.rating} /></span>
          <span className="meta-rating">{toolB.name} <RatingBar rating={toolB.rating} /></span>
          <span className="card-badge tested" style={{ display: 'inline-flex', alignItems: 'center', gap: 4, background: 'var(--c-bg)', color: 'var(--c-text)', fontSize: '0.68rem', fontWeight: 600, padding: '2px 8px', borderRadius: '100px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>✓ 2026 Data Verified</span>
        </div>
        {/* 8/6 信任三件套: 作者署名 (人格背书) */}
        <p className="byline" style={{ fontSize: '0.85rem', color: 'var(--k-secondary)', margin: '6px 0 0' }}>
          By <strong>Jerome Tang</strong> — Print industry expert · hands-on tested on real print jobs
        </p>

        {/* The Verdict — 8/6 信任三件套: 结论前置三行框 (谁赢/赢在哪/适合谁) */}
        <div className="verdict-box">
          <h2 style={{ fontSize: '1.15rem', fontWeight: 700, marginBottom: 8, color: 'var(--k-deep)' }}>⚡ The Verdict</h2>
          {(() => {
            const top = comp.picks?.find(p => p.type === 'top')
            const also = comp.picks?.find(p => p.type === 'also')
            if (!top) return <p>{comp.quickVerdict}</p>
            return (
              <div className="verdict-3line">
                <p><strong className="verdict-winner">🏆 Winner: {top.name}</strong> — {top.tagline}</p>
                {also && <p><strong>Also great: </strong>{also.name} — {also.tagline}</p>}
                <p><strong>Best for: </strong>{comp.quickVerdict}</p>
              </div>
            )
          })()}
          <div className="verdict-ctas">
            {(() => {
              // W1-T1 度量埋点: aff-link class + data-merchant + data-link-id + UTM
              const affA = buildAffLinkAttrs(toolA, 'verdict-cta-a')
              return affA ? (
                <a
                  href={affA.href}
                  className={`${affA.className} cta-button`}
                  data-merchant={affA['data-merchant']}
                  data-link-id={affA['data-link-id']}
                  data-target={affA['data-target']}
                  target="_blank"
                  rel="nofollow sponsored"
                >
                  Try {toolA.name} Free →
                </a>
              ) : (
                <a href={toolA.visitUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
                  Try {toolA.name} Free →
                </a>
              )
            })()}
            {(() => {
              const affB = buildAffLinkAttrs(toolB, 'verdict-cta-b')
              return affB ? (
                <a
                  href={affB.href}
                  className={`${affB.className} cta-button cta-secondary`}
                  data-merchant={affB['data-merchant']}
                  data-link-id={affB['data-link-id']}
                  data-target={affB['data-target']}
                  target="_blank"
                  rel="nofollow sponsored"
                >
                  Try {toolB.name} Free →
                </a>
              ) : (
                <a href={toolB.visitUrl} target="_blank" rel="nofollow sponsored" className="cta-button cta-secondary">
                  Try {toolB.name} Free →
                </a>
              )
            })()}
          </div>
          {/* T11 Boost (8/12): relatedLinks 渲染 — 指向 /best/printful-alternatives/ 与 /best/printify-alternatives/ */}
          {comp.relatedLinks && (
            <div style={{ marginTop: 14, fontSize: '0.95rem', lineHeight: 1.7, color: 'var(--k-deep)' }}>
              <span dangerouslySetInnerHTML={{ __html: comp.relatedLinks }} />
            </div>
          )}
          {/* K3 7/28 护栏对齐 (与详情页 [slug]/page.js L150-152 一致): verdict-ctas 旁加 organic Visit Official 出口, 不加 aff-link 标 + 不加 UTM + rel="nofollow", 让用户能直接去官网, 避免全 CTA 都是 affiliate 强行压转化 */}
          <p style={{ marginTop: 10, fontSize: '0.85rem', color: 'var(--k-tertiary)', textAlign: 'center' }}>
            Just looking?{' '}
            <a href={toolA.visitUrl} target="_blank" rel="nofollow" style={{ color: 'var(--c-primary)', fontWeight: 500 }}>
              Visit {toolA.name} official ↗
            </a>
            {' · '}
            <a href={toolB.visitUrl} target="_blank" rel="nofollow" style={{ color: 'var(--c-primary)', fontWeight: 500 }}>
              Visit {toolB.name} official ↗
            </a>
          </p>
        </div>

        {/* Wirecutter-style three-tier picks */}
        <PicksCards picks={comp.picks} />

        {/* Side-by-side comparison table */}
        <h2 id="at-a-glance" style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>{toolA.name} vs {toolB.name} at a Glance</h2>
        <div className="review-content compare-table-wrap">
          <table className="compare-table">
            <thead>
              <tr>
                <th></th>
                <th>{toolA.name}</th>
                <th>{toolB.name}</th>
              </tr>
            </thead>
            <tbody>
              {comp.comparisonTable.map((row, i) => (
                <tr key={i}>
                  <th scope="row">{row.dimension}</th>
                  <td className={winnerClass(row.winner, 'a')}>{row.a}{row.winner === toolA.name ? ' ✓' : ''}</td>
                  <td className={winnerClass(row.winner, 'b')}>{row.b}{row.winner === toolB.name ? ' ✓' : ''}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Feature matrix */}
        {comp.features?.length > 0 && (
          <>
            <h2 style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>Feature by Feature</h2>
            <FeatureMatrix features={comp.features} names={[toolA.name, toolB.name]} />
          </>
        )}

        {/* Pricing table with better-value highlight */}
        {comp.pricing?.rows?.length > 0 && (
          <>
            <h2 id="pricing" style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>Pricing Compared</h2>
            <PricingTable pricing={comp.pricing} nameA={toolA.name} nameB={toolB.name} />
          </>
        )}

        {/* Main content */}
        <div className="review-content" dangerouslySetInnerHTML={{ __html: comp.content }} />

        {/* Related single reviews */}
        <div className="section-header" style={{ marginTop: 40 }}>
          <h2 id="full-reviews" style={{ fontSize: '1.75rem', fontWeight: 700, color: 'var(--k-deep)' }}>Read the Full Reviews</h2>
        </div>
        <div className="review-grid" style={{ gridTemplateColumns: 'repeat(2, 1fr)' }}>
          {[reviewA, reviewB].filter(Boolean).map(r => (
            <article key={r.slug} className="review-card">
              <div className="card-badges"><span className="card-badge tested">Hands-on Tested</span></div>
              <div className="card-meta">
                <span className="card-cat">{r.category}</span>
                <span className="card-rating">{starRating(r.rating)} {r.rating}</span>
              </div>
              <h3><Link href={`/${r.slug}/`}>{r.title}</Link></h3>
              <p className="card-desc">{r.metaDesc}</p>
              <Link href={`/${r.slug}/`} className="card-cta">Read Review →</Link>
            </article>
          ))}
        </div>

        {/* Why trust us — shared editorial module */}
        <WhyTrustUs />

        {/* FAQ */}
        <div className="faq-section">
          <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 16, color: 'var(--k-deep)' }}>Frequently Asked Questions</h2>
          {comp.faqs.map((faq, i) => (
            <details key={i} className="faq-item">
              <summary className="faq-question">{faq.q}</summary>
              <div className="faq-answer"><p>{faq.a}</p></div>
            </details>
          ))}
        </div>

        {/* Dual CTA */}
        <div className="cta-box">
          <p>Ready to start your POD store?</p>
          <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginBottom: 12 }}>
            Both platforms are free to start — you only pay when an order comes in. If you sign up through our links, we may earn a commission at no extra cost to you.
          </p>
          <div className="verdict-ctas" style={{ justifyContent: 'center' }}>
            <a href={toolA.affiliateUrl || toolA.visitUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
              Try {toolA.name} Free →
            </a>
            <a href={toolB.affiliateUrl || toolB.visitUrl} target="_blank" rel="nofollow sponsored" className="cta-button cta-secondary">
              Try {toolB.name} Free →
            </a>
          </div>
        </div>

        {/* Affiliate Disclosure */}
        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. All comparisons are based on honest, independent research by print industry professionals. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
