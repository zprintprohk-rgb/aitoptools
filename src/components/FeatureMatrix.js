const SYMBOLS = { yes: '✓', no: '✗', partial: '◐' }
const LABELS = { yes: 'Yes', no: 'No', partial: 'Partial' }

function Cell({ value, highlight }) {
  return (
    <td className={`fm-cell fm-${value}${highlight ? ' fm-highlight' : ''}`}>
      <span className="fm-symbol" aria-hidden="true">{SYMBOLS[value] || value}</span>
      <span className="fm-sr">{LABELS[value] || value}</span>
    </td>
  )
}

/**
 * G2-style feature comparison matrix.
 * Two modes:
 *  - head-to-head: features = [{ feature, a: 'yes'|'no'|'partial', b }], names = [nameA, nameB]
 *  - multi-column: features = [{ feature, values: [...] }], names = [col1, col2, ...]
 * The winning cell (yes vs a lesser value) gets a light brand-green tint.
 */
export default function FeatureMatrix({ features, names }) {
  if (!features?.length || !names?.length) return null
  const rank = { yes: 2, partial: 1, no: 0 }
  return (
    <div className="feature-matrix-wrap">
      <table className="feature-matrix">
        <thead>
          <tr>
            <th scope="col">Feature</th>
            {names.map(n => <th key={n} scope="col">{n}</th>)}
          </tr>
        </thead>
        <tbody>
          {features.map((row, i) => {
            const vals = row.values ? row.values : [row.a, row.b]
            const best = Math.max(...vals.map(v => rank[v] ?? 0))
            return (
              <tr key={i}>
                <th scope="row">{row.feature}</th>
                {vals.map((v, j) => (
                  <Cell key={j} value={v} highlight={(rank[v] ?? 0) === best && best > 0 && vals.some(x => (rank[x] ?? 0) < best)} />
                ))}
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  )
}
