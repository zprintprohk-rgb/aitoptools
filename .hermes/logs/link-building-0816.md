# 外链提交记录 — 首批 8 站 (2026-08-14)

> 执行: W1-0816 B 类快修 cron (f44b540b) | 依据: .cluster/link-directory-list.md P0 清单 (免费可投 + dofollow 已核实/官方自述优先)
> 统一实体描述: aitoptools.net — Print AI Tools review site specializing in AI-powered solutions for print shops, packaging design, and e-commerce store operations. Founded by Jerome Tang of Shenzhen Cai Long Printing
> 邮箱: jerome@aitoptools.net | 目标 URL: https://aitoptools.net
> 原则: 表单被 CAPTCHA/验证码/登录墙挡住 → 记录 BLOCKED_* 不硬闯; 不自动加站内回链 (需 K3 拍板)

## 提交结果总表

| # | 站点 | URL | 提交时间 | 结果 | 说明 |
|---|------|-----|---------|------|------|
| 1 | AI Toolz Dir | https://www.aitoolzdir.com/submit | 2026-08-14 06:0x | BLOCKED_REQUIRES_BACKLINK | API 已发现并实测可通: POST /api/tool/submit/free (JSON, 无验证码)。返回 "Backlink not found on your website" — 免费档需先挂站内回链 (锚文本 AI Toolz Dir, DR66 dofollow)。回链待 K3 拍板, 加后重提即可收录 |
| 2 | Wired Business | https://wired.business/submit-your-website | 2026-08-14 06:0x | BLOCKED_REQUIRES_BACKLINK | 免费档 $0 要求主页/footer 回链 (DR77 dofollow 已实测核实, 72h 审核); Pro $29 免回链 (FROGDR 码 -30% = $20.30)。表单为 JS 流程, curl 无法直接提交 |
| 3 | Findly.tools | https://findly.tools/submit | 2026-08-14 06:0x | BLOCKED_BY_CAPTCHA | 表单存在但无 action (JS 提交) + Cloudflare Turnstile 验证码。需人工浏览器提交 (挂 badge 后得 dofollow, DR80) |
| 4 | ToolPilot | https://www.toolpilot.ai/pages/submit-your-ai-tool | 2026-08-14 06:0x | BLOCKED_BY_CAPTCHA | Shopify 站, 提交走 /contact 表单, Shopify 全局 captcha (Turnstile) 绑定 contact 表单, curl 无法绕过。需人工浏览器提交 (免费+挂 badge, dofollow 已实测核实 DR78, 队列最长 90 天) |
| 5 | The Next AI | https://thenextai.com/submit-ai-tool/ | 2026-08-14 06:0x | BLOCKED_BY_CAPTCHA | 提交页含 captcha 校验。需人工浏览器提交 (免费, 链接干净 dofollow DR4, 数天发布, 适合快速铺量) |
| 6 | LaunchBoosts | https://launchboosts.com/submit | 2026-08-14 06:0x | BLOCKED_BY_CAPTCHA | Cloudflare challenge-platform 拦截 (challenge 页), curl 拿不到表单。需人工浏览器提交 (免费, 官方自述 dofollow, 审核快) |
| 7 | Startuplist.in | https://startuplist.in/submit | 2026-08-14 06:0x | BLOCKED_CONNECTION | 两次请求均连接超时 (000), 站点边缘防护或网络问题。下次 cron 重试 |
| 8 | Dofollow.Tools | https://dofollow.tools/submit | 2026-08-14 06:0x | BLOCKED_NEEDS_LOGIN | Next.js 客户端表单 + /api/auth (需账号), 且免费档模型 = footer 互链 + badge (每天 1 免费位)。需注册账号 + 互链, 暂缓 |

## 小结

- **成功提交: 0/8** (全部被验证码/登录/回链业务规则拦截, 按"不硬闯"原则全部记录 BLOCKED)
- **最大收获**: AI Toolz Dir 的免费提交 API 已逆向并实测 (POST /api/tool/submit/free, JSON body: name/url/logo/shortDesc/longDesc/category/email/type), 请求体已存档 .hermes/tmp/linkbuild-0816/aitoolzdir-body.json — K3 拍板加回链后可直接重提
- **回链决策待办 (K3)**: aitoolzdir.com + wired.business 免费档需站内回链 (footer 锚文本); 加回链属站内改动, 本 cron 不自动执行
- **人工浏览器提交待办**: findly.tools / toolpilot.ai / thenextai.com / launchboosts.com 共 4 站, 已准备好统一实体描述 (建议后续带浏览器工具的 cron 或 user 手动执行)
- 探测文件存档: .hermes/tmp/linkbuild-0816/ (HTML + JS chunk + body.json)
