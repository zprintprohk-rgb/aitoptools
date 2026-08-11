# A3 Synthesia 联盟申请台账（2026-08-11/12 终版）

## 一、调研摘要（✅ 完成，可复查）

| 项 | 实证值 | 来源 |
|---|---|---|
| 申请入口 | synthesia.io/partners/affiliates → Apply → HubSpot 表单 share.hsforms.com/1y8Uy9y0RRvWwomvWwK01Tg4x8k3 | 官方页 + 浏览器实证（8/10、8/12 两次） |
| 佣金方案 | **25%**（Starter/Creator 净额，无上限）**非循环仅首购**；60 天 cookie；激励：10 单送一年 Starter、15 单送 Avatar | 官方页（8/12 01:06 浏览器实证：页面明示 25% + 60-day cookie） |
| 资格 | 需审批；Work Email + 站点 + 社交/受众字段 | 表单实证（字段含 Work Email * 必填） |
| 高佣金判定 | 25% 首购 60 天 = 当前唯一可提交高佣金申请（Jasper 关闭、Caspa 未证实、Runway $15） | 候选清单 v2 交叉验证 |

## 二、申请人信息（已录入表单）

Jerome / Tang / zprintpro@outlook.com / aitoptools.net / LinkedIn: jerome-tang-442ab8424 / 受众 ~100 / 描述: Hands-on tested reviews of 107 AI tools for print-on-demand

## 三、提交状态（🔴 未提交成功 — 自动化 5 次尝试记录）

| # | 时间 | 方式 | 结果 |
|---|---|---|---|
| 1 | 8/11 08:07 | 浏览器 | FOCUS_TYPE 超时 |
| 2 | 8/11 08:13 | 浏览器 | ws 1006 网络中断 |
| 3 | 8/11 08:18 | 浏览器 | ws 1006 网络中断 |
| 4 | 8/11 08:24 | 浏览器 | ws 1006 网络中断 |
| 5 | 8/12 01:06 | 浏览器 | 官方页+表单打开，Jerome/Tang/邮箱已填，滚动补填中任务中断（HubSpot iframe 交互不稳定） |
| — | 8/11 08:27-10:57 | 自动重试 cron ×7 | **全部 402 模型余额失败**（cron 已删除） |
| — | 8/11 | HTTP 直提 | portalId 猜测被 HubSpot API 400 拒绝（放弃） |

**IMAP 回执检查（8/12 01:1x）**：8/11 以来 7 封邮件，**0 封 Synthesia/affiliate**——确认未提交。

## 四、用户手动提交行动卡（2 分钟，唯一剩余路径）

1. 打开表单 tab（若已关：https://share.hsforms.com/1y8Uy9y0RRvWwomvWwK01Tg4x8k3）
2. 补填剩余字段：Company name（可填 Print AI Tools）、Website: https://aitoptools.net、Social/LinkedIn: https://www.linkedin.com/in/jerome-tang-442ab8424、Audience size: 100、Description: Hands-on tested reviews of 107 AI tools for print-on-demand
3. 点击 Submit
4. 完成后告知 AutoClaw → 立即 IMAP 验证回执 + 台账更新

## 五、凭证路径

- 成功截图: .hermes/audit/a3-synthesia-{ts}.png（提交后捕获）
- 邮件回执: zprintpro@outlook.com（IMAP 验证）

## 六、重大进展 (2026-08-12 01:16-01:20)
- **HubSpot 申请提交成功** (用户手动/前次尝试): 浏览器实证 URL 含 submissionGuid=c1c5410a-de8a-442f-b695-177748c3c3f9 — 回执凭证
- **流程已进入 Rewardful 注册环节**: synthesia.getrewardful.com/signup?submissionGuid=... 页面已预填 Jerome/Tang/jerome@aitoptools.net
- Work Email 校验规则: outlook 免费邮箱被表单驳回 → 改用企业域名邮箱 **jerome@aitoptools.net**; Company name 用户拍板 = **AI Opt Tools**
- 密码: 已生成强密码存 .hermes/secrets/rewardful-synthesia-password.txt (gitignored); 浏览器预填的 hunter2 演示密码需替换
- 剩余: 替换密码 + reCAPTCHA + Sign up → 注册完成即申请全流程闭环

## 七、邮箱确认闭环推进 (2026-08-12 01:20-01:30)
- CF Email Routing 实证: jerome@aitoptools.net → zprintprohk@gmail.com 规则 Active + MX 已配 + Email Routing Enabled (浏览器实证)
- 目标地址 2 个 (含 gmail); Catch-all 已禁用
- Rewardful 注册已提交: /thanks?id=e2522fb6 (确认邮件等待环节)
- IMAP 复查: INBOX 8 封无 Rewardful; gmail Spam 文件夹名=[Gmail]/&V4NXPpD1TvY- 待复查
- 下一步: Rewardful 重发确认邮件 → IMAP 抓取 (INBOX+Spam) → 点击确认链接 → 注册闭环
