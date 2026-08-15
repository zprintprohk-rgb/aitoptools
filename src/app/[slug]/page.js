import { notFound } from 'next/navigation'
import Link from 'next/link'
import reviews from '@/data/reviews'
import comparisons from '@/data/comparisons.json'
import RatingBar from '@/components/RatingBar'
import ProsCons from '@/components/ProsCons'
import { buildAffLinkAttrs } from '@/lib/affiliate'

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
      canonical: `https://aitoptools.net/${params.slug}/`,
    },
    openGraph: {
      title: review.title,
      description: review.metaDesc,
      url: `https://aitoptools.net/${params.slug}/`,
      type: 'article',
    },
    twitter: {
      card: 'summary_large_image',
      title: review.title,
      description: review.metaDesc,
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

const CATEGORY_DISPLAY = {
  'ai-print-design': '🖨️ Print & Packaging',
  'ai-ecommerce': '🛒 E-Commerce & Shopify',
  'ai-writing': 'AI Writing',
  'ai-image': 'AI Image',
  'ai-video': 'AI Video',
  'ai-voice': 'AI Voice',
}

function getCatSlug(review) {
  return review.categorySlug ? `/category/${review.categorySlug}/` : '/'
}

function generateReviewJsonLd(review) {
  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const priceStr = (review.price || '$0').replace('$', '').split('/')[0]
  const price = parseFloat(priceStr) || 0
  const schema = {
    '@context': 'https://schema.org',
    '@graph': [{
      '@type': 'Review',
      name: review.title,
      author: { '@type': 'Person', name: 'Jerome Tang', jobTitle: 'Print Industry Expert', worksFor: { '@type': 'Organization', name: 'Shenzhen Cai Long Printing', address: { '@type': 'PostalAddress', addressLocality: 'Shenzhen', addressCountry: 'CN' } } },
      publisher: { '@type': 'Organization', name: 'Print AI Tools', url: 'https://aitoptools.net/' },
      datePublished: review.datePublished || '2026-06-25',
      dateModified: review.dateModified || review.datePublished || '2026-06-25',
      reviewRating: { '@type': 'Rating', ratingValue: String(review.rating), bestRating: '5', worstRating: '1' },
      itemReviewed: {
        '@type': 'SoftwareApplication', name: toolName, applicationCategory: 'AIApplication',
        operatingSystem: 'All',
        offers: { '@type': 'Offer', price: String(price), priceCurrency: 'USD' },
      },
    }],
  }
  if (review.pros?.length) schema['@graph'][0].positiveNotes = review.pros.map((p, i) => ({ '@type': 'ListItem', position: i + 1, text: p }))
  if (review.cons?.length) schema['@graph'][0].negativeNotes = review.cons.map((c, i) => ({ '@type': 'ListItem', position: i + 1, text: c }))
  if (review.affiliateUrl) schema['@graph'][0].url = review.affiliateUrl
  if (review.metaDesc) schema['@graph'][0].description = review.metaDesc
  return JSON.stringify(schema)
}

function generateBreadcrumbJsonLd(review, slug) {
  const catSlug = getCatSlug(review)
  return JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
      { '@type': 'ListItem', position: 2, name: review.category || 'AI Tools', item: `https://aitoptools.net${catSlug}` },
      { '@type': 'ListItem', position: 3, name: review.title, item: `https://aitoptools.net/${slug}/` },
    ],
  })
}

function generateFaqJsonLd(review) {
  if (!review.faqs?.length) return null
  return JSON.stringify({
    '@context': 'https://schema.org', '@type': 'FAQPage',
    mainEntity: review.faqs.map(f => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
  })
}

const HUB_ROUNDUPS = [
  { cats: ['ai-print-design'], href: '/best/best-ai-tshirt-design-generators/', label: 'Best AI T-Shirt Design Generators (2026)', desc: 'our ranked roundup of 7 design tools for print-on-demand sellers' },
  { cats: ['ai-ecommerce'], href: '/best/printful-alternatives/', label: 'Best Printful Alternatives (2026)', desc: 'cheaper and faster POD platform options, ranked' },
  { cats: ['ai-writing'], href: '/best-ai-writing-tools-comparison/', label: 'Best AI Writing Tools Comparison', desc: 'Jasper vs Writesonic vs Copy.ai vs Rytr vs ChatGPT, side by side' },
  { cats: ['ai-image'], href: '/best-ai-background-removers-2026/', label: 'Best AI Background Removers for POD', desc: '7 tools tested on real print mockups' },
  { cats: ['ai-video', 'ai-voice'], href: '/category/ai-video/', label: 'AI Video & Voice category', desc: 'every video and voice tool review in one place' },
]
const POD_ROUNDUPS = [
  { slug: 'printful-review', href: '/best/printful-alternatives/', label: 'Best Printful Alternatives (2026)', desc: 'cheaper and faster POD platform options, ranked' },
  { slug: 'printify-review', href: '/best/printify-alternatives/', label: 'Best Printify Alternatives (2026)', desc: 'top picks after the Premium price hike' },
  { slug: 'gelato-review', href: '/best/best-print-on-demand-companies/', label: 'Best Print-on-Demand Companies (2026)', desc: '8 POD platforms compared for Etsy and Shopify sellers' },
]
function getHubLinks(review) {
  const pod = POD_ROUNDUPS.find(p => p.slug === review.slug)
  if (pod) return [pod]
  return HUB_ROUNDUPS.filter(h => h.cats.includes(review.categorySlug)).map(h => ({ href: h.href, label: h.label, desc: h.desc }))
}

function getCategoryDisplay(review) {
  return CATEGORY_DISPLAY[review.categorySlug] || review.category || 'AI Tools'
}

export default function ReviewPage({ params }) {
  const review = reviews.find(r => r.slug === params.slug)
  if (!review) notFound()

  const toolName = review.title.split(' Review')[0] || getToolName(review.slug)
  const isVertical = review.categorySlug === 'ai-print-design' || review.categorySlug === 'ai-ecommerce'
  const catSlug = getCatSlug(review)
  const catDisplay = getCategoryDisplay(review)

  const reviewJsonLd = generateReviewJsonLd(review)
  const breadcrumbJsonLd = generateBreadcrumbJsonLd(review, params.slug)
  const faqJsonLd = generateFaqJsonLd(review)

  const faqs = review.faqs || []

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: reviewJsonLd }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: breadcrumbJsonLd }} />
      {faqJsonLd && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: faqJsonLd }} />}

      <div className="review-page container">
        {/* Breadcrumb */}
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <Link href={catSlug}>{catDisplay}</Link>
          <span className="sep">›</span>
          <span className="current">{review.title}</span>
        </nav>

        <h1>{review.title}</h1>
        <div className="meta-bar">
          <span className="card-cat">{review.category}</span>
          <span className="meta-rating"><RatingBar rating={review.rating} /></span>
          <span className="card-price">From {review.price}</span>
          {review.dateModified && (
            <span style={{ color: 'var(--k-tertiary)', fontSize: '0.8rem' }}>· Last updated {review.dateModified}</span>
          )}
          {isVertical && <span className="card-badge vertical" style={{ display: 'inline-flex', alignItems: 'center', gap: 4, background: 'var(--y-bg)', color: 'var(--y-text)', fontSize: '0.7rem', fontWeight: 600, padding: '2px 8px', borderRadius: '100px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>🖨️ Print & E-Com</span>}
          <span className="card-badge tested" style={{ display: 'inline-flex', alignItems: 'center', gap: 4, background: 'var(--c-bg)', color: 'var(--c-text)', fontSize: '0.68rem', fontWeight: 600, padding: '2px 8px', borderRadius: '100px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>✓ Hands-on Tested</span>
          <a href={review.visitUrl} target="_blank" rel="nofollow sponsored" style={{ color: 'var(--c-primary)', fontWeight: 500, fontSize: '0.85rem' }}>
            Visit Official Site ↗
          </a>
        </div>
        {/* 8/6 信任三件套: 作者署名 (人格背书) */}
        <p className="byline" style={{ fontSize: '0.85rem', color: 'var(--k-secondary)', margin: '6px 0 0' }}>
          By <strong>Jerome Tang</strong> — Print industry expert · hands-on tested on real print jobs
        </p>
        <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', margin: '4px 0 0' }}>
          <strong>How we tested:</strong> Tested by Jerome Tang, Shenzhen Cai Long Printing — hands-on account testing, live pricing verification, and real print-order checks. See our <Link href="/methodology/">full testing methodology</Link>.
        </p>

        {review.featureLine && (
          <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', margin: '4px 0 0' }}>
            <strong>Key features:</strong> {review.featureLine}
          </p>
        )}

        {/* Pros & Cons */}
        <ProsCons pros={review.pros} cons={review.cons} />

        {/* Review Content */}
        {review.content ? (
          <div className="review-content" dangerouslySetInnerHTML={{ __html: review.content }} />
        ) : (
          <div className="review-content review-placeholder">
            <p>Full review coming soon. In the meantime, check out the pros/cons summary above.</p>
          </div>
        )}

        {/* FAQ Section (visible) */}
        <div className="faq-section">
          <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 16, color: 'var(--k-deep)' }}>Frequently Asked Questions</h2>
          {faqs.map((faq, i) => (
            <details key={i} className="faq-item">
              <summary className="faq-question">{faq.q}</summary>
              <div className="faq-answer"><p>{faq.a}</p></div>
            </details>
          ))}
        </div>

        {/* CTA */}
        <div className="cta-box">
          <p>Ready to try <strong>{toolName}</strong> for your business?</p>
          <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginBottom: 12 }}>
            Click below to start your free trial or explore plans. If you purchase through our link, we may earn a commission at no extra cost to you.
          </p>
          {(() => {
            // W1-T1 度量埋点: aff-link class + data-merchant + data-link-id + UTM
            const aff = buildAffLinkAttrs(review, 'detail-cta')
            if (aff) {
              return (
                <a
                  href={aff.href}
                  className={`${aff.className} cta-button`}
                  data-merchant={aff['data-merchant']}
                  data-link-id={aff['data-link-id']}
                  data-target={aff['data-target']}
                  target="_blank"
                  rel="nofollow sponsored"
                >
                  Try {toolName} Free →
                </a>
              )
            }
            if (review.visitUrl) {
              return (
                <a href={review.visitUrl} target="_blank" rel="nofollow sponsored" className="cta-button">
                  Try {toolName} Free →
                </a>
              )
            }
            return <p style={{ fontSize: '0.9rem', color: 'var(--k-tertiary)' }}>Review coming soon — check back for a hands-on link.</p>
          })()}
        </div>

        {/* W2-0823 four-layer internal links: tool -> compare -> list (hub cross-links) */}
        {(() => {
          const relatedComp = comparisons.filter(c => (c.toolA && c.toolA.reviewSlug === review.slug) || (c.toolB && c.toolB.reviewSlug === review.slug))
          const hubs = getHubLinks(review)
          if (!relatedComp.length && !hubs.length) return null
          return (
            <div className="related-links" style={{ marginTop: 36 }}>
              <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>Deeper Reads: Comparisons &amp; Roundups</h2>
              <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
                {relatedComp.map(c => (
                  <li key={c.slug}><Link href={`/compare/${c.slug}/`}>{c.title}</Link> — side-by-side pricing, catalog, and print-quality notes.</li>
                ))}
                {hubs.map(h => (
                  <li key={h.href}><Link href={h.href}>{h.label}</Link> — {h.desc}.</li>
                ))}
              </ul>
            </div>
          )
        })()}

        {/* Similar tools */}
        <div className="section-header" style={{ marginTop: 36 }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>Compare Similar Tools</h2>
        </div>
        <div className="review-grid" style={{ gridTemplateColumns: 'repeat(2, 1fr)' }}>
          {reviews
            .filter(r => r.slug !== review.slug && r.categorySlug === review.categorySlug)
            .slice(0, 2)
            .map(r => (
              <article key={r.slug} className="review-card">
                <div className="card-badges"><span className="card-badge tested">Hands-on Tested</span></div>
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

        {/* Affiliate Disclosure */}
        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. All reviews are based on honest, independent testing by print industry professionals. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
