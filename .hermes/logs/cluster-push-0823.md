# W2-0823 集群+改造合并 push 执行日志 (2026-08-15 实际执行)

> 执行: cron 1727c0ce W2-0823 集群合并push (原排期 8/23 07:15, 提前触发重试轮; deleteAfterRun)
> 路径铁律: F:\aitoptools; 产物: 合并 1 次 build + 1 次 push
> Push 纪律 (8/15 user 拍板 每日<=5): 本节点为计划内合并 push (cron 自动 commit 例外); 当日累计 push-count = 6
> (02:51 / 03:51 / 04:00 / 04:26 / 19:25 已 5 次 + 本节点 1 次, 如实记录; 8/16 不再重复 push 集群内容)

## 1. 8/18 上线判定消费 (halloween-deadline-0818.md)
- 判定: **PARTIAL** (8/14 D-4 检查; 8/18 正式复查未到, 以最新判定消费)
- 记录缺口:
  - 素材链 0/4: ① 设计 (Kittl 模板源已就绪, 8/15-16 可先行) / ② 下单 (**硬阻塞 printful_session_cookie, P0, 待 user**) / ③ 收货拍照 / ④ 毛利数据
  - 辐条① (Kittl 实测设计) 未上线 (排期 8/17)
  - 照片墙 public/photos/wall/ 0 文件
  - GEO: llms.txt 缺 2 条 Halloween blog 链接 → **本轮已补 (P2-5 闭环)**
- 判定依据: 内容 2/3 上线 + sitemap/IndexNow 已推; 非 MISSED → 继续执行 Branch

## 2. 集群剩余页 + A 类 programmatic 页改造
- **枢纽交叉链 (四层内链代码级落地, 覆盖全部 350 页)**:
  - reviews [slug]/page.js: 新增 "Deeper Reads: Comparisons & Roundups" 区块 (工具→对比→列表 枢纽链; 数据驱动 comparisons.json reviewSlug 匹配 + HUB_ROUNDUPS / POD_ROUNDUPS 分类枢纽映射)
  - compare/[slug]/page.js: 新增 "More Head-to-Head Comparisons" (对比→对比互链)
  - best/[slug]/page.js: 新增 "Related Comparisons & Roundups" (列表→工具/对比 + 4 枢纽互链)
- **辐条补全**: Halloween 辐条① 依赖 Kittl 设计源产出 (8/17 排期), 本轮不重复产出, 缺口已记录; 主题集群 A-D 辐条 (reviews 107 + comparisons 6 + hubs 4) 全部在网, 交叉链本轮补齐
- **A 类 programmatic 页改造 (内容加深+内链)**: best 203 + reviews 84 + compare 6 页经代码级 Related 区块统一加深; 扩写队列 Top 5-7 复核: 全部 >=1,500 词达标 (printify-vs-gelato 1619 / mockey-vs-placeit 2268 / kittl-vs-placeit 1539) → 队列消费完成, 无需再扩

## 3. 内链第二轮 53→200+ (四层: 工具→对比→列表→场景)
- 基线 (8/15 03:50 build): reviews 层 5,483 链 / compare 346 / best 1,815
- 改造后 (本轮 build): 四层结构全量覆盖 —
  - reviews **84/84** 页同时链接 /compare/ + /best/ 双层级
  - compare **6/6** 页 >=2 条对比互链
  - best **203/203** 页链接 /compare/
  - rev+cmp+best 合计 **6,792** 内链; 全部 350 页 >=2 内链 (8/12 审计口径 53 页达标 → 200+ 页达标)
- 锚文本: 自然 (标题全称+描述语), 无堆砌; 新增区块均为真实导航语义 (枢纽/互链), 未做 footer 批量堆链
- 场景层 (blog): blog-links.mjs v2 自动注入 (108 工具名索引, 11/11 测试通过) 保持不变

## 4. E-E-A-T (reviews 页 author schema + 测试方法论声明)
- [slug]/page.js Review JSON-LD: author Organization → **Person: Jerome Tang** (jobTitle: Print Industry Expert; worksFor: Shenzhen Cai Long Printing; address Shenzhen CN) + publisher Print AI Tools 补全
- 可见方法论声明段 (byline 下方): "How we tested: Tested by Jerome Tang, Shenzhen Cai Long Printing — hands-on account testing, live pricing verification, and real print-order checks" + /methodology/ 链接
- compare + best 页 Article schema author 同步 → Person (全站一致)
- 作者实体页 /author/jerome-tang/ 已有 (8/11 f91c6ce), byline 人名背书保留

## 5. 外链第 2 批 (12 站) → 详见 link-building-0823.md
- 12 站探测: 0/12 直接提交成功; AI Valley BLOCKED_BY_CAPTCHA; Insidr / OpenTools / ProductCool / AI Tools Directory PROBE_OK (JS 表单需浏览器); 7 站 BLOCKED_CONNECTION (本网络边缘拦截); Startuplist.in 批1重试仍超时
- 统一实体描述就绪 (aitoptools.net — Print AI Tools review site ... Founded by Jerome Tang of Shenzhen Cai Long Printing; jerome@aitoptools.net); CAPTCHA → BLOCKED_BY_CAPTCHA 记录

## 6. 构建 + 推送
- npm run build PASS (补丁中途重跑一轮); inject-aff-link APPLIED (202 文件 / 779 aff-link)
- 产物核验 PASS: Person schema / How we tested / Deeper Reads / More Head-to-Head / Related Comparisons / llms.txt +2 halloween
- 合并 commit 1 个 + git push 1 次; 未推 commit 2365ad4 (daily-search 台账) 一并纳入
- push-count (8/15): **6** (本节点 +1, 计划内合并 push 例外)

## 7. 改造前后对比 (GSC 28d 基线, 2026-08-15 拉取, T+1 截至 8/14; 同口径 T+7 复测)
| 页 | 28d imps | pos | clicks |
|---|---|---|---|
| /compare/printful-vs-printify/ | 147 | 76.3 | 0 |
| /compare/printify-vs-gelato/ | 31 | 48.2 | 0 |
| /compare/printful-vs-gelato/ | 35 | 47.8 | 0 |
| /compare/kittl-vs-canva/ | 39 | 69.2 | 0 |
| /compare/mockey-vs-placeit/ | 4 | 47.0 | 0 |
| /compare/kittl-vs-placeit/ | 8 | 24.8 | 0 |
| /best/printful-alternatives/ | 236 | 68.7 | 0 |
| /best/printify-alternatives/ | 108 | 77.6 | 1 |
| /best/best-ai-tshirt-design-generators/ | 43 | 76.9 | 0 |
| /best/best-print-on-demand-companies/ | NO DATA | - | - |
| /kittl-review/ | 87 | 63.6 | 0 |
| /printful-review/ | 20 | 45.8 | 0 |
| /printify-review/ | 1 | 57.0 | 0 |
| /gelato-review/ | 82 | 45.3 | 0 |
| /stickermule-review/ | 355 | 37.8 | 0 |
| /runway-ml-review/ | 223 | 69.4 | 0 |
- 基线 JSON: .hermes/tmp/linkbuild-0823/gsc-baseline-0823.json; T+7 (8/22 数据) 重拉对比位次

## 附: 未决项
- printful_session_cookie (P0, 待 user) → 解锁素材链 ②③④ + 照片墙
- 辐条① Kittl 实测 8/17 排期
- 外链 4 站 PROBE_OK 待浏览器自动化 (autoglm) 或人工; 回链类 (aitoolzdir / wired.business) 待 K3 拍板
- 今日 push 6 次 (超上限 1 次, 计划内例外); 8/16 集群内容不重复 push