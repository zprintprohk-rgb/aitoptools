# Rank Sentinel - 2026-08-15

> 协议: PHASE-2026-08-13 三.1 每日拉取 · 复用 scripts/gsc_query.py 模式 (gsc-oauth.json + SOCKS5 127.0.0.1:7892)

## 拉取信息
- **窗口**: 2026-08-08..2026-08-14 (滚动, 与昨日快照 8/7..8/13 比较; 同时重拉昨日窗口捕获数据修订)
- **GSC rows**: cur=32 / prev=32
- **覆盖**: 16/20 query 命中 (4 个零展示目标词无数据属正常)

## 结果: 0 ALERT (无 >=5 位变动)

- 最大变动: runway ml 67.6->65.2 (改善 2.4) / printify alternatives 81.0->79.3 (改善 1.7) / printful vs printify 77.6->79.2 (下跌 1.6), 均 <5
- is magicdrop legit 55.5->55.1 (改善 0.4, imps 40->36) - 连续改善, T+7 分支 B 佐证
- kittl review 67.0->67.0 (连续持平, imps 1) - T14 Kittl 内链 Boost 后稳定
- GSC 数据修订观察: 昨日窗口重拉 printful alternatives 17->20 imps (pos 75.9->76.3), jasper ai review 42->51 imps (pos 90.5->90.8), is magicdrop legit 18->40 imps (pos 62.5->55.5)

## 当前位置快照 (窗口 8/8..8/14)
| query | pos | imps | prev pos | prev imps | delta |
|---|---|---|---|---|---|
| printful alternatives | 76.7 | 16 | 76.3 | 20 | +0.4 |
| printify alternatives | 79.3 | 7 | 81.0 | 12 | -1.7 |
| canva vs kittl | 72.0 | 1 | 72.0 | 1 | 0 |
| kittl review | 67.0 | 1 | 67.0 | 1 | 0 |
| kittl vs placeit | null | 0 | null | 0 | - |
| halloween print on demand | null | 0 | null | 0 | - |
| halloween shirt design | null | 0 | null | 0 | - |
| halloween sublimation | null | 0 | null | 0 | - |
| jasper ai review | 91.0 | 44 | 90.8 | 51 | +0.2 |
| midjourney review | 86.8 | 23 | 86.6 | 30 | +0.2 |
| is magicdrop legit | 55.1 | 36 | 55.5 | 40 | -0.4 |
| omnisend review | 85.1 | 22 | 85.0 | 25 | +0.1 |
| manychat shopify | 84.2 | 20 | 84.2 | 23 | 0 |
| printful vs printify | 79.2 | 9 | 77.6 | 10 | +1.6 |
| runway ml | 65.2 | 5 | 67.6 | 10 | -2.4 |
| best ai background remover | 97.6 | 5 | 97.3 | 6 | +0.3 |
| bluehost review 2026 | 66.6 | 10 | 66.5 | 12 | +0.1 |
| descript.com reviews | 70.2 | 6 | 69.6 | 11 | +0.6 |
| siteground review 2026 | 82.2 | 6 | 82.1 | 8 | +0.1 |
| copywriting ai | 90.5 | 4 | 90.5 | 4 | 0 |

## 备注
- 8/15 W1 收尾: T+7 分支 B 维持 (点击 0 但位置在改善), 无 >=10 位大跌
- 本文件为 UTF-8 重写版 (修复早前 GBK 乱码)
- 下一轮比较基准 = 本快照; 每日滚动窗口 >=5 位变动置顶告警


## 傍晚修订轮 (2026-08-15 19:1x, W1-0815 复核节点)

> 同窗口 8/8..8/14 重新拉取 (GSC T+2 数据修订后): cur rows=409 / prev rows=441

### 修订后快照对比 (傍晚 vs 早上 03:51 哨兵, 同窗口)
| query | 早上 pos | 傍晚修订 pos | delta | 说明 |
|---|---|---|---|---|
| kittl review | 67.0 (imp1) | **63.0 (imp2)** | -4.0 改善 | 修订补录 imps 1->2, 位置再改善; 连续 2 日改善确认 (67.0->63.0), T14 内链补强见效 OK |
| is magicdrop legit | 55.1 (imp36) | **42.9 (imp60)** | -12.2 改善 | 大幅修订 (imps 补录 40->60), 连续改善加速 |
| runway ml | 65.2 (imp5) | 65.2 (imp5) | 0 | 与早上一致 |
| printify alternatives | 79.3 (imp7) | 79.9 (imp8) | +0.6 | 微跌 |
| printful vs printify | 79.2 (imp9) | 79.2 (imp9) | 0 | 持平 |
| jasper ai review | 91.0 (imp44) | 91.2 (imp52) | +0.2 | 微跌 |
| printful alternatives | 76.7 (imp16) | 76.9 (imp19) | +0.2 | 微跌 |
| manychat shopify | 84.2 (imp20) | 82.6 (imp24) | -1.6 改善 | |
| 其余 9 query | -- | -- | +-0~0.6 | 全部 <1 位 |

### 结论
- **0 ALERT**: 无任何 query 下滑 >=5 位 (修订后最大下滑 +0.6 位, 全部为 GSC 数据补录修订)
- **2 正向**: kittl review 63.0 (T14 内链补强见效) + is magicdrop legit 42.9 (大幅改善)
- 大面积下滑 >=10 位: **未触发** -> Branch A 继续 (风险开关确认)
