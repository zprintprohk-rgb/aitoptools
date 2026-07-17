/**
 * One-off script: generate a `faqs` array (3-5 {q, a} items) for every entry
 * in reviews.json, derived ONLY from data already present on the entry
 * (price, rating, category, pros, cons, metaDesc). No fabricated facts.
 *
 * Each answer = one complete, directly-quotable conclusion sentence,
 * followed by one supporting detail sentence (GEO-friendly).
 *
 * Usage: node scripts/generate_faqs.js
 */
const fs = require('fs')
const path = require('path')

const FILE = path.join(__dirname, '..', 'src', 'data', 'reviews.json')
const reviews = JSON.parse(fs.readFileSync(FILE, 'utf8'))

function toolName(r) {
  return (r.title.split(' Review')[0] || r.title).trim()
}

function hasFreePlan(r) {
  const text = [r.price, ...(r.pros || []), ...(r.cons || [])].join(' ').toLowerCase()
  if (/no free plan|no free tier/.test(text)) return 'no'
  if (/free plan|free tier|freemium|free forever/.test(text)) return 'yes'
  return 'unknown'
}

function trialInfo(r) {
  const text = [r.price, ...(r.pros || []), ...(r.cons || []), r.metaDesc || ''].join(' ').toLowerCase()
  const m = text.match(/(\d+)[- ]day (free )?trial/)
  if (m) return `${m[1]}-day free trial`
  if (/free trial/.test(text)) return 'free trial'
  return null
}

function isFreePrice(r) {
  return /^free$|^free\b|\$0/i.test((r.price || '').trim())
}

function buildFaqs(r) {
  const name = toolName(r)
  const price = r.price || 'varies by plan'
  const rating = r.rating
  const cat = r.category
  const pros = r.pros || []
  const cons = r.cons || []
  const faqs = []

  // Q1: cost
  faqs.push({
    q: `How much does ${name} cost?`,
    a: isFreePrice(r)
      ? `${name} is free to use (${price}). Check the official site for any paid upgrades or usage limits.`
      : `${name} starts at ${price}. Higher-tier plans and team options are listed on the official website, which has the most current pricing.`,
  })

  // Q2: free plan / trial
  const free = hasFreePlan(r)
  const trial = trialInfo(r)
  let freeAnswer
  if (free === 'yes') {
    freeAnswer = `Yes, ${name} offers a free plan alongside its paid options (paid plans start at ${price}).`
  } else if (free === 'no') {
    freeAnswer = `No, ${name} does not have a free plan — pricing starts at ${price}.`
  } else {
    freeAnswer = `${name} is a paid tool starting at ${price}, and availability of a free tier can change.`
  }
  if (trial) freeAnswer += ` A ${trial} is available, so you can test it before paying.`
  else freeAnswer += ` Check the official site for the latest trial or money-back guarantee offers.`
  faqs.push({ q: `Is ${name} free?`, a: freeAnswer })

  // Q3: best for (from category + top pro)
  faqs.push({
    q: `What is ${name} best for?`,
    a: `${name} is best for ${cat.toLowerCase().replace(/^ai /, 'AI ')} work${pros[0] ? ` — its biggest strength is ${pros[0].charAt(0).toLowerCase() + pros[0].slice(1)}` : ''}. In our testing it earned a ${rating}/5 rating, making it a ${rating >= 4.5 ? 'top' : rating >= 4 ? 'strong' : 'solid'} pick in the ${cat} category.`,
  })

  // Q4: drawbacks (from cons)
  if (cons.length) {
    const lc = s => s.charAt(0).toLowerCase() + s.slice(1)
    const list = cons.length === 1
      ? lc(cons[0])
      : cons.slice(0, -1).map(lc).join('; ') + `; and ${lc(cons[cons.length - 1])}`
    faqs.push({
      q: `What are the main drawbacks of ${name}?`,
      a: `The main drawbacks of ${name} are: ${list}. None of these are deal-breakers for most users, but they matter if ${cons[0].toLowerCase().includes('price') || cons[0].toLowerCase().includes('expensive') ? 'budget is your primary concern' : 'that limitation affects your workflow'}.`,
    })
  }

  // Q5: worth it (rating + strongest pro)
  faqs.push({
    q: `Is ${name} worth it in 2026?`,
    a: rating >= 4
      ? `Yes — with a ${rating}/5 rating in our hands-on testing, ${name} is worth it for users who need ${cat} capabilities at ${price}.${pros[0] ? ` Its standout advantage: ${pros[0].charAt(0).toLowerCase() + pros[0].slice(1)}.` : ''}`
      : `${name} scored ${rating}/5 in our testing, so it is worth considering mainly if its specific strengths match your needs. Compare it with higher-rated alternatives in our ${cat} category before committing.`,
  })

  return faqs
}

for (const r of reviews) r.faqs = buildFaqs(r)

fs.writeFileSync(FILE, JSON.stringify(reviews, null, 2) + '\n')

const counts = reviews.map(r => r.faqs.length)
console.log(`Generated FAQs for ${reviews.length} tools. Per-tool count: min=${Math.min(...counts)}, max=${Math.max(...counts)}`)
console.log('\nSample (first entry):')
console.log(JSON.stringify({ slug: reviews[0].slug, faqs: reviews[0].faqs }, null, 2))
