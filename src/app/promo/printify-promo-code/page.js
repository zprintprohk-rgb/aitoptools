import Link from 'next/link'
import { buildAffLinkAttrs } from '@/lib/affiliate'

export const metadata = {
  title: 'Printify Promo Code AITOOLTOOLS20: 20% Off Your First Order (2026)',
  description: 'Verified Printify promo code AITOOLTOOLS20 gives new sellers 20% off their first order (confirmed by Printify support, 8/24/2026). Apply it at checkout and sign up through our affiliate link to support this site for free.',
  alternates: { canonical: 'https://aitoptools.net/promo/printify-promo-code/' },
  openGraph: {
    title: 'Printify Promo Code AITOOLTOOLS20: 20% Off Your First Order (2026)',
    description: 'Verified Printify promo code AITOOLTOOLS20 gives new sellers 20% off their first order (confirmed by Printify support, 8/24/2026).',
    url: 'https://aitoptools.net/promo/printify-promo-code/',
    type: 'website',
    siteName: 'Print AI Tools',
  },
}

const PROMO_CODE = 'AITOOLTOOLS20'
const AFFILIATE_URL = 'https://try.printify.com/4fs863rfz2yc'

function buildCta() {
  return buildAffLinkAttrs({ slug: 'printify-promo-code', affiliateUrl: AFFILIATE_URL }, 'promo-cta')
}

const FAQS = [
  {
    q: 'Is AITOOLTOOLS20 a working Printify promo code?',
    a: 'Yes. AITOOLTOOLS20 was created by Printify\u2019s affiliate team on August 24, 2026, confirmed directly by email from affiliate@printify.com. It is a real, active code for new accounts \u2014 not a placeholder or an expired deal.',
  },
  {
    q: 'How much does the AITOOLTOOLS20 promo code save me?',
    a: 'It gives new Printify accounts 20% off their first order. Because it is a first-order code, the exact dollar amount depends on what you order, but on a typical $100 order you would save about $20.',
  },
  {
    q: 'Why do I need to sign up through an affiliate link if I already have the promo code?',
    a: 'Printify\u2019s affiliate team confirmed that promo codes are not commission-trackable \u2014 using the code alone does not credit the site that gave it to you. If you sign up through our affiliate link first (free, no downside), your order still earns a small commission that supports this site, and you can still apply AITOOLTOOLS20 at checkout for the discount.',
  },
  {
    q: 'Can existing Printify accounts use this promo code?',
    a: 'No. The code is for new or not-yet-activated accounts only, per Printify\u2019s confirmation. If you already have a Printify account with an active plan, this code will not apply to your checkout.',
  },
]

const RELATED = [
  { href: '/printify-review/', label: 'Printify Review 2026', desc: 'full hands-on review: catalog, pricing, margins, and mockup tools' },
  { href: '/compare/printful-vs-printify/', label: 'Printful vs Printify (2026)', desc: 'head-to-head pricing, quality, and shipping tested side by side' },
  { href: '/best/printify-alternatives/', label: 'Best Printify Alternatives', desc: 'cheaper and faster POD platform options, ranked' },
  { href: '/blog/printful-vs-printify-2026/', label: 'Printful vs Printify blog deep-dive', desc: 'the long-form version with real order numbers' },
]

export default function PromoPage() {
  const cta = buildCta()
  const faqJsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: FAQS.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
  })
  const breadcrumbJsonLd = JSON.stringify({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://aitoptools.net/' },
      { '@type': 'ListItem', position: 2, name: 'Printify Review', item: 'https://aitoptools.net/printify-review/' },
      { '@type': 'ListItem', position: 3, name: 'Printify Promo Code AITOOLTOOLS20', item: 'https://aitoptools.net/promo/printify-promo-code/' },
    ],
  })

  return (
    <div className="promo-page container" style={{ maxWidth: 780, margin: '0 auto', padding: '32px 0 64px' }}>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: faqJsonLd }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: breadcrumbJsonLd }} />

      <nav className="breadcrumb" aria-label="Breadcrumb">
        <Link href="/">Home</Link>
        <span className="sep">&rsaquo;</span>
        <Link href="/printify-review/">Printify Review</Link>
        <span className="sep">&rsaquo;</span>
        <span className="current">Promo Code</span>
      </nav>

      <h1>Printify Promo Code AITOOLTOOLS20: 20% Off Your First Order (2026)</h1>

      <p style={{ fontSize: '1.02rem', lineHeight: 1.7 }}>
        <strong>AITOOLTOOLS20 is a working Printify promo code</strong> &mdash; confirmed by Printify&apos;s affiliate
        team on August 24, 2026. New accounts get <strong>20% off their first order</strong> when they enter the code
        at checkout. One catch worth knowing: the code itself is not commission-trackable, so to support this site for
        free, sign up through our <a href={AFFILIATE_URL} target="_blank" rel="nofollow sponsored">Printify affiliate
        link</a> first, then apply the code at checkout.
      </p>

      <div style={{ background: 'var(--y-bg, #fdf6e3)', border: '1px solid rgba(180,140,20,0.3)', borderRadius: 12, padding: '20px 24px', margin: '24px 0' }}>
        <div style={{ fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '1px', color: 'var(--k-tertiary)', marginBottom: 8 }}>
          Your Printify promo code
        </div>
        <div style={{ fontSize: '1.6rem', fontWeight: 800, letterSpacing: '2px', fontFamily: 'monospace', color: 'var(--k-deep)' }}>
          {PROMO_CODE}
        </div>
        <div style={{ fontSize: '0.9rem', color: 'var(--k-secondary)', marginTop: 6 }}>
          20% off your first order &middot; for new Printify accounts &middot; verified 8/24/2026
        </div>
      </div>

      <h2>How to use the AITOOLTOOLS20 promo code (3 steps)</h2>
      <ol style={{ lineHeight: 1.8, paddingLeft: 22 }}>
        <li><strong>Sign up through our Printify affiliate link</strong> (free, no downside):{' '}
          <a href={AFFILIATE_URL} target="_blank" rel="nofollow sponsored">try.printify.com/4fs863rfz2yc</a>. This is how
          the site earns a commission &mdash; the promo code alone is not trackable.</li>
        <li><strong>Create your first product and go to checkout</strong>. If you are a new account, you will see a
          promo-code box before you pay.</li>
        <li><strong>Enter {PROMO_CODE} and apply</strong>. Your first-order total drops by 20% before you confirm the order.</li>
      </ol>

      <h2>What does the AITOOLTOOLS20 promo code save you?</h2>
      <p>
        The code gives new Printify accounts <strong>20% off their first order</strong>. On a typical starter order of
        five sample products (roughly $60&ndash;$120 depending on the product), that is about <strong>$12&ndash;$24
        back</strong>. Printify&apos;s base prices are already among the lowest in print-on-demand (a Bella+Canvas 3001
        tee starts around $4.45 with the right provider), so the discount lands on top of an already-thin margin.
      </p>

      <h2>Why sign up through the affiliate link if I already have the code?</h2>
      <p>
        Printify&apos;s affiliate team confirmed that promo codes are <strong>not commission-trackable</strong>.
        If you type the code in on its own, whoever shared it gets no credit. Signing up through our affiliate link
        (same price, same products, no extra cost to you) lets your order support this site &mdash; and you can still
        apply {PROMO_CODE} at checkout for the 20% off. Best of both worlds.
      </p>

      <h2>Who can use the AITOOLTOOLS20 promo code?</h2>
      <p>
        Per Printify&apos;s confirmation, the code is for <strong>new or not-yet-activated accounts</strong>.
        If you already have a Printify account with an active plan, the code will not apply. If you are brand new to
        Printify &mdash; or signed up but never activated a plan &mdash; you are eligible.
      </p>

      <div className="cta-box">
        <p>Ready to try Printify with 20% off your first order?</p>
        <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginBottom: 12 }}>
          Click below to sign up through our affiliate link, then enter {PROMO_CODE} at checkout. If you purchase
          through our link, we may earn a commission at no extra cost to you.
        </p>
        {cta ? (
          <a
            href={cta.href}
            className={`${cta.className} cta-button`}
            data-merchant={cta['data-merchant']}
            data-link-id={cta['data-link-id']}
            data-target={cta['data-target']}
            target="_blank"
            rel="nofollow sponsored"
          >
            Get 20% Off Your First Order &rarr;
          </a>
        ) : (
          <a href={AFFILIATE_URL} target="_blank" rel="nofollow sponsored" className="cta-button">
            Get 20% Off Your First Order &rarr;
          </a>
        )}
      </div>

      <div className="faq-section">
        <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 16, color: 'var(--k-deep)' }}>Frequently Asked Questions</h2>
        {FAQS.map((faq, i) => (
          <details key={i} className="faq-item">
            <summary className="faq-question">{faq.q}</summary>
            <div className="faq-answer"><p>{faq.a}</p></div>
          </details>
        ))}
      </div>

      <div className="related-links" style={{ marginTop: 36 }}>
        <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>Related Reads</h2>
        <ul style={{ fontSize: '0.95rem', lineHeight: 1.8, paddingLeft: 20 }}>
          {RELATED.map((r) => (
            <li key={r.href}><Link href={r.href}>{r.label}</Link> &mdash; {r.desc}.</li>
          ))}
        </ul>
      </div>

      <div className="aff-disc">
        <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if
        you make a purchase through these links, at no additional cost to you. The AITOOLTOOLS20 promo code was
        confirmed by Printify&apos;s affiliate team on 8/24/2026. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
      </div>
    </div>
  )
}
