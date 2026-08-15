# 执行准备包 — 8/16-8/17（subagent_04-prep0816）

> 生成: 2026-08-15 20:3x（整理视角，只读，未修改任何文件）
> 依据: bfix-plan-0816.md / bfix-0816.md（W1 执行报告）/ content-expansion-queue.md / link-building-0816.md / link-directory-list.md / halloween-asset-chain.md / halloween-deadline-0818.md / kittl-diagnosis-0814.md / boost-0817.md / STRATEGY-2026-08-15 / t7-0814.md / rank-sentinel-0812~0815 / scorecard-before·after.json
> 关键事实: **push 纪律已切换（8/15 user 拍板）**：产出即部署、当日 push；8/16 ★批量计划取消，改为"快修+扩写+外链当日合并 push"

---

## §1 T1 快修清单（8/16 B 类快修收尾 — 4 项）

> 计划来源: `.cluster/bfix-plan-0816.md` + STRATEGY-0815 T1。**注意**：bfix-plan 的「其余 54 页」清单（copy-ai-review 等）未出现在 STRATEGY-0815 T1 中，是否 8/16 一并处理需策略确认（W1 仅处理了 25 高优先页 + 3 个被触碰页）。

| # | 项目 | 目标文件/字段 | 问题描述 | 验收标准 | 现状证据 | 状态 |
|---|---|---|---|---|---|---|
| 1 | copy ai review 标题对齐（-7.5 微降告警，8/16 快修） | `src/data/reviews.json` → slug `copy-ai-review` 的 `title` / `metaDesc` | title 66 字符超长（>65，目标 50-60）；metaDesc 146 字符偏短（目标 150-160）；kw 已含（Copy.ai Review 前置，kw_ok=true） | title 50-60 + 主词前置；meta 150-160 + 数字锚点 + CTA；记分卡 title_ok/meta_ok=true | scorecard-after.json: `{"slug":"copy-ai-review","title_len":66,"title_ok":false,"meta_len":146,"meta_ok":false,"meta_digit":true,"meta_cta":true,"wc":121,"links":0}`；当前 title='Copy.ai Review 2026: Best AI Copywriting Tool for Marketing Teams?'；dateModified=None | **未修复**（W1 25 页清单不含此页）⚠️ 附带观察: wc=121 严重不足（<2500 军规线），links=0，建议一并评估扩写 |
| 2 | descript.com reviews 标题对齐 | `src/data/reviews.json` → slug `descript-review` 的 `title` / `metaDesc` | W1 已修：title 66→54（`Descript Review 2026: AI Video & Podcast Editor Tested`，主词前置），meta 164→150（含 $ 数字 + CTA "read our 2026 verdict"） | title 50-60 + kw 前置；meta 150-160 + digit + CTA | scorecard-after.json: `{"title_len":54,"title_ok":true,"meta_len":150,"meta_ok":true,"meta_digit":true,"meta_cta":true}`；bfix-0816.md §一 列 descript-review ∈ 25 页 ✅ | **已修复**（W1, 8/14）。⚠️ 需人工确认: T1 表述"descript.com reviews"如要求字面含 ".com"，当前 title 为 "Descript Review" 无 ".com"，按 bfix 规则（slug 主词前置）已达标，是否补 ".com" 由策略判断；wc=102 同样偏弱（观察项） |
| 3 | canva-vs-kittl 词序 | `src/data/comparisons.json` → slug `kittl-vs-canva` 的 `title`（路由 `src/app/compare/[slug]/page.js` 动态生成） | 搜索词 "kittl vs canva"（28d imp 17）+ "canva vs kittl"（imp 2）合计 19 imp，kittl 系第二大入口；页面标题需对齐主导词序 | title 词序 = "Kittl vs Canva"（主导查询序） | comparisons.json: `{"slug":"kittl-vs-canva","title":"Kittl vs Canva (2026): Which Design Tool Should POD Sellers Choose?"}`；bfix-0816.md §三: "对比页词序 'Kittl vs Canva' 已对齐 17-imp 主搜索词序，无需改动" | **已修复/无需改动**（W1 确认对齐） |
| 4 | printful alternatives 微降观察 | `src/data/listicles.json` → slug `printful-alternatives`（"7 Best Printful Alternatives for 2026"） | 观察项（无修复动作）：哨兵/GA 持续跟踪，微降即告警 | 无修复动作；观察是否持续下滑（<5 位波动属正常） | rank-sentinel-0815: `printful alternatives | 76.7 | 16 | 76.3 | 20 | +0.4`（稳定，无 ALERT）；t7-0814.md 决策树: "printful-alternatives 72.8→65.8 (+7.0)"（GSC 窗口口径改善）；8/12-8/15 哨兵 75.6→76.7 平稳 | **观察中·无下滑信号**（无需修复） |

**W1 已处理背景**（bfix-0816.md）: 高优先 25 页 title/meta 双达标 25/25（T 50-60 / M 150-160 / digit 25/25 / CTA 25/25），另修 kittl-review(184→159)/gear-launch(57→151)/removebg(95→150)；记分卡 A 13→15、B 39→52、C 65→50；快照 `.hermes/tmp/scorecard-before·after.json`。

---

## §2 S1 扩写队列（8/16 T3 消费对象）

> 来源: `.cluster/content-expansion-queue.md`（文件头标称 Top 20）
> **统计结论: 队列实载 7 项，非 20 项**（"## 全部候选"节为空）→ "Top 20" 名不副实，8/16 如需满 20 项队列需策略层补录

| # | slug | 展示 | pos | 变现 | 优先级 | 目标字数 | 当前状态（bfix-0816.md §二 W1 已全做完） | 证据 |
|---|---|---|---|---|---|---|---|---|
| 1 | printful-vs-printify | 82 | 77.6 | 1 | 高展示 | ≥1,500 | ✅ 1951→1959 词；内链 3；引用链 0→2；FAQ 7 | content-expansion-queue.md row1 + bfix-0816.md |
| 2 | kittl-vs-canva | 27 | 72.3 | 1 | 高展示 | ≥1,500 | ✅ 1841→1848；内链 4；引用 0→2；FAQ 6 | 同上 row2 |
| 3 | printful-vs-gelato | 20 | 46.5 | 1 | 高展示 | ≥1,500 | ✅ 1647→1668；内链 2→4；引用 0→2；FAQ 7 | 同上 row3 |
| 4 | best-ai-tshirt-design-generators | 15 | 68.0 | 1 | 高展示 | ≥1,500 | ✅ 859→1590（实扩：How We Tested + 7 工具表 + 逐工具点评）；内链 4；引用 0→2；FAQ 6 | 同上 row4 |
| 5 | printify-vs-gelato | 12 | 51.5 | 1 | 高展示 | ≥1,500 | ✅ 1681→1688；内链 4；引用 0→2；FAQ 7 | 同上 row5 |
| 6 | mockey-vs-placeit | 4 | 47.0 | 1 | 高展示 | ≥1,500 | ✅ 2321→2355；内链 0→3；引用 0→2；FAQ 7 | 同上 row6 |
| 7 | kittl-vs-placeit | 2 | 39.5 | 1 | 高展示 | ≥1,500 | ✅ 1596→1603；内链 4；引用 0→2；FAQ 7 | 同上 row7 |

- 引用链全部用实测核验官方定价页（kittl/canva/gelato/printify/placeit HTTP 200；printful 403 反爬但真实；mockey 525 边缘但真实）
- 证据要求（队列头部标准，W1 已全达标）: BLUF 首段 / 对比表 / FAQ≥5 / 内链 3-5 / 原创截图（**截图项 W1 未做**，属内容补强观察）
- **T3 消费结论**: 8/16 对 S1 的"扩写启动"= 队列 7 项已于 8/14 全部完成 → 幂等键应判 ALREADY-DONE/NOOP，除非策略层补充新队列（队列文件含空"全部候选"节，无 B 级候选项清单可消费）

---

## §3 S3 外链首批 8 站台账（8/16 T3 消费对象）

> 来源: `.hermes/logs/link-building-0816.md`（8/14 W1 实测）+ `.cluster/link-directory-list.md`（112 站调研：免费可投 104 / 纯付费 7 / 已死 1；dofollow 已核实或官方自述 12）
> **统计: 恰 8 站；8/8 均有免费入口，但 8/14 实测 0/8 提交成功（全部 BLOCKED，未硬闯）**

| # | 站点 | URL（提交页） | 免费可投 | 风险标注 | CAPTCHA/阻塞 | 提交方式 |
|---|---|---|---|---|---|---|
| 1 | AI Toolz Dir | https://www.aitoolzdir.com/submit | ✅ 免费档（需先挂站内回链，锚文本 "AI Toolz Dir"，DR66 dofollow） | 回链业务规则；API 无验证码 | 无 CAPTCHA；BLOCKED_REQUIRES_BACKLINK | 免费提交 API 已逆向实测: `POST /api/tool/submit/free`（JSON: name/url/logo/shortDesc/longDesc/category/email/type），请求体存档 `.hermes/tmp/linkbuild-0816/aitoolzdir-body.json` → **回链待 K3 拍板后可直接 API 重提** |
| 2 | Wired Business | https://wired.business/submit-your-website | ✅ 免费档 $0（需主页/footer 回链，DR77 dofollow 已实测，72h 审核）；Pro $29 免回链（FROGDR -30%=$20.30） | 回链业务规则 | 无验证码但 JS 流程表单，curl 无法提交；BLOCKED_REQUIRES_BACKLINK | 回链待 K3 拍板；拍板后人工浏览器提交 |
| 3 | Findly.tools | https://findly.tools/submit | ✅ 免费（挂 badge + 1 个永久 dofollow，DR80 已实测；$19 买 4 个） | badge 撤则链接失效 | Cloudflare Turnstile；BLOCKED_BY_CAPTCHA | 人工浏览器提交（挂 badge） |
| 4 | ToolPilot | https://www.toolpilot.ai/pages/submit-your-ai-tool | ✅ 免费（挂 badge，dofollow DR78 已实测） | 免费队列最长 90 天 | Shopify 全局 captcha（Turnstile）绑 contact 表单；BLOCKED_BY_CAPTCHA | 人工浏览器提交（挂 badge） |
| 5 | The Next AI | https://thenextai.com/submit-ai-tool/ | ✅ $0 基础档（数天发布，链接干净 dofollow 已实测，DR4 低） | 低 DR，仅铺量价值 | 提交页含 captcha；BLOCKED_BY_CAPTCHA | 人工浏览器提交（适合快速铺量） |
| 6 | LaunchBoosts | https://launchboosts.com/submit | ✅ 免费 | 官方自述 dofollow（未经外部核实） | Cloudflare challenge-platform 拦截；BLOCKED_BY_CAPTCHA | 人工浏览器提交 |
| 7 | Startuplist.in | https://startuplist.in/submit | ✅ 免费 | 官方主打免费 dofollow | 无验证码信息；两次请求连接超时（000）；BLOCKED_CONNECTION | 下次 cron 重试 |
| 8 | Dofollow.Tools | https://dofollow.tools/submit | ✅ 免费（全站每天 1 个免费位，等 7 天） | 外链交换模式（footer 互链 + badge，DR73） | 需注册账号（Next.js /api/auth）；BLOCKED_NEEDS_LOGIN | 暂缓（注册+互链成本） |

**关键事实标注**:
- ✅ **8 站均有免费入口**（但附条件：回链/badge/互链/人工过验证码）
- ⚠️ **Futurepedia 免费入口已关闭**（2026 起 $497 起，link-directory-list.md ❌ 不推荐区）— 不在首批 8 站内，8/16 不得投递
- 实体描述（人工提交统一用）: "aitoptools.net — Print AI Tools review site specializing in AI-powered solutions for print shops, packaging design, and e-commerce store operations. Founded by Jerome Tang of Shenzhen Cai Long Printing"；邮箱 jerome@aitoptools.net；目标 URL https://aitoptools.net
- 不硬闯原则: 表单被 CAPTCHA/登录墙/回链规则挡 → 记 BLOCKED_*；不自动加站内回链（需 K3 拍板）
- 待办拆分: ① 回链拍板 2 站（aitoolzdir/wired.business）② 人工浏览器提交 4 站（findly/toolpilot/thenextai/launchboosts）③ 重试 1 站（startuplist.in）④ 暂缓 1 站（dofollow.tools）

---

## §4 T4 辐条①发布清单（8/17 Halloween 素材实测）

> 来源: `.hermes/logs/halloween-asset-chain.md` + `halloween-deadline-0818.md` + STRATEGY-0815 T4
> 现状: **辐条①未上线**（blog-posts.json 现有 10 篇，含支柱 halloween-pod-ideas-2026 ✅ + 辐条② printful-vs-printify-halloween-2026 ✅，无辐条①）；素材链 0/4（设计 0 文件 / 下单 0 / 拍照 0 / 毛利无）

### 4.1 所需素材

| 素材 | 要求 | 现状证据 |
|---|---|---|
| Kittl 设计源文件 | 设计 1-2 个 → `.hermes/designs/halloween-test-{date}.png`（设计源已切换：8/11 起用 **Kittl 内置 Halloween 模板**，CF 素材降级为可选加分项——CF 付费墙实测绑定 All Access，自动化下载路径不存在） | `.hermes/designs/` = **空目录**（0 文件）；deadline 报告 P1-3: 8/15-16 可先行（不依赖 user） |
| 独家截图 3-5 张（blog 军规） | block type `screenshot`，路径 `/tool-screenshots/blog/{slug}-NN.webp`，先放 public/ 再引用；渲染器已确认支持（src/app/blog/[slug]/page.js `case 'screenshot'`: src/alt/caption） | `public/tool-screenshots/` 仅有 hostinger-home.webp + hostinger-pricing.webp 2 个非 blog 文件；**`public/tool-screenshots/blog/` 目录尚不存在，需新建** |
| 正文 | ≥2,500 字（军规 2,500-3,500），TL;DR → TOC → 第一人称实测 → 表格 → Pros/Cons → FAQ 4-5 → Related；CTA: **Kittl（Impact pxf.io 20%×12mo）**联动（STRATEGY T4: "Kittl 20%×12mo 联动"） | blog 模板: `scripts/templates/blog-post.example.json`（复制填值）；wordCount 由 page.js 自动统计（军规不足 2500 禁上线） |

### 4.2 发布步骤（顺序执行）

| 步骤 | 动作 | 证据/检查点 |
|---|---|---|
| 1 | 确定 slug（**文件中未定义，需执行层确定**，建议含 kittl/halloween 主词）+ 按 `blog-post.example.json` 结构写入 `src/data/blog-posts.json`（SSoT，数组追加） | 幂等键 = "辐条① live→NOOP"（检查 blog-posts.json 含 slug） |
| 2 | 截图转 WebP 放 `public/tool-screenshots/blog/{slug}-NN.webp`（新建目录） | 3-5 张；文件存在 + block 引用一致 |
| 3 | `python scripts/generate-sitemap.py`（合并保底模式，勿手改 sitemap） | 新 URL 在 public/ 与 out/ 的 sitemap.xml 均存在（sitemap 变更即推铁律） |
| 4 | `npm run build`（全量 PASS；blog-posts.json 非空约束已满足——现有 10 篇） | 构建页数只增不减 |
| 5 | IndexNow 增量推新 URL（参考 `scripts/submit_indexnow_blog_20260808.py` 模式；8/17 boost 已有 `submit_indexnow_boost_0817.py` 先例） | 日志 `.hermes/logs/indexnow-2026-08-17.log` 追加；HTTP 200 |
| 6 | git push（产出即部署纪律，当日 push；与同日 T3/T5 改动合并一次 build） | 以 CF Pages check-runs 为准 |
| 7 | 收尾: `.hermes/logs/halloween-asset-chain.md` 每日 brief 更新 + AFFILIATE_LOG.md C2b 计数表 + 若顺带提交则补 `llms.txt` 2 条 halloween blog 链接（P2-5，8/18 前） | llms.txt 现状: 仅 best-free-creative-fabrica-assets-this-week 1 条提及 halloween，支柱+辐条② 2 条缺失（deadline 报告 §4 GEO ❌） |

### 4.3 相关阻塞（不挡辐条①内容，但挡素材链 ②③④）

- **printful_session_cookie 缺失**（.hermes/secrets/ 无此文件）= 下单唯一硬阻塞（D6 行动卡，8/16 前补录）；test-address.json ✅ 已就位（8/10）
- 拍照 0/6（public/photos/wall/ 空）；fallback = 官方 mockup
- 8/18 deadline 判定 cron（T7, 19:37）将盘点素材链/照片墙 GO/NO-GO

---

## §5 Kittl review 待办（kittl-diagnosis-0814.md 消费）

> 诊断结论: **非真实下跌**（"kittl review" 仅 7 imp/28d 低量噪音；哨兵 8/12→8/13 -5.5 位属抖动）；真实风险 = 内容缺口 + 对比词入口未对齐

| # | 动作（诊断优先级） | 排期 | 8/15 现状 | 证据 |
|---|---|---|---|---|
| A | 内容补强 3 项: dateModified / featureLine / Sources 引用链 ≥1 | T14（8/21 前） | **已基本完成**（W1 重写覆盖）: dateModified=2026-08-15 ✅；featureLine ✅（'Vector-first AI design editor, Magic Resize, print-ready ex...'）；引用链 1→2 ✅（≥1 达标） | reviews.json kittl-review + bfix-0816.md §三 |
| B | 内链补覆盖（kittl-vs-canva / kittl-vs-placeit / 首页卡 / category 变体锚 → /kittl-review/） | T14 | 内链 2→5 ✅（≥4 达标）；词数 441→1,519 ✅；FAQ 5→6 ✅；修复 1 处未闭合 `<p>` bug | bfix-0816.md §三 |
| C | 对比页词序对齐（canva vs kittl + kittl vs canva = 19 imp 最大入口） | 8/16 B 类快修评估 | **已完成**（§1 第 3 项，kittl-vs-canva title 对齐 17-imp 主导序） | comparisons.json + bfix-0816.md §三 |
| D | 哨兵持续跟踪: 若 8/15-16 连续 >74 位 → Boost 队列插队 | 每日 | 8/14: 74.0→67.0（改善 7.0，恢复且低于前低 68.5）；8/15: 67.0→67.0（连续持平，imps 1，0 ALERT） | rank-sentinel-0814/0815 |
| E | Impact 数据回填后终判加投/撤位（判定线: ≥5 点击/天加投，1-5 维持，<1 撤首页 2 pxf） | user 回填后 | **待 user**: Impact 后台数字仍缺（8/11 指引未回填）；最新已知 = 7/30 时点 1 click/$0；pxf 链接已部署 4 处（首页卡/详情页/2 对比页） | kittl-diagnosis-0814 §二 + t7-0814 第 6 项 |

**消费建议**: 8/17 或后续 = 仅剩 D（每日哨兵，8/22 Boost T+14 复读验证）+ E（user 行动卡 5min）→ A/B/C 实质完成，**无内容待办遗留**

---

## §6 幂等键总表（8/16-8/17，源自 STRATEGY-2026-08-15 TASKS）

| id | 日期 | 任务 | 幂等键 | 检查方式 | 8/15 预判 |
|---|---|---|---|---|---|
| T1 | 8/16 | B 类快修收尾（copy ai review 标题对齐 / descript 词序 / canva-vs-kittl 词序 / printful alternatives 观察） | 当日已修→NOOP | scorecard 重跑: copy-ai-review `title_ok=true` / `meta_ok=true`；comparisons.json 词序比对；哨兵 printful alternatives 无 ALERT | 3/4 项已完（§1），**执行重点 = copy-ai-review 1 项** |
| T2 | 8/16 | generate-sitemap.py 重复追加 bug 修复（防 541 条复发） | 单测通过→NOOP | 脚本修复 + 单测脚本跑通；跑一次验证 sitemap 条数稳定（8/14 曾 541 条/唯一 342） | 专项审计员另处理（本包不含） |
| T3 | 8/16 | S1 B 级扩写启动（Top 20 队列）+ S3 外链首批 8 站 | 队列消费记录→NOOP | content-expansion-queue.md 消费记录 + link-building-0816.md 台账更新（8/14 已全量执行，**8/16 预期 NOOP**；若策略补新队列则消费新项） | 见 §2/§3 |
| T4 | 8/17 | 辐条① Halloween 素材实测（Kittl 设计 + 截图 3-5 张）发布 | 辐条① live→NOOP | blog-posts.json 含辐条① slug + build PASS + IndexNow log HTTP 200 + sitemap 含新 URL | 未开始（§4 全清单待执行） |
| T5 | 8/17 | 周一例行: geo-technical（schema 覆盖率）+ discovery-radar + mining | 当日日志存在→NOOP | `.hermes/logs/` 当日 geo-technical / discovery / gsc-mining 日志落盘 | 未开始（例行） |
| T6 | 8/17 | Boost #5/#6（midjourney/jasper）cron 到点幂等验证 | 内容已部署→NOOP | reviews.json `midjourney-review` + `jasper-ai-review` 的 `dateModified=2026-08-17` + featureLine 存在 + boost-0817.md 日志 + 8/15 push（commit b7df3ab） | **预期 NOOP ✅**（证据已核: 两页 dateModified=2026-08-17，featureLine 均在；IndexNow 8/14 已推 2/2 200，log `.hermes/logs/indexnow-2026-08-17.log` 已存在） |

**执行顺序建议（8/16）**: T1 修 copy-ai-review → T2（专项）→ T3 幂等确认 → 合并 build + 当日 push；**8/17**: T6 幂等 NOOP 记录 → T4 辐条①全流程 → T5 例行 → RESULT 当晚必写（T11）。

---

## 附录：关键路径索引

| 路径 | 用途 |
|---|---|
| `.cluster/bfix-plan-0816.md` | T1 修正规则与 25+54 页清单 |
| `.hermes/logs/bfix-0816.md` | W1 执行报告（8/14 已完成项的证据源） |
| `.hermes/tmp/scorecard-before·after.json` | 记分卡逐页诊断（117 页） |
| `.cluster/content-expansion-queue.md` | S1 队列（实载 7 项） |
| `.hermes/logs/link-building-0816.md` | S3 8 站提交台账 + AI Toolz Dir API body |
| `.hermes/tmp/linkbuild-0816/aitoolzdir-body.json` | 重提交请求体存档 |
| `.hermes/logs/halloween-asset-chain.md` / `halloween-deadline-0818.md` | T4 素材链 + 8/18 补漏清单 |
| `.hermes/logs/kittl-diagnosis-0814.md` | §5 待办源文件 |
| `.hermes/logs/boost-0817.md` / `indexnow-2026-08-17.log` | T6 幂等证据 |
| `scripts/generate-sitemap.py` / `submit_indexnow_blog_20260808.py` / `submit_indexnow_boost_0817.py` | T2/T4 工具链 |
| `scripts/templates/blog-post.example.json` / `src/app/blog/[slug]/page.js` | 辐条①结构与渲染（screenshot block 已支持） |
| `public/tool-screenshots/blog/`（需新建） | 辐条①截图落盘目录 |
