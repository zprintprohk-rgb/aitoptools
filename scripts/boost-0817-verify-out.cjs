const fs = require('fs')
for (const slug of ['midjourney-review', 'jasper-ai-review']) {
  const h = fs.readFileSync('out/' + slug + '/index.html', 'utf8')
  const checks = {
    'FAQPage schema': h.includes('FAQPage'),
    'Review schema': h.includes('"@type":"Review"') || h.includes('"@type": "Review"'),
    'dateModified schema (2026-08-17)': h.includes('2026-08-17'),
    'Last updated 可见行': h.includes('Last updated 2026-08-17'),
    'Key features 功能行': h.includes('Key features:'),
    'Sources 引用链段': h.includes('Sources &amp; References') || h.includes('Sources & References'),
    '内链1 (同品类 review)': h.includes('/leonardo-ai-review/') || h.includes('/writesonic-review/'),
    '内链2 (category)': h.includes('/category/ai-image/') || h.includes('/category/ai-writing/'),
    '内链3 (hub/best)': h.includes('/best-design-tools-for-ai-art/') || h.includes('/best-ai-writing-tools-comparison/'),
    '嵌套<a> 全站该页': !/<a\b[^>]*>[^<]*<a\b/.test(h.replace(/<script[\s\S]*?<\/script>/g,'')),
  }
  console.log('== ' + slug + ' ==')
  for (const [k, v] of Object.entries(checks)) console.log((v ? 'PASS' : 'FAIL') + ' ' + k)
}
