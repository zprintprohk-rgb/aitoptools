# Rank Sentinel — 2026-08-12 (首次每日拉取, 管线打通日)

> 协议: PHASE-2026-08-13 三.1 (8/13 起每日, 本次为预跑打通) · 复用 scripts/gsc_query.py 模式 (gsc-oauth.json + SOCKS5 127.0.0.1:7892)

## 拉取信息
- **窗口**: 2026-08-05..2026-08-11 (与 baseline 同窗口比较 — GSC 数据 T+1, 8/12 可查最新完整数据即 8/11)
- **GSC rows**: 303
- **覆盖**: 20/20 query 全部命中 (含 4 个零展示 query: kittl vs placeit / halloween 三词)

## 结果: 0 ALERT ✅
- 全部 20 query 位置与 baseline (8/12 10:14 建立) **完全一致** — 同一覆盖窗口, 数据已定稿, 无变动属预期
- 无任何 query 位置变动 ≥5 位

## 当前位置快照 (下一轮比较基准)
| query | pos | imps |
|---|---|---|
| printful alternatives | 75.6 | 15 |
| printify alternatives | 81.9 | 7 |
| canva vs kittl | 70.0 | 4 |
| kittl review | 68.5 | 2 |
| jasper ai review | 89.9 | 37 |
| midjourney review | 86.4 | 35 |
| is magicdrop legit | 62.7 | 23 |
| omnisend review | 84.8 | 20 |
| manychat shopify | 84.7 | 15 |
| printful vs printify | 79.8 | 11 |
| runway ml | 69.1 | 11 |
| best ai background remover | 96.9 | 10 |
| bluehost review 2026 | 65.6 | 10 |
| descript.com reviews | 68.8 | 10 |
| siteground review 2026 | 82.3 | 10 |
| copywriting ai | 88.0 | 9 |
| kittl vs placeit | null | 0 |
| halloween print on demand | null | 0 |
| halloween shirt design | null | 0 |
| halloween sublimation | null | 0 |

## 备注
- 4 个零展示 query (kittl vs placeit + halloween 三词) 是 8/13 起 W1 内链 Boost + Halloween 集群的目标词, 上线前无数据属正常
- **明日 (8/13) 起正式每日拉取**: 窗口滚动 (8/6..8/12), 与本次快照比较, ≥5 位变动置顶告警
- 8/14 T+7 决策树读数与哨兵日数据互相印证
