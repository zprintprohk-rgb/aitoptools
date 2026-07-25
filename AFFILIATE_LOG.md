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


## 2026-07-24 Printify ✅ 获批（PartnerStack）
- 登录 PartnerStack 后台发现 Printify 申请已获批，现场同意服务条款后取到默认链接：`https://try.printify.com/4fs863rfz2yc`
- 彩蛋：Printify 每月挑战——发布 Printify 相关博客/视频赢 $150（截止 2026-09-29），我们已有 Printify 对比/榜单内容可提交
- 下一步：链接入库走 replace_affiliate_links.py 管线替换全站 Printify CTA

## 2026-07-24 Claid AI ✅ 获批（FirstPromoter）
- 后台已激活，链接：`https://claid.ai?via=jerome94`（20% 终身循环 / 60 天 cookie / $20 起付 / 每月 15 日结算）
- ⚠️ 待办：后台提示未设置收款方式（Select Payout Method），涉及收款账户需用户自行设置

## 2026-07-24 Printful ✅ 获批（in-house）
- 联盟后台已激活，链接：`https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a`
- 佣金 10%×12 个月；奖励活动：$5000 销售奖 $50、5 个下单客户奖 $25
- 待办：Printful 发了一封邮箱确认邮件到 zprintprohk@gmail.com，看到点一下确认即可

## 2026-07-24 Looka ❌ 维持放弃（二次确认）
- looka.com/affiliate-program/ 落地页仍在宣传，但点击「Become an affiliate」跳转到 looka.partnerstack.com 显示「Looka program page not found」——PartnerStack 侧计划确已关闭（与 7/17 api 返回 Company not found 互证）
- 唯一遗留路径：发邮件至 partnerships@looka.com 询问直签，优先级低，等主力平台链接铺满后再说

## 2026-07-24 下午
- **Gelato 申请已提交**（PartnerStack，身份 Blogger or Review Site，网站 aitoptools.net，受众 1,001-10,000，国家 Hong Kong，电话 +86 18126380255）→ 状态：申请待处理。条款：最高 12% × 12 个月。
- **Printify $150 挑战赛报名占位**（非收入） PartnerStack 活动记录：「Publish a blog post about Printify」系统记录"已赚取"$150 实为活动候选占位，每月仅抽 5 人发放，选中才生效，未选中记录消失——不计入收入，Printify 计划状态「已启用」。
- PartnerStack 收款+税务由用户本人完成：PayPal doolen@126.com，公司主体 SHENZHEN SHI CAILONG YINSHUA BAOZHUANG YOUXIAN GONGSI（深圳市彩龙印刷包装有限公司），地址深圳龙岗平湖华南城。
- 待办：Deel 申请等用户注册 LinkedIn 后补链接提交；Gelato 获批后链接入 AFFILIATE_LINKS.json 并跑替换管线。

## 2026-07-24 傍晚
- **Gelato 申请被拒**（Identity mismatch：Jerome Tang / ZPrintPro / aitoptools.net / "Print AI Tools" 身份链不一致）。根因：网站无运营者署名可交叉验证。
- **修复**：About 页新增 "Who Runs This Site" 板块（Jerome Tang = ZPrintPro = Print AI Tools，LinkedIn + 邮箱），页脚全站加运营者署名。commit 2382561 已 push（当日第 2 次，紧急修复例外）。
- **LinkedIn 已注册**：linkedin.com/in/jerome-tang-442ab8424（资料 5 项全齐，用户自行养号）。
- Deel 申请待提交：用户网络节点 ERR_CONNECTION_CLOSED，等恢复。
- **Gelato 重申已提交**（Business name 改为 Print AI Tools (ZPrintPro)，websites 加 LinkedIn，why-join 字段直接解释身份链并指向 About 页）→ 待审批。
- **Deel 申请已提交（搁置中）**：用户手动触碰字段解锁 PrimeVue 提交按钮后成功提交。状态：等待 PartnerStack 网络审批，批准后 Deel 申请自动发送。$1500/单，审核 >5 天。周五巡检盯。
- **《Mockey vs Placeit》对比页上线并经独立验证**（/compare/mockey-vs-placeit/，112KB）：三级推荐卡（Our Pick Mockey 4.3 / Also Great Placeit 4.0 / Budget Pick Mockey Free）+ 功能矩阵 + Better Value 定价标注 + FAQ 齐；Mockey 真联盟链接 ×2 已嵌。Placeit 侧 ?fpr=partner 占位，待 Impact 升级获批后统一替换。

## 2026-07-24 晚 · 账本更正（用户+外部复核确认）
- $150 为 Printify 内容挑战赛**报名占位**（每月抽 5 人），非保底收入；点击 1 次无转化。
- **当前真实佣金收入 = $0 / 目标 $3000**。辨别规则：PartnerStack 账单来源写活动名/challenge=碰运气奖励；写客户订单=真佣金。
- 第一美元只能靠：SEO 流量→点链接→注册/下单。内容量产和 GSC 数据是核心。
