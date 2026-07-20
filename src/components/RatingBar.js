export default function RatingBar({ rating, max = 5, showValue = true }) {
  const pct = Math.max(0, Math.min(100, (rating / max) * 100))
  const full = Math.floor(rating)
  const stars = '★'.repeat(full) + '☆'.repeat(max - full)
  return (
    <span className="rating-bar" role="img" aria-label={`Rated ${rating} out of ${max}`}>
      <span className="rating-stars" aria-hidden="true">{stars}</span>
      {showValue && <span className="rating-value">{rating.toFixed(1)}</span>}
      <span className="rating-track" aria-hidden="true">
        <span className="rating-fill" style={{ width: `${pct}%` }} />
      </span>
    </span>
  )
}
