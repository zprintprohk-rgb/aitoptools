/**
 * One-off script: infer explicit `categorySlug` for every entry in reviews.json.
 *
 * Precedence:
 *  1. Reproduce the EXACT legacy fuzzy-matching rules used by
 *     src/app/category/[slug]/page.js and src/app/best-ai-tools/page.js,
 *     so every tool that appeared on a category page keeps that category
 *     (checked in order: ai-print-design, ai-ecommerce, then name/prefix match).
 *  2. For the 43 tools the legacy rules never matched, map the existing
 *     `category` string to the best-fit of the 6 category slugs.
 *  3. Anything still unmapped is logged as a warning (should not happen).
 *
 * Usage: node scripts/infer_category_slug.js
 */
const fs = require('fs')
const path = require('path')

const FILE = path.join(__dirname, '..', 'src', 'data', 'reviews.json')
const reviews = JSON.parse(fs.readFileSync(FILE, 'utf8'))

// --- 1. Legacy rules, verbatim from category/[slug]/page.js ---
function legacyMatch(r, catSlug) {
  if (catSlug === 'ai-print-design') return r.slug.includes('print') || r.slug.includes('packag')
  if (catSlug === 'ai-ecommerce') return r.slug.includes('ecom') || r.slug.includes('shopify')
  return r.category.toLowerCase().replace(/\s+/g, '-') === catSlug ||
         r.slug.startsWith(catSlug.replace('ai-', ''))
}
const LEGACY_ORDER = ['ai-print-design', 'ai-ecommerce', 'ai-writing', 'ai-image', 'ai-video', 'ai-voice']

// --- 2. Best-fit map for category strings the legacy rules never matched ---
const CATEGORY_NAME_MAP = {
  'AI Print Design': 'ai-print-design',
  'AI Print & Packaging': 'ai-print-design',
  'AI Print Marketing': 'ai-print-design',
  'AI POD Platform': 'ai-print-design',
  'AI E-Commerce': 'ai-ecommerce',
  'AI Shopify Plugins': 'ai-ecommerce',
  'AI Customer Service': 'ai-ecommerce',   // e-com customer engagement tools
  'Web Hosting': 'ai-ecommerce',           // store/site builders
  'AI Product Photography': 'ai-image',
  'AI Presentation': 'ai-image',
  'AI Music': 'ai-voice',                  // audio generation
  'AI Productivity': 'ai-writing',         // general assistant / writing-adjacent
  'AI Search': 'ai-writing',
  'AI Coding': 'ai-writing',               // text/code generation
  'Security': 'ai-ecommerce',              // business-ops tools, closest available bucket
  'Security & Privacy': 'ai-ecommerce',
}

let legacyCount = 0, mappedCount = 0
const warnings = []

for (const r of reviews) {
  let slug = LEGACY_ORDER.find(c => legacyMatch(r, c))
  if (slug) legacyCount++
  else {
    slug = CATEGORY_NAME_MAP[r.category]
    if (slug) mappedCount++
    else warnings.push(`${r.slug} | category="${r.category}" -> NO MAPPING`)
  }
  r.categorySlug = slug || null
}

if (warnings.length) {
  console.error('WARNING, unmapped entries:')
  warnings.forEach(w => console.error('  ' + w))
  process.exit(1)
}

fs.writeFileSync(FILE, JSON.stringify(reviews, null, 2) + '\n')

// --- report ---
const dist = {}
for (const r of reviews) dist[r.categorySlug] = (dist[r.categorySlug] || 0) + 1
console.log(`Total: ${reviews.length} | legacy-rule matches: ${legacyCount} | name-map fallback: ${mappedCount}`)
console.log('Distribution:', dist)

console.log('\n10-entry spot check (slug | category -> categorySlug):')
const picks = [0, 7, 15, 23, 31, 39, 47, 55, 63, 73]
for (const i of picks) {
  const r = reviews[i]
  console.log(`  ${r.slug} | ${r.category} -> ${r.categorySlug}`)
}
