# legit-check 页模板 v2 — 公开评分 Rubric 版（2026-08-18 起草，D13 拍板即用）

> **状态**: D13 待拍板草稿。依据 DEEPDIVE-2026-08-17-GEO-SEO-MASTERPLAN §四-引擎1 + §二-8 竞品对标（peptideprices.net /is-legit/ 公开 rubric 模式、trtpicks.com 数据库对比）。
> **升级自**: `.hermes/drafts/legit-template.md`（T3, 2026-08-17）。v1 硬约束全部继承，v2 新增：①公开评分 rubric ②answer-first 结构 ③方法页骨架 ④每篇可执行字段清单。
> **适用**: legit-queue.md 首批 10 篇统一执行；每篇上线前事实核实（AutoClaw），核实红线不降级。
> **存量页兼容**: 已部署的 `is-magicdrop-legit`（8/17 扩写，~3,420 词）按核心更新滚动期纪律——本轮只加内容不改模板结构；下轮更新时补 rubric 评分卡 + answer-first 结论框。

---

## 1. 公开评分 Rubric（独立成节 — /methodology/ 引用源）

> 本节全文可直接复制进方法页（§3），每篇 legit 页的评分卡（blocks table）按此计算。

### 1.1 权重与数据要求

| 维度 | 权重 | 数据要求 | 来源 URL 必带? |
|---|---|---|---|
| Trustpilot 声誉 | **30%** | 评分 (X/5) + 评论数 + 档案活跃度（近 90 天新增评论） | ✅ 必须（trustpilot.com/review/{domain}） |
| 退款与支付安全 | **25%** | 官方退款政策页 + 支付方式 + 投诉模式（扣款不退类） | ✅ 必须（官方政策页 / BBB / Trustpilot 投诉） |
| 公司透明度 | **25%** | 公司名/注册地/注册号/地址/负责人 + 域名 WHOIS/注册年限 | ✅ 必须（About/Contact/BBB 档案） |
| 实测体验 | **20%** | 我们的注册/下单/客服记录（截图/订单号可复述） | 实测记录（截图路径）+ 二手实测须带源 |

### 1.2 评分标准分档（每维 0-2 分）

**① Trustpilot 声誉 (30%)**
- **2 分**: 评分 ≥4.0 且评论数 ≥500，且近 90 天有新增评论（档案活跃，口碑+声量双达标）
- **1 分**: 3.0 ≤ 评分 < 4.0；或评论数 50–499；或评分高但评论数 <50（样本偏差风险，需标注）
- **0 分**: 评分 <3.0 / 评论数 <50 / 无 Trustpilot 档案 / 档案显示停运 / 30 天负面率 >30% 的集中差评风暴
- **规则**: 无档案 ≠ 骗局，但必须如实陈述「X has no Trustpilot profile」（平台已关闭信号之一，magicdrop 案例模式）；**无来源 URL 该维直接 0 分且不得写入数据**

**② 退款与支付安全 (25%)**
- **2 分**: 公开退款政策页（时限+条件明确），支持买家保护型支付（信用卡/PayPal/Stripe/Shopify Pay），无「扣款不退」投诉模式
- **1 分**: 退款政策含糊 / 仅 store credit / 限时 <14 天 / 部分支付方式无保护
- **0 分**: 无公开退款政策 / 无客服渠道 / 仅不可逆支付（crypto/银行转账）/ 「扣款不退」投诉簇且无官方回应

**③ 公司透明度 (25%)**
- **2 分**: 公司实体信息完整公开（可查注册号或 BBB 档案），域名注册 ≥3 年，WHOIS 可查
- **1 分**: 有公司名但注册信息/地址不全；域名注册 1–3 年
- **0 分**: 完全匿名 / 域名 <1 年 / WHOIS 隐私隐藏且无公司实体信息 / **域名停运或转让中（parked/Afternic 停放页 = 平台关闭信号）**

**④ 实测体验 (20%)**
- **2 分**: 完整实测（注册+下单+收货 或 注册+客服对话+界面走查），有截图与可复述流程
- **1 分**: 部分实测（仅免费注册+界面走查+客服响应测试）；或二手实测（真实用户投诉整理，每条带来源 URL）
- **0 分**: 无任何实测（纯 desk research）→ 该篇强制标注 "desk-research only"，**且总分上限 60，不得进入「推荐」档**

### 1.3 总分与档位

```
Total = (T×0.30 + R×0.25 + C×0.25 + H×0.20) × 50   （T/R/C/H 各为 0-2 分）→ 0-100
```

| 总分档位 | 结论口径 | 页面措辞示例 |
|---|---|---|
| **≥80** | ✅ **推荐 (Recommended)** | "X is legit and safe to use for POD sellers…" |
| **60–79** | ⚠️ **有条件推荐 (Conditional)** | "X is legitimate, but only if…"（列明条件） |
| **<60** | ❌ **不推荐 (Not Recommended)** | "X fails our trust checks…"（列明失败维度） |
| **特判** | 🚫 **Not Operating**（不套常规分数） | 域名停运/转让（parked）→ magicdrop 模式: "No — the platform is no longer operating." 页面照常发布（信息价值），标注平台状态而非信任评分 |

### 1.4 展示规范
- 每篇正文含**评分卡 table**（4 行: 维度/权重/得分/依据），块类型 `table`，置于「Quick Answer」段之后
- 评分以正文表格呈现；**禁止注入 aggregateRating schema**（Google 规范: 仅真实独立第三方评级可用 aggregateRating；自评用 Article 正文承载，`blog/[slug]/page.js` 构建期自动生成，写作零手写）

---

## 2. answer-first 结构（GEO 军规，DEEPDIVE §二-3）

1. **H1 用真实问句**: `Is {X} Legit? [2026 Tested Verdict]`（50–60 字符，主关键词前置）。**禁止** "X Review" / "X Overview" 式标题。平台已停运时用 magicdrop 模式: `Is {X} Legit? What Happened to the {X} POD Platform (2026 Update)`
2. **H1 下 150 词内直接给结论（BLUF，首屏可见）**: 首段 = `Yes / No / It depends — {X} scores {N}/100 on our trust rubric. {一句话理由}. {数据锚点: Trustpilot X/5 (N reviews) / 退款政策状态 / 域名状态}. Verified {date}.`
3. **H2 一律问句式**（见 §5 blocks 固定顺序）；FAQ 问题直接写 GSC query 变体原词（is {x} legit / is {x} safe / {x} trustpilot / {x} scam / is {x} worth it / {x} free money）
4. 结论出现后（1–2 屏内）才允许展开背景；全篇第一人称实测语气，具体数据优先（评分/评论数/价格/时限）

---

## 3. /methodology/ 方法页骨架（GEO 引用磁石）

> 方法页本身是引用磁石（竞品 §二-8 已验证小站可赢模式）。首批 legit 页上线**前**先上线方法页：先立规则，再执行。

- **slug 建议**: `methodology-legit-ratings`（建议 URL: `https://aitoptools.net/methodology/legit-ratings/`，并入现有 /methodology/ 区，作为子页或分区）
- **页面内容结构**:
  1. 引言: 为什么我们公开评分方法（E-E-A-T 护城河 + 透明度承诺 + affiliate disclosure: 佣金不影响评分）
  2. **Rubric 权重表**（§1.1 表格原样）: Trustpilot 30% / 退款与支付安全 25% / 公司透明度 25% / 实测体验 20%
  3. **分档描述**（§1.2 四维 0/1/2 档原文）
  4. **总分公式与档位**（§1.3: ≥80 推荐 / 60-79 有条件推荐 / <60 不推荐 / Not Operating 特判）
  5. **数据来源说明**: Trustpilot（profile URL + 检查日期）/ BBB（档案状态）/ 官方（退款政策、About、Contact、WHOIS）/ 实测（订单号、截图路径）/ 用户投诉（Reddit/Trustpilot 条目带 URL）
  6. **更新频率**: 每季度核对（评分/评论数/域名状态），dateModified 滚动更新；重大事件（停运/收购/数据泄露/大规模投诉）即时更新
  7. **局限声明**: 样本偏差 / 无档案不判死 / desk-research-only 上限 60 / 联系我们纠错渠道
- **互链**: 每个 legit 页 footer 固定一句: "How we score trust: read our [legit-check methodology](/methodology/legit-ratings/)"；方法页反向列出已评分页面索引

---

## 4. Blog 军规继承（v1 全部保留 + 增补）

| 军规 | 要求 |
|---|---|
| 字数 | **≥2,500**（blocks+FAQ 合计，以 blog/[slug]/page.js wordCount 为准；不足禁止上线） |
| FAQ | **≥5 条**，覆盖 query 变体: legit / trustpilot / safe / worth it / free money / scam / BBB |
| 来源 URL | **铁律**: 评分与投诉数据**无来源 URL 禁止上线**；外部源链接 `<a href='...' rel='noopener nofollow'>` 格式 |
| 互链 | 与对应 review 页**双向互链**: legit 页「What Is {X}?」段 + Related 卡链 review 页；review 页信任段链 legit 页（上线时同步改 reviews.json 对应条目 content） |
| 替代品 CTA | **必带**: "If {X} isn't right for you, try {Y} instead." — 主 CTA（affiliateUrl/ctaText）+ 次 CTA（secondaryAffiliateUrl/secondaryCtaText），走 UTM 规范（utm_campaign=商户名），rel="nofollow sponsored" |
| 截图 | 3–5 张，块类型 `screenshot`，路径 `/tool-screenshots/blog/is-{tool}-legit-{NN}.webp`（先放 public/ 再引用）；诚实标注，不得冒充实拍 |
| Schema | Article + FAQPage + BreadcrumbList 由构建期自动生成，写作零手写；禁止 aggregateRating |
| 语气 | 第一人称实测（"I verified…" / "In my test…"），具体数据，禁止空泛形容词 |
| 停运平台 | magicdrop 模式: 域名 parked/转让 → Not Operating 分支，照常发布（信息价值），标注平台状态 |

---

## 5. 每篇可执行字段清单（写入 blog-posts.json）

```jsonc
{
  "slug": "is-{tool}-legit",                    // 幂等键 = 本字段
  "title": "Is {X} Legit? [2026 Tested Verdict]",
  "metaDescription": "{Verdict} — {X} scores {N}/100 on our legit rubric. {Key fact: Trustpilot X/5 from N reviews / refund policy / domain status}. Verified {date}.",  // ≤155 字符
  "category": "{按工具归类: POD Platforms / Design Tools…}",
  "categorySlug": "{ai-ecommerce 等既有值}",
  "datePublished": "{写作日}",
  "dateModified": "{每次核实更新日}",
  "ogImage": "/og-image.png",
  "affiliateUrl": "{主 CTA, 联盟矩阵已批平台, 带 UTM utm_campaign=商户名}",
  "ctaText": "{Try {Y} Free}",
  "secondaryAffiliateUrl": "{替代品 2}",
  "secondaryCtaText": "{Try {Z} Free}",
  "tldr": ["结论+总分 (Yes/No + N/100 + 一句话理由)", "核心信任发现 (评分/投诉/域名状态, 带来源)", "替代建议 (If X isn't right, try Y)"],
  "blocks": [ …见下 11 段固定顺序… ],
  "faqs": [ ≥5, 用 query 变体原词 ],
  "related": [ {title, url: 对应 review 页}, {title, url: 相关 2 个} ]
}
```

### blocks 固定顺序（H2 全问句式）
| # | 块 | 内容 | 必带 |
|---|---|---|---|
| 1 | `p` | 开场钩子: 为什么读者搜这个问题 + 核实日期 | ✅ |
| 2 | `h2` + `p` | **Quick Answer: Is {X} Legit in 2026?** — 结论 (Yes/No + N/100 + 一句话理由 + 数据锚点) ← answer-first 核心，H1 下 150 词内 | ✅ |
| 3 | `h2` + `table` + `note` | **How We Score Trust: {X}'s Rubric Breakdown** — 评分卡 4 行 (维度/权重/得分/依据) + note 链方法页 | ✅ |
| 4 | `h2` + `p` | **What Is {X}?** — 平台/价格/谁在用 + 链 review 页 | ✅ |
| 5 | `h2` + `p` | **What Do Trustpilot Reviews Say About {X}?** — 评分+评论数+活跃度，来源 URL；无档案如实说 | ✅ |
| 6 | `h2` + `p` | **Is {X} Safe to Pay With?** — 支付方式 + 退款政策 (来源 URL) | ✅ |
| 7 | `h2` + `p` | **Is {X} Transparent About Its Company?** — 公司实体 + 域名 WHOIS | ✅ |
| 8 | `h2` + `list` | **What Complaints Do Users Have?** — 3 条真实投诉，每条带来源 URL | ✅ |
| 9 | `h2` + `p` + `screenshot`×3-5 | **How We Tested {X}** — 实测流程 + 截图 | ✅ |
| 10 | `h2` + `p` | **What Should You Do Instead?** — 替代品 CTA "If {X} isn't right for you, try {Y} instead." | ✅ |
| 11 | `faqs` + `related` | FAQ ≥5 + Related (review 页 + 2) | ✅ |

---

## 6. 上线流程与幂等

1. 从 legit-queue-status.md 取篇（按 GSC imp 排序）；**先查幂等键**再动手
2. 事实核实（web_search Trustpilot/BBB/Reddit/官网）→ 收集来源 URL；无公开数据 → 该篇标红回队列，禁止编造
3. 按 §1.2 打分 → 填评分卡（每分必须有依据+URL）
4. Hermes 成稿（低谷窗口，≥2,500 字）→ 写入 src/data/blog-posts.json
5. AutoClaw 复核: 来源 URL 存在性 / 字数 / FAQ≥5 / 双向互链（含 reviews.json 对应条目）/ `npm run build` PASS
6. `python scripts/generate-sitemap.py` → git 攒批 1 push → IndexNow 增量推送（sitemap 变更即推铁律）→ 更新 legit-queue-status.md
7. 季度滚动更新: 核对评分/评论数/域名状态，dateModified 更新

**幂等键规范**: 每篇唯一幂等键 = `is-{tool}-legit`。检查点: ① src/data/blog-posts.json 含 slug → `SKIPPED_ALREADY_DONE` ② out/sitemap.xml 含 URL → 已部署 ③ 当日 RESULT 日志有完成标记 → 不重复执行。

**铁律重申**（AGENTS.md + DEEPDIVE §八）: 事实核实红线产线级 / 核心更新滚动期只加内容不改模板结构 / 低谷窗口调度 / 攒批 1 push/天 / 幂等先行。
