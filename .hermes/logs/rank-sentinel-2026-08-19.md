# Rank Sentinel — 2026-08-19 (第 6 天, 补 8/18 缺口)

> 窗口: 2026-08-12..2026-08-18 (GSC T+1 滚动) | 比较基准: 8/17 快照 (8/10..8/16) | 同轮重拉 8/10..8/16 捕获修订

## 结果: 1 ALERT (正向)

### ⚠️ RANK-ALERT: is magicdrop legit 31.1 → 26.0 (改善 5.2 位)
- **方向: 正向改善** — 20q 历史最佳排名 (连续 6 次改善: 55.1→42.9→34.2→33.6→31.1→26.0)
- imps 76→82 (展示增长); 8/17 快照同窗口修订 31.1→28.5 (GSC 修订亦确认改善方向)
- 处置: 维持观察 — 与 legit 簇内容 (is-gearlaunch-legit 等 8/18-19 上线) 及 STRATEGY T2 legit pilot 一致; 无修复项, 无 PUSH_READY

## 主要变动 (今日窗口 vs 8/17 快照)

| query | 旧 pos | 新 pos | diff | imps | 备注 |
|---|---|---|---|---|---|
| is magicdrop legit | 31.1 | 26.0 | -5.2 | 76→82 | 🔥 历史最佳, ALERT 正向 |
| kittl review | 63.0 | 59.0 | -4.0 | 2→1 | 改善, 连续 5 日稳定后新低 (低量) |
| printify alternatives | 81.3 | 85.4 | +4.1 | 7→7 | 下跌接近阈值, 低量噪音观察 |
| printful vs printify | 82.3 | 84.0 | +1.7 | 3→1 | 低量 |
| bluehost review 2026 | 67.5 | 68.5 | +1.0 | 10→11 | 稳定 |
| printful alternatives | 77.2 | 78.0 | +0.8 | 17→17 | 稳定 |
| descript.com reviews | 72.0 | 72.6 | +0.6 | 6→5 | 稳定 |
| omnisend review | 85.8 | 86.2 | +0.4 | 21→19 | 稳定 |
| manychat shopify | 82.3 | 82.1 | -0.2 | 19→18 | 稳定 |
| midjourney review | 86.9 | 86.2 | -0.7 | 17→14 | 改善 |
| jasper ai review | 91.5 | 91.5 | 0 | 43→42 | 稳定 |

## 无数据 (9/20, 零展示窗口)

canva vs kittl / kittl vs placeit / halloween print on demand / halloween shirt design / halloween sublimation / runway ml / best ai background remover / siteground review 2026 / copywriting ai

## 数据修订 (同窗口 8/10..8/16 重拉 vs 8/17 快照)

- is magicdrop legit: 31.1 → 28.5 (修订改善, 佐证 ALERT 方向)
- printify alternatives: 81.3 → 83.0 (修订下跌 1.7, 结合今日 85.4 需观察)

## 附注

- 8/18 daily-ops 未运行 (cron 缺口), 本次为 2 天合并窗口比较; 8/17→8/18 中间日无独立快照
- 窗口拉取: GSC API via gsc-oauth.json + SOCKS5 (372 rows); 修订窗口 478 rows
- 日志: .hermes/logs/rank-sentinel-2026-08-19.md; JSON 快照数 7→8