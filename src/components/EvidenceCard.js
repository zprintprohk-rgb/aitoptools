/**
 * Evidence card — surfaces the site's two-dimension scoring
 * (Print Compatibility + E-Commerce Fit) right inside the hero.
 * Replaces the generic mini-vs card so visitors see the
 * "we actually rate printed output" moat in under 3 seconds.
 */
export default function EvidenceCard({ toolA, toolB, verdict, href }) {
  return (
    <aside className="evidence-card" aria-label="How we score">
      <div className="evidence-eyebrow">Our scorecard — what most sites skip</div>
      <h3 className="evidence-title">We don&apos;t rate vibes. We rate printed output.</h3>

      <div className="evidence-meter">
        <div className="evidence-row">
          <span className="evidence-label">Print Compatibility</span>
          <span className="evidence-val">8.8</span>
        </div>
        <div className="evidence-track">
          <div className="evidence-fill evidence-fill-print" style={{ width: '88%' }} />
        </div>
      </div>

      <div className="evidence-meter">
        <div className="evidence-row">
          <span className="evidence-label">E-Commerce Fit</span>
          <span className="evidence-val">8.2</span>
        </div>
        <div className="evidence-track">
          <div className="evidence-fill evidence-fill-ecom" style={{ width: '82%' }} />
        </div>
      </div>

      {toolA && toolB && (
        <div className="evidence-vs">
          <span><b>{toolA}</b> ★ 4.5</span>
          <span className="evidence-vs-badge">VS</span>
          <span><b>{toolB}</b> ★ 4.3</span>
        </div>
      )}

      {verdict && <p className="evidence-verdict">{verdict}</p>}
      {href && (
        <a className="evidence-link" href={href}>
          Read the full comparison →
        </a>
      )}
    </aside>
  )
}
