/**
 * Two-column pros/cons panel. Green checks, muted-gray crosses.
 * Stacks vertically on mobile.
 */
export default function ProsCons({ pros = [], cons = [] }) {
  return (
    <div className="pros-cons">
      <div className="pros-box">
        <h3>✓ Pros</h3>
        <ul>{pros.map((p, i) => <li key={i} dangerouslySetInnerHTML={{ __html: p }} />)}</ul>
      </div>
      <div className="cons-box">
        <h3>✗ Cons</h3>
        <ul>{cons.map((c, i) => <li key={i} dangerouslySetInnerHTML={{ __html: c }} />)}</ul>
      </div>
    </div>
  )
}
