# rank-sentinel 2026-08-21

- date: 2026-08-21 12:3x CST
- window: 2026-08-14..2026-08-20 (滚动, 与 8/19 快照窗口 8/12..8/18 比较; 同轮重拉昨日窗口捕获修订)
- status: PIPELINE-OK (正式每日拉取第 6 天, 8/18/8/20 无运行记录= cron 缺失日)
- alerts: 1

## ALERT (变动 >=5 位)

1. **is magicdrop legit 25.58 -> 12.93 (改善 12.7 位, imps 86->40)** — 正向大跳, 全站最佳位置突破 13 位. 处置: 无需修复, 继续观察; 18:45 已执行内链加权 (POD 集群 related 入链, commit 21ad4d2, 待 19:23 push). 与 8/19 快照 (25.95) 对比同样为大幅改善.

## 其他变动 (无告警)

- printful alternatives 78.0 -> 77.85 (+0.15 改善)
- printify alternatives 85.25 -> 85.67 (-0.42)
- jasper ai review 90.90 -> 90.32 (+0.58 改善)
- midjourney review 85.95 -> 85.25 (+0.70 改善)
- omnisend review 86.14 -> 86.50 (-0.36)
- manychat shopify 84.0 -> 86.29 (-2.29)
- bluehost review 2026 67.92 -> 67.56 (+0.37 改善)
- descript.com reviews 72.17 -> 72.00 (+0.17 改善)
- kittl review / printful vs printify / printify alternatives: 今日窗口 0 展示 (低量噪音, 无位置数据)
- 零展示目标词 (canva vs kittl / kittl vs placeit / halloween x3 / runway ml / best ai background remover / siteground / copywriting ai): 持续无数据, 属正常

## print-price 里程碑补充 (8/21 节点)

- print price ai tool: 62.33 (8/12..8/18) -> 62.75 (8/14..8/20) — 持平微跌, **里程碑 <=30 未达** (基线 65.5, T+7 ~61.5, 现 62.8). 无 RANK-ALERT, 如实记录.

## HITS

- 命中 9/20 (5 个零展示目标词 + 6 个近期低量词无数据, 属正常波动)