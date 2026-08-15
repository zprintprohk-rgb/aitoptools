# 拍板看板（user 只看这里）

> 更新：2026-08-16 03:55 · K3 维护。无待拍板项时本表为空，您无需做任何事。

## 待拍板

| # | 事项 | 为什么必须您来 | 耗时 | 状态 |
|---|---|---|---|---|
| D5 | 回填 3 个经营数据：Printful 佣金比例 / 月运营成本 / Pinterest 做不做 | 决定盈亏平衡点计算与第二流量引擎是否启动 | 5 min | ⏳ |
| D6 | 补录 printful_session_cookie（登录 Printful 后台取 cookie 存 .hermes/secrets/） | Halloween 素材链下单的唯一阻塞（test-address 已就绪，阻塞点转移）；登录态不自动化 | 5 min | ⏳ 8/18 判定前 |
| D7 | 配置 CF API token（或授权 dashboard 人工导出） | 8/19 GEO 首读数前置；无数据则 GEO 支柱决策空转 | 5 min | ⏳ 8/19 前 |

~~D1 测试收货地址~~ → **已关闭**（test-address.json 8/10 就绪，周报实证；阻塞点转移为 D6）
~~D2 GSC OAuth~~ / ~~D3 CF beacon~~ / ~~D4 Impact 登录~~ → 已关闭（8/12）

## 您的行动卡（3 项，均 5 分钟内，非拍板）

1. **Synthesia 邮件确认**（2 min）：后台状态 applied-pending-email-confirm，点确认链接即激活追踪——审批通过后 25% 首购佣金才能归因。
2. **Kittl Impact 数据回填**（5 min）：app.impact.com → Kittl 项目 → 8/1-15 clicks/conversions（指引见 .hermes/logs/2026-08-11-kittl-measure.md §二）——加投/撤位判定被它卡着（判定线 ≥5 点击/天加投）。
3. **Printify PartnerStack 站内催**（3 min，可选）：promo code 邮件 8/8 发出后 0 回复，8/14 已收口升级站内渠道；催到码即可建 /promo/ 页。

## 执行进展速览（无需动作）

- 8/16 ⏳ **今日主任务已排期**（cron 84c86e36，07:15 触发；03:50 声明的 11524761611778 未落库，主线 03:53 已重建并字节级核验在库）：T1 copy-ai-review 快修 + T2 sitemap 脚本替换（merged 版+27单测）+ T3 辐条①补正（保留 slug 补字段+截图）+ T3b 全 11 篇 blog 补 publishedAt + T4 外链提交（user 授权全权处理）+ T5 排期治理 + T6 根目录卫生 + T7 合并 1 push + T8 RESULT-0816。原 W1-0816（de9fad65）因 gateway restart 超时失败 3 次被系统禁用，已重建。⚠️ 观察项（R-14）：cron 工具视图与任务库背离（list/get 不可见、jobs.json 权威库完好），07:15 触发预计不受影响，执行后复核；另有会话 03:40 起每分钟无效 cron.add（178 次全被拒，不写库），T5 排查来源。
- 8/15 ⚠️ **排期失控+push 违规**：外部实例提前执行了 8/17 Boost#5/#6、8/17 辐条①（不达标版）、8/18 llms、8/23 集群push、8/31 IndexNow、9/13 T30校准（deleteAfterRun 已删原任务）；当日实际 6 次 push（违反单日1push）。好消息：T+2 GSC 7d 日均展示 307.2（+56% vs 基线），Branch A 数据更强。
- 8/15 ✅ #1/#2 T+7 严格复核 + push 纪律切换为"产出即部署"
- 8/14 ✅ T+7 首读 Branch A 温和加速 + cron 丢失事件重建
- 联盟：W-8BEN-E Pending review / Synthesia 待邮件确认 / Kittl 激活无转化 / 累计 $0

## 近期日程（无需动作）

- 8/16 07:15: B类快修(copy-ai) + sitemap脚本替换 + 辐条①补正 + 全blog补publishedAt + 外链提交 + 排期治理 + 合并1push + RESULT-0816（cron 84c86e36）
- 8/17: Boost #5/#6 幂等验证（已提前部署，预期 NOOP）+ geo-technical + radar + mining
- 8/18: Halloween deadline 判定（19:37，D6 cookie 为下单前置）
- 8/19: GEO 首读数（D7 CF token 为前置）
- 8/21: print-price ≤30 里程碑 + #3/#4 T+7
- 8/22: Boost T+14 Branch A/B/C/D 判定
- 8/25: W3 万圣节全量push（98ebd150，需确认无重复）
- 9/13前: 重建 T30 校准 cron（原 02fee02d 被 deleteAfterRun 删除）
- 9/13: T+30 全量校准（V2 目标 $2,200 核验）
- 9/29: Printify $150 博客挑战赛截止
