# plan.md — PHASE-2026-08-13-09-13 指令执行闭环（workbench）

- taskId: goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645
- 发起: 2026-08-15 20:24 (Asia/Shanghai)
- 核心指令: handoff/strategy/PHASE-2026-08-13-09-13.md (v2.0, 8/15 更新)
- 背景约束: handoff/strategy/STRATEGY-2026-08-15.md (当日策略) + STRATEGY-2026-08-14.md (V2 执行解析)
- 冲突裁决: PHASE 优先，冲突点显式记录于风险清单
- 执行边界: 本地分析/文档/计算；不做外部发布、付款、真实部署、不可逆操作
- 输出语言: 中文
- 交付: DELIVERY/ 下总览 HTML + 台账/风险/复核/交接 MD

## 依赖图

```
[理解三文件] → [状态核查 S1] ─┐
                [技术债核查 S2] ─┼→ [S4 汇总+台账] → [S5 风险/复核/交接] → [HTML 交付]
                [交叉核验 S3] ─┤
                [队列准备 S4] ─┘
```

## 子任务 → subagent → 产物

| # | 子任务 | 角色视角 | 产物文件 | 复核项 |
|---|---|---|---|---|
| 1 | 状态核查：RESULT 三日齐全性 + NORTH-STAR-DATA + BOARD D 清单 + Boost 4/25 + 哨兵 + Halloween 链 | 事实核对员（只报证据，不推断） | subagent_01-status.md | 每个 PHASE §0 快照项 → 文件+字段证据；偏差标红 |
| 2 | 技术债：generate-sitemap.py 重复 bug 根因 + 修复补丁 + 单测（沙盒验证）+ sitemap 现况 342 断言 | 代码审计员（读码定位，改沙盒副本） | subagent_02-techdebt.md + sitemap_fix.patch + sitemap_fix_test.py | 根因行号；补丁最小化；沙盒测试 PASS 输出 |
| 3 | 交叉核验：三文件数字口径冲突（记分卡 A=180/138/14 vs git log A13→15/B39→51/C65→51、kittl 67.0 vs 63.0、W-8 工作日、push 是否含 #5/#6）+ cron 基线核对（jobs.json 21 条 vs STRATEGY-0814 §5 11 条 vs AGENTS.md 4 条） | 数字口径审计员（以一手证据文件裁决） | subagent_03-crosscheck.md | 每个冲突项给裁决+依据文件；cron 清单对比表 |
| 4 | 8/16-8/17 执行准备包：T1 快修 4 项现况 + 扩写 Top20 队列消费计划 + 外链首批 8 站台账 + Halloween 辐条①清单 + 幂等键表 | 执行准备员（只整理现有计划文件，不新写策略） | subagent_04-prep0816.md | 每项产出给可执行清单+现状证据 |

## 主线职责（非派单部分）
- 台账：PHASE 每条指令 → 任务条目（状态/证据/责任人/日期）
- 风险清单：阻塞、歧义、矛盾（含 8/14 cron 丢失事件复核、cron list 过滤为 0 的发现）
- 复核记录：对照 Goal Brief 7 项验收标准逐项自检
- 交接文档：未决项、下一步、回滚方式
- HTML 交付：Müller-Brockmann 功能主义网格（黑+纸白+琥珀单强调色，严格对齐）

## 幂等/纪律
- 只读现有文件；不改 src/ 生产代码（sitemap 补丁仅沙盒验证，是否应用由主线在复核后决定并记录）
- 所有产物 UTF-8；不碰凭证、secrets、git push
