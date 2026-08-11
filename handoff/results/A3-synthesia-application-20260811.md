# A3 Synthesia 联盟申请台账（2026-08-11）

## 一、调研摘要（research-concluded ✅）

| 项 | 实证值 | 来源 |
|---|---|---|
| 申请入口 | https://www.synthesia.io/partners/affiliates → Apply → **HubSpot 表单** share.hsforms.com/1y8Uy9y0RRvWwomvWwK01Tg4x8k3 | 官方页 + 浏览器实证（tab 97685851） |
| 佣金方案 | **25%**（Starter/Creator 计划净额，无上限）；**非循环仅首购**；激励：10 单送一年免费 Starter、15 单送定制 Avatar | 官方联盟页（8/10 浏览器实证） |
| Cookie | 60 天 | 官方页实证 |
| 支付 | Rewardful 平台发链（页面未明示起付额，获批后以条款邮件为准） | 官方页 + postaffiliatepro 第三方口径 $30 |
| 资格 | 需审批；推广站点 + 社交 URL + 受众规模 | 官方页 |
| 高佣金判定 | 25% 首购 60 天 cookie = 当前唯一可提交的高佣金申请（Jasper 程序关闭、Caspa 未证实、Runway $15 固定） | 候选清单 v2 交叉验证 |

## 二、申请人信息（提交用）

- First name: Jerome / Last name: Tang
- Email: zprintpro@outlook.com（项目主邮箱，IMAP 监控中）
- Website: https://aitoptools.net（Print AI Tools — 印刷/POD 垂直 AI 工具评测站）
- LinkedIn: https://www.linkedin.com/in/jerome-tang-442ab8424（about 页实证）
- 受众规模: ~100（如实小值；107 工具评测站，冷启动期）
- 推广描述: Hands-on tested reviews of 107 AI tools for print-on-demand, packaging and product photography

## 三、提交状态（进行中 — 自动重试机制）

| 字段 | 值 |
|---|---|
| 提交时间 | 待定（表单未提交成功） |
| 提交方式 | 浏览器（tab 97685851）+ HTTP 直提解析（portalId 猜测被 400 拒，已放弃） |
| 网络事件 | 08:07 FOCUS_TYPE 超时；08:13 ws 1006；08:18 ws 1006；08:24 ws 1006（浏览器 4 次中断，表单 tab 保持打开） |
| **自动重试** | cron「Synthesia 申请自动重试」已注册（08:25）：每 15 分钟（8/9/10 点 :27/:42/:57），复用 tab 续填提交，成功即自删，TTL 2h |
| 敏感字段 | 无（表单仅姓名/邮箱/网站/描述，未要求付费/税务/证件） |
| 回执 | 待捕获（页面成功提示或邮件） |

## 四、凭证路径（待补）

- 提交成功截图: 待捕获 → .hermes/audit/a3-synthesia-{timestamp}.png
- 邮件回执: zprintpro@outlook.com（IMAP 可监控确认）

## 五、下一步

1. 自动重试 cron 逐轮尝试（网络波动间歇，复用已填表单）
2. 成功 → 捕获页面成功提示截图 + IMAP 邮件回执 → 更新台账 → cron 自删
3. 若 TTL 内持续失败 → 升级用户手动提交（Chrome 表单 tab 已就绪，仅需补 2-3 字段点提交）
