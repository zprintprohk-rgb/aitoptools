/**
 * Decision box — Wirecutter-style "Who it's for / NOT for / Best deal"
 * Used on tool detail pages to collapse hesitation into a single decision.
 * Token contract: --c-primary (teal check), --error (red cross),
 * --a-primary (amber deal), existing --bg-card / --border tokens.
 */
export default function DecisionBox({ goodFor = [], notFor = [], deal }) {
  if ((!goodFor.length) && (!notFor.length) && !deal) return null
  return (
    <div className="decision-box" aria-label="Decision summary">
      <div className="decision-col decision-good">
        <h4 className="decision-h">✓ Who it&apos;s for</h4>
        <ul>{goodFor.map((g, i) => <li key={i}>{g}</li>)}</ul>
      </div>
      <div className="decision-col decision-bad">
        <h4 className="decision-h">✗ Who it&apos;s NOT for</h4>
        <ul>{notFor.map((n, i) => <li key={i}>{n}</li>)}</ul>
      </div>
      {deal && (
        <div className="decision-col decision-deal">
          <h4 className="decision-h">💰 Best deal</h4>
          <p>{deal}</p>
        </div>
      )}
    </div>
  )
}
