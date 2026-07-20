import RatingBar from './RatingBar'

const PICK_LABELS = {
  top: 'Our Pick',
  also: 'Also Great',
  budget: 'Budget Pick',
}

/**
 * Wirecutter-style three-tier recommendation cards.
 * picks: [{ type: 'top'|'also'|'budget', name, tagline, rating, anchor }]
 */
export default function PicksCards({ picks }) {
  if (!picks?.length) return null
  const ordered = ['top', 'also', 'budget'].map(t => picks.find(p => p.type === t)).filter(Boolean)
  return (
    <div className="picks-grid">
      {ordered.map(p => (
        <a key={p.type} href={p.anchor} className={`pick-card pick-${p.type}`}>
          <span className="pick-badge">{PICK_LABELS[p.type]}</span>
          <span className="pick-name">{p.name}</span>
          <span className="pick-tagline">{p.tagline}</span>
          {typeof p.rating === 'number' && <RatingBar rating={p.rating} />}
        </a>
      ))}
    </div>
  )
}
