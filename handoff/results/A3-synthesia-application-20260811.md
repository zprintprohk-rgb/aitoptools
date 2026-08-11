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

## 三、提交状态（进行中）

| 字段 | 值 |
|---|---|
| 提交时间 | 待定（表单未提交） |
| 提交方式 | 浏览器（tab 97685851，部分字段已填）+ HTTP 直提解析（portalId=3610186955 已解出，formGuid 提取中） |
| 网络事件 | 08:07 FOCUS_TYPE 超时；08:13 ws 1006 中断（浏览器路径两次受阻） |
| 敏感字段 | 无（表单仅姓名/邮箱/网站/描述，未要求付费/税务/证件） |
| 回执 | 待捕获（页面成功提示或邮件） |

## 四、凭证路径（待补）

- 提交成功截图: 待捕获 → .hermes/audit/a3-synthesia-{timestamp}.png
- 邮件回执: zprintpro@outlook.com（IMAP 可监控确认）

## 五、下一步

1. 提取 formGuid（iframe 脚本）→ HTTP POST 提交（api.hsforms.com/submissions/v3/integration/submit/{portal}/{guid}）
2. 或浏览器第三次恢复（网络低峰窗口）完成提交
3. 提交后立即验证回执（页面提示 + 邮件双通道）
