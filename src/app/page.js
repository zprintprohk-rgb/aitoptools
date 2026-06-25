import Link from 'next/link'
import reviews from '@/data/reviews'

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export default function Home() {
  const categories = [...new Set(reviews.map(r => r.category))]
  
  return (
    <>
      <div className="hero">
        <h1>Best AI Tools Reviews 2026</h1>
        <p>Honest, in-depth reviews of the best AI tools. We test every tool so you don't have to.</p>
        <div className="categories">
          {categories.map(cat => (
            <span key={cat} className="cat-tag">{cat}</span>
          ))}
        </div>
      </div>

      <div className="review-grid">
        {reviews.map(review => (
          <article key={review.slug} className="review-card">
            <div className="meta">
              <span className="cat">{review.category}</span>
              <span className="rating">{starRating(review.rating)} {review.rating}</span>
              <span>{review.price}</span>
            </div>
            <h2><Link href={`/${review.slug}/`}>{review.title}</Link></h2>
            <p>{review.metaDesc}</p>
            <Link href={`/${review.slug}/`} className="cta">Read Full Review →</Link>
          </article>
        ))}
      </div>
    </>
  )
}
