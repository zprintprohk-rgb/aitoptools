# 站外提及运营日志 — 2026-08-27 (mention-ops)

> 执行: 手动触发 (webchat "执行", 03:07) | 依据: PLAN-2026-09 §三-修订2/§六
> 核心依据: 站外品牌提及相关性 0.664 vs 外链 0.218 (~3倍) — 升级为与外链并列的 GEO 主引擎
> 战略聚焦 (2026-08-24 千问指令 #3): 停止低质目录站提交; 全力聚焦 Reddit/Quora 种子帖质量 (真实人类口吻、自然讨论、品牌提及优先于链接); 即使不带链接也目标让 "aitoptools {tool}" 可被搜索到 (信任分)

## Step 1 收录状态核查
台账: .hermes/logs/backlink-ledger.md (口径 v2: 收录数, 8/19 起) + link-building-0816/0823.md

| # | 站点 | 提交日 | 状态 | 收录证据 | 复核日 |
|---|------|--------|------|----------|--------|
| 1 | Wired Business (wired.business) | 8/15 | **LIVE** | badge 验证通过 (8/17 06:41 autoglm) | 8/17 |
| 2 | TheNextAI | 8/16 | SUBMITTED | 审核中 (24-48h 承诺) | 待核 |
| 3 | AI Toolz Dir (aitoolzdir.com) | 8/16 | SUBMITTED | footer 回链 8/16 live; 收录 API 无法核 | 待核 |

**站外提及复核 (8/27 web_search)**: "aitoptools.net" + Society6/Kittl/Spocket 检索 → 仅返回自身页面 (aitoptools.net 域名内), 无新站外品牌提及/收录证据 → 收录计数维持不变。

**站外提及 + 外链收录计数 (KPI 口径)**: LIVE = 1 (Wired Business)
**KPI 偏差**: 9/13 目标 ≥5 → 当前 1 → 偏差 = |1-5|/5 = **80% > 20%** → 🔴 **标红** (PLAN-2026-09 §六: 若 9/13 站外收录 <3, 12 月目标自动下调一档)

## Step 2 下一批候选调研
- 目录站: 维持停止新增 (战略聚焦 #3)
- Reddit/Quora 种子队列 .hermes/drafts/reddit-seed-queue.md 扩至 8 选题:
  - #1 Spocket (74 imp) → ✅ seed-02 (8/24, 待发布)
  - #2 Kittl (67+73) → ✅ seed-03 (8/26, 待发布)
  - #3 Society6 (59) → ✅ seed-04 (8/27, 本次产出)
  - #4 TeePublic (66) → 待写 (factcheck 8/22 已备)
  - #5 Redbubble (67) → 待写
  - #6 Veed (80) → ⚠️ 待 veed-review 页上线 (未在 sitemap, 不可链)
  - #7 PosterMyWall (63.5) → 待写 (factcheck 8/22 已备)
  - #8 Gelato (26) → 待写 (factcheck 8/20 已备)
- 新增依据: legit-queue.md GSC imp 排序 + sitemap 已上线 review 页 (Veed 例外, 已标注)

## Step 3 种子草稿 (本次产出)

- .hermes/drafts/reddit-seed-04.md — **Is Society6 legit? / Is Society6 worth it?** (约 400 词, 目标 r/printondemand / r/EtsySellers / r/passive_income)
- 链接目标: https://aitoptools.net/society6-review/ (sitemap 已上线 ✅)
- 数据: Trustpilot 3.6/5 · 2,111 条 (highly mixed, 2026-08-24 验证) + BBB A+ Accredited (2026-08-24 验证) + 站内实测 4.0/5 免月费 (society6-review 页) — 全部带来源, 禁止编造
- 角度: 先答 "legit 无疑问 (BBB A+)", 再给真实痛点 (利润率薄 / 差评模式), 最后实用建议 (被动画廊定位, 非主收入)
- 纪律遵守: 真实问题开头 / 品牌提及优先 / 单链接自然语境 / 不吹嘘不编造
- 发布: 交 user 行动卡 (不自动发布, 铁律)
- 待 user 发布存货累计: seed-01 (GearLaunch) + seed-02 (Spocket) + seed-03 (Kittl) + seed-04 (Society6)

## KPI 偏差汇总
- 站外提及+收录: 目标 9/13 ≥5, 当前 1 → **偏差 80% 标红 🔴**
- 处置: 每周 1 条第二梯队节奏维持 (本周已超产: seed-03 + seed-04 两条); 发布动作全部在 user 侧
- 收录目标实现依赖: user 发布 4 条已备种子帖 + autoglm credits 恢复后补交目录等待队列 (insidr.ai / productcool.com 等 PROBE_OK)

## user 动作清单 (≥)
1. 发布 reddit-seed-01 (GearLaunch) / seed-02 (Spocket) / seed-03 (Kittl) / seed-04 (Society6) — 个人账号, 单帖一次, 遵循各 sub 规则
2. autoglm credits 恢复后, 提交待浏览器队列 (insidr.ai / productcool.com / findly.tools / toolpilot.ai) — 目录收录 +2-4 潜在
3. 知悉 KPI 偏差 80% 标红: 若 9/13 前收录 <3, 12 月目标自动下调一档 (PLAN-2026-09 §六敏感性)

## 下一步 (下周三 20:17 或下次触发)
- 核对 seed-01~04 发布回填 → 若已发布标 PUBLISHED, 继续写 TeePublic 种子草稿 (seed-05, factcheck 已备)
- Veed: veed-review 页上线后从 ⚠️ 转 ✅ 可写 (GSC 80 imp, 队列最高)
- 若 autoglm 恢复: 启动目录浏览器提交 (含 insidr.ai + productcool.com, 均 PROBE_OK)
