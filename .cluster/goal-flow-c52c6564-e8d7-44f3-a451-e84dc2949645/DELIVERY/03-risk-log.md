# 03 风险与异常处理记录（定稿）— PHASE-2026-08-13-09-13 执行闭环

> 生成：2026-08-15 20:5x · 依据：4 路 subagent 报告（01 状态核查 / 02 技术债 / 03 交叉核验 / 04 执行准备）+ 主线 cron/git/文件核查
> 类型：🔴 阻塞（阻止进度）/ ⚠️ 偏差（与声明不符）/ ❓ 歧义（口径不清）/ 🧹 卫生（低危清理）
> 每条含处置建议与回滚/调整方式，可追溯

---

## R-01 🧹 cron 归属与可见性（8/14 丢失事件的复核结论）

- **描述**：cron 调度器共 26 个任务（sqlite，jobs.json），aitoptools 相关 14 条全部注册在 `agentId=main` 下；用 cron list 按 agentId=aitoptools 过滤返回 0，易被误判为「再次丢失」。**8/14 丢失事件后重建的任务实际全部在库，功能覆盖完整**。
- **证据**：C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json（26 条，main=14）；cron status jobs=21（不含 disabled）
- **处置建议**：① cron 健康核查一律读 jobs.json 全量 + `cron status` 总数，不信 agent 过滤的 list；② AGENTS.md「定时任务统一管理铁律」查重步骤改为读 jobs.json；③ 可选：将 main 名下任务 agentId 统一为 aitoptools（需确认 cron 工具过滤语义后由 user 拍板）。
- **回滚/调整**：无需回滚；若再发生丢失，按 STRATEGY-0814 §五 + jobs.json.bak 双源重建。

## R-02 ⚠️ cron 恢复基准名不副实（STRATEGY-0814 §五）

- **描述**：STRATEGY-0814 第五节声明「已在本文件记录全部任务清单作为恢复基准」，但该文件**未实际列出 11 条任务 id**；明示的 4 个新 id 中 f44b540b/52054088/4aa59006 不在库，但有功能等价物以新 id 在库（de9fad65/6db4582b/02fee02d，时间完全匹配）。
- **证据**：STRATEGY-0814.md §五 + jobs.json 全量比对（subagent_03 §5）
- **处置建议**：补一份真正的 cron 基线清单（本次台账 C 节即为此而建），写入 STRATEGY 存档；后续每次 cron 变更（新增/修改/删除）按 PHASE 指令 7 追加存档。
- **回滚/调整**：清单补齐后，任何任务丢失都按清单重建。

## R-03 🧹 cron 重复/僵尸任务（8/25 双触发风险）

- **描述**：① `W3-0825 万圣节全量push` 重复 2 条（98ebd150 + d9aacbed，同名、同时 8/25 07:15、均 enabled）→ **8/25 将双触发**，需删 1 条；② W1-0815 复核节点（4e8a920d）disabled 残留；③ W1-0814（4f19a24a）已触发仍 enabled（一次性任务触发后未自动禁用）。
- **证据**：jobs.json（主线 + subagent_03 §5）
- **处置建议**：8/16 合并 push 日顺手：删 1 条 W3-0825（删前复制 payload 到存档，遵守 PHASE 指令 7）；4e8a920d 可直接删除；4f19a24a 已触发无副作用，可禁用或删除。删除操作属 cron 修改，按纪律交 user 拍板或经 approval。
- **回滚/调整**：删除前存档 payload；jobs.json.bak 为最后兜底。

## R-04 ⚠️ 记分卡 A/B/C 数字口径冲突（PHASE 引用失真）

- **描述**：PHASE §零「A=180/B=138/C=14」vs 一手审计产物「341 页 A=187/B=138/C=16」（programmatic-audit-0813.md L17 + summary.json + commit 639936f）。A=180 全仓无出处（系转抄 RESULT-0812「333 页 A=180/B=138/C=14」的失真记录；而 RESULT-0812 的 333 vs 审计自述 333 但求和=341 亦内部不一致）。git log「A13→15/B39→51/C65→51」为 117 页子集口径，不可与全站对比。B=138 跨所有版本稳定。
- **证据**：subagent_01 §6 + subagent_03 §1（全仓 grep 无 A=180 出处）
- **处置建议**：全站口径统一采用 **341 页 A=187/B=138/C=16**（本次台账已按此修正）；B 级队列（138 页）不受影响；「333 vs 341」「180/14 出处」两点存疑，需千问/执行层回查 8/12 当晚生成记录；建议策略文件引用记分卡时附口径说明（全站 341 vs review 子集 107 vs 抽样 117）。
- **回滚/调整**：若千问确认另有口径，仅需更新台账 A 节与 B 节引用，不影响其他任务。

## R-05 ⚠️ 外链 8/16 执行现实 vs 排期（0/8 已实测）

- **描述**：首批 8 站均有免费入口，但 8/14 实测 0/8 提交成功：AI Toolz Dir（API 已逆向，需站内回链 DR66）与 Wired Business（DR77，需回链）→ **回链待 K3 拍板**；Findly/ToolPilot/TheNextAI/LaunchBoosts → CAPTCHA/登录墙，需人工浏览器提交（不硬闯）；Startuplist.in → 连接超时待重试；Dofollow.Tools → 需注册+互链，暂缓。
- **证据**：.hermes/logs/link-building-0816.md；subagent_04 §3
- **处置建议**：8/16 S3 任务=「重试 Startuplist + AI Toolz Dir API 重提（回链拍板后）+ 人工提交 4 站（user 在场时）+ 2 站回链请求」，产出台账更新；「首批 8 站落地」里程碑顺延至实际提交成功日并记录。Futurepedia 免费入口已关闭（$497 起），不在候选内。
- **回滚/调整**：回链未拍板前不自动加站内回链；CAPTCHA 不硬闯（纪律），可随时暂停。

## R-06 ❓ 哨兵数字口径提示（kittl 67.0 vs 63.0、copy ai -7.5）

- **描述**：kittl review 晨轮 67.0 vs 傍晚修订 63.0——同一指标（GSC 平均位置）不同数据时点（GSC T+2 补录 imps 1→2），**当前真实值 63.0**（三处一致），STRATEGY-0815 08:10 写 67.0 时点正确非错误；「-5.5」为 8/13 告警事件（68.5→74.0）已修复，现状 63.0 已优于告警前基线。「copy ai review -7.5」属 T+7 基线对比口径（73.4→80.9），哨兵 20q 追踪的是「copywriting ai」90.5（delta 0），两者不对应。
- **证据**：rank-sentinel-20q.json 5 快照 + rank-sentinel-2026-08-15.md 傍晚轮 + review-0815.md；subagent_01 §4、subagent_03 §2
- **处置建议**：策略文件引用哨兵数字时标注数据时点（晨轮/傍晚修订）；-7.5 快修目标以 bfix 记分卡字段（title 66→50-60、meta 146→150-160）为验收，不以哨兵数值为验收。
- **回滚/调整**：无。

## R-07 ⚠️ push 纪律执行偏差（8/15 实际 5 次 vs 单日 1 push）

- **描述**：8/15 为纪律切换首日（产出即部署），当日实际 5 次 push（02:51/03:51/04:00/04:26/19:25，达 daily-ops 自记 5 次日限）；2365ad4（20:27）已进 origin/main（若单独推送为第 6 次）；STRATEGY-0815 08:10「今日已 push 1 次」当刻已失真（当时 4 次）；push-count 自记口径（48e6163=1、2365ad4=2）与 daily-ops 5 次不一致。
- **证据**：git log + daily-ops-2026-08-15.md 终版；subagent_03 §7
- **处置建议**：8/15 含 8/13-14 攒批 flush（b7df3ab/f4f5c64/3d0f7f7 原计划 8/16 ★），属过渡期集中推送可解释；但 5 次/日对 CF build quota 有实耗，建议：① 统一 push 计数口径（按 daily-ops 日志为准，commit 内 push-count 字段废弃或改义）；② 8/16 起严格执行单日 1 push，多改动合并一次 build；③ BOARD.md 更新 8/15 记录（仍写「push 1 次」为 04:00 时点旧值）。
- **回滚/调整**：无回滚（已推送）；后续靠纪律执行 + 台账计数监督。

## R-08 ❓ S1 扩写队列规模（Top 20 名不副实）

- **描述**：content-expansion-queue.md 标称 Top 20，实载 7 项且 8/14 已全部扩写完成（wordCount 均 ≥1500、内链/引用/FAQ 达标）；「全部候选」节为空 → 8/16 S1「扩写启动」应判幂等 NOOP，除非策略层补录新队列。截图项 7 页均未做（内容补强观察项）。
- **证据**：.cluster/content-expansion-queue.md；bfix-0816.md §二；subagent_04 §2
- **处置建议**：① 8/16 T3 幂等 NOOP 并记录；② 请千问/策略层从 B 级 138 页按记分卡补建 Top 20 队列（或授权执行层按 programmatic-audit-0813 排序重建）；③ 队列文件头部「Top 20」改为实际数量，避免口径误导。
- **回滚/调整**：队列为数据文件，随时可追加；不涉及代码。

## R-09 ❓ W-8BEN-E 触发线口径（5 工作日 vs 8/18 从严线）

- **描述**：PHASE §五「超 5 工作日仍 Pending → 出行动卡」（以 v2 8/15 02:57 上传起算 ≈8/21-22）；执行层自设更早线「8/18 仍 Pending → 升级 user」（review-0815 傍晚轮）；STRATEGY-0815「超 3 工作日窗口」指 v1（8/9 提交，8/13 起超窗）。三条表述指代不同对象（v1/v2/从严线），均未定义工作日起算（8/15 周六上传 → 第 1 个工作日实际 8/17 周一）。
- **证据**：AFFILIATE_LOG.md 时间线 + review-0815.md + daily-ops-2026-08-15.md；subagent_03 §4
- **处置建议**：统一口径：以 v2 上传后第 1 个工作日（8/17 周一）起算，5 个工作日 ≈ 8/21（周五）；8/18 从严线保留为「早预警」不冲突，但上报时标注「从严线」；8/18 仍 Pending 且无响应 → 按从严线升级 user（不违反 PHASE，从严不越权）。
- **回滚/调整**：纯口径问题，无回滚。

## R-10 🔴 Halloween 素材链阻塞（D6 printful_session_cookie）

- **描述**：素材链 0/4（设计 0 文件 / 下单无 order_id / 拍照 0/6 / 毛利无）；下单唯一硬阻塞 = printful_session_cookie 缺失（.hermes/secrets/ 无该文件，env 无 PRINTFUL keys）。test-address.json 已就绪但**位于项目根**（F:\aitoptools\test-address.json）而非 .hermes/secrets/（位置与任务假设不符，已 gitignore 未入库，无泄露）。
- **证据**：halloween-asset-chain.md + halloween-deadline-0818.md + 目录实测；subagent_01 §5
- **处置建议**：① D6 行动卡（user 登录 Printful 后台取 cookie 存 .hermes/secrets/）8/16 前补录；② 8/18 判定：cookie 未就位 → 下单环节 NO-GO、内容环节照常（辐条① 8/17 发布不依赖 D6）；③ test-address.json 移入 .hermes/secrets/（或更新假设文档），保持 gitignore 覆盖。
- **回滚/调整**：下单属资金操作，永不自动执行（铁律）；cookie 补录后按订单限值（≤$25/笔、≤$50/日）执行。

## R-11 🧹 杂项卫生

- **描述**：① BOARD.md 头部自称「08:15 更新」实为 04:00 落盘、未随傍晚轮刷新（仍记 push 1 次）；② programmatic-audit-0813.md 节标题「C 级 14 页」下列 16 个 slug（14=review 子集、16=全量含 tool 类）；③ rank-sentinel-20q.json 主 queries 字段未覆写（67.0）与 snapshot 8/15-eve（63.0）并存；④ boost-0817.md 写于部署前（8/14），与「已部署」表面矛盾实为提交-推送分离；⑤ commit b7df3ab 标题「ops(0817)」日期笔误；⑥ workbench 缺 .cluster/expert-playbook.md（集群约定文件）。
- **处置建议**：①②③ 修正文档字段（下次 push 顺带）；④⑤ 已证实无偏差，仅备注；⑥ 交接文档中提示补齐。
- **回滚/调整**：无。

---

## R-12 ⚠️ 并行执行实例发现（8/15 20:45-21:05 外部会话已推进多任务）

- **描述**：执行本任务期间，另一执行实例（会话/进程）已将多项任务完成并推上 origin/main：b58cb7d（集群合并 push：四层内链第二轮 E-E-A-T、llms.txt 补 2 halloween、外链批2 12 站探测 0/12 BLOCKED、扩写队列 Top5-7 复核达标，build PASS 202 文件/779 aff-link，push-count=6）；a064467（T30 校准 cron 提前触发检查点：GSC 30d 4211imp/7d 日均 307.2、联盟 $0、beacon NODATA-D7、K3 KPI 六项核验：内链 597 达成/扩写 7of7/title-meta 25of25/排名 8q 改善 ≥5 位/外链 0of20 阻塞、Branch A 维持；02fee02d deleteAfterRun 将删原任务，重建规格入日志第七节）；8bd7ab1（W3-0831 IndexNow 全推收口 342 URL 200、sitemap 342/342、合并 2365ad4、.gitignore +.openclaw/）。另 20:45:43 外部修改 generate-sitemap.py（new_urls 去重 + robots 4 代理）→ 20:45:56 重生成 343 条 sitemap（仍无标记）。
- **证据**：git log origin/main（b58cb7d/a064467/8bd7ab1）；scripts/generate-sitemap.py mtime 20:45:43；public/sitemap.xml 343 条
- **处置建议**：① 台账 C 节部分任务已被外部实例提前完成（扩写 7of7、IndexNow 全推、T30 提前检查），8/16 cron 按幂等键消费（NOOP）即可；② sitemap 修复（本任务产物 v2）与外部改动不冲突——v2 补丁基于当前 HEAD 生成且 git apply --check 通过，合入时保留外部 robots 4 代理与 new_urls 去重（已并入 merged 版）；③ 多实例并发执行同一仓库存在互相覆盖风险，建议后续在每日策略中明确「同日仅一个执行实例推进代码类任务」。
- **回滚/调整**：外部改动均已入库可 revert；本任务未修改任何生产文件（v2 补丁仅 check 未 apply）。

## R-13 ⚠️ 辐条①提前上线但未达军规（8/15 20:47 外部实例发布）

- **描述**：外部实例已于 8/15 20:44-20:47 将辐条①写入 blog-posts.json（第 11 篇，slug=`kittl-halloween-template-test-2026`）并构建部署（out/blog HTML mtime 20:47；public/out sitemap 均含该 URL，blog 条目 12=11 文+1 索引）。但**未达 blog 军规**：① slug 含 "test"（生产 URL 命名不专业）；② publishedAt/wordCount/status 字段为 null（SSoT 结构缺失）；③ public/tool-screenshots/blog/ 目录不存在（军规要求 3-5 张独家截图，文章 blocks 疑似无截图）；④ 提前于排期（8/17）上线，8/17 cron 的 T4 幂等键需改为"辐条①已 live（不达标版）→ 补正"而非 NOOP。
- **证据**：blog-posts.json 第 11 篇字段；out/blog/kittl-halloween-template-test-2026/ mtime 08-15 20:47；public+out sitemap 含 slug（刷新脚本实测）
- **处置建议**：① 8/16 优先补正：补 publishedAt/wordCount/status 字段（字段可后补，不改 URL）；② slug 重命名需谨慎（URL 变更+IndexNow 重推+旧 URL 404），建议**不重命名**（IndexNow 已推送过该 URL，保一致），改为在文章内不影响 SEO 处说明；若千问坚持重命名，走"新 slug 发布 + 旧 URL 301/404 处理"流程（涉及部署，需 user 拍板）；③ 补截图需先造 Kittl 设计（夜间窗口）+ 截图转 WebP 放 public/tool-screenshots/blog/（目录新建）后二次 push（当日 1 push 合并）；④ 8/17 T4 任务改为"辐条①补正核验 + llms.txt 补 2 条 halloween 链接"。
- **回滚/调整**：不重命名前提下无需回滚；若重命名，git revert 该 blog 条目并走新 slug 流程。

## 需 user/千问拍板清单（汇总）

| 编号 | 事项 | 建议动作 | 时限 |
|---|---|---|---|
| P-1 | 记分卡口径：341 页 A=187/B=138/C=16 是否确认为全站基准；RESULT-0812「333/180/14」出处回查 | 千问确认 + 修正 PHASE 引用 | 8/16 前 |
| P-2 | W3-0825 万圣节全量 push 重复对删 1 条（98ebd150 或 d9aacbed） | user 拍板删除 + 存档 | 8/25 前（建议 8/16） |
| P-3 | push 计数口径统一（daily-ops 5 次为准；commit push-count 字段废弃） | 执行层定规 | 8/16 起 |
| P-4 | W-8 触发线口径统一（v2 起算 5 工作日 ≈8/21；8/18 从严线保留为早预警） | 千问确认 | 8/18 前 |
| P-5 | S1 扩写队列补建 Top 20（当前 7 项已完） | 千问补录或授权重建 | 8/16 起 |
| P-6 | 外链回链拍板（AI Toolz Dir / Wired Business 共 2 站） | K3/user 拍板 | 8/16 |
| P-7 | D6 printful_session_cookie 补录（user 行动） | user 登录取 cookie | 8/18 前 |
| P-8 | D7 CF API token 或 dashboard 导出授权（user 行动） | user 配置 | 8/19 前 |
