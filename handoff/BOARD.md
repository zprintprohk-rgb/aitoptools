# 拍板看板（user 只看这里）

> 更新：2026-08-15 08:15 · 千问 3.8-Max 维护。无待拍板项时本表为空，您无需做任何事。

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

- 8/15 ✅ #1/#2 T+7 严格复核：stickermule 36.0 保持（28d 337 展示全站第 1）/ runway 65.2 微降已处置（GEO 3 项修复+定价表扩写 2161→3475 字符）；当日 push 1 次（B 类快修+Boost #5/#6+W-8 上传+修复）；**push 纪律切换为"产出即部署"**（您 8/15 拍板）
- 8/14 ✅ **T+7 首读数完成：Branch A 温和加速**（日均展示 216.5，+10%；print-price +4.0 / kittl +4.6 / manychat +6.6；copy ai -7.5 入快修）；GSC API 实时源启用（DATA_STALE 解除）；sitemap 重复 bug 应急修复
- 8/14 ⚠️ **cron 丢失事件**：10 个既有 cron 全部消失（疑似 Gateway 重启存储丢失）→ 已按配置重建 11 个，恢复基准已存档；重建窗口无执行缺口
- 8/13 ✅ Boost #3/#4 完成（4/25）+ IndexNow 4/4 200 + 死链 2 条修复 + 周更帖刷新；cron 模型凭证 4 连 401 已恢复
- 8/12 ✅ 战略 v2.0 三支柱下发 + Kittl 全量激活（260 处 CTA）+ GSC 通道打通
- 联盟：W-8BEN-E 已上传 Pending review / Synthesia 待邮件确认 / Kittl 激活无转化（待 Impact 数据）/ 累计 $0

## 近期日程（无需动作）

- 8/16: B 类快修 + sitemap bug 修复 + S1 扩写启动 + S3 外链首批 8 站（当日合并 push）
- 8/17: 辐条① Halloween 实测发布 + geo-technical + radar + Boost #5/#6 幂等验证
- 8/18: Halloween deadline 判定（19:37，D6 为下单前置）
- 8/19: GEO 首读数（09:00，D7 为前置）
- 8/21: print-price ≤30 里程碑 + #3/#4 T+7
- 8/22: Boost T+14 Branch A/B/C/D 判定
- 9/13: T+30 全量校准（V2 目标 $2,200 核验）
- 9/29: Printify $150 博客挑战赛截止（规则已核实：月访客 1000 门槛当前不满足，ALLOWED-WITH-CONDITIONS）
