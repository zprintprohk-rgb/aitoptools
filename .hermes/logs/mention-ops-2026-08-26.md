# 站外提及运营日志 — 2026-08-26 (mention-ops)

> 执行: cron 681966d9 (站外提及运营, 周三 20:17) | 依据: PLAN-2026-09 §三-修订2/§六
> 核心依据: 站外品牌提及相关性 0.664 vs 外链 0.218 (~3倍) — 升级为与外链并列的 GEO 主引擎
> 战略聚焦 (2026-08-24 千问指令 #3): 停止低质目录站提交; 全力聚焦 Reddit/Quora 种子帖质量 (真实人类口吻、自然讨论、品牌提及优先于链接); 即使不带链接也目标让 "aitoptools {tool}" 可被搜索到 (信任分)

## Step 1 收录状态核查
台账: .hermes/logs/backlink-ledger.md (口径 v2: 收录数, 8/19 起) + link-building-0816/0823.md

| # | 站点 | 提交日 | 状态 | 收录证据 | 复核日 |
|---|------|--------|------|----------|--------|
| 1 | Wired Business (wired.business) | 8/15 | **LIVE** | badge 验证通过 (8/17 06:41 autoglm) | 8/17 |
| 2 | TheNextAI | 8/16 | SUBMITTED | 审核中 (24-48h 承诺) | 待核 |
| 3 | AI Toolz Dir (aitoolzdir.com) | 8/16 | SUBMITTED | footer 回链 8/16 live; 收录 API 无法核 | 待核 |

**站外提及 + 外链收录计数 (KPI 口径)**: LIVE = 1 (Wired Business)
**KPI 偏差**: 9/13 目标 ≥5 → 当前 1 → 偏差 = |1-5|/5 = **80% > 20%** → 🔴 **标红** (PLAN-2026-09 §六: 若 9/13 站外收录 <3, 12 月目标自动下调一档)

## Step 2 下一批候选调研
- 目录站: 已按战略聚焦 #3 停止新增目录类候选 (TheNextAI 类对 2026 Google 无权重贡献, 不再提交流水)
- Reddit/Quora 种子队列 .hermes/drafts/reddit-seed-queue.md 已就绪 (5 选题, 全为 legit 队列 + review 页已上线):
  - #1 Is Spocket legit? (74 imp) → ✅ 草稿 8/24 (seed-02, 待 user 发布)
  - #2 Is Kittl worth it? (67+73 imp) → ✅ 草稿 8/26 (seed-03, 本次产出)
  - #3 Is Society6 legit? (59 imp) → 待写 (factcheck 8/22 已备)
  - #4 Is TeePublic legit? (66 imp) → 待写 (factcheck 8/22 已备)
  - #5 Is Redbubble legit? (67 imp) → 待写
- LaunchBuck 类机会: 维持 link-building-0823 待浏览器提交队列 (insidr.ai / productcool.com / opentools.ai / findly.tools / toolpilot.ai / thenextai.com / launchboosts.com + AI Valley CAPTCHA) — 不新增, 待 autoglm credits 恢复

## Step 3 种子草稿 (本次产出)

- .hermes/drafts/reddit-seed-03.md — **Is Kittl worth it?** (约 380 词, 目标 r/printondemand / r/graphic_design / Quora)
- 链接目标: https://aitoptools.net/kittl-review/ (sitemap 已上线 ✅)
- 数据: Trustpilot 4.8/5 ~1,150-1,200 reviews + G2 4.8/5 ~31-33 (fritz.ai 2026-07-15, 已验证) + Kittl 官网 (矢量导出 / ~$13/mo / free tier) + 无移动端等负面平衡点
- 纪律遵守: 真实问题开头 / 品牌提及优先 / 单链接自然语境 / 不吹嘘不编造 (所有数字带来源)
- 发布: 交 user 行动卡 (不自动发布, 铁律)
- 待 user 发布存货累计: seed-01 (GearLaunch) + seed-02 (Spocket) + seed-03 (Kittl)

## KPI 偏差汇总
- 站外提及+收录: 目标 9/13 ≥5, 当前 1 → **偏差 80% 标红 🔴**
- 处置: 每周 1 条第二梯队节奏维持 (seed-01/02/03 发布是当前最快增量路径, 发布动作全部在 user 侧)
- 收录目标实现依赖: user 发布 3 条已备种子帖 + autoglm credits 恢复后补交目录等待队列

## user 动作清单 (≥)
1. 发布 reddit-seed-01.md (GearLaunch) / seed-02 (Spocket) / seed-03 (Kittl) — 用个人账号, 单帖一次, 遵循各 sub 规则
2. autoglm credits 恢复后, 提交待浏览器队列 (insidr.ai / productcool.com / findly.tools / toolpilot.ai) — 目录收录 +2-4 潜在
3. 知悉 KPI 偏差 80% 标红: 若 9/13 前收录 <3, 12 月目标自动下调一档 (PLAN-2026-09 §六敏感性)

## 下一步 (下周三 20:17)
- 核对 seed-01/02/03 发布回填 → 若已发布则标 PUBLISHED, 继续写 Society6 种子草稿 (seed-04, factcheck 已备)
- 若 autoglm 恢复: 启动目录浏览器提交 (含 insidr.ai + productcool.com, 均 PROBE_OK)
