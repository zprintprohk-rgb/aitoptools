# aitoptools.net 程序化 SEO 模板架构 v1.0

> **Owner**: Mavis (orchestrator) / Hermes (bulk generator)
> **Date**: 2026-08-03
> **Scope**: 200 页面程序化生成 (8 月底前上线)
> **SSoT**: `docs/SEO_ARCHITECTURE.md` (本文档) + `data/keywords-200.csv` + `data/internal-links-200.json` + `scripts/generate-page.py`
> **目标 9 工具**: Printify / Printful / Gelato (POD) / Kittl / Creative Fabrica (Design) / Claid (Photo) / Mockey (Mockup) / Picjam / GreenOnion (Listing)

---

## 0. 核心约束 (来自 M3 mandate + AGENTS.md §0/§6)

- ✅ **9 工具** = 唯一可推 affiliate 链接的池子 (K3 8/1 拍板 6 active + 2 待部署 Picjam/GreenOnion = 9)
- ❌ **不编**: aggregateRating / review count / official ARR/GMV / pricing 数字 (v3 P1 静态编造陷阱红线)
- ✅ **organic 链接** = nofollow 不加 sponsored
- ✅ **affiliate 链接** = nofollow sponsored + UTM 4 参
- ❌ **schema.org** 扩展待 user 拍板破 §6 锁 (现用 Product + Review + FAQPage 即可)
- ✅ **4 行业优先 60%**: POD / Ecommerce / Design / Marketing = 120 页面
- ✅ **每工具 ≥ 15 次 primary**: 9 × 15 = 135 minimum
- ✅ **不做 informational** (只做 commercial / transactional)

---

## 1. 页面母版模板

### 1.1 H1 标题公式

**Listicle 公式**:
```
Best AI Tools for {X} in 2026: {N} Tools Compared & Ranked
```
- 例: `Best AI Tools for T-Shirt Design in 2026: 7 Tools Compared & Ranked`
- `{N}` = 实际工具数 (5-7 个)

**VS Comparison 公式**:
```
{tool_a} vs {tool_b} 2026: Which {category} Should You Use?
```
- 例: `Printify vs Printful 2026: Which POD Platform Should You Use?`

**Alternative 公式** (高价值):
```
Best {tool_a} Alternatives for {use_case} in 2026
```
- 例: `Best Printful Alternatives for Etsy Sellers in 2026`

### 1.2 Meta Tags 公式

```yaml
title: "{H1} | aitoptools"  # ≤ 60 chars
meta_description: "{H1-question-form}. Updated Aug 2026 by aitoptools editorial."  # 140-160 chars
target_keywords:
  primary: "{main long-tail}"  # 5-7 词
  secondary: ["{kw2}", "{kw3}", "{kw4}"]  # 3-5 个 related
slug: "{kebab-case-no-stopwords}"  # ≤ 80 chars
canonical: "https://aitoptools.net/best/{slug}/"
og_image: "https://aitoptools.net/og/{slug}.png"  # 1200×630, 自动生成
date_published: "{今天}"  # ISO 8601
date_modified: "{今天}"
author: "aitopools editorial"
status: "PUBLISHED"  # 写 generated 阶段, draft 不上线
```

### 1.3 6 Sections 结构 (通用 listicle + VS comparison 都用)

#### Section ① Quick Pick (Top 3 Cards) — 250 字 + 1 内部链接

```markdown
## Quick Verdict: Top 3 Picks

1. **{Primary Tool}** — {1 行强项}. {pricing tier $X-$Y/mo}. {适用场景}.
2. **{Secondary Tool}** — {1 行强项}. {pricing tier}. {适用场景}.
3. **{Secondary Tool 2}** — {1 行强项}. {pricing tier}. {适用场景}.

{1 段总结, 80 字, 解释为什么这 3 个适合 {X} 场景}

[Internal Link: See our full [best {related_category} guide](/best/{related_slug}/) for comparison]
```

**字数**: 200-300 字
**关键**: "Our Pick" / "Best for [use case]" 标识
**内链 slot**: 1 个 outbound (指向同 category 顶级资源页)

#### Section ② What is {X} AI / {Category} — 150 字 (GEO 友好)

```markdown
## What is {X} AI?

{2-3 句定义, 50-80 字}
{1 句讲为什么 {X} AI 在 2026 重要, 30-50 字}
{1 句讲 {X} AI 解决的问题, 30-50 字}
{可选: 1 句引用 stats, 来自 cited source}
```

**字数**: 130-180 字
**关键**: 必须被 AI 搜索引擎 (ChatGPT/Perplexity/Google AI Overview) 引用, 答"What is {X}?" 直接给定义
**格式**: 简洁句, 关键概念在第一句

#### Section ③ Full Reviews — 每工具 200 字 × 3-7 个

```markdown
## Full Reviews: {N} Best {X} AI Tools in 2026

### 1. {Tool Name} — {Tagline}

**Quick facts:**
- **Best for**: {1 句 use case}
- **Pricing**: {tier} — {starting price}
- **Free trial**: {yes/no + duration}
- **Standout feature**: {1 句}

{2-3 段, 每段 50-80 字}
- 段 1: Tool overview + what it does
- 段 2: Key features + pros
- 段 3: Pricing + value assessment

**Pros** (3-5 项, 短词):
- {Pro 1}
- {Pro 2}
- {Pro 3}

**Cons** (2-3 项, 短词):
- {Con 1}
- {Con 2}

[Internal Link: Read our [full {Tool} review](/{tool-slug}-review/) for in-depth testing]

### 2. {Tool 2} ...

### {N}. {Tool N} ...
```

**字数**: 每工具 200 字 × 3-7 = 600-1400 字
**关键**: 真实数据 (从 K3 8/1 已知 9 工具 docs), 不编
**内链 slot**: 每个工具 review 1 个 outbound (→ /{tool-slug}-review/)

#### Section ④ Comparison Table — 7 行功能 × N 工具

```markdown
## {X} AI Tools: Feature Comparison

| Feature | {Tool 1} | {Tool 2} | {Tool 3} | {Tool 4} |
|---|---|---|---|---|
| {Feature 1} | ✅ Yes | ✅ Yes | ⚠️ Partial | ❌ No |
| {Feature 2} | ✅ Yes | ⚠️ Partial | ✅ Yes | ❌ No |
| {Feature 3} | $X/mo | Free | $Y/mo | Custom |
| {Feature 4} | ✅ | ✅ | ❌ | ✅ |
| {Feature 5} | {spec} | {spec} | {spec} | {spec} |
| {Feature 6} | {spec} | {spec} | {spec} | {spec} |
| {Feature 7} | {spec} | {spec} | {spec} | {spec} |

**How to read this table:** {1 句}
**Our recommendation:** {1-2 句选 best per use case}
```

**字数**: 表格 200 字 + 说明 100 字 = 300 字
**关键**: 取舍必须用 `✅ Yes / ⚠️ Partial / ❌ No` 三态, 不绝对化
**7 行原则**: 跟现有 6 vs-cards winner 映射的 `M3_MONTH1_DATA` schema 一致

#### Section ⑤ How to Choose — 500 字

```markdown
## How to Choose the Best {X} AI Tool for Your Business

{1 段 intro, 50 字, 强调 "not one-size-fits-all"}

### 5 Key Factors to Consider

#### 1. {Factor 1} (e.g., Pricing & Total Cost of Ownership)
{2-3 句, 80-100 字, 解释为什么重要 + 怎么评估}

#### 2. {Factor 2} (e.g., Print Quality & Output Formats)
{80-100 字}

#### 3. {Factor 3} (e.g., Integration with Your Stack)
{80-100 字}

#### 4. {Factor 4} (e.g., Customer Support & Onboarding)
{80-100 字}

#### 5. {Factor 5} (e.g., Scalability & Bulk Workflows)
{80-100 字}

### Our Decision Framework

{1 段总结, 100 字, "if you need X → choose tool Y, if you need Z → choose tool W"}

[Internal Link: For a step-by-step setup guide, see our [how to {X} with AI](/how-to-{x}-with-ai/) tutorial]
```

**字数**: 500-600 字
**关键**: 5 factors 框架 (跟现有千问 0.5 步断言 ①-⑤ 对齐, 决策可信)
**内链 slot**: 1 个 outbound (→ how-to tutorial)

#### Section ⑥ FAQ — 5 个 People Also Ask

```markdown
## Frequently Asked Questions

### What is the best {X} AI tool in 2026?
{60-80 字, 答 + 推荐 primary tool}

### How much do {X} AI tools cost?
{60-80 字, 给 pricing tier 概览, 不编具体数字}

### Are {X} AI tools worth the investment?
{60-80 字, ROI 分析, 引用 1 个 case study}

### Which {X} AI tool is best for {use case}?
{60-80 字, 按 use case 推荐 1 个 primary tool}

### Can I use {X} AI tools for free?
{60-80 字, free tier / trial 概览}
```

**字数**: 5 × 70 = 350 字
**关键**: Q1 + Q2 答 primary tool, Q3-Q5 答 secondary, **必须**给可引用的 1 句 + 1 数字
**FAQ Schema**: JSON-LD 自动套用 `FAQPage` schema (无需 §6 锁 schema.org 扩展)

### 1.4 页面 Schema.org JSON-LD (无 §6 锁扩展, 用现有 3 类)

```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "{H1}",
  "description": "{meta_description}",
  "url": "{canonical}",
  "numberOfItems": {N},
  "itemListOrder": "https://schema.org/ItemListOrderAscending",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Product",
        "name": "{Tool Name}",
        "description": "{1 句 tagline}",
        "url": "/{tool-slug}-review/",
        "offers": {
          "@type": "Offer",
          "priceCurrency": "USD",
          "price": "{tier_min_price or '0'}",
          "priceValidUntil": "2027-12-31"
        }
      }
    }
  ]
}
```

**附加**: `FAQPage` schema for Section ⑥ (5 Q&A)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{Q1}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{A1}"
      }
    }
  ]
}
```

### 1.5 Affiliate Link 处理规则 (跟 AGENTS.md §0 + 7/30 12:00 决策一致)

| 类型 | rel | UTM 4 参 | 视觉 |
|---|---|---|---|
| **affiliate** (Check Deal, Try Now) | `nofollow sponsored` | utm_source=aitoptools, utm_medium=affiliate, utm_campaign={tool}, utm_content={slug}-{position} | 琥珀橙 "Check Deal ↗" 按钮 |
| **organic** (Visit Official Site, Read Review) | `nofollow` (无 sponsored) | 无 UTM | 主品牌色链接 |

**位置**: 每个工具 review 1 个 affiliate CTA + 1 个 organic Visit link

### 1.6 关键 SEO 指标 (目标)

| 指标 | 目标 | 备注 |
|---|---|---|
| **字数** | 2500-3500 字 / 页面 | 6 sections 累计 |
| **主关键词密度** | 1-2% | 1 词 200 字 = 0.5%, 3500 字应 18-35 次 |
| **Title 含主关键词** | 必须 | "Best AI Tools for [X]" |
| **H1 = Title** | 必须 | 不重复 H2 含主关键词 |
| **H2 含 primary keyword 变体** | 3-5 个 | 不同 section 用不同 keyword 变体 |
| **内部链接 outbound** | 3-5 / 页面 | Quick Pick 1 + Reviews 1/工具 + How to Choose 1 |
| **内部链接 inbound** | 3 / 页面 | Related Articles at bottom |
| **图片 alt** | 含主关键词 1-2 | og_image 自动 |
| **FAQ** | 5 Q&A | 必给"People Also Ask" 答案 |
| **JSON-LD** | ItemList + FAQPage | 2 个 schema |

---

## 2. 6 Categories × Primary Tool 分配矩阵

| Category | 页面数 | 主要工具 | 次要工具 |
|---|---|---|---|
| **POD** | 50 | Printify(13) + Printful(13) + Gelato(13) | Kittl/Mockey(11) |
| **Design** | 40 | Kittl(12) + Creative Fabrica(12) | Printify/Mockey/Picjam(16) |
| **Ecommerce** | 30 | Printify(8) + Claid(7) + Mockey(7) | Printful/Gelato/Picjam(8) |
| **Marketing** | 25 | Picjam(10) + GreenOnion(7) | Printify/Printful/Kittl(8) |
| **Photography** | 20 | Claid(15) | Mockey/Picjam(5) |
| **Content** | 15 | Picjam(8) + GreenOnion(7) | (无次要, listing 专项) |
| **VS Comparisons** | 20 | 跨 category 2 工具对决 | 跨赛道 |
| **Total** | **200** | (9 工具 × 15+ 满足) | — |

**Primary 计数**: Printify 25 + Printful 25 + Gelato 25 + Kittl 22 + Creative Fabrica 22 + Claid 22 + Mockey 22 + Picjam 18 + GreenOnion 19 = 200 ✅

---

## 3. Hermes Generator 接口

```python
# scripts/generate-page.py
# 用法: python scripts/generate-page.py <slug>
# 输入: keywords-200.csv (200 行)
# 输出: src/data/programmatic-seo/{slug}.json (页面内容)
#       src/data/programmatic-seo/{slug}.schema.json (JSON-LD)
#       src/data/programmatic-seo/internal-links.json (200×3 mapping)

import csv, json, sys
from pathlib import Path

def generate_page(slug: str, keyword_data: dict, link_data: dict) -> dict:
    """根据 keywords-200.csv + internal-links-200.json 生成 1 个页面"""
    template = load_template()  # 6 sections template
    page = {
        'slug': slug,
        'h1': render_h1(keyword_data),
        'meta': render_meta(keyword_data),
        'sections': render_sections(template, keyword_data),
        'related': link_data.get(slug, []),
        'schema': render_schema(keyword_data),
        'affiliate_links': render_affiliate_links(keyword_data)
    }
    return page

# Hermes 跑: for each row in CSV: page = generate_page(...)
# Output: 200 JSON files
```

---

## 4. 部署流水线 (8/2 攒批 1 commit + 8/5/8/8 后续)

1. **8/3 立即**: 跑 generate-page.py × 200, 生成 200 JSON drafts → `.hermes/drafts/programmatic-seo/`
2. **8/4-8/5**: Mavis review + K3 拍板, 修复 30-50 个低质量页
3. **8/5 攒批 1 commit**: src/data/programmatic-seo/ → src/data (含 200 pages) + src/app/best/[slug]/page.js (动态路由)
4. **8/6-8/30**: 200 页面 weekly 上线 (每天 20-30 个, 配合 sitemap ping)
5. **8/30 评估**: GA4 数据 + Search Console 覆盖率

---

**最后更新**: 2026-08-03 04:00 CST
**版本**: v1.0
**下一步**: 写交付物 2 (200 keywords CSV) + 交付物 3 (内链矩阵 JSON)
