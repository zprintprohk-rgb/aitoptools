import './globals.css'
import Link from 'next/link'
import config from '@/config'

export const metadata = {
  title: { default: `${config.brand} — ${config.tagline}`, template: `%s | ${config.brand}` },
  description: config.description,
  metadataBase: new URL(`https://${config.domain}`),
  alternates: { canonical: '/' },
  openGraph: {
    title: config.brand,
    description: config.description,
    url: `https://${config.domain}`,
    siteName: config.ogSiteName,
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="container header-inner">
            <Link href="/" className="site-logo">
              <span className="logo-icon">🖨️</span>
              <span className="logo-text">{config.brand}</span>
            </Link>
            <nav className="main-nav">
              {config.categories.map(cat => (
                <Link key={cat.slug} href={`/category/${cat.slug}/`} className="nav-link">
                  {cat.name}
                </Link>
              ))}
            </nav>
            <button className="mobile-menu-btn" aria-label="Menu">☰</button>
          </div>
        </header>

        <main>{children}</main>

        <footer className="site-footer">
          <div className="container footer-grid">
            <div className="footer-brand">
              <span className="footer-logo">🖨️ {config.brand}</span>
              <p className="footer-tagline">{config.footerTagline}</p>
            </div>
            <div className="footer-nav">
              <h4>Categories</h4>
              {config.categories.map(cat => (
                <Link key={cat.slug} href={`/category/${cat.slug}/`}>{cat.name}</Link>
              ))}
            </div>
            <div className="footer-nav">
              <h4>Resources</h4>
              <Link href="/about/">About</Link>
              <Link href="/best-ai-tools/">Best AI Tools</Link>
              <Link href="/submit-tool/">Submit Your Tool</Link>
              <Link href="/sponsorships/">Sponsorships</Link>
            </div>
            <div className="footer-nav">
              <h4>Legal</h4>
              <Link href="/disclaimer/">Disclaimer</Link>
              <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link>
              <Link href="/privacy/">Privacy Policy</Link>
            </div>
          </div>
          <div className="footer-bottom container">
            <p>© {new Date().getFullYear()} {config.brand} ({config.domain}). All rights reserved.</p>
            <p className="footer-disclaimer">
              <strong>Independent Operation:</strong> {config.independentDisclaimer}
            </p>
            <p className="footer-disclosure">
              Some links on this site are affiliate links. We may earn a commission if you purchase through these links,
              at no additional cost to you. See our <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link> for details.
            </p>
          </div>
        </footer>
      </body>
    </html>
  )
}
