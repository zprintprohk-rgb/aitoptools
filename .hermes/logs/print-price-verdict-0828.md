# print-price T+7 终判 (8/28 窗口 · 8/27 03:0x 提前执行)

> 数据来源: GSC API (sc-domain:aitoptools.net, searchAnalytics/query, 2026-08-27 03:0x 拉取, SOCKS5 127.0.0.1:7892) + 历史窗口记录 (daily-ops-0823/0824/0826, daily-search-0826, RESULT-0826, commit 47858ad/effa8fa)
> 判定依据: STRATEGY-2026-08-25 T3 (K3 拍板, 回滚触发 81.3>=67.75) + .hermes/drafts/print-price-revert-0823.md + 8/28 终判 cron payload 规则
> 窗口说明: 请求 8/21-8/27; GSC T+1, 实际含至 8/26 终值 (8/27 当日数据 8/28 才出)。本次为手动提前执行 (cron 8/28 20:37 槽位已消费, deleteAfterRun 一次性)

## 一、数据
| 窗口 | imps | clicks | pos | 备注 |
|---|---|---|---|---|
| 基线 (6/28-8/5) | - | - | 62.75 | 优化前基线 (boost-tracking.md) |
| 8/16-8/22 | - | - | 72.92 | T2 Day-1, vs 基线 -10.17 位 |
| 8/19-8/25 | 12 | - | 81.3 | Day-3 复读, 触发回滚 (8/26 执行) |
| 8/21-8/27 (至 8/26) | 8 | 0 | 82.62 | 本次终判窗口, CTR 0 |

窗口内全站 query 维度共 11 行有展示 (悬崖期低位环境), 主词 print price ai tool 为该窗口最高 imps query 之一。

## 二、判定: 维持方案 A 已回滚对照 ✅
- 命中分支: **位置 82.62 ≥ 67.75 且 imps=8 > 0** → 维持方案 A 已回滚对照
- 8/26 已执行回滚 (还原 title/meta/H1/首段/FAQ, 保留 Kittl 定价修正 3 处, dateModified=8/26, IndexNow 已推) → 状态确认, 不回改
- 方案 A (calculator 意图优化版) 不回恢复; 已回滚版 (旧 H1/首段) 作为对照继续观察
- 悬崖期 caveat: 全站处于 Branch B 滚动期 (至 9/6), 数据环境低位; 主词有量 (imps=8) 可比较, 协议优先 (与 8/26 同口径)
- 未命中分支: pos<67.75 作废预案 (未触发, 预案保留待后续窗口); NODATA 顺延 (不适用, 有数据)

## 三、动作
- 无内容改动, 无 push 需求 (回滚已就位, 本次仅确认状态 + 记录)
- 后续复核点: 9/6 Branch B 滚动期结束 / 9/13 T30 校准 (t30-0913.md) 一并复核
  - 若后续窗口 pos 回升 <67.75 且 imps 恢复 → 方案 A 作废预案正式落档
  - 若 pos 持续 ≥67.75 → 已回滚版定档, 方案 A 关闭 (calculator 产线立项样板状态同步 BOARD)
- 幂等: 本文件存在非空 → NOOP