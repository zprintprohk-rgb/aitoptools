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
