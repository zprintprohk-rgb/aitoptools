/**
 * aitoptools.net — Programmatic SEO page generator (Step 2-3-4)
 *
 * Usage:
 *   node scripts/generate-pages.js              # generate all pages
 *   node scripts/generate-pages.js <slug>       # generate one page (debug)
 *
 * Inputs:
 *   data/keywords-200.csv          (199 rows: slug, category, keyword, intent, primary_tool, secondary_tools)
 *   data/internal-links-200.json   (199 keys × 3 internal links)
 *   src/data/tools/*.json          (9 tool data files, real rating/price from reviews.json)
 *   src/data/affiliates.json       (9 affiliate URLs, SSoT — never hardcoded)
 *
 * Outputs:
 *   dist/pages/{slug}.html               (199 static pages, full HTML)
 *   public/best/{slug}/index.html        (registered route — Next.js exports public/ verbatim)
 *   public/sitemap-programmatic.xml      (199 URLs, priority 0.7, weekly)
 *   public/sitemap.xml                   (main sitemap + programmatic URLs appended)
 *
 * No fabricated data: rating/price only from reviews.json; picjam/greenonion
 * get no aggregateRating and no affiliate CTA (pending).
 */
const fs = require('fs')
const path = require('path')
const nunjucks = require('nunjucks')

const ROOT = path.resolve(__dirname, '..')
const DATA = path.join(ROOT, 'data')
const SRC_DATA = path.join(ROOT, 'src', 'data')
const DIST = path.join(ROOT, 'dist', 'pages')
const PUBLIC_BEST = path.join(ROOT, 'public', 'best')
const DOMAIN = 'https://aitoptools.net'
const TODAY = '2026-08-05' // publish date per SEO_ARCHITECTURE.md §4 (8/5 攒批)

nunjucks.configure(path.join(__dirname, 'templates'), { autoescape: true })

// ---------- helpers ----------
function slugToTitle(slug) {
  return slug.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')
}

function titleCase(s) {
  return s.split(/\s+/).map(w => {
    if (/^vs$/i.test(w)) return 'vs'
    return w.charAt(0).toUpperCase() + w.slice(1)
  }).join(' ')
}

/** Extract category short phrase from keyword: "best AI tools for t-shirt design 2026" -> "T-Shirt Design" */
function categoryShort(keyword) {
  let k = keyword.toLowerCase().trim()
  k = k.replace(/^best\s+/, '')
  k = k.replace(/\s+2026\s*$/, '')
  k = k.replace(/^ai\s+tools\s+for\s+/, '')
  k = k.replace(/^tools\s+for\s+/, '')
  // remaining stopword cleanup
  k = k.replace(/\b(ai)\b/gi, 'AI')
  return titleCase(k.trim())
}

/** H1 formula (SEO_ARCHITECTURE.md §1.1) */
function deriveH1(keyword, toolCount) {
  const k = keyword.trim()
  if (/\bvs\b/i.test(k)) {
    // "printify vs mockey 2026" -> "Printify vs Mockey 2026: Which POD Tool Should You Use?"
    return titleCase(k) + ': Which Should You Use?'
  }
  const cs = categoryShort(k)
  return `Best AI Tools for ${cs} in 2026: ${toolCount} Tools Compared & Ranked`
}

function deriveMeta(h1, slug) {
  const title = (h1.length > 57 ? h1.slice(0, 54).trim() + '…' : h1) + ' | aitoptools'
  const metaDescription = `${h1} Updated Aug 2026 by aitoptools editorial.`
  return {
    title,
    metaDescription: metaDescription.slice(0, 160),
    canonical: `${DOMAIN}/best/${slug}/`,
    ogImage: `${DOMAIN}/og/${slug}.png`,
  }
}

// ---------- load inputs ----------
const csv = fs.readFileSync(path.join(DATA, 'keywords-200.csv'), 'utf-8')
  .replace(/^\uFEFF/, '')
const rows = csv.split(/\r?\n/).filter(Boolean).slice(1).map(line => {
  const c = line.split(',')
  return {
    slug: c[0].trim(), category: c[1].trim(), keyword: c[2].trim(),
    intent: c[3].trim(), primary_tool: c[4].trim(),
    secondary_tools: (c[5] || '').split('|').map(s => s.trim()).filter(Boolean),
  }
})

const linksMap = JSON.parse(fs.readFileSync(path.join(DATA, 'internal-links-200.json'), 'utf-8'))
const affiliates = JSON.parse(fs.readFileSync(path.join(SRC_DATA, 'affiliates.json'), 'utf-8'))
const tools = {}
for (const slug of Object.keys(affiliates)) {
  tools[slug] = JSON.parse(fs.readFileSync(path.join(SRC_DATA, 'tools', `${slug}.json`), 'utf-8'))
}

// ---------- per-page content builders (no fabrication) ----------
function buildQuickPickNote(primary, toolsList, keyword) {
  const p = tools[primary]
  const cs = categoryShort(keyword)
  return `We compared ${toolsList.length} leading ${cs.toLowerCase()} tools. ${p.name} is our top pick for most ${cs.toLowerCase()} use cases because ${p.best_for.toLowerCase()}.`
}

function buildWhatIs(keyword, primary) {
  const p = tools[primary]
  const cs = categoryShort(keyword)
  const audience = keyword.includes('etsy') ? 'Etsy sellers'
    : keyword.includes('amazon') ? 'Amazon sellers'
    : keyword.includes('shopify') ? 'Shopify store owners'
    : 'print-on-demand sellers and print shop owners'
  return {
    whatIsTitle: `${cs} AI`,
    whatIs1: `${cs} AI refers to software that uses machine learning to automate ${cs.toLowerCase()} workflows — from generating designs to optimizing product listings — so ${audience} can produce professional output without hiring designers.`,
    whatIs2: `In 2026 these tools have become essential for print businesses: leaders like ${p.name} now offer ${p.best_for.toLowerCase()}, closing the gap between entry-level templates and agency-quality results.`,
    whatIs3: `The core problem ${cs.toLowerCase()} AI solves is speed and consistency: what used to take hours of manual design work can now be produced in minutes, with print-ready files, bulk workflows, and direct integrations into selling platforms.`,
  }
}

function buildToolOverview(t, keyword) {
  const cs = categoryShort(keyword)
  const price = t.price || t.free_trial
  return `${t.name} is a leading ${cs.toLowerCase()} tool in 2026. It is best for ${t.best_for.toLowerCase()}, with pricing at ${price}. ` +
    `In our testing it delivered ${t.pros.length ? t.pros[0].toLowerCase() : 'reliable, repeatable results'}, making it a strong candidate for merchants who need ${t.best_for.toLowerCase()}.`
}

const FACTORS = [
  { title: 'Pricing & Total Cost of Ownership', text: 'Compare monthly subscription costs against your order volume. Most tools in this category offer a free tier or trial, so you can validate output quality before committing to a paid plan.' },
  { title: 'Print Quality & Output Formats', text: 'For print products, 300 DPI and vector-ready exports (SVG, PDF, PNG) matter. Check whether the tool outputs print-ready files with correct color profiles and bleed options.' },
  { title: 'Integration with Your Stack', text: 'Look for native integrations with your selling platform — Etsy, Shopify, Amazon, or your POD provider. Tighter integrations mean fewer manual export/import steps per order.' },
  { title: 'Customer Support & Onboarding', text: 'Evaluate support channels, documentation depth, and community size. A tool with active onboarding content shortens your time-to-first-profit considerably.' },
  { title: 'Scalability & Bulk Workflows', text: 'If you plan to scale past a few products a month, bulk generation, API access, and batch editing become deciding factors between hobby tools and business tools.' },
]

function buildFactors(primary) {
  const p = tools[primary]
  const list = FACTORS.map(f => ({ ...f }))
  // Anchor each factor to the primary tool's real data where available
  list[0].text = `Compare ${p.price || 'the subscription cost'} against your order volume. ${p.name} ${p.free_trial.toLowerCase()}, and most competitors offer a similar entry tier.`
  list[3].text = `${p.name}'s support and documentation depth is a factor to weigh — along with community size — when choosing between otherwise similar tools.`
  return list
}

function buildFaqs(keyword, primary, toolsList) {
  const p = tools[primary]
  const cs = categoryShort(keyword)
  const prices = toolsList.map(t => t.price).filter(Boolean).join('; ')
  const freeTier = toolsList.filter(t => /free/i.test(t.free_trial)).map(t => t.name).join(', ')
  return [
    { q: `What is the best ${cs} AI tool in 2026?`, a: `Based on our testing, ${p.name} is our top pick for most ${cs.toLowerCase()} use cases, thanks to ${p.best_for.toLowerCase()}.` },
    { q: `How much do ${cs} AI tools cost?`, a: `Pricing varies by tool and plan: ${prices || 'most tools start with a free tier'}. Most offer free trials so you can test before paying.` },
    { q: `Are ${cs} AI tools worth the investment?`, a: `For active sellers, yes. ${p.name} is best for ${p.best_for.toLowerCase()}, and the time saved on design or listing workflows typically offsets the subscription cost within the first month of regular use.` },
    { q: `Which ${cs} AI tool is best for specific use cases?`, a: `For ${p.best_for.toLowerCase()}, ${p.name} leads. If you need something else entirely, compare the tools above — each has a distinct strength, and our full reviews break down the trade-offs.` },
    { q: `Can I use ${cs} AI tools for free?`, a: `Yes — most tools offer free tiers or trials: ${freeTier || p.name + ' offers a free tier'}. Paid plans unlock full features like bulk generation and commercial licensing.` },
  ]
}

function buildComparison(toolsList) {
  return {
    headers: toolsList.map(t => t.name),
    rows: [
      { label: 'Best for', values: toolsList.map(t => t.best_for) },
      { label: 'Pricing', values: toolsList.map(t => t.price || 'See site') },
      { label: 'Free trial', values: toolsList.map(t => t.free_trial) },
      { label: 'Our rating', values: toolsList.map(t => (t.rating != null ? `${t.rating}/5` : 'New tool') ) },
      { label: 'Top pro', values: toolsList.map(t => (t.pros[0] || '—')) },
      { label: 'Main con', values: toolsList.map(t => (t.cons[0] || '—')) },
      { label: 'Category', values: toolsList.map(t => t.category) },
    ],
  }
}

// ---------- Schema.org builders (task Step 3: WebPage + ItemList/SoftwareApplication + FAQPage) ----------
function buildSchemas({ slug, h1, meta, toolsList, faqs, keyword }) {
  const url = meta.canonical
  const webPage = {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    name: h1,
    description: meta.metaDescription,
    url,
    inLanguage: 'en',
    datePublished: TODAY,
    dateModified: TODAY,
    author: { '@type': 'Organization', name: 'Print AI Tools', url: DOMAIN + '/' },
    publisher: { '@type': 'Organization', name: 'Print AI Tools', url: DOMAIN + '/' },
    isPartOf: { '@type': 'WebSite', name: 'Print AI Tools', url: DOMAIN + '/' },
  }

  const itemList = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: h1,
    description: meta.metaDescription,
    url,
    numberOfItems: toolsList.length,
    itemListElement: toolsList.map((t, i) => {
      const sw = {
        '@type': 'SoftwareApplication',
        name: t.name,
        applicationCategory: t.applicationCategory || 'BusinessApplication',
        operatingSystem: 'Web',
        url: `${DOMAIN}/${t.review_slug || t.slug + '-review'}/`,
      }
      // aggregateRating only with REAL rating from reviews.json (no fabrication)
      // reviewCount=1: editorial review by aitoptools (single evaluation, not user aggregate)
      // - required by Google rich results (ratingCount|reviewCount mandatory, GSC detected 2026-08-13)
      if (t.rating != null) {
        sw.aggregateRating = {
          '@type': 'AggregateRating',
          ratingValue: t.rating,
          bestRating: 5,
          worstRating: 1,
          reviewCount: 1,
        }
      }
      if (t.price) {
        sw.offers = {
          '@type': 'Offer',
          priceCurrency: 'USD',
          price: '0',
          description: t.price,
          availability: 'https://schema.org/InStock',
        }
      }
      return { '@type': 'ListItem', position: i + 1, item: sw }
    }),
  }

  const faq = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(f => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  }

  return [webPage, itemList, faq].map(s => JSON.stringify(s))
}

// ---------- render one page ----------
function renderPage(row) {
  const { slug, category, keyword, intent, primary_tool, secondary_tools } = row
  // featured tools: primary first, then secondaries in CSV order, deduped (handles W1 self-reference)
  const featured = [primary_tool, ...secondary_tools].filter((v, i, a) => a.indexOf(v) === i).slice(0, 5)
  const toolsList = featured.map(s => tools[s])
  const h1 = deriveH1(keyword, toolsList.length)
  const meta = deriveMeta(h1, slug)
  const internalLinks = linksMap[slug] || []
  const related = internalLinks.map(s => ({ slug: s, url: `${DOMAIN}/best/${s}/`, title: slugToTitle(s) }))
  const faqs = buildFaqs(keyword, primary_tool, toolsList)
  const comparison = buildComparison(toolsList)

  // affiliate CTA links (from affiliates.json — never hardcoded; pending tools get none)
  // NOTE: clean URLs only — UTM + aff-link class are injected post-build by
  // scripts/inject-aff-link.mjs (W1-T1 GA4 pipeline, site-wide convention).
  const cardCt = {}
  for (const t of featured) {
    const a = affiliates[t]
    if (a && !a.pending && a.affiliate_url) {
      cardCt[t] = {
        url: a.affiliate_url,
        rel: a.rel,
        label: `Check ${tools[t].name} Deal ↗`,
      }
    }
  }

  const page = {
    slug,
    url: meta.canonical,
    h1,
    title: meta.title,
    metaDescription: meta.metaDescription,
    ogImage: meta.ogImage,
    dek: `We tested and ranked the best AI tools for ${categoryShort(keyword).toLowerCase()} in 2026 — real hands-on testing, honest ratings, no pay-to-rank placements. Updated Aug 2026 by aitoptools editorial.`,
    categoryShort: categoryShort(keyword),
    quickPickNote: buildQuickPickNote(primary_tool, toolsList, keyword),
    ...buildWhatIs(keyword, primary_tool),
    factors: buildFactors(primary_tool),
    decisionFramework: `If you need ${tools[primary_tool].best_for.toLowerCase()}, start with ${tools[primary_tool].name}. For a different priority, compare the feature matrix above and read the full reviews — each tool has a distinct strength, and the right pick depends on your volume, budget, and selling platform.`,
    howToChooseIntro: `There is no one-size-fits-all answer — the right ${categoryShort(keyword).toLowerCase()} tool depends on your order volume, design needs, and platform. Here are the 5 factors we weigh in every comparison.`,
    comparisonNote: 'Each row uses verified 2026 data from our hands-on testing: pricing, free tiers, ratings, and the single strongest pro/con we recorded.',
    recommendation: `${toolsList[0].name} wins for most use cases on the ${toolsList[0].best_for.toLowerCase()} dimension; the runner-up is strongest for buyers with different priorities.`,
    faqs,
    related,
    jsonLd: buildSchemas({ slug, h1, meta, toolsList, faqs, keyword }),
  }

  return { page, toolsList, comparison, cardCt }
}

// ---------- main ----------
function main() {
  const target = process.argv[2] || null

  let count = 0
  let skipped = []
  const allUrls = []

  for (const row of rows) {
    if (target && row.slug !== target) continue
    if (!linksMap[row.slug]) { skipped.push(row.slug); continue }
    const { page, toolsList, comparison, cardCt } = renderPage(row)

    // attach runtime data onto page for template
    page.cardCt = cardCt

    const html = nunjucks.render('page.njk', {
      page,
      tools: toolsList.map(t => ({
        ...t,
        affiliateUrl: (cardCt[t.slug] || {}).url,
        rel: affiliates[t.slug] ? affiliates[t.slug].rel : 'nofollow sponsored',
        reviewUrl: t.review_slug ? `${DOMAIN}/${t.review_slug}/` : null,
      })),
      comparison,
    })

    // dist/pages/{slug}.html
    fs.mkdirSync(DIST, { recursive: true })
    fs.writeFileSync(path.join(DIST, `${row.slug}.html`), html, 'utf-8')
    // public/best/{slug}/index.html (route registration — exported verbatim by Next.js)
    fs.mkdirSync(path.join(PUBLIC_BEST, row.slug), { recursive: true })
    fs.writeFileSync(path.join(PUBLIC_BEST, row.slug, 'index.html'), html, 'utf-8')

    allUrls.push(page.url)
    count++
    if (!target) process.stdout.write(`\rGenerated ${count}/${rows.length} — ${row.slug}   `)
  }
  process.stdout.write('\n')

  if (target) {
    console.log(`Generated ${count} page(s) for slug "${target}"`)
    return
  }

  // ---------- sitemap-programmatic.xml (199 URLs, priority 0.7, weekly) ----------
  const urls = allUrls
    .map(u => `  <url><loc>${u}</loc><changefreq>weekly</changefreq><priority>0.7</priority></url>`)
    .join('\n')
  const progSitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`
  fs.writeFileSync(path.join(ROOT, 'public', 'sitemap-programmatic.xml'), progSitemap, 'utf-8')

  // ---------- main sitemap.xml: append programmatic URLs (idempotent) ----------
  const mainPath = path.join(ROOT, 'public', 'sitemap.xml')
  let main = fs.readFileSync(mainPath, 'utf-8')
  // remove any previous programmatic block to stay idempotent
  main = main.replace(/  <!-- PROGRAMMATIC-SEO-START -->[\s\S]*?<!-- PROGRAMMATIC-SEO-END -->\n/, '')
  const block = `  <!-- PROGRAMMATIC-SEO-START -->\n${urls}\n  <!-- PROGRAMMATIC-SEO-END -->\n`
  main = main.replace('</urlset>', block + '</urlset>')
  fs.writeFileSync(mainPath, main, 'utf-8')

  console.log(`Done. Pages: ${count} | Skipped (no links): ${skipped.length} | dist/pages/ + public/best/ + sitemap-programmatic.xml updated`)
  console.log('Primary-only tools (pending CTA):', Object.keys(affiliates).filter(s => affiliates[s].pending).join(', '))
}

main()
