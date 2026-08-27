# Schema 覆盖审计 — 2026-08-28（二期战略 S6）

> 触发: cron「Schema 覆盖审计」(9dcdde69) · 执行: isolated session
> 数据来源: ① 直接读取 5 个审计目标源文件 ② src/ 全量 ld+json emitter 扫描（node 脚本）③ reviews.json 全字段 JSON.parse + /&(?!amp;)/g 遍历实扫 ④ npm run build 实跑输出
> 幂等: 执行前检查 .hermes/logs/schema-audit-2026-08-28.md 不存在 → 正常执行

## 一、覆盖矩阵（页面类型 × Schema 类型 × 实体完整性）

| 页面模板 | Schema 类型 | Organization (name/url/logo) | Author Person (name/url) | 判定 |
|---|---|---|---|---|
| src/app/layout.js（全局布局层） | Organization | ✓ / ✓ / ✓ | —（按规范不在此层） | PASS 原有 |
| src/app/[slug]/page.js（107 条 Review） | Review + BreadcrumbList + FAQPage | publisher name ✓ / url ✓ / logo ✗→✓ 已补 | author name ✓ / url ✗→✓ 已补（含 worksFor 结构） | 缺口→已修复 |
| src/app/blog/[slug]/page.js（20 篇） | Article + FAQPage + BreadcrumbList | publisher name ✓ / url ✓ / logo ✓ | author name ✓ / url ✗→✓ 已补 | 缺口→已修复 |
| /about | 无页面级 JSON-LD，继承布局层 Organization | ✓（布局层注入确认） | — | PASS |
| /methodology（+ /methodology/legit-ratings） | 无页面级 JSON-LD，继承布局层 Organization | ✓（布局层注入确认） | — | PASS |
| /author/jerome-tang | Person + Organization | — | ✓ 原有 | PASS 原有 |
| /best + /best/[slug] | CollectionPage / Article / ItemList / Person / Organization / BreadcrumbList / FAQPage | ✓ | ✓ | PASS 原有 |
| /compare + /compare/[slug] | CollectionPage / Article / Person / Organization / BreadcrumbList / FAQPage | ✓ | ✓ | PASS 原有 |
| /category/[slug] | CollectionPage + ItemList | 继承布局层 | — | PASS 原有 |
| /best-ai-tools | ItemList + ListItem | 继承布局层 | — | PASS 原有 |
| /（首页） | WebSite | 继承布局层 | — | PASS 原有 |
| /promo/printify-promo-code | FAQPage + BreadcrumbList | 继承布局层 | — | PASS 原有 |

结论: Organization 实体（name/url/logo）确认在布局层 layout.js 注入，全站每页（含 about/methodology）均有输出；Author 实体在 Review/Article 页缺失 url 属性，本次补齐。

## 二、修复清单（改前均已备份）

1. src/app/[slug]/page.js
   - Review.author Person 补 `url: 'https://aitoptools.net/author/jerome-tang/'`（/author/jerome-tang/ 路由已确认存在）
   - Review.publisher Organization 补 `logo: { '@type': 'ImageObject', url: 'https://aitoptools.net/og-image.png' }`
   - reviewRating 保持原样；未新增 aggregateRating（遵守「Review 页保持 reviewRating」约束）
2. src/app/blog/[slug]/page.js
   - Article.author Person（AUTHOR 常量）补 `url: 'https://aitoptools.net/author/jerome-tang/'`
3. src/data/reviews.json 裸 & 清理（文本字段 & → &amp;，URL 字段除外）
   - 任务预期 22 处 → 实扫 27 处裸 &（其中文本字段 23 + URL 字段 4）；以实扫为准全清文本字段，与预期差 1 处如实记录
   - 明细: notion-ai-review 3（pros[1] / cons[2] / faqs[3].a）· best-ai-writing 对比页 10（faqs[0-4].q/a）· stickermule 3（faqs[2].a ×2 / faqs[4].a）· nordpass 4（pros[3] / faqs[2].a ×2 / faqs[4].a）· printreadybook 3（faqs[2].a ×2 / faqs[4].a）· nordvpn 0（仅 URL）
   - URL 字段保留 4 处不转义: nordvpn affiliateUrl ×2（go.nordvpn.net aff_c 参数）· nordpass affiliateUrl ×2（go.nordpass.io aff_c 参数）
   - 技术注记: 整文件 JSON 重序列化与原文件字节不一致（原文件含 \u2014 转义序列，RT_DIFF_AT=264534），故弃用 stringify 整写，改用「精确转义值原文替换」，原格式零破坏

## 三、校验结果

- 补丁 marker 复核: 3/3 命中（author_url_review / publisher_logo_review / author_url_blog 全 true）
- reviews.json 复检: 重新 parse 有效，text_bare=0，url_bare=4（符合预期 0/4）
- 字节差验证: 609167 → 609259 = +92 = 23 处 × 4 字节，证明无其他改动混入
- npm run build: PASS（Next.js 15.5.19 · 编译 21.3s · 静态页 166/166 · Export 2/2 · inject-aff-link 797 注入 / 212 文件正常）

## 四、备份与产物

- 备份目录: .hermes/backups/schema-audit-0828/
  - src__app__[slug]__page.js（14594B 原件）
  - src__app__blog__[slug]__page.js（13749B 原件）
  - src__data__reviews.json（609167B 原件）
- 修复脚本存档: .hermes/tmp-schema-audit-0828.js / tmp-schema-audit-0828b.js

## 五、状态与遗留

- 改动文件 3 个，均未 commit / 未 push（任务范围未含 push；建议并入下一次 aitoptools ops 批量 push）
- 遗留观察（不阻塞）: /about 与 /methodology 可选加 AboutPage/WebPage 页面级 schema（当前继承布局层 Organization 已满足本任务验收线）；/best/[slug] 与 /compare/[slug] 的 Article author 已有 Person 结构，未动
