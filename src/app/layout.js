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
    type: 'website',
    images: [{ url: '/og-image.png', width: 1200, height: 630, alt: `${config.brand} — ${config.tagline}` }],
  },
  twitter: {
    card: 'summary_large_image',
    title: config.brand,
    description: config.description,
    images: ['/og-image.png'],
  },
  other: {
    'impact-site-verification': 'a6e51cad-9e2c-472d-8743-47da5b391774',
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              '@context': 'https://schema.org',
              '@type': 'Organization',
              name: config.brand,
              url: `https://${config.domain}`,
              logo: `https://${config.domain}/og-image.png`,
              description: config.description,
            }),
          }}
        />
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
              <Link href="/compare/" className="nav-link">⚖️ Comparisons</Link>
              <Link href="/best/" className="nav-link">🏆 Best Of</Link>
              <Link href="/#search" className="nav-search-icon" aria-label="Search tools">🔍</Link>
              <Link href="/submit-tool/" className="nav-cta">Submit</Link>
            </nav>
            <details className="mobile-nav">
              <summary className="mobile-menu-btn" aria-label="Open menu">☰</summary>
              <nav className="mobile-nav-panel" aria-label="Mobile">
                <Link href="/category/ai-print-design/">🖨️ Print &amp; Packaging</Link>
                <Link href="/category/ai-ecommerce/">🛒 E-Commerce &amp; Shopify</Link>
                <Link href="/category/ai-writing/">✍️ AI Writing</Link>
                <Link href="/category/ai-image/">🎨 AI Image</Link>
                <Link href="/category/ai-video/">🎬 AI Video</Link>
                <Link href="/category/ai-voice/">🎙️ AI Voice</Link>
                <Link href="/compare/">⚖️ Comparisons</Link>
                <Link href="/best/">🏆 Best Of</Link>
                <Link href="/submit-tool/" className="mobile-nav-cta">Submit Your Tool</Link>
              </nav>
            </details>
          </div>
          <div className="trust-bar">
            <div className="container trust-bar-inner">
              <span>✓ Hands-On Tested</span>
              <span className="trust-dot" aria-hidden="true">·</span>
              <span>✓ 74+ Tools Reviewed</span>
              <span className="trust-dot" aria-hidden="true">·</span>
              <span>✓ Independent Reviews</span>
              <span className="trust-dot" aria-hidden="true">·</span>
              <span>✓ Updated July 2026</span>
            </div>
          </div>
        </header>

        <main className="main-content container">
          {children}
        </main>

        <footer className="site-footer">
          <div className="container">
            <div className="footer-grid">
              <div className="footer-brand">
                <span className="footer-logo"><span className="logo-icon">🖨️</span> {config.brand}</span>
                <p className="footer-tagline">Hands-on AI tool reviews for print shops and independent store owners — tested, compared, and ranked by industry professionals.</p>
                <div className="footer-badges">
                  <span className="footer-badge">✓ Hands-On Tested</span>
                  <span className="footer-badge">✓ 74+ Tools Reviewed</span>
                  <span className="footer-badge">✓ Independent &amp; Unbiased</span>
                </div>
              </div>
              <div className="footer-nav">
                <h4>Categories</h4>
                <Link href="/category/ai-print-design/">Print &amp; Packaging</Link>
                <Link href="/category/ai-ecommerce/">E-Commerce &amp; Shopify</Link>
                <Link href="/category/ai-writing/">AI Writing</Link>
                <Link href="/category/ai-image/">AI Image</Link>
                <Link href="/category/ai-video/">AI Video</Link>
                <Link href="/category/ai-voice/">AI Voice</Link>
              </div>
              <div className="footer-nav">
                <h4>Content</h4>
                <Link href="/compare/">Comparisons</Link>
                <Link href="/best/">Best Of</Link>
                <Link href="/best-ai-tools/">All Reviews</Link>
                <Link href="/submit-tool/">Submit Your Tool</Link>
              </div>
              <div className="footer-nav">
                <h4>Resources</h4>
                <Link href="/about/">About</Link>
                <Link href="/contact/">Contact</Link>
                <Link href="/sponsorships/">Advertise</Link>
                <Link href="/sponsorships/">Sponsorships</Link>
              </div>
            </div>
            <p className="footer-disclaimer">
              <strong>Independent Operation:</strong> {config.brand} (aitoptools.net) is <strong>independently operated</strong> and is <strong>not affiliated with, partnered with, or authorized by</strong> aitoptools.com. All content is original and focused on AI tools for print shops, packaging, cross-border e-commerce, and independent store operations.
            </p>
            <p className="footer-disclaimer">
              <strong>Operated by:</strong> {config.brand} is published by Jerome Tang (trade name ZPrintPro), a digital project of Shenzhen Cai Long Printing &amp; Packaging Co., Ltd. — <a href="https://www.linkedin.com/in/jerome-tang-442ab8424" target="_blank" rel="noopener noreferrer" style={{ color: 'inherit', textDecoration: 'underline' }}>LinkedIn</a> · <a href="mailto:zprintprohk@gmail.com" style={{ color: 'inherit', textDecoration: 'underline' }}>zprintprohk@gmail.com</a>
            </p>
            <div className="footer-legal">
              <p className="footer-copy">© {new Date().getFullYear()} {config.brand} ({config.domain}). All rights reserved. We may earn commissions from links on this site.</p>
              <nav className="footer-legal-links" aria-label="Legal">
                <Link href="/disclaimer/">Disclaimer</Link>
                <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link>
                <Link href="/privacy/">Privacy Policy</Link>
                <Link href="/terms/">Terms of Service</Link>
              </nav>
            </div>
            <p className="footer-copy" style={{ marginTop: 8, opacity: 0.6 }}>Photos: Openverse (CC0 / public domain).</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
