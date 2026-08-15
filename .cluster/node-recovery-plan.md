# 节点恢复预案（2026-08-14 建立）

> 用途: 每日任务数据就绪 + 用户明确指令后，按本预案逐个重建一次性节点 cron
> 触发条件: daily-ops-0814.md / rank-sentinel-0814.md / daily-search-0814.md / weekly-0814.md 落盘
> 原则: 串行恢复（前序产物是后序输入），每个节点 deleteAfterRun=true，时间避开高峰

## 依赖链与恢复顺序

| 顺序 | 节点 | 依赖数据 | 核心任务 | 时间槽 |
|---|---|---|---|---|
| 1 | 8/14 T+7 首读 + kittl 诊断 | 哨兵 20q 位置 + GSC 覆盖至 8/13 | 四分支决策树；SERP 诊断 → kittl-diagnosis-0814.md | 07:15 |
| 2 | 8/16 B 类快修 | T+7 诊断产物 + bfix-plan + 扩写队列 | 79 页 title/meta + 扩写 Top10 + kittl 重写 + 外链首批 8 站 + push | 07:15 |
| 3 | 8/17 Boost #5-6 | 8/16 产物（reviews.json 状态） | midjourney/jasper 信任型补强 + IndexNow | 08:41 |
| 4 | 8/19 GEO 首读 | beacon 7 天（8/12 上线→8/19 满） | CF 引荐流量 + GEO 基线表 20 query 消费 | 07:15 |
| 5 | 8/23 集群合并 | 8/18 Halloween 判定 + 扩写队列剩余 | 集群页 + 内链 53→200+ + E-E-A-T + 外链第 2 批 + push | 07:15 |
| 6 | 8/25 万圣节全量 | 8/23 产物 + Kittl 素材 | 全量检查 + Kittl 联动 UTM + GEO 三词 + push | 07:15 |
| 7 | 8/31 IndexNow 全推 | sitemap 全量 | 增量推送 + 核验 + 月末收口 | 07:15 |
| 8 | 9/13 T+30 校准 | 30 天全量数据 + K3 KPI | 三源汇总 + KPI 六项 + Kittl 假设替换 + Phase 3 产出 | 07:15 |

## 时间换算（Asia/Shanghai → UTC）
- 07:15 = 前日 23:15Z
- 08:41 = 当日 00:41Z

## 每节点消息要点（重建时使用）
1. 路径铁律: cd /d F:\aitoptools；写文件用 exec node/python 禁 write 工具；禁读写 F:\zprintpro-nextjs
2. fallbacks: deepseek__4111173b... / deepseek__840d2872...
3. 幂等: 产物已存在（git log/文件检查）→ NOOP
4. 输出中文；产物路径固定（见各节点消息原文，历史 add 记录可查）

## 状态记录
- 2026-08-14 05:33: 8 节点全部停用待命；4 每日任务运行中（无 8/14 产物）
- 恢复后每节点勾选 + 记录实际时间/结果
