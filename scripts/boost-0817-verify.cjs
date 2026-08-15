const fs = require('fs')
const reviews = JSON.parse(fs.readFileSync('src/data/reviews.json', 'utf8'))
const reviewsArr = Array.isArray(reviews) ? reviews : Object.values(reviews)
const bestDirs = fs.existsSync('public/best') ? fs.readdirSync('public/best') : []
const blogPosts = JSON.parse(fs.readFileSync('src/data/blog-posts.json', 'utf8'))
const blogSlugs = (Array.isArray(blogPosts) ? blogPosts : Object.values(blogPosts)).map(b => b.slug)
const comparisons = JSON.parse(fs.readFileSync('src/data/comparisons.json', 'utf8'))
const cmpSlugs = (Array.isArray(comparisons) ? comparisons : Object.values(comparisons)).map(c => c.slug || String(c.url||'').replace(/^\//,'').replace(/\/$/,''))
const reviewSlugs = new Set(reviewsArr.map(r => r.slug))
const valid = new Set([...reviewSlugs, ...bestDirs, ...blogSlugs.map(s=>'blog/'+s), ...cmpSlugs,
  'category/ai-image','category/ai-writing','category/ai-print-design','category/ai-ecommerce','category/ai-video','category/ai-voice',
  'best','blog','compare','about','methodology'])

for (const slug of ['midjourney-review', 'jasper-ai-review']) {
  const r = reviewsArr.find(x => x.slug === slug)
  const c = r.content || ''
  const links = [...c.matchAll(/href=["']([^"']+)["']/g)].map(m => m[1])
  const external = links.filter(l => /^https?:/i.test(l))
  const internal = links.filter(l => !/^https?:/i.test(l) && !/^mailto:/i.test(l))
  const bad = internal.filter(l => !valid.has(l.replace(/^\//,'').replace(/\/$/,'')))
  // 真嵌套检测: 迭代剥掉完整 <a>...</a>, 残留 <a 即嵌套
  let t = c, prev = ''
  while (t !== prev) { prev = t; t = t.replace(/<a\b[^>]*>[\s\S]*?<\/a>/gi, '') }
  const nested = /<a\b/i.test(t)
  console.log(`== ${slug} ==`)
  console.log(` 内链 ${internal.length} | 外链引用 ${external.length} | FAQ ${(r.faqs||[]).length} | 无效内链 ${bad.length ? bad.join(',') : '无'} | 嵌套 ${nested ? '有!' : '无'}`)
}
