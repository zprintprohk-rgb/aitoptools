/**
 * Pricing comparison table for head-to-head pages.
 * pricing: { betterValue: 'a'|'b', rows: [{ label, a, b }] }
 * The better-value column gets an amber tint and a "Better Value" tag.
 */
export default function PricingTable({ pricing, nameA, nameB }) {
  if (!pricing?.rows?.length) return null
  const betterA = pricing.betterValue === 'a'
  const betterB = pricing.betterValue === 'b'
  return (
    <div className="pricing-table-wrap">
      <table className="pricing-table">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col" className={betterA ? 'pt-better' : ''}>
              {nameA}
              {betterA && <span className="pt-tag">Better Value</span>}
            </th>
            <th scope="col" className={betterB ? 'pt-better' : ''}>
              {nameB}
              {betterB && <span className="pt-tag">Better Value</span>}
            </th>
          </tr>
        </thead>
        <tbody>
          {pricing.rows.map((r, i) => (
            <tr key={i}>
              <th scope="row">{r.label}</th>
              <td className={betterA ? 'pt-better' : ''}>{r.a}</td>
              <td className={betterB ? 'pt-better' : ''}>{r.b}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
