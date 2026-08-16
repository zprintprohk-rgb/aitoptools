# 拍板看板（user 只看这里）

> 更新：2026-08-17 04:1x · K3 维护。无待拍板项时本表为空，您无需做任何事。

## 待拍板

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D11 🆕 | Q4 集群日历：Black Friday 集群 9/15 开产、Christmas 集群 10/1 开产（B 级扩写第二批顺位后移） | 涉及 9-11 月内容资源重排；Q4 是 $2,200 目标的胜负手（测算见 STRATEGY-2026-08-17 §六） | 1 min 回复「同意」 | ⏳ |
| D12 🆕 | legit-check 产线首批 10 篇选题确认（magicdrop 深化/gearlaunch/spocket/kittl/society6/teepublic/redbubble/gelato/postermywall/veed） | 新内容产线启动，选题方向拍板一次后续按模板自动跑 | 2 min | ⏳ |
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎是否启动 | 5 min | ⏳ |
| D6 | 补录 printful_session_cookie（登录 Printful 后台取 cookie 存 .hermes/secrets/） | Halloween 素材链下单的唯一阻塞（test-address 已就绪，阻塞点转移）；登录态不自动化 | 5 min | ⏳ **8/18 判定前，明天截止** |
| D7 | 配置 CF API token（或授权 dashboard 人工导出） | 8/19 GEO 首读数前置；无数据则 GEO 支柱决策空转 | 5 min | ⏳ **后天 8/19 前** |

~~D1 测试收货地址~~ → **已关闭**（test-address.json 8/10 就绪，周报实证；阻塞点转移为 D6）
~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭（8/12）

## 您的行动卡（3 项，均 5 分钟内，非拍板）

1. **Synthesia 邮件确认**（2 min）：后台状态 applied-pending-email-confirm，点确认链接即激活追踪——审批通过后 25% 首购佣金才能归因。
2. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → 8/1-15 clicks/conversions（指引见 .hermes/logs/2026-08-11-kittl-measure.md §二）——加投/撤位判定被它卡着（判定线 ≥5 点击/天加投）。
3. **Printify PartnerStack 站内催**（3 min，可选）：promo code 邮件 8/8 发出后 0 回复，8/14 已收口升级站内渠道；催到码即可建 /promo/ 页。

## 执行进展速览（无需动作）

- 8/17 🧠 **K3 战略修订已下发**（STRATEGY-2026-08-17）：GSC 8/17 批次确认三大里程碑——**史上首次自然点击**（8/13，gear-launch-review，CTR 5%）、**首个 top-20 页面**（is-magicdrop-legit pos 18.29）、**Halloween 集群两页已进首页**（pos 8.38 / 5.0）；7d 日均展示 316（+50% vs 上一批次）。新增三条战线：A 准首页冲刺 5 页 / B legit-check 信任验证产线（待 D12 拍板）/ C Q4 集群日历（待 D11 拍板）。归因警示：8/12-14 飙升含 Google 8 月核心更新洗牌成分，回吐至日均 <250 不恐慌。
- 8/16 ✅ **全量完成**：copy-ai 快修 + sitemap merged 版（27 单测 PASS，344 URL）+ 辐条①补正 + 11 篇 blog 补 publishedAt + **外链破冰 0→3/20 已提交**（AI Toolz Dir 200 / TheNextAI 审核 / Wired Business 注册）+ 排期治理 + 2 次 push 全部署（HEAD=a6ff975）+ IndexNow 3/3 200
- 8/15 ⚠️ **排期失控+push 违规**：外部实例提前执行了 8/17 Boost#5/#6、8/17 辐条①（不达标版）、8/18 llms、8/23 集群push、8/31 IndexNow、9/13 T30校准（deleteAfterRun 已删原任务）；当日实际 6 次 push（违反单日1push）。好消息：T+2 GSC 7d 日均展示 307.2（+56% vs 基线），Branch A 数据更强。
- 8/15 ✅ #1/#2 T+7 严格复核 + push 纪律切换为"产出即部署"
- 8/14 ✅ T+7 首读 Branch A 温和加速 + cron 丢失事件重建
- 联盟：W-8BEN-E Pending review（复核窗口今起 8/17-8/19）/ Synthesia 待邮件确认 / Kittl 激活无转化 / 累计 $0

## 近期日程（无需动作）

- 8/17: 承接待办（tax-audit/badge 验证/Boost#5#6 幂等/重建 T30 cron）+ **战线A magicdrop 扩写** + **战线B legit 模板** + 辐条①收尾 + GEO 读数准备 + 合并 1 push
- 8/18: Halloween deadline 判定（19:37，D6 cookie 为下单前置）
- 8/19: GEO 首读数（D7 CF token 为前置，dashboard 人工导出兜底）
- 8/21: print-price ≤30 里程碑 + #3/#4 T+7
- 8/22: Boost T+14 Branch A/B/C/D 判定
- 8/25: W3 万圣节全量push（98ebd150，需确认无重复）
- 9/13前: 重建 T30 校准 cron（原 02fee02d 被 deleteAfterRun 删除）
- 9/13: T+30 全量校准（V2 目标 $2,200 核验）
- 9/15: **Black Friday 集群开产**（待 D11 拍板）
- 9/29: Printify $150 博客挑战赛截止
- 10/1: Christmas 集群开产（待 D11 拍板）
