import Link from 'next/link'
import WhyTrustUs from '@/components/WhyTrustUs'

export const metadata = {
  title: 'Legit Ratings Methodology — How We Score Tool Trustworthiness (2026)',
  description: 'The exact rubric Print AI Tools uses to score whether a tool is legit: Trustpilot reputation (30%), refund & payment safety (25%), company transparency (25%), and hands-on testing (20%). Updated quarterly.',
  alternates: { canonical: 'https://aitoptools.net/methodology/legit-ratings/' },
}

export default function LegitRatingsMethodologyPage() {
  return (
    <div className="methodology-page">
      <h1>How We Rate Whether a Tool Is Legit</h1>
      <p className="methodology-lede">
        Every &quot;Is [tool] Legit?&quot; page on this site is scored with one public rubric — the
        same weights, the same thresholds, and the same evidence rules for every tool. Here is
        exactly how the score is calculated, where the data comes from, and what we refuse to do.
      </p>

      <section className="methodology-section">
        <h2>The four factors and their weights</h2>
        <div className="methodology-scores">
          <div className="methodology-score-card">
            <h3>Trustpilot reputation — 30%</h3>
            <p>
              Rating (X/5) plus review count plus account activity (new reviews in the last 90 days).
              Every score must link to the live Trustpilot profile. No source URL = 0 points on this
              factor — no exceptions.
            </p>
          </div>
          <div className="methodology-score-card">
            <h3>Refund &amp; payment safety — 25%</h3>
            <p>
              A published refund policy (clear terms and window), buyer-protected payment options
              (card, PayPal, Stripe, Shopify Pay), and no pattern of &quot;charged but no refund&quot;
              complaints. We link the official policy page.
            </p>
          </div>
          <div className="methodology-score-card">
            <h3>Company transparency — 25%</h3>
            <p>
              Public company name, registration number or BBB profile, real address, and a domain
              that is more than 1 year old. A parked or recently transferred domain is a closing
              signal, not a neutral fact.
            </p>
          </div>
          <div className="methodology-score-card">
            <h3>Hands-on testing — 20%</h3>
            <p>
              Our own sign-up, order, or support interaction, with screenshots or an order reference.
              If we have not tested a tool yet, we say so in plain words instead of padding the score.
            </p>
          </div>
        </div>
      </section>

      <section className="methodology-section">
        <h2>Scoring scale (0–2 per factor)</h2>
        <ul>
          <li>
            <strong>2 points:</strong> rating ≥ 4.0 with 500+ reviews and active in the last 90 days
            (Trustpilot); clear refund policy with buyer protection and no complaint cluster
            (refunds); full public company details with a 3+ year domain (transparency); a real
            test record we can reproduce (hands-on).
          </li>
          <li>
            <strong>1 point:</strong> rating 3.0–3.9, or 50–499 reviews, or a high rating with a thin
            review base; a vague or store-credit-only refund policy; partial company info or a
            1–3 year domain; second-hand evidence with a source (no first-party test).
          </li>
          <li>
            <strong>0 points:</strong> rating below 3.0, fewer than 50 reviews, no Trustpilot
            profile, or a concentrated negative-complaint storm; no refund policy, no support
            channel, or irreversible payment only; fully anonymous, sub-1-year domain, or a
            parked/transferred domain; no test and no sourced evidence.
          </li>
        </ul>
        <p className="methodology-note">
          A missing Trustpilot profile is not the same as &quot;scam&quot; — we state it as a
          signal and let the other three factors carry the score. &quot;Not Operating&quot;
          (domain parked, store closed) is its own special verdict, not a 0.
        </p>
      </section>

      <section className="methodology-section">
        <h2>Final score formula</h2>
        <p>
          Each factor is scored 0–2, multiplied by its weight, and scaled to 100:
        </p>
        <p className="methodology-note">
          <strong>Score = (Trustpilot × 0.30 + Refund × 0.25 + Transparency × 0.25 + Testing × 0.20) × 50</strong>
        </p>
        <ul>
          <li><strong>≥ 80</strong> — Recommended. We are comfortable sending readers to this tool.</li>
          <li><strong>60–79</strong> — Conditional. Works, but with caveats we spell out.</li>
          <li><strong>&lt; 60</strong> — Not Recommended. We say why, with evidence.</li>
        </ul>
      </section>

      <section className="methodology-section">
        <h2>Where the data comes from</h2>
        <ul>
          <li>
            <strong>Trustpilot profiles</strong> — linked live, with the rating and review count as
            shown on the profile page at the time of writing (date noted on each page).
          </li>
          <li>
            <strong>Official refund policies</strong> — the vendor&apos;s own page, quoted directly.
          </li>
          <li>
            <strong>BBB profiles and company registries</strong> — linked where they exist; &quot;no
            BBB profile&quot; is stated as a fact, not assumed to be a failure.
          </li>
          <li>
            <strong>Our own test records</strong> — screenshots, order references, and support-ticket
            summaries. Anything second-hand carries a source URL.
          </li>
        </ul>
        <p className="methodology-note">
          Rule: no source URL, no score. Every number on a legit page traces back to a linked source
          or an explicit &quot;we have not tested this yet&quot; statement.
        </p>
      </section>

      <section className="methodology-section">
        <h2>Update frequency</h2>
        <p>
          Rubric weights are reviewed quarterly. Individual tool scores are re-checked when a
          Trustpilot profile moves materially (rating or review count), when a refund policy
          changes, or when we complete a new hands-on test. Each legit page shows its last
          verified date.
        </p>
      </section>

      <section className="methodology-section">
        <h2>Limitations we admit</h2>
        <ul>
          <li>
            Trustpilot data is a snapshot in time — a profile can change after we publish. We
            re-verify quarterly.
          </li>
          <li>
            Hands-on testing covers one order flow, not every edge case a vendor has.
          </li>
          <li>
            A high score is &quot;legit enough to consider&quot;, not a guarantee against future
            problems. We update pages when evidence changes.
          </li>
        </ul>
      </section>

      <section className="methodology-section">
        <h2>Affiliate disclosure</h2>
        <p>
          Some links on this site are affiliate links (we may earn a commission at no extra cost to
          you). Commissions never affect a legit score: the rubric above is applied the same way to
          tools we promote and tools we don&apos;t. Our Spocket review, for example, scores
          52.5/100 (Not Recommended) and stays that way with both sides of the evidence shown.
        </p>
      </section>

      <section className="methodology-section">
        <h2>See it in action</h2>
        <ul>
          <li><Link href="/blog/is-magicdrop-legit">Is MagicDrop Legit?</Link> — our first Branch-A page (score after platform closure)</li>
          <li><Link href="/blog/is-gearlaunch-legit">Is GearLaunch Legit?</Link> — pilot page, 2,562 words</li>
          <li><Link href="/blog/is-spocket-legit">Is Spocket Legit?</Link> — 52.5/100, Not Recommended, with both sources shown</li>
        </ul>
      </section>

      <WhyTrustUs />
    </div>
  )
}
