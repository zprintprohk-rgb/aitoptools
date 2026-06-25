import './globals.css'

export const metadata = {
  title: { default: 'AI Tool Reviews 2026 - Honest & In-Depth Reviews', template: '%s | AI Tool Reviews' },
  description: 'Honest and in-depth reviews of the best AI tools in 2026. Find the perfect AI writing, video, voice, and productivity tools for your needs.',
  openGraph: { title: 'AI Tool Reviews 2026', description: 'Honest reviews of the best AI tools.' },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header className="header">
          <div className="container header-inner">
            <a href="/" className="logo">AI Tool Reviews</a>
            <nav>
              <a href="/">Home</a>
            </nav>
          </div>
        </header>
        <main className="container">{children}</main>
        <footer className="footer">
          <div className="container">
            <p>© 2026 AI Tool Reviews. Honest, independent reviews. Some links are affiliate links.</p>
          </div>
        </footer>
      </body>
    </html>
  )
}
