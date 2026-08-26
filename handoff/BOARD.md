# 拍板看板（user 只看这里）

> 更新：2026-08-26 21:2x · K3 维护。🎉 **Printify 优惠码 AITOOLTOOLS20 已诞生、promo 页已上线；D17 安全事件已闭环。** 破零链路只剩 W-8BEN 一块砖（行动卡 #1，3 分钟）。

## 待拍板（按杠杆排序）

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D12+D13 🔥 | **legit 产线放量解锁（内容第一杠杆）**：首批 10 篇选题 + 公开评分 rubric 一次拍板 | **4 篇成稿堵在门口**（spocket/kittl/society6/veed 核实全备）；拍板当日即部署 + 激活每晚放量 cron；9/13 目标 ≥10 篇当前 2 篇 | 2 min 回复「同意」 | ⏳ |
| D15 🔴 | **402/billing 根因（第二次实锤）**：充值 DeepSeek（或修复 c493 fallback key）或允许接 MINIMAX fallback | 8/25 billing cooldown 致全天 cron 停摆（继 8/18 后第二次）；绕行稳定但根因未解，单日停摆会复发 | 5 min | ⏳ 重新升级 |
| D11 | Q4 集群日历：Black Friday 集群 9/15 开产（剩 20 天）、Christmas 集群 10/1 开产 | BF 内容需 6-8 周排名成熟期，9/15 硬红线；**9/1 宽限截止（剩 6 天）**，未拍板则执行层按已备大纲先行核实 | 1 min 回复「同意」 | ⏳ 宽限至 9/1 |
| D6 🔄 | Christmas 素材链测试单路径：① 补录 Printful cookie ② 或拍板改走 Printify（已有联盟链路） | Printful cookie 不再是唯一路径；10/1 Christmas 开产前定即可 | 1 min 回复「走 Printify」 | ⏳ 新增选项 |
| D7 🔴 | 配置 CF API token（或按 .hermes/logs/geo-cf-analytics-export-fallback.md 人工导出，2 min） | CF AI-crawler 侧连续 NODATA 第 10 天——9/13 校准证据链持续被削弱 | 5 min | ⏳ 逾期 10 天 |
| D14 | 配置 GA4 service-account 凭证（ga4-service-account.json） | affiliate_click 与 AI Assistant 渠道自 8/11 起全盲；9/13 校准只能 GSC 单源 | 5 min | ⏳ |
| D16 | LaunchBuck 外链机会 #2（免费目录 + dofollow badge，launchbuck.com/submit） | 外链收录口径 1/20；站外提及 KPI 已标红（偏差 80%） | 1 min 回复「同意」 | ⏳ |
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎 | 5 min | ⏳ |
| ~~D17~~ ✅ | Gmail app password 轮换 | **8/24 已闭环**：secrets + .env 双处更新，IMAP/SMTP 冒烟通过，旧密码作废 | - | ✅ 已闭环 8/24 |

~~D1 测试收货地址~~ / ~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭

## 您的行动卡（均 5 分钟内，非拍板）

1. **W-8BEN 二选一（破零最后一块砖）**：① 重传：打开 `.hermes/tmp/W8BEN-Jerome-Tang-prefilled.pdf` 补填地址/生日/签名 → Printful Dashboard → Tax & Legal 上传（3 min）；② 或回复我「授权代发」，我用已备草稿给 Printful support 发第二封跟进（1 min）。
2. **GSC 重提 sitemap（1 min，悬崖排查联动）**：GSC UI → Sitemaps → 重新提交 sitemap.xml——lastDownloaded 仍停 7/17。
3. **Reddit 种子帖发布 ×3（合计 <10 min）**：草稿全备——seed-01 GearLaunch / seed-02 Spocket / seed-03 Kittl（.hermes/drafts/reddit-seed-0X.md），用个人账号发到 r/printondemand 等对应 sub。**这是标红 KPI（站外提及 1/5）最快的增量路径。**
4. **Bing Webmaster Tools 验证（5 min，ChatGPT 引用通道门票）**：bing.com/webmasters → 「Import from Google Search Console」一键导入。
5. **Synthesia 邮件确认**（2 min）：点确认链接即激活追踪。
6. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → clicks/conversions——加投/撤位判定被卡。
7. **跨项目：Supabase togthr-life 已暂停（8/24 落地）**——决定恢复（登录控制台 unpause，1 min）或接受暂停。

## 执行进展速览（无需动作）

- 8/26 🎉 **破零链路总装日**：**Printify 码 AITOOLTOOLS20 已创建（8/24）、/promo/printify-promo-code 页已上线**（sitemap 348 + IndexNow 2/2 200）；**print-price 回滚按预案执行**（pos 81.3 ≥ 67.75 触发，8/28 T+7 终判）；CF 周更帖刷新（282 槽）+ merger-fyul BLUF + Kittl review 更新；mention-ops 新产线启动（reddit-seed-03 成稿）。8/25 停摆根因定位 = deepseek billing cooldown（D15 第二次实锤）。push 2 次合规（内容+sitemap / 晚间批）。
- 8/24 ✅ 悬崖 Branch B 滚动期纪律执行良好；llms.txt 全量补齐 355 URL 部署；legit x2 按纪律正确悬置；**D17 轮换闭环**。
- 8/23 🔴 悬崖正式判定 = Branch B（曝光测试结束，排名资产无损）：滚动期至 9/6，禁恐慌改版；BF 战前准备完成。
- 8/22 🔴 P0 展示悬崖确认（-92%）+ T+14 复读收官（#3 magicdrop Branch A 首个达标）+ 破零链路双回复。
- 8/21 🧠 K3 九月月度战略下发（PLAN-2026-09-MONTHLY）：九月第一目标 = 佣金破零；GEO 规则修订；BF 9/15 红线。
- 联盟：W-8BEN 待重传（行动卡 #1）/ **Printify 码已到 + promo 页已上线 ✅** / 累计 $0 第 18 天 / 外链 1/20 LIVE

## 近期日程（无需动作）

- 8/27: billing 晨检 + 悬崖追踪 Day-5 + print-price T+7 终判前备 + **Printify $150 挑战资格问询草稿**（发送待您确认）+ legit 条件激活待命
- 8/28: **print-price 方案 A T+7 终判**（恢复原词位=回滚成功；继续跌=方案 A 证伪）
- 8/26-8/30: Printify 挑战资格确认窗口（资格未定前不制作投稿内容）
- 9/1: **D11 宽限截止（剩 6 天）**；North Star 月度读数；Halloween title/meta CTR 终审
- 9/6: 悬崖滚动期纪律结束
- 9/13: **T+30 全量校准** + AI 引用审计第二轮（站外提及若 <3，12 月目标下调一档）
- 9/15: **Black Friday 集群开产**（硬红线，剩 20 天）
- 9/29: Printify $150 博客挑战赛截止
- 10/1: Christmas 集群开产（待 D11）
