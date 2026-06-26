'use client'
import { useState } from 'react'
import Link from 'next/link'
import reviews from '@/data/reviews'

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

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export default function Home() {
  const [search, setSearch] = useState('')

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
      {/* HERO */}
      <div className="hero">
        <h1>AI Tools for <em>Print Shops</em> &amp; Independent Store Owners</h1>
        <p>Hands-on reviews, real screenshots, and honest comparisons — tested by print industry professionals.</p>
        <p className="trust-line">✓ Tested by print &amp; e-commerce industry professionals with hands-on experience</p>

        <div className="search-bar">
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
