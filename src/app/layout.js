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
              {/* Core vertical — always first */}
              <Link href="/category/ai-print-design/" className="nav-link">🖨️ Print &amp; Packaging</Link>
              <Link href="/category/ai-ecommerce/" className="nav-link">🛒 E-Commerce</Link>
              <span className="nav-divider" aria-hidden="true" />
              {/* General categories — visually de-emphasized */}
              <Link href="/category/ai-writing/" className="nav-link nav-secondary">Writing</Link>
              <Link href="/category/ai-image/" className="nav-link nav-secondary">Image</Link>
              <Link href="/category/ai-video/" className="nav-link nav-secondary">Video</Link>
              <Link href="/category/ai-voice/" className="nav-link nav-secondary">Voice</Link>
              <span className="nav-divider" aria-hidden="true" />
              <Link href="/submit-tool/" className="nav-link">Submit</Link>
              <Link href="/sponsorships/" className="nav-link">Ads</Link>
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
              <Link href="/category/ai-print-design/">🖨️ Print &amp; Packaging</Link>
              <Link href="/category/ai-ecommerce/">🛒 E-Commerce &amp; Shopify</Link>
              <Link href="/category/ai-writing/">✍️ AI Writing</Link>
              <Link href="/category/ai-image/">🎨 AI Image</Link>
              <Link href="/category/ai-video/">🎬 AI Video</Link>
              <Link href="/category/ai-voice/">🎙️ AI Voice</Link>
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
            <p className="footer-disclaimer">
              <strong>Independent Operation:</strong> {config.brand} (aitoptools.net) is <strong>independently operated</strong> and is <strong>not affiliated with, partnered with, or authorized by</strong> aitoptools.com. All content is original and focused on AI tools for print shops, packaging, cross-border e-commerce, and independent store operations.
            </p>
            <p className="footer-disclosure">
              Some links on this site are affiliate links. We may earn a commission if you purchase through these links,
              at no additional cost to you. See our <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link> for details.
            </p>
            <p>© {new Date().getFullYear()} {config.brand} ({config.domain}). All rights reserved.</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
