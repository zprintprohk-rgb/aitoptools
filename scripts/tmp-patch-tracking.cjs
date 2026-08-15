const fs = require('fs')
const p = '.hermes/logs/boost-tracking.md'
let s = fs.readFileSync(p, 'utf8')
const a = '| 5 | /midjourney-review/ | 84.6 | 8/17 | 对比矩阵 (替代型) |'
const b = '| 6 | /jasper-ai-review/ | 91.5 | 8/17 | 对比矩阵 (替代型) |'
if (!s.includes(a)) throw new Error('row5 not found')
s = s.replace(a, a + ' DONE 8/17 (内容深度+引用链3+内链6+FAQ5+schema; IndexNow 2/2)')
s = s.replace(b, b + ' DONE 8/17 (内容深度+引用链3+内链6+FAQ5+schema; IndexNow 2/2)')
fs.writeFileSync(p, s, 'utf8')
console.log('boost-tracking updated OK')
