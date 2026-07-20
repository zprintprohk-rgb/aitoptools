import { notFound } from 'next/navigation'
import Link from 'next/link'
import listicles from '@/data/listicles.json'
import reviews from '@/data/reviews'
import RatingBar from '@/components/RatingBar'
import PicksCards from '@/components/PicksCards'
import WhyTrustUs from '@/components/WhyTrustUs'
import FeatureMatrix from '@/components/FeatureMatrix'

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export function generateStaticParams() {
  return listicles.map(l => ({ slug: l.slug }))
}

export function generateMetadata({ params }) {
  const l = listicles.find(x => x.slug === params.slug)
  if (!l) return { title: 'Not Found' }
  return {
    title: l.title,
    description: l.metaDesc,
    alternates: { canonical: `https://aitoptools.net/best/${params.slug}/` },
    openGraph: {
      title: l.title,
      description: l.metaDesc,
      url: `https://aitoptools.net/best/${params.slug}/`,
      type: 'article',
    },
    twitter: { card: 'summary_large_image', title: l.title, description: l.metaDesc },
  }
}

function generateJsonLd(l) {
  const schemas = [
    {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: l.title,
      description: l.metaDesc,
      author: { '@type': 'Organization', name: 'Print AI Tools' },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },
      datePublished: l.datePublished,
      dateModified: l.dateModified || l.datePublished,
      mainEntityOfPage: `https://aitoptools.net/best/${l.slug}/`,
    },
    {
      '@context': 'https://schema.org',
      '@type': 'ItemList',
      name: l.title,
      numberOfItems: l.items.length,
      itemListElement: l.items.map((it, i) => ({
        '@type': 'ListItem',
        position: i + 1,
        name: it.name,
        description: it.tagline,
      })),
    },
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
        { '@type': 'ListItem', position: 2, name: 'Best Of', item: `https://aitoptools.net/best/${l.slug}/` },
        { '@type': 'ListItem', position: 3, name: l.title, item: `https://aitoptools.net/best/${l.slug}/` },
      ],
    },
    {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: l.faqs.map(f => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    },
  ]
  return schemas.map(s => JSON.stringify(s))
}

export default function ListiclePage({ params }) {
  const l = listicles.find(x => x.slug === params.slug)
  if (!l) notFound()

  const jsonLd = generateJsonLd(l)

  return (
    <>
      {jsonLd.map((s, i) => (
        <script key={i} type="application/ld+json" dangerouslySetInnerHTML={{ __html: s }} />
      ))}

      <div className="review-page container">
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <span>Best Of</span>
          <span className="sep">›</span>
          <span className="current">{l.shortTitle}</span>
        </nav>

        <h1>{l.title}</h1>
        <div className="meta-bar">
          <span className="card-cat">{l.category}</span>
          <span className="card-price">{l.items.length} tools ranked</span>
          <span className="card-badge tested" style={{ display: 'inline-flex', alignItems: 'center', gap: 4, background: 'var(--c-bg)', color: 'var(--c-text)', fontSize: '0.68rem', fontWeight: 600, padding: '2px 8px', borderRadius: '100px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>✓ 2026 Data Verified</span>
        </div>

        {/* Quick verdict */}
        <div className="verdict-box">
          <h2 style={{ fontSize: '1.15rem', fontWeight: 700, marginBottom: 8, color: 'var(--k-deep)' }}>⚡ Quick Verdict (30-Second Answer)</h2>
          <p>{l.quickVerdict}</p>
        </div>

        {/* Wirecutter-style three-tier picks */}
        <PicksCards picks={
          l.items
            .map((it, i) => ({ it, i }))
            .filter(({ it }) => it.pickType)
            .map(({ it, i }) => {
              const rev = it.reviewSlug ? reviews.find(r => r.slug === it.reviewSlug) : null
              return { type: it.pickType, name: it.name, tagline: it.tagline, rating: rev ? rev.rating : undefined, anchor: `#pick-${i + 1}` }
            })
        } />

        {/* Intro */}
        {l.introContent && (
          <div className="review-content" dangerouslySetInnerHTML={{ __html: l.introContent }} />
        )}

        {/* Summary table */}
        <h2 id="at-a-glance" style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>The {l.items.length} at a Glance</h2>
        <div className="review-content compare-table-wrap">
          <table className="compare-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Alternative</th>
                <th>Best For</th>
                <th>Pricing</th>
                <th>Catalog</th>
              </tr>
            </thead>
            <tbody>
              {l.items.map((it, i) => (
                <tr key={i}>
                  <td>{i + 1}</td>
                  <td><strong>{it.name}</strong>{it.pickType === 'top' && <span className="pick-inline-tag">Our Pick</span>}</td>
                  <td>{it.bestFor}</td>
                  <td>{it.pricingShort}</td>
                  <td>{it.catalogShort}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* Feature matrix — top contenders side by side */}
        {l.features?.length > 0 && l.featureCols?.length > 0 && (
          <>
            <h2 style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>Top Contenders, Feature by Feature</h2>
            <FeatureMatrix features={l.features} names={l.featureCols} />
          </>
        )}

        {/* Per-tool sections */}
        {l.items.map((it, i) => {
          const review = it.reviewSlug ? reviews.find(r => r.slug === it.reviewSlug) : null
          return (
            <section key={i} id={`pick-${i + 1}`} className={`listicle-item${i === 0 ? ' top-pick' : ''}`}>
              {i === 0 && <span className="pick-badge top-pick-badge">#1 Our Pick</span>}
              <h2>{i + 1}. {it.name} — {it.tagline}</h2>
              {review && (
                <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginBottom: 10 }}>
                  Our rating: <RatingBar rating={review.rating} />
                  {' · '}<Link href={`/${review.slug}/`} style={{ color: 'var(--c-primary)' }}>Read the full {it.name} review →</Link>
                </p>
              )}
              <div className="review-content" dangerouslySetInnerHTML={{ __html: it.content }} />
              <p>
                <a href={it.ctaUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
                  Try {it.name} →
                </a>
              </p>
            </section>
          )
        })}

        {/* How to choose + closing */}
        <div className="review-content" dangerouslySetInnerHTML={{ __html: l.closingContent }} />

        {/* Why trust us — shared editorial module */}
        <WhyTrustUs />

        {/* FAQ */}
        <div className="faq-section">
          <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 16, color: 'var(--k-deep)' }}>Frequently Asked Questions</h2>
          {l.faqs.map((faq, i) => (
            <details key={i} className="faq-item">
              <summary className="faq-question">{faq.q}</summary>
              <div className="faq-answer"><p>{faq.a}</p></div>
            </details>
          ))}
        </div>

        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. All rankings are based on honest, independent research. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
