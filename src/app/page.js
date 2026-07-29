'use client'
import { useState, useEffect } from 'react'
import Link from 'next/link'
import reviews from '@/data/reviews'
import comparisons from '@/data/comparisons.json'
import { buildAffLinkAttrs } from '@/lib/affiliate'
import listicles from '@/data/listicles.json'
import RatingBar from '@/components/RatingBar'
import WinnerBadge from '@/components/WinnerBadge'
import EvidenceCard from '@/components/EvidenceCard'

// A4 胜方映射 — 6 篇首页可见的对比。详情页 /compare/[slug]/ 由 B 桶统一接入
// hotfix 7/27: printify-vs-gelato 'B'→'A' 修 winner/conclusion 打架（结论首句 Choose Printify）
const COMPARISON_WINNERS = {
  'printful-vs-printify': 'B',
  'printify-vs-gelato': 'A',
  'printful-vs-gelato': 'A',
  'kittl-vs-placeit': 'A',
  'kittl-vs-canva': 'A',
  'mockey-vs-placeit': 'A',
}

const VERTICAL_CATEGORIES = [
  { name: '🖨️ Print & Packaging', slug: 'ai-print-design', desc: 'AI for print-on-demand, packaging design, label making', featured: true },
  { name: '🛒 E-Commerce & Shopify', slug: 'ai-ecommerce', desc: 'AI for product descriptions, store optimization, cross-border', featured: true },
  { name: '✍️ AI Writing', slug: 'ai-writing', desc: 'Copywriting, content creation, multilingual writing' },
  { name: '🎨 AI Image', slug: 'ai-image', desc: 'Image generation, editing, product photography' },
  { name: '🎬 AI Video', slug: 'ai-video', desc: 'Video generation, avatars, editing' },
  { name: '🎙️ AI Voice', slug: 'ai-voice', desc: 'Voice synthesis, dubbing, podcasting' },
]

const SCENARIO_TAGS = [
  { label: '📦 Packaging Design', href: '/category/ai-print-design/' },
  { label: '🛍️ Shopify', href: '/category/ai-ecommerce/' },
  { label: '👕 Print-on-Demand', href: '/category/ai-print-design/' },
  { label: '📸 Product Photos', href: '/category/ai-ecommerce/' },
]

const CAT_CARDS = [
  { name: 'Print & Packaging', slug: 'ai-print-design', desc: 'AI for print-on-demand, packaging design, label making' },
  { name: 'E-Commerce & Shopify', slug: 'ai-ecommerce', desc: 'AI for product descriptions, store optimization, cross-border' },
  { name: 'AI Writing', slug: 'ai-writing', desc: 'Copywriting, content creation, multilingual writing' },
  { name: 'AI Image', slug: 'ai-image', desc: 'Image generation, editing, product photography' },
  { name: 'AI Video', slug: 'ai-video', desc: 'Video generation, avatars, editing' },
  { name: 'AI Voice', slug: 'ai-voice', desc: 'Voice synthesis, dubbing, podcasting' },
]

function starRating(rating) {
  const full = Math.floor(rating)
  return '★'.repeat(full) + '☆'.repeat(5 - full)
}

export default function Home() {
  const [search, setSearch] = useState('')

  // Pick up ?q= from the nav search box (GET form → /?q=...)
  useEffect(() => {
    const q = new URLSearchParams(window.location.search).get('q')
    if (q) setSearch(q)
  }, [])

  const filtered = search.trim()
    ? reviews.filter(r =>
        r.title.toLowerCase().includes(search.toLowerCase()) ||
        r.category.toLowerCase().includes(search.toLowerCase()) ||
        r.metaDesc.toLowerCase().includes(search.toLowerCase())
      )
    : []

  // Identify vertical tools (print/e-commerce)
  const printTools = reviews.filter(r => 
    r.slug.includes('print') || r.slug.includes('packag') || 
    r.slug.includes('kittl') || r.slug.includes('placeit') || r.slug.includes('looka') ||
    r.slug.includes('claid') || r.slug.includes('photoroom')
  )
  const ecomTools = reviews.filter(r =>
    r.slug.includes('ecom') || r.slug.includes('shopify') ||
    r.slug.includes('product')
  )
  const verticalSlugs = [...printTools, ...ecomTools].map(r => r.slug)
  const generalTools = reviews.filter(r => !verticalSlugs.includes(r.slug))

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'WebSite',
            name: 'Print AI Tools',
            url: 'https://aitoptools.net/',
          }),
        }}
      />
      {/* HERO — A1 利益钩子 + eyebrow + 副标重写 */}
      <div className="hero">
        <div className="container hero-inner">
          <div className="hero-text">
            <span className="hero-eyebrow">
              <span className="hero-eyebrow-dot" aria-hidden="true" />
              For print shops &amp; POD sellers · Hands-on tested
            </span>
            <h1>
              Stop guessing which AI tool{' '}
              <em>actually prints well.</em>
            </h1>
            {/* hotfix 7/27 路 B 收尾 (千问诊断): 删 "the two numbers / print compatibility / e-commerce fit"。
                旧副标承诺了全站 107 篇 reviews 都不存在的两个维度 (printCompatibility/ecommerceFit 字段空)，
                右边 EvidenceCard 已删假进度条改 3 真 stat，左边副标还在承诺 = 首屏左右互搏 / 空头支票。
                新副标只承诺兑现得了的 (output quality + margin math 来自 reviews.json rating/price 字段)。
                改前画 SSoT: 旧钩子被哪些用户记忆点接? 现有 trust-bar "Updated July 2026" + EvidenceCard
                3 stat 块 + 4 FAQ 答案 + methodology 页 → 维度承诺足够,删掉空头不削弱。 */}
            <p>
              <b>{reviews.length} tools</b> tested on real print jobs and live stores — graded on output
              quality and margin math, not vendor demos. Verified 2026 pricing, no pay-to-rank.
            </p>
            <p className="trust-line">✓ Independent reviews from print &amp; e-commerce professionals — <Link href="/methodology/">see our methodology</Link></p>

            <div className="search-bar cmdk" id="search">
              <kbd className="cmdk-badge" aria-hidden="true">⌘K</kbd>
              <input
                type="text"
                placeholder="Search AI tools... (e.g. packaging design, Shopify)"
                value={search}
                onChange={e => setSearch(e.target.value)}
              />
              <button type="button">Search</button>
            </div>

            {/* Scenario tags — replaces duplicate category nav */}
            <div className="scenario-tags">
              {SCENARIO_TAGS.map(tag => (
                <Link key={tag.label} href={tag.href} className="scenario-tag">{tag.label}</Link>
              ))}
            </div>
          </div>

          {/* A2-2: 证据卡 — 替换 mini-vs，把双维度评分（Print Compatibility / E-Commerce Fit）顶到首屏 */}
          <EvidenceCard
            toolA="Printful"
            toolB="Printify"
            verdict="Printify wins on margin &amp; catalog (1,300+ items). Printful wins on quality &amp; branding."
            href="/compare/printful-vs-printify/"
          />
        </div>
      </div>

      {/* CATEGORY PHOTO CARDS */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2>Browse by Category</h2>
          </div>
          <div className="cat-grid">
            {CAT_CARDS.map(c => (
              <article key={c.slug} className="cat-card">
                <h3><Link href={`/category/${c.slug}/`}>{c.name}</Link></h3>
                <p>{c.desc}</p>
                <span className="cat-meta">{reviews.filter(r => r.categorySlug === c.slug).length} tools <i>→</i></span>
              </article>
            ))}
          </div>
        </div>
      </div>

      {/* SEARCH RESULTS */}
      {search.trim() && (
        <div className="section">
          <div className="container">
            <div className="section-header">
              <h2>Results for &ldquo;{search}&rdquo;</h2>
              <span style={{ color: 'var(--k-tertiary)', fontSize: '0.85rem' }}>{filtered.length} tool{filtered.length !== 1 ? 's' : ''} found</span>
            </div>
            {filtered.length === 0 ? (
              <p style={{ color: 'var(--k-tertiary)', padding: '20px 0' }}>No tools found. Try a different keyword.</p>
            ) : (
              <div className="review-grid">
                {filtered.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            )}
          </div>
        </div>
      )}

      {/* TOP COMPARISONS — duel-style cards, visually distinct from tool cards */}
      <div className="section section-alt">
        <div className="container">
          <div className="featured-panel">
            <div className="section-header">
              <h2>⚖️ Top Comparisons</h2>
              <Link href="/compare/" className="view-all">View All →</Link>
            </div>
            <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
              Head-to-head showdowns with clear winners — verified 2026 pricing, real cost math, no fence-sitting.
            </p>
            <div className="vs-grid">
              {comparisons.map(c => {
                const winner = COMPARISON_WINNERS[c.slug]
                return (
                  <article
                    key={c.slug}
                    className={`vs-card ${winner === 'A' ? 'vs-card-a-wins' : winner === 'B' ? 'vs-card-b-wins' : ''}`}
                  >
                    <div className="vs-card-battle">
                      <div className="vs-side">
                        <span className="vs-name">{c.toolA.name}</span>
                        <span className="vs-rating">★ {c.toolA.rating}</span>
                        {winner === 'A' && <WinnerBadge />}
                      </div>
                      <span className="vs-badge">VS</span>
                      <div className="vs-side">
                        <span className="vs-name">{c.toolB.name}</span>
                        <span className="vs-rating">★ {c.toolB.rating}</span>
                        {winner === 'B' && <WinnerBadge />}
                      </div>
                    </div>
                    <h3 className="vs-title"><Link href={`/compare/${c.slug}/`}>{c.title}</Link></h3>
                    <p className="vs-verdict">{c.quickVerdict.split('.')[0]}.</p>
                    <Link href={`/compare/${c.slug}/`} className="card-cta">Read Comparison →</Link>
                  </article>
                )
              })}
            </div>
          </div>
        </div>
      </div>

      {/* BEST OF LISTS — ranked roundups, third content type */}
      <div className="section">
        <div className="container">
          <div className="featured-panel green">
            <div className="section-header">
              <h2>🏆 Best Of Lists</h2>
              <Link href="/best/" className="view-all">View All →</Link>
            </div>
            <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
              Ranked roundups with clear winners — no pay-to-rank placements.
            </p>
            <div className="best-grid">
            {listicles.map(l => (
              <article key={l.slug} className="best-card">
                <span className="best-card-count">{l.items.length} ranked</span>
                <h3 className="best-card-title"><Link href={`/best/${l.slug}/`}>{l.title}</Link></h3>
                <div className="best-card-names">
                  {l.items.slice(0, 4).map((it, i) => (
                    <span key={i} className="best-card-name">#{i + 1} {it.name}</span>
                  ))}
                  {l.items.length > 4 && <span className="best-card-name more">+{l.items.length - 4} more</span>}
                </div>
                <Link href={`/best/${l.slug}/`} className="card-cta">See the Rankings →</Link>
              </article>
            ))}
            </div>
          </div>
        </div>
      </div>

      {/* SECTION 2: Vertical Featured — Print & Packaging */}
      <div className="section section-alt">
        <div className="container">
          <div className="vertical-featured">
            <div className="vertical-featured-header">
              <h2>🖨️ Best AI Tools for <strong>Print &amp; Packaging</strong></h2>
              <Link href="/category/ai-print-design/" className="view-all">View All →</Link>
            </div>
            {printTools.length > 0 ? (
              <div className="review-grid">
                {printTools.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            ) : (
              <p style={{ color: 'var(--k-tertiary)', fontSize: '0.9rem' }}>Print &amp; packaging reviews coming soon. <Link href="/submit-tool/">Suggest a tool.</Link></p>
            )}
          </div>

          <div className="vertical-featured" style={{ marginTop: 24 }}>
            <div className="vertical-featured-header">
              <h2>🛒 Best AI Tools for <strong>E-Commerce &amp; Shopify</strong></h2>
              <Link href="/category/ai-ecommerce/" className="view-all">View All →</Link>
            </div>
            {ecomTools.length > 0 ? (
              <div className="review-grid">
                {ecomTools.map(r => <ReviewCard key={r.slug} review={r} />)}
              </div>
            ) : (
              <p style={{ color: 'var(--k-tertiary)', fontSize: '0.9rem' }}>E-commerce reviews coming soon. <Link href="/submit-tool/">Suggest a tool.</Link></p>
            )}
          </div>
        </div>
      </div>

      {/* SECTION 3: All Tools (vertical-first sort) */}
      <div className="section">
        <div className="container">
          <div className="section-header">
            <h2>All Tool Reviews</h2>
            <span style={{ color: 'var(--k-tertiary)', fontSize: '0.85rem' }}>{reviews.length} tools reviewed</span>
          </div>
          <p style={{ color: 'var(--k-muted)', fontSize: '0.85rem', marginBottom: 20 }}>
            Sorted by relevance — print &amp; e-commerce tools shown first.
          </p>
          <div className="review-grid">
            {[...printTools, ...ecomTools, ...generalTools].map(r => (
              <ReviewCard key={r.slug} review={r} />
            ))}
          </div>
        </div>
      </div>

      {/* SECTION 4: CTA */}
      <div className="section section-alt">
        <div className="container" style={{ textAlign: 'center', maxWidth: 600, margin: '0 auto' }}>
          <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: 6, color: 'var(--k-deep)' }}>
            Have an AI tool for print shops or e-commerce?
          </h2>
          <p style={{ color: 'var(--k-tertiary)', marginBottom: 20, fontSize: '0.9rem' }}>
            We&apos;re always looking for great AI tools serving independent store owners and print businesses. Submit your tool for review.
          </p>
          <Link href="/submit-tool/" className="cta-button">Submit Your Tool →</Link>
        </div>
      </div>
    </>
  )
}

function ReviewCard({ review }) {
  const isVertical = review.slug.includes('print') || review.slug.includes('packag') ||
    review.slug.includes('kittl') || review.slug.includes('placeit') || review.slug.includes('looka') ||
    review.slug.includes('claid') || review.slug.includes('photoroom') ||
    review.slug.includes('ecom') || review.slug.includes('shopify')

  const isGenericCat = review.category === 'AI Writing' || review.category === 'AI Video' ||
    review.category === 'AI Voice' || review.category === 'AI Image'

  return (
    <article className="review-card">
      {/* hotfix 7/27 P1-3: affiliate-tag 挪到 card 右上角（不在 cta 行内，避免折行） */}
      {review.affiliateUrl && (
        <span className="affiliate-tag" aria-label="Affiliate link">Affiliate</span>
      )}
      <div className="card-badges">
        <span className="card-badge tested">Hands-on Tested</span>
        {isVertical && <span className="card-badge vertical">Print &amp; E-Com</span>}
      </div>
      <div className="card-meta">
        <span className={isGenericCat ? "card-cat generic" : "card-cat"}>{review.category}</span>
        <RatingBar rating={review.rating} />
        <span className="card-price">{review.price}</span>
      </div>
      <h3><Link href={`/${review.slug}/`}>{review.title}</Link></h3>
      <p className="card-desc">{review.metaDesc}</p>
      <div className="card-cta-group">
        <Link href={`/${review.slug}/`} className="card-cta card-cta-read">Read Full Review →</Link>
        {(() => {
          // W1-T1 度量埋点: aff-link class + data-merchant + data-link-id + UTM
          const aff = buildAffLinkAttrs(review, 'card-cta')
          if (!aff) return null
          return (
            <a
              href={aff.href}
              className={`${aff.className} card-cta card-cta-deal`}
              data-merchant={aff['data-merchant']}
              data-link-id={aff['data-link-id']}
              data-target={aff['data-target']}
              target="_blank"
              rel="nofollow sponsored"
            >
              Check Deal ↗
            </a>
          )
        })()}
        {/* K3 7/29 拍板 🟡⑤: 首页 review-card 加 organic "Visit Official Site ↗" 出口, 与详情页 [slug]/page.js L150-152 护栏对齐
            理由: 护栏意图 = "organic 链接不打 aff-link 标, 不加 UTM, 保护 organic SEO"
            rel="nofollow" (不含 sponsored) → inject-aff-link.mjs 守卫自动跳过, 不会被 rewrite
            href=review.visitUrl (原始商家直链, 不加 UTM) → §0 攒批不破, §0 护栏 organic 清洁
            7/30 03:43 user 推翻 7/30 03:40 撤首页 pxf 决定 (选 A 维持现状), pxf Check Deal 保留 + organic 出口保留 (两侧都生效) */}
        {review.visitUrl && (
          <a
            href={review.visitUrl}
            target="_blank"
            rel="nofollow"
            className="card-cta card-cta-visit"
            style={{ fontSize: '0.78rem', fontWeight: 500, color: 'var(--c-primary)' }}
          >
            Visit Official Site ↗
          </a>
        )}
      </div>
      {/* hotfix 7/27 P1-1: 进度条删除（107 篇 reviews 全无 printCompatibility/ecommerceFit 字段，硬编 8.8/8.2 是凭空捏造）
          待 reviews.json 真实数据补齐 + verify-cron 加"进度条全雷同"断言 后再绑字段。CSS 保留在 globals.css 备用。 */}
    </article>
  )
}
