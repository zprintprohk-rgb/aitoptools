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

  // Separate vertical-specific tools (print, e-commerce) from general
  const verticalTools = reviews.filter(r => 
    r.slug.includes('print') || r.slug.includes('packag') || 
    r.slug.includes('ecom') || r.slug.includes('shopify') ||
    r.slug.includes('product')
  )
  const generalTools = reviews.filter(r => !verticalTools.find(v => v.slug === r.slug))

  return (
    <>
      {/* Hero */}
      <div className="hero">
        <h1>AI Tools for <em>Print Shops</em> &amp; Independent Store Owners</h1>
        <p>Hands-on reviews, real screenshots, and honest comparisons of the best AI tools for print-on-demand, packaging design, cross-border e-commerce, and independent stores.</p>

        <div className="search-bar">
          <input
            type="text"
            placeholder="Search AI tools... (e.g. packaging design, Shopify)"
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
          <button type="button">Search</button>
        </div>

        <div className="vertical-tabs">
          <Link href="/category/ai-print-design/" className="vertical-tab featured">🖨️ Print &amp; Packaging</Link>
          <Link href="/category/ai-ecommerce/" className="vertical-tab featured">🛒 E-Commerce &amp; Shopify</Link>
          <Link href="/category/ai-writing/" className="vertical-tab">✍️ AI Writing</Link>
          <Link href="/category/ai-image/" className="vertical-tab">🎨 AI Image</Link>
          <Link href="/category/ai-video/" className="vertical-tab">🎬 AI Video</Link>
          <Link href="/category/ai-voice/" className="vertical-tab">🎙️ AI Voice</Link>
        </div>
      </div>

      {/* Search Results */}
      {search.trim() && (
        <div className="section">
          <div className="container">
            <div className="section-header">
              <h2>Search Results for &ldquo;{search}&rdquo;</h2>
              <span>{filtered.length} tool{filtered.length !== 1 ? 's' : ''} found</span>
            </div>
            {filtered.length === 0 ? (
              <p style={{ color: '#78716c', padding: '20px 0' }}>No tools found matching your search. Try a different keyword.</p>
            ) : (
              <div className="review-grid">
                {filtered.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            )}
          </div>
        </div>
      )}

      {/* Vertical Feature Section */}
      {verticalTools.length > 0 && (
        <div className="section section-alt">
          <div className="container">
            <div className="section-header">
              <h2>🖨️ For Print Shops &amp; E-Commerce</h2>
              <Link href="/category/ai-print-design/" className="view-all">View All →</Link>
            </div>
            <p style={{ color: '#78716c', marginBottom: 24, fontSize: '0.9rem' }}>
              AI tools specifically useful for print-on-demand stores, packaging design, Shopify sellers, and cross-border e-commerce.
            </p>
            <div className="review-grid">
              {verticalTools.map(r => <ReviewCard key={r.slug} review={r} />)}
            </div>
          </div>
        </div>
      )}

      {/* All Reviews */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2>All Tool Reviews</h2>
            <span style={{ color: '#78716c', fontSize: '0.85rem' }}>{reviews.length} tools reviewed</span>
          </div>
          <div className="review-grid">
            {generalTools.map(r => <ReviewCard key={r.slug} review={r} />)}
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="section section-alt">
        <div className="container" style={{ textAlign: 'center', maxWidth: 600, margin: '0 auto' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 700, marginBottom: 8, color: '#1c1917' }}>
            Have an AI tool for print shops or e-commerce?
          </h2>
          <p style={{ color: '#78716c', marginBottom: 20 }}>
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
    review.slug.includes('ecom') || review.slug.includes('shopify')
  return (
    <article className="review-card">
      <div className="card-meta">
        <span className="card-cat">{review.category}</span>
        <span className="card-rating">{starRating(review.rating)} {review.rating}</span>
        <span className="card-price">{review.price}</span>
      </div>
      <h3><Link href={`/${review.slug}/`}>{review.title}</Link></h3>
      <p className="card-desc">{review.metaDesc}</p>
      {isVertical && <span className="vertical-badge">🖨️ Print & E-Commerce</span>}
      <Link href={`/${review.slug}/`} className="card-cta">Read Full Review →</Link>
    </article>
  )
}
