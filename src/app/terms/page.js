import Link from 'next/link'

export const metadata = {
  title: 'Terms of Service',
  description: 'Terms of Service for Print AI Tools (aitoptools.net). By using this site, you agree to these terms.',
  alternates: { canonical: 'https://aitoptools.net/terms/' },
}

export default function TermsPage() {
  return (
    <div className="legal-page">
      <h1>Terms of Service</h1>
      <p className="meta-date">Last updated: July 15, 2026</p>

      <h2>Acceptance of Terms</h2>
      <p>By accessing or using Print AI Tools (aitoptools.net), you agree to be bound by these Terms of Service. If you do not agree, please do not use this site.</p>

      <h2>Use of Content</h2>
      <p>All content on this site — including reviews, comparisons, screenshots, and ratings — is for informational purposes only. You may not reproduce, distribute, or create derivative works without our written permission.</p>

      <h2>Affiliate Links &amp; Compensation</h2>
      <p>Print AI Tools participates in affiliate marketing programs. Some links on this site are affiliate links, and we may earn a commission when you make a purchase through these links, at no additional cost to you. This does not influence our reviews or recommendations. See our <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link> for details.</p>

      <h2>User Conduct</h2>
      <p>You agree not to:</p>
      <ul>
        <li>Use automated systems (bots, crawlers) to access the site without permission</li>
        <li>Submit false information through any forms</li>
        <li>Interfere with the site&#39;s operation or security</li>
        <li>Use the site for any illegal purpose</li>
      </ul>

      <h2>Intellectual Property</h2>
      <p>All content, design, and code on Print AI Tools is owned by the site operator unless otherwise credited. Unauthorized use is prohibited.</p>

      <h2>Disclaimer</h2>
      <p>The information on this site is provided &#34;as is&#34; without warranties of any kind. We make no representations about the accuracy, reliability, or completeness of the content. Tool features, pricing, and availability may change without notice.</p>

      <h2>Limitation of Liability</h2>
      <p>Print AI Tools and its operators shall not be liable for any damages arising from the use of this site or reliance on its content.</p>

      <h2>Third-Party Links</h2>
      <p>This site contains links to third-party websites. We are not responsible for the content, privacy practices, or terms of those sites.</p>

      <h2>Changes</h2>
      <p>We reserve the right to update these Terms at any time. Changes will be posted on this page with a revised date.</p>

      <h2>Contact</h2>
      <p>For questions about these Terms, please <Link href="/contact/">contact us</Link>.</p>
    </div>
  )
}
