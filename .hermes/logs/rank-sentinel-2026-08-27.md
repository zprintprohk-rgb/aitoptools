# rank-sentinel 2026-08-27

- date: 2026-08-27 补偿 (daily-ops 8/27 billing 失败, 8/28 02:3x 补跑)
- window: 2026-08-21..2026-08-27 (GSC API 实时, 滚动 +2d vs 8/26 快照)
- status: PIPELINE-OK (gsc_query.py 200, SOCKS5) | 悬崖 Day-10 (8/18 起)
- alerts: **0 新增** (print price 回滚后对比无 ≥5 告警)

## 20q 命中 (3/20 有展示, 悬崖期基数极低)
| query | pos | imp | vs 上窗 | 判定 |
|---|---|---|---|---|
| manychat shopify | 90.6 | 8 | 91.92 → 90.6 (+1.3) | 无告警 |
| print price ai tool | 83.7 | 10 | 81.3 (8/25 回滚触发位) → 83.7 (-2.4) | 无告警; 回滚维持 (8/27 终判 82.62 >= 67.75) |
| sticker mule | 35.0 | 1 | 35.0 → 35.0 (持平) | 无告警; T+14 Branch B 确认位维持 |

## 0 展示 (17/20)
printful/printify alternatives, canva vs kittl, kittl review, kittl vs placeit, halloween x3, printful vs printify, runway ml (+review), best ai background remover, siteground, copywriting ai, bluehost review 2026, omnisend review, descript, designpickle

**⚠️ 值得记录**: is magicdrop legit 本窗 0 展示 (8/14-20 窗曾 40 imp @12.9) — 悬崖对最强页也无豁免; 12.9 排名位仍在 (排名稳, 展示层被压), 符合 Branch B 判定

## 窗口新词 (非哨兵, 参考)
- writesonic 裸词 pos 1.0 @2 / adcreative.ai review pos 1.0 @1 / omnisend 裸词 pos 9.5 @2 / mockey pos 37.5 @2 / zyro 88.0 / b12 ai 3.0 — 均为 1-2 imp 噪声级, 其中 writesonic/omnisend/adcreative 裸词高位值得后续观察 (我们有无对应页: writesonic-review 排期 P2 暂缓清单)

## 全窗总量
12 query / 37 imp / 0 click (7 天) — 悬崖 Day-10, 日均 5.3 imp (8/17 基线 374 的 1.4%)
