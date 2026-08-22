# rank-sentinel 2026-08-22

- date: 2026-08-22 18:2x CST
- window: 2026-08-15..2026-08-21 (滚动, 与 8/21 快照窗口 8/14..8/20 比较; 同口径滚动 1 日)
- status: PIPELINE-OK (正式每日拉取第 7 天; GSC API 直连 200, SOCKS5 代理 OK, PyJWT+cryptography 依赖 8/22 补装)
- alerts: 1 (负向)

## ALERT (变动 >=5 位)

1. **print price ai tool 62.75 -> 71.92 (下滑 9.17 位, imps 8->13)** — 负向 RANK-ALERT. 与 8/21 部署的方案 A (title/H1 -> Print Price Calculator) 时间重叠, 首次触及回滚阀值 (>5 位). 处置建议: 单窗口低量 (13 imp) 存噪音可能, 8/23-8/24 连续窗口确认; 若持续 >=5 位下跌 -> 按 t14-verdict 风险控制回滚 H1 (8/28 T+7 复读节点前 由 daily-search/K3 判定, 本日志如实上报).

## 其他变动 (无告警)

- is magicdrop legit 12.93 -> 13.50 (-0.57, imps 40->16 掉量观察; 页级 24 imp pos 14.21, 仍历史最佳区间)
- manychat shopify 86.29 -> 89.88 (-3.59, 观察)
- printful alternatives 77.85 -> 78.00 (-0.15)
- printify alternatives 85.67 -> 85.60 (+0.07)
- jasper ai review 90.32 -> 90.00 (+0.32)
- midjourney review 85.25 -> 84.33 (+0.92)
- omnisend review 86.50 -> 86.44 (+0.06)
- bluehost review 2026 67.56 -> 67.43 (+0.13)
- descript.com reviews 72.00 -> 71.33 (+0.67)
- kittl review / printful vs printify / runway ml: 今日窗口 0 展示 (低量噪音)
- 零展示目标词 (canva vs kittl / kittl vs placeit / halloween x3 / best ai background remover / siteground / copywriting ai): 持续无数据, 属正常

## Boost T+14 严格复读支持数据 (8/15..8/21 窗口, 供 19:23 daily-search T2)

- #1 stickermule-review: 页级 39 imp pos 53.59; 主词 sticker mule review 本窗口 0 imp (NODATA, 低量波动) — Branch B 复核数据
- #2 runway-ml-review: 页级 28 imp pos 70.86; 主词 runway ml review NODATA x4 连续 (8/18..8/21 窗口仅 12 query 有展示) — 按判定书走 Branch C 路径 (重爬请求 + 锚文本核查)
- #3 blog/is-magicdrop-legit/: 页级 24 imp pos 14.21 — Branch A 维持
- #4 blog/print-price-ai-tools-2026/: 页级 2 imp pos 5.5 (噪音); 主词 print price ai tool 71.92 (⚠️ 见 ALERT)
- #5 midjourney-review: 页级 28 imp pos 78.5 (基线 84.6, 改善 +6.1) — 8/24 T+7 前观察
- #6 jasper-ai-review: 页级 72 imp pos 83.56 (基线 91.5, 改善 +7.9) — 8/24 T+7 前观察

## HITS

- 命中 10/20 (其余 10 词零展示属正常; 全站 query 数 8/18 起骤降 321->12, 见 daily-ops 展示悬崖节)

## 数据备注

- 全站展示 8/18 起 -92% 悬崖 (8/15-8/17 日均 447 -> 8/18-8/20 日均 30) — 哨兵位置未变而总量崩塌, 指向索引/覆盖层问题而非排名问题, 详见 daily-ops-2026-08-22.md P0 节
