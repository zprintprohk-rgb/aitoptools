# 落地冲突审查报告 — aitoptools GEO+SEO 战略升级与 Agent 集群执行规划

> 审查对象: `F:\aitoptools\20260811-042320-e6a260d3\aitoptools-GEO与SEO战略升级与Agent集群执行规划.md`（2026-08-11）
> 审查员: 落地冲突审查员（subagent）· 审查日期: 2026-08-11 04:40 (GMT+8)
> 审查基准: F:\aitoptools 代码库 + handoff/BOARD.md + CONTENT_PLAN.md + STRATEGY-2026-08-10.md + .hermes/logs/boost-tracking.md + EXECUTION_PLAN.md
> 结论速览: **现状 6 项中 3 项属实 / 1 项部分属实 / 2 项不属实（含 1 项重大数据失真）；冲突 8 条；遗漏 10 条。规划可执行，但前提数据（143 页 / 94 工具 / Organization 缺口）必须修正，且 W1/W2 与既有 Boost/Halloween/M3 排期严重挤占，需重新排期或明确优先级。**

---

## 一、现状核对逐项结论

### a. "Article/FAQPage/SoftwareApplication Review/BreadcrumbList 四类 schema 构建期自动生成" — ✅ 属实（四类存在）；⚠️ 但"缺口在 Organization"不属实

证据路径:
- `src/app/[slug]/page.js` — `generateReviewJsonLd()` 输出 `@type: Review` + `itemReviewed: SoftwareApplication` + `reviewRating`（评分卡 0-10 换算为 Rating）；`generateBreadcrumbJsonLd()` 输出 BreadcrumbList；`generateFaqJsonLd()` 输出 FAQPage（有 faqs 时）
- `src/app/blog/[slug]/page.js` — `buildSchemas()` 输出 Article（headline/datePublished/dateModified/author=Person/wordCount）+ FAQPage + BreadcrumbList
- `src/app/best/[slug]/page.js` — Article + ItemList + BreadcrumbList + FAQPage；`src/app/compare/[slug]/page.js` — Article + BreadcrumbList + FAQPage
- 均已构建期生成，无需手写。**四类 schema 的现状陈述属实。**

**不属实部分**: 规划称"缺口在 Organization 与 Person 两个实体类"。
- **Organization 已在全站存在**: `src/app/layout.js` body 首元素即全局 `application/ld+json` 块（`@type: Organization`, name/url/logo/description），每个页面都注入。规划 §3.2 把 Organization 列为缺口 = 与代码库现状直接冲突，执行层若照单施工会重复造轮子。
- **Person 部分属实**: Person 实体仅存在于 blog Article schema 的 `author` 字段（`blog/[slug]/page.js` 的 `AUTHOR = { '@type': 'Person', name: 'Jerome Tang', jobTitle: 'Print Industry Expert' }`）；工具页 Review schema 的 author 反而是 `Organization 'Print AI Tools'`（`[slug]/page.js`）。无独立 Person schema 块、无作者落地页。规划的 Person 补强方向成立，但"AI 引擎无法把身份信号与站点绑定"属过度声明——blog 文章已把 Person↔站点绑定。

### b. "作者实体页缺失（byline 只有文字，无 Person schema 落地页）" — ⚠️ 基本属实，但 about 页已有作者资历全文，规划未识别存量

证据路径:
- byline 文字: `src/app/[slug]/page.js`（"By Jerome Tang — Print industry expert · hands-on tested on real print jobs"）、`compare/[slug]/page.js` 同款、blog 页 "Reviewed by Jerome Tang, Print Industry Expert"
- **`src/app/about/page.js` "Who Runs This Site" 节已含完整作者资历**: Founder & Editor Jerome Tang / trade name ZPrintPro / Sales & Marketing Manager at Shenzhen Cai Long Printing / 10+ 年印刷行业经验 / LinkedIn 链接 / 邮箱。**无 Person JSON-LD、无独立 /author/ 页**。
- 结论: "无 Person schema 落地页"属实；"作者信息全站缺失"不属实。真正增量 = Person schema 注入 + 作者页（或 about 加 Person schema + byline 链接），且必须与 about 页去重互链，否则制造重复内容。

### c. "最后更新时间展示不足（dateModified 存在但不可见）" — ✅ 属实（工具页更严重：完全无日期）

证据路径:
- 工具页 `src/app/[slug]/page.js` meta-bar 无任何日期；Review schema 无 dateModified（仅 datePublished，默认 '2026-06-25'）
- blog 页 `blog/[slug]/page.js` meta-bar 只显示 `{datePublished} · 阅读时长 · 字数`；dateModified 仅在 Article schema 内（不可见）
- listicle（`best/[slug]/page.js`）/ compare（`compare/[slug]/page.js`）meta-bar 无日期（schema 有 dateModified）
- 全站可见"更新时间"仅 layout.js trust-bar 的 "Updated {Month Year}"（月度粒度，链接 /methodology/#updates）+ methodology 页 update log。**属实，且比规划描述的缺口更大（工具页连 datePublished 都不可见）。**

### d. "143 页为页面集合，无集群结构" — ❌ 页码不属实（重大数据失真）；集群判断部分属实

证据路径（代码库实测）:
- `src/data/reviews.json` = **107** 条（非 94）；`blog-posts.json` = 9；`listicles.json` = 4；`comparisons.json` = 6；category = 6；静态页 ≈ 13
- `scripts/generate-pages.js`（keywords-200.csv 驱动）生成 **~199 个 programmatic 页** → `public/best/{slug}/index.html`（Next 原样导出，`out/best/printify-vs-printful/index.html` 实测存在）
- `public/sitemap.xml` = **341 URL**（8/9 时 339，与 STRATEGY 一致）；`out/` 构建产物 = 347 个 index.html
- **"143 页 / 94 工具"与代码库不符**，疑似取自旧构建/旧 AGENTS.md（"当前 113 页"同样过期）。规划 §4.3"143 页重组为集群"的前提数据错误，实际波及面 ≈ 344+ 页。
- blog-links.mjs（`src/lib/blog-links.mjs`）**只被 `blog/[slug]/page.js` 引用**（全库 grep 确认）——单向 blog→工具页自动内链；工具页/榜单/对比页无工具名自动内链。工具页内链 = "Compare Similar Tools" 同分类静态 2 卡；listicle→评测页（reviewSlug）、compare→评测页（"Read the Full Reviews"）为数据驱动单跳。
- 存在分类级 hub 骨架（`category/*` 6 页 + `/best-ai-tools/` + `/best/` + `/compare/` + `/blog/`，均有 CollectionPage/ItemList schema），**但无主题集群联动**（listicle ↔ 对比页 ↔ blog 之间无枢纽逻辑）。"无集群结构"部分属实，"无任何结构"不属实。

### e. "llms.txt 已部署" — ✅ 属实

证据路径: `public/llms.txt` 存在（90 行，含 Core pages/Categories/Best Of/Blog 分区）。规划"保留不动、降级为维护项"与项目现状一致（STRATEGY T10 8/10 已补新 blog URL）。

### f. "GEO 盲区（CF beacon 未装）" — ✅ 属实

证据路径: `src/app/layout.js` head 仅 GA4 gtag（G-248QMCT2S3）+ affiliate_click 委托脚本，**无 Cloudflare Web Analytics beacon 脚本**。与 BOARD D3、STRATEGY GEO_BLIND 一致。

---

## 二、冲突清单（8 条）

| # | 冲突 | 说明 | 严重度 |
|---|---|---|---|
| C1 | **Organization 缺口声明与代码现状冲突** | 规划 §3.2 把 Organization 列为缺口，`layout.js` 已全站注入 Organization JSON-LD。执行层照规划施工 = 重复建设 | 高 |
| C2 | **页码/工具数数据失真** | 规划"143 页 / 94 工具评测" vs 实测 107 reviews / 341 sitemap URL / 347 built 页 / ~199 programmatic /best/ 页。§4.3 集群改造的工程量估算整体失真 | 高 |
| C3 | **集群枢纽页与现有 programmatic best/ 体系重叠** | 规划"复用 listicles 结构搭两个集群枢纽页（不新增页面类型）"，但 /best/ 命名空间已被 ~199 个 programmatic 页占用（printify-vs-printful、kittl-vs-canva、claid-vs-photoroom、best-pod-for-etsy-sellers 等已在 sitemap/out 中，命名即集群辐条形状）。规划通篇未提及这 199 页的存在、质量与去留——枢纽 URL 选位、内链方向梳理都会撞车；且 sitemap 341 URL 中 ~199 为模板生成页，GEO 引用稀释风险未评估 | 高 |
| C4 | **作者实体页与 about 页重复** | about/page.js 已有作者资历全文（含 LinkedIn/邮箱/公司/年限）。独立作者页需与 about 去重互链，否则同义重复内容 | 中 |
| C5 | **W1 (8/11-17) 与既有排期挤占** | BOARD 日程 + STRATEGY T3/T4/T6/T7: 8/11 Boost #3、8/12 Printful W-8 复核 + Hermes 切换检查、8/13 Boost #4、8/14 T+7 首读数 + Placeit 催办、8/12-8/16 M3 写作。规划 W1 五个任务（beacon/GSC OAuth/双联盟申请/两枢纽页/Kittl+Placeit）与之并行，未核算人力与 1 push/天 quota 约束（W1 内联链+枢纽页+E-E-A-T+Boost 并发 ≈ 10+ 天 push 容量） | 高 |
| C6 | **T+30 日期自相矛盾** | §6.2 写 "T+30 全量校准（9 月 10 日）"，W3 路线图（8/25-31）写 "T+30 全量校准"。相差近两周，执行层无法同时满足 | 高 |
| C7 | **Jasper/Synthesia 申请前置条件未标** | W1"提交申请"依赖 T1b（WebSearch 凭证 BROKER_UNAUTHORIZED 恢复后补全 4 家调研，尚未恢复）；且 AGENTS.md 铁律"联盟申请表单提交 = 行动卡片交 user 人工"。规划未标注依赖与人工闸口 | 中 |
| C8 | **Hermes 角色与停用决策冲突** | 规划 §7.2 夜间批量含"Hermes 写手扩写"；项目 8/12 有 Hermes 切换检查（建议停用 Hermes 侧 daily-content cron）。若 Hermes 停用，写手角色归属（AutoClaw/千问/其他）未定义 | 中 |

---

## 三、遗漏清单（10 条）

1. **Boost 战线整体缺位**: 8/11 Boost #3 / 8/13 Boost #4 / 8/14 T+7 首读数 / 8/15 Boost #1/#2 T+7 对比全部未进 30 天路线图。T+7 (8/14) 是规划 T+30 校准链的数据前置，漏掉 = 规划自己的校准逻辑断链
2. **8/12 Printful W-8BEN-E 复核窗（T5）**未提及——payout-ready 解锁（离钱最近项）与 W1 联盟申请任务并行却互不知晓
3. **Printify $150 博客挑战赛（9/29 截止）无内容排期**: 规划 §6.2 将其列为高额佣金补充项，但 30 天路线图（至 9/7）未安排任何投稿内容任务，截止前只剩 ~3 周窗口
4. **seasonal-exec cron（8/10+8/18 19:37）+ halloween-asset-chain 素材链**未计入规划负载: 素材池已 25/去重 24，8/18 判定只是"判定"，素材→设计→下单→拍照→内容全链路工时（D1 测试地址仍阻塞）未与 W2 集群任务合并排期
5. **每周复盘 cron（周日 07:47）+ 每日 3 cron 的持续负载**未纳入 Agent 集群方案（§7.2 只讲了新自动化，没讲既有 4 cron 的并存与算力叠加，也未提 4 cron 已全配 deepseek fallback 的状态）
6. **GSC 基线未衔接**: 北极星现状 = 28 天 2044 展示 / 3 点击 / CTR 0.15%（STRATEGY-08-10），规划 M1 占位"月访问 300"与 8/8 基线（日均 ~200 展示）的换算关系未说明
7. **llms.txt 治理与 sitemap 合并保底模式的联动遗漏**: generate-sitemap.py 合并保底会把 programmatic 199 URL 持续并入 sitemap；若规划做集群改造不动这层，sitemap 会继续携带模板页，GEO/索引健康度评估缺失
8. **IndexNow 即推铁律 + 攒批 1 push/天 未给 push 日历**: W1/W2 的高频内容/内链改动与"1 push/天"配额没有排期核算（规划只说"攒批"，未列哪几天 push、哪些改动合并）
9. **枢纽页文案的事实核查预算缺失**: 集群改造被描述为"增量工作集中在内链方向梳理与枢纽页文案"，但事实核查军规（WebSearch 引用源未过禁止上线）同样适用于枢纽页文案，未给核查工时
10. **Kittl 审核复查与 Impact 升级（D4）的状态未入路线图依赖**: W1"Kittl 审核复查 + Placeit 申请"依赖 D4 人工登录 Impact（仍缺），规划未将其标为阻塞前置

---

## 四、执行建议（审查员注）

1. 修正现状基准确认项: Organization 已存在（C1）、页数按 341 sitemap URL / 107 reviews 重算（C2）、盘点 programmatic 199 页后再定集群枢纽方案（C3）
2. 拍板 T+30 日期（C6）: 建议以 8/14 T+7 读数 +30 天 = 9/13 为准，或明确 T+30 = 9/10 且 W3 只做"预校准"
3. 30 天路线图重排: 把 Boost #3/#4、T+7 (8/14)、W-8 复核 (8/12)、M3 写作 (8/12-16)、Halloween 素材链、seasonal-exec cron 并入 W1/W2 时间轴，按 1 push/天 出 push 日历
4. 作者实体方案: 优先"about 页加 Person JSON-LD + byline 链接 + blog Person 已有"三步，独立作者页放二期（C4）
5. Printify 挑战赛（9/29）进 W4 内容计划，与 Shopify $150 申请并列

*本报告仅审查，未修改任何项目文件。*