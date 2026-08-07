# aitoptools weekly-report 模板 (2026-08-08 K3 拍板固定四块)

> 用途: 每周日 weekly-report 执行时照本模板填写。四块必须全部出现, 不得删减。
> 原则: 数据优先 (GSC 实数), 结论一句话, 对动作可执行。

# 周报 … 2026-08-09 (Week …)

## 块 1 • GSC top queries
| query | 展示 | 点击 | CTR | 排名 | 变动 vs 上周 | 是否有专页 | 进队列? |
|---|---|---|---|---|---|---|---|
| (top 10 by 展示, ≥5 展示才记) | | | | | | | |

## 块 2 • CTR 榜 (来源×商户组合)
| 页面 | 商户 | 点击 | 展示 | CTR | 上周 CTR | 动作 (杀/加/提权) |
|---|---|---|---|---|---|---|
| (affiliate_click 事件 GA4 + 各联盟后台数据) | | | | | | |

## 块 3 • 联盟状态
| 平台 | 状态 | 本周变动 | 下周动作 |
|---|---|---|---|
| Printful / Printify / Claid / Mockey / Kittl / Placeit / Creative Fabrica / 其他 | | | |

## 块 4 • user 手工清单 (≤3 条)
1. …… (2 分钟)
2. ……
3. ……

---
## 附: 输出规则
- 发送地: 周报落盘 .hermes/logs/weekly-report-YYYY-MM-DD.md + 给 K3 一句话摘要
- GSC 数据来源: 本周 gsc_data.csv / GSC API; 凭证缺失时填 "blocked_missing_credentials"
- 块 4 不超过 3 条, 每条带时长; 不够重要的不写
- 输出后更新 gsc-mining-queue.md (展示≥10 无专页 → 进队列)
