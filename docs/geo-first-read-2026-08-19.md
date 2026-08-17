# GEO 首读数方案 (2026-08-19, T5 前置)

> 状态: 2026-08-17 由 daily-search (T5) 建立 README + 规范化脚本; 8/19 执行读数
> 依据: STRATEGY-2026-08-17 T5 / cef69df (T30 早检: beacon NODATA-D7) / daily-ops 8/17 (AI 爬虫 24h 160 次)

## 一、读数目标 (GEO 投入决策证据)
1. AI 爬虫访问趋势 (7 天窗口): CF Web Analytics + AI Crawl Control (8/17 实测 24h: BingBot 23 / Baidu 22 / ChatGPT-User 20 / Googlebot 19 / Claude-SearchBot 14 / Applebot 7; PerplexityBot/Bytespider/CCBot 0)
2. GSC 位置对比: base 窗口 vs cur 窗口同 query 排名位移 (衡量站内 GEO 改动是否拉高自然排名)
3. LLM 引用初判: llms.txt / robots.txt AI UA 显式欢迎生效验证 (geo-technical G1/G2 已上线)

## 二、数据源与工具 (就绪状态)
| 数据 | 工具 | 状态 |
|---|---|---|
| GSC query 维度 | scripts/gsc_query.py (Service Account + SOCKS5 127.0.0.1:7892) | ✅ gsc-oauth.json 存在 (2,365B), 8/17 weekly-review 已验证 |
| 双窗口对比 | scripts/geo-0819-first-read/pull.py (base 8/4-8/9 vs cur 8/10-8/16) → .hermes/tmp/geo-0819-gsc-full.tsv | ✅ 由已验证的 .openclaw-tmp-geo0819-* 规范化而来 (TSV 已实证产出) |
| 位移分析 | scripts/geo-0819-first-read/compare.py (位置改善 TOP 12 / 下滑 TOP 10 / 总览) | ✅ 同上 |
| AI 爬虫趋势 | CF 仪表板: Analytics → AI Crawl Control (或 Log Explorer) | ⚠️ D7 CF API token 缺失 → 8/19 人工导出 CSV 兜底 |
| Beacon 7d | 站点 beacon 数据位 | ⚠️ NODATA (D7 未就位); 见下 |

## 三、执行步骤 (8/19)
1. 跑 pull.py (双窗口 query 维度) → TSV
2. 跑 compare.py → 位移 TOP 榜
3. CF 仪表板人工导出: AI Crawl Control 7d 数据 (D7 token 就位则 API 拉取)
4. 汇总三源 → docs/GEO-FIRST-READ-2026-08-19.md (含 NORTH-STAR-DATA 追加)
5. 结论: AI 引用趋势 + GSC 位移归因 → GEO 投入继续/调整建议

## 四、兜底方案 (D7 未就位)
- CF dashboard 人工导出 (Web Analytics → AI Crawl Control → Export CSV) 替代 API;
- beacon 数据位缺失时: 用 llms.txt/robots.txt 抓取日志 (Log Explorer) 近似替代;
- 若两者都拿不到: 诚实标注 AI 趋势 NODATA, 仅交付 GSC 位移 + llms.txt 覆盖验证。

## 五、铁律
- 不编造 AI 爬虫数字; 拿不到就标 NODATA (与 T30 早检口径一致)
- GSC 位移区分归因: 核心更新滚动期 (8/15-8/20) 位移可能回吐, 与 8/21 T+14 读数合并判断
- 产出即部署: 8/19 读数结果写入 RESULT + 当日 push
