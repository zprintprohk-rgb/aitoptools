# M3 首月执行手册（Month 1 Runbook）— aitoptools.net 联盟佣金破冰

> **文件用途**：M3 及执行团队**逐条照做**的操作手册。每个任务含步骤、命令/代码、验收线、负责人占位、依赖。**不需要读任何上游对话**即可执行。
> **版本**：v1.0 ｜ **窗口**：M3 第 1–30 天 ｜ **站点**：aitoptools.net
> **上游指针**（只读引用，不在本文件复述）：`AGENTS.md`、`AFFILIATE_PROGRAMS.md`（费率/EPC 表）、`TRAFFIC_STRATEGY.md`、`AFFILIATE_LOG.md`、`CONTENT_PLAN.md`。本文件与它们冲突时，**变现动作以本文件为准**，设计/合规动作以上游为准。

---

## 0. 阅读约定（M3 开工前必读，3 分钟）

- 任务编号 `W{n}-T{m}` = 第 n 周第 m 个任务。`[P0]` = 阻塞型，不做后面全停。
- 每个任务卡字段：`负责人`（填人名/角色）、`耗时`、`前置`（依赖的任务 ID）、`撬动环`（见 §2）、`步骤`、`DoD`（完成定义，**必须可判定**）、`产出物`、`风险/回滚`。
- **checkbox 用法**：`- [ ]` 未做 / `- [x]` 完成。M3 每完成一步打勾，**DoD 全勾才算该任务完成**，不许"差不多"。
- **阻塞规则**：单任务卡住 **> 4 小时**无进展 → 在 `AFFILIATE_LOG.md` 记一行 `[BLOCKED W{n}-T{m}] 原因 / 已尝试 / 需谁` 并升级给决策人，**不要静默停摆**。
- **范围护栏（红线，违反即停）**：
  1. 首月**新内容只允许 3 篇 + 1 篇 3D 桥接文**（见 W3-T2 / W2-T3）。**禁止**自建新垂直、新支柱、新 IA 分支。3D 仅限 W2-T3 定义的范围，**多写 1 篇 3D = 违规**。
  2. 首月**禁止**做"立规则/画 IA/重构设计系统"类 0 佣金动作占用本手册排期。设计修复（深底文本/grid 溢出/section 节奏）**并行另开线**，不占 W1–W4 任何工时。
  3. 首月**禁止**接任何"付费上位/paid placement"，违反即破坏中立人设（见 `AGENTS.md`）。

---

## 1. 首月北极星 & 预期管理（KPI 写错，执行必歪——必读）

- **首月北极星 ≠ 收入金额。** 首月北极星 = **"变现管道三件套跑通"**：① 度量能看见每个链接的点击；② 带佣按钮是主 CTA；③ 至少有 1 个非搜索流量渠道带来非零点击。
- **首月收入目标 = 破冰 $20–50，不是 $3000÷6=$500。** 用 $500 考核 M1 会导致动作变形（去追短期低质流量）。**M1 看到 $30 且三件套跑通 = 成功**；看到 $0 但三件套跑通 = 部分成功（管道对，灌水从 M2 起）；看到 $500 但三件套没跑通 = **失败**（不可持续，M2 会归零）。
- **6 个月总目标**：累计 $3,000，M6 单月 ≥ $800。首月只负责"建管道"，**爬坡在 M2–M4，冲量在 M5–M6**。

---

## 2. 佣金公式 & 四环诊断（每个任务在撬哪一环）

`佣金 = 访客 × 看到链接率 × 点击率(CTR) × 转化率(CVR) × EPC`

| 环 | 现状 | 首月负责撬动的任务 |
|---|---|---|
| 度量（地基） | GA4/点击事件**未装** → 0 元第一因 | **W1-T1 [P0]** |
| 看到链接率 | 带佣按钮 `Check Deal` 与阅读按钮平权/更弱 | **W1-T2** |
| 访客 | 自然流量≈0，缺社媒快钱腿 | **W2-T1 / W2-T2 / W2-T3 / W3-T2** |
| 转化率 × EPC | 链接多指商户首页，非深链；高佣商户未优先 | **W3-T1** |
| 闭环优化 | 无链接级 CTR 榜，不知砍/加 | **W4-T1** |

> **优先级铁律**：W1-T1 > W1-T2 > W2-T1 > W3-T1 > 其余。**度量与提权不做，后面灌的流量全是浪费。**

---

## 3. 关键路径（依赖图）

```
W1-T1[度量,P0] ──┬──> W1-T2[提权] ──> W2-T1[社媒分发] ──> W4-T1[看数据砍/加]
                 ├──> W2-T2[社群分发]
                 ├──> W2-T3[3D桥接,仅此1篇]
                 ├──> W3-T1[深链+高佣] ──> W4-T1
                 └──> W3-T2[3篇高意图新文]

```
- **串行硬依赖**：W1-T1 必须先于一切（没埋点，W4 无从判定）。W1-T2 先于 W2 分发（灌流量前先确保带钱按钮突出）。W3-T1/W2 先于 W4-T1。
- **可并行**：W2-T1 / W2-T2 / W2-T3 三者互不依赖；W3-T1 与 W3-T2 可并行。

---

## 4. 周任务卡

### WEEK 1 — 度量 + 提权（管道第一节）

#### W1-T1 [P0] 装度量：GA4 + 联盟链接点击事件 + UTM
- **负责人**：______ ｜ **耗时**：0.5–1 天 ｜ **前置**：无 ｜ **撬动环**：地基
- **目标**：后台能看见"每个联盟链接被点几次、来自哪篇、点去哪个商户"。
- **步骤**：
  1. 在 GA4 创建媒体资源，取 `G-XXXXXXXXXX`，全站注入 gtag（`<head>` 或 tag manager 二选一，**全站唯一**，禁止重复注入）。
  2. 给所有联盟链接统一加 class `aff-link` 与 data 属性（命名规范见附录 A）：
     ```html
     <a class="aff-link"
        data-link-id="printful-review-cta1"
        data-merchant="printful"
        data-target="product"
        href="https://...?utm_source=aitoptools&utm_medium=review&utm_campaign=m1&utm_content=printful-review-cta1">…</a>

     ```
  3. 注入出站点击事件脚本（**复制即用**）：
     ```html
     <script>
     document.addEventListener('click', function(e){
       var a = e.target.closest('a.aff-link');
       if(!a) return;
       gtag('event','outbound_click',{
         link_id:   a.dataset.linkId   || 'unknown',
         merchant:  a.dataset.merchant || 'unknown',
         target_type: a.dataset.target || 'unknown',
         page_path: location.pathname,
         link_url:  a.href
       });
     }, true);
     </script>

     ```
  4. GA4 后台把 `outbound_click` 标记为**转化事件**；建自定义维度 `link_id / merchant / target_type`。
  5. 用 GA4 **DebugView** 实时点 3 个不同链接，确认事件带齐 4 个参数。
- **DoD**：
  - [ ] 全站 gtag 唯一注入，无重复。
  - [ ] 71 个联盟链接**100%** 带 `aff-link` + 3 个 data 属性 + UTM（用脚本扫：`document.querySelectorAll('a[href*="affiliate-or-known-domain"]').length` 应等于带 `aff-link` 的数量；不等则补漏）。
  - [ ] DebugView 看到 `outbound_click` 且参数齐全。
  - [ ] 在 GA4 建好"链接点击"探索报表模板（维度 `link_id`，指标 `event_count`）。
- **产出物**：埋点上线 + 报表模板 + 一份"71 链接埋点核对表"（link_id ↔ 商户 ↔ 所在页）。
- **风险/回滚**：gtag 注入冲突 → 回滚到注入前 commit；事件丢失 → 检查是否被 CSP/广告拦截，改用 `navigator.sendBeacon` 兜底。

#### W1-T2 带钱按钮提权：`Check Deal` 升为主 CTA
- **负责人**：______ ｜ **耗时**：0.5 天 ｜ **前置**：无（但建议 W1-T1 后做，便于 W4 测 CTR）｜ **撬动环**：看到链接率 × CTR
- **目标**：卡片+详情页里，带佣按钮视觉权重 > 阅读按钮；并加价格锚点微文案。
- **步骤**：
  1. 卡片结构改为：主 CTA = `Check Deal`（联盟链，class `cta-primary aff-link`），次 CTA = `Read Full Review`（class `cta-secondary`）。**DOM 顺序主在前**。
  2. 套用样式（**复制即用**，可按设计 token 调色，但**对比关系不可反**）：
     ```css
     .cta-primary{ /* 带佣 */
       background:var(--c-accent,#e07b00); color:#fff;
       font-weight:700; padding:.7em 1.1em; border-radius:10px;
       font-size:1rem; box-shadow:0 2px 8px rgba(224,123,0,.25);
     }
     .cta-secondary{ /* 阅读 */
       background:transparent; color:var(--c-accent,#e07b00);
       font-weight:600; padding:.6em .9em; border:1px solid currentColor;
       font-size:.92rem;
     }
     .cta-primary .price-anchor{ font-size:.8em; opacity:.92; display:block; }

     ```
  3. 给主 CTA 加**价格锚点微文案**（模板见附录 C），例：`Check Deal` 下挂一行 `$49/mo · 14-day trial`。**价格必须取自 `AFFILIATE_PROGRAMS.md`/商户页真实值，禁止编造**；取不到则只显示 `See current deal ↗`，不写数字。
  4. 详情页正文结论段后**再放一次**主 CTA（深链，见 W3-T1）。
- **DoD**：
  - [ ] 主 CTA computed `font-size` ≥ 次 CTA × 1.05，且主为实心填充、次为描边（肉眼+DevTools 双确认）。
  - [ ] 主 CTA 与背景对比度 ≥ 3:1（大文本 UI 组件线）。
  - [ ] 71 链接所在卡片**100%** 完成主次排序；价格锚点要么真实要么不显示数字。
  - [ ] 移动端（360px）主 CTA 不折行、不溢出。
- **产出物**：提权上线 + 前后截图对比 + 一份"无价格锚点的链接清单"（交 W3-T1 补深链时一并处理）。
- **风险/回滚**：若提权后 `Read Full Review` 点击暴跌而 `Check Deal` 未涨 → 说明文案/锚点问题，回滚文案不改结构，A/B 一轮。

---

### WEEK 2 — 灌第一批流量（社媒快钱腿 + 3D 侧链）

#### W2-T1 Pinterest 视觉分发
- **负责人**：______ ｜ **耗时**：2–3 小时/周（持续）｜ **前置**：W1-T2 ｜ **撬动环**：访客
- **步骤**：
  1. 建商业号 + 认领站点；建 3 个板：`POD Tools`、`AI Product Photography`、`Print-on-Demand Comparisons`。
  2. 把现有 6 对比 + 头部 10 review 各做 **1 张竖版 pin（1000×1500）**：标题=对比/榜单标题，主体=胜方徽章+一句结论，底=站点 URL。**用 Canva/Placeit 模板批产**。
  3. 每 pin 描述含 1 个目标关键字 + 链回对应页（带 UTM `utm_medium=pinterest`）。
  4. 节奏：**首周发 16 张**（6 对比+10 头部），之后每周 +5 张。
- **DoD**：[ ] 16 张 pin 上线且链回带 UTM；[ ] W2 末 GA4 出现 `source=pinterest` 非零会话。
- **产出物**：pin 模板源文件 + 发布排期表。

#### W2-T2 Reddit / Quora / 社群 价值分发
- **负责人**：______ ｜ **耗时**：2–3 小时/周 ｜ **前置**：W1-T2 ｜ **撬动环**：访客
- **步骤**：
  1. 选 5 个版/空间：`r/printondemand`、`r/Shopify`、`r/Etsy`、`r/3Dprinting`、Quora "best POD platform" 类问题。
  2. **先给价值后放链**：每条回答 ≥150 字真实建议，**链接只在末尾自然出现 1 次**，且链到"对比/榜单"页而非首页。每周 5–8 条，**禁止刷量/复制粘贴**（防删+防封）。
  3. 记录每条的 URL 与带来点击（靠 UTM `utm_medium=reddit|quora`）。
- **DoD**：[ ] 首周 ≥5 条存活回答；[ ] 无被删/被封；[ ] GA4 出现对应 source 非零（允许为 0 点击但必须有会话或印象记录）。
- **风险**：被判定 spam → 立即停该渠道 2 周，转 W2-T1 加倍。**绝不买量顶帖**。

#### W2-T3 3D 桥接（**范围护栏：仅此 1 篇 + 5 内链，禁止扩**）
- **负责人**：______ ｜ **耗时**：0.5–1 天 ｜ **前置**：W1-T1 ｜ **撬动环**：长尾访客 + SEO 多样性
- **步骤**：
  1. 写 **1 篇** `POD vs 3D-Print-on-Demand: Which Margins Win in 2026?`，套用现有 vs-card 模板，挂 ≥2 深链。
  2. 给头部 5 篇 review 各加 **1 个** 3D 应用场景内链（锚文本自然，如 "also works for 3D-printed product mockups"）。
  3. **停。** 不写第 2 篇 3D，不建 3D 分类页，不加顶栏入口。
- **DoD**：[ ] 1 篇上线 + 5 内链通 + 链接带 UTM；[ ] **3D 相关新增页面数 = 1**（用 `git`/sitemap 核对，>1 即违规回滚）。
- **风险**：执行中"顺手"想加 3D 榜单 → **停，记入 backlog 交 M2 决策**，不在 M1 做。

---

### WEEK 3 — 深链 + 高佣 + 3 篇高意图新文

#### W3-T1 高佣深链改造（**同样流量下佣金 2–3× 的关键**）
- **负责人**：______ ｜ **耗时**：1 天 ｜ **前置**：W1-T1 ｜ **撬动环**：CVR × EPC
- **步骤**：
  1. 打开 `AFFILIATE_PROGRAMS.md`，按 **佣金率/EPC 降序**排出 Top 10 商户（**用文件内真实值，本手册不预设名次**）。
  2. 审查 71 链接：凡 `data-target="home"` 或指向商户首页的 → 改为**具体产品/定价页深链**（深链拼接规则见附录 B）。
  3. 把 Top 10 高佣商户的链接**优先塞进头部 10 篇 review + 6 对比**的结论段与主 CTA（每篇至少 1 个高佣深链）。
  4. 更新 W1-T2 留下的"无价格锚点清单"：能取真实价格的补锚点。
- **DoD**：
  - [ ] 头部 16 篇内容**100%** 含 ≥1 深链；首页链占比从现状降到 **< 20%**。
  - [ ] 头部 16 篇**100%** 含 ≥1 个 Top10 高佣商户链接。
  - [ ] 所有深链点击在 GA4 可按 `target_type=product` 过滤验证。
- **产出物**：深链改造清单（link_id ↔ 旧 URL ↔ 新深链 ↔ 商户 ↔ 佣金率）+ 高佣商户×头部内容映射表。

#### W3-T2 写 3 篇高意图新文（**只 3 篇，只商业意图词**）
- **负责人**：______ ｜ **耗时**：2–3 天 ｜ **前置**：W1-T1 ｜ **撬动环**：高意图访客
- **步骤**：
  1. 选题**固定 3 个**（不许换成长尾/信息型）：
     - `Best AI Product Photography Tools for POD (2026)`
     - `Printful vs Printify 2026`（若已有则**优化**而非重写：补深链+提权+结论首句对齐 winner）
     - `Best Mockup Generator for Etsy Sellers (2026)`
  2. 每篇结构：结论首句=胜方 → 对比表（可被 AI 摘引）→ 每工具卡挂 ≥2 深链 + 主 CTA 提权。
  3. **每篇承诺的评分维度必须真能产出**（红线，见 §0）；产不出的维度**不显示**，宁可空。
- **DoD**：[ ] 3 篇上线；[ ] 每篇 ≥2 深链 + 主 CTA 提权；[ ] winner 徽章 = 结论首句 = 对比表胜方（三者一致，机器校验见附录 D）；[ ] 无空头维度。
- **风险**：写不完 3 篇 → **保 2 篇高意图，砍第 3 篇**，不许用 1 篇信息型长尾凑数。

---

### WEEK 4 — 看数据砍/加（第一次闭环）

#### W4-T1 链接级 CTR 榜 + 据此 10 处改动
- **负责人**：______ ｜ **耗时**：1 天 ｜ **前置**：W1-T1, W2-*, W3-* ｜ **撬动环**：CTR × EPC
- **步骤**：
  1. 从 GA4 导出 `link_id` 级 `outbound_click` 与所在页 `page_view`，算 **CTR = click / page_view**（按 link_id 聚合）。
  2. 排出 **Top10 / Bottom10** 链接。
  3. **Top10**：提炼共性（锚文本？位置？锚点文案？商户？），**复制模式**到同页其它链接。
  4. **Bottom10**：按判定线（附录 D）二选一——改锚文本/换位置/补锚点，或**换商户**（换 `AFFILIATE_PROGRAMS.md` 里同品类更高 EPC 的）。
  5. 把 W2 各渠道按"带来点击"排序：**有点击的加倍，0 点击且 0 会话的停**。
- **DoD**：
  - [ ] 产出"链接级 CTR 榜 v1"；[ ] 完成 ≥10 处改动并记录 before/after；[ ] 停掉 ≥1 个 0 产出渠道或动作。
- **产出物**：CTR 榜 v1 + 改动日志 + **M2 输入**（哪些模式有效→M2 复制扩量）。

---

## 5. 数据看板 & 判定线（M3 每周看这些，阈值写死）

每周日跑一次，填入 `AFFILIATE_LOG.md`：

| 指标 | 取数 | M1 健康线 | 不达标动作 |
|---|---|---|---|
| 联盟点击/天 | `outbound_click` 日均 | W2 末 > 0；W4 末 ≥ 5/天 | =0 查埋点+提权是否生效 |
| 带佣按钮 CTR | 主 CTA click / 卡片 impression | ≥ 1.5% | <1% 改文案/锚点 |
| 深链占比 | `target_type=product` / 全部 | W3 末 ≥ 80% | 补 W3-T1 |
| 非搜索流量会话 | social+referral 会话 | W2 末 > 0 | 加 W2-T1 产量 |
| 收入 | 联盟后台 | 破冰 $20–50 | 见 §1 预期管理，**不用 $500 判失败** |

**判定线（附录 D 摘要）**：链接 CTR **≥2% = 高**（复制模式）；**<0.5% = 低**（改或换）；0.5–2% = 观察 1 周。

---

## 6. 升级 / 阻塞规则

- 卡 **>4h** → 记 `[BLOCKED]` 并升级（见 §0）。
- **数据异常**（点击突降 >50%）→ 先查埋点是否掉线，**24h 内**定位，未定位前不回滚内容。
- **合规红线触发**（误接 paid placement / 编造价格 / 3D 超范围）→ **立即停 + 回滚 + 记事故**，不议价。

---

## 7. 首月结束复盘模板（M1 收尾必交）

```
M1 复盘 — aitoptools
- 管道三件套：度量[✓/✗] 提权[✓/✗] 非搜索流量[✓/✗]
- 收入： $ __（破冰线 $20–50 是否达到：是/否；未达是否管道已通：是/否）
- 联盟点击/天（W4 末）：__
- 链接级 CTR 榜 v1：Top3 = __；Bottom3 = __
- 有效模式（M2 复制）：__
- 停止的渠道/动作：__
- 3D 范围核对：新增 3D 页 = 1？是/否
- M2 建议优先级（≤3 条）：__

```

---

## 附录 A — 命名规范
- `link_id` = `{slug}-{位置}`，例 `printful-review-cta1`、`printful-vs-printify-table-row1`。**全站唯一**。
- `merchant` = 小写品牌名，与 `AFFILIATE_PROGRAMS.md` 一致。
- `target_type` ∈ {`product`,`pricing`,`home`,`signup`}。

## 附录 B — 深链 URL 拼接规则
- 优先用联盟后台提供的 **deeplink generator** 生成（保留追踪参数）。
- 无生成器时：商户产品页 URL + 联盟参数 + UTM。**禁止**只链首页。
- 每个深链上线前**人工点开验证 200 且落到目标页**（非 404/非跳首页）。

## 附录 C — 价格锚点微文案模板
- 有真实价：`{price}/mo · {trial}` 例 `$9.99/mo · free plan`。
- 有折扣：`{off}% off · {code?}` 仅当商户公开活动时用。
- 无可靠数字：`See current deal ↗`（**不写数字**）。

## 附录 D — 一致性 & 判定校验（可脚本化）
- **winner 三一致**：vs-card 的 `winner` 字段 == 结论首句主语 == 对比表高亮行。任一不等 = fail（构建期 lint）。
- **空头维度**：卡片显示的评分维度名 ∈ 数据 schema 已填充字段集合；否则 fail。
- **CTR 判定线**：≥2% 高 / <0.5% 低 / 中间观察。

---

> **M3 开工第一步**：先做 **W1-T1**，做完打勾、在 `AFFILIATE_LOG.md` 记 `W1-T1 DONE @ {date}`，再开 W1-T2。**不要跳过 T1 去写内容或做分发。** 管道第一节没接上，后面灌的水都漏光。
## 2026-07-28 · 千问报告勘误 + M3 首月 Runbook 采用决议
- **采用** M3_MONTH1_RUNBOOK.md 为首月作战手册，KPI 护栏：管道三件套+破冰 $20-50（非 $500）；3D 限 1 篇；W1-T1 度量 P0。
- **填实**：M3_MONTH1_DATA.md（高佣 Top5 已获批商户、头部 16 页、商户×页面映射、16 pin 清单、W3-T2 对账）。
- **千问报告勘误**（K3 实测）："Printful vs Printify 未发布"/"best-ai-tools 死链"/"title 重复"/"CTA 无 href P0" 均不成立；唯一坐实 P0 = GA4 未装。`?fpr=partner` 失效链按 DATA 文件第三节补位。
- 周报 cron 已更新：加入 Runbook §5 五项判定线指标。

---

## 双引擎日志区（SEO+GEO，2026-07-28 增补 · 追加区块，勿覆盖上方原有日志）
写入约定：每周日随周报一起填；事件/阻塞仍记 `[BLOCKED W{n}-T{m}]` / `W{n}-T{m} DONE @ {date}`，本区只记"来源三分 + 双引擎结构进度 + 交叉榜结论"。

### C1 周记·来源三分 + GSC（每周日一行）

| 周 | 日期 | SEO 会话 | GEO 会话 | 社媒会话 | 联盟点击/天 | GSC non-brand 印象 | GSC non-brand 点击 | 备注 |
|---|---|---|---|---|---|---|---|---|
| W1 | ____ | — | — | — | __ | — | — | 埋点+提权周 |
| W2 | ____ | __ | __ | __ | __ | __ | __ | GSC 接入周；GEO 首现记 1 即达标 |
| W3 | ____ | __ | __ | __ | __ | __ | __ | SEO 应随 3 篇新文抬头 |
| W4 | ____ | __ | __ | __ | __ | __ | __ | 填交叉榜结论于 C3 |

### C2 双引擎结构进度

| 周 | 任务 | GEO 4 线达标率 | SEO 4 线达标率 | JSON-LD 0 error 页数 | GSC 验证 | spot check |
|---|---|---|---|---|---|---|
| W2 | W2-T4 | __% (≥80%) | __% (=100%) | __/16 | [✓/✗] | __/3 |
| W3 | W3-T2 | 3 篇全 4 线 | 100% | 3/3 | n/a | __/3 |

### C3 双引擎交叉榜结论（W4-T1 记，喂 M2）
- 来源×商家 CTR 最高组合：____
- 来源×坑位 CTR 最高组合：____
- 据此已落地的 ≥3 处改动：① ____ ② ____ ③ ____
- M2 双引擎输入：____

## 2026-07-28 · W1-T1 DONE（K3 线上验收通过）
- gtag G-248QMCT2S3 全站唯一注入 ✅；53/53 联盟链接 aff-link+UTM ✅；affiliate_click 事件 5 参 ✅（curl 抽查 mockey-review / printful-vs-printify 两页核实）。
- 事件名为 `affiliate_click`（非 runbook 原文 outbound_click）→ 用户 GA4 关键事件标记请用此名。
- 采纳新规：utm_campaign={merchant} 替代 m1（更利于分析），runbook 附录 A 待改注。
- 遗留小疵：post-build 注入链接 link_id=global-injected-{hash} 不可读 → 排 W1-T2 顺手修为 {slug}-{位置}。
- 待用户 GA4 后台：① affiliate_click 标为关键事件 ② 建链接点击探索报表。

---

## 2026-07-28 · affiliate-monitor cron 5 天回填 (Gmail 通道仍缺失 D6)
- **Gmail 通道**: 6 天空转,凭证未补,日更仍靠 state file + user 手动告知 (与 7/22 启动现状一致,本 cron 不自报"完成")
- **5 天 (7/24-7/28) 状态变更 (来源 AGENTS.md §5 + credentials.affiliate.local.json)**:
  - ✅ **approved (4 个, 7/24 同日 batch)**: Claid AI (FirstPromoter, 20% lifetime) / Printify (PartnerStack) / Printful (in-house, 10%×12) / (Looka 7/24 二次确认 declined-program-closed)
  - ❌ **declined-closed (1 个)**: Looka — partner program 已关闭,仅留 partnerships@looka.com 直邮,优先级低
  - 📤 **新增 3 申请 (7/24)**: Gelato (PartnerStack 重申, identity mismatch 已修复) / PartnerStack Network membership / Deel (挂网络下,批准后自动激活)
- **aging 风险 (D6)**:
  - 🔴 **Kittl 13 天** (7/15 首次,超阈值 6 天,卡 Impact 升级依赖) — user 拍板: 等升级 vs 走 in-house kittl.com/affiliates 绕道
  - 🔴 **Impact Marketplace Upgrade 10 天** (7/18 提交,超阈值 3 天,卡 Kittl/Placeit/Copy.ai/Canva/Shopify/Surfer/Bluehost 全部 Impact 系) — user 登录 app.impact.com 查看
  - 🟢 Gelato 重申 / PartnerStack Network / Deel = 4 天,正常窗口
- **建议立即动作 (user)**:
  1. **P0 解决 Gmail 通道**: 16-char App Password → F:\aitoptools\.hermes\secrets\gmail_credentials.json → 改 cron 通道 (per k3 memory 7/23 拍板)
  2. **P0 解决 Impact 卡**: user 浏览器登录 app.impact.com 查看 Marketplace 申请,或发邮件 follow-up 至 partner-support@impact.com
  3. **P1 Claid PayPal + Printful 邮箱确认**: user 浏览器手动,本 cron 不自动 (per AGENTS.md §7)
  4. **P1 3 链接激活**: Claid/Printify/Printful 走 python scripts/replace_affiliate_links.py --apply,需 user 拍板激活顺序 (建议 Printful 先, /printful-vs-printify/ 已有对比页,收益最快)
- **5 个 M3 评测候选 (7/22 入队)**: MockupHive/Packify.ai/Nightjar/Dynamic Mockups/Mintly 仍在 M3 gate review 队列,本 cron 不动
- **北极星指标**: $0/3000 (5 个月倒计时,剩 171 天) — 5 天来 0 收入,3 链接未上线 = 现金转化路径未启动

---

## 2026-07-28 20:32 · Kittl Impact 链接 user 主动提供 (待拍板)

- user 给链接: **https://kittl.pxf.io/qWNvPn** (Impact 标准 pxf.io 短链, 含义 = Kittl 已经在 Impact 侧拿到联盟 deep link)
- 现状: K3 7/28 5 天回填仍标 "Kittl 🔴 13 天卡 Impact 升级依赖" — 此 pxf.io 链接可能为以下 3 种:
  - (a) **已获批活链接** (Marketplace 升级已悄悄过, 链接提前可用) — **优先级最高**, 攒批时可立刻上
  - (b) **临时 shortlink** (Impact 自动给申请中的账户生成的 tracking 占位, 获批后会自动绑定) — 可先用, 但 commission 状态待确认
  - (c) **其他渠道直签** (如 in-house kittl.com/affiliates 申请已通过) — 与 Marketplace 升级解耦
- 本 cron 不动 reviews.json / inject-aff-link.mjs (今天 8 push + partnerships 紧急修复 1 push = 9 破例, 攒批等明天 reset)
- **建议**:
  1. user 浏览器打开 https://kittl.pxf.io/qWNvPn 跳到 Kittl 哪个页面 (pricing? signup? home?) — 记下来
  2. user 登录 app.impact.com 看 "Partnerships / Campaigns" 里 Kittl 状态 (Approved? Pending? Inactive?) — 决定是 (a)/(b)/(c) 哪种
  3. 拍板后: W1-T2 攒批时一起替换 Kittl 的 7 处 Check Deal (3 详情页 + 2 卡片 + 2 内链) + inject-aff-link.mjs 加 impact 短链 pattern + affiliateUrl 字段从 reviews.json 66 条里找 Kittl 工具 (3 条: kittl / kittl-vs-* / 等)
- **预估激活收益**: Kittl 是高佣 SaaS 设计工具 (30% 循环 假设), 跟 Mockey 同档, 替换 7 处 → 跟 Mockey 当前 5 处量级一致 → 长期 CTR 收益可类比 Mockey (10-15 clicks/周 baseline)
