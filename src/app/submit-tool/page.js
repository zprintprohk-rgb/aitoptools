export const metadata = {
  title: 'Submit Your AI Tool',
  description: 'Submit your AI tool for review on Print AI Tools. We specialize in AI tools for print shops, packaging design, cross-border e-commerce, and independent stores.',
  alternates: { canonical: 'https://aitoptools.net/submit-tool/' },
}

export default function SubmitToolPage() {
  return (
    <div className="submit-page">
      <h1 style={{ fontSize: '2rem', fontWeight: 700, color: '#1c1917', marginBottom: 8 }}>Submit Your AI Tool</h1>
      <p style={{ color: '#78716c', marginBottom: 24 }}>Have an AI tool that serves print shops, packaging designers, e-commerce sellers, or independent store owners? We want to review it.</p>

      <div className="highlight-box">
        <p><strong>Our Focus:</strong> We specialize in AI tools for print-on-demand, packaging design, cross-border e-commerce, Shopify stores, and independent business operations. If your tool helps any of these audiences, we&apos;d love to feature it.</p>
      </div>

      <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>What We Offer</h2>
      <ul>
        <li><strong>Free basic listing</strong> — Your tool gets added to our directory with a brief description and link to your website.</li>
        <li><strong>In-depth review</strong> — Our team tests your tool and publishes a full hands-on review with screenshots, pros/cons, and pricing.</li>
        <li><strong>Featured placement</strong> — Premium placement on category pages and the homepage (see <a href="/sponsorships/">sponsorship options</a>).</li>
      </ul>

      <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>Submission Guidelines</h2>
      <ul>
        <li>Your tool must use AI/ML technology as a core feature</li>
        <li>Your tool should be relevant to print, packaging, e-commerce, or independent business operations</li>
        <li>Provide accurate pricing information (we will update if needed)</li>
        <li>Include high-quality logo and product screenshots</li>
      </ul>

      <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>Currently Accepting Submissions</h2>
      <p>We are actively looking for tools in these categories:</p>
      <ul>
        <li>🖨️ AI print-on-demand &amp; packaging design tools</li>
        <li>🛒 AI e-commerce &amp; Shopify store tools</li>
        <li>🎨 AI product photography &amp; image editing</li>
        <li>✍️ AI multilingual copywriting for cross-border sellers</li>
        <li>📊 AI analytics &amp; store optimization tools</li>
        <li>🎬 AI video creation for product demos &amp; tutorials</li>
      </ul>

      <h2 style={{ fontSize: '1.2rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>How to Submit</h2>
      <p>For now, please reach out through our <a href="/about/">contact page</a> with the following information:</p>
      <ul>
        <li>Tool name and website URL</li>
        <li>Brief description (2-3 sentences)</li>
        <li>Pricing model (free, freemium, paid)</li>
        <li>What print/e-commerce problem it solves</li>
        <li>Affiliate program details (if applicable)</li>
      </ul>

      <p style={{ color: '#a8a29e', fontSize: '0.85rem', marginTop: 32 }}>
        Note: Submission does not guarantee a review. We prioritize tools that are most relevant to our audience of print shop owners and independent store operators.
      </p>
    </div>
  )
}
