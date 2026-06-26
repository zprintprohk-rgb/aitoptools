import Link from 'next/link'

export const metadata = {
  title: 'About Print AI Tools',
  description: 'Print AI Tools is your trusted source for hands-on reviews of AI tools for print shops, packaging design, cross-border e-commerce, and independent store owners.',
  alternates: { canonical: 'https://aitoptools.net/about/' },
}

export default function AboutPage() {
  return (
    <div className="about-page">
      <h1 style={{ fontSize: '2rem', fontWeight: 700, color: '#1c1917', marginBottom: 24 }}>About Print AI Tools</h1>

      <div className="highlight-box">
        <p><strong>Independent Operation:</strong> Print AI Tools (aitoptools.net) is independently operated and is not affiliated with, partnered with, or authorized by aitoptools.com. Our content focuses exclusively on AI tools for print shops, packaging, cross-border e-commerce, and independent store operations.</p>
      </div>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>Our Mission</h2>
      <p>Print AI Tools was created to fill a gap in the AI review space. Most AI tool directories review everything from chatbots to video generators — but nobody specializes in tools for <strong>print shops, packaging design, cross-border e-commerce, and independent store owners</strong>.</p>
      <p>We believe these industries have unique needs that general AI reviews don&apos;t address. A tool that&apos;s great for writing blog posts might be terrible at generating print-ready packaging designs. A video avatar platform might be perfect for social media but useless for product demonstrations in a print catalog.</p>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>Our Approach</h2>
      <ul>
        <li><strong>Hands-on testing:</strong> Every tool is tested with real use cases relevant to print and e-commerce before we write a review.</li>
        <li><strong>Real screenshots:</strong> We capture actual screenshots during testing — no stock images or vendor-provided mockups.</li>
        <li><strong>Honest pros and cons:</strong> Every review includes balanced pros and cons. No tool is perfect, and we tell you why.</li>
        <li><strong>Scenario-focused:</strong> We evaluate tools based on how they perform in real print shop and e-commerce scenarios.</li>
      </ul>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>What We Cover</h2>
      <ul>
        <li>🖨️ <strong>Print &amp; Packaging AI</strong> — Print-on-demand, packaging design, label making, brochure design, print shop workflow automation</li>
        <li>🛒 <strong>E-Commerce &amp; Shopify AI</strong> — Product descriptions, cross-border selling, store optimization, AI for independent store owners</li>
        <li>✍️ <strong>AI Writing</strong> — Copywriting, multilingual content, marketing copy</li>
        <li>🎨 <strong>AI Image</strong> — Image generation, product photography, design</li>
        <li>🎬 <strong>AI Video</strong> — Video creation, avatars, tutorials</li>
        <li>🎙️ <strong>AI Voice</strong> — Voice synthesis, dubbing, audio</li>
      </ul>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>How We Make Money</h2>
      <p>Print AI Tools is supported by affiliate commissions and sponsorships. When you click an affiliate link on our site and make a purchase, we may earn a commission — at no extra cost to you. This allows us to keep producing independent, honest reviews. See our <Link href="/affiliate-disclosure/">Affiliate Disclosure</Link> for details.</p>

      <h2 style={{ fontSize: '1.3rem', fontWeight: 600, margin: '28px 0 10px', color: '#292524' }}>Get in Touch</h2>
      <p>Have an AI tool you think print shop owners or independent store operators should know about? <Link href="/submit-tool/">Submit it for review</Link>.</p>
      <p>Interested in sponsoring a review or getting featured placement? Check out our <Link href="/sponsorships/">sponsorship options</Link>.</p>
    </div>
  )
}
