/**
 * Blog 文章页 — 内容军规渲染模板 (2026-08-04)
 *
 * 结构（AGENTS.md §3.1 内容军规）:
 *   TL;DR 摘要框 → 目录 TOC → 第一人称实测正文（blocks）→ Pros/Cons → FAQ → Related
 * Schema（指令二）: Article + FAQPage + BreadcrumbList
 *    - Article 字段: headline / datePublished / dateModified / author (Person Jerome Tang) /
 *      publisher / wordCount / image / mainEntityOfPage / articleSection
 *    - 注意: aggregateRating 不属于 Article（Google 规范）, 工具页的
 *      SoftwareApplication + rating 由 src/app/[slug]/page.js 的 Review schema 承载
 * 内链（指令三）: autoLinkTools() 自动扫描 src/data/tools/*.json + reviews.json,
 *   正文/FAQ 首次出现的工具名自动链到详情页 (每工具每篇只链一次)
 */
import { notFound } from 'next/navigation'
import Link from 'next/link'
import posts from '@/data/blog-posts.json'
import ProsCons from '@/components/ProsCons'
import { buildToolLinkIndex, autoLinkTools } from '@/lib/blog-links.mjs'

const DOMAIN = 'https://aitoptools.net'
const AUTHOR_NAME = 'Jerome Tang'
const AUTHOR_TITLE = 'Print Industry Expert'
const AUTHOR = { '@type': 'Person', name: AUTHOR_NAME, jobTitle: AUTHOR_TITLE }

export function generateStaticParams() {
  return posts.map((p) => ({ slug: p.slug }))
}

export function generateMetadata({ params }) {
  const post = posts.find((p) => p.slug === params.slug)
  if (!post) return { title: 'Not Found' }
  const url = `${DOMAIN}/blog/${post.slug}/`
  const ogImage = post.ogImage || '/og-image.png'
  return {
    title: post.title,
    description: post.metaDescription,
    alternates: { canonical: url },
    openGraph: {
      title: post.title,
      description: post.metaDescription,
      url,
      type: 'article',
      siteName: 'Print AI Tools',
      publishedTime: post.datePublished,
      modifiedTime: post.dateModified || post.datePublished,
      authors: [AUTHOR_NAME],
      images: [{ url: ogImage }],
    },
    twitter: {
      card: 'summary_large_image',
      title: post.title,
      description: post.metaDescription,
      images: [ogImage],
    },
  }
}

function slugify(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '')
}

/** 军规字数统计: blocks 全部文本 + FAQ（用于 Article.wordCount 与 readTime） */
function countWords(post) {
  let n = 0
  const count = (s) => { if (s) n += String(s).split(/\s+/).length }
  for (const b of post.blocks || []) {
    count(b.text)
    if (b.items) b.items.forEach(count)
    if (b.rows) b.rows.forEach((r) => r.forEach(count))
    if (b.pros) b.pros.forEach(count)
    if (b.cons) b.cons.forEach(count)
  }
  for (const f of post.faqs || []) { count(f.q); count(f.a) }
  return n
}

function buildSchemas(post) {
  const url = `${DOMAIN}/blog/${post.slug}/`
  const wordCount = countWords(post)
  const graph = [
    {
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: post.title,
      description: post.metaDescription,
      image: post.ogImage || `${DOMAIN}/og-image.png`,
      datePublished: post.datePublished,
      dateModified: post.dateModified || post.datePublished,
      author: AUTHOR,
      publisher: {
        '@type': 'Organization',
        name: 'Print AI Tools',
        url: `${DOMAIN}/`,
        logo: { '@type': 'ImageObject', url: `${DOMAIN}/og-image.png` },
      },
      mainEntityOfPage: url,
      wordCount,
      articleSection: post.category || 'AI Tools for Print',
      inLanguage: 'en',
    },
  ]
  if (post.faqs?.length) {
    graph.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: post.faqs.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    })
  }
  graph.push({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'Home', item: `${DOMAIN}/` },
      { '@type': 'ListItem', position: 2, name: 'Blog', item: `${DOMAIN}/blog/` },
      { '@type': 'ListItem', position: 3, name: post.title, item: url },
    ],
  })
  return graph
}

export default function BlogPostPage({ params }) {
  const post = posts.find((p) => p.slug === params.slug)
  if (!post) notFound()

  // 指令三: 内链自动注入 — 每篇文章一个去重集合, 跨块共享
  const toolIndex = buildToolLinkIndex()
  const alreadyLinked = new Set()
  const L = (text) => autoLinkTools(text, toolIndex, alreadyLinked)

  const wordCount = countWords(post)
  const readTime = Math.max(1, Math.round(wordCount / 200))
  const jsonLd = buildSchemas(post)
  const blocks = (post.blocks || []).filter(
    (b) => !(b.type === 'h2' && /frequently asked questions/i.test(b.text))
  )
  const toc = blocks.filter((b) => b.type === 'h2').map((b) => ({ id: slugify(b.text), text: b.text }))
  const related = post.related?.length
    ? post.related
    : posts.filter((p) => p.slug !== post.slug).slice(0, 3).map((p) => ({ title: p.title, url: `/blog/${p.slug}/` }))

  return (
    <>
      {jsonLd.map((s, i) => (
        <script key={i} type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(s) }} />
      ))}

      <div className="review-page container">
        {/* Breadcrumb */}
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="sep">›</span>
          <Link href="/blog/">Blog</Link>
          <span className="sep">›</span>
          <span className="current">{post.title}</span>
        </nav>

        <h1>{post.title}</h1>
        <div className="meta-bar">
          <span className="card-cat">{post.category}</span>
          <span>{post.datePublished} · {readTime} min read · {wordCount.toLocaleString()} words</span>
          <span className="card-badge tested" style={{ display: 'inline-flex', alignItems: 'center', gap: 4, background: 'var(--c-bg)', color: 'var(--c-text)', fontSize: '0.68rem', fontWeight: 600, padding: '2px 8px', borderRadius: '100px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>✓ Hands-on Tested</span>
        </div>
        <p style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginTop: -8, marginBottom: 24 }}>
          Reviewed by <strong>{AUTHOR_NAME}, {AUTHOR_TITLE}</strong>
        </p>

        {/* TL;DR — 太长不看 */}
        {post.tldr?.length > 0 && (
          <div className="verdict-box">
            <h2 style={{ fontSize: '1.15rem', fontWeight: 700, marginBottom: 8, color: 'var(--k-deep)' }}>⚡ TL;DR — Too Long; Didn't Read</h2>
            <ul style={{ margin: 0, paddingLeft: 20 }}>
              {post.tldr.map((t, i) => (
                <li key={i} style={{ marginBottom: 6 }} dangerouslySetInnerHTML={{ __html: L(t) }} />
              ))}
            </ul>
          </div>
        )}

        {/* TOC — 目录锚点 */}
        {toc.length >= 2 && (
          <div style={{ border: '1px solid rgba(23,32,28,0.10)', background: '#fff', padding: '16px 24px', margin: '24px 0' }}>
            <p style={{ fontWeight: 700, marginBottom: 8, fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--k-tertiary)' }}>In this article</p>
            <ol style={{ margin: 0, paddingLeft: 20 }}>
              {toc.map((t) => (
                <li key={t.id} style={{ marginBottom: 4 }}>
                  <a href={`#${t.id}`} style={{ color: 'var(--c-primary)', textDecoration: 'none' }}>{t.text}</a>
                </li>
              ))}
            </ol>
          </div>
        )}

        {/* 正文 blocks */}
        <div className="review-content">
          {blocks.map((b, i) => {
            switch (b.type) {
              case 'h2':
                return (
                  <h2 key={i} id={slugify(b.text)} style={{ fontSize: '1.75rem', fontWeight: 700, margin: '40px 0 16px', color: 'var(--k-deep)' }}>
                    {b.text}
                  </h2>
                )
              case 'h3':
                return <h3 key={i} style={{ fontSize: '1.2rem', fontWeight: 700, margin: '28px 0 10px', color: 'var(--k-deep)' }}>{b.text}</h3>
              case 'p':
                return <p key={i} dangerouslySetInnerHTML={{ __html: L(b.text) }} />
              case 'list':
                return (
                  <ul key={i}>
                    {(b.items || []).map((it, j) => (
                      <li key={j} dangerouslySetInnerHTML={{ __html: L(it) }} />
                    ))}
                  </ul>
                )
              case 'table':
                return (
                  <div key={i} className="compare-table-wrap" style={{ overflowX: 'auto' }}>
                    <table className="compare-table">
                      <thead>
                        <tr>{(b.headers || []).map((h, j) => <th key={j}>{h}</th>)}</tr>
                      </thead>
                      <tbody>
                        {(b.rows || []).map((row, j) => (
                          <tr key={j}>
                            {(row || []).map((cell, k) => (
                              <td key={k} dangerouslySetInnerHTML={{ __html: k === 0 ? `<strong>${cell}</strong>` : L(cell) }} />
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )
              case 'screenshot':
                return (
                  <figure key={i} style={{ margin: '24px 0' }}>
                    <img src={b.src} alt={b.alt || ''} loading="lazy" style={{ width: '100%', maxWidth: 720, border: '1px solid rgba(23,32,28,0.10)', borderRadius: 4 }} />
                    {b.caption && <figcaption style={{ fontSize: '0.85rem', color: 'var(--k-tertiary)', marginTop: 8 }}>{b.caption}</figcaption>}
                  </figure>
                )
              case 'note':
                return (
                  <div key={i} style={{ fontSize: '0.92rem', color: '#2a322d', background: 'rgba(11,95,89,0.05)', borderLeft: '3px solid var(--c-primary)', padding: '10px 16px', margin: '16px 0' }}>
                    <strong>Note:</strong> <span dangerouslySetInnerHTML={{ __html: L(b.text) }} />
                  </div>
                )
              case 'proscons':
                return (
                  <div key={i} style={{ margin: '20px 0' }}>
                    <ProsCons pros={(b.pros || []).map(L)} cons={(b.cons || []).map(L)} />
                  </div>
                )
              default:
                return null
            }
          })}
        </div>

        {/* CTA (联盟转化, 8/5 补: Blog 必须有 CTA 才有收益) */}
        {post.affiliateUrl && (
          <div style={{ margin: '28px 0', padding: '20px 24px', background: 'rgba(11,95,89,0.06)', border: '1px solid rgba(11,95,89,0.25)', borderRadius: 6, textAlign: 'center' }}>
            <p style={{ fontSize: '1.05rem', fontWeight: 700, color: 'var(--k-deep)', margin: '0 0 12px' }}>
              {post.ctaText || 'Try it Free'} →
            </p>
            <a href={post.affiliateUrl} target="_blank" rel="nofollow sponsored" style={{ display: 'inline-block', background: 'var(--c-primary)', color: '#fff', padding: '12px 28px', borderRadius: 4, fontWeight: 700, textDecoration: 'none' }}>
              {post.ctaText || 'Check Deal'}
            </a>
            {post.secondaryAffiliateUrl && (
              <p style={{ marginTop: 12, fontSize: '0.9rem' }}>
                <a href={post.secondaryAffiliateUrl} target="_blank" rel="nofollow sponsored" style={{ color: 'var(--c-primary)', fontWeight: 600 }}>
                  {post.secondaryCtaText || 'Try Alternative'} →
                </a>
              </p>
            )}
          </div>
        )}

        {/* FAQ */}
        {post.faqs?.length > 0 && (
          <div className="faq-section">
            <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 16, color: 'var(--k-deep)' }}>Frequently Asked Questions</h2>
            {post.faqs.map((faq, i) => (
              <details key={i} className="faq-item">
                <summary className="faq-question">{faq.q}</summary>
                <div className="faq-answer"><p dangerouslySetInnerHTML={{ __html: L(faq.a) }} /></div>
              </details>
            ))}
          </div>
        )}

        {/* Related */}
        {related.length > 0 && (
          <div className="section-header" style={{ marginTop: 36 }}>
            <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: 'var(--k-deep)' }}>Keep Reading</h2>
          </div>
        )}
        <div className="review-grid" style={{ gridTemplateColumns: 'repeat(2, 1fr)' }}>
          {related.map((r, i) => (
            <article key={i} className="review-card">
              <h3 style={{ fontSize: '1rem' }}><Link href={r.url}>{r.title}</Link></h3>
            </article>
          ))}
        </div>

        {/* Affiliate Disclosure */}
        <div className="aff-disc">
          <strong>Affiliate Disclosure:</strong> Some links on this page are affiliate links. We may earn a commission if you make a purchase through these links, at no additional cost to you. All reviews are based on honest, independent testing by print industry professionals. See our <Link href="/affiliate-disclosure/">full disclosure</Link>.
        </div>
      </div>
    </>
  )
}
