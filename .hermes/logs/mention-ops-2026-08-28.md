# 站外提及运营日志 — 2026-08-28 (mention-ops)

> 执行: 手动触发 (webchat "执行", 02:20) | 依据: PLAN-2026-09 §三-修订2/§六
> 核心依据: 站外品牌提及相关性 0.664 vs 外链 0.218 (~3倍) — 升级为与外链并列的 GEO 主引擎
> 战略聚焦 (2026-08-24 千问指令 #3): 停止低质目录站提交; 全力聚焦 Reddit/Quora 种子帖质量 (真实人类口吻、自然讨论、品牌提及优先于链接); 即使不带链接也目标让 "aitoptools {tool}" 可被搜索到 (信任分)

## Step 1 收录状态核查
台账: .hermes/logs/backlink-ledger.md (口径 v2: 收录数, 8/19 起) + link-building-0816/0823.md

| # | 站点 | 提交日 | 状态 | 收录证据 | 复核日 |
|---|------|--------|------|----------|--------|
| 1 | Wired Business (wired.business) | 8/15 | **LIVE** | badge 验证通过 (8/17 06:41 autoglm) | 8/17 |
| 2 | TheNextAI | 8/16 | SUBMITTED | 审核中 (24-48h 承诺) | 待核 |
| 3 | AI Toolz Dir (aitoolzdir.com) | 8/16 | SUBMITTED | footer 回链 8/16 live; 收录 API 无法核 | 待核 |

**站外提及复核 (8/28 web_search "aitoptools" -site:aitoptools.net)**: 全部结果均为同名竞品 aitoptools.com 资产 (官网/Crunchbase/G2/beehiiv/GitHub) — aitoptools.net **0 条站外提及证据**。同名混淆风险持续存在 (站内已有 "Independent Operation" 声明兜底), 印证品牌提及信任分建设必要性。
**发布回填检查**: 队列无 PUBLISHED 标记 (seed-01~04 仍待 user 发布)。

**站外提及 + 外链收录计数 (KPI 口径)**: LIVE = 1 (Wired Business)
**KPI 偏差**: 9/13 目标 ≥5 → 当前 1 → 偏差 = |1-5|/5 = **80% > 20%** → 🔴 **标红** (PLAN-2026-09 §六: 若 9/13 站外收录 <3, 12 月目标自动下调一档)

## Step 2 下一批候选调研
- **发现队列遗漏**: MagicDrop (is magicdrop legit 82 imp, 簇 120+ 含 trustpilot 13 + free money 3) — 全站最高 legit 需求簇, 但 8/24 建队时漏收 (当时只有 GearLaunch 有种子)
- 补入队列 #1 (按 imp 重排): 目标页 /blog/is-magicdrop-legit/ (sitemap 已上线 ✅, 8/17 扩写 3,520 词, hands-on 域名验证)
- 队列现 9 选题: #1 MagicDrop 82 → #2 Spocket 74 → #3 Kittl 67+73 → #4 Society6 59 → #5 TeePublic 66 → #6 Redbubble 67 → #7 Veed 80 (⚠️ 页面未上线) → #8 PosterMyWall 63.5 → #9 Gelato 26
- 目录站: 维持停止新增 (战略聚焦 #3); LaunchBuck 类等待队列不动 (insidr.ai / productcool.com 等 PROBE_OK, 待 autoglm credits)

## Step 3 种子草稿 (本次产出)

- .hermes/drafts/reddit-seed-05.md — **Is MagicDrop legit? / What happened to MagicDrop?** (约 400 词, 目标 r/printondemand / r/Shopify / Quora)
- 链接目标: https://aitoptools.net/blog/is-magicdrop-legit/ (sitemap 已上线 ✅)
- 数据 (全部带来源): 8/7 实测 magicdrop.com → Afternic 出售页 (hands-on) + Trustpilot 主域无档案 / magic-drop.top 2.9/5 仅 2 条 (~2021) + BBB 无档案 (8/17 检索) + 旧投诉模式 (2-4 周发货/质量不稳/退款看供应商) + "free money" 山寨陷阱警告
- 角度: 「不是诈骗, 是已关闭」差异化结论 + 5 分钟域名自查 evergreen 方法论 (高收藏率选题) + 迁移建议
- 纪律遵守: 真实问题开头 / 单链接自然语境 / 不吹嘘不编造
- 发布: 交 user 行动卡 (不自动发布, 铁律)
- 待 user 发布存货累计: seed-01 (GearLaunch) + seed-02 (Spocket) + seed-03 (Kittl) + seed-04 (Society6) + seed-05 (MagicDrop) — **5 条积压**

## KPI 偏差汇总
- 站外提及+收录: 目标 9/13 ≥5, 当前 1 → **偏差 80% 标红 🔴**
- 处置: 种子存货已 5 条 (远超每周 1 条节奏), **瓶颈已从产能转到 user 发布动作** — 建议 user 本周内分 2-3 天发布 (勿单日刷屏)
- 收录目标实现依赖: user 发布 5 条种子帖 + autoglm credits 恢复后补交目录等待队列

## user 动作清单 (≥)
1. **发布积压 5 条种子帖** (seed-01 GearLaunch / seed-02 Spocket / seed-03 Kittl / seed-04 Society6 / seed-05 MagicDrop) — 个人账号, 建议 2-3 天分批, 单帖一次, 遵循各 sub 规则
2. autoglm credits 恢复后, 提交待浏览器队列 (insidr.ai / productcool.com / findly.tools / toolpilot.ai) — 目录收录 +2-4 潜在
3. 知悉 KPI 偏差 80% 标红: 若 9/13 前收录 <3, 12 月目标自动下调一档 (PLAN-2026-09 §六敏感性)

## 下一步 (下周三 20:17 或下次触发)
- 核对 seed-01~05 发布回填 → 标 PUBLISHED
- 继续写 TeePublic 种子草稿 (seed-06, factcheck 8/20 已备: TP 4.4/5 640k+ 样本)
- Veed: veed-review 页上线后转可写 (80 imp)
- 若 autoglm 恢复: 启动目录浏览器提交 (insidr.ai + productcool.com)
