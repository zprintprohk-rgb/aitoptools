# 拍板看板（user 只看这里）

> 更新：2026-08-21 19:5x · K3 维护。拍板项已按杠杆重排——前 3 项解锁后，自动化与产线立刻全速。**本周吞吐目标：D17 + D15 + D12/D13 三项。**

## 待拍板（按杠杆排序）

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D17 🔴 | **Gmail app password 立即轮换（P0 安全事件）**：旧密码在公开仓库历史暴露 18 天（已脱敏但根治靠轮换）——Google 账户 → 安全 → 应用专用密码 → 删除旧密码并新建 → 告诉我，我更新本地 secrets/gmail_credentials.json | 任何人可从公开历史提取旧密码；且不换则 IMAP 联盟审批监控链随时可能被人恶意触发改密后中断 | 5 min | ⏳ **最优先（安全）** |
| D15 🔴 | **402 模型余额 + autoglm credits（第 4 天，已超升级线）**：① 充值 DeepSeek（或修复 c493 fallback key）② 或允许接 MINIMAX fallback；autoglm "No credits left" 需充值/确认恢复 | 8/18 全天 cron 已整批失败过一次；今日 0 发作只是欠费间歇，根因未解；浏览器任务（W-8 复核/GEO beacon/外链提交）全部受阻 | 5 min | ⏳ |
| D12+D13 | **legit 产线放量解锁**：首批 10 篇选题 + 公开评分 rubric（Trustpilot 30%/退款 25%/透明度 25%/实测 20%）一次拍板 | 执行层草稿已囤饱和（模板 v2 + 前 5 篇事实核实全备好）；不拍板产线只能维持 pilot 蜗牛速——当前增长引擎最大的闲置 | 2 min 回复「同意」 | ⏳ |
| D11 | Q4 集群日历：Black Friday 集群 9/15 开产（剩 26 天）、Christmas 集群 10/1 开产 | Q4 是 $2,200 目标的胜负手；BF 内容需 6-8 周排名成熟期，9/15 是硬红线 | 1 min 回复「同意」 | ⏳ |
| D7 🔴 | 配置 CF API token（或按 .hermes/logs/geo-cf-analytics-export-fallback.md 人工导出，2 min） | GEO 首读数 GSC 侧已完成（+48% 词量），CF AI-crawler 侧连续 NODATA 第 4 天——AI 爬虫是否转化成引用完全盲 | 5 min | ⏳ 逾期 4 天 |
| D14 | 配置 GA4 service-account 凭证（ga4-service-account.json） | affiliate_click 与 AI Assistant 渠道自 8/11 起全盲；9/13 校准只能 GSC 单源 | 5 min | ⏳ |
| D16 | LaunchBuck 外链机会 #2（免费目录 + dofollow badge，launchbuck.com/submit） | 外链收录口径 1/20，每个 dofollow 直接服务域名权威 | 1 min 回复「同意」 | ⏳ |
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎 | 5 min | ⏳ |
| ~~D6~~ ✅ | printful_session_cookie | 8/19 判定已闭环：未就位 → 下单链挂起，Halloween 内容线关闭（5/5 已上线），素材链转 Christmas 10/1 再激活 | - | ✅ 已闭环 |

~~D1 测试收货地址~~ → **已关闭**（test-address.json 8/10 就绪）
~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭（8/12）

## 您的行动卡（7 项，均 5 分钟内，非拍板）

1. **W-8BEN-E 跟进已发（8/21）→ 只需等回复**：若收到 Printful 回复告诉我；8/25 仍无回复我出第二封 + Impact 工单。
2. **autoglm credits 充值/确认恢复**——浏览器任务全受阻（W-8 复核 / GEO beacon / S3 提交）。
3. **Bing Webmaster Tools 验证（5 min，ChatGPT 引用通道门票）**：bing.com/webmasters → 选「Import from Google Search Console」一键导入。
4. **Reddit 种子回答发布（3 min）**：草稿已就绪（.hermes/drafts/reddit-seed-01.md，GearLaunch legit 主题）——复制到 r/printondemand 发布即可。**（GEO 新规则下权重升级：品牌站外提及 = AI 引用第一因子，见 PLAN-09 §三）**
5. **Synthesia 邮件确认**（2 min）：点确认链接即激活追踪——审批后 25% 首购佣金才能归因。
6. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → 8/1-15 clicks/conversions——加投/撤位判定被卡。
7. **Printify PartnerStack 站内催**（3 min，可选）：promo code 邮件 8/8 发出、8/21 已催办；催到码即可建 /promo/ 页。

## 执行进展速览（无需动作）

- 8/21 晚 🧠 **K3 九月月度战略下发**（PLAN-2026-09-MONTHLY，PHASE 级）：① 九月第一目标 = **佣金破零**（结算链验证优先于展示数字）；② GEO 规则修订——AIO top-10 重叠率 76%→38%、品牌站外提及相关性 0.664（外链 3 倍），legit 簇 pos 12-35 即刻具备 AI 引用资格，站外提及升级为与外链并列主引擎；③ BF 9/15 红线维持，W1 预置备战不依赖拍板；④ AutoClaw 目标模式四指标（legit≥10 / 收录≥5 / 日均≥500 / top-20≥5）。
- 8/21 ✅ **T+14 判定日落盘**：#3 magicdrop 12.93 **Branch A（首个 Boost 达标里程碑）**；#1 Branch B；#2 runway 悬置（8/22 严格复读）；#4 print-price 方案 A 已部署（8/28 复读）。merger-fyul 扩写 + Kittl 定价全站修正上线；W-8 问询 + Printify 催办两封邮件已发。
- 8/21 🔴 **P0 安全事件已处置**：Gmail app password 公开暴露 18 天 → 工作副本+线上均已脱敏（b268b7d）；根治 = D17 轮换。

- 8/19 晚 ✅ **8/18 故障缺口已全补 + GEO 首读数落地**：is-gearlaunch-legit 上线（2,562 词 8 FAQ 全带源，blog 14 篇）；printful-vs-printify CTR 修复部署（title 77→57）；GEO GSC 侧首读 **queries +48% / imp +36%**，magicdrop 26.0 六连升；CF 周更帖刷新至 Aug 19（素材池 45）。GSC 日均展示 ~447（+19%，月化 ~1.34 万，9/13 目标 2 万在轨）。⚠️ 当日实测 4 push 仍超标（含 8/18 补偿因素；已加硬纪律：除 sitemap 新 URL 外一切攒到末次 cron 单次 push，台账以 git reflog 为准）。autoglm credits 耗尽 + W-8 超窗未复核——凭证类全部转入上方行动卡。
- 8/19 晨 🧠 **K3 战略修订 v2**（STRATEGY-2026-08-19）：① GEO 兑现时点提前（AIO 引用 top-10 份额 <54%，pos 17-30 的 legit 簇现在就是引用候选）；② Bing/ChatGPT 升为第一站外 GEO 通道（技术因子全命中，只差 BWT 验证=行动卡 #3）。
- 8/17 晚 🧠 **K3 全局战略升级**（DEEPDIVE-2026-08-17-GEO-SEO-MASTERPLAN，PHASE 级）：三引擎一底座——legit 产线放量 / Q4 季节日历 / 准首页 answer-first 冲刺 + 外链收录运营与 GA4 测量闭环。Q4 占 POD 全年 40-60% 收入，是 $2,200 北极星唯一现实路径。
- 8/17 晚 ✅ **Halloween 提前 8 天全量上线（5/5 页）+ legit 产线启动**：外链首收录 Wired Business LIVE。
- 8/16 ✅ 全量完成：sitemap merged（344 URL）+ 外链破冰 0→3/20 已提交。
- 8/15 ⚠️ 排期失控+push 违规（当日 6 push）；GSC 日均 307（+56%）。
- 联盟：W-8BEN-E 超窗待自查 / Synthesia 待确认 / Kittl 无转化 / 累计 $0 第 12 天 / 外链 1/20 LIVE + 2 SUBMITTED + LaunchBuck 待拍板

## 近期日程（无需动作）

- 8/22: **#1/#2 严格 T+14 复读 + runway URL Inspection** + print-price 方案 A 复核（K3 已确认维持）+ legit #9-10 备战 + 合并 1 push
- 8/24 前后: CF freebie 下轮刷新监控
- 8/25: W3-0825 cron（98ebd150）冗余触发 NOOP——**建议删除，等您一个「删」字**；W-8 第二封跟进（若无回复）
- 8/28: print-price 方案 A T+7 复读（回滚阀值：主词跌 >5 位）
- 9/1: D11 宽限截止 → 未拍板则 BF 集群先行事实核实备战；North Star 月度读数
- 9/4: Shopify $150 联盟申请（行动卡）
- 9/10: T+30 数据收口 → 9/13: **T+30 全量校准**（V2 目标 $2,200 核验 + AI 引用审计第二轮）
- 9/15: **Black Friday 集群开产**（硬红线，待 D11）
- 9/29: Printify $150 博客挑战赛截止
- 10/1: Christmas 集群开产（待 D11）
