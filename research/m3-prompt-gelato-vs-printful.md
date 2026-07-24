# M3 建页任务：《Gelato vs Printful》对比页

> **当前动作支撑赚钱目标**: CPA/CPS 佣金/月 — 新增 1 个深度对比页，Gelato 联盟链接获批后可立即变现；Printful 真链接已就绪。
> **任务路由**: M3 深度内容（对标 mockey-vs-placeit 结构）
> **算力窗口约束**: 必须在夜间 18:00-08:00 或午间 12:05-13:30 执行

---

## 一、前置状态（K3 已核实）

### 1.1 联盟审批状态

| 项目 | 状态 | 事实来源 |
|---|---|---|
| **PartnerStack 网络资格** | 🟡 **待处理** | WebBridge snapshot 确认 dash.partnerstack.com/home 显示「PartnerStack 网络审批状态：待处理」「您的计划申请处于搁置状态」 |
| **Gelato 重申** | 🟡 **待审批（被搁置）** | 2026-07-24 重申已提交，因 PartnerStack 网络审批未过，申请处于搁置状态 |
| **Deel** | 🟡 **已提交（被搁置）** | 同样因 PartnerStack 网络审批未过，申请处于搁置状态 |

**根因诊断**: PartnerStack 网络审批（平台级账户审核）是瓶颈。Printify 之前能获批可能是因为其审批在网络审批重新审查之前完成，或走独立流程。所有新申请（Gelato、Deel）都被系统拦截在网络审批通过前。

**用户行动卡片**: 请自行登录 dash.partnerstack.com 跟进网络审批状态，或联系 PartnerStack 支持（support@partnerstack.com）询问审批进度。网络审批通过后，Gelato 和 Deel 的申请会自动提交。

### 1.2 现有 Gelato 相关页面核查

- ✅ `src/data/comparisons.json` 已有 `printful-vs-gelato`（完整页面，slug: printful-vs-gelato）
- ✅ `src/data/reviews.json` 已有 `gelato-review`（独立评测页）和 `printful-review`
- ✅ `src/data/listicles.json` 中 `printful-alternatives` 和 `printify-alternatives` 榜单均引用 Gelato
- ❌ **尚无 `gelato-vs-printful` slug** — 本次新建

> 注意：`printful-vs-gelato` 和 `gelato-vs-printful` 是同一对比的两种搜索意图。已有前者从 Printful 视角出发，新建后者从 Gelato 视角出发，覆盖 "Gelato vs Printful" 搜索词。

### 1.3 联盟链接（AFFILIATE_LINKS.json 确认）

```json
{
  "printful.com": "https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a",
  "gelato.com": ""  // 空串 = 未获批
}
```

**链接规则**:
- Printful CTA 用真联盟链接：`https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a`
- Gelato CTA 用官网裸链：`https://gelato.com` + HTML 注释 `<!-- AFFILIATE-TODO: replace with PartnerStack link once approved -->`

---

## 二、页面规格（严格复用 mockey-vs-placeit 结构）

### 2.1 基础字段

```json
{
  "slug": "gelato-vs-printful",
  "title": "Gelato vs Printful (2026): Which POD Platform Wins for Your Store?",
  "metaDesc": "Gelato vs Printful compared for 2026: pricing, product catalogs, print quality, local production vs in-house factories, shipping speed, branding, and which POD platform Etsy & Shopify sellers should choose.",
  "datePublished": "2026-08-01",
  "dateModified": "2026-08-01"
}
```

### 2.2 toolA / toolB（注意：本次 toolA = Gelato，toolB = Printful）

```json
"toolA": {
  "name": "Gelato",
  "reviewSlug": "gelato-review",
  "visitUrl": "https://gelato.com",
  "affiliateUrl": "",
  "rating": 4.4
},
"toolB": {
  "name": "Printful",
  "reviewSlug": "printful-review",
  "visitUrl": "https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a",
  "affiliateUrl": "",
  "rating": 4.5
}
```

### 2.3 Quick Verdict

从 Gelato 视角重写（约 80-100 词），核心信息：
- Choose Gelato if you sell internationally or want lower base costs: 140+ local production hubs in 32 countries, base prices 15–35% below Printful's, Gelato+ at $19.99/mo annual.
- Choose Printful if you're building a premium brand: in-house production, best print consistency, unmatched branding depth (labels, pack-ins, branded packaging), but 15–35% higher base costs.
- Both free to start; order samples to compare.

### 2.4 Comparison Table（8 行，从 Gelato 视角）

复用 printful-vs-gelato 的事实数据，但 A/B 列互换，winner 相应调整：

| dimension | a (Gelato) | b (Printful) | winner |
|---|---|---|---|
| Pricing | Free plan; Gelato+ $19.99/mo annual / $23.99 monthly, up to 25% off; lower base costs 15–35% | Free plan; Growth $24.99/mo (free after $12K/yr), up to 33% off; base costs 15–35% higher | Gelato |
| Product catalog | ~250 curated products; strongest in wall art & paper goods | 300+ products across 25+ categories; strongest in apparel & embroidery | Printful |
| Print quality | Vetted partner network, consistently strong; gallery-grade wall art | In-house production, one QA standard, ~0.24% reshipment rate | Printful |
| Production & shipping | 24–72 hour production typical; 90% of orders produced locally in 32 countries | 2–5 business day production from 12 centers; US delivery typically 5–10 business days | Gelato |
| International selling | 140+ hubs, automatic routing, local production worldwide | Strong inside US/EU zones; cross-border elsewhere | Gelato |
| Branding options | Branded inserts on Gelato+; limited beyond that | Inside/outside labels, hang tags, pack-ins, branded packaging & tracking | Printful |
| Integrations & support | Shopify, Etsy, WooCommerce, Wix, BigCommerce + API; 24/7 support | Shopify, Etsy, WooCommerce, Amazon, eBay, Wix + API; 24/7 single-company support | Tie |
| Embroidery | Limited embroidery options | Best-in-class embroidery depth | Printful |

### 2.5 Content（HTML 长文）

从 Gelato 视角重写 printful-vs-gelato 的内容，结构严格对齐 mockey-vs-placeit：

1. **Intro paragraph**（~150 词）: Gelato 和 Printful 都位于 POD 质量端，但架构相反 — Gelato 是 140+ 合作伙伴的分布式网络，Printful 是自有工厂垂直整合。从 Gelato 视角切入。
2. **Pricing & Plans**（~300 词）: Gelato 更便宜 — 订阅 ($19.99 vs $24.99) 和基础成本都更低。Printful 的 Growth 折扣更深 (33% vs 25%) 且 $12K/年后免费。
3. **Product Catalog**（~200 词）: Printful 300+ 产品 vs Gelato ~250。Gelato 在墙艺和纸品上最强。
4. **Print Quality**（~200 词）: Printful 自有工厂一致性略胜 (0.24% 重发率)。Gelato 的审核合作伙伴网络非常接近，墙艺达到画廊级。
5. **Shipping & Fulfillment**（~200 词）: Gelato 全球更快 — 90% 订单本地生产，2-5 天送达。Printful 12 个固定中心，跨区域较慢。
6. **Branding**（~150 词）: Printful 深度 branding 无可匹敌。Gelato+ 只有 branded inserts。
7. **Integrations**（~100 词）: 两者都覆盖 Shopify/Etsy/WooCommerce。Printful 多 Amazon/eBay。
8. **Which Should You Choose?**（~150 词）: 决策框架 — 国际/墙艺/低成本 → Gelato；高端品牌/刺绣/branding → Printful。

所有数据必须引用 printful-vs-gelato 已有页面中的核实数据，不得编造新数字。

### 2.6 FAQs（7 条，从 Gelato 视角改写）

1. Is Gelato cheaper than Printful? → Yes, on both subscriptions and base costs...
2. Which has better print quality, Gelato or Printful? → Printful slight edge on consistency...
3. Is Gelato or Printful better for international orders? → Gelato, 140+ hubs...
4. Which ships faster, Gelato or Printful? → Gelato globally, comparable US/EU...
5. Can I use both Gelato and Printful at the same time? → Yes, hybrid setup...
6. Does Gelato have custom branding like Printful? → Only partially...
7. Is Gelato+ or Printful Growth worth it first? → Gelato+ pays back sooner...

### 2.7 Picks（3 级推荐卡）

```json
"picks": [
  {
    "type": "top",
    "name": "Gelato",
    "tagline": "Lower base costs and global local production for international sellers",
    "rating": 4.4,
    "anchor": "#at-a-glance"
  },
  {
    "type": "also",
    "name": "Printful",
    "tagline": "Premium branding and print consistency for serious brands",
    "rating": 4.5,
    "anchor": "#full-reviews"
  },
  {
    "type": "budget",
    "name": "Gelato Free plan",
    "tagline": "Free plan with lower base product costs than Printful",
    "rating": 4.4,
    "anchor": "#pricing"
  }
]
```

### 2.8 Features（8 行功能矩阵，a = Gelato, b = Printful）

```json
"features": [
  {"feature": "Free plan with no monthly fee", "a": "yes", "b": "yes"},
  {"feature": "Local production in 30+ countries", "a": "yes", "b": "partial"},
  {"feature": "Lower base product costs", "a": "yes", "b": "no"},
  {"feature": "In-house production facilities", "a": "no", "b": "yes"},
  {"feature": "Custom labels & pack-ins", "a": "partial", "b": "yes"},
  {"feature": "Embroidery options", "a": "partial", "b": "yes"},
  {"feature": "Membership discounts (paid plan)", "a": "yes", "b": "yes"},
  {"feature": "Branded packaging & tracking page", "a": "no", "b": "yes"}
]
```

### 2.9 Pricing（带 Better Value 标注）

```json
"pricing": {
  "betterValue": "a",
  "rows": [
    {"label": "Free plan", "a": "$0 — full platform access", "b": "$0 — full platform access"},
    {"label": "Paid plan", "a": "Gelato+ $19.99/mo (annual) / $23.99/mo", "b": "Growth $24.99/mo (free after $12K/yr)"},
    {"label": "Base product costs", "a": "Lower (15–35% below Printful)", "b": "15–35% higher"},
    {"label": "Max product discount", "a": "Up to 25% off", "b": "Up to 33% off"}
  ]
}
```

Better Value 标给 Gelato（订阅更便宜，基础成本更低）。

---

## 三、WhyTrustUs 模块

页底 FAQ 前固定插入 WhyTrustUs 模块，文案复用 mockey-vs-placeit 结构，调整关键词为 POD 平台对比：

> "We test every tool hands-on before writing. This comparison is based on verified 2026 pricing from both platforms' official sites, independent quality analyses, and real seller feedback. We earn commissions through affiliate links — this never affects our ratings or recommendations."

---

## 四、联盟链接处理清单

| CTA 位置 | 链接 | 状态 |
|---|---|---|
| Printful CTA | `https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a` | ✅ 真链接 |
| Gelato CTA | `https://gelato.com` | ⚠️ 裸链占位 |
| Gelato 页内所有 href | `https://gelato.com` | ⚠️ 裸链占位，加 `<!-- AFFILIATE-TODO: replace once approved -->` |

**后续管线**: Gelato PartnerStack 获批后 → 链接入 AFFILIATE_LINKS.json → `python scripts/replace_affiliate_links.py --apply` → `python scripts/affiliate_link_audit.py` 验证。

---

## 五、产出要求

1. **目标文件**: 将完整 JSON 对象追加到 `src/data/comparisons.json` 数组末尾（在闭合 `]` 前插入新对象）。
2. **校验**: 运行 `python scripts/validate_content_data.py` 确保全过。
3. **构建自检**: `npm run build` 页数只增不减（当前 113 页 → 应变为 114 页）。
4. **不攒批 push**: 本页单独不入库，等 Gelato 链接替换后同批次 push（遵守 1 push/天 规则）。
5. **事实红线**: 所有定价、数字、百分比必须与 `printful-vs-gelato` 已有页面一致，不得编造新数据。

---

## 六、参考数据源

- `src/data/comparisons.json` line 357-532: `printful-vs-gelato`（事实来源，反向改写）
- `src/data/reviews.json` line 1956-1998: `gelato-review`（补充细节）
- `src/data/reviews.json` line 2024-2070: `printful-review`（补充细节）
- `AFFILIATE_LINKS.json`: 联盟链接真值
- `src/data/comparisons.json` line 889-1081: `mockey-vs-placeit`（结构模板）

---

*K3 前置任务完成时间: 见本文件元数据*
*PartnerStack 网络审批状态: 待处理（需用户跟进）*
*Gelato 联盟链接: 待替换（裸链占位）*
