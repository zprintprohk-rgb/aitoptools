# Bing 收录核查报告（T2 · STRATEGY-2026-08-19）

> 执行：2026-08-19 06:5x AutoClaw · 依据 STRATEGY-0819 R2（Bing/ChatGPT 第一站外 GEO 通道）+ K3 NOTES 4（site: 抽样仅参考，以 BWT 为准）
> 结论：**Bing 收录通道技术侧就绪（IndexNow 全 200），唯一缺口 = BWT 站点验证未做 → user 行动卡（5 分钟）**

## 核查项

| # | 核查项 | 结果 | 证据 |
|---|---|---|---|
| 1 | BWT 站点验证凭证 | **缺失**（.hermes/secrets/ 无 bing/webmaster 相关文件） | 目录扫描 |
| 2 | IndexNow 近 7 天推送 | **全部 200**（8/13、8/16、8/17、8/19 各 200；8/14、8/15 日志中 [45]\d\d 匹配为 hash 字符串 58E31E… 误报，非 HTTP 错误） | indexnow-*.log 逐文件复核 |
| 3 | Bing site: 抽样 | **不可行**——Bing 对无痕爬虫请求返回本地化无关结果（Hilton Sydney 等），无法解析真实收录；按 K3 NOTES 4 不臆断收录率，以 BWT 后台为准 | curl/python 实测 |
| 4 | 技术栈命中（R2 预测因子） | ✅ 全命中：Next.js 静态导出 SSR / 自指 canonical / 内链 597+6,792 / 全站 schema / IndexNow 直推 Bing | 既有资产（无需新验证） |
| 5 | BingBot 活跃度 | ✅ BingBot 23 次/24h 全站最活跃 AI 爬虫（8/17 基线） | daily-ops 8/17 |

## 结论与动作

- **技术通道已就绪**：IndexNow 直推 Bing 全程 200 → Bing 收录入口正常；Next.js SSR + canonical + schema 全命中 ChatGPT 引用预测因子
- **唯一缺口 = BWT 站点验证**：未验证则无法确认 Bing 实际收录覆盖（小站通常比 Google 少 15-30%），也无法用 BWT 后台确认 ChatGPT 引用状态
- **user 行动卡（5 分钟，中文步骤）**：
  1. 打开 <https://www.bing.com/webmasters> → 用微软账号登录（或 Google 账号）
  2. 选 **Import from Google Search Console**（从 GSC 导入）→ 选 aitoptools.net → 确认导入
  3. 若无 GSC 关联：手动添加站点 → 下载 HTML 验证文件放 F:\aitoptools\public\ 根 → 我等下轮 push 带上线后点验证（或选 DNS 验证）
  4. 完成后告诉我，我用 BWT API/后台读数确认收录覆盖，并接入 ChatGPT 引用审计

## 幂等
- 本报告存在 → T2 NOOP；BWT 验证完成后需在 BWT 后台做一次「URL Inspection」确认关键页收录（legit 2 + Halloween 2 + money 3 + 首页/对比 3）
