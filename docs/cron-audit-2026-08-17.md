# Cron 核对与修复报告（2026-08-17 05:0x）

> 执行：AutoClaw 执行层 · 依据：CRON-REGISTRY-2026-08-17.md（K3）+ STRATEGY-2026-08-17.md（T1 要求重建 T30）+ jobs.json 全量实测（30 条，mtime 08-17 04:59）
> 纪律：R-14「信 jobs.json、不信工具过滤视图」；cron 变更后以 jobs.json 验证落库

## 一、核对结论（注册表 10 任务 vs 实况）

| # | 任务 | 注册表调度 | jobs.json 实测 | 处置 |
|---|---|---|---|---|
| 1 | 每日联盟运营 | 每天 12:17 | cf28f53d ✅ enabled | 无动作 |
| 2 | 每日搜索增长 | 每天 19:23 | 78e5671a ✅ enabled | 无动作 |
| 3 | 每周复盘 | 周日 07:47 | c3a11910 ✅ enabled（最近 ok） | 无动作 |
| 4 | W1-0816 快修 | 8/16 07:15 | de9fad65 ❌ disabled（gateway restart 3 连错）+ 84c86e36 已跑完 | ✅ 实质完成（afc0dff 07:26，见 §二） |
| 5 | W2-0817 Boost56 | 8/17 08:41 | 6db4582b ❌ disabled（402+401） | ✅ **已恢复 enabled**（幂等轮 NOOP 预期） |
| 6 | W2-0819 GEO首读数 | 8/19 07:15 | 53646f7f ❌ disabled 且**工具视图不可达** | ✅ **已重建 43b01d80**（enabled，8/19 07:15，含 D7 兜底逻辑） |
| 7 | W2-0823 集群合并 | 8/23 07:15 | 1727c0ce ❌ disabled | ✅ 8/15 提前完成（cluster-push-0823.md 在库） |
| 8 | W3-0825 万圣节全量 | 8/25 07:15 | 98ebd150 ✅ enabled（d9aacbed 重复条 disabled） | 无动作（8/25 兜底轮有效） |
| 9 | W3-0831 IndexNow | 8/31 07:15 | 26a0ac2a ❌ disabled | ✅ 8/15 提前完成（indexnow-0831.md 在库） |
| 10 | W4-0913 T30校准 | 9/13 07:15 | 02fee02d ❌ disabled | ✅ **已恢复 enabled**（9/13 07:15，STRATEGY-0817 T1 要求） |

额外：季节集群执行（19de4109，8/18 19:37）✅ enabled；每日策略复盘 = K3 侧 Blueprint（automation_a826c0a9，17 21 * * *）不在 AutoClaw jobs.json，**不重复创建**（防双触发）。

## 二、8/16 主任务复盘（probe-1230.md + git 实测）

- 07:15 触发成功（jobs.json.bak 快照 runningAtMs=07:15:00.026；gateway 日志 07:15-07:17 模型调用全 200，zai 已恢复）
- run#1 超时（30min）→ run#2 滞留后被 18:08 gateway restart 收尾 → consecutiveErrors=3 自动禁用（非人为）
- **交付物 commit afc0dff（07:26:32）**：T1 copy-ai-review 补正 / T2 sitemap merged（单测 27/27，343/343）/ T3 辐条①补正 + T3b 11 篇字段 / T4 /resources/ 外链聚合页 / T5 僵尸 cron disable / T6 .gitignore；build PASS 202 文件/779 aff-link
- push 纪律：当日 1 次 ✅ 达标；T8 RESULT-0816 于 19:38 补齐（含 NORTH-STAR-DATA）

## 三、补跑节点状态（8/17 04:04 入队）

| 节点 | 产物 | 状态 |
|---|---|---|
| 万圣节全量（8/25 前置） | halloween-full-0825.md（04:17，3.6KB）+ RESULT-0817 | ✅ 完成：5/5 页上线（辐条③④补全，blog 11→13）、Kittl 三件套互链+UTM、GEO 三词入 keywords-200.csv、sitemap 344→346、IndexNow 5/5 200、单测 13/13 |
| T30 校准（9/13 前置） | t30-0913.md（04:14，10.2KB）+ RESULT-0913 早检版 | ✅ 完成（早检版）：GSC 30d 4,579imp/3clk、7d 日均 317.0（+61%）、Branch A 维持；9/13 正式校准由已恢复的 02fee02d 重写 |
| GEO 首读数（8/19） | geo-0819.md 缺失 | ⏳ 依赖 D7（CF token 未配 → Beacon NODATA，属数据源缺失非执行失败）；8/19 07:15 正式轮已就位（43b01d80，含人工导出兜底） |

## 四、风险置顶（今日起第 2 天）

1. **402 模型余额**：zai 已恢复（8/16 实测 200）；但 **deepseek fallback key（c493）仍 401 无效**——若 zai 再欠费，fallback 链全挂（8/17 Boost56 幂等轮即如此失败过）。按余额监控规则第 2 天 → **升级 user 二选一：充值 DeepSeek 或 config 接 MINIMAX fallback**。
2. D6 Printful cookie（8/18 截止，卡 Halloween 判定）/ D7 CF token（8/19 截止，卡 GEO 读数）：中文操作指引已在 action-cards-0816.md（含 F12 取 cookie 逐步步骤），待 user 执行。
3. D11/D12 待拍板（Q4 集群日历 / legit-check 首批 10 篇）——回复"同意"即生效，9/15 BF 开产倒计时。

## 五、验证（可复现）

- sqlite 权威库实测（8/17 05:1x）：02fee02d ✅ / 6db4582b ✅ / 43b01d80 ✅ / 1c606a9d ✅ 全部 enabled=1；每日 3 任务 + 98ebd150 在库 enabled
- **R-14 根因确认**：调度权威 = `C:\Users\Administrator\.openclaw-autoclaw\state\openclaw.sqlite` 的 cron_jobs 表（25 条）；jobs.json（30 条）是导出视图，两层存在 6 条差异（jobs.json 独有：4f19a24a/19de4109/53646f7f/4e8a51cd/c21196df/9efb842b；sqlite 独有：43b01d80）→ 千问 11524761611778 与工具 get/list 失效均由此层间差异解释；**今后 cron 增改后以 sqlite 验证**
- 补跑产物：.hermes/logs/halloween-full-0825.md、t30-0913.md 均存在非空；geo-0819.md 缺失=依赖 D7
- 回滚：若 8/19 GEO 轮与 53646f7f 意外双触发（不在 sqlite 不应触发），产物幂等键（geo-0819.md 已存在→NOOP）兜底；1c606a9d 与原 19de4109 同为 8/18 19:37 单日一次，原任务不在 sqlite 不会触发，无双触发
