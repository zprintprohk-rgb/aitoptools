# Kittl 专项诊断 — 2026-08-14 (S2, STRATEGY-2026-08-14 执行映射)

> 背景: rank-sentinel 8/13 告警 kittl review 68.5→74.0 (-5.5 位); 8/14 上午 T+7 读数周已确认
> 数据: GSC API 实时 (8d 窗口 8/6-8/13, page+query 维度) + 哨兵 8/12-8/13 + 8/11 联盟实测日

## 一、排名趋势 (kittl 系 query 全景, 28d 窗口 7/17-8/13)

| query | 28d imp | 28d pos | 判定 |
|---|---|---|---|
| kittl | 24 | 68.2 | 主品牌词, 稳定 65-70 区间 |
| kittl review | 7 | 69.0 | **波动源: 仅 7 imp/28d = 低量噪音区** |
| canva vs kittl | 2 (8d) | 72.5 (8d) | 低量 |
| kittl vs canva | 17 | 73.0 | 对比词合计 ~19 imp, 是 kittl 系第二大流量 |
| kittl vs placeit | 3 (8d) | 30.0 (8d) | 排名健康 (前 30) |
| /kittl-review/ 页 (8d) | 21 | 68.1 | 页级位置 8/13 哨兵 74.0 → 8/14 拉取 68.1: 单日 ±6 波动 |

## 二、诊断结论: 低量噪音 + 内容缺口双因素

1. **低量噪音主因**: "kittl review" 28 天仅 7 次展示 (~0.25/天), 位置 69-74 的跳动基本是统计噪音, 不代表真实下跌。哨兵 8/12→8/13 的 -5.5 位告警属低量窗口的正常抖动。
2. **可控内容缺口 (GEO 8 项检查)**:
   - dateModified: ❌ 缺失 (页面无更新日期)
   - featureLine: ❌ 缺失 (reviews.json 无功能行)
   - 引用链 Sources: ❌ 缺失 (无外部权威来源)
   - 其余 5 项 ✅ (BLUF summary-box / 数据表 / FAQ 6 条≥5 / FAQPage+Article Schema 自动渲染 / verdict)
3. **联盟侧**: pxf 链接已部署 4 处 (首页卡 CTA / 详情页 CTA / 2 对比页); Impact 后台数字仍缺 (8/11 指引待 user 回填 5min) — 位置 69-74 区间本无点击, 联盟转化暂不受排名波动实质影响。

## 三、修复建议 (按优先级)

| # | 动作 | 排期 | 说明 |
|---|---|---|---|
| A | 内容补强 3 项: dateModified→执行日 / featureLine 补功能行 / Sources 引用链 ≥1 (kittl.com 官网 + pricing + 第三方评测) | T14 (8/21 前) | GEO 完整性, 与 #5/#6 Boost 同标准 |
| B | 内链补覆盖: /compare/kittl-vs-canva/ (pos 73) + /compare/kittl-vs-placeit/ (pos 30) + 首页 review 卡 + category/ai-print-design 变体锚 → /kittl-review/ | T14 | 四杠杆标准内链 ≥4 |
| C | 对比页词序对齐: "canva vs kittl"(2 imp) + "kittl vs canva"(17 imp) 合计 19 imp 是 kittl 系最大入口 — 标题/简介对齐用户实际搜索词序 | 8/16 B 类快修评估 | 低投入高回报 |
| D | 哨兵持续跟踪: 若 8/15-8/16 连续 >74 位 → 升级 Boost 队列插队 (kittl-review 已在队列) | 每日 | 风险开关 |
| E | Impact 数据回填后终判加投/撤位 (判定线: ≥5 点击/天加投, 1-5 维持, <1 撤首页 2 pxf) | user 回填后 | 联盟侧 |

## 四、结论

**不判定为真实下跌** — 展示量级过低 (7 imp/28d), 波动属噪音; 真实风险在内容缺口 (3 项 GEO) 与对比词流量入口未对齐。按 A-E 执行, 8/22 Boost T+14 复读验证。