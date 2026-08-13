# Boost Tracking — aitoptools 推排名作战记录 (2026-08-08 启动)

> 策略依据: GSC 真实数据 (6/28-8/5, 427 query): 收录已启动 (日均 200 展示) 但排名 60-90 → CTR 0.15% → **从"扩内容"切换"推排名"** (25 个 Boost 候选)

## 四杠杆 SOP (每页统一 5 步)
1. **内链强化**: hub 页 + 2-3 个相关 spoke 页加锚文本 (变体锚)
2. **内容补强**: BLUF 首段 (前 50 词答意图) + 数据锚点 (≥1 表格) + FAQ ≥3 (信任型 ≥5) + 更新日期
3. **Schema 更新**: Article + FAQPage (faqs 字段自动渲染) — 随 reviews.json 自动
4. **IndexNow 重推**: 更新后 30 分钟内推送
5. **验证记录**: 优化前排名 → T+7 对比 → 本表更新

## Boost Queue 执行状态 (2026-08-08 快照)

| # | 页面 | 展示 | 优化前排名 | 目标 | 状态 | 优化日期 | T+7 排名 |
|---|---|---|---|---|---|---|---|
| 1 | /stickermule-review/ | 179 | 35.1 | ≤15 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 待 8/15 对比 |
| 2 | /runway-ml-review/ | 201 | 63.0 | ≤20 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 待 8/15 对比 |
| 3 | /blog/is-magicdrop-legit/ | 33 | 64.6 | ≤20 | ✅ DONE 8/13 (8/11 排期错过→补执行; FAQ5+引用链+内链4) | 8/13 | 待 8/21 对比 |
| 4 | /blog/print-price-ai-tools-2026/ | 26 | 69.5 | ≤30 | ✅ DONE 8/13 (对比表+引用链3+内链4+Schema; 8/21 ≤30) | 8/13 | 待 8/21 对比 |
| 5 | /kittl-review/ | 49 | 59.7 | ≤40 | 队列 | - | - |
| 6 | /gempages-review/ | 80 | 47.8 | ≤35 | 队列 | - | - |
| 7 | /bluehost-review-2026/ | 14 | 63.7 | ≤45 | 队列 | - | - |
| 8 | /mockey-review/ | 8 | 51.1 | ≤40 | 队列 | - | - |
| 9 | /gelato-review/ | 6 | 40.5 | ≤35 | 队列 | - | - |
| 10 | /placeit-review/ | 6 | 68.8 | ≤45 | 队列 | - | - |

## 北极星指标 (8/8 基线 → 8/14 T+7 → 8/31)
| 指标 | 当前 | T+7 目标 | 8/31 目标 |
|---|---|---|---|
| 日均展示 | ~200 | ≥200 | ≥300 |
| CTR | 0.15% | ≥0.3% | ≥1% |
| 日均点击 | ~0.3 | ≥1 | ≥5 |
| Boost 完成 | 2/25 | 4/25 | 10/25 |
| 联盟 payout-ready | 1 (Printful 税审中) | 2 | 3 |

## T+7 决策树 (8/14 启用)
- 展示持续增长 + Boost 页排名有移动 → 策略正确, 每天 Boost 1 页, 3 周清完 25
- 展示持平 + 排名不动 → 查内链/Schema, 补外部信号 (Pinterest/社交)
- 展示下降 <150 → 紧急排查 robots/sitemap/算法
- 新 query 展示≥5 无页 → Data-Driven Queue, 建页节奏 ≤2 页/周


## 升级 v2 (2026-08-08 首战复盘, 千问 3.8 策略)
### 内链最低标准 (#3 起, 每页 4 条)
1. Hub 页 (首页/工具分类页) → 目标页 (主锚文本)
2. 同品类 spoke A → 目标页 (交叉引用)
3. 同品类 spoke B → 目标页 (对比引用)
4. 最新博文/评测 → 目标页 (新鲜度信号)
锚文本: 变体锚, 禁完全匹配 (sticker mule alternatives / compared to X / vs X)

### GEO 嵌入检查清单 (每页必做 8 项)
□ BLUF 首段 (前 50 词直接回答)
□ ≥1 数据表格 (AI 可摘引)
□ FAQ ≥3 (信任型 ≥5)
□ FAQPage JSON-LD
□ Article Schema (author + dateModified 当天)
□ 引用链 (≥1 外部权威来源 cite)
□ llms.txt 包含该 URL
□ robots.txt AI 爬虫段完好

### 页面类型 × 补强重点
| 类型 | 重点 | 示例 |
|---|---|---|
| 评测型 | 数据表 + verdict BLUF | sticker-mule / runway-ml (已完成) |
| 信任型 | FAQ≥5 + 用户评价 + 退款政策 | is-magicdrop-legit (#3) |
| 价格型 | 实时对比表 + 更新日期 + 计算逻辑 | print-price (#4) |
| 替代型 | 对比矩阵 + 场景分流 | midjourney/jasper alternatives (#5/#6) |

### 排期更新 (v2)
| # | 页面 | 优化前排名 | 排期 | 动作 |
|---|---|---|---|---|
| 3 | /blog/is-magicdrop-legit/ | 64.6 | 8/11 | 信任 FAQ≥5 + 引用链 + 内链≥4 |
| 4 | /blog/print-price-ai-tools-2026/ | 69.5 | 8/13 | 对比表 + 内链 + Schema (8/21 ≤30) |
| 5 | /midjourney-review/ | 84.6 | 8/17 | 对比矩阵 (替代型) | DONE 8/17 (内容深度+引用链3+内链6+FAQ5+schema; IndexNow 2/2)
| 6 | /jasper-ai-review/ | 91.5 | 8/17 | 对比矩阵 (替代型) | DONE 8/17 (内容深度+引用链3+内链6+FAQ5+schema; IndexNow 2/2)

### 北极星指标 (T+14 目标加入)
| 指标 | 基线 8/8 | T+7 (8/14) | T+14 (8/22) |
|---|---|---|---|
| 日均展示 | ~200 | ≥200 | ≥220 |
| CTR | 0.15% | ≥0.2% | ≥0.3% |
| 日均点击 | ~0.3 | ≥0.5 | ≥1 |
| Boost 完成 | 2/25 | 4/25 | 6/25 |
| 首批排名移动 | — | 可测量 | ≥5 位 = 策略有效 |

### 8/22 验证分支 (提前规划)
- Branch A 排名移动 ≥5 位 → 四杠杆有效 → 每天 1 页, 9/5 前清完 25 → 开始 10-20 区间 title/meta 精修
- Branch B 移动 1-4 位 → 保持节奏 + 外部信号 (Pinterest/社交) + Guest Post/论坛外链 (POD 社区)
- Branch C 无移动 → 排查: GSC URL Inspection 请求重爬 + SSR 确认锚文本 + 外部信号 (Reddit/Quora + pin)
- Branch D 排名下降 → 疑似过度优化 → 减内链密度查堆砌 → 暂停 Boost 2 天

## 8/13 执行记录 (daily-search; T3 补执行 + T6)
- **T3 is-magicdrop-legit (原排 8/11, cron 凭证故障错过 → 8/13 补执行)**: dateModified→8/13; 引用链 +1 (Afternic 官方 listing 验证链); 内链 +4 (printify-alternatives hub / printful-review / printify-review / fyul blog); FAQ 5 (达标); FAQPage+Article Schema 自动渲染核验 PASS (构建产物确认)
- **T6 print-price-ai-tools-2026**: dateModified→8/13; 引用链 +3 (Printify/Printful/Gelato 官方 pricing 页); 内链 +4 (print-on-demand-companies hub / printful-vs-printify blog / printify-vs-gelato compare / claid review); 对比表已有 1; FAQ 5; 死链修复: related 中 /best/ai-tools-for-pod-pricing/ + /best/ai-tools-for-pricing-strategy/ (404) → 换成真实页面
- 副产品修复: reviews.json 10 处 chr(8594) 字面量 bug (CTA 箭头显示为文本) → 替换为 →
- 本地构建: npm run build PASS; out/ 产物 11/11 页含新链接/Schema 核验 PASS
- IndexNow: 4 URL 推送 4/4 HTTP 200 (8/13 19:2x)
- T+7 对比: #1/#2 → 8/15; #3/#4 → 8/21 (与 #4 8/21 里程碑合并读)

## 8/14 T+7 首读记录 (daily-search; 正式读数 = .hermes/reports/t7-reading-2026-08-14.md, weekly-review cron 05:3x 产出)

- **读数窗口**: GSC API 实时 7d 8/7-8/13 (T+2 → 有效至 8/11); 日均展示 **216.5** (vs 基线 ~197, +10%)
- **决策**: **Branch A (加速·温和版)** — 展示 ≥200 且多数目标页位置改善 (print-price +4.0 / magicdrop +2.1 / manychat +6.6 / printify-alternatives +1.9); 点击仍 0 (深度排名期常态)
- **告警项**: kittl review 哨兵 68.5→74.0 (-5.5) → 8/14 专项诊断: 低量噪音 (7 imp/28d) + 3 项 GEO 缺口, 见 kittl-diagnosis-0814.md; copy ai review -7.5 → 8/16 B 类快修候选
- **窗口说明**: 本读数基本不含 Boost 效果 (内容 8/13 上线, T+1~2 延迟) — 属 Boost 前基线确认 + 监控起点; #1/#2 严格 T+7 = **8/15**; #3/#4 T+7 = 8/21 (与 print-price ≤30 里程碑合并)
- **风险开关**: 8/15-8/16 大面积下滑 ≥10 位 → Branch D (紧急审计 + 暂停 Boost 2 天)