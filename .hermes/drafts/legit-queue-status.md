# legit-queue 状态核对 (2026-08-18 03:5x 核查)

> 目的: 核对 legit-queue.md（T3, 8/17 建立）首批 10 篇是否存在、是否带 GSC imp 数据、现状与状态。
> 核对方法: 只读实际文件 — `src/data/blog-posts.json` / `src/data/reviews.json` / `public/sitemap.xml` / `out/sitemap.xml` / `handoff/strategy/STRATEGY-2026-08-17.md` / git log。
> 结论先行: 队列文件存在且 10 项完整；GSC imp 数据与 STRATEGY-2026-08-17 一致（转抄，未二次拉取 GSC）；仅 #1 MagicDrop 已部署，其余 9 篇均待写（各自 review 页全部存在，互链目标就绪）。

## 10 项状态总表

| # | 工具 | GSC imp（来源: STRATEGY 8/17 + legit-queue） | review 页存在? (reviews.json) | legit 页存在? (blog-posts.json) | 状态 | 幂等键 |
|---|---|---|---|---|---|---|
| 1 | MagicDrop | 120+ imp 簇（is magicdrop legit 84 / magicdrop trustpilot 12 / magicdrop legit 19 / 其他变体） | ❌ 无专页（related 卡链 printify/printful/claid/gear-launch 兜底互链） | ✅ `is-magicdrop-legit` **已部署** | **DONE 8/17** | 扩写已部署 → SKIPPED |
| 2 | GearLaunch | is gearlaunch legit 29 + gearlaunch.com legit 46 = 75（首点击 8/13 在 review 页 pos 36.15, CTR 5%） | ✅ `gear-launch-review-2026` | ❌ | **待写** (8/18 优先) | 页面存在→扩写路线 |
| 3 | Spocket | is spocket legit 74 | ✅ `spocket-review` | ❌ | 待写 (8/19 优先) | 页面存在→扩写路线 |
| 4 | Kittl | is kittl legit 67 / is kittl worth it 73 | ✅ `kittl-review` | ❌ | 待写 | 页面存在→扩写路线 |
| 5 | Society6 | society6 legit 59 | ✅ `society6-review` | ❌ | 待写 | 无专页→新建 |
| 6 | TeePublic | teepublic legit 66 | ✅ `teepublic-review` | ❌ | 待写 | 无专页→新建 |
| 7 | Redbubble | is redbubble legit 67（与 society6 同簇） | ✅ `redbubble-review` | ❌ | 待写 | 无专页→新建 |
| 8 | Gelato | is gelato worth it 26 | ✅ `gelato-review` | ❌ | 待写 | 页面存在→扩写路线 |
| 9 | PosterMyWall | is postermywall safe 63.5 | ✅ `postermywall-review` | ❌ | 待写 | 无专页→新建 |
| 10 | Veed | is veed io safe 80 | ✅ `veed-io-review` | ❌ | 待写 | 无专页→新建 |

**要点**: ① 10 项全部带 GSC imp 数据，无缺项；② review 页 9/9 存在（仅 MagicDrop 无专页，其 legit 页自身已含替代品 CTA 互链），双向互链目标全部就绪；③ legit 页仅 1/10 部署（MagicDrop）。

## #1 MagicDrop 已部署实证（字节级核对 2026-08-18）

- `src/data/blog-posts.json` 存在条目: slug `is-magicdrop-legit`，datePublished 2026-08-07，dateModified 2026-08-17（8/17 扩写）
- 字数: blocks+FAQ 实测 ≈**3,420 词**（队列记 3,132 — 计数口径差异，两种口径均 ≥2,500 军规达标，如实标注）
- FAQ: **8 条**（≥5 达标），覆盖变体: scam / what happened / magicdrop.io / alternative / how to check / trustpilot / free money / BBB
- 来源 URL 已带（12 处 Trustpilot 提及 + 4 个外源）: `trustpilot.com/review/magic-drop.top` / `gridinsoft.com/online-virus-scanner/url/magicdrop-link` / `afternic.com/domain/magicdrop.com` / `magicdrop.com`(+lander)
- 部署实证: `public/sitemap.xml` ✅ + `out/sitemap.xml` ✅ 均含 `https://aitoptools.net/blog/is-magicdrop-legit/`；git commit `e44c13c`（ops 0817 daily-search: "T2 is-magicdrop-legit 扩写(Trustpilot专章+3 FAQ变体+gear-launch互链, 3,132词, 8 FAQ)"）
- GSC 实测（STRATEGY 8/17 F3）: 页级 pos 18.29 / 79 imp —— 全站首个 top-20 页面；"magicdrop trustpilot" pos 19.17 / 12 imp

## 缺失项与风险（如实标注）

1. **GSC imp 未二次拉取**: 上表 imp 均转抄自 STRATEGY-2026-08-17.md（其源为 8/17 早 GSC 拉取）。如需精确现值，下次 daily-search 补拉后再校。
2. **D12（选题确认）/ D13（公开 rubric 确认）均待拍板**: 模板 v2 已起草（legit-template-v2.md）拍板即用；首批 10 篇执行节奏 2 篇/日夜间窗口。
3. **方法页未建**: `methodology-legit-ratings` 页尚未开工（现有 /methodology/ 仅有通用测试方法页）。按 v2 模板 §3，首批 legit 页上线前应先上线方法页。
4. **队列未含字段**: 每篇 metaDesc / 联盟 CTA 目标（affiliateUrl 商户）/ 截图路径未在队列中指定 —— v2 模板 §5 已补齐规范，写作时按联盟矩阵（AGENTS.md §5）选已批平台。
5. **无独立 GSC 导出文件**: 队列 GSC 列无法独立复核原始数据，仅 STRATEGY 单源（跨文件一致性已核对 ✅）。
6. **MagicDrop 无独立 review 页**: 其互链靠 related 卡（printful-vs-printify / print-price-ai / printify-review / printful-review / claid-ai-review / gear-launch-review-2026）承担，不阻塞。

## 下一步（对齐 legit-queue.md 8/18-8/19 窗口）

- 8/18: GearLaunch legit 扩写（有真实点击背书，优先最高）→ 按 v2 模板出评分卡 + answer-first 结构
- 8/19: Spocket legit 扩写（74 imp 簇）
- 每篇上线前事实核实（web_search Trustpilot/BBB/Reddit），评分数据无来源 URL 禁止上线
