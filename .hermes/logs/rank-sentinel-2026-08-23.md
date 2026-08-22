# rank-sentinel 2026-08-23

- date: 2026-08-23 04:2x CST
- window: 2026-08-16..2026-08-22 (滚动, 与 8/22 快照窗口 8/15..8/21 比较)
- status: PIPELINE-OK (第 8 天; GSC API 恢复 200 — 8/23 修复 header 拼写问题: 必须显式 Bearer 前缀)
- alerts: 1 持续 (print price, T2 回滚确认窗 Day-1)

## ALERT (变动 >=5 位)

1. **print price ai tool 71.92 -> 72.92 (再跌 1.0, 累计 vs 基线 62.75 = -10.17, imps 12)** — RANK-ALERT 持续 + STRATEGY T2 Day-1 确认窗触发 (仍 >=5 位低于基线). 处置: 回滚方案已备好 (.hermes/drafts/print-price-revert-0823.md, 只备不改); 8/24 Day-2 确认后执行 (git revert 或反向编辑 title/H1/FAQ + build + IndexNow).

## 其他变动 (无告警)

- is magicdrop legit 13.50 -> 13.40 (+0.10 微改善, 历史最佳区间维持)
- manychat shopify 89.88 -> 91.92 (-2.04, 观察)
- jasper ai review 90.00 -> 90.21 (-0.21)
- midjourney review 84.33 -> 84.62 (-0.29)
- omnisend review 86.44 -> 86.43 (+0.01)
- bluehost review 2026 67.43 -> 66.75 (+0.68 改善)
- descript.com reviews 71.33 -> 71.00 (+0.33)
- printful alternatives 78.00 -> 77.86 (+0.14)
- printify alternatives 85.60 -> 85.67 (-0.07)
- kittl review / canva vs kittl / kittl vs placeit / halloween x3 / printful vs printify / runway ml / best ai background remover / siteground / copywriting ai / sticker mule review / runway ml review: 0 展示 (持续低量噪音 + 悬崖期)

## HITS

- 命中 10/20; 全站 query 数 409 -> 314 -> 12 (悬崖期仅 12 query 有展示, 见 daily-ops T1 数据位)

## Boost 支持数据 (窗口 8/16..8/22)

- #1 stickermule-review 页级 15 imp pos 62.4 (悬崖期仍有展示, 抗跌) / #2 runway NODATA (主词 x5 连续) / #3 magicdrop 13.40 / #4 print price 72.92 (T2 Day-1) / #5 midjourney 84.62 / #6 jasper 90.21
