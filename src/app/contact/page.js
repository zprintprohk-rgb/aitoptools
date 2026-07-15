export const metadata = {
  title: 'Contact Us',
  description: 'Contact Print AI Tools. For affiliate inquiries, tool submissions, sponsorships, or general questions.',
  alternates: { canonical: 'https://aitoptools.net/contact/' },
}

export default function ContactPage() {
  return (
    <div className="legal-page">
      <h1>Contact Us</h1>
      <p className="meta-date">Last updated: July 15, 2026</p>

      <div className="highlight-box">
        <p><strong>Preferred contact method:</strong> We respond fastest via email or the tool submission form.</p>
      </div>

      <h2>Email</h2>
      <p><a href="mailto:contact@aitoptools.net">contact@aitoptools.net</a></p>

      <h2>Tool Submissions</h2>
      <p>Have an AI tool you want reviewed? Use our <a href="/submit-tool/">submission form</a>.</p>

      <h2>Sponsorships &amp; Advertising</h2>
      <p>Interested in sponsoring a review or advertising on Print AI Tools? See <a href="/sponsorships/">sponsorship options</a> or email us.</p>

      <h2>Affiliate Partnerships</h2>
      <p>Want to join our affiliate program or partner with us? Email <a href="mailto:contact@aitoptools.net">contact@aitoptools.net</a> with details about your program.</p>

      <h2>General Inquiries</h2>
      <p>For anything else, email <a href="mailto:contact@aitoptools.net">contact@aitoptools.net</a>. We aim to respond within 48 hours.</p>
    </div>
  )
}
