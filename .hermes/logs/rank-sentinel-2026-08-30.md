# rank-sentinel 2026-08-30 (12:17 daily-ops)

> 拉取: scripts/gsc_query.py (12:2x, SOCKS5 7892) | queries days 7 + days 3 + days 28 (归属验证) | 窗口: 7d = 8/23-8/29 (8/27-29 稀薄) | 日值有效至 8/27

## 日值 (全 query 口径)
8/19=29 | 8/20=29 | 8/21=17 | 8/22=21 | 8/23=22 | 8/24=17 | 8/25=22 | 8/26=22 | 8/27=19 (8/28-29 未出, T+2 滞后)
- 7d (8/21-8/27): 140 imp / 0 click / 日均 20.0 — 悬崖 Day-15, 无恢复; 悬崖前基线 8/2-8/5 = 152-230 imp/日

## 20q 哨兵对照
- manychat shopify 8 imp / pos 99.9 (8/29 窗 91.8, 基线 90.6) -> **⚠️ RANK-ALERT: manychat shopify 91.8 -> 99.9 (变动 -8.1 ≥ 5)**
- 处置: 低样本 (8 imp) 噪声概率高, pos 99.9 为底部边缘展示; 处置建议 = 观察 2 窗确认, 不动作, 无 PUSH_READY; 若下窗回到 <90 恢复则撤销记录
- 其余 19 query 0 命中 (窗口右移 + 滞后稀释, 与 8/29 同型)

## 观察位
- print price ai tool 11 imp / pos 85.9 (8/29: 83.3, 变动 -2.6 < 5 -> 无 alert; T+7 终判回滚对照口径维持)
- sticker mule 2 imp / pos 47.5 (8/29: 35.0, 观察位非 20q, Branch B 追踪)
- mockey 1 imp / pos 39.0 (8/29: 37.5, 观察)

## GEO 探针 (排除社媒域查询, 7d)
- adcreative.ai review pos 1.0 (1 imp) | writesonic pos 1.0 (2 imp) | b12 ai pos 3.0 (1 imp) | omnisend pos 9.5 (2 imp) | ai tools for print on demand pos 72 (3 imp)
- AI 爬虫可见性信号维持 (无点击, 深度排名期常态)

## 归属验证附注
- GSC 恭喜邮件 28 天 250 clicks 不属本项目: aitoptools.net 28d 实证 1 click (8/3), 邮件归属 zprintpro.com