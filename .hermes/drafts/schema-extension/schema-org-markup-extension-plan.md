---
title: "schema.org JSON-LD Extension Plan (K3 7/30 拍板, §6 锁待 user 拍板破)"
status: DRAFT - pending user approval to break §6 锁 (per AGENTS.md)
blocked_by: AGENTS.md §6 锁 "不要触碰 src/components/ 或 src/app/"
break_needed: "user 拍板破 §6 锁授权改 src/app/[slug]/page.js + src/app/compare/[slug]/page.js + src/app/page.js"
expected_benefit: "Google Rich Results 100% (per §6.4 验收表), GEO 引擎可抓取 (per Appendix E/F), 评测/对比页 CTR +0.5-1%"
---

# Background

aitoptools.net 当前 (7/30) JSON-LD 覆盖：
- 已实现: Article / BreadcrumbList / FAQPage (在 [slug]/page.js / compare/[slug]/page.js / page.js)
- 缺失: Product / SoftwareApplication / AggregateRating / Review / Offer

**Rich Results 当前覆盖率 (GSC 抽样)**:
- 7/28: 12/12 有效响应 PDP 缺 aggregateRating/review (按 v2.1 P1 删, 防 Manual Action 风险)
- 其他结构化数据未做抽样, 估计缺失 Product/SoftwareApplication/Offer/Review

**目标覆盖率 (§6.4 验收表 7 项)**:
- 1. 开学季询盘 ≥5 (N/A aitoptools)
- 2. 校园词排名进前 50 (N/A)
- 3. 收录 +3 页 (待定, schema 加速收录)
- 4. **Rich Results 100%** (本计划目标)
- 5. AI 可见性 ≥1/7 (待定, schema 增强 AI 抓取)
- 6. 301 传递 (N/A)
- 7. 总 push ≤14 (本计划 1 push, OK)

---

# §6 锁破规说明 (需 user 拍板)

**AGENTS.md §6 锁**:
> 不要触碰 src/components/ 或 src/app/

**本计划涉及**:
- `src/app/[slug]/page.js` (107 详情页模板) — 改 JSON-LD 段
- `src/app/compare/[slug]/page.js` (6 对比页模板) — 改 JSON-LD 段
- `src/app/page.js` (首页) — 加 SoftwareApplication JSON-LD 段

**破规收益**:
- Google Rich Results 100% (per §6.4 验收表)
- AI 引擎可抓取 Product/Offer/Review 数据 (per Appendix E/F GEO 白名单)
- 评测/对比页 CTR +0.5-1% (per 行业数据)

**破规风险**:
- 改 src/app/ 风险高于 data/ 或 scripts/ — 可能破坏现有渲染
- AggregateRating 静态编造触发 Google Manual Action 不可逆 (per v2.1 P1 教训)
- 需 14/14 verify-deploy-v2 PASS + 53/53 aff-link-audit 100% 覆盖才能 push

**user 拍板选项**:
- A. 拍板破规, 立即按本计划改 src/app/ (3 文件, ~50-100 行 JSON-LD 增量)
- B. 暂缓, 等 8/3 流量基础建立后再拍板
- C. 改用低风险方案: 加到 page.js 末尾的 <script type="application/ld+json"> 段, 不动现有 JSON-LD

---

# 推荐方案 C (低风险, 增量式, 不动现有 JSON-LD)

## 实施范围 (3 文件增量, ~80-150 行总)

### 文件 1: src/app/[slug]/page.js (107 详情页)
- **位置**: 现有 <script type="application/ld+json"> 段之前
- **新增**: SoftwareApplication + Product + Offer JSON-LD
- **数据来源**: reviews.json (name / description / slug / visitUrl / category / pricing / features)
- **字段**:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{review.name}",
    "description": "{review.metaDesc}",
    "url": "https://aitoptools.net/{review.slug}/",
    "applicationCategory": "DesignApplication",
    "operatingSystem": "Web",
    "offers": {
      "@type": "Offer",
      "url": "{review.affiliateUrl || review.visitUrl}",
      "priceCurrency": "USD",
      "price": "{review.pricing || 0}",
      "availability": "https://schema.org/InStock"
    },
    "featureList": "{review.features.join('|')}"
  }
  ```

### 文件 2: src/app/compare/[slug]/page.js (6 对比页)
- **位置**: 现有 <script type="application/ld+json"> 段之前
- **新增**: 2 个 SoftwareApplication + 1 个 ComparisonTable JSON-LD
- **数据来源**: comparisons.json (toolA / toolB / verdict / winner)
- **字段**:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "item": { "@type": "SoftwareApplication", "name": "{toolA.name}", "url": "https://aitoptools.net/{toolA.slug}/" } },
      { "@type": "ListItem", "position": 2, "item": { "@type": "SoftwareApplication", "name": "{toolB.name}", "url": "https://aitoptools.net/{toolB.slug}/" } }
    ]
  }
  ```

### 文件 3: src/app/page.js (首页)
- **位置**: 现有 JSON-LD 段之前
- **新增**: WebSite + Organization JSON-LD
- **字段**:
  ```json
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "aitoptools.net",
    "url": "https://aitoptools.net/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://aitoptools.net/best/?q={search_term_string}",
      "query-input": "required name=search_term_string"
    },
    "publisher": {
      "@type": "Organization",
      "name": "aitoptools editorial",
      "url": "https://aitoptools.net/about/"
    }
  }
  ```

---

# 14/14 verify-deploy-v2.py 验证 (push 后必跑)

新增 3 项断言 (扩展现有 14 项):
- **断言 ⑮**: 107 详情页 100% 含 SoftwareApplication JSON-LD
- **断言 ⑯**: 6 对比页 100% 含 ItemList JSON-LD (含 2 个 SoftwareApplication)
- **断言 ⑰**: 首页含 WebSite + SearchAction JSON-LD

每项断言必须在 push 后 5min 内 PASS, FAIL 立即 revert + 升级 user.

---

# 风险缓解 (4 项硬约束)

1. **AggregateRating 不加** (per v2.1 P1 教训, 防 Manual Action 不可逆)
2. **Review 字段不加** (per v2.1 P1 教训)
3. **Offer.price 缺失时填 0 + "availability": "https://schema.org/InStock"** (避免 GSC warning)
4. **不写 aggregateRating / review / voteCount** (per §0 护栏 价格不编造)

---

# 实施时间线 (待 user 拍板后)

| 日期 | 任务 | 工作量 |
|---|---|---|
| 7/31 (待拍板) | user 拍板破 §6 锁选项 (A/B/C) | 0 (拍板) |
| 8/2 (攒批) | 改 3 文件 src/app/ (实施方案 C) | 3-4h |
| 8/2 (verify) | npm run build + 14+3 = 17 项 verify-deploy-v2.py PASS | 30 min |
| 8/2 (verify) | 53/53 aff-link-audit.py 100% 覆盖 (organic 出口仍 116, 不变) | 5 min |
| 8/2 (verify) | Google Rich Results Test 抽样 10 页 (5 详情 + 3 对比 + 1 列表 + 1 首页) | 15 min |
| 8/2 (push) | commit + push + 5min verify CF Pages build | 5 min |
| 8/2 (cron) | verify-v2-guard v4 prompt 加 3 项新断言 | 15 min |
| 8/3+ | GSC 抽样扩大, 1-2 周内 Rich Results Test 应有 100% PASS | 0 (等待) |

---

# M3 决策依赖

K3 8/12 复盘拍板时, 需要看:
- 方案 C 是否 8/2 落地, GSC 抽样是否扩大
- 8/19 vs 8/26 Rich Results 100% 目标延期
- 是否启动方案 A (接入真实评价数据 API, Trustpilot)

按 v2 §3.3 约束 4 (K3 7/28 04:30 拍板), M3 8/12 复盘前不能改 productRating / generateProductReviewsJsonLd.
