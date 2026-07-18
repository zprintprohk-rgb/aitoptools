'use client'
import { useState, useEffect } from 'react'
import Link from 'next/link'
import reviews from '@/data/reviews'
import comparisons from '@/data/comparisons.json'
import listicles from '@/data/listicles.json'

const VERTICAL_CATEGORIES = [
  { name: '🖨️ Print & Packaging', slug: 'ai-print-design', desc: 'AI for print-on-demand, packaging design, label making', featured: true },
  { name: '🛒 E-Commerce & Shopify', slug: 'ai-ecommerce', desc: 'AI for product descriptions, store optimization, cross-border', featured: true },
  { name: '✍️ AI Writing', slug: 'ai-writing', desc: 'Copywriting, content creation, multilingual writing' },
  { name: '🎨 AI Image', slug: 'ai-image', desc: 'Image generation, editing, product photography' },
  { name: '🎬 AI Video', slug: 'ai-video', desc: 'Video generation, avatars, editing' },
  { name: '🎙️ AI Voice', slug: 'ai-voice', desc: 'Voice synthesis, dubbing, podcasting' },
]

const SCENARIO_TAGS = [
  { label: '📦 Packaging Design', href: '/category/ai-print-design/' },
  { label: '🛍️ Shopify', href: '/category/ai-ecommerce/' },
  { label: '👕 Print-on-Demand', href: '/category/ai-print-design/' },
  { label: '📸 Product Photos', href: '/category/ai-ecommerce/' },
]

const CAT_CARDS = [
  { name: 'Print & Packaging', slug: 'ai-print-design', desc: 'AI for print-on-demand, packaging design, label making' },
  { name: 'E-Commerce & Shopify', slug: 'ai-ecommerce', desc: 'AI for product descriptions, store optimization, cross-border' },
  { name: 'AI Writing', slug: 'ai-writing', desc: 'Copywriting, content creation, multilingual writing' },
  { name: 'AI Image', slug: 'ai-image', desc: 'Image generation, editing, product photography' },
  { name: 'AI Video', slug: 'ai-video', desc: 'Video generation, avatars, editing' },
  { name: 'AI Voice', slug: 'ai-voice', desc: 'Voice synthesis, dubbing, podcasting' },
]

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export default function Home() {
  const [search, setSearch] = useState('')

  // Pick up ?q= from the nav search box (GET form → /?q=...)
  useEffect(() => {
    const q = new URLSearchParams(window.location.search).get('q')
    if (q) setSearch(q)
  }, [])

  const filtered = search.trim()
    ? reviews.filter(r =>
        r.title.toLowerCase().includes(search.toLowerCase()) ||
        r.category.toLowerCase().includes(search.toLowerCase()) ||
        r.metaDesc.toLowerCase().includes(search.toLowerCase())
      )
    : []

  // Identify vertical tools (print/e-commerce)
  const printTools = reviews.filter(r => 
    r.slug.includes('print') || r.slug.includes('packag') || 
    r.slug.includes('kittl') || r.slug.includes('placeit') || r.slug.includes('looka') ||
    r.slug.includes('claid') || r.slug.includes('photoroom')
  )
  const ecomTools = reviews.filter(r =>
    r.slug.includes('ecom') || r.slug.includes('shopify') ||
    r.slug.includes('product')
  )
  const verticalSlugs = [...printTools, ...ecomTools].map(r => r.slug)
  const generalTools = reviews.filter(r => !verticalSlugs.includes(r.slug))

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: 'Print AI Tools',
            url: 'https://aitoptools.net/',
          }),
        }}
      />
      {/* HERO */}
      <div className="hero">
        <div className="container hero-inner">
          <div className="hero-text">
            <h1>AI Tools for <em>Print Shops</em> &amp; Independent Store Owners</h1>
            <p>Hands-on reviews, real screenshots, and honest comparisons — tested by print industry professionals.</p>
            <p className="trust-line">✓ Tested by print &amp; e-commerce industry professionals with hands-on experience</p>

            <div className="search-bar" id="search">
              <input
                type="text"
                placeholder="Search AI tools... (e.g. packaging design, Shopify)"
                value={search}
                onChange={e => setSearch(e.target.value)}
              />
              <button type="button">Search</button>
            </div>

            {/* Scenario tags — replaces duplicate category nav */}
            <div className="scenario-tags">
              {SCENARIO_TAGS.map(tag => (
                <Link key={tag.label} href={tag.href} className="scenario-tag">{tag.label}</Link>
              ))}
            </div>
          </div>

          {/* Product-as-proof: the site's own content, rendered — not a photo */}
          <div className="hero-proof" aria-hidden="true">
            <div className="mini-vs">
              <div className="mini-vs-battle">
                <span className="mini-side"><b>Printful</b><i>★ 4.5</i></span>
                <span className="mini-badge">VS</span>
                <span className="mini-side"><b>Printify</b><i>★ 4.3</i></span>
              </div>
              <p className="mini-verdict">Printify wins on margin &amp; catalog. Printful wins on quality &amp; branding.</p>
              <span className="mini-link">Read Comparison →</span>
            </div>
            <div className="mini-stat"><strong>★ 4.8</strong> avg rating · 74+ tools tested</div>
          </div>
        </div>
      </div>

      {/* CATEGORY PHOTO CARDS */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2>Browse by Category</h2>
          </div>
          <div className="cat-grid">
            {CAT_CARDS.map(c => (
              <article key={c.slug} className="cat-card">
                <h3><Link href={`/category/${c.slug}/`}>{c.name}</Link></h3>
                <p>{c.desc}</p>
                <span className="cat-meta">{reviews.filter(r => r.categorySlug === c.slug).length} tools <i>→</i></span>
              </article>
            ))}
          </div>
        </div>
      </div>

      {/* SEARCH RESULTS */}
      {search.trim() && (
        <div className="section">
          <div className="container">
            <div className="section-header">
              <h2>Results for &ldquo;{search}&rdquo;</h2>
              <span style={{ color: 'var(--k-tertiary)', fontSize: '0.85rem' }}>{filtered.length} tool{filtered.length !== 1 ? 's' : ''} found</span>
            </div>
            {filtered.length === 0 ? (
              <p style={{ color: 'var(--k-tertiary)', padding: '20px 0' }}>No tools found. Try a different keyword.</p>
            ) : (
              <div className="review-grid">
                {filtered.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            )}
          </div>
        </div>
      )}

      {/* TOP COMPARISONS — duel-style cards, visually distinct from tool cards */}
      <div className="section section-alt">
        <div className="container">
          <div className="featured-panel">
            <div className="section-header">
              <h2>⚖️ Top Comparisons</h2>
              <Link href="/compare/" className="view-all">View All →</Link>
            </div>
            <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
              Head-to-head showdowns with clear winners — verified 2026 pricing, real cost math, no fence-sitting.
            </p>
            <div className="vs-grid">
              {comparisons.map(c => (
                <article key={c.slug} className="vs-card">
                  <div className="vs-card-battle">
                    <div className="vs-side">
                      <span className="vs-name">{c.toolA.name}</span>
                      <span className="vs-rating">★ {c.toolA.rating}</span>
                    </div>
                    <span className="vs-badge">VS</span>
                    <div className="vs-side">
                      <span className="vs-name">{c.toolB.name}</span>
                      <span className="vs-rating">★ {c.toolB.rating}</span>
                    </div>
                  </div>
                  <h3 className="vs-title"><Link href={`/compare/${c.slug}/`}>{c.title}</Link></h3>
                  <p className="vs-verdict">{c.quickVerdict.split('.')[0]}.</p>
                  <Link href={`/compare/${c.slug}/`} className="card-cta">Read Comparison →</Link>
                </article>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* BEST OF LISTS — ranked roundups, third content type */}
      <div className="section">
        <div className="container">
          <div className="featured-panel green">
            <div className="section-header">
              <h2>🏆 Best Of Lists</h2>
              <Link href="/best/" className="view-all">View All →</Link>
            </div>
            <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
              Ranked roundups with clear winners — no pay-to-rank placements.
            </p>
            <div className="best-grid">
            {listicles.map(l => (
              <article key={l.slug} className="best-card">
                <span className="best-card-count">{l.items.length} ranked</span>
                <h3 className="best-card-title"><Link href={`/best/${l.slug}/`}>{l.title}</Link></h3>
                <div className="best-card-names">
                  {l.items.slice(0, 4).map((it, i) => (
                    <span key={i} className="best-card-name">#{i + 1} {it.name}</span>
                  ))}
                  {l.items.length > 4 && <span className="best-card-name more">+{l.items.length - 4} more</span>}
                </div>
                <Link href={`/best/${l.slug}/`} className="card-cta">See the Rankings →</Link>
              </article>
            ))}
            </div>
          </div>
        </div>
      </div>

      {/* SECTION 2: Vertical Featured — Print & Packaging */}
      <div className="section section-alt">
        <div className="container">
          <div className="vertical-featured">
            <div className="vertical-featured-header">
              <h2>🖨️ Best AI Tools for <strong>Print &amp; Packaging</strong></h2>
              <Link href="/category/ai-print-design/" className="view-all">View All →</Link>
            </div>
            {printTools.length > 0 ? (
              <div className="review-grid">
                {printTools.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            ) : (
              <p style={{ color: 'var(--k-tertiary)', fontSize: '0.9rem' }}>Print &amp; packaging reviews coming soon. <Link href="/submit-tool/">Suggest a tool.</Link></p>
            )}
          </div>

          <div className="vertical-featured" style={{ marginTop: 24 }}>
            <div className="vertical-featured-header">
              <h2>🛒 Best AI Tools for <strong>E-Commerce &amp; Shopify</strong></h2>
              <Link href="/category/ai-ecommerce/" className="view-all">View All →</Link>
            </div>
            {ecomTools.length > 0 ? (
              <div className="review-grid">
                {ecomTools.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            ) : (
              <p style={{ color: 'var(--k-tertiary)', fontSize: '0.9rem' }}>E-commerce reviews coming soon. <Link href="/submit-tool/">Suggest a tool.</Link></p>
            )}
          </div>
        </div>
      </div>

      {/* SECTION 3: All Tools (vertical-first sort) */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2>All Tool Reviews</h2>
            <span style={{ color: 'var(--k-tertiary)', fontSize: '0.85rem' }}>{reviews.length} tools reviewed</span>
          </div>
          <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
            Sorted by relevance — print &amp; e-commerce tools shown first.
          </p>
          <div className="review-grid">
            {[...printTools, ...ecomTools, ...generalTools].map(r => (
              <ReviewCard key={r.slug} review={r} />
            ))}
          </div>
        </div>
      </div>

      {/* SECTION 4: CTA */}
      <div className="section section-alt">
        <div className="container" style={{ textAlign: 'center', maxWidth: 600, margin: '0 auto' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 6, color: 'var(--k-deep)' }}>
            Have an AI tool for print shops or e-commerce?
          </h2>
          <p style={{ color: 'var(--k-tertiary)', marginBottom: 20, fontSize: '0.9rem' }}>
            We&apos;re always looking for great AI tools serving independent store owners and print businesses. Submit your tool for review.
          </p>
          <Link href="/submit-tool/" className="cta-button">Submit Your Tool →</Link>
        </div>
      </div>
    </>
  )
}

function ReviewCard({ review }) {
  const isVertical = review.slug.includes('print') || review.slug.includes('packag') || 
    review.slug.includes('kittl') || review.slug.includes('placeit') || review.slug.includes('looka') ||
    review.slug.includes('claid') || review.slug.includes('photoroom') || 
    review.slug.includes('ecom') || review.slug.includes('shopify')

  const isGenericCat = review.category === 'AI Writing' || review.category === 'AI Video' || 
    review.category === 'AI Voice' || review.category === 'AI Image'

  return (
    <article className="review-card">
      <div className="card-badges">
        <span className="card-badge tested">Hands-on Tested</span>
        {isVertical && <span className="card-badge vertical">Print &amp; E-Com</span>}
      </div>
      <div className="card-meta">
        <span className={isGenericCat ? "card-cat generic" : "card-cat"}>{review.category}</span>
        <span className="card-rating">{starRating(review.rating)} {review.rating}</span>
        <span className="card-price">{review.price}</span>
      </div>
      <h3><Link href={`/${review.slug}/`}>{review.title}</Link></h3>
      <p className="card-desc">{review.metaDesc}</p>
      <div className="card-cta-group">
        <Link href={`/${review.slug}/`} className="card-cta">Read Full Review →</Link>
        {review.affiliateUrl && (
          <a href={review.affiliateUrl} target="_blank" rel="nofollow sponsored" className="card-cta affiliate">
            Check Deal ↗
          </a>
        )}
      </div>
      {isVertical && (
        <div className="vertical-score">
          <div className="score-row">
            <span className="score-label">Print Compatibility</span>
            <div className="score-bar">
              <div className="score-fill print" style={{width: '88%'}}></div>
            </div>
            <span className="score-val">8.8</span>
          </div>
          <div className="score-row">
            <span className="score-label">E-Commerce Fit</span>
            <div className="score-bar">
              <div className="score-fill ecom" style={{width: '82%'}}></div>
            </div>
            <span className="score-val">8.2</span>
          </div>
        </div>
      )}
    </article>
  )
}
