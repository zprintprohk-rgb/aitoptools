# 站外提及运营日志 — 2026-08-24 (mention-ops)

> 执行: cron 681966d9 (站外提及运营, 周三 20:17) | 依据: PLAN-2026-09 §三-修订2/§六
> 核心依据: 站外品牌提及相关性 0.664 vs 外链 0.218 (~3倍) — 升级为与外链并列的 GEO 主引擎

## Step 1 收录状态核查

台账: .hermes/logs/backlink-ledger.md (口径 v2: 收录数, 8/19 起) + link-building-0816/0823.md

| # | 站点 | 提交日 | 状态 | 收录证据 | 复核日 |
|---|------|--------|------|----------|--------|
| 1 | Wired Business (wired.business) | 8/15 | **LIVE** | badge 验证通过 (8/17 06:41 autoglm) | 8/17 |
| 2 | TheNextAI | 8/16 | SUBMITTED | 审核中 (24-48h 承诺) | 待核 |
| 3 | AI Toolz Dir (aitoolzdir.com) | 8/16 | SUBMITTED | footer 回链 8/16 live; 收录 API 无法核 (无凭证) | 待核 |

**站外提及 + 外链收录计数 (KPI 口径)**: LIVE = 1 (Wired Business)
**KPI 偏差**: 9/13 目标 ≥5 → 当前 1 → 偏差 = |1-5|/5 = **80% > 20%** → ⚠️ **标红** (PLAN-2026-09 §四: 若 9/13 站外收录 <3, 12 月目标自动下调一档)

## Step 2 下一批候选调研

- 目录池: .cluster/link-directory-list.md (112 站, 免费可投 104) — 已在前几轮 BLOCKED_CAPTCHA 池, 待 autoglm credits 恢复后浏览器提交
- 新增: Reddit/Quora 种子选题队列 .hermes/drafts/reddit-seed-queue.md (首次建立, 5 个选题按 GSC imp 排序)
  - #1 Is Spocket legit? (74 imp) → ✅ 草稿 8/24
  - #2 Is Kittl worth it? (67+73 imp) → 待写
  - #3 Is Society6 legit? (59 imp) → 待写 (factcheck 8/22 已备)
  - #4 Is TeePublic legit? (66 imp) → 待写 (factcheck 8/22 已备)
  - #5 Is Redbubble legit? (67 imp) → 待写
- LaunchBuck 类目录: 维持 link-building-0823 待浏览器提交池 (insidr.ai / productcool.com / opentools.ai / findly.tools / toolpilot.ai / thenextai.com / launchboosts.com + AI Valley CAPTCHA)

## Step 3 种子草稿

- .hermes/drafts/reddit-seed-02.md — **Is Spocket legit?** (约 420 词, 目标 r/dropshipping / r/printondemand / r/Shopify)
- 链接目标: https://aitoptools.net/spocket-review/ (sitemap 已上线, is-spocket-legit 未部署不可链 ✅ 合规)
- 数据: Sitejabber/SmartCustomer 2.1/5 · 29 reviews (8/22 验证, 不编造)
- 发布: 交 user 行动卡 (不自动发布 — 铁律)
- 上一份: reddit-seed-01.md (GearLaunch, 8/19) 仍待 user 发布

## KPI 偏差汇总

- 站外提及+收录: 目标 9/13 ≥5, 当前 1 → **偏差 80% 标红 ⚠️**
- 处置: 每周 1 条第二梯队节奏维持; seed-01/02 发布是当前最快增量路径, 发布动作全部在 user 侧

## user 动作清单 (≤3)

1. 发布 reddit-seed-01.md (GearLaunch) + reddit-seed-02.md (Spocket) — 用个人账号, 单帖一次
2. autoglm credits 恢复后: 提交待浏览器池 (insidr.ai / productcool.com / findly.tools / toolpilot.ai) — 目录收录 +2-4 潜在
3. 知悉 KPI 偏差 80% 标红: 若 9/13 前收录 <3, 12 月目标自动下调一档 (PLAN-2026-09 §四敏感性)

## 下一步 (下周三 20:17)

- 核 reddit-seed-queue.md 发布回填 → 写 Kittl 种子草稿 (seed-03)
- 若 autoglm 恢复: 启动目录浏览器提交 (先 insidr.ai + productcool.com, 均 PROBE_OK)
