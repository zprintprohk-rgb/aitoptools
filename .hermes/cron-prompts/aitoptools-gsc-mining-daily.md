# Task Card: gsc_mining_daily (P3, 每日 13:00 触发 — gsc-indexnow 12:40 之后)

> 2026-08-08 v2 指令集 P3 · 数据源: GSC (gsc-oauth.json 若已配置; 否则 gsc_data.csv 或 blocked_missing_credentials)

## logic
1. mining: query 展示≥10 AND CTR<0.05 AND 无专页 → 追加 CONTENT_PLAN.md "## Data-Driven Queue"
2. boosting: 现有页排名 20-70 AND 展示≥5 → 动作: ① top 3 相关帖注入内链 ② 追加目标 query 的 FAQ schema ③ 生成 2 个指向该 URL 的 Pinterest pin
3. report: 写入每日 brief "🎯 GSC Opportunities" 段

## 幂等检查 (R4)
- CONTENT_PLAN.md 队列已有同 query 同日期行 → 跳过 (只追加不重复)
