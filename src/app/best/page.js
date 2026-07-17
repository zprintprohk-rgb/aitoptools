import Link from 'next/link'
import listicles from '@/data/listicles.json'

export const metadata = {
  title: 'Best Of Lists — Ranked AI & POD Tool Roundups',
  description: 'Ranked roundups of the best print-on-demand platforms and AI tools: best Printful alternatives, best tools for Etsy sellers, and more — tested and ranked by print industry professionals.',
  alternates: { canonical: 'https://aitoptools.net/best/' },
  openGraph: {
    title: 'Best Of Lists — Print AI Tools',
    description: 'Ranked roundups of the best print-on-demand platforms and AI tools.',
    url: 'https://aitoptools.net/best/',
    type: 'website',
  },
}

export default function BestIndex() {
  const jsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: 'Best Of Lists',
    description: 'Ranked roundups of print-on-demand platforms and AI tools.',
    url: 'https://aitoptools.net/best/',
    hasPart: listicles.map(l => ({
      '@type': 'Article',
      headline: l.title,
      url: `https://aitoptools.net/best/${l.slug}/`,
    })),
  })

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: jsonLd }} />

      <div className="page-title">
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <span className="current">Best Of</span>
        </nav>
        <h1>🏆 Best Of Lists</h1>
        <p style={{ color: 'var(--k-tertiary)', fontSize: '0.95rem', maxWidth: 640 }}>
          Ranked roundups with clear winners. Every list is built from verified 2026 pricing, hands-on reviews, and real seller scenarios — no pay-to-rank placements.
        </p>
      </div>

      <div className="best-grid">
        {listicles.map(l => (
          <article key={l.slug} className="best-card">
            <span className="best-card-count">{l.items.length} ranked</span>
            <h2 className="best-card-title"><Link href={`/best/${l.slug}/`}>{l.title}</Link></h2>
            <p className="best-card-desc">{l.metaDesc}</p>
            <div className="best-card-names">
              {l.items.slice(0, 4).map((it, i) => (
                <span key={i} className="best-card-name">#{i + 1} {it.name}</span>
              ))}
              {l.items.length > 4 && <span className="best-card-name more">+{l.items.length - 4} more</span>}
            </div>
            <Link href={`/best/${l.slug}/`} className="card-cta">See the Rankings →</Link>
          </article>
        ))}
      </div>

      <div className="aff-disc" style={{ marginTop: 32 }}>
        <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
      </div>
    </>
  )
}
