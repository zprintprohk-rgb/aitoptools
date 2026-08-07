# Task Card: printful_verify_resend (P0, cookie 解锁后立即执行)

> 2026-08-08 v2 指令集 P0 · 前置: .hermes/secrets/printful_session_cookie (user 补录)
> 安全边界: 仅做邮箱重发验证, 不碰支付/资金/改密; 异常立即停止 + 告警 (AGENTS.md 安全与审计铁律)

## 幂等检查 (R4, 先做)
- affiliate-programs.json 的 printful.email_verified=true → 输出 "ALREADY DONE" 退出

## 步骤
1. cookie 文件存在且有效 (HEAD https://www.printful.com/dashboard 不 302 到 login)
2. headless login Affiliate Dashboard (cookie 通道, 不输密码)
3. navigate Settings → Email Verification → Resend
4. poll Gmail IMAP 新 verify 邮件 (max 3 次, 60s 间隔; 用 .env IMAP_PASSWORD, 勿用失效的 app_password)
5. 提取链接 → GET → 验证响应含 "verified"
6. 更新 affiliate-programs.json: email_verified=true, status=approved
7. 触发 aff-link scanner: 裸 printful.com 链接替换为跟踪 URL (scripts/replace_affiliate_links.py 模式)
8. log 到 .hermes/audit/printful-verify-{timestamp}.json + browser-auto log
9. 删除本 watcher cron (自清理)

## fallback
- 任一 403/CAPTCHA/超时 (2 次重试后) → 停止 + 告警 user (附截图 + 手动重发指引)
- timeout: 5 min
