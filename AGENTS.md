# aitoptools.net — AI 协作指南

> **项目**: F:\aitoptools（Next.js 14 静态导出，AI 工具评测站）
> **定位**: AI Tools for Print Shops & Independent Store Owners —— 印刷店/POD 卖家的垂直 AI 工具决策平台
> **域名**: aitoptools.net（品牌不换名，2026-07-17 user 拍板）
> **启动必读**: 每次进场先读 `k3-ops-constitution-v2.md`（多项目运营宪法），再读本文件

## 0. 运营约束（源自宪法 v2，最高优先级）

- **资源配比**: C 项目 15%，Hermes 批量评测草稿为主，**M3 只做深度对比/榜单**
- **北极星指标**: CPA/CPS 佣金/月（6 个月目标 $3000，见 EXECUTION_PLAN.md）
- **攒批 push**: Cloudflare Pages build quota 稀缺，**1 push/天**，改动攒批；仅紧急修复（404/死链/白屏）可单独 push
- **免检原则**: 执行层报 Success + 构建页数自检正确 = 免检；只有 Error/Timeout/user 报错才截图诊断
- **push ≠ deploy**: 以 GitHub check-runs 的 CF Pages 状态为准，不以 git log 为准
- **任务卡铁律**: 任何任务必须带「当前动作支撑赚钱目标: [具体指标]」，缺了自动驳回

## 1. 核心定位（一句话）

> 不做通用 AI 导航站（红海，有巨头和 aitoptools.com 在前），做**印刷/POD 行业的 AI 工具雷达 + 深度决策内容**——别人收 3 万个工具，我们只收 300 个，每个都有评测和购买建议。

- **目标读者**: POD 卖家、印刷店主、包装设计/电商物料从业者（英文站）
- **内容哲学**: Wirecutter 的决策结构（骨架）+ G2 的数据组件（肌肉）+ Raycast 的克制视觉（外衣）
- **发布纪律**: 雷达发现 → 模板草稿 → **事实核实（WebSearch 引用源）→ 才允许上线**。宁可每周 3 篇精品，不要每天 10 篇垃圾（Google Helpful Content 红线）

## 2. 设计 Token（默认锁定，2026-07-18 拍板；2026-07-22 修订变更规则）

| Token | 值 | 用途 |
|---|---|---|
| 纸白 | `#FAF7F2` | 页面背景 |
| 墨黑 | `#17201c` | 标题/正文 |
| 品牌绿 | `#0b5f59` | 页头、链接、强调 |
| 琥珀橙 | 唯一强调色 | CTA、Our Pick、下划线、Better Value |

**变更规则（2026-07-22 user 拍板）**：Token 默认锁定，但不为锁而锁。若确实有很好的 UI/UX 设计方案，允许改——准入门槛：① 明显更大气、更美观、更专业（有对标参照或设计依据，不是换个颜色而已）；② 全站一致替换，不做局部变色；③ 改前给 user 看方案，user 拍板后才动工。

- ❌ 默认禁止第三色（黄色已清除）、禁止 muddy 渐变、禁止照片 hero（评测站产品是内容本身）——除非走上面的变更规则且方案确实更好
- 卡片：1px `rgba(23,32,28,0.10)` 细边框，**零阴影**；hover 只留颜色/边框过渡，禁止 scale/translate 动效
- 区块间距桌面 115px，卡片内边距 28-32px，正文行高 1.7

## 3. 内容标准模板（所有新对比页/榜单页必须遵守）

数据结构在 `src/data/comparisons.json` / `listicles.json`，渲染组件已固化：

- **picks 三级推荐卡**: 恰好 3 项（top / also / budget），PicksCards.js
- **features 功能矩阵**: 7-8 行，取值 true/false/"partial"，FeatureMatrix.js（✓/✗/◐）
- **pricing 定价表**: 含 betterValue 标记，PricingTable.js（Better Value 琥珀标签）
- **WhyTrustUs**: 页底 FAQ 前固定模块
- 评分一律走 RatingBar.js；Pros/Cons 走 ProsCons.js 双栏
- 校验: `python scripts/validate_content_data.py` 全过才允许构建（M3 任务，2026-07-21 已派）

### 3.1 Blog 内容军规（2026-08-04 K3 拍板 — Blog 是流量主力，非工具页附属）

**为什么**: 工具页是商业意图（转化主力），Blog 打信息意图长尾（流量主力）。无 Blog 灌溉，工具页是死水。

| 标准 | 要求 |
|---|---|
| 字数 | 单篇 **2,500–3,500 字**（英文正文，含表格/FAQ；不足 2500 禁止上线） |
| 选题 | 信息意图长尾词（how-to / vs / best-for-beginners），禁与工具页抢商业词 |
| 结构 | TL;DR 摘要框 → 目录 TOC → 第一人称实测正文 → 对比表格 → Pros/Cons → FAQ(4-5条) → Related |
| 语气 | 第一人称实测（"I tested…" / "In my 6-week test…"），具体数据（速度/分辨率/成本），禁止空泛形容词 |
| 截图 | 每篇 3-5 张独家截图，block type `screenshot`，路径 `/tool-screenshots/blog/{slug}-NN.webp`（先放 public/ 再引用） |
| 背书 | 文末 byline 自动渲染 "Reviewed by Jerome Tang, Print Industry Expert"（模板内置，勿手写） |
| Schema | Article + FAQPage + BreadcrumbList 由 `src/app/blog/[slug]/page.js` 构建期自动生成，**写作时零手写** |
| 内链 | **直接写工具名即可** — `src/lib/blog-links.mjs` 构建时自动扫描 `src/data/tools/*.json` + `reviews.json`，首次出现自动链到详情页 `/review-slug/`（每工具每篇一次）。pending 工具（无 review 页）自动不链 |
| 结构数据 | SSoT = `src/data/blog-posts.json`（数组）；模板 = `scripts/templates/blog-post.example.json`（复制填值） |

**写入流程**（8/5 攒批第 2、3 篇文章走此流程）:
1. 从 `.hermes/drafts/articles/*.md` 按军规扩写到 2500+ 字（含截图占位）
2. 按 `blog-post.example.json` 结构写入 `src/data/blog-posts.json`
3. 截图转 WebP 放 `public/tool-screenshots/blog/`
4. `python scripts/generate-sitemap.py`（合并保底模式，勿手改 sitemap）
5. `npm run build` → git 攒批 1 push

> ⚠️ **build 硬约束**: `blog-posts.json` 为空数组 `[]` 时 `npm run build` 会失败（Next `output:'export'` 动态路由必须 ≥1 个静态参数，报错信息误导为 "missing generateStaticParams"）。**8/5 push 前必须先写入文章**。已用 example 验证: 有 ≥1 篇时 build 全绿（143 页）。

**技术埋点**（指令二）: 工具页 SoftwareApplication + rating 已由 `src/app/[slug]/page.js` 的 Review schema 承载（reviewRating 比 aggregateRating 更合规，勿改成 aggregateRating）；`scripts/schema-generator.py` 有 `generate_article_schema()` 可独立调用。

## 4. 自动化管线（已建）

| 任务 | 触发 | 作用 |
|---|---|---|
| 每日 AI 工具发现 | cron `23 8 * * *` Asia/Shanghai | 扫 ProductHunt/聚合站 → 垂直过滤 → 写 `discovery/YYYY-MM-DD.md` |
| 联盟审批监控 | cron `12 9 * * *` Asia/Shanghai | 查 Gmail 审批结果邮件 + 通知 |

- 发现 → 评测队列（CONTENT_PLAN.md 63 页分三批，第一批 7 篇已完成）
- CTA 占位 `?fpr=partner`，联盟链接批下后走 `scripts/replace_affiliate_links.py --apply` 统一替换 → `scripts/affiliate_link_audit.py` 验证

## 5. 联盟账户矩阵（凭证在 credentials.affiliate.local.json，已 gitignore，勿提交）

| 平台 | 状态 | 说明 |
|---|---|---|
| Creative Fabrica | ✅ 已获批 | ref/27832838 |
| Claid (FirstPromoter) | ✅ 已获批 7/24 | `https://claid.ai?via=jerome94`；⚠️ 收款方式待用户设置 |
| Printify (PartnerStack) | ✅ 已获批 7/24 | `https://try.printify.com/4fs863rfz2yc`；有 $150 博客挑战（9/29 截止） |
| Printful (in-house) | ✅ 已获批 7/24 | `https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a`；确认邮件待点 |
| Mockey (Endorsely) | ✅ 已激活 7/22 | `https://mockey.ai?via=jerome796`，30% 循环 |
| Kittl (Impact) | 🟡 审核中 | 7/15 提交，Impact 账号 Jerome88 / zprintpro@outlook.com；依赖 Impact Marketplace 升级获批 |
| Placeit | ⏸ 待申请 | 等 Impact Marketplace 升级获批后申请 |
| Looka | ❌ 计划已关闭 | 7/24 二次确认 PartnerStack 侧 program page not found；仅 partnerships@looka.com 邮件直签一路，低优先 |
| Photoroom | ⚠️ 待重签 | 现有 ?fpr=partner 疑似失效，需走 Awin 重新签约替换 |

- 日志: `AFFILIATE_LOG.md`；审计: `AFFILIATE_AUDIT.md`
- 敏感操作（登录/验证码/资金）→ 交 user 行动卡片，绝不自动

## 6. 技术架构

- Next.js 14 `output:'export'` → `out/`，push main 触发 CF Pages 部署（CDN 传播 1-2 分钟）
- 仓库: github.com/zprintprohk-rgb/aitoptools
- 数据驱动: `src/data/tools.json`（实为 reviews.json 收录 94 工具）/ comparisons.json / listicles.json
- SEO: llms.txt + robots 放行 AI 爬虫 + 74 页 FAQ JSON-LD（scripts/generate_faqs.js）
- 构建验证: `npm run build` 全量通过，页数只增不减（当前 113 页）

## 7. 7 大"绝对不要做"清单

1. ❌ 不要改品牌名/换域名（已拍板，不再投入）
2. ❌ 不要做通用 AI 导航站定位（垂直护城河不可稀释）
3. ❌ 不要未经事实核实直接发布 AI 生成的评测内容
4. ❌ 不要擅自加照片 hero / 第三色 / 阴影 / 缩放 hover（默认锁定；确有更优设计按 §2 变更规则走，user 拍板后执行）
5. ❌ 不要一天多次 push（攒批，quota 稀缺）
6. ❌ 不要提交 credentials.affiliate.local.json 或任何凭证
7. ❌ 不要自动执行登录/验证码/资金操作（交 user）

## 8. 关键文件别删

- `k3-ops-constitution-v2.md`（宪法，启动必读）
- `EXECUTION_PLAN.md` / `CONTENT_PLAN.md` / `TRAFFIC_STRATEGY.md`
- `AFFILIATE_LOG.md` / `AFFILIATE_PROGRAMS.md`
- `scripts/replace_affiliate_links.py` / `affiliate_link_audit.py` / `generate_faqs.js`
- `discovery/`（雷达产出目录）
- `AGENTS.md`（本文件）

## 算力低谷执行窗口（2026-07-24 用户拍板，不可违反）

- **Hermes Agent（DeepSeek V4 Flash）与 GLM 智谱模型**：一切批量/耗时任务只准在算力低谷运行：
  - 夜间窗口：**18:00 — 次日 08:00**
  - 午间窗口：**12:05 — 13:30**
- K3（本 Agent）安排定时任务、给 Hermes 派活时，触发时间必须落在上述窗口内（避开整点/半点，用 7-23 或 37-53 分）。
- 白天 08:00-12:05 / 13:30-18:00 只安排：K3 自己的轻量核查、用户手动操作、紧急修复。

## 度量新规（2026-07-28 K3 拍板）
- GA4 点击事件名统一 `affiliate_click`（非 outbound_click），关键事件标记用此名。
- utm_campaign 用商户名（如 mockey），不用统一 m1。
- link_id 命名 {slug}-{位置}，禁止 global-injected-{hash} 式不可读 ID（存量 27 条 W1-T2 修复）。
