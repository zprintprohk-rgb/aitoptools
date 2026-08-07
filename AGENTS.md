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

## 终端脱敏判定规则（2026-08-05 K3 拍板 — Printful"坏链"误报教训）
- **Hermes 终端会对 32 位 hex / affiliate hash 自动打码为 `***`**（如 printful.com/a/15297661:***）。grep/sed/cat 输出中的 `***` 不代表文件里真有星号。
- **判定文件内容必须用字节级方法，不信终端显示**：
  - `od -c file | head` 看原始字节
  - Python `repr(open(f).read()[i-30:i+60])` 或 `[ord(c) for c in seg]` 看字符码
  - `git diff` 对比真实改动
- **上报"坏链/死链/泄漏"前必须先做上述字节级验证**；疑似坏链 0 成本先查，勿直接报 P0 让全队烧工时（8/5 Printful 排查消耗 20+ 分钟，实际 0 坏链，副产品是发现 3 篇 Blog 缺 CTA）。
- 例外：字面 `***` 出现在文件里（非脱敏场景）才真有问题。

## 模型余额监控规则（2026-08-05 K3 拍板 — 8/5 晚 402 事故）
- **事实**: 8/5 20:30 daily-report 因 `HTTP 402: Insufficient Balance` 失败（DeepSeek 余额不足）。备用 MINIMAX key 存在（.env MINIMAX_CN_API_KEY）但 config 未接 fallback。
- **规则**:
  1. 所有 cron 首任务 = ping 模型（检查 gateway.log 是否有 402/insufficient balance），有则**置顶告警**并尝试继续，再遇 402 记录中断点
  2. 任何 cron 失败先查 executions.db / output 目录的 Error 段，402 与 Timeout 区分上报（402=钱的问题，Timeout=高峰/网络）
  3. 402 持续 2 天 → 升级 user 二选一：充值 DeepSeek 或 config 接 MINIMAX fallback
- **触发线**: 任意 cron 报 402 即告警，不等待

## 对比度双变量铁律（2026-08-06 K3 拍板 — hero 深底灰字二修教训）
- **深底（#0f5d4e / #0b5f59 / --c-deep 级）上的正文**: 必须"近白"——≥ #DCEDE7（当前用 #EAF4F0, 对比 ≈11:1）。**禁止**用白底灰变量（--k-tertiary / --k-secondary / #4a5568 之类），深底上用它们对比度只有 2-3:1。
- **白底正文**: ≤ #4a5568（--k-tertiary 已从 #727d77 提暗, 对比 7:1）。**禁止**在浅色容器里用近白/浅薄荷色。
- **两套变量, 禁止混用**: 深底只吃"近白系", 白底只吃"深灰系"。判定容器底色后再选变量, 不要沿用上一处代码的变量。
- **全站排查方法**: grep `background: var(--c-deep)` / `--k-deep` / `#0b5f59` / `#17201c` 找到深底容器, 检查容器内所有 `color:` 是否 ≥ #DCEDE7; 浅底容器检查是否 ≤ #4a5568。
- 已排查点位 (8/6): evidence-card 正文 (#EAF4F0) / evidence-stat-label (0.75 白) / footer-copy+footer-disclosure (--k-muted) / mobile-nav-panel (0.88 白) / hero trust-line (--k-secondary, hero 实为浅底)。
- 新组件上线前: 深底组件默认 `color: #EAF4F0 系`, 白底默认 `--k-tertiary`, 除非有明确理由。

## CSS 部署核对铁律（2026-08-06 K3 拍板 — 线上 hashed 文件名核对）
- **CSS/JS 改动 push 后, 必须核对线上 hashed 文件名**（Next.js 产物 CSS 文件名带 hash, 如 `/_next/static/css/41d6f17fd1783abd.css`）:
  1. `LOCAL=$(ls out/_next/static/css/*.css | xargs -n1 basename | head -1)`
  2. `ONLINE=$(curl -s https://aitoptools.net/ | grep -oP '/_next/static/css/[^"]+\.css' | head -1)`
  3. 相同 = 新构建已上线; 不同 = 部署未生效/传播中/构建失败
- **改了 CSS 变量但线上 CSS 文件 hash 没变 = 改动没上线**, 不要对用户说"已生效"
- 传播窗口 1-10 分钟 (CF 边缘节点); 用户截图往往落在传播前的旧版本 — 判定"是否上线"以线上 hashed 文件内容为准, 不是用户截图
- 实例 (8/6): hero 深底正文 #E6F2EE→#EAF4F0 二修, 用户说"还是糊"实为截图落在 8bf54a6 部署传播窗口; 核对线上 CSS 已含 #EAF4F0 即确认生效

## 关键激活邮件全量搜索铁律（2026-08-06 K3 拍板 — Printful 17 天误判教训）
- **关键激活类邮件（verify/activation/confirm/tax/W-8/payment/approved）必须全量搜索 ≥90 天**（SINCE 至少 90 天前, 推荐 6 个月）, 禁止用 7/14/30 天窗口
- **"未搜到" ≠ "不存在"** — 脚本窗口太窄会冤枉发件人 (Printful 确认邮件在 7/20, fetch 脚本 SINCE=30-Jul 查不到, 误判"email-unconfirmed" 17 天)
- **脚本结论与 user 记忆冲突时, 以 user 记忆为优先假设复核** — user 说"发过确认邮件"就按存在去找, 扩大窗口直到找到或穷尽
- 搜索方法: IMAP 按发件人 domain + 主题关键词双过滤; 确认类邮件看正文提取链接; 链接过期(404) → 引导后台重发
- 已纠正案例: Printful 7/20 "Confirm email address" (support@info.printful.com) 8/6 定位, 链接待 user 点击


## sitemap 变更即推铁律 (2026-08-08 K3 拍板 — 8/8 6 篇 Blog 缺失 sitemap 交讯)
- **每次新增 Blog/页面 (发布确认后), 当天内必须完成**: ① 重跑 `python scripts/generate-sitemap.py` (合并保底模式, 勿手改 sitemap) ② 验证新 URL 在 public/ 与 out/ 的 sitemap.xml 均存在 ③ git push ④ IndexNow 增量推送新 URL (参考 scripts/submit_indexnow_blog_20260808.py 模式) ⑤ 填写 AFFILIATE_LOG.md C2b 计数表
- **不等攒批**: sitemap/推送缺失会直接延迟 GSC 收录 (T+7 读数失真), 属“紧急修复”级别, 可单独 push
- 验收: 每次发布后 grep sitemap 含新 slug = 0 缺失

## 季节内容启动条件 (2026-08-08 K3 拍板 — CF 万圣节素材累积启动)
- **素材落盘 = 启动信号**: 季节集群设计主题的免费素材累积≥3 个 (如 CF freebies 记录) → 启动“素材→设计→下单→收货拍照→内容”闭环, 不等完整计划书
- 跟踪器: .hermes/logs/halloween-asset-chain.md (每日 brief 更新进度: 设计→下单→收货→拍照)
- 时间窗: 季节前 6-8 周启动最佳; 过时窗则评估是否下一季节。例: Halloween 集群目标 8/18 前上线

## 🔐 安全与审计铁律 (2026-08-07 Hermes 全权执行指令 #6)
- 所有浏览器 session cookie 仅存 `.hermes/secrets/` (gitignore 覆盖, 严禁 commit)
- 支付操作必须二次确认字段 (test_mode=true OR amount <= hard_limit); 测试订单: 单笔 <= $25, 当日累计 <= $50, 超限即暂停并告警
- 每次自动化执行生成 checksum (log + screenshot) 存入 `.hermes/audit/`
- 异常 (403/captcha/balance) 立即停止 + 告警, 不重试超过 2 次
- 浏览器操作 log 写 `.hermes/logs/browser-auto-{date}.md`, 含截图路径


## 定时任务统一管理铁律 (2026-08-08 user 拍板, evo-2026-08-08-cron-unify-autoclaw)
- **定时任务一律由 AutoClaw cron 统一管理**, 逐步取代 Hermes/mavis 的定时任务 (mavis CLI 已损坏, Hermes 侧黑盒)
- **新建/合并 cron 前必须先查重**: 读取本文件 §自动化管线 + C:\Users\Administrator\.hermes\cron\jobs.json + AutoClaw cron list, 防双系统重复触发
- **调度时间一律避开高峰期**: 批量任务落 18:00-08:00 夜间窗口或 12:05-13:30 午间窗口; 避开整点/半点, 用 7-23 或 37-53 分
- **当前状态 (2026-08-08)**: AutoClaw 4 个合并 cron (daily-ops 12:17 / daily-search 19:23 / weekly-review 周日 07:47 / seasonal-exec 8/10+8/18 19:37), 旧 10 个已删; 详见 .hermes/logs/cron-merge-20260808.md
- Hermes 侧 aitoptools-daily-content (13:30) 仍在 MiniMax app 内运行 → 并存期由 AutoClaw 幂等检查 (SKIPPED_HERMES_ALREADY_DONE) 兜底; 8/12 切换检查后建议停用
