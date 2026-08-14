# GSC 挖矿内容队列 (选题引擎 v8, 2026-08-07 启动)

> 由 weekly-report (周日) + daily-content (每日) 追加; daily-content Step 0 消费。
> 规则: 展示≥10 且无专页的 query → 进队列; 排期优先级 = 矩阵 P0 > 本队列高意图词 > 推排名优化。

| 日期 | query | 展示 | 排名 | 现状 | 排期 | 状态 |
|------|-------|------|------|------|------|------|
| (示例) 2026-08-09 | print price calculator | 15 | 82 | 无专页 | TBD | queue |

## 推排名清单 (有页, 排名 20-70, 做内链/FAQ/pin 强化)
| 日期 | page | 展示 | 排名 | 目标 | 动作 | 状态 |
|------|------|------|------|------|------|------|
| 2026-08-07 | /blog/print-price-ai-tools-2026/ | 23 | 70 | ≤30 | 内链+FAQ+2 pin | **DONE 8/13** (T6: 对比表+引用链3+内链4+Schema; T+7 8/21) |

| 2026-08-08 | ai print estimator | 13 | 73.8 | No dedicated page | TBD (weekly-review) | queue |
---
## 2026-08-09 weekly-report 更新 (cron 首跑基线)

- GSC 凭证缺失 (gsc-oauth.json 不存在, 本地无 gsc_data.csv) → 本轮无新 query 入 Data-Driven Queue
- print-price-ai-tools 推排名条目维持 (2026-08-07, rank 70 > 50, 已在 CONTENT_PLAN.md Boost Queue, in-progress)
- Data-Driven Queue: 无追加; 待 user 配置 GSC OAuth 后恢复数据驱动

## 2026-08-08 运行记录 (AUTOCLAW_PRIMARY)
- Step 0 IndexNow: Hermes 00:21-00:23 已完成 (commit 75c4c88) — sitemap 338 URL 修复 + 6 blog 增量推送 6/6 HTTP 200; AFFILIATE_LOG.md C2b 8/8 行已记; 本次复查无新增 URL, 不重复推送; 状态文件已同步基线。
- Step 1 mining: 数据源=③ keywords-200.csv 静态兜底 (gsc-oauth.json 缺失, gsc_data.csv 缺失); 静态表无 展示/CTR 指标 → 无 query 满足 展示≥10 且 CTR<0.05 → Data-Driven Queue 无新增。
- Step 2 boosting: 无 GSC 排名数据; /blog/print-price-ai-tools-2026/ Boost Queue 行已存在 (2026-08-07, in-progress, 8/21 目标 ≤30), 无新增登记。
- Daily brief: .hermes/logs/2026-08-08-cron.md 不存在 → 未写入 GSC Opportunities 段。
- 凭证缺口: .hermes/secrets/gsc-oauth.json 缺失 (仅 template) — 补录后解锁真实 GSC mining。

| 2026-08-08 | /kittl-vs-canva/ | 12 | 72.3 | <=40 | links+FAQ+Schema | queue |
---
## 2026-08-09 运行记录 (AUTOCLAW_PRIMARY)

- Step 0 IndexNow: 16:33 已推 (sitemap 变更后全量 339 URL, 339/339 HTTP 200, 含 +1 blog best-free-creative-fabrica-assets-this-week); 本跑复查 public/sitemap.xml hash == last_submitted_hash (1D71C1...) → 无新增, 不重复推; C2b 表已补 8/9 行。
- Step 1 mining: 数据源=② data/gsc_data.json (8/8 落盘, 427 query; gsc-oauth.json 缺失 → OAuth API 不可用)。展示≥10 共 27 query, 全部已有专页或已在队列 → **Data-Driven Queue 无新增** (幂等, 与 8/8 同源同结果)。唯一无专页词 ai print estimator (13/73.8) 已于 8/8 入队, 不重复登记。
- Step 2 boosting: 完整扫描 pos 20-70 & imp≥5 → 昨日已登记候选 (kittl-vs-canva / murf ai / manychat shopify / claid / reconvert) 维持 TBD; **新增 5 个推排名候选** (下表)。writesonic 带 site: 过滤符 query (11 imp, pos 7.0) 判定为噪音, 不登记。

| 日期 | page | 展示 | 排名 | 目标 | 动作 | 状态 |
|------|------|------|------|------|------|------|
| 2026-08-09 | /pixlr-ai-review/ | 7 | 43.3 | ≤30 | links+FAQ+Schema | queue (TBD weekly-review) |
| 2026-08-09 | /compare/printful-vs-gelato/ | 10 (5+5) | 63.2/68.4 | ≤30 | links+FAQ+Schema | queue (TBD weekly-review) |
| 2026-08-09 | /descript-review/ | 5 | 67.4 | ≤40 | links+FAQ+Schema | queue (TBD weekly-review) |
| 2026-08-09 | /pika-labs-review/ | 9 | 69.2 | ≤40 | links+FAQ+Schema | queue (TBD weekly-review) |
| 2026-08-09 | /redbubble-review/ | 8 | 69.2 | ≤40 | 信任型 FAQ≥5+引用链 | queue (TBD weekly-review) |

## 2026-08-13 运行记录 (daily-search)
- 数据源: data/gsc_data.json (8/8 落盘, 427 query; gsc-oauth.json 仍缺失 → OAuth API 不可用, 数据窗口 6/28-8/5 未更新)
- 幂等检查: 全部 27 个展示≥10 query 已映射; 唯一新增无专页词 = **copywriting ai** (11 imp / 0 clk / pos 89.91, 无专页) → 入 Data-Driven Queue
- 推排名清单: 无新候选 (pos 20-70 扫描与 8/9 同源同结果); **print-price-ai-tools-2026 行 → DONE (8/13 T6 执行, T+7 对比 8/21)**
- 噪音排除: writesonic site: 过滤符 query (11 imp / pos 7) 不登记 (与 8/9 一致)
- T3 补执行记录: is-magicdrop-legit (8/11 排期因 cron 凭证故障错过, 8/13 补执行, 引用链+内链4+dateModified)

| 2026-08-13 | copywriting ai | 11 | 89.91 | 无专页 | TBD (weekly-review) | queue |

## 2026-08-14 weekly-review 更新 (T+7 读数日)
- GSC API 实时窗口 (8/7-8/13, T+2 → 至 8/11): 展示≥10 无专页 query = **0** → Data-Driven Queue 无新增
- 新 query 观察: copywriting ai (4 imp/90.5, 已入队 8/13 不重复); best ai tools for editing ecommerce photos 2026 (6 imp/88.3, 有页 /best/ai-tools-for-ecommerce-photos/, 标题对齐机会); gearlaunch (4 imp/33.3, 有页, 内链强化候选)
- 推排名清单: print-price DONE 8/13 维持; 新增候选待 8/16 快修评估: copy ai review (-7.5) / printful alternatives (微降 -1.0)

## 2026-08-14 daily-search 运行记录 (数据源升级 ① GSC API 实时)

- **数据源**: GSC API 实时 (gsc-oauth.json 有效, SOCKS5 拉取成功) — 28d 窗口 7/17-8/13 共 608 query; 取代陈旧 data/gsc_data.json (8/8 落盘), DATA_STALE 解除
- **幂等检查 (imp≥10 共 43 条)**: 全部已有专页或已在队列 → **Data-Driven Queue 无新增** (与 8/14 weekly-review 结论一致)
- **观察 (低于门槛)**: copymatic review (6 imp / pos 69.3 / 无专页) — 28d 未达 10 imp 门槛 → watchlist, 若升 ≥10 即入队
- **推排名清单 (pos 20-70)**: 无新候选; 已登记候选全部维持; 新增观察: gearlaunch (5 imp / pos 33.8, 有页 /gear-launch-review-2026/, 内链强化候选)
- **噪音排除**: writesonic site: 过滤符 query (11 imp / pos 7) 不登记 (与 8/9 一致)
- **备注**: runwayml (26 imp/71.6) + descript.com reviews (17 imp/68.8) 均已有专页 (runway-ml-review / descript-review) — 非无专页词, 标题对齐机会归 8/16 B 类快修

## 2026-08-15 daily-search 运行记录 (GSC API 实时 + T+2 并入)

- **数据源**: ① GSC API 实时 (gsc-oauth.json 有效) — 28d 窗口 7/18-8/14 共 250 query (rowLimit) + 7d 97 页 + 28d 117 页; **T+2 并入达成**: 7d 窗口 8/8-8/14 已含 8/12-8/13 (T+7 首读缺失段)
- **幂等检查 (imp>=10 共 17 条)**: 全部已有专页或已在队列 → **Data-Driven Queue 无新增**
- **观察**: ai print estimator (18 imp/74.7, 8/8 起 13→18 上升, 队列已有) / copywriting ai (17 imp/89.7, 队列已有) / **变体并入: ai copywriting (11 imp/92.9) 与 copywriting ai 同意图 → 并入既有队列行, 不重复登记**
- **推排名清单 (pos 20-70)**: 无新候选; **gear-launch-review-2026 (7d 19 imp/pos 38, 28d 起量) — B类快修 (8/14 f4f5c64) 后上升, 观察维持**
- **噪音排除**: writesonic site: 过滤符 (11 imp/pos 7) 不登记 (与 8/9-8/14 一致); jasper 系 3 变体 (jasper ai review 109 / jasper review 20 / jasper reviews 17) 全映射 /jasper-ai-review/
- **备注**: descript.com reviews (18 imp/68.9) 有专页, 标题对齐归 8/16 B 类快修候选维持; watchlist copymatic review 未达门槛
