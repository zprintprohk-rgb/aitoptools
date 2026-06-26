import { notFound } from 'next/navigation'
import Link from 'next/link'
import reviews from '@/data/reviews'

const CATEGORY_MAP = {
  'ai-print-design': { title: 'AI Print & Packaging Design Tools', desc: 'AI tools for print-on-demand, packaging design, label making, brochure design, and print shop automation.' },
  'ai-ecommerce': { title: 'AI E-Commerce & Shopify Tools', desc: 'AI tools for product descriptions, cross-border e-commerce, store optimization, and Shopify store management.' },
  'ai-writing': { title: 'AI Writing & Copywriting Tools', desc: 'AI writing assistants for content creation, copywriting, multilingual translations, and marketing copy.' },
  'ai-image': { title: 'AI Image Generation & Editing Tools', desc: 'AI image generators, editors, product photography tools, and design automation software.' },
  'ai-video': { title: 'AI Video Generation & Editing Tools', desc: 'AI video creators, avatar generators, and video editing tools for marketing and content creation.' },
  'ai-voice': { title: 'AI Voice & Audio Tools', desc: 'AI voice synthesis, text-to-speech, dubbing, podcasting, and audio production tools.' },
}

export function generateStaticParams() {
  return Object.keys(CATEGORY_MAP).map(slug => ({ slug }))
}

export function generateMetadata({ params }) {
  const cat = CATEGORY_MAP[params.slug]
  if (!cat) return { title: 'Not Found' }
  return {
    title: `${cat.title} 2026 | Print AI Tools`,
    description: cat.desc,
    alternates: { canonical: `https://aitoptools.net/category/${params.slug}/` },
  }
}

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export default function CategoryPage({ params }) {
  const cat = CATEGORY_MAP[params.slug]
  if (!cat) notFound()

  const categoryReviews = reviews.filter(r => {
    const catSlug = params.slug
    if (catSlug === 'ai-print-design') return r.slug.includes('print') || r.slug.includes('packag')
    if (catSlug === 'ai-ecommerce') return r.slug.includes('ecom') || r.slug.includes('shopify')
    return r.category.toLowerCase().replace(/\s+/g, '-') === catSlug || 
           r.slug.startsWith(catSlug.replace('ai-', ''))
  })

  return (
    <>
      <div className="category-header">
        <div className="container">
          <h1>{cat.title}</h1>
          <p>{cat.desc}</p>
          <p style={{ marginTop: 8, color: '#a8a29e', fontSize: '0.85rem' }}>
            {categoryReviews.length} tool{categoryReviews.length !== 1 ? 's' : ''} reviewed
          </p>
        </div>
      </div>

      <div className="section">
        <div className="container">
          {categoryReviews.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 0', color: '#78716c' }}>
              <p style={{ fontSize: '1.1rem', marginBottom: 12 }}>No reviews in this category yet.</p>
              <p>Check back soon — we&apos;re adding new reviews every week!</p>
              <Link href="/" className="cta-button" style={{ display: 'inline-block', marginTop: 20 }}>Back to Home</Link>
            </div>
          ) : (
            <div className="review-grid">
              {categoryReviews.map(r => (
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
          )}
        </div>
      </div>
    </>
  )
}
