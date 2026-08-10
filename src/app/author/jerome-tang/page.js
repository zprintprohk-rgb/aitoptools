import Link from 'next/link'
import config from '@/config'
import reviews from '@/data/reviews'
import blogPosts from '@/data/blog-posts.json'

export const metadata = {
  title: 'Jerome Tang — Print Industry Expert & Editor',
  description: 'Jerome Tang is the editor of Print AI Tools (aitoptools.net) — a print industry professional who hands-on tests AI tools for print-on-demand, packaging and product photography.',
  alternates: { canonical: 'https://aitoptools.net/author/jerome-tang/' },
}

export default function AuthorPage() {
  const reviewedCount = reviews.length
  const posts = blogPosts.slice(0, 8)
  return (
    <div className="review-page container" style={{ maxWidth: 760, margin: '0 auto' }}>
      <nav className="breadcrumb" aria-label="Breadcrumb">
        <Link href="/">Home</Link>
        <span className="sep">/</span>
        <Link href="/about/">About</Link>
        <span className="sep">/</span>
        <span className="current">Jerome Tang</span>
      </nav>

      <h1>Jerome Tang — Print Industry Expert &amp; Editor</h1>

      <div style={{ background: '#fff', border: '1px solid rgba(23,32,28,0.10)', borderRadius: 8, padding: '24px 28px', margin: '20px 0' }}>
        <p style={{ fontSize: '1.05rem', lineHeight: 1.8 }}>
          Jerome Tang is the editor of <strong>{config.brand}</strong> (aitoptools.net), a print-industry professional
          who has hands-on tested <strong>{reviewedCount} AI tools</strong> for print-on-demand, packaging design,
          mockups and product photography. Every review on this site is based on first-hand testing —
          real accounts, real orders, real screenshots — not vendor claims.
        </p>
        <h2 style={{ fontSize: '1.1rem', fontWeight: 700, margin: '18px 0 10px' }}>Credentials</h2>
        <ul style={{ lineHeight: 1.9, paddingLeft: 20 }}>
          <li>Editor, {config.brand} — {config.domain}</li>
          <li>Hands-on testing methodology: <Link href="/methodology/">see our methodology</Link></li>
          <li>Reviewed {reviewedCount} tools across AI print design, e-commerce, image, video and voice</li>
          <li>Independent reviews — no paid placements; full <Link href="/affiliate-disclosure/">affiliate disclosure</Link></li>
        </ul>
      </div>

      <h2 style={{ fontSize: '1.15rem', fontWeight: 700, margin: '24px 0 12px' }}>Latest Articles</h2>
      <ul style={{ lineHeight: 2, paddingLeft: 20 }}>
        {posts.map(p => (
          <li key={p.slug}><Link href={`/blog/${p.slug}/`}>{p.title}</Link> <span style={{ color: 'var(--k-tertiary)', fontSize: '0.85rem' }}>({p.datePublished})</span></li>
        ))}
      </ul>
      <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginTop: 20 }}>
        <Link href="/methodology/#updates">Review methodology &amp; update log</Link>
      </p>

      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Person',
        name: 'Jerome Tang',
        jobTitle: 'Print Industry Expert & Editor',
        url: 'https://aitoptools.net/author/jerome-tang/',
        worksFor: { '@type': 'Organization', name: config.brand, url: `https://${config.domain}` },
        knowsAbout: ['print on demand', 'AI design tools', 'packaging', 'product photography', 'mockups'],
        sameAs: []
      }) }} />
    </div>
  )
}
