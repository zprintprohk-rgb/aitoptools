# 任务台账（v2 草稿，证据已回填 2/4：subagent_01 + subagent_04）— PHASE-2026-08-13-09-13 指令拆解

> 台账最终版 = 01-task-ledger.md。证据列来源：subagent_01-status.md（状态核查）、subagent_04-prep0816.md（执行准备）。待 subagent_02（技术债）、subagent_03（交叉核验）回传后定稿。

## A. 执行进度快照核验（PHASE §零）
| 条目 | PHASE 声明 | 一手证据 | 裁决 |
|---|---|---|---|
| T+7 首读数 Branch A 判定 | ✅ Branch A 温和加速 | t7-0814.md + RESULT-0814（subagent_01 §4） | ✅ 一致 |
| Boost 完成度 4/25 | 4/25（#1-#4） | boost-tracking.md L33/L114；RESULT-0813 | ✅ 一致 |
| #5/#6 已部署（8/15 push） | 已部署 | `git branch -r --contains b7df3ab` → origin/main 含 b7df3ab；boost-0817.md 写于部署前（表面矛盾已解） | ✅ 一致 |
| 记分卡 A=180/B=138/C=14 | A=180 / B=138 / C=14 | programmatic-audit-0813.md L17 = **A=187/B=138/C=16**（341 页）；A=180 无出处；A13/B39/C65 是 117 页抽样旧值 | ❌ **偏差**（A 差 7、C 差 2）→ 进风险清单 |
| 外链 S3 首批 8 站排 8/16 | 首批 8 站 | link-building-0816.md：8 站均有免费入口，但 8/14 实测 0/8 成功（6 CAPTCHA/登录、2 需回链拍板） | ⚠️ 部分偏差（8/16 可执行=重试+拍板请求）→ 进风险清单 |
| 联盟 7 活跃 + Synthesia | 7 活跃 + Synthesia 待确认 | BOARD.md 行动卡 3 项（Synthesia 2min / Kittl 回填 / Printify 催办） | ✅ 一致 |
| D6/D7 阻塞 | D6 printful_session_cookie / D7 CF token | BOARD.md L10-11；.hermes/secrets/ 无 cookie 文件；D6 为 Halloween 下单唯一阻塞；D7 为 8/19 GEO 读数前置 | ✅ 一致 |
| push 纪律切换 | 8/15 拍板：产出即部署 | 8/15 实际 **5 次 push**（02:51/03:51/04:00/04:26/19:25），daily-ops-0815 终版记「5 次, 达日限」；BOARD 仍记「push 1 次」（04:00 时点未刷新） | ⚠️ 纪律执行偏差（日 1 push vs 实际 5）→ 进风险清单 |
| generate-sitemap.py 重复 bug | 8/16 必修 | 8/14 曾 541 条/唯一 342（3d0f7f7）；根因分析待 subagent_02 | 待回传 |
| cron 健康 11 任务重建 | 8/14 丢失已闭环 | jobs.json（主线已核）：main 名下 14 条（13 enabled + 1 disabled），11 个重建任务均存在；**W3-0825 万圣节全量push 重复 2 条** | ⚠️ 已闭环但发现重复任务 → 进风险清单 |

## B. 阶段目标（PHASE §一，9/13 验收）
1. Boost 25/25 + print-price 8/21 ≤30 → 8/21 里程碑、9/13 验收（未到期，跟踪中）
2. B 级扩写 Top 20 + 外链首批 8 站 → ⚠️ 队列实载 7 项且已全完成（非 20）；外链 0/8 → 进风险清单
3. Halloween 集群 9/1 前全量（8/18 判定 GO 为前提）→ 素材链 0/4、照片墙 0/6、辐条①未上线；D6 是唯一硬阻塞（不挡内容发布）
4. 8/19 GEO 首读数 → D7 CF token 前置未就绪；beacon 已上线（8/15 首读 24h：3 visits/4 PV/797ms；AI UA 视图 NODATA）
5. Shopify 9/4 + Placeit 催办 + Printify 资格确认（8/26-30）→ 未到期，跟踪中

## C. 周度排期（PHASE §二）→ cron 映射（jobs.json main 名下，主线已核）
| 日期 | 任务 | cron | 状态 |
|---|---|---|---|
| 8/16 | B 类快修收尾 + sitemap 修复 + S1 扩写启动 + S3 外链 | W1-0816 B类快修push（8/16 07:15） | 已排期；快修实待办=copy-ai-review 1 项；S1/S3 预期幂等 NOOP 或重试 |
| 8/17 | 辐条①发布 + IndexNow + 周一例行 + Boost #5/#6 幂等 | W2-0817 Boost56（8/17 08:41） | 已排期；T6 预期 NOOP（dateModified=2026-08-17 已写入） |
| 8/18 | Halloween 判定 19:37 | 季节集群执行（8/18 19:37） | 已排期 |
| 8/19 | GEO 首读数 07:15 | W2-0819 GEO首读数（8/19 07:15） | 已排期；D7 前置未就绪 |
| 8/23 | 集群+改造合并 push | W2-0823 集群合并push（8/23 07:15） | 已排期 |
| 8/25 | 万圣节全量 push | W3-0825 万圣节全量push（8/25 07:15）⚠️ 重复 2 条 | 已排期/重复 |
| 8/31 | IndexNow 全推 | W3-0831 IndexNow全推（8/31 07:15） | 已排期 |
| 9/13 | T+30 全量校准 | W4-0913 T30全量校准（9/13 07:15） | 已排期 |
| 周日 | 每周复盘 07:47 | 每周复盘 | 已排期 |
| 每日 | 联盟运营 12:17 / 搜索增长 19:23 | 每日联盟运营 / 每日搜索增长 | 已排期 |

## D. 执行层增强指令（PHASE §三，1-9）状态
1. 排名哨兵：✅ 运行中（8/15 双轮 0 ALERT；kittl 最新 63.0）
2. 记分卡口径：✅ 已应用（6 项检查；A/B/C 计数需按 187/138/16 修正口径）
3. 辐条②模板：✅ 已产出（2,574 词/双 CTA/多源交叉，辐条② live 8/11）
4. 内容断供守护：✅ 8/13-15 三日 RESULT 齐全
5. push 纪律：⚠️ 已切换但 8/15 实际 5 push（执行偏差，进风险）
6. RESULT 每晚必写：✅ 8/9-8/15 连续齐全（NORTH-STAR-DATA 均含）
7. cron 备份纪律：⚠️ STRATEGY-0814 §5 为基准；8/15 后无新 cron 变更，无需追加存档；**但发现重复任务 W3-0825 → 需删一条并存档**
8. 校验闸门：✅ 8/15 各 push 前 build PASS 记录在案
9. sitemap 修复验证：⏳ 8/16（待 subagent_02 根因+补丁）

## E. 决策树闸门（PHASE §四）
- 8/14 T+7 Branch A ✅ 已执行（后续分支保留）
- 8/19 GEO 首读数：D7 未就绪 → 顺延风险（顺延 ≥3 天升级 user）
- 8/22 T+14 Boost 判定：A/B/C/D 分支待 8/22
- 9/13 T+30：V2 口径 ≥$300 / $150-300 / <$150 三分支

## F. 待核实项（PHASE §五）
| 项 | 状态 | 下一步 |
|---|---|---|
| Printify 挑战门槛 | ✅ 已核实（ALLOWED-WITH-CONDITIONS，月访客 1000 不满足） | 8/26-30 资格问询 |
| Shopify 条款 | ⚠️ 第三方口径 | 9/4 前官方实证 |
| Kittl Expert 数据 | 假设非事实 | user 回填 Impact（行动卡 2） |
| W-8BEN-E | Pending（uploaded-pending-review，8/15 02:57 上传后第 1 个工作日，3 business days 窗口内） | 每日 tax-audit 复核；8/18 仍 Pending → 出行动卡 |
