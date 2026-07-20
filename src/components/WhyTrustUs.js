import Link from 'next/link'

/**
 * Reusable editorial-integrity module. One copy, used site-wide.
 */
export default function WhyTrustUs() {
  return (
    <section className="why-trust" aria-label="Why you can trust us">
      <h2 className="why-trust-title">Why You Can Trust Us</h2>
      <ul className="why-trust-list">
        <li><strong>Hands-on tested.</strong> Every tool we rank is used by our team of print industry professionals before we write a word.</li>
        <li><strong>2026 pricing verified.</strong> All prices, plan limits, and library figures on this page are checked against current 2026 sources and updated when vendors change them.</li>
        <li><strong>Independent, never sponsored.</strong> No vendor pays for rankings, ratings, or placement. Some links are affiliate links — if you buy through them we may earn a commission at no extra cost to you. See our <Link href="/affiliate-disclosure/">affiliate disclosure</Link>.</li>
      </ul>
    </section>
  )
}
