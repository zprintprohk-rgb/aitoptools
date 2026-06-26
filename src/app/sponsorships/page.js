export const metadata = {
  title: 'Sponsorships & Advertising',
  description: 'Promote your AI tool to print shop owners, packaging designers, and independent e-commerce sellers. Sponsorship plans for Print AI Tools.',
  alternates: { canonical: 'https://aitoptools.net/sponsorships/' },
}

export default function SponsorshipsPage() {
  return (
    <div className="sponsor-page">
      <h1 style={{ fontSize: '2rem', fontWeight: 700, color: '#1c1917', marginBottom: 8 }}>Sponsorships &amp; Advertising</h1>
      <p style={{ color: '#78716c', marginBottom: 8, fontSize: '1.05rem' }}>
        Get your AI tool in front of print shop owners, packaging designers, and independent e-commerce sellers.
      </p>
      <p style={{ color: '#a8a29e', marginBottom: 28, fontSize: '0.9rem' }}>
        Our audience is niche, targeted, and ready to buy — every visitor is a potential customer for your tool.
      </p>

      <div className="pricing-grid">
        <div className="pricing-card">
          <h3>Standard</h3>
          <div className="price">$199<span>/week</span></div>
          <ul>
            <li>Featured on homepage for 1 week</li>
            <li>Priority listing in category page</li>
            <li>Social media mention</li>
            <li>Standard review page placement</li>
          </ul>
          <a href="/submit-tool/" className="cta-button" style={{ fontSize: '0.9rem', padding: '10px 24px' }}>Get Started</a>
        </div>

        <div className="pricing-card featured">
          <div style={{ color: '#d97706', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: 1, marginBottom: 4 }}>Popular</div>
          <h3>Business</h3>
          <div className="price">$499<span>/week</span></div>
          <ul>
            <li>Everything in Standard, plus:</li>
            <li>Dedicated in-depth review with screenshots</li>
            <li>Full-page sponsored review article</li>
            <li>Featured banner on all category pages</li>
            <li>Email mention to our subscribers</li>
          </ul>
          <a href="/submit-tool/" className="cta-button" style={{ fontSize: '0.9rem', padding: '10px 24px' }}>Get Started</a>
        </div>

        <div className="pricing-card">
          <h3>Enterprise</h3>
          <div className="price">$1,198<span>/month</span></div>
          <ul>
            <li>Everything in Business, plus:</li>
            <li>Priority placement in all relevant categories</li>
            <li>Monthly featured article rotation</li>
            <li>Dedicated tool comparison article</li>
            <li>Social media campaign (3 posts)</li>
            <li>Analytics report (impressions + clicks)</li>
          </ul>
          <a href="/submit-tool/" className="cta-button" style={{ fontSize: '0.9rem', padding: '10px 24px' }}>Contact Us</a>
        </div>
      </div>

      <div className="highlight-box">
        <p><strong>Why advertise with Print AI Tools?</strong> Our visitors are print shop operators, packaging designers, cross-border e-commerce sellers, and independent store owners — a high-intent audience actively looking for tools to grow their businesses. Every click comes from someone who could be your paying customer.</p>
      </div>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>FAQ</h2>

      <h3 style={{ fontSize: '1rem', fontWeight: 600, margin: '20px 0 6px', color: '#292524' }}>How are sponsors displayed?</h3>
      <p>Sponsors appear as featured listings on the homepage, in relevant category pages, and as part of dedicated review articles. Each placement is clearly marked as "Sponsored" or "Featured."</p>

      <h3 style={{ fontSize: '1rem', fontWeight: 600, margin: '20px 0 6px', color: '#292524' }}>Do sponsored reviews get higher ratings?</h3>
      <p>No. Sponsored placement gets your tool visibility, but all reviews — sponsored or not — are based on honest hands-on testing with balanced pros and cons. We never guarantee positive ratings.</p>

      <h3 style={{ fontSize: '1rem', fontWeight: 600, margin: '20px 0 6px', color: '#292524' }}>What categories get the best results?</h3>
      <p>Tools in the print/packaging, e-commerce/Shopify, and product photography categories perform best with our audience since these are our core verticals.</p>

      <h3 style={{ fontSize: '1rem', fontWeight: 600, margin: '20px 0 6px', color: '#292524' }}>Can I sponsor a single article?</h3>
      <p>Yes. The Business plan includes a dedicated sponsored review article. Contact us for custom single-article sponsorship options.</p>
    </div>
  )
}
