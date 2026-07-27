# M3 首月 Runbook · 真实数据填充版（K3 填实，2026-07-28）

> 配套 `M3_MONTH1_RUNBOOK.md` 使用，替换其中所有 ______ 与"按文件排"占位。
> 数据来源：`AFFILIATE_PROGRAMS.md` + `credentials.affiliate.local.json` + src/data 实际页面。**未获批商户一律不用真实追踪链**。

## 一、W3-T1 高佣商户名次（已获批·有真链接，按 EPC 降序）

| 名次 | 商户 | 条款（真实值） | 追踪链 | 平台 |
|---|---|---|---|---|
| 1 | **Mockey** | **30% 循环** | `mockey.ai?via=jerome796` | Endorsely |
| 2 | **Creative Fabrica** | 25% 首购 + **20% 循环无上限**，Cookie 90 天 | `creativefabrica.com/ref/27832838/` | in-house |
| 3 | **Claid** | **20% 终身循环**，起付 $20 | `claid.ai?via=jerome94` | FirstPromoter |
| 4 | **Printful** | 履约 10%×12 月 + Growth 订阅 $25/单 | `printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a` | in-house |
| 5 | **Printify** | 销售额 5%×12 月，Cookie 90 天 | `try.printify.com/4fs863rfz2yc` | PartnerStack |

**待激活（获批后按此顺位插队）**：Deel $1500/单（B2B 场景页专用）＞ Placeit $50/年订阅（Impact 待批）＞ Kittl 20%×12 月（Impact 待批）＞ Gelato 最高 12%（PartnerStack 重申待批）。

## 二、头部 16 篇内容清单（W2-T1 pin 映射 + W3-T1 深链落点）

**6 对比页**：printful-vs-printify / printify-vs-gelato / printful-vs-gelato / kittl-vs-placeit / kittl-vs-canva / mockey-vs-placeit

**10 评测页**：mockey-review / creative-fabrica-review / claid-ai-review / printful-review / printify-review / placeit-review / kittl-review / gelato-review / mockuphive-review / photoroom-review

## 三、商户 × 头部内容映射（W3-T1 照单执行）

| 头部页 | 必挂高佣链（名次） | 备注 |
|---|---|---|
| mockey-review / mockey-vs-placeit | Mockey(1) 已有真链 ✅ | Placeit 侧占位链待 Impact |
| creative-fabrica-review | CF(2) 已有 ✅ | 补 1 个具体素材分类页深链 |
| claid-ai-review | Claid(3) 已有 ✅ | 深链指 pricing 页 |
| printful-review / 全部 POD 对比页 | Printful(4) 已有 ✅ | 对比页补 Printful 定价页深链 |
| printify-review / printful-vs-printify / printify-vs-gelato | Printify(5) 已有 ✅ | — |
| placeit-review / kittl-vs-placeit | Mockey(1) 补位 + Placeit 待批 | 获批后换真链 |
| kittl-review / kittl-vs-canva | CF(2) 补位 + Kittl 待批 | 获批后换真链 |
| gelato-review / 2 篇 gelato 对比 | Printful(4)+Printify(5) 补位 + Gelato 待批 | 获批后跑替换管线 |
| mockuphive-review | Mockey(1) 补位 | MockupHive 无联盟时挂 Mockey |
| photoroom-review | Claid(3) 补位 | Photoroom `?fpr=partner` 为失效链，Awin 重签后排期 |

**深链拼接红线**：一律用各平台后台 deeplink generator 或「产品页 URL + 已有追踪参数」，**禁止编造 URL 格式**；上线前人工点开验证 200 且落到目标页（runbook 附录 B 原规则）。

## 四、W2-T1 的 16 张 pin

直接用上方 16 页清单：每页 1 张 1000×1500 竖版 pin，标题=页标题，主体=胜方徽章+一句结论，底部 aitoptools.net，描述含目标关键词 + UTM `?utm_source=pinterest&utm_medium=pin&utm_campaign=m1`。首周 16 张，之后每周 +5。

## 五、W3-T2 三篇高意图新文 · 对账结论

1. `Best AI Product Photography Tools for POD (2026)` — **新建**（榜单结构复用 printful-alternatives 模板）
2. `Printful vs Printify 2026` — **已存在 → 只做优化**：补深链 + 主 CTA 提权 + 核对 winner 三一致，**禁止重写**
3. `Best Mockup Generator for Etsy Sellers (2026)` — **新建**，Mockey 为主推（30% 循环最高佣）

## 六、千问报告勘误（K3 实测，防止 M3 被带偏）

- ❌ "Printful vs Printify 未发布" → 实际已上线 200
- ❌ "页脚死链 /best-ai-tools/" → 实际 200 正常
- ❌ "全站 title 重复" → 抽查首页/about/compare 均唯一
- ⚠️ "CTA 无 href 37 页" → 首页 128 个 CTA 全部有 href；个别老评测页需抽查，**非 P0**
- ✅ 唯一坐实的 P0：**GA4/点击度量全站未装**（W1-T1 必须最先做）
- ⚠️ `?fpr=partner` 失效链确实存在（Placeit/Photoroom 系），按本文件第三节补位方案处理

## 七、三个护栏（用户拍板，M3 违反即停）

1. 首月 KPI = **管道三件套 + 破冰 $20–50**，不是 $500
2. 3D 桥接只 **1 篇 + 5 内链**，多 1 篇即违规
3. **W1-T1 度量是 P0**，不许跳过去先写内容

## 八、双引擎字段填充（W2-T4 / W3-T2 照单执行，2026-07-28 增补）

> 头部 16 页预置"主关键词 + 结论首句模板 + JSON-LD 类型 + FAQ 三问"，执行直接套，禁止现场自由发挥。结论首句的 {winner} 必须 = 该页 vs-card 的 winner 字段（附录 D 同源）。

### 8.1 六对比页（主关键词 / 结论首句模板 / schema / FAQ 三问）

| 页 | 主关键词 | 结论首句模板 | JSON-LD | FAQ 三问 |
|---|---|---|---|---|
| printful-vs-printify | printful vs printify | {winner} is the best POD fulfillment for {audience} in 2026 because {margin/UX 理由}. | ItemList+2×Product | which is cheaper for beginners / which integrates with Etsy / which has faster shipping |
| printify-vs-gelato | printify vs gelato | {winner} is the best POD fulfillment for {audience} in 2026 because {理由}. | ItemList+2×Product | global coverage vs price / print quality difference / best for EU sellers |
| printful-vs-gelato | printful vs gelato | {winner} …（同上模板） | ItemList+2×Product | branding options / per-item cost / eco-friendly options |
| kittl-vs-placeit | kittl vs placeit | {winner} is the best design tool for {audience} in 2026 because {理由}. | ItemList+2×SoftwareApplication | template library size / learning curve / best for merch sellers |
| kittl-vs-canva | kittl vs canva | {winner} …（同上模板） | ItemList+2×SoftwareApplication | free plan limits / merch/POD workflow / team features |
| mockey-vs-placeit | mockey vs placeit | {winner} is the best mockup generator for {audience} in 2026 because {理由}. | ItemList+2×SoftwareApplication | 3D vs 2D mockups / bulk generation / free tier |

### 8.2 十评测页（主关键词 / 结论首句模板 / schema / FAQ 三问）

| 页 | 主关键词 | 结论首句模板 | JSON-LD | FAQ 三问 |
|---|---|---|---|---|
| mockey-review | mockey review / mockey ai | Mockey is the best mockup tool for {audience} in 2026 because {理由}. | SoftwareApplication+Review | is mockey free / mockey vs placeit / does it do 3D mockups |
| creative-fabrica-review | creative fabrica review | Creative Fabrica is the best asset marketplace for {audience} in 2026 because {理由}. | SoftwareApplication+Review | commercial license included / subscription vs credits / best for POD sellers |
| claid-ai-review | claid ai review | Claid.ai is the best AI product photo tool for {audience} in 2026 because {理由}. | SoftwareApplication+Review | claid vs photoroom / api access / free tier limits |
| printful-review | printful review | Printful is the best POD fulfillment for {audience} in 2026 because {理由}. | SoftwareApplication+Review | printful pricing / printful vs printify / integrations list |
| printify-review | printify review | Printify is the best POD fulfillment for {audience} in 2026 because {理由}. | SoftwareApplication+Review | printify premium worth it / print providers rating / global shipping |
| placeit-review | placeit review | Placeit is the best mockup/logo tool for {audience} in 2026 because {理由}. | SoftwareApplication+Review | placeit free mockups / placeit vs mockey / video mockups |
| kittl-review | kittl review | Kittl is the best design tool for {audience} in 2026 because {理由}. | SoftwareApplication+Review | kittl free plan / kittl for t-shirts / kittl vs canva |
| gelato-review | gelato review | Gelato is the best local POD for {audience} in 2026 because {理由}. | SoftwareApplication+Review | gelato countries / gelato vs printful / paper products |
| mockuphive-review | mockup hive review | MockupHive is the best mockup resource for {audience} in 2026 because {理由}. | SoftwareApplication+Review | free vs paid / file formats / best for Etsy listings |
| photoroom-review | photoroom review | Photoroom is the best product photo tool for {audience} in 2026 because {理由}. | SoftwareApplication+Review | photoroom free / batch editing / photoroom vs claid |

### 8.3 meta 模板（SEO 4 线，≤60/≤155 字符）

- title：{主关键词} (2026): {Winner} Wins for {Audience} | aitoptools
- description：We tested {N} {category}. {Winner} wins on {1 个可量化理由}. See the comparison table, pricing, and best deal inside.

### 8.4 内链网（每页 ≥3 条，预置映射）

- 每个对比页 → 链到两个品牌评测页 + 1 个同品类对比页
- 每个评测页 → 链到该品牌出现的对比页 + 2 个同品类评测页
- 锚文本 = 对方页主关键词自然变体，禁止全站统一锚文本

⚠️ 双引擎澄清（防 M3 被带偏）：本方案 GEO = **Generative Engine Optimization**（被 AI 答案引用），不是多语言/多地区（Geographic，本方案不做）。首月不为 GEO 新建 hub 页/不写新文，只改 16 页结构（W2-T4）+ 3 篇新文自带结构（W3-T2）。
