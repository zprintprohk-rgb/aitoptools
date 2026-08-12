/**
 * blog-links — Blog 内链自动注入（指令三, 2026-08-04）
 *
 * 生成 Blog 文章时自动扫描 src/data/tools/*.json（9 工具 SSoT）+ src/data/reviews.json（94 工具），
 * 文章正文/FAQ 中首次出现某工具名 → 自动加指向该工具详情页（/review-slug/）的内链。
 * 每个工具每篇文章只链第一次出现（标准内链实践，避免堆砌）。
 *
 * 用法（build 时, 服务端/构建期执行）:
 *   import { buildToolLinkIndex, autoLinkTools } from '@/lib/blog-links.mjs'
 *   const index = buildToolLinkIndex()          // 构建一次
 *   const linked = new Set()                    // 每篇文章一个去重集合
 *   const html = autoLinkTools(plainText, index, linked)
 *
 * 仅处理纯文本块（段落/列表项/FAQ 答案/表格单元格）——不碰已含 <a> 的富文本。
 */
import fs from 'fs'
import path from 'path'

const ROOT = path.resolve(process.cwd())

function loadJson(rel) {
  try {
    return JSON.parse(fs.readFileSync(path.join(ROOT, rel), 'utf-8'))
  } catch {
    return null
  }
}

/**
 * 构建 工具名(小写) -> { name, url } 索引。
 * 优先级: src/data/tools/*.json（review_slug 权威）> reviews.json（slug 即详情页）。
 * @returns {Map<string, {name: string, url: string}>}
 */
export function buildToolLinkIndex() {
  const index = new Map()
  const add = (name, reviewSlug) => {
    if (!name || !reviewSlug) return
    const key = name.toLowerCase()
    if (!index.has(key)) index.set(key, { name, url: `/${reviewSlug}/` })
  }

  // 1) src/data/tools/*.json — 联盟工具 SSoT（name + review_slug）
  const toolsDir = path.join(ROOT, 'src', 'data', 'tools')
  if (fs.existsSync(toolsDir)) {
    for (const f of fs.readdirSync(toolsDir).filter((x) => x.endsWith('.json'))) {
      try {
        const t = JSON.parse(fs.readFileSync(path.join(toolsDir, f), 'utf-8'))
        add(t.name, t.review_slug || (t.has_review ? `${t.slug}-review` : null))
      } catch {
        /* 坏文件跳过 */
      }
    }
  }

  // 2) reviews.json — 其余已收录工具（title 去掉 " Review" 前缀, slug 即详情页）
  const reviews = loadJson('src/data/reviews.json') || []
  for (const r of reviews) {
    const name = (r.title || '').split(' Review')[0] || String(r.slug).replace(/-review$/, '')
    add(name, r.slug)
  }

  return index
}

const escapeRegExp = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')

/**
 * 在纯文本中为「首次出现的工具名」包上内链。
 * @param {string} text 纯文本（无 HTML）
 * @param {Map} index buildToolLinkIndex() 的返回
 * @param {Set} alreadyLinked 本篇文章已链过的工具 key（小写名），跨块共享
 * @returns {string} 含 <a class="blog-internal-link"> 的 HTML 片段
 */
export function autoLinkTools(text, index, alreadyLinked = new Set()) {
  if (!text || !index || index.size === 0) return text
  // 长名优先匹配（"Creative Fabrica" 不会被 "Fabrica" 截胡；同名前缀场景更稳）
  const names = [...index.keys()].sort((a, b) => b.length - a.length)
  // 8/12 v2 修复: <a>...</a> 整体不可入侵（href 属性值 + 锚文本都不动），
  // 只在 anchor 之外的纯文本段匹配工具名 —— 避免 T11 Boost 链接被二次 autoLink 造成嵌套 <a>
  const anchorBlock = /<a\b[^>]*>[\s\S]*?<\/a>/i
  let out = text
  for (const key of names) {
    const entry = index.get(key)
    if (alreadyLinked.has(key)) continue
    const re = new RegExp(`\\b${escapeRegExp(entry.name)}\\b`, 'i')
    // 分段: anchor 整体为不可变段, 其余按普通标签切分
    const segments = out.split(/(<a\b[^>]*>[\s\S]*?<\/a>)/i)
    let done = false
    for (let i = 0; i < segments.length; i++) {
      const seg = segments[i]
      if (anchorBlock.test(seg)) continue
      // 段内再跳过普通标签（href 属性值等）, 只匹配纯文本
      const inner = seg.split(/(<[^>]+>)/)
      for (let j = 0; j < inner.length; j++) {
        const piece = inner[j]
        if (/^<[^>]+>$/.test(piece)) continue
        const m = re.exec(piece)
        if (!m) continue
        alreadyLinked.add(key)
        const link = `<a href="${entry.url}" class="blog-internal-link">${m[0]}</a>`
        inner[j] = piece.slice(0, m.index) + link + piece.slice(m.index + m[0].length)
        done = true
        break
      }
      if (done) {
        segments[i] = inner.join('')
        break
      }
    }
    out = segments.join('')
  }
  return out
}