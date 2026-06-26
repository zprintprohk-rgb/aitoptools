import './globals.css'
import Link from 'next/link'

export const metadata = {
  title: { default: 'Print AI Tools — AI Tools for Print Shops & Independent Store Owners', template: '%s | Print AI Tools' },
  description: 'Hands-on reviews of the best AI tools for print shops, packaging design, cross-border e-commerce, and independent store owners. Real screenshots, real tests.',
  metadataBase: new URL('https://aitoptools.net'),
  alternates: { canonical: '/' },
  openGraph: { title: 'Print AI Tools', description: 'AI tools reviewed for print shops and independent store owners.', url: 'https://aitoptools.net', siteName: 'Print AI Tools' },
}

const NAV_CATEGORIES = [
  { name: 'Print & Packaging', href: '/category/ai-print-design/' },
  { name: 'E-Commerce', href: '/category/ai-ecommerce/' },
  { name: 'AI Writing', href: '/category/ai-writing/' },
  { name: 'AI Image', href: '/category/ai-image/' },
  { name: 'AI Video', href: '/category/ai-video/' },
  { name: 'AI Voice', href: '/category/ai-voice/' },
]

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="container header-inner">
            <Link href="/" className="site-logo">
              <span className="logo-icon">🖨️</span>
              <span className="logo-text">Print AI Tools</span>
            </Link>
            <nav className="main-nav">
              {NAV_CATEGORIES.map(cat => (
                <Link key={cat.href} href={cat.href} className="nav-link">{cat.name}</Link>
              ))}
            </nav>
            <button className="mobile-menu-btn" aria-label="Menu">☰</button>
          </div>
        </header>

        <main>{children}</main>

        <footer className="site-footer">
          <div className="container footer-grid">
            <div className="footer-brand">
              <span className="footer-logo">🖨️ Print AI Tools</span>
              <p className="footer-tagline">Helping print shops and independent store owners find the right AI tools.</p>
            </div>
            <div className="footer-nav">
              <h4>Categories</h4>
              {NAV_CATEGORIES.map(cat => (
                <Link key={cat.href} href={cat.href}>{cat.name}</Link>
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
            <p>© {new Date().getFullYear()} Print AI Tools (aitoptools.net). All rights reserved.</p>
            <p className="footer-disclaimer">
              <strong>Independent Operation:</strong> This site is independently operated and is not affiliated with,
              partnered with, or authorized by aitoptools.com. All content is original and focused on AI tools for
              print shops, packaging, cross-border e-commerce, and independent store operations.
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
