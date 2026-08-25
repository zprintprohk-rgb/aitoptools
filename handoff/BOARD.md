# 拍板看板（user 只看这里）

> 更新：2026-08-24 21:2x · K3 维护。悬崖已判定 **Branch B**（核心更新曝光测试结束，排名资产无损），滚动期至 9/6 不恐慌改版。**行动卡 #1-#3 是破零链路最后的物理障碍，合计 5 分钟。**

## 待拍板（按杠杆排序）

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D17 🔴 | **Gmail app password 立即轮换（P0 安全事件，第 4 天）**：Google 账户 → 安全 → 应用专用密码 → 删除旧密码并新建 → 告诉我，我更新本地 secrets/gmail_credentials.json | 旧密码在公开仓库历史暴露 21 天，任何人可提取；gmail_credentials.json 至今未换（mtime 8/7） | 5 min | ⏳ **最优先（安全）** |
| D12+D13 🔥 | **legit 产线放量解锁（内容第一杠杆）**：首批 10 篇选题 + 公开评分 rubric 一次拍板 | **已到成稿积压阶段**：spocket/kittl 2 篇成稿 + 事实核实 3/3（Trustpilot 数据全）+ bug 修复全部就绪，拍板当日即部署 + 激活每晚 19:47 放量 cron；每拖一天 = 2 篇/日复利损失 | 2 min 回复「同意」 | ⏳ |
| D15 | **402 模型余额根因**：充值 DeepSeek（或修复 c493 fallback key）或允许接 MINIMAX fallback | autoglm/web_search 已恢复（8/24）✅；余下仅 DeepSeek 侧——绕行（deepseek-v4-flash 显式）目前稳定 0 发作，但根因未解 | 5 min | ⏳ 降级（autoglm 已恢复） |
| D11 | Q4 集群日历：Black Friday 集群 9/15 开产（剩 22 天）、Christmas 集群 10/1 开产 | BF 内容需 6-8 周排名成熟期，9/15 是硬红线；9/1 宽限截止后执行层先行备战（BF 关键词核实 + 支柱大纲 + 试产草稿已备） | 1 min 回复「同意」 | ⏳ 宽限至 9/1 |
| D7 🔴 | 配置 CF API token（或按 .hermes/logs/geo-cf-analytics-export-fallback.md 人工导出，2 min） | CF AI-crawler 侧连续 NODATA 第 8 天——9/13 校准证据链正在被削弱 | 5 min | ⏳ 逾期 8 天 |
| D14 | 配置 GA4 service-account 凭证（ga4-service-account.json） | affiliate_click 与 AI Assistant 渠道自 8/11 起全盲；9/13 校准只能 GSC 单源 | 5 min | ⏳ |
| D16 | LaunchBuck 外链机会 #2（免费目录 + dofollow badge，launchbuck.com/submit） | 外链收录口径 1/20，每个 dofollow 直接服务域名权威 | 1 min 回复「同意」 | ⏳ |
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎 | 5 min | ⏳ |
| ~~D6~~ ✅ | printful_session_cookie | 8/19 判定已闭环：未就位 → 下单链挂起，素材链转 Christmas 10/1 再激活 | - | ✅ 已闭环 |

~~D1 测试收货地址~~ → **已关闭**（test-address.json 8/10 就绪）
~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭（8/12）

## 您的行动卡（8 项，均 5 分钟内，非拍板）

1. **W-8BEN 重传（3 min，破零最短路径）**：打开 `.hermes/tmp/W8BEN-Jerome-Tang-prefilled.pdf` → 补填地址/生日/签名 → Printful Dashboard → Tax & Legal 上传 → 完成告诉我复核（指引：.hermes/logs/w8ben-fill-guide-0822.md）。
2. **Printify 回信码名（1 min）**：Printify 8/21 回复愿给 20% off 码——回复 affiliate@printify.com，码名建议 **AITOOL20**；码到即建 /promo/printify-promo-code 页。
3. **GSC 重提 sitemap（1 min，悬崖排查联动）**：GSC UI → Sitemaps → 重新提交 sitemap.xml——GSC 端 lastDownloaded 停在 7/17、indexed 显示 0。
4. **Bing Webmaster Tools 验证（5 min，ChatGPT 引用通道门票）**：bing.com/webmasters → 选「Import from Google Search Console」一键导入。
5. **Reddit 种子回答发布（3 min）**：草稿已就绪（.hermes/drafts/reddit-seed-01.md）——复制到 r/printondemand 发布即可（GEO 新规则：品牌站外提及 = AI 引用第一因子）。
6. **Synthesia 邮件确认**（2 min）：点确认链接即激活追踪。
7. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → 8/1-15 clicks/conversions——加投/撤位判定被卡。
8. **跨项目：Supabase togthr-life 保活（1 min）**——8/23 收暂停预警（7 天无活动将暂停），登录 dashboard 一次即可。

~~autoglm credits~~ ✅ 8/24 已恢复（雷达/事实核实链路解锁）。

## 执行进展速览（无需动作）

- 8/24 ✅ **悬崖滚动期纪律执行良好 + 产线蓄势**：Branch B 第 2 天（8/21=17 仍探底，不恐慌改版）；print-price Day-2 NODATA 顺延（8/25 复读判定：pos<67.75 作废 / ≥67.75 回滚）；**legit x2 成稿+核实+bug 修复全就绪、按 BOARD 纪律正确悬置**（19:23 复跑零改动自律）；llms.txt 全量补齐 355 URL 已部署；雷达解锁（Kittl AI Style / Recraft 300DPI 候选）；push 1 次 ✅（连续 2 天合规）。
- 8/23 🔴 **悬崖正式判定 = Branch B**（核心更新曝光测试结束 / 均匀低展示 / 位置稳 / 页在索引，判定书 cliff-verdict-0823.md）：滚动期纪律延长至 9/6，产线节奏不变，禁止恐慌改版。BF 战前准备完成（关键词 5 词核实 0 imp 正常 + 辐条②试产骨架）。
- 8/22 🔴 P0 展示悬崖确认（-92%）+ T+14 复读收官（#3 magicdrop Branch A 首个达标）+ 破零链路双回复（Printful W-8 重传要求 / Printify 愿给 20% 码）。push 1 次 ✅。
- 8/21 🧠 **K3 九月月度战略下发**（PLAN-2026-09-MONTHLY）：九月第一目标 = 佣金破零；GEO 规则修订（站外提及 = AI 引用第一因子）；BF 9/15 红线；T+14 判定日落盘。
- 8/19 ✅ GEO 首读数 GSC 侧落地（词量 +48%）；is-gearlaunch-legit 上线。
- 联盟：W-8BEN 待重传（行动卡 #1）/ Printify 20% 码待回信（行动卡 #2）/ 累计 $0 第 16 天 / 外链 1/20 LIVE

## 近期日程（无需动作）

- 8/25: **print-price 复读判定日** + W3-0825 原 Halloween 节点（cron 自检 NOOP，严禁重复 push）+ CF 周更帖刷新窗（素材池 ~60 🎃）+ W-8 第二封跟进文案备（发送待您确认）
- 8/28: print-price 方案 A T+7 终判（回滚或加码定案）
- 9/1: D11 宽限截止（未拍板则 BF 先行备战，已备）；North Star 月度读数；Halloween title/meta CTR 终审
- 9/6: 悬崖滚动期纪律结束（恢复正常评估）
- 9/10: T+30 数据收口 → 9/13: **T+30 全量校准** + AI 引用审计第二轮（对比 8/21 的 0 条基线）
- 9/15: **Black Friday 集群开产**（硬红线，待 D11，剩 22 天）
- 9/29: Printify $150 博客挑战赛截止
- 10/1: Christmas 集群开产（待 D11）
