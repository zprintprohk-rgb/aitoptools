import Link from 'next/link'

export const metadata = {
  title: 'Disclaimer',
  description: 'Independent operation disclaimer for Print AI Tools (aitoptools.net).',
  alternates: { canonical: 'https://aitoptools.net/disclaimer/' },
}

export default function DisclaimerPage() {
  return (
    <div className="legal-page">
      <h1>Disclaimer</h1>

      <div className="highlight-box">
        <p><strong>Independent Operation:</strong> Print AI Tools (aitoptools.net) is independently operated and is <strong>not affiliated with, partnered with, or authorized by</strong> aitoptools.com or any other AI tool directory. All content on this site is original and focused on AI tools for print shops, packaging, cross-border e-commerce, and independent store operations.</p>
      </div>

      <h2>No Affiliation</h2>
      <p>Print AI Tools (accessible at aitoptools.net) is an independent website that provides reviews and comparisons of AI tools for the print and e-commerce industries. We are not officially associated with, endorsed by, or in any way connected to aitoptools.com, its owners, or its affiliates.</p>
      <p>Any similarity in domain naming is coincidental. Our content, focus, and target audience are distinctly different — we specialize in AI tools for print shops, packaging design, and cross-border e-commerce, while aitoptools.com covers general-purpose AI tools across all categories.</p>

      <h2>Content Originality</h2>
      <p>All reviews, comparisons, screenshots, and editorial content on this site are produced independently. We do not copy, translate, or repurpose content from other websites. Our reviews are based on hands-on testing and original research.</p>

      <h2>No Professional Advice</h2>
      <p>The information provided on this website is for general informational and educational purposes only. It is not intended as professional, legal, financial, or technical advice. You should consult with appropriate professionals before making any decisions based on the content found here.</p>

      <h2>Limitation of Liability</h2>
      <p>Print AI Tools makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the information, products, services, or related graphics contained on the website for any purpose. Any reliance you place on such information is strictly at your own risk.</p>

      <h2>External Links</h2>
      <p>This site contains affiliate links to third-party websites. We may earn a commission if you make a purchase through these links, at no additional cost to you. See our <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link> for details. We are not responsible for the content, privacy practices, or terms of any linked third-party websites.</p>

      <h2>Contact</h2>
      <p>If you have any questions about this disclaimer, please <Link href="/about/">contact us</Link>.</p>

      <p style={{ marginTop: 32, color: '#a8a29e', fontSize: '0.85rem' }}>Last updated: June 26, 2026</p>
    </div>
  )
}
