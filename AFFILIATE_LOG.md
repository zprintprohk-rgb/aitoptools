- 2026-07-17 Looka: PartnerStack 计划已关闭（api.partnerstack.com 返回 Company not found），landing 页为空壳。备选：邮件 partnerships@looka.com 询问，或放弃。已在 looka.com 创建普通账号（非联盟）。
- 2026-07-18 Kittl/Impact：放弃 gmail 新注册（手机号必填卡住）。改用用户15号已提交过 Kittl 申请的老账号 Jerome88（zprintpro@outlook.com）。旧密码失效，已通过重置邮件改为新密码（存 credentials）。登录后发现：Shopify 申请被 Declined（auto-rejected）；Kittl 15号申请状态在受限门户不可见，用户称"没有通过"（待确认是被拒还是仍在审核，以 Outlook 后续邮件为准）。已通过 /secure/none/joinPlatform.ihtml 提交 Join Impact Marketplace 升级申请，状态 awaiting approval——升级获批后才能在市场内重新申请 Kittl 和 Placeit。Outlook 邮箱（zprintpro@outlook.com）的审批邮件需用户自行留意，每日定时任务只查 Gmail。

## 2026-07-22 Mockey AI ✅ 获批即激活
- 雷达 7/21 发现的候选，7/22 凌晨完成申请→激活全流程（Endorsely 平台，无审批等待）
- 联盟链接：`https://mockey.ai?via=jerome796`（30% 经常性佣金 / 90 天 cookie / PayPal 月结）
- 账号：zprintprohk@gmail.com（Jerome），魔法链接登录，无密码
- 坑位记录：确认邮件进 Gmail 垃圾邮件文件夹，以后 Endorsely 系邮件先查垃圾邮件
- 下一步：《Mockey vs Placeit》对比页（M3 任务已派）+ 链接走 replace_affiliate_links.py 管线

## 2026-07-23 巡检日（affiliate-monitor cron 启动 D2）
- **Gmail 通道状态**：❌ UNAVAILABLE。凭证文件 `credentials.affiliate.local.json` 仅有 7 个平台账号（CF/Claid/PartnerStack/Looka/Printful/Impact/Mockey），无 Gmail OAuth / App Password / IMAP 凭证。Cron 启动 24h 内 0 封真实邮件被读取。
- **本次巡检证据基础**：仅靠 state file + 凭证时间戳 + 历史 log 推断，**无新增/拒绝/待审邮件事实**。任何"今日获批 X 封"类断言均不成立，禁止 cron 自报数据。
- **待审申请 aging 监控**（7/24 将达 7 天阈值，需 user 拍板 follow-up 或换平台）：
  - Claid AI (FirstPromoter) — 2026-07-17 申请，6 天
  - Printify (PartnerStack) — 2026-07-17 申请，6 天
  - Looka (in-house) — 2026-07-17 注册，账号已建，推广链接未生成，6 天
  - Printful (in-house) — 2026-07-17 申请，6 天，官方 2-5 工作日人工审批承诺
  - Impact Marketplace 升级 — 2026-07-18 提交，5 天，7/25 达阈值；Kittl/Placeit 二次申请前置依赖
- **建议操作（按优先级）**：
  1. **P0**：补 Gmail API 通道 — 写 `gmail_credentials.json` (gitignore) 或在 `credentials.affiliate.local.json` 加 `gmail` 段，cron 才能真读取 zprintprohk@gmail.com（**否则此 cron 长期空转**）
  2. **P1**：7/24 前 user 主动 follow-up 4 个 7 天阈值的申请（Claid / Printify / Looka / Printful），附 aitoptools.net 流量+合规页证据
  3. **P2**：明日 7/24 cron 跑完，验证 Looka 账号后台是否生成推广链接（looka.com 7/17 提示"推广链接需在联盟后台另行提取"，6 天未提取 = 账号半成品）
- **链接替换管线（不动）**：`scripts/replace_affiliate_links.py --apply` 仍需 user 拍板（per AGENTS.md §6 + project.yaml compliance.review_required_for）。今日不自动跑。
- **AFFILIATE_LINKS.json 真实覆盖**：仍 1/11 (Creative Fabrica)。其余 10 项空串 = 占位阶段。
- **北极星指标**：6 个月目标 $3000，截至 7/23 $0。当前真实计佣入口 = CF (in-house) + NordVPN/NordPass (Impact) + Mockey (Endorsely)，3 个真实链接，需 1-3 个月才有第一笔成交。

