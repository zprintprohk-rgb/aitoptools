# M3 首月 Runbook · 真实数据填充版（K3 填实，2026-07-28）

> 配套 `M3_MONTH1_RUNBOOK.md` 使用，替换其中所有 ______ 与"按文件排"占位。
> 数据来源：`AFFILIATE_PROGRAMS.md` + `credentials.affiliate.local.json` + src/data 实际页面。**未获批商户一律不用真实追踪链**。

## 一、W3-T1 高佣商户名次（已获批·有真链接，按 EPC 降序）

| 名次 | 商户 | 条款（真实值） | 追踪链 | 平台 |
|---|---|---|---|---|
| 1 | **Mockey** | **30% 循环** | `mockey.ai?via=jerome796` | Endorsely |
| 2 | **Creative Fabrica** | 25% 首购 + **20% 循环无上限**，Cookie 90 天 | `creativefabrica.com/ref/27832838/` | in-house |
| 3 | **Claid** | **20% 终身循环**，起付 $20 | `claid.ai?via=jerome94` | FirstPromoter |
| 4 | **Printful** | 履约 10%×12 月 + Growth 订阅 $25/单 | `printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a` | in-house |
| 5 | **Printify** | 销售额 5%×12 月，Cookie 90 天 | `try.printify.com/4fs863rfz2yc` | PartnerStack |

**待激活（获批后按此顺位插队）**：Deel $1500/单（B2B 场景页专用）＞ Placeit $50/年订阅（Impact 待批）＞ Kittl 20%×12 月（Impact 待批）＞ Gelato 最高 12%（PartnerStack 重申待批）。

## 二、头部 16 篇内容清单（W2-T1 pin 映射 + W3-T1 深链落点）

**6 对比页**：printful-vs-printify / printify-vs-gelato / printful-vs-gelato / kittl-vs-placeit / kittl-vs-canva / mockey-vs-placeit

**10 评测页**：mockey-review / creative-fabrica-review / claid-ai-review / printful-review / printify-review / placeit-review / kittl-review / gelato-review / mockuphive-review / photoroom-review

## 三、商户 × 头部内容映射（W3-T1 照单执行）

| 头部页 | 必挂高佣链（名次） | 备注 |
|---|---|---|
| mockey-review / mockey-vs-placeit | Mockey(1) 已有真链 ✅ | Placeit 侧占位链待 Impact |
| creative-fabrica-review | CF(2) 已有 ✅ | 补 1 个具体素材分类页深链 |
| claid-ai-review | Claid(3) 已有 ✅ | 深链指 pricing 页 |
| printful-review / 全部 POD 对比页 | Printful(4) 已有 ✅ | 对比页补 Printful 定价页深链 |
| printify-review / printful-vs-printify / printify-vs-gelato | Printify(5) 已有 ✅ | — |
| placeit-review / kittl-vs-placeit | Mockey(1) 补位 + Placeit 待批 | 获批后换真链 |
| kittl-review / kittl-vs-canva | CF(2) 补位 + Kittl 待批 | 获批后换真链 |
| gelato-review / 2 篇 gelato 对比 | Printful(4)+Printify(5) 补位 + Gelato 待批 | 获批后跑替换管线 |
| mockuphive-review | Mockey(1) 补位 | MockupHive 无联盟时挂 Mockey |
| photoroom-review | Claid(3) 补位 | Photoroom `?fpr=partner` 为失效链，Awin 重签后排期 |

**深链拼接红线**：一律用各平台后台 deeplink generator 或「产品页 URL + 已有追踪参数」，**禁止编造 URL 格式**；上线前人工点开验证 200 且落到目标页（runbook 附录 B 原规则）。

## 四、W2-T1 的 16 张 pin

直接用上方 16 页清单：每页 1 张 1000×1500 竖版 pin，标题=页标题，主体=胜方徽章+一句结论，底部 aitoptools.net，描述含目标关键词 + UTM `?utm_source=pinterest&utm_medium=pin&utm_campaign=m1`。首周 16 张，之后每周 +5。

## 五、W3-T2 三篇高意图新文 · 对账结论

1. `Best AI Product Photography Tools for POD (2026)` — **新建**（榜单结构复用 printful-alternatives 模板）
2. `Printful vs Printify 2026` — **已存在 → 只做优化**：补深链 + 主 CTA 提权 + 核对 winner 三一致，**禁止重写**
3. `Best Mockup Generator for Etsy Sellers (2026)` — **新建**，Mockey 为主推（30% 循环最高佣）

## 六、千问报告勘误（K3 实测，防止 M3 被带偏）

- ❌ "Printful vs Printify 未发布" → 实际已上线 200
- ❌ "页脚死链 /best-ai-tools/" → 实际 200 正常
- ❌ "全站 title 重复" → 抽查首页/about/compare 均唯一
- ⚠️ "CTA 无 href 37 页" → 首页 128 个 CTA 全部有 href；个别老评测页需抽查，**非 P0**
- ✅ 唯一坐实的 P0：**GA4/点击度量全站未装**（W1-T1 必须最先做）
- ⚠️ `?fpr=partner` 失效链确实存在（Placeit/Photoroom 系），按本文件第三节补位方案处理

## 七、三个护栏（用户拍板，M3 违反即停）

1. 首月 KPI = **管道三件套 + 破冰 $20–50**，不是 $500
2. 3D 桥接只 **1 篇 + 5 内链**，多 1 篇即违规
3. **W1-T1 度量是 P0**，不许跳过去先写内容
