# refresh-line-2026-08-29 (旧页刷新产线 S5) — 提前执行下周队列 + 全库乱码修复

> 触发: cron session 用户「继续」(2026-08-29 04:5x GMT+8) — 按上轮 NOOP 落盘的队列预览, 提前执行下一批 2 页
> 语义: 「继续」= 拉前执行 queued batch (shopify-magic + creative-fabrica); 下周二 9/1 cron 顺延取再下一批, 周总量仍守 2 页/批节律
> 沙盒期纪律: 未改 H1/URL/结构

## 本批刷新 2 页

### 1. /shopify-magic-review/ (imp 21, pos 69.9)
- dateModified: 2026-07-15 (仅 datePublished) → dateModified: 2026-08-29
- 新增 What's New in 2026:
  1. Sidekick 为核心 AI 助手 (admin 内内容生成/数据分析/店铺管理) — 来源: https://www.shopify.com/sidekick
  2. Winter '26 Editions 150+ 更新, Sidekick/AI 主线 — 来源: https://www.shopify.com/releasenotes
- **数据修复 (生成器乱码)**:
  - content 内 24 处共享模式 (本页 4 处): \"''' + D + '''\" → \"$\" (价格符号丢失), \"''' + chr(10008) + '''\" → ❌
  - price 字段 \"Included (9+/mo Shopify)\" → \"Included ($39+/mo Shopify)\" (与页内定价表 Basic $39/mo 一致)
  - cons/content/FAQ \"Full AI on 05/mo plan\" → \"on $105/mo plan\" (3 处, 同表)
  - \"Requires Shopify (9+/mo)\" → \"($39+/mo)\" (2 处)

### 2. /creative-fabrica-review/ (imp 15, pos 61.3)
- dateModified: (缺失) → 2026-08-29
- 新增 What's New in 2026:
  1. CF Spark AI 套件扩张 (image/text/pattern + vectorizer 转 SVG, premium 含) — 来源: https://www.creativefabrica.com/the-artistry/cf-spark
  2. CF Studio 全家桶定位 (7M+ 资产库 + 内置设计/AI 工具) — 来源: https://www.creativefabrica.com/

## 顺手全库修复 (7 页, 仅机械乱码, 不动内容语义/dateModified)
gelato-review / printful-review / printify-review / looka-review / logoai-review / vistacreate-review / postermywall-review / zmo-ai-review 中的 \"''' + D + '''\" (→ $) 与 \"''' + chr(10008) + '''\" (→ ❌) 全部清零 (合计 24 D + 17 X08, 82 个 ''' 残留 = 0)
- 先例: 8/28 daily-search \"reviews 裸amp清理23处\" 同类数据修复; 本修复纯字符级, 不构成刷新信号, 故不改这 7 页 dateModified

## 残留发现 (不动, 交 daily-search 判定)
- tidio-ai-review: 2 处 \"9+/month\" (\"premium plan at 9+/month\") — 语义存疑 ($9+ or $39+?), 需对 Tidio 官方定价核实后再修

## 校验
- validate_content_data.py: [OK] 全部通过
- npm run build: PASS (aff-link 797 / 212 文件)
- reviews.json JSON.parse OK (107), \"'''\" 残留 = 0

## Push 纪律
- 不单独 push; PUSH_READY: shopify-magic + creative-fabrica 刷新 + 9 页乱码修复 (当日合并 push)

数据来源: data/gsc_data.json (2026-08-17_2026-08-23) | reviews.json HEAD(57f6fa4) 工作区改动未提交 | web_search 官方源 (shopify.com/sidekick, shopify.com/releasenotes, creativefabrica.com)
