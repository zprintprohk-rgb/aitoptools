import Link from 'next/link'
import reviews from '@/data/reviews'
import config from '@/config'

export const metadata = {
  title: 'Best AI Tools 2026: Top Picks for Print Shops & E-Commerce',
  description: 'Our hand-tested picks of the best AI tools for print shops, packaging design, e-commerce, writing, image, video, and voice — ranked by category with honest ratings.',
  alternates: { canonical: `https://${config.domain}/best-ai-tools/` },
  openGraph: {
    title: 'Best AI Tools 2026: Top Picks for Print Shops & E-Commerce',
    description: 'Hand-tested picks of the best AI tools for print shops, packaging design, and e-commerce — ranked by category.',
    url: `https://${config.domain}/best-ai-tools/`,
    type: 'website',
  },
}

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

// Explicit per-tool categorySlug field (replaces legacy slug/category fuzzy matching)
function matchesCategory(r, catSlug) {
  return r.categorySlug === catSlug
}

export default function BestAiToolsPage() {
  const top10 = [...reviews].sort((a, b) => b.rating - a.rating).slice(0, 10)

  const itemListJsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: 'Best AI Tools 2026',
    description: metadata.description,
    url: `https://${config.domain}/best-ai-tools/`,
    numberOfItems: top10.length,
    itemListElement: top10.map((r, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: r.title.split(' Review')[0] || r.title,
      url: `https://${config.domain}/${r.slug}/`,
    })),
  })

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: itemListJsonLd }} />

      <div className="category-header">
        <div className="container">
          <h1>Best AI Tools 2026</h1>
          <p>Every tool below has been hands-on tested by our team. Ranked by category, with honest ratings for print shops and independent store owners.</p>
          <p style={{ marginTop: 8, color: '#a8a29e', fontSize: '0.85rem' }}>
            {reviews.length} tools reviewed across {config.categories.length} categories
          </p>
        </div>
      </div>

      {/* Top 10 overall */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2 style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--k-deep)' }}>🏆 Top 10 Overall</h2>
          </div>
          <div className="review-grid">
            {top10.map((r, i) => (
              <article key={r.slug} className="review-card">
                <div className="card-badges">
                  <span className="card-badge tested">#{i + 1} Overall</span>
                </div>
                <div className="card-meta">
                  <span className="card-cat">{r.category}</span>
                  <span className="card-rating">{starRating(r.rating)} {r.rating}</span>
                  <span className="card-price">{r.price}</span>
                </div>
                <h3><Link href={`/${r.slug}/`}>{r.title}</Link></h3>
                <p className="card-desc">{r.metaDesc}</p>
                <Link href={`/${r.slug}/`} className="card-cta">Read Full Review →</Link>
              </article>
            ))}
          </div>
        </div>
      </div>

      {/* By category */}
      {config.categories.map(cat => {
        const catReviews = reviews
          .filter(r => matchesCategory(r, cat.slug))
          .sort((a, b) => b.rating - a.rating)
        if (catReviews.length === 0) return null
        return (
          <div className="section" key={cat.slug}>
            <div className="container">
              <div className="section-header">
                <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>
                  {cat.icon} Best {cat.name} Tools
                </h2>
                <Link href={`/category/${cat.slug}/`} className="card-cta">
                  View all {catReviews.length} →
                </Link>
              </div>
              <div className="review-grid">
                {catReviews.map(r => (
                  <article key={r.slug} className="review-card">
                    <div className="card-meta">
                      <span className="card-cat">{r.category}</span>
                      <span className="card-rating">{starRating(r.rating)} {r.rating}</span>
                      <span className="card-price">{r.price}</span>
                    </div>
                    <h3><Link href={`/${r.slug}/`}>{r.title}</Link></h3>
                    <p className="card-desc">{r.metaDesc}</p>
                    <Link href={`/${r.slug}/`} className="card-cta">Read Full Review →</Link>
                  </article>
                ))}
              </div>
            </div>
          </div>
        )
      })}

      <div className="container">
        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
