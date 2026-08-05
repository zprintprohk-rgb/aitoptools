/**
 * Blog 索引页 — 文章列表 (2026-08-04)
 * 数据源: src/data/blog-posts.json (SSoT, 内容军规 §3.1)
 */
import Link from 'next/link'
import posts from '@/data/blog-posts.json'

export const metadata = {
  title: 'Blog — Hands-On AI Tool Tests for Print & POD',
  description: 'Real-world testing reports, step-by-step tutorials, and honest comparisons of AI tools for print shops, packaging design, and POD sellers. Written by Jerome Tang, print industry expert.',
  alternates: { canonical: 'https://aitoptools.net/blog/' },
  openGraph: {
    title: 'Blog — Hands-On AI Tool Tests for Print & POD',
    description: 'Real-world testing reports and honest comparisons of AI tools for print shops and POD sellers.',
    url: 'https://aitoptools.net/blog/',
    type: 'website',
    siteName: 'Print AI Tools',
  },
}

export default function BlogIndexPage() {
  const sorted = [...posts].sort((a, b) => (b.datePublished || '').localeCompare(a.datePublished || ''))

  return (
    <div className="review-page container">
      <nav className="breadcrumb" aria-label="Breadcrumb">
        <Link href="/">Home</Link>
        <span className="sep">›</span>
        <span className="current">Blog</span>
      </nav>

      <h1>Print AI Tools Blog</h1>
      <p style={{ color: 'var(--k-tertiary)', maxWidth: 720, marginBottom: 32 }}>
        Real testing reports, step-by-step tutorials, and honest comparisons — every article written in the first
        person by <strong>Jerome Tang, Print Industry Expert</strong>, with screenshots from actual test runs.
      </p>

      {sorted.length === 0 ? (
        <div className="verdict-box">
          <p style={{ margin: 0 }}>
            📝 New articles are landing with the 8/5 content batch — check back shortly. Meanwhile, browse the{' '}
            <Link href="/best/" style={{ color: 'var(--c-primary)' }}>Best Of rankings</Link> or{' '}
            <Link href="/compare/" style={{ color: 'var(--c-primary)' }}>comparisons</Link>.
          </p>
        </div>
      ) : (
        <div className="review-grid">
          {sorted.map((p) => (
            <article key={p.slug} className="review-card">
              <div className="card-badges">
                <span className="card-badge tested">✓ Hands-on Tested</span>
              </div>
              <div className="card-meta">
                <span className="card-cat">{p.category}</span>
                <span className="card-rating" style={{ fontSize: '0.85rem' }}>{p.datePublished}</span>
              </div>
              <h3 style={{ fontSize: '1.1rem', lineHeight: 1.4 }}>
                <Link href={`/blog/${p.slug}/`}>{p.title}</Link>
              </h3>
              <p className="card-desc">{p.metaDescription}</p>
              <Link href={`/blog/${p.slug}/`} className="card-cta">Read Article →</Link>
            </article>
          ))}
        </div>
      )}

      <div className="aff-disc" style={{ marginTop: 40 }}>
        <strong>Affiliate Disclosure:</strong> Some links on this site are affiliate links. We may earn a commission
        if you make a purchase through these links, at no additional cost to you. All reviews are based on honest,
        independent testing by print industry professionals. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
      </div>
    </div>
  )
}
