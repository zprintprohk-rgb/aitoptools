# 排名冲刺期台账 (2026-08-12 启动准备版)

> 上游: PHASE-2026-08-13-09-13.md（commit a5f4436）· 本台账为执行层启动记录

## 一、北极星基线（已写入，后续环比以此为准）
- GSC API 实测（8/4-8/9 六天）: 展示 152/230/212/182/134/273（合计 1183，**日均约 197**）/ 点击 0 / CTR 0 / 均 pos 59-71
- 佣金: $0（联盟矩阵 7 活跃 + Kittl 20%×12mo 已激活，尚无转化）
- 数据源: scripts/gsc_query.py（gsc-oauth.json + SOCKS5 127.0.0.1:7892，8/12 验证链路可用）

## 二、排名哨兵（20 核心 query，8/12 启动）
- 配置: `.hermes/logs/rank-sentinel-20q.json`（基线窗口 2026-08-05..08-11）
- 构成: 变现页 2（printful/printify alternatives 组，聚合 15/7 展示）+ Kittl 系 3（canva vs kittl 4、kittl review 2、kittl vs placeit NODATA）+ 季节 3（halloween 词 NODATA）+ GSC 高展示 12
- 高展示 top12: jasper ai review 37 (pos 89.9) / midjourney review 35 (86.4) / is magicdrop legit 23 (62.7) / omnisend review 20 (84.8) / manychat shopify 15 (84.7) / printful vs printify 11 (79.8) / runway ml 11 (69.1) / best ai background remover 10 (96.9) / bluehost review 2026 10 (65.6) / descript.com reviews 10 (68.8) / siteground review 2026 10 (82.3) / copywriting ai 9 (88.0)
- 告警逻辑: 单日变动 ≥5 位 → RESULT 置顶 ⚠️ RANK-ALERT（已入 daily-ops Step 0b）

## 三、四周排期 → 日历（8 个一次性 cron 已建，deleteAfterRun）
| 节点 | cron 名 | 时间 |
|---|---|---|
| 8/13 | W1-0813 变现页+Kittl内链Boost | 09:00 |
| 8/14 | W1-0814 T+7首读数决策 | 09:00 |
| 8/16 | W1-0816 B类快修push | 09:00 |
| 8/19 | W2-0819 GEO首读数 | 09:00 |
| 8/23 | W2-0823 集群合并push | 09:00 |
| 8/25 | W3-0825 万圣节全量push | 09:00 |
| 8/31 | W3-0831 IndexNow全推 | 09:00 |
| 9/13 | W4-0913 T30全量校准 | 09:00 |
- 既有 cron: 每日联盟运营 12:17（已加 Step 0 PHASE 消费 + Step 0b 排名哨兵）/ 每日搜索增长 19:23 / 每周复盘 周日 07:47 / 季节集群执行 8/18 19:37

## 四、T13 记分卡正式版（8/12 全量，口径 v1.1 已核验）
- 台账: `.cluster/programmatic-audit-0813.md` + .html（可视化报告）+ summary.json；抽样核验: scorecard-sample-audit-0812.md（页面清单: page-inventory-0812.json）
- 口径: **333 programmatic 页** = best 199（keywords-200.csv → generate-pages.js）+ reviews 107 + comparisons 6 + listicles 4 + blog 10 + category 6（tools 9 无独立页仅喂 best；category 实为 6 类非 13）
- 分级: **A=187 / B=138 / C=16**（best 149/50/0 · review 5/88/14 · comparison 6/0/0 · listicle 4/0/0 · blog 10/0/0 · category 6/0/0 · tool 7/0/2）
- C 级 16 页: -2026 批 10 页 affiliateUrl="#" 占位符（无真实 CTA）+ dalle/removebg 标点变体 + gear-launch/packify + greenonion/picjam（pending 无 CTA）
- B 类主短板: 正文 <800 词（postermywall 75 词最短）+ 站内链接=0 → 8/16 快修靶心（C 级 16 页优先 + B 类正文扩写队列 20 页）
- 口径修正: v0→v1.1 依据抽样核验 5 根因（listicle 全文词数 / comparison toolA-toolB aff / "#" 假阳性 / 内链口径 / kw 标点宽容）

## 五、Printify 挑战规则核实（8/20 前置提前完成）
- 报告: `.hermes/logs/printify-challenge-verification-0812.md`（邮件 #495 原文规则 + #497 已提交实证 + #651 8/9 邮件）
- 结论: **ALLOWED-WITH-CONDITIONS**（$150/月 5 名；7/24-9/28；博客需月访客≥1000 当前不满足；视频需≥500 观看；不可重复提交）

## 六、启动准备验证清单
- [x] 路线图入库（a5f4436）+ daily-ops Step 0 消费已配置
- [x] 基线落台账（上表一）
- [x] 排期落日历（上表三，8 cron）
- [x] 排名哨兵启动（20 query + 首拉 + 告警逻辑）
- [x] 记分卡 v0 分级（117 页 A/B/C）
- [x] Printify 规则核实（ALLOWED-WITH-CONDITIONS）
- [ ] 8/13 Boost push（cron 待触发）
- [ ] 8/14 T+7 决策（cron 待触发）
- [ ] 8/19 GEO 决策（cron 待触发）
- [ ] 8/23/8/25/8/31/9/13 节点（cron 待触发）
