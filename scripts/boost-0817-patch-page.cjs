const fs = require('fs')
const p = 'src/app/[slug]/page.js'
let s = fs.readFileSync(p, 'utf8')
const log = []
function rep(name, from, to) {
  if (!s.includes(from)) throw new Error('PATTERN NOT FOUND: ' + name)
  s = s.replace(from, to)
  log.push('OK ' + name)
}
// 1) Review schema: dateModified
rep('schema-dateModified',
  "datePublished: review.datePublished || '2026-06-25',",
  "datePublished: review.datePublished || '2026-06-25',\n      dateModified: review.dateModified || review.datePublished || '2026-06-25',")
// 2) meta-bar: Last updated span
rep('meta-last-updated',
  '<span className="card-price">From {review.price}</span>',
  '<span className="card-price">From {review.price}</span>\n          {review.dateModified && (\n            <span style={{ color: \'var(--k-tertiary)\', fontSize: \'0.8rem\' }}>· Last updated {review.dateModified}</span>\n          )}')
// 3) byline 后: 功能行 featureLine
rep('feature-line',
  '        {/* Pros & Cons */}',
  `        {review.featureLine && (
          <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', margin: '4px 0 0' }}>
            <strong>Key features:</strong> {review.featureLine}
          </p>
        )}

        {/* Pros & Cons */}`)
fs.writeFileSync(p, s, 'utf8')
console.log(log.join('\n'))
console.log('page.js patched OK')
