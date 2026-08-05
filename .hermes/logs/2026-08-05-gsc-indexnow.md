# GSC / IndexNow 收录提交日志 — 2026-08-05

**任务**: aitoptools.net 搜索引擎收录提交 (Hermes role, 每日 12:40)
**结果**: 凭证缺失,已升级 user 一次性配置

## 一、sitemap 检测
- public/sitemap.xml: 531 URLs, mtime 2026-08-05 10:44
- public/sitemap-programmatic.xml: 199 URLs, mtime 2026-08-05 10:44
- out/sitemap.xml 与 public 同步 (build 已产出)
- 合计待提交: 730 URLs
- 首次运行 (无 state 文件) 视为有变更

## 二、凭证检查
- IndexNow: .hermes/secrets/indexnow-key.txt 缺失 (仅 template), 环境变量 INDEXNOW_API_KEY 未设置
- GSC: .hermes/secrets/gsc-oauth.json 缺失 (仅 template)
- 结论: 两项均缺失,不猜测不编造 key, 按流程 Step 4 升级 user

## 三、处置
- 未提交任何请求 (IndexNow API / GSC API 均未调用)
- state 文件已写入: gsc-indexnow-state.json (last_submitted_* = null, 状态 blocked_missing_credentials)
- 待 user 配置凭证后, 每日 12:40 cron 自动检测并提交, 无需重建

## 四、user 一次性配置指引 (约 10-15 分钟)
### IndexNow (5 分钟, 免费, 无注册)
1. 打开 https://www.indexnow.org/ekit 生成 32 位 hex key (例: a1b2c3d4e5f67890abcdef1234567890)
2. 保存到 F:/aitoptools/.hermes/secrets/indexnow-key.txt (纯文本, 只含 key)
3. 上传验证文件 {key}.txt 到 https://aitoptools.net/ 根目录 (内容为 key 本身, Bing 校验返回 200)
   - 可通过仓库 public/ 目录添加后走一次 push (CF Pages 自动部署), 或直接在 CF 管理面板上传

### GSC (一次性 OAuth)
1. https://console.cloud.google.com/apis/credentials 创建 OAuth 2.0 Client ID (Desktop app 或 Web app)
2. 同一项目启用 Search Console API + Indexing API
3. OAuth Playground 拿 refresh_token:
   - https://developers.google.com/oauthplayground/ 齿轮图标 → Use your own OAuth credentials 填 client_id/secret
   - Step 1 选 scope: https://www.googleapis.com/auth/webmasters 和 https://www.googleapis.com/auth/indexing
   - Authorize APIs (登录 zprintprohk@gmail.com) → Exchange code for tokens → 复制 refresh_token
4. 保存到 F:/aitoptools/.hermes/secrets/gsc-oauth.json:
   {"client_id": "...", "client_secret": "...", "refresh_token": "...", "site_url": "sc-domain:aitoptools.net"}
5. 验证: python scripts/submit-indexnow.py --dry-run 和 python scripts/submit-gsc-sitemap.py --dry-run
6. 正式提交: python scripts/submit-indexnow.py 和 python scripts/submit-gsc-sitemap.py

## 五、硬约束自检
- 未自动 push / 未自动 build / 未改凭证文件
- 凭证缺失仅升级 user, 未猜测 key
- state 文件已更新
