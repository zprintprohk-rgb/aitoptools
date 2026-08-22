# print-price 回滚预案 (T2 Day-1, 只备不改) — 2026-08-23

> 触发: STRATEGY-2026-08-23 T2 — print price ai tool 72.92 (8/16..8/22) vs 基线 62.75 = -10.17 位, 连续 2 窗 >=5 位低于基线; Day-1 确认窗触发, 预案备好待 8/24 Day-2 确认

## 回滚对象 (8/21 方案 A 部署内容, commit 55bb1a2)

1. title: Print Price Calculator 2026 -> 还原为 print price ai tool 主词版本
2. H1: 还原 (calculator 意图 -> 原始定位)
3. 首段: calculator-first -> 还原 BLUF
4. FAQ +1 (free print price calculator) -> 删除
5. dateModified 8/21 -> 回滚当日刷新 (回滚动作也算一次更新)

## 执行步骤 (8/24 Day-2 确认后)

1. git log 定位 55bb1a2 中 print-price-ai-tools-2026 相关 diff
2. 反向编辑 src/data/blog-posts.json (或对应 reviews 数据) — 精确还原 title/H1/首段/FAQ
3. npm run build PASS + 本地核验 (title/H1 已还原)
4. IndexNow 推 /blog/print-price-ai-tools-2026/ (submit_indexnow 脚本)
5. 8/28 T+7 复读对照 (若回滚后回升则确认 calculator 意图误判)

## 反触发条件 (不回滚)

- 8/24 窗口回升 (72.92 -> <67.75, 即 <5 位低于基线) 或 imps 恢复
- T1 悬崖判定为分支 A (数据滞后) 且回填后 print price 位置同步恢复 — 悬崖期数据整体不可信时顺延判定

## 备注

- 本预案只备不改; 执行权在 8/24 daily-search/K3 判定后
- 与悬崖判定联动: 若 8/21-8/22 数据回填后 print price 位置大幅修正, 本预案作废重评
