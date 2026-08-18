# GEO 基线表（2026-08-13 建立）

> 目的: K3 战略轨道二（GEO）基线——记录 20 核心 query 在 AI 引擎的引用状态，8/19 首读 + 每月复查对比
> 方法: 人工/浏览器查询 AI 引擎（ChatGPT/Perplexity/Google AI Overview）→ 记录是否提及 aitoptools.net
> 当前状态: 基线建立日，AI 引用 = 待测（无 API 密钥，走浏览器手动/autoglm 查询）

## 20 核心 query 基线

| # | query | GSC pos(8/5-12) | 展示 | AI 引用状态 | 备注 |
|---|---|---|---|---|---|
| 1 | printful alternatives | 72.6 | 55 | ⏳ 待测 | 变现核心页 |
| 2 | printify alternatives | 81.0 | 29 | ⏳ 待测 | 变现核心页 |
| 3 | printful vs printify | 77.6 | 82 | ⏳ 待测 | 最高展示对比页 |
| 4 | canva vs kittl | 72.3 | 27 | ⏳ 待测 | Kittl 系 |
| 5 | kittl review | — | 2 | ⏳ 待测 | Kittl 系 |
| 6 | kittl vs placeit | 39.5 | 2 | ⏳ 待测 | Kittl 系 |
| 7-9 | halloween 三词 | NODATA | 0 | ⏳ 待测 | 季节词 8/25 上线后入列 |
| 10-20 | jasper ai review / midjourney review / magicdrop / omnisend / manychat shopify / runway ml / best ai background remover / bluehost 2026 / descript / siteground 2026 / copywriting ai | 62-97 | 9-37 | ⏳ 待测 | GSC 高展示 12 词 |

## 待办
- [ ] 8/19 GEO 首读 cron: 用 autoglm 浏览器查询上述 query（ChatGPT/Perplexity），记录引用状态 → 填表
- [ ] 每月复查: 9/13 T+30 校准同步复查

## 方法说明
- AI 引擎无公开 API 密钥（ChatGPT/Perplexity 需登录/付费）→ 浏览器查询为基线方法
- Google AI Overview 结果随搜索可查（无登录）
- 判定标准: 结果中是否出现 aitoptools.net URL 或品牌名

## 8/19 首读结果 (2026-08-19 cron 追加)
> GSC 位移 (base 8/4-9 vs cur 8/10-16) 见 .hermes/logs/geo-0819.md; AI 引擎引用状态本次 NODATA (browser 工具未就位 / D7 缺失)
> AI 引荐流量 (beacon 7d) = NODATA (D7 CF token 缺失 ≥3 天, 已升级 user)

| # | query | GSC pos(8/19 cur) | 8/19 位移 | AI 引用状态 (8/19) |
|---|---|---|---|---|
| 1 | printful alternatives | 77.4 | +1.8 (样本小) | NODATA (待测) |
| 2 | printify alternatives | 83.0 | -- (仅 cur) | NODATA (待测) |
| 3 | printful vs printify | 82.3 | 微升 (84.5→82.3) | NODATA (待测) |
| 4 | canva vs kittl | 72.0 | -- | NODATA (待测) |
| 5 | kittl review | 63.0 | 样本小 | NODATA (待测) |
| 6 | kittl vs placeit | NODATA | 不在 cur 窗口 | NODATA (待测) |
| 7-9 | halloween 三词 | NODATA | 未入列 (8/25 上线) | NODATA (待测) |
| 10 | jasper ai review | 91.4 | 位置未提升 (imp 44→59) | NODATA (待测) |
| 11 | midjourney review | 86.2 | -- (imp 42→21) | NODATA (待测) |
| 12 | magicdrop | NODATA | 见 is magicdrop legit (-35) | NODATA (待测) |
| 13 | omnisend | 62.0 | -- | NODATA (待测) |
| 14 | manychat shopify | 82.7 | 微升 (84.9→82.7) | NODATA (待测) |
| 15 | runway ml | NODATA | 不在 cur 窗口 | NODATA (待测) |
| 16 | best ai background remover | NODATA | -- | NODATA (待测) |
| 17 | bluehost 2026 | NODATA | -- | NODATA (待测) |
| 18 | descript | 55.0 | -- | NODATA (待测) |
| 19 | siteground 2026 | NODATA | -- | NODATA (待测) |
| 20 | copywriting ai | NODATA | -- | NODATA (待测) |

**GEO 决策 (8/19)**: 维持投入 (保守) — GSC 位移正面 (is magicdrop legit -35 / magicdrop legit -25.9 / stickermule 簇 -23~-24) + GEO 技术层 (robots/llms) LIVE 低维护;
AI 引荐流量 NODATA 无法触发降级 (需 =0 硬证据); D7 缺失 ≥3 天 → 升级 user 补凭证; 8/21 T+14 合并复核定级。
