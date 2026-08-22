# 拍板看板（user 只看这里）

> 更新：2026-08-22 21:2x · K3 维护。**🔴 当前第一优先是排查展示悬崖（8/18 起 -92%），行动卡 #3 的 GSC 重提 sitemap 只需 1 分钟。** 拍板项按杠杆排序不变。

## 待拍板（按杠杆排序）

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D17 🔴 | **Gmail app password 立即轮换（P0 安全事件）**：Google 账户 → 安全 → 应用专用密码 → 删除旧密码并新建 → 告诉我，我更新本地 secrets/gmail_credentials.json | 旧密码在公开仓库历史暴露 18 天，任何人可提取；不换则联盟审批监控链也有被恶意中断的风险 | 5 min | ⏳ **最优先（安全）** |
| D15 🔴 | **402 模型余额 + autoglm credits**：① 充值 DeepSeek（或修复 c493 fallback key）② 或允许接 MINIMAX fallback；autoglm "No credits left" 需充值/确认恢复 | 今日 web_search 仍 insufficient_credits；浏览器任务（W-8 复核/GEO beacon/外链提交）全部受阻 | 5 min | ⏳ |
| D12+D13 | **legit 产线放量解锁**：首批 10 篇选题 + 公开评分 rubric（Trustpilot 30%/退款 25%/透明度 25%/实测 20%）一次拍板 | 备战已囤到 #10（事实核实全备）；不拍板产线只能维持 pilot 蜗牛速 | 2 min 回复「同意」 | ⏳ |
| D11 | Q4 集群日历：Black Friday 集群 9/15 开产（剩 24 天）、Christmas 集群 10/1 开产 | BF 内容需 6-8 周排名成熟期，9/15 是硬红线；9/1 宽限截止后执行层将先行备战 | 1 min 回复「同意」 | ⏳ 宽限至 9/1 |
| D7 🔴 | 配置 CF API token（或按 .hermes/logs/geo-cf-analytics-export-fallback.md 人工导出，2 min） | CF AI-crawler 侧连续 NODATA 第 6 天——9/13 校准证据链正在被削弱 | 5 min | ⏳ 逾期 6 天 |
| D14 | 配置 GA4 service-account 凭证（ga4-service-account.json） | affiliate_click 与 AI Assistant 渠道自 8/11 起全盲；9/13 校准只能 GSC 单源 | 5 min | ⏳ |
| D16 | LaunchBuck 外链机会 #2（免费目录 + dofollow badge，launchbuck.com/submit） | 外链收录口径 1/20，每个 dofollow 直接服务域名权威 | 1 min 回复「同意」 | ⏳ |
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎 | 5 min | ⏳ |
| ~~D6~~ ✅ | printful_session_cookie | 8/19 判定已闭环：未就位 → 下单链挂起，Halloween 内容线关闭（5/5 已上线），素材链转 Christmas 10/1 再激活 | - | ✅ 已闭环 |

~~D1 测试收货地址~~ → **已关闭**（test-address.json 8/10 就绪）
~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭（8/12）

## 您的行动卡（8 项，均 5 分钟内，非拍板）

1. **W-8BEN 重传（3 min，破零最短路径）**：Printful support 8/21 回复说原文件不可读需重传——打开 `.hermes/tmp/W8BEN-Jerome-Tang-prefilled.pdf` → 补填地址/生日/签名 → Printful Dashboard → Tax & Legal 上传 → 完成告诉我复核（填表指引：.hermes/logs/w8ben-fill-guide-0822.md）。
2. **Printify 回信码名（1 min）**：Printify 8/21 回复愿给 20% off 码——回复 affiliate@printify.com 邮件，码名建议 **AITOOL20**；码到即建 /promo/printify-promo-code 页。
3. **GSC 重提 sitemap（1 min，悬崖排查联动）**：GSC UI → Sitemaps → 重新提交 sitemap.xml——GSC 端 lastDownloaded 停在 7/17 已 36 天、indexed 显示 0，与 8/18 起展示 -92% 的排查直接相关。
4. **autoglm credits 充值/确认恢复**——浏览器任务全受阻（W-8 复核 / GEO beacon / S3 提交），今日 web_search 也报 insufficient_credits。
5. **Bing Webmaster Tools 验证（5 min，ChatGPT 引用通道门票）**：bing.com/webmasters → 选「Import from Google Search Console」一键导入。
6. **Reddit 种子回答发布（3 min）**：草稿已就绪（.hermes/drafts/reddit-seed-01.md）——复制到 r/printondemand 发布即可（GEO 新规则：品牌站外提及 = AI 引用第一因子）。
7. **Synthesia 邮件确认**（2 min）：点确认链接即激活追踪。
8. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → 8/1-15 clicks/conversions——加投/撤位判定被卡。

## 执行进展速览（无需动作）

- 8/22 🔴 **P0 展示悬崖确认 + T+14 复读收官**：8/18 起全站展示 -92%（447→30/日，query 321→12），GSC sitemap 端 36 天失联（indexed 0）但排名位置稳定 → 指向索引/覆盖层，**8/23 正式判定**（判定树已预登记：滞后/算法回吐/索引故障三分支各配动作）。T+14 严格复读：#3 magicdrop Branch A 维持（页级 14.21 历史最佳）、#1 Branch B、#2 runway 转 Branch C（发现是孤儿页，0 站内入链）；print-price -9.17 首触回滚阀值（8/23-24 连续窗确认）。**破零链路双回复**：Printful 要 W-8 重传（预填 PDF 已备）、Printify 愿给 20% 码（待回信码名）。push 1 次 ✅ 合规。
- 8/21 晚 🧠 **K3 九月月度战略下发**（PLAN-2026-09-MONTHLY，PHASE 级）：① 九月第一目标 = **佣金破零**；② GEO 规则修订——品牌站外提及相关性 0.664（外链 3 倍），legit 簇 pos 12-35 即刻具备 AI 引用资格；③ BF 9/15 红线维持；④ 目标模式四指标（legit≥10 / 收录≥5 / 日均≥500 / top-20≥5）。
- 8/21 ✅ **T+14 判定日**：#3 magicdrop 12.93 **Branch A（首个 Boost 达标里程碑）**；merger-fyul 扩写 + Kittl 定价修正上线；W-8 问询 + Printify 催办两封邮件已发（8/22 均获回复）。
- 8/21 🔴 P0 安全事件已处置（脱敏完成，根治=D17 轮换）。
- 8/19 ✅ GEO 首读数 GSC 侧落地（词量 +48%）；is-gearlaunch-legit 上线；CF 周更帖刷新。
- 8/17 ✅ Halloween 提前 8 天全量上线（5/5 页）+ legit 产线启动 + 外链首收录。
- 联盟：W-8BEN 待重传（行动卡 #1）/ Printify 20% 码待回信（行动卡 #2）/ 累计 $0 第 14 天 / 外链 1/20 LIVE

## 近期日程（无需动作）

- 8/23: **🔴 悬崖正式判定日**（判定树落盘）+ print-price 回滚确认窗 Day-1 + BF 集群战前准备（不依赖 D11）+ weekly-review 悬崖专项
- 8/24: print-price 确认窗 Day-2（持续跌 → 回滚 H1）+ Boost #5/#6 T+7 + CF freebie 下轮监控
- 8/25: W3-0825 cron 冗余触发 NOOP——**建议删除，等您一个「删」字**；W-8 无回复则第二封 + Impact 工单
- 8/28: print-price 方案 A T+7 复读
- 9/1: D11 宽限截止（未拍板则 BF 先行备战）；North Star 月度读数；Halloween title/meta CTR 终审
- 9/10: T+30 数据收口 → 9/13: **T+30 全量校准** + AI 引用审计第二轮（对比 8/21 的 0 条基线）
- 9/15: **Black Friday 集群开产**（硬红线，待 D11，剩 24 天）
- 9/29: Printify $150 博客挑战赛截止
- 10/1: Christmas 集群开产（待 D11）
