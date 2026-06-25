import { notFound } from 'next/navigation'
import Link from 'next/link'
import reviews from '@/data/reviews'

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export function generateStaticParams() {
  return reviews.map(r => ({ slug: r.slug }))
}

export function generateMetadata({ params }) {
  const review = reviews.find(r => r.slug === params.slug)
  if (!review) return { title: 'Not Found' }
  return {
    title: review.title,
    description: review.metaDesc,
  }
}

export default function ReviewPage({ params }) {
  const review = reviews.find(r => r.slug === params.slug)
  if (!review) notFound()

  return (
    <div className="review-page">
      <Link href="/" style={{ color: '#64748b', fontSize: '0.9rem' }}>← Back to all reviews</Link>
      
      <h1>{review.title}</h1>
      <div className="meta-bar">
        <span className="cat" style={{ background: '#dbeafe', color: '#1d4ed8', padding: '2px 10px', borderRadius: '12px', fontSize: '0.85rem' }}>{review.category}</span>
        <span className="rating" style={{ color: '#f59e0b' }}>{starRating(review.rating)} {review.rating}</span>
        <span style={{ color: '#64748b' }}>Starting at {review.price}</span>
        <a href={review.visitUrl} target="_blank" rel="nofollow sponsored" style={{ color: '#2563eb' }}>Visit →</a>
      </div>

      <div className="pros-cons">
        <div className="pros">
          <h3>Pros</h3>
          <ul>{review.pros.map((p, i) => <li key={i}>{p}</li>)}</ul>
        </div>
        <div className="cons">
          <h3>Cons</h3>
          <ul>{review.cons.map((c, i) => <li key={i}>{c}</li>)}</ul>
        </div>
      </div>

      <div className="review-content" dangerouslySetInnerHTML={{ __html: review.content }} />

      <div className="cta-box">
        <p style={{ marginBottom: '12px', fontSize: '1.1rem' }}>Ready to try {review.title.split(' Review')[0]}?</p>
        <a href={review.affiliateUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
          Get Started with {review.title.split(' Review')[0]} →
        </a>
      </div>
    </div>
  )
}
