# legit-check 产线队列 (T3, 2026-08-17 建立)

> 依据: STRATEGY-2026-08-17 战线 B (Legit-Check 内容产线) / GSC 已有 imp 排序 / 事实核实红线: Trustpilot 评分必须带真实来源 URL, 无公开数据不入列
> 模板: .hermes/drafts/legit-template.md (复用辐条②结构 + Trustpilot 段落模板)
> 产能: 2 篇/日, Hermes 草稿 → 事实核实 → AutoClaw 上线; 铁律: 宁精勿滥

| # | 工具 | GSC 信号 (imp, STRATEGY 8/17) | 现状 | 状态 | 幂等键 |
|---|---|---|---|---|---|
| 1 | MagicDrop | 120+ imp 簇 (is magicdrop legit 82 / magicdrop trustpilot 13 / free money 3) | 8/17 扩写完成: Trustpilot 专章 + 3 个 FAQ 变体 + gear-launch 互链 + 3,132 词 | DONE 8/17 | 扩写已部署 (commit 见 daily-search) |
| 2 | GearLaunch | is gearlaunch legit 29 / gearlaunch.com legit 46 | gear-launch-review-2026 已有真实点击 (8/13 摩洛哥首点击); legit 独立页待产 | queue | 页面存在→扩写路线 |
| 3 | Spocket | is spocket legit 74 | 有 spocket 评测页, legit 深化待产 | queue | 页面存在→扩写路线 |
| 4 | Kittl | is kittl legit 67 / is kittl worth it 73 | 有 kittl-review (Boost 页), legit 深化待产 | queue | 页面存在→扩写路线 |
| 5 | Society6 | society6 legit 59 | 无 legit 专页 | queue | 无专页→新建 |
| 6 | TeePublic | teepublic legit 66 | 无 legit 专页 | queue | 无专页→新建 |
| 7 | Redbubble | is redbubble legit 67 (与 society6 同簇) | 无 legit 专页 | queue | 无专页→新建 |
| 8 | Gelato | is gelato worth it 26 | 有 gelato 评测页, legit 深化待产 | queue | 页面存在→扩写路线 |
| 9 | PosterMyWall | is postermywall safe 63.5 | 无 legit 专页 | queue | 无专页→新建 |
| 10 | Veed | is veed io safe 80 | 无 legit 专页 | queue | 无专页→新建 |

## 产线规则 (沿用 Blog 军规)
- 字数 ≥2,500 / 实测语气 / 截图 3-5 张 / FAQPage schema (覆盖 GSC 变体 query: legit / trustpilot / safe / worth it / free money)
- Trustpilot/BBB/Reddit 数据必须引用真实来源 URL; 无公开数据的工具不入列 (禁止编造评分)
- 每个 legit 页配 1-2 个联盟替代品 CTA (UTM 规范) + 与既有 review 页互链
- 核心更新滚动期纪律: 只加内容不改模板结构

## 下一步 (8/18-8/19 窗口)
- 8/18: GearLaunch legit 扩写 (有真实点击背书, 优先级最高)
- 8/19: Spocket legit 扩写 (74 imp 簇)
- 每篇上线前跑事实核实 (web_search Trustpilot/BBB/Reddit)
