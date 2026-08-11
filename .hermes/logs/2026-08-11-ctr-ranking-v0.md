# CTR 榜 v0 — 2026-08-11（W4-T1 数据基线）

**目标**: 每个 affiliate 链接 (page_url, link_id, clicks, page_views) → CTR = clicks/page_views → TOP 10
**数据源**: GA4 affiliate_click 事件 × page_view (GA4 属性 G-248QMCT2S3, 埋点已上线 layout.js)

## 状态: ❌ GA4 凭证缺失, CTR 榜 v0 延迟
- .hermes/secrets/: 仅有 affiliate-credentials.md / gmail_credentials.json / gsc-oauth.json.template (模板) / indexnow-key.txt — 无 GA4 服务账号 JSON 或 OAuth token
- 项目根 / .env / hermes .env: 无 GA4 API 凭证 (只有浏览器端 gtag 埋点, 无服务端读取权)
- 埋点本身已就绪: gtag affiliate_click 事件 + data-link-id (kittl-review-card-cta 等) 正常打标, 数据正在 GA4 累积, 只差读取凭证

## 一次性配置指引 (约 10 分钟)
1. Google Cloud Console → 建服务账号 (或复用 GSC OAuth 流程, 参照 gsc-oauth.json.template 结构)
2. 授权该账号访问 GA4 属性 G-248QMCT2S3 (Property 权限: Viewer 即可)
3. 下载服务账号 JSON → 存 .hermes/secrets/ga4-service-account.json
4. 告知 Hermes 文件就位 → 下轮 cron 用 Google Analytics Data API v1 (analyticsdata.runReport) 拉 7 天 affiliate_click + page_view 出榜

## 备注
- 无凭证期 GA4 数据仍在累积, 不会丢; 榜单延迟不阻塞 Kittl 判定 (判定靠 Impact 点击数, 与 CTR 榜独立)
- 拉取脚本将按本项目惯例写 /tmp/ga4_ctr.py (不用 inline python -c)
