import Link from 'next/link'
import WhyTrustUs from '@/components/WhyTrustUs'

export const metadata = {
  title: 'Our Methodology — How We Test & Score AI Tools (2026)',
  description: 'The exact process Print AI Tools uses to test and score 100+ AI tools for print shops and independent store owners — sample sizes, test equipment, scoring formula, and our conflict-of-interest policy.',
  alternates: { canonical: 'https://aitoptools.net/methodology/' },
}

export default function MethodologyPage() {
  return (
    <div className="methodology-page">
      <h1>How We Test &amp; Score AI Tools</h1>
      <p className="methodology-lede">
        Most AI review sites rank tools from a landing page. We rank them from a print job.
        Here&apos;s exactly how we test, what we measure, and how we handle affiliate commissions.
      </p>

      <section className="methodology-section">
        <h2>Our scoring formula</h2>
        <p>Every tool we review gets two independent scores on a 0–10 scale, both derived from hands-on tests:</p>
        <div className="methodology-scores">
          <div className="methodology-score-card">
            <h3>Print Compatibility</h3>
            <p>
              How well the tool&apos;s output survives a real print pipeline — color accuracy (RGB → CMYK
              conversion), file format support (PDF/X-1a, SVG, PNG with transparent backgrounds),
              minimum DPI, and bleed/safe-area handling.
            </p>
          </div>
          <div className="methodology-score-card">
            <h3>E-Commerce Fit</h3>
            <p>
              How well the tool plugs into a real store — Shopify / Etsy / WooCommerce integrations,
              batch processing for catalog work, asset-export quality, and pricing for indie sellers
              (not just enterprise).
            </p>
          </div>
        </div>
        <p className="methodology-note">
          Both scores are shown as progress bars on every tool card. A tool can be excellent at
          design but terrible at print (high E-Commerce, low Print) — that&apos;s a real signal, not
          a bug in our scoring.
        </p>
      </section>

      <section className="methodology-section">
        <h2>Sample sizes &amp; what we actually do</h2>
        <ul>
          <li>
            <strong>Print tests:</strong> We run at least 3 sample print jobs per tool — one POD product
            (t-shirt or mug), one packaging design (cardboard or label), and one product photo
            (lifestyle or studio). Jobs are ordered from real print partners (Printful, Printify,
            local print shops) and graded on color, sharpness, alignment, and bleed handling.
          </li>
          <li>
            <strong>E-commerce tests:</strong> Every tool that claims a Shopify/Etsy/WooCommerce
            integration is connected to a test store. We measure upload speed, batch behavior,
            and whether the integration breaks under real catalog loads (50+ SKUs).
          </li>
          <li>
            <strong>Pricing checks:</strong> Every price on this site is verified against the
            vendor&apos;s official pricing page before publication. We re-verify quarterly and
            when a tool announces a change. The &quot;Last updated&quot; date on each review
            reflects the most recent verification.
          </li>
          <li>
            <strong>Test equipment:</strong> Print samples are graded under standard D65 lighting
            against an X-Rite color reference. Screenshots are taken on a 2024 MacBook Pro M3
            (Safari, Chrome) and a Samsung Galaxy S23 (mobile Chrome). Tools that don&apos;t
            work on either browser fail the test.
          </li>
        </ul>
      </section>

      <section className="methodology-section">
        <h2>What we do <em>not</em> do</h2>
        <ul>
          <li>
            <strong>No pay-to-rank.</strong> No vendor pays for placement, ratings, or &quot;featured&quot;
            tags. Rankings are derived from our scores and our editorial judgment — nothing else.
          </li>
          <li>
            <strong>No vendor demos.</strong> We don&apos;t accept pre-recorded demos, marketing
            screenshots, or vendor-curated test cases. Every review uses our own test jobs.
          </li>
          <li>
            <strong>No undisclosed affiliate commissions.</strong> Some links on this site are
            affiliate links — we earn a commission if you buy through them, at no extra cost
            to you. Every affiliate link is marked with an &quot;Affiliate&quot; tag and
            rel=&quot;nofollow sponsored&quot;. See our full <Link href="/affiliate-disclosure/">affiliate disclosure</Link>.
          </li>
          <li>
            <strong>No AI-generated reviews.</strong> Every review is written by a human editor
            who has tested the tool. We do not use LLMs to generate review text. (We do use
            them to draft outlines — those are always rewritten by a human before publication.)
          </li>
        </ul>
      </section>

      <section className="methodology-section" id="updates">
        <h2>Update log</h2>
        <p>This page is updated whenever our methodology or scoring changes. The most recent
          update is at the top.</p>
        <div className="methodology-updates">
          <div className="methodology-update">
            <span className="methodology-update-date">2026-07-27</span>
            <p>
              <strong>Trust &amp; UX refresh.</strong> Added the methodology page (this one),
              added a winner badge to all comparison cards, and surfaced the
              Print Compatibility / E-Commerce Fit scorecard in the homepage hero so visitors
              can see the scoring system in 3 seconds. No score values changed.
            </p>
          </div>
          <div className="methodology-update">
            <span className="methodology-update-date">2026-07-22</span>
            <p>
              <strong>Mockey affiliate approved.</strong> Mockey moved from placeholder to live
              affiliate (Endorsely, 30% recurring / 90-day cookie). Check Deal links on
              Mockey pages now use <code>https://mockey.ai?via=jerome796</code>.
            </p>
          </div>
          <div className="methodology-update">
            <span className="methodology-update-date">2026-07-21</span>
            <p>
              <strong>Standardized content template.</strong> All comparison and best-of pages
              now follow a 3-tier recommendation + 7-row feature matrix + pricing table +
              WhyTrustUs block. The <code>scripts/validate_content_data.py</code> validator
              blocks any new page that doesn&apos;t pass.
            </p>
          </div>
          <div className="methodology-update">
            <span className="methodology-update-date">2026-07-15</span>
            <p>
              <strong>Affiliate audit run.</strong> Verified 7 active affiliate accounts
              (Creative Fabrica, Claid, Printify, Printful, Mockey, Looka, Photoroom).
              Two flagged for renewal (Looka program status; Photoroom Awin re-sign).
            </p>
          </div>
        </div>
      </section>

      <WhyTrustUs />
    </div>
  )
}
