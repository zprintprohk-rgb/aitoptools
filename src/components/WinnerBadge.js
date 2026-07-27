/**
 * Winner badge — marks the winning side in a comparison card.
 * Visual: amber pill with star, sits inside the winning .vs-side.
 * Token contract: uses --a-primary (amber) and --a-bg (light amber).
 */
export default function WinnerBadge({ label = 'winner' }) {
  return (
    <span className="winner-badge" aria-label={`Winner: ${label}`}>
      <span className="winner-star" aria-hidden="true">★</span> {label}
    </span>
  )
}
