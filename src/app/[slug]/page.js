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
    title: `${review.title} | Print AI Tools`,
    description: review.metaDesc,
    alternates: {
      canonical: `https://aitoptools.net/${params.slug}/`,
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
        author: { '@type': 'Organization', name: 'Print AI Tools' },
        datePublished: review.datePublished || '2026-06-25',
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
  const catSlug = getCategorySlug(review)
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
      { '@type': 'ListItem', position: 2, name: review.category || 'AI Tools', item: `https://aitoptools.net/${catSlug}/` },
      { '@type': 'ListItem', position: 3, name: review.title, item: `https://aitoptools.net/${slug}/` },
    ],
  })
}

function getCategorySlug(review) {
  if (review.slug.includes('print') || review.slug.includes('packag')) return 'category/ai-print-design'
  if (review.slug.includes('ecom') || review.slug.includes('shopify')) return 'category/ai-ecommerce'
  const cat = (review.category || '').toLowerCase().replace(/\s+/g, '-')
  const map = {
    'ai-writing': 'category/ai-writing',
    'ai-image': 'category/ai-image',
    'ai-video': 'category/ai-video',
    'ai-voice': 'category/ai-voice',
  }
  return map[cat] || '/'
}

function generateFaqJsonLd(review) {
  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const price = review.price || '$0'

  const faqs = [
    {
      question: `Is ${toolName} worth it?`,
      answer: `${toolName} is a top tool in the ${review.category} category. With a rating of ${review.rating}/5 and pricing starting at ${price}, it's a ${review.rating >= 4 ? 'strong choice' : 'decent option'} for print shop owners and independent store operators looking to streamline their workflows.`,
    },
    {
      question: `How much does ${toolName} cost?`,
      answer: `${toolName} starts at ${price}. Visit their official website for the latest pricing, plans, and any available discounts — especially for print and e-commerce business users.`,
    },
    {
      question: `Does ${toolName} have a free trial?`,
      answer: `Most AI tools offer either a free tier or a free trial. Check ${toolName}'s website for current trial offers to see if it meets your print shop or e-commerce needs before committing.`,
    },
    {
      question: `What is ${toolName} best for?`,
      answer: `${toolName} is designed for ${review.category} use cases. It's particularly useful for independent store owners and print businesses that need reliable, professional-grade AI tools.`,
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

  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const isVertical = review.slug.includes('print') || review.slug.includes('packag') || 
    review.slug.includes('ecom') || review.slug.includes('shopify')

  const reviewJsonLd = generateReviewJsonLd(review)
  const breadcrumbJsonLd = generateBreadcrumbJsonLd(review, params.slug)
  const faqJsonLd = generateFaqJsonLd(review)

  return (
    <>
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

      <div className="review-page container">
        <Link href="/" className="back-link">← Back to all tools</Link>
        
        <h1>{review.title}</h1>
        <div className="meta-bar">
          <span className="card-cat">{review.category}</span>
          <span className="card-rating">{starRating(review.rating)} {review.rating}</span>
          <span className="card-price">From {review.price}</span>
          {isVertical && <span className="vertical-badge">🖨️ Print & E-Commerce</span>}
          <a href={review.visitUrl} target="_blank" rel="nofollow sponsored" style={{ color: '#0d9488', fontWeight: 500 }}>
            Visit Official Site →
          </a>
        </div>

        <div className="pros-cons">
          <div className="pros-box">
            <h3>✓ Pros</h3>
            <ul>{review.pros.map((p, i) => <li key={i}>{p}</li>)}</ul>
          </div>
          <div className="cons-box">
            <h3>✗ Cons</h3>
            <ul>{review.cons.map((c, i) => <li key={i}>{c}</li>)}</ul>
          </div>
        </div>

        <div className="review-content" dangerouslySetInnerHTML={{ __html: review.content }} />

        {/* Affiliate CTA */}
        <div className="cta-box">
          <p>Ready to try <strong>{toolName}</strong> for your business?</p>
          <p style={{ fontSize: '0.9rem', color: '#78716c', marginBottom: 14 }}>
            Click below to start your free trial or explore plans. If you purchase through our link, we may earn a commission at no extra cost to you.
          </p>
          <a href={review.affiliateUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
            Try {toolName} Free →
          </a>
        </div>

        {/* Similar tools */}
        <div className="section-header" style={{ marginTop: 40 }}>
          <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#1c1917' }}>Compare Similar Tools</h2>
        </div>
        <div className="review-grid" style={{ gridTemplateColumns: 'repeat(2, 1fr)' }}>
          {reviews
            .filter(r => r.slug !== review.slug && r.category === review.category)
            .slice(0, 2)
            .map(r => (
              <article key={r.slug} className="review-card">
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

        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. All reviews are based on honest, independent testing. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
