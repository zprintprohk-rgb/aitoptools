/**
 * blog-links.mjs 单元测试 — 内链注入逻辑验证
 * 运行: node scripts/test-blog-links.mjs   (cwd 必须是 F:/aitoptools)
 */
import { buildToolLinkIndex, autoLinkTools } from '../src/lib/blog-links.mjs'

let pass = 0
let fail = 0
function assert(name, cond, extra = '') {
  if (cond) { pass++; console.log(`  ✓ ${name}`) }
  else { fail++; console.log(`  ✗ ${name} ${extra}`) }
}

console.log('== buildToolLinkIndex ==')
const index = buildToolLinkIndex()
assert('索引非空', index.size > 0, `size=${index.size}`)
console.log(`  (索引含 ${index.size} 个工具名)`)

console.log('== autoLinkTools ==')
const linked = new Set()

// 1. 首现包链
const t1 = autoLinkTools('We tested Mockey for 3 weeks.', index, linked)
assert('Mockey 首现被链', t1.includes('<a href="/mockey-review/" class="blog-internal-link">Mockey</a>'), t1)

// 2. 同一工具第二次出现不再链
const t2 = autoLinkTools('Mockey is also great for bulk mockups.', index, linked)
assert('第二次出现不重复链', t2.includes('Mockey') && !t2.includes('<a href'), t2)

// 3. 无匹配原样返回
const t3 = autoLinkTools('This paragraph mentions nothing relevant.', index, linked)
assert('无匹配原样返回', t3 === 'This paragraph mentions nothing relevant.')

// 4. 词边界: "Mockey's" 应匹配并只包 "Mockey"
const linked4 = new Set()
const t4 = autoLinkTools("Mockey's AI background remover is fast.", index, linked4)
assert('Mockey\'s 词边界匹配', t4.includes('>Mockey</a>\'s'), t4)

// 5. 不应匹配前缀词 "MockeyX"（\b 后无边界）
const linked5 = new Set()
const t5 = autoLinkTools('MockeyX is not a real tool.', index, linked5)
assert('MockeyX 不误链', t5 === 'MockeyX is not a real tool.', t5)

// 6. 长名优先: 用合成索引验证排序（真实索引里无名称前缀重叠对）
const synthetic = new Map([
  ['ai design', { name: 'AI Design', url: '/ai-design-review/' }],
  ['design', { name: 'Design', url: '/design-review/' }],
])
const linked6 = new Set()
const t6 = autoLinkTools('AI design tools and design guides both matter.', synthetic, linked6)
assert('长名优先匹配', t6.includes('>AI design</a>') && t6.includes('>design</a>'), t6)

// 7. 大小写不敏感
const linked7 = new Set()
const t7 = autoLinkTools('printify and PRINTFUL both serve POD sellers.', index, linked7)
assert('大小写不敏感', t7.includes('>printify</a>') && t7.includes('>PRINTFUL</a>'), t7)

// 8. 索引里确有 9 个联盟工具中的已收录者; pending 工具（picjam 无 review）正确不链
assert('tools/ SSoT 已入索引', index.has('mockey') && index.has('printify') && index.has('creative fabrica'))
assert('pending 工具不链（picjam 无详情页）', !index.has('picjam'))
assert('reviews 兜底入索引', index.has('jasper ai'))

console.log(`\n结果: ${pass} 通过 / ${fail} 失败`)
process.exit(fail ? 1 : 0)
