# Cloudflare AI 爬虫数据 - 人工导出兜底指引 (GEO 首读数)
> 建立: 2026-08-19 (GEO 首读数 cron) - 原因: D7 CF API token 缺失 → 无法 API 拉取 AI 爬虫数据
> 适用: aitoptools.net 的 AI 引擎引荐流量 (beacon 7 天) 读数兜底

## 为什么需要人工导出
GEO 首读数需要「AI 爬虫访问趋势 (7 天窗口)」作为 AI 引荐流量 >0/=0 的硬证据。但 D7 CF API token 一直未就位, API 拉取不可用, 本次只能标 NODATA。本 README 记录人工从 CF Dashboard 导出的步骤, 供 user/工具替代 D7 缺口。

## 导出步骤 (约2分钟)
1. 登录 https://dash.cloudflare.com/ → 选择 aitoptools.net 站点
2. 左侧 Analytics → Web Analytics (或 Log Explorer)
3. 时间窗选「近7天」(或自定义: 上次读数日→今天)
4. 视图切到 AI Crawl Control (若无, 用 Web Analytics → User Agents, 按 AI UA 名过滤)
5. 关注 AI 爬虫 UA: GPTBot / ClaudeBot / PerplexityBot / Google-Extended / Applebot-Extended / Amazonbot / meta-externalagent / cohere-ai / Bytespider / CCBot / ChatGPT-User
6. 点右上角 Export → 导出 CSV
7. 把 CSV 丢到 .hermes/tmp/geo-cf-ai-crawlers-YYYY-MM-DD.csv, 并在当次 GEO 读数日志引用

## 判定口径 (与 K3 T30 早检 cef69df 一致)
- 7 天窗口内任意 AI 爬虫 UA 引荐流量 > 0 → AI 引荐 = 有量 (正值)
- 全部 AI UA 均 0 次 → AI 引荐 = 0
- 拿不到 / 无法导出 → 诚实标 NODATA, 不编造数字

## 现状 (2026-08-19)
- D7 CF API token: 缺失 (自 8/15 documented, 已 ≥3 天)
- 本次读数: NODATA (AI 爬虫引荐), 已升级 user 补齐凭证
