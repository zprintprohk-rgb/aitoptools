# aitoptools.net — AI 协作指南

> **项目**: F:\aitoptools（Next.js 14 静态导出，AI 工具评测站）
> **定位**: AI Tools for Print Shops & Independent Store Owners —— 印刷店/POD 卖家的垂直 AI 工具决策平台
> **域名**: aitoptools.net（品牌不换名，2026-07-17 user 拍板）
> **启动必读**: 每次进场先读 `k3-ops-constitution-v2.md`（多项目运营宪法），再读本文件

## 0. 运营约束（源自宪法 v2，最高优先级）

- **资源配比**: C 项目 15%，Hermes 批量评测草稿为主，**M3 只做深度对比/榜单**
- **北极星指标**: CPA/CPS 佣金/月（6 个月目标 $3000，见 EXECUTION_PLAN.md）
- **攒批 push**: Cloudflare Pages build quota 稀缺，**1 push/天**，改动攒批；仅紧急修复（404/死链/白屏）可单独 push
- **免检原则**: 执行层报 Success + 构建页数自检正确 = 免检；只有 Error/Timeout/user 报错才截图诊断
- **push ≠ deploy**: 以 GitHub check-runs 的 CF Pages 状态为准，不以 git log 为准
- **任务卡铁律**: 任何任务必须带「当前动作支撑赚钱目标: [具体指标]」，缺了自动驳回

## 1. 核心定位（一句话）

> 不做通用 AI 导航站（红海，有巨头和 aitoptools.com 在前），做**印刷/POD 行业的 AI 工具雷达 + 深度决策内容**——别人收 3 万个工具，我们只收 300 个，每个都有评测和购买建议。

- **目标读者**: POD 卖家、印刷店主、包装设计/电商物料从业者（英文站）
- **内容哲学**: Wirecutter 的决策结构（骨架）+ G2 的数据组件（肌肉）+ Raycast 的克制视觉（外衣）
- **发布纪律**: 雷达发现 → 模板草稿 → **事实核实（WebSearch 引用源）→ 才允许上线**。宁可每周 3 篇精品，不要每天 10 篇垃圾（Google Helpful Content 红线）

## 2. 设计 Token（默认锁定，2026-07-18 拍板；2026-07-22 修订变更规则）

| Token | 值 | 用途 |
|---|---|---|
| 纸白 | `#FAF7F2` | 页面背景 |
| 墨黑 | `#17201c` | 标题/正文 |
| 品牌绿 | `#0b5f59` | 页头、链接、强调 |
| 琥珀橙 | 唯一强调色 | CTA、Our Pick、下划线、Better Value |

**变更规则（2026-07-22 user 拍板）**：Token 默认锁定，但不为锁而锁。若确实有很好的 UI/UX 设计方案，允许改——准入门槛：① 明显更大气、更美观、更专业（有对标参照或设计依据，不是换个颜色而已）；② 全站一致替换，不做局部变色；③ 改前给 user 看方案，user 拍板后才动工。

- ❌ 默认禁止第三色（黄色已清除）、禁止 muddy 渐变、禁止照片 hero（评测站产品是内容本身）——除非走上面的变更规则且方案确实更好
- 卡片：1px `rgba(23,32,28,0.10)` 细边框，**零阴影**；hover 只留颜色/边框过渡，禁止 scale/translate 动效
- 区块间距桌面 115px，卡片内边距 28-32px，正文行高 1.7

## 3. 内容标准模板（所有新对比页/榜单页必须遵守）

数据结构在 `src/data/comparisons.json` / `listicles.json`，渲染组件已固化：

- **picks 三级推荐卡**: 恰好 3 项（top / also / budget），PicksCards.js
- **features 功能矩阵**: 7-8 行，取值 true/false/"partial"，FeatureMatrix.js（✓/✗/◐）
- **pricing 定价表**: 含 betterValue 标记，PricingTable.js（Better Value 琥珀标签）
- **WhyTrustUs**: 页底 FAQ 前固定模块
- 评分一律走 RatingBar.js；Pros/Cons 走 ProsCons.js 双栏
- 校验: `python scripts/validate_content_data.py` 全过才允许构建（M3 任务，2026-07-21 已派）

## 4. 自动化管线（已建）

| 任务 | 触发 | 作用 |
|---|---|---|
| 每日 AI 工具发现 | cron `23 8 * * *` Asia/Shanghai | 扫 ProductHunt/聚合站 → 垂直过滤 → 写 `discovery/YYYY-MM-DD.md` |
| 联盟审批监控 | cron `12 9 * * *` Asia/Shanghai | 查 Gmail 审批结果邮件 + 通知 |

- 发现 → 评测队列（CONTENT_PLAN.md 63 页分三批，第一批 7 篇已完成）
- CTA 占位 `?fpr=partner`，联盟链接批下后走 `scripts/replace_affiliate_links.py --apply` 统一替换 → `scripts/affiliate_link_audit.py` 验证

## 5. 联盟账户矩阵（凭证在 credentials.affiliate.local.json，已 gitignore，勿提交）

| 平台 | 状态 | 说明 |
|---|---|---|
| Creative Fabrica | ✅ 已获批 | ref/27832838 |
| Kittl (Impact) | 🟡 审核中 | 7/15 提交，Impact 账号 Jerome88 / zprintpro@outlook.com |
| Claid / Printify / Printful | 🟡 审批中 | 预计 7/21-23 出结果 |
| Placeit | ⏸ 待申请 | 等 Impact Marketplace 升级获批后申请 |
| Looka | ❌ 计划关闭 | 不再投入 |
| Mockey | 🆕 雷达发现 | 30% 经常性佣金公开计划，待申请（高优先级） |

- 日志: `AFFILIATE_LOG.md`；审计: `AFFILIATE_AUDIT.md`
- 敏感操作（登录/验证码/资金）→ 交 user 行动卡片，绝不自动

## 6. 技术架构

- Next.js 14 `output:'export'` → `out/`，push main 触发 CF Pages 部署（CDN 传播 1-2 分钟）
- 仓库: github.com/zprintprohk-rgb/aitoptools
- 数据驱动: `src/data/tools.json`（实为 reviews.json 收录 94 工具）/ comparisons.json / listicles.json
- SEO: llms.txt + robots 放行 AI 爬虫 + 74 页 FAQ JSON-LD（scripts/generate_faqs.js）
- 构建验证: `npm run build` 全量通过，页数只增不减（当前 113 页）

## 7. 7 大"绝对不要做"清单

1. ❌ 不要改品牌名/换域名（已拍板，不再投入）
2. ❌ 不要做通用 AI 导航站定位（垂直护城河不可稀释）
3. ❌ 不要未经事实核实直接发布 AI 生成的评测内容
4. ❌ 不要擅自加照片 hero / 第三色 / 阴影 / 缩放 hover（默认锁定；确有更优设计按 §2 变更规则走，user 拍板后执行）
5. ❌ 不要一天多次 push（攒批，quota 稀缺）
6. ❌ 不要提交 credentials.affiliate.local.json 或任何凭证
7. ❌ 不要自动执行登录/验证码/资金操作（交 user）

## 8. 关键文件别删

- `k3-ops-constitution-v2.md`（宪法，启动必读）
- `EXECUTION_PLAN.md` / `CONTENT_PLAN.md` / `TRAFFIC_STRATEGY.md`
- `AFFILIATE_LOG.md` / `AFFILIATE_PROGRAMS.md`
- `scripts/replace_affiliate_links.py` / `affiliate_link_audit.py` / `generate_faqs.js`
- `discovery/`（雷达产出目录）
- `AGENTS.md`（本文件）
