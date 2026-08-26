# refresh-line-2026-08-27 (旧页刷新产线 S5)

> 执行: cron 手动触发 (用户「执行」) | 2026-08-27 03:1x GMT+8
> 选页依据: reviews.json/comparisons.json × GSC 8/17-8/23 imp, dateModified 最久优先, 避开本周已更新页 (kittl 8/26)
> 沙盒期纪律: 未改 H1/URL/页面结构, 仅内容 refresh + dateModified

## 本轮刷新 2 页

### 1. /manychat-ai-review/ (Manychat AI Review)
- 旧 dateModified: (无, 从未刷新) → 新: 2026-08-27
- GSC 8/17-8/23: imp 29, pos 83.8 (本轮最高 imp 候选)
- 更新内容:
  - 新增 "What's New in 2026" 章节 (2 个新事实):
    1. AI Behavior controls (tone/persona/guardrails) 官方社区公告 — 来源: https://community.manychat.com/
    2. AI 功能转向付费计划 (intent recognition/AI steps), WhatsApp/SMS/AI 附加费可超基础 $15/mo Pro — 来源: https://manychat.com/pricing (2026 年中第三方复核一致)
  - 数据修正 (带源): price 字段 "5/month"(缺失 $) → "$15/month" (与页内定价表 + 官方定价一致); FAQ 两处 "5/month" → "$15/month"; NOT Friendly 段 "99/mo Premium" → "$199/mo Premium" (页内定价表同值)

### 2. /gempages-review/ (GemPages Review)
- 旧 dateModified: (无, 从未刷新) → 新: 2026-08-27
- GSC 8/17-8/23: imp 26, pos 68.0 (本轮第 2 高 imp 候选)
- 更新内容:
  - 新增 "What's New in 2026" 章节 (2 个新事实):
    1. AI Image-to-Layout (截图/设计稿→可编辑布局) + Content Generator 集成到 inline 工具栏 — 来源: https://gempages.net/blogs/shopify/ai-product-page-builder (2026-02)
    2. Shopify App Store 评分 4.9/5 (4,000+ reviews) — 来源: https://apps.shopify.com/gempages

## 校验
- python scripts/validate_content_data.py: [OK] 全部通过
- npm run build: PASS (aff-link 795 注入, 210 文件)
- reviews.json JSON.parse: OK (107 entries)

## Push 纪律
- 本任务不单独 push; 改动攒入当日合并 push (PUSH_READY: /manychat-ai-review/ + /gempages-review/ 内容刷新 + dateModified 更新)

数据来源: data/gsc_data.json (2026-08-17_2026-08-23 窗口, 95 页) | reviews.json (git 工作区, 改动未提交)
