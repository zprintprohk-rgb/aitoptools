import Link from 'next/link'
import comparisons from '@/data/comparisons.json'
import WinnerBadge from '@/components/WinnerBadge'

export const metadata = {
  title: 'Tool Comparisons — Head-to-Head AI & POD Platform Showdowns',
  description: 'Side-by-side comparisons of the top print-on-demand platforms and AI tools: pricing, quality, shipping, and honest verdicts on which tool wins for your store.',
  alternates: { canonical: 'https://aitoptools.net/compare/' },
  openGraph: {
    title: 'Tool Comparisons — Print AI Tools',
    description: 'Side-by-side comparisons of the top print-on-demand platforms and AI tools.',
    url: 'https://aitoptools.net/compare/',
    type: 'website',
  },
}

export default function CompareIndex() {
  const jsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: 'Tool Comparisons',
    description: 'Side-by-side comparisons of print-on-demand platforms and AI tools.',
    url: 'https://aitoptools.net/compare/',
    hasPart: comparisons.map(c => ({
      '@type': 'Article',
      headline: c.title,
      url: `https://aitoptools.net/compare/${c.slug}/`,
    })),
  })

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: jsonLd }} />

      <div className="page-title">
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <span className="current">Comparisons</span>
        </nav>
        <h1>⚖️ Head-to-Head Tool Comparisons</h1>
        <p style={{ color: 'var(--k-tertiary)', fontSize: '0.95rem', maxWidth: 640 }}>
          No fence-sitting. Each comparison ends with a clear verdict on which tool wins — backed by verified 2026 pricing, real cost math, and scenario-based recommendations.
        </p>
      </div>

      <div className="vs-grid">
        {comparisons.map(c => (
          <article key={c.slug} className="vs-card">
            <div className="vs-card-battle">
              <div className="vs-side">
                <span className="vs-name">{c.toolA.name}</span>
                <span className="vs-rating">★ {c.toolA.rating}</span>
              </div>
              <span className="vs-badge">VS</span>
              <div className="vs-side">
                <span className="vs-name">{c.toolB.name}</span>
                <span className="vs-rating">★ {c.toolB.rating}</span>
              </div>
            </div>
            <h2 className="vs-title">
              <Link href={`/compare/${c.slug}/`}>{c.title}</Link>
              {c.picks?.find(p => p.type === 'top') && (
                <WinnerBadge label={c.picks.find(p => p.type === 'top').name} />
              )}
            </h2>
            <p className="vs-verdict">{c.quickVerdict.split('.')[0]}.</p>
            <Link href={`/compare/${c.slug}/`} className="card-cta">Read Comparison →</Link>
          </article>
        ))}
      </div>

      <div className="aff-disc" style={{ marginTop: 32 }}>
        <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
      </div>
    </>
  )
}
