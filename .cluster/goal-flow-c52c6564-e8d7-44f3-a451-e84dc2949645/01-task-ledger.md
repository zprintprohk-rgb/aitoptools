# 01 任务拆解与追踪清单 — PHASE-2026-08-13-09-13 指令台账（定稿）

> 生成：2026-08-15 20:5x · 主控汇总（依据 4 路 subagent 报告 + 主线 cron/git 核查）
> 指令源：handoff/strategy/PHASE-2026-08-13-09-13.md（v2.0）；冲突裁决：PHASE 优先，详见 03-risk-log.md
> 状态图例：✅ 已完成 / ⚠️ 部分完成或有偏差 / ⏳ 已排期待触发 / 🔴 阻塞 / ⏸ 暂停待拍板

## A. 执行进度快照核验（PHASE §零 — 8/15 08:30 口径 vs 8/15 20:5x 实测）

| # | 快照项 | PHASE 声明 | 实测裁决 | 证据 | 状态 |
|---|---|---|---|---|---|
| A1 | T+7 首读数 | Branch A 温和加速 | 成立（216.5/197=+10%，1299/6 精确） | t7-reading-2026-08-14.md；subagent_03 §6 | ✅ |
| A2 | Boost 完成度 | 4/25（#1-#4） | 成立；#5/#6 已部署（b7df3ab ∈ origin/main） | boost-tracking.md L33/L114；subagent_01 §3 | ✅ |
| A3 | 记分卡 | A=180/B=138/C=14 | **偏差**：审计产物为 341 页 A=187/B=138/C=16；A=180 无出处（转抄 RESULT-0812 失真）；A13→15/B39→51/C65→51 为 117 页子集口径 | programmatic-audit-0813.md L17 + summary.json；subagent_01 §6、subagent_03 §1 | ⚠️ 需千问确认口径（R-04） |
| A4 | 外链 S3 | 首批 8 站排 8/16 | 8 站均有免费入口但 8/14 实测 0/8 成功（6 CAPTCHA/登录、2 需回链拍板） | link-building-0816.md；subagent_04 §3 | ⚠️ 执行现实偏差（R-05） |
| A5 | 联盟 | 7 活跃 + Synthesia 待确认 | 成立；行动卡 3 项在 BOARD | BOARD.md L16-20；subagent_01 §2 | ✅ |
| A6 | 阻塞 | D6 printful_session_cookie / D7 CF token | 成立：D6 为 Halloween 下单唯一硬阻塞（secrets 无 cookie）；D7 为 8/19 GEO 读数前置（beacon 已上线，8/15 首读 3 visits/4 PV/797ms，AI UA 视图 NODATA） | BOARD.md L10-11；halloween-deadline-0818.md；subagent_01 §5 | ⚠️ 双前置均未就绪（user 行动卡） |
| A7 | push 纪律 | 产出即部署、单日 1 push（8/15 切换） | **偏差**：8/15 实际 5 次 push（02:51/03:51/04:00/04:26/19:25），daily-ops 自记「5 次, 达日限」；2365ad4 20:27 已进 origin/main | git log + daily-ops-2026-08-15.md；subagent_03 §7 | ⚠️ 纪律冲突（R-07） |
| A8 | 技术债 sitemap | 8/16 必修 | 根因已定位（generate-sitemap.py L92-96 切分丢 PROGRAMMATIC-SEO 标记 → generate-pages.js 幂等正则失配 → 每次 +199 必复发）；补丁+单测 20/20 PASS（待代码复核员独立确认） | subagent_02；review-code.md（待回传） | ⏳ 8/16 T2 应用补丁 |
| A9 | cron 健康 | 8/14 丢失已闭环，11 任务重建 | 成立且有新发现：26 任务在库（main=14）；11 重建任务功能覆盖完整；**W3-0825 万圣节全量push 重复 2 条**（8/25 双触发风险）；4e8a920d 停用残留；4f19a24a 已触发未禁用；agentId 全部=main（cron list 按 aitoptools 过滤=0 的根因） | jobs.json（主线 + subagent_03 §5） | ⚠️ 需清理（R-02/R-03） |
| A10 | 哨兵 | 每日 20q，变动 ≥5 位告警 | 成立：8/15 双轮 0 ALERT；kittl review 最新 63.0（8/15-eve，GSC T+2 修订，非 67.0）；copy ai -7.5 属 T+7 基线口径（哨兵追踪 copywriting ai 90.5 delta 0） | rank-sentinel-20q.json + rank-sentinel-2026-08-15.md；subagent_01 §4、subagent_03 §2 | ✅（口径提示见 R-06） |

## B. 阶段目标跟踪（PHASE §一 — 9/13 验收）

| # | 目标 | 当前状态 | 关键路径/前置 | 状态 |
|---|---|---|---|---|
| B1 | Boost 25/25 + print-price 8/21 ≤30 | 4/25（+2 已部署未计入）；print-price 65.5（+4.0 改善） | 每天 1 页；8/21 里程碑读数；8/22 T+14 判定 | ⏳ |
| B2 | B 级扩写 Top 20 + 外链首批 8 站 | 队列实载 7 项且 8/14 已全完成（非 20，名不副实）；外链 0/8 | 补建 Top 20 队列（需千问）；外链回链拍板 2 站 + 人工提交 4 站 + 重试 1 站 | ⚠️ R-05/R-08 |
| B3 | Halloween 集群 9/1 前全量 | 支柱✅ 辐条②✅ 辐条①未上线；素材链 0/4、照片墙 0/6 | 8/17 辐条①发布（Kittl 设计+截图 3-5 张）；8/18 判定（D6 cookie 决定下单环节 GO/NO-GO，内容环节不受阻） | ⏳ |
| B4 | 8/19 GEO 首读数 | beacon 上线 8/12；8/15 首读 24h 3 visits/4 PV | D7 CF token（或 dashboard 人工导出）；顺延 ≥3 天升级 user | ⚠️ 前置未就绪 |
| B5 | 高佣：Shopify 9/4 + Placeit 催办 + Printify 挑战 | Printify 挑战门槛受限（月访客 1000 不满足，已实证）；Shopify/Placeit 未到期 | W3 资格问询（8/26-30）；9/4 申请行动卡 | ⏳ |

## C. 周度排期任务（PHASE §二 → cron 映射，jobs.json main 名下）

| # | 日期 | 任务 | cron id（名称） | 状态 |
|---|---|---|---|---|
| C1 | 8/16 | B 类快修收尾 + sitemap 修复 + S1 扩写启动 + S3 外链 | de9fad65（W1-0816 B类快修push 07:15） | ⏳ 实待办收窄：快修=copy-ai-review 1 项；sitemap=应用补丁；S1/S3 幂等 NOOP/重试 |
| C2 | 8/17 | 辐条①发布 + IndexNow + 周一例行 + Boost #5/#6 幂等 | 6db4582b（W2-0817 Boost56 08:41） | ⏳ T6 预期 NOOP（dateModified=2026-08-17 已写入） |
| C3 | 8/18 | Halloween 判定 19:37 | 19de4109（季节集群执行 8/18 19:37） | ⏳ |
| C4 | 8/19 | GEO 首读数 07:15 | 53646f7f（W2-0819 GEO首读数 8/19 07:15） | ⏳ 依赖 D7 |
| C5 | 8/23 | 集群+改造合并 push | 1727c0ce（W2-0823 集群合并push 8/23 07:15） | ⏳ |
| C6 | 8/25 | 万圣节全量 push | 98ebd150 + d9aacbed（W3-0825 重复 2 条） | ⚠️ 删 1 条（R-03） |
| C7 | 8/31 | IndexNow 全推 + sitemap 核验 | 26a0ac2a（W3-0831 IndexNow全推 8/31 07:15） | ⏳ |
| C8 | 9/13 | T+30 全量校准，出 Phase 3 | 02fee02d（W4-0913 T30全量校准 9/13 07:15） | ⏳ |
| C9 | 每日 | 联盟运营 12:17 / 搜索增长 19:23 | cf28f53d / 78e5671a | ✅ 运行中 |
| C10 | 周日 | 每周复盘 07:47 | c3a11910 | ✅ 运行中 |

## D. 执行层增强指令（PHASE §三 1-9）状态

| # | 指令 | 状态 | 证据/说明 |
|---|---|---|---|
| D1 | 排名哨兵每日 20q | ✅ | 8/12 起每日运行；8/15 双轮 0 ALERT |
| D2 | 记分卡口径（≥5=A/3-4=B/≤2=C） | ✅ | 已应用；A/B/C 计数按 187/138/16 修正（R-04） |
| D3 | 季节内容辐条②模板 | ✅ | 2,574 词/双 CTA/多源交叉；辐条② live 8/11 |
| D4 | 内容断供守护 | ✅ | 8/13-15 RESULT 连续齐全（8/9 起 7 连） |
| D5 | push 纪律（产出即部署，单日 1 push） | ⚠️ | 已切换但 8/15 实际 5 次（R-07）；计数口径待统一 |
| D6 | RESULT 每晚必写 + NORTH-STAR-DATA | ✅ | 三日齐全；NORTH-STAR-DATA 均在 L20-21 |
| D7 | cron 配置备份纪律 | ⚠️ | STRATEGY-0814 §5 未实际记录 11 条 id（恢复基准名不副实，R-02）；8/15 后无新 cron 变更 |
| D8 | 产出即部署校验闸门 | ✅ | 8/15 push 前 build PASS 记录在案 |
| D9 | generate-sitemap.py 修复验证 | ⏳ | 根因+补丁+单测 20/20 就绪（subagent_02）；待代码复核 + 8/16 应用；应用后断言 342 无重复、cron 恢复自动调用 |

## E. 决策树闸门（PHASE §四）

| 闸门 | 时点 | 条件 | 状态 |
|---|---|---|---|
| T+7 Branch A | 8/14 | 已执行：日均展示 216.5 ≥200 → Branch A 温和加速 | ✅ 已判定 |
| 风险开关 | 随时 | 连续 2 日哨兵下滑 ≥10 位 → Branch D | 未触发（8/15 0 ALERT） |
| GEO 首读数 | 8/19 | AI 引荐流量 >0 持续投入 / =0 降维护级；D7 未就位顺延，≥3 天升级 user | ⏳ 依赖 D7 |
| T+14 Boost 判定 | 8/22 | A(≥5位)维持 / B(1-4位)维持+外部信号 / C(无移动)URL Inspection / D(下降)减内链暂停 2 天 | ⏳ |
| T+30 校准 | 9/13 | 月化 ≥$300 提强度 / $150-300 重排 / <$150 战略复审 | ⏳ |

## F. 待核实项（PHASE §五）

| # | 项 | 状态 | 结论/下一步 | 截止 |
|---|---|---|---|---|
| F1 | Printify 挑战门槛 | ✅ 已核实 | ALLOWED-WITH-CONDITIONS：月访客 1000 不满足 → W3 资格问询（豁免/达标路径），确认前不制作投稿内容 | 8/26-30 |
| F2 | Shopify 联盟条款 | ⚠️ 第三方口径 | 官方/Impact 实证后出申请卡 | 9/4 |
| F3 | Kittl Expert 订阅数据 | 假设非事实 | user 回填 Impact 后 9/13 替换 | 9/13 |
| F4 | W-8BEN-E 审批 | Pending（v2 8/15 02:57 上传，第 1 个工作日窗口内） | 每日 tax-audit 复核；5 工作日线 ≈8/21-22；执行层 8/18 从严线（口径待统一 R-09） | 持续 |
