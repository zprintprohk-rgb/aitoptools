# legit-check 页模板骨架 (T3, 2026-08-17)

> 用途: legit-check 产线标准结构 (战线 B); 复用辐条②结构 + Trustpilot 段落模板; 每篇上线前事实核实

## 页面结构 (H2 顺序固定)
1. **H1**: Is X Legit? [2026 实测结论] (50-60 字符, 主关键词前置)
2. **Quick Answer (BLUF)**: 首段 3 行内给结论 + 数据锚点 (域名状态/评分/投诉数)
3. **What X Is**: 平台/工具是什么, 价格, 谁在用 (2021-2023 背景)
4. **The Trust Complaints**: 真实投诉点 3 条 (物流/售后/质量), 每条引来源
5. **Trustpilot and BBB Data 专章**: 评分/评论数/检查日期 + 来源 URL; 无档案如实说 (如: 无 Trustpilot 档案/无 BBB 档案 = 平台已关闭信号)
6. **Lookalike and Security Warning**: 钓鱼域名警示 (引 gridinsoft 类安全扫描来源)
7. **How to Verify Yourself**: 5 分钟自查 (域名状态/测试订单/退款政策/WHOIS)
8. **Alternatives CTA**: 2-3 个联盟替代品 (UTM 规范), 互链既有 review 页
9. **FAQ (≥5)**: 覆盖 GSC 变体 query: legit / trustpilot / free money / safe / worth it
10. **Schema**: Article + FAQPage + BreadcrumbList + author (Person); dateModified 更新

## Trustpilot 段落模板 (事实核实版)
- 开头: The first thing to know: {domain} itself has {no|a} Trustpilot profile.
- 数据: rated X/5 from N reviews (last activity {year}) + Trustpilot 免责声明引用 (reviews may not be representative)
- 交叉: BBB 档案状态 (有/无) + 对卖家的操作意义 (有无可投诉主体)
- 结论句: 三信号组合 (域名/档案/评分) → 平台关闭 vs 诈骗 的判定
- 格式: <a href='https://www.trustpilot.com/review/{domain}' rel='noopener nofollow'> 来源链接

## 硬约束
- 铁律: Trustpilot/BBB/Reddit 数据必须引用真实来源 URL, 禁止编造评分; 无公开数据不入列
- 字数 ≥2,500 / 实测语气 / 截图 3-5 张 (诚实标注 illustrative 不得冒充实拍)
- FAQPage schema 覆盖 GSC 变体 query; 上线前 npm run build PASS
- 核心更新滚动期: 只加内容不改模板结构/内链架构
