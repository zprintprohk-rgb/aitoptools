# T13 记分卡 v0 抽样核验报告 (scorecard-sample-audit-0812)

> 核验时间: 2026-08-12 12:22 (GMT+8) | 台账: `.cluster/programmatic-audit-0813.json` (117 页) | 抽查 10 页 (A×2 + B×6 + C×2, 覆盖全部 8 个指定 slug)
> 评分标准 (v0): title 含目标词 + H1/title_ok + 正文≥800 词 + 内链≥2 + FAQ schema + CTA affiliateUrl; A≥5 / B=3-4 / C≤2

## 一、10 页核对表

| slug | 类型 | v0 评分 | 实际评分 | wc (v0→实) | 内链 (v0→实) | faqs (v0→实) | aff (v0→实) | kw (v0→实) | 判定 |
|---|---|---|---|---|---|---|---|---|---|
| kittl-vs-placeit | comparison | 5A | 6A | 1532→1532 | 4→4 | 7→7 | False→True | True→True | ❌ 误判 |
| kittl-vs-canva | comparison | 5A | 6A | 1757→1757 | 4→4 | 6→6 | False→True | True→True | ❌ 误判 |
| printful-alternatives | listicle | 3B | 6A | 0→1915 | 0→5 | 7→7 | False→True | True→True | ❌ 误判 |
| printify-alternatives | listicle | 3B | 6A | 0→1925 | 0→4 | 7→7 | False→True | True→True | ❌ 误判 |
| mockey-vs-placeit | comparison | 4B | 5A | 2234→2234 | 0→0 | 7→7 | False→True | True→True | ❌ 误判 |
| jasper-ai-review | review | 4B | 4B | 145→145 | 0→0 | 5→5 | True→True | True→True | ✅ 一致 |
| printful-review | review | 4B | 4B | 204→204 | 2→2 | 5→5 | False→False | True→True | ✅ 一致 |
| seede-ai-review-2026 | review | 4B | 3B | 863→863 | 0→0 | 0→0 | True→False | True→True | ❌ 误判 |
| removebg-review | review | 2C | 2C | 114→114 | 0→0 | 5→5 | False→False | False→False | ✅ 一致 |
| dalle-review | review | 1C | 1C | 698→698 | 0→0 | 0→0 | False→False | False→False | ✅ 一致 |

## 二、误判清单 (抽样 10 页内)

### 等级翻级 (grade flip) — 3 页

| slug | v0 | 实际 | 原因 |
|---|---|---|---|
| printful-alternatives | 3B | 6A | **wc=0 假象**: listicle 无顶层 `content` 字段, 正文在 introContent+items[].content+closingContent, 实为 1915 词; 内链实为 5 条; items 有 7 个 CTA (ctaUrl, 其中 2 个带 affiliate 追踪) → aff=True |
| printify-alternatives | 3B | 6A | 同上: 实 wc=1925, 内链 4, CTA×7 (2 带追踪) |
| mockey-vs-placeit | 4B | 5A | comparison 的 affiliateUrl 嵌套在 toolA/toolB 内 (mockey.ai?via=jerome796 + placeit.net/?fpr=partner), v0 只查顶层字段 → aff 漏判 False→True |

### 分数级误判 (metric miss, 等级不变) — 3 页

| slug | v0 | 实际 | 原因 |
|---|---|---|---|
| kittl-vs-placeit | 5A | 6A | toolA/toolB 均有真实 aff URL (kittl.pxf.io/qWNvPn, placeit.net/?fpr=partner) → aff 漏判 |
| kittl-vs-canva | 5A | 6A | 同上 (kittl.pxf.io/qWNvPn, canva.com/?fpr=partner) → aff 漏判 |
| seede-ai-review-2026 | 4B | 3B | affiliateUrl=`#` 占位符被 v0 当 aff=True (假阳性); 实为无真实 affiliate CTA → aff 应为 False |

### 边缘/可疑但等级一致 — 4 页

| slug | v0 | 实际 | 说明 |
|---|---|---|---|
| jasper-ai-review | 4B | 4B | wc=145 为真实 (content 确实短); 1 条外链 CTA (jasper.ai, 单引号 href) 不满足内链≥2; v0 判 links=0 可接受 |
| printful-review | 4B | 4B | affiliateUrl 字段为空但 content 内含 1 条真实 affiliate 链接 (printful.com/a/152976…cc4a CTA); 若按"页面存在 affiliate CTA"计则应为 5A — 属标准口径问题, 非解析 bug |
| removebg-review | 2C | 2C | kw_ok=False 属标点变体误判: title 含 "Remove.bg" 但 slug 词 "removebg" 无点; 建议 kw 匹配容忍 . - 空格变体 |
| dalle-review | 1C | 1C | 同上: title 含 "DALL-E 3" vs slug "dalle"; affiliateUrl 与 visitUrl 相同 (非 affiliate 直链), aff=False 合理 |

## 三、全量 117 页量化影响 (修正口径重算)

修正口径: wc 按类型解析 (listicle 用 intro+items+closing); 内链=href 以 `/` 开头 (单/双引号都算); aff=review 顶层非空且≠`#`且≠visitUrl / comparison 查 toolA/toolB.affiliateUrl+visitUrl 追踪参数 / listicle 查 items[].ctaUrl; kw 容忍 . - 空格变体。

- 全量受影响页: **29/117** (评分或等级与 v0 不同)
- 等级翻级 15 页:
  - **4 页 B→A** (listicle 全部): printful-alternatives, printify-alternatives, best-ai-tshirt-design-generators (实 wc=849, 内链2), best-print-on-demand-companies (实 wc=1043, 内链9)
  - **1 页 B→A**: mockey-vs-placeit (aff)
  - **10 页 B→C** (-2026 批 affiliateUrl=`#` 假阳性): playht-review-2026, topaz-photo-ai-review-2026, pebblely-review-2026, gorgias-ai-review-2026, wix-ai-review-2026, grammarly-business-review-2026, fliki-ai-review-2026, squarespace-ai-review-2026, bluehost-review-2026, reconvert-upsell-review-2026
- 分数级修正 14 页 (等级不变): 6 个 comparison 页 aff False→True (5A→6A×5, printful-vs-printify 靠 visitUrl 追踪参数); 9 个 -2026 review 4B→3B (`#` aff 假阳性)

## 四、系统性 bug 清单 (v0 根因)

| # | Bug | 影响面 | 证据 |
|---|---|---|---|
| B1 | **listicle 无 `content` 字段 → wc=0** | 4/4 listicle 全中 | 真实内容在 introContent / items[].content / closingContent; 4 页实 wc 849-1925, v0 全记 0 |
| B2 | **comparison aff 只查顶层, 未查 toolA/toolB.affiliateUrl** | 6/6 comparison | 5 页 tool 层有真实 aff URL; 1 页 (printful-vs-printify) visitUrl 含 /a/ 追踪参数; v0 全判 False |
| B3 | **affiliateUrl=`#` 占位符判为 aff=True** | 20 页 (-2026 批) | seede/vestia/sloap/imagetostl/aisvg/alttextgenerator/playht/siteground/tome/packhelp/topaz/pebblely/gorgias/wix/grammarly/fliki/squarespace/bluehost/reconvert/gear-launch 共 20 页 au=`#`; 其中 10 页因此被虚高为 B |
| B4 | **内链解析疑似只认双引号 + 内链口径** | 至少 4 页 | best-print-on-demand-companies 9 条单引号内链 v0=0; jasper 单引号外链 CTA 漏计 (无害); seede 2 条 href=`#` 占位被 v0 计 0 (正确) — 建议统一: 内链=以 `/` 开头, 单双引号都算, 排除 `#`/空串 |
| B5 | **kw 标点变体误判** | 5 页 v0 kw=False | Remove.bg / DALL-E 3 / Sticker Mule / Play.ht / GearLaunch (gearlaunch 明确应为 True, 其余为边缘) |

## 五、修正建议 (v1)

1. **listicle 解析**: wc 取 introContent + Σ items[].content + closingContent (去 HTML); 内链、kw 同样作用于此文本; aff 取 items[].ctaUrl 非空 (建议同时标记带追踪参数的条数)
2. **comparison aff**: 查 toolA/toolB.affiliateUrl 非空 OR visitUrl 含追踪标记 (pxf.io / ?fpr= / via= / /a/ / aff_ / ref)
3. **aff 白名单净化**: 排除 `#`、空串、等于 visitUrl 的直链; `#` 应记 False 并在台账标注 "placeholder"
4. **内链口径**: 仅 href 以 `/` 开头 (站内), 单双引号都解析; 排除 `#` 与空 href; 外链 CTA 不算内链
5. **kw 匹配**: slug 词去除 -review/-alternatives/-2026 后缀后, 与 title 做 去连字符/去点/空格 三种变体匹配
6. **台账补充**: 每页记录 type 字段 (review/comparison/listicle), 便于按类型回归

---
核验数据源: src/data/reviews.json (107) + comparisons.json (6) + listicles.json (4) = 117 页, 与台账一一对应。