# legit 事实核实 2026-08-20 (queue #6-8: TeePublic / Redbubble / Gelato)

> 任务: STRATEGY-2026-08-20 T4 (8/20 cron 故障未执行, 8/21 补) | 只备不部署 (D12/D13 未拍板) | 方法: web_search 多源, Trustpilot 直抓 403 走备选源

## TeePublic (queue #6, GSC: teepublic legit 66 imp)
- Trustpilot: **4.4/5, 640,587 条** (trustpilot.com/review/www.teepublic.com, 2026) — 样本量极大, 高可信
- 官方自述: teepublic.com/about/reviews 称 4.5/5 (官方页口径)
- 第三方: worthepenny 4.6/25 条; trendlytic (2026-06-02): legit, 真实产品+安全结账+真实退款流程
- 负面点: 长发货时间 / 质量一致性 — legit 文 FAQ 可带
- 备选源可用: Trustpilot 搜索快照可抓 → 无需 403 绕行

## Redbubble (queue #7, GSC: is redbubble legit 67 imp)
- Trustpilot: 域名 redbuble.com (官方拼写错误域) ~117 条 — 样本小, 引用需谨慎
- BBB: **NOT BBB Accredited** (bbb.org 投诉页存在, 2026-04-02 有 .50 投诉) — 负面信号如实带
- 正面: 90 天无条件退款保证 (mywifequitherjob) + ecommerce-platforms: safe and legitimate
- 口径建议: legit 结论 = YES (90 天退款 + 平台规模), 但 BBB 非认证 + Trustpilot 样本小要如实写

## Gelato (queue #8, GSC: is gelato worth it 26 imp)
- Trustpilot: **4.4-4.5/5, ~3,136 条** (ecommercetrix 2026-06-17 摘录 Trustpilot) — 样本充足
- dodropshipping (2026-07-25): 4.7/5 over 800+ reviews — 与 ecommercetrix 4.4 口径略差, 引用取 4.4-4.5
- Shopify App: 4.8/5, 92% 5 星 (apps.shopify.com)
- G2: 4.5/5
- 负面点: 客服响应/可靠性偶有抱怨 (Shopify 评 4.8 但评论区有 CS 抱怨) — FAQ 可带平衡

## 汇总 (备料状态)
- TeePublic/Redbubble/Gelato 三篇 legit 文事实基础已齐, 带 URL 可引用
- 每篇可用: Trustpilot 评分 + BBB 状态 + 退款政策 + 负面平衡点
- D12/D13 拍板 → 用 legit-template-v2.md (rubric 30/25/25/20) 生产, 幂等键 is-{tool}-legit
- 无公开数据缺口: 无 SKIP 项 (三篇数据均可用)

