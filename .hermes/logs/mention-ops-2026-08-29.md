# 站外提及运营日志 — 2026-08-29 (mention-ops)

> 执行: 手动触发 (webchat "执行", 04:51) | 依据: PLAN-2026-09 §三-修订2/§六
> 核心依据: 站外品牌提及相关性 0.664 vs 外链 0.218 (~3倍) — 升级为与外链并列的 GEO 主引擎
> 战略聚焦 (2026-08-24 千问指令 #3): 停止低质目录站提交; 全力聚焦 Reddit/Quora 种子帖质量 (真实人类口吻、自然讨论、品牌提及优先于链接); 即使不带链接也目标让 "aitoptools {tool}" 可被搜索到 (信任分)

## Step 1 收录状态核查
台账: .hermes/logs/backlink-ledger.md (口径 v2: 收录数, 8/19 起) + link-building-0816/0823.md

| # | 站点 | 提交日 | 状态 | 收录证据 | 复核日 |
|---|------|--------|------|----------|--------|
| 1 | Wired Business (wired.business) | 8/15 | **LIVE** | badge 验证通过 (8/17 06:41 autoglm) | 8/17 |
| 2 | TheNextAI | 8/16 | SUBMITTED | 审核中 (24-48h 承诺) | 待核 |
| 3 | AI Toolz Dir (aitoolzdir.com) | 8/16 | SUBMITTED | footer 回链 8/16 live; 收录 API 无法核 | 待核 |

**站外提及复核 (8/29 web_search "aitoptools.net" review OR mention OR list)**: **0 结果** — aitoptools.net 在已索引 web 站外提及为真空。品牌提及信任分建设 (Reddit/Quora 种子) 是当前唯一在途增量路径, 发布动作全在 user 侧。
**发布回填检查**: 队列完成记录无 PUBLISHED 标记 (seed-01~05 仍待 user 发布)。

**站外提及 + 外链收录计数 (KPI 口径)**: LIVE = 1 (Wired Business)
**KPI 偏差**: 9/13 目标 ≥5 → 当前 1 → 偏差 = |1-5|/5 = **80% > 20%** → 🔴 **标红** (PLAN-2026-09 §六: 若 9/13 站外收录 <3, 12 月目标自动下调一档)

## Step 2 下一批候选调研
- 队列 9 选题已饱和 (覆盖 legit-queue 全部可链页面); 本次无可新增候选
- TeePublic 数据复验 (8/29): Trustpilot 官方页 4.4/5 · 640,587 条 (8/20 核) 与官方自述 4.5/5 · 375k+ 条 口径接近, 取区间写法 "4.4-4.5/5, 数十万条" — 避免精确数漂移争议
- Veed: veed-review 仍未在 sitemap (8/29 复查), 维持 ⚠️
- 目录站: 维持停止新增 (战略聚焦 #3)

## Step 3 种子草稿 (本次产出)

- .hermes/drafts/reddit-seed-06.md — **Is TeePublic legit?** (约 410 词, 目标 r/printondemand / r/artbusiness / Quora)
- 链接目标: https://aitoptools.net/teepublic-review/ (sitemap 已上线 ✅)
- 数据 (全部带来源): TP 4.4-4.5/5 数十万条 (8/20 核 + 官方页 8/29 复核) + trendlytic 2026-06 (legit/真实退款) + 站内实测 3.8/5 (2025 佣金重构 10% / 仅服饰配件 / AI 竞争激烈 / SEO 强)
- 角度: 买家问题与卖家问题分离作答 — 买家 "非常 legit" (大样本好评), 卖家 "数学要算清" (10% 基础佣金 + 品类窄 + AI 竞争), 定位 "upload and forget 附加渠道"; 附买家省钱 tip (site-wide sale 半价)
- 纪律遵守: 真实问题开头 / 单链接自然语境 / 不吹嘘不编造 (评分取区间 + 标注两个口径)
- 发布: 交 user 行动卡 (不自动发布, 铁律)
- 待 user 发布存货累计: seed-01 (GearLaunch) + seed-02 (Spocket) + seed-03 (Kittl) + seed-04 (Society6) + seed-05 (MagicDrop) + seed-06 (TeePublic) — **6 条积压**

## KPI 偏差汇总
- 站外提及+收录: 目标 9/13 ≥5, 当前 1 → **偏差 80% 标红 🔴**
- 处置: 种子存货 6 条, 产能持续领先于发布动作; **继续加产边际价值递减, 建议 user 集中执行发布**; 下次触发优先核对回填而非新增草稿
- 收录目标实现依赖: user 发布 6 条种子帖 + autoglm credits 恢复后补交目录等待队列

## user 动作清单 (≥)
1. **发布积压 6 条种子帖** (seed-01 GearLaunch / seed-02 Spocket / seed-03 Kittl / seed-04 Society6 / seed-05 MagicDrop / seed-06 TeePublic) — 个人账号, 分 2-4 天分批, 单帖一次, 遵循各 sub 规则
2. autoglm credits 恢复后, 提交待浏览器队列 (insidr.ai / productcool.com / findly.tools / toolpilot.ai) — 目录收录 +2-4 潜在
3. 知悉 KPI 偏差 80% 标红: 若 9/13 前收录 <3, 12 月目标自动下调一档 (PLAN-2026-09 §六敏感性)

## 下一步 (下周三 20:17 或下次触发)
- **优先**: 核对 seed-01~06 发布回填 (标 PUBLISHED) — 若零回填, 升级 user 发布阻塞而非继续产草稿
- 剩余可写: Redbubble (seed-07, factcheck 8/20 已备) / PosterMyWall (factcheck 8/22) / Gelato (factcheck 8/20)
- Veed 页上线后转可写 (80 imp)
- 若 autoglm 恢复: 启动目录浏览器提交 (insidr.ai + productcool.com)
