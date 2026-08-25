# rank-sentinel 2026-08-26

- date: 2026-08-26 04:4x CST
- window: 2026-08-19..2026-08-25（GSC T+1；8/25 哨兵未跑（cron billing cooldown 失败），相对上窗 8/17..8/23 平移 2 天）
- status: PIPELINE-OK（GSC API 200 rows=15，SOCKS5 OK）
- alerts: 1（T2 主词 print price ai tool 恢复 imps 且 pos 恶化触发回滚协议）

## ALERT（变动 >=5 位）

- **T2 print price ai tool：72.92 → 81.3（-8.38，窗口 8/19..8/25 vs 8/17..8/23）** — 悬崖期首度恢复 imps=12
  - 处置（按 8/24 哨兵日志既定协议）：imps 恢复且 pos>=67.75 → **执行回滚**（预案 .hermes/drafts/print-price-revert-0823.md）
  - PUSH_READY 已标记（daily-ops 2026-08-26），19:23 daily-search 消费执行；8/28 T+7 最终对照

## 悬崖期哨兵读数（窗口 8/19..8/25）

- **20q 命中 1/20**（上窗 2/20）— 悬崖持续且加深；仅 manychat shopify 有展示（imp9 pos91.3，vs 基线 91.92 = +0.62 改善）
- 其余 19 query NODATA（含 magicdrop：8/17..8/23 窗后再次 0 imps；bluehost/descript 上窗有量今日归零）
- 20q 内无 ≥5 位变动 → 无 20q RANK-ALERT

## T2 print-price Day-3（回滚确认窗）

| 窗口 | 主词 print price ai tool | Δ vs 基线 62.75 |
|---|---|---|
| 8/14-20 (8/21 读) | 62.75 @8 | 基线（方案 A 部署前） |
| 8/15-21 (8/22 复读) | 71.92 @13 | -9.17 |
| 8/16-22 (8/23 Day-1) | 72.92 @12 | -10.17 |
| 8/17-23 (8/24 Day-2) | NODATA (0 imps) | 无法比较 |
| 8/19-25 (8/26 Day-3) | **81.3 @12** | **-18.55** |

- **Day-3 结论：触发回滚条件（imps 恢复 12，pos 81.3 >= 67.75）** — 按 8/24 哨兵日志协议执行回滚；悬崖期 caveat 已记录（Branch B 滚动期至 9/6，但主词有量可比较，协议优先）
- 最终对照点：8/28 T+7 复读（daily-search/K3）

## Boost 支持数据（窗口 8/19..8/25）

- #1 stickermule-review NODATA / #2 runway NODATA / #3 magicdrop NODATA / #4 print price = ALERT（见上） / #5 midjourney NODATA / #6 jasper NODATA
- 悬崖期无新稳定信号词（design pickle 上窗 8 imps 今日归零）

## 跨窗口备注

- 8/25 哨兵缺失（cron 模型 billing cooldown 失败，consecutiveErrors=1），本窗为恢复后首读，窗口平移 2 天