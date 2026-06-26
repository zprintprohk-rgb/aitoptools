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
    alternates: {
      canonical: `https://aitoptools.net/${params.slug}`,
    },
  }
}

function getToolName(slug) {
  return slug
    .replace('-review', '')
    .split('-')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1))
    .join(' ')
}

function generateReviewJsonLd(review) {
  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const priceStr = (review.price || '$0').replace('$', '').split('/')[0]
  const price = parseFloat(priceStr) || 0

  const schema = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Review',
        name: review.title,
        author: { '@type': 'Organization', name: 'AI Tool Reviews' },
        datePublished: '2026-06-25',
        reviewRating: {
          '@type': 'Rating',
          ratingValue: String(review.rating),
          bestRating: '5',
          worstRating: '1',
        },
        itemReviewed: {
          '@type': 'SoftwareApplication',
          name: toolName,
          applicationCategory: 'AIApplication',
          operatingSystem: 'All',
          offers: {
            '@type': 'Offer',
            price: String(price),
            priceCurrency: 'USD',
          },
        },
      },
    ],
  }
  if (review.pros?.length) {
    schema['@graph'][0].positiveNotes = review.pros.map((p, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      text: p,
    }))
  }
  if (review.cons?.length) {
    schema['@graph'][0].negativeNotes = review.cons.map((c, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      text: c,
    }))
  }
  if (review.affiliateUrl) {
    schema['@graph'][0].url = review.affiliateUrl
  }
  if (review.metaDesc) {
    schema['@graph'][0].description = review.metaDesc
  }

  return JSON.stringify(schema)
}

function generateBreadcrumbJsonLd(review, slug) {
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
      { '@type': 'ListItem', position: 2, name: review.category || 'AI Tools', item: 'https://aitoptools.net/' },
      { '@type': 'ListItem', position: 3, name: review.title, item: `https://aitoptools.net/${slug}` },
    ],
  })
}

function generateFaqJsonLd(review) {
  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const price = review.price || '$0'

  const faqs = [
    {
      question: `Is ${toolName} worth it?`,
      answer: `${toolName} is one of the top tools in its category. With a rating of ${review.rating}/5 and starting at ${price}, it's a ${review.rating >= 4 ? 'solid choice' : 'decent option'} for users who need its specific capabilities.`,
    },
    {
      question: `How much does ${toolName} cost?`,
      answer: `${toolName} starts at ${price}. Check their official website for the latest pricing, plans, and any available discounts or promotions.`,
    },
    {
      question: `Does ${toolName} have a free trial?`,
      answer: `Most AI tools offer either a free tier or a free trial. Visit ${toolName}'s website to check their current trial offer and see if it meets your needs.`,
    },
    {
      question: `What is ${toolName} best for?`,
      answer: `${toolName} is designed for ${review.category || 'AI tool'} use cases. It's particularly well-suited for users who need professional-grade features and reliable performance.`,
    },
  ]

  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(f => ({
      '@type': 'Question',
      name: f.question,
      acceptedAnswer: { '@type': 'Answer', text: f.answer },
    })),
  })
}

export default function ReviewPage({ params }) {
  const review = reviews.find(r => r.slug === params.slug)
  if (!review) notFound()

  const reviewJsonLd = generateReviewJsonLd(review)
  const breadcrumbJsonLd = generateBreadcrumbJsonLd(review, params.slug)
  const faqJsonLd = generateFaqJsonLd(review)

  return (
    <>
      {/* JSON-LD Structured Data for Google Rich Results */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: reviewJsonLd }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbJsonLd }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: faqJsonLd }}
      />

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
    </>
  )
}
