# rank-sentinel 2026-08-24

- date: 2026-08-24 01:5x CST
- window: 2026-08-17..2026-08-23 (滚动, 与 8/23 快照窗口 8/16..8/22 比较)
- status: PIPELINE-OK (第 9 天; GSC API 200, SOCKS5 OK; 输出经 node 转 UTF-8 落盘)
- alerts: 0 新增 (悬崖期 20q 仅 2 命中); print price NODATA -> T2 Day-2 回滚执行顺延

## ALERT (变动 >=5 位)

- **无新 RANK-ALERT** — 仅 2 query 有展示且均改善: bluehost review 2026 66.75->65.0 (+1.75) / descript.com reviews 71.0->70.0 (+1.0)

## 悬崖期哨兵读数 (窗口 8/17..8/23)

- **20q 命中 2/20** (昨日 10/20) — 悬崖持续且哨兵池内加深; 全站 40 query 有展示 (imp 均 1-5), 日均展示仍处悬崖低位
- 其余 18 query NODATA (含 magicdrop: 13.40 连续 6 窗有数据后今日 0 imps — 悬崖覆盖所有有量词)
- 新低量信号: creative fabrica imp5 pos50.4 / design pickle review imp4 pos49.5 / design pickle reviews imp4 pos56.5 (Boost #7 候选词初现)

## T2 print-price Day-2 (回滚确认窗)

| 窗口 | 主词 print price ai tool | Δ vs 基线 62.75 |
|---|---|---|
| 8/14-20 (8/21 读) | 62.75 @8 | 基线 (方案 A 部署前) |
| 8/15-21 (8/22 复读) | 71.92 @13 | -9.17 |
| 8/16-22 (8/23 Day-1) | 72.92 @12 | -10.17 |
| 8/17-23 (8/24 Day-2) | **NODATA (0 imps)** | 无法比较 |

- **Day-2 结论: 无法确认, 回滚顺延** — 悬崖期 (Branch B 判定, 滚动期至 9/6) 数据整体不可信, 且主词 0 imps 无位置可比较
- 处置: 不执行回滚 (无恐慌性改版纪律); 8/25 窗口复读: imps 恢复且 pos<67.75 -> 预案作废; pos 仍 >=67.75 -> 执行回滚 (预案 .hermes/drafts/print-price-revert-0823.md)
- 最终对照点: 8/28 T+7 复读 (daily-search/K3)

## Boost 支持数据 (窗口 8/17..8/23)

- #1 stickermule-review NODATA / #2 runway NODATA x6 / #3 magicdrop NODATA (悬崖) / #4 print price NODATA (T2 顺延) / #5 midjourney NODATA / #6 jasper NODATA
- design pickle (Boost #7 候选) 双词 8 imps 首次进入哨兵视野 — 悬崖期仍稳定的新词, 8/25 后持续观察
