# 联盟申请审批监控 — 2026-09-12 (12:1x CST)

**任务**: aitoptools-affiliate-monitor (job 95f431cc7a95) · **模型**: deepseek-v4-flash · **TTL**: 30 min
**当前动作支撑赚钱目标**: CPA/CPS 佣金/月 — 恢复 15 天中断的联盟审批监控 + 定位 402 停摆根因，保护全部联盟归因链路

---

## 🔴 P0 — 置顶升级 (离钱最近)

### P0-1 · DeepSeek 余额仅 ¥1.59，全链 15 天停摆根因 = fallback 未接线 【超期 13 天】

| 项 | 证据 |
|---|---|
| 停摆区间 | **2026-08-28 → 2026-09-11，共 15 天，全部 cron 运行 100% 失败** |
| 错误 | `RuntimeError: HTTP 402: Insufficient Balance` |
| 受影响任务 | affiliate-monitor 15/16 · daily-content 15/15 · gsc-indexnow 15/15 · daily-radar 7/7 · weekly-report 2/2 · zprintpro-daily-seo 15/15 · 备份数据库 56/59 |
| 最后有效产物 | 2026-09-02 (commit `3a343be`)；线上无损坏 (site 200，本地 CSS `41d6f17fd1783abd` = 线上) |
| 根因 | `config.yaml` 第 512 行起 `fallback_model` **整段被注释**（`# provider: openrouter`）→ deepseek 402 后无任何 failover；`.env` 已有 `MINIMAX_CN_API_KEY` 但未接线 |
| 当前余额 | DeepSeek `/user/balance` 实查：`is_available=true`, **total_balance = 1.59 CNY** (granted 0.00 / topped_up 1.59) |
| 恢复信号 | 今日 12:06 本 run 首次跑通（今日 3 runs / 0 failed） |

**⚠️ 判定：¥1.59 只够数轮，今晚 19:45 daily-content 极可能再次 402。必须二选一：**
- (a) 充值 DeepSeek（web 控制台，最低档即可）
- (b) `config.yaml` 接 fallback（`fallback_model` 解除注释 + `provider: minimax` + `model: minimax/minimax-m3`），
  已备 `MINIMAX_CN_API_KEY`，一次性根治 15 天循环

---

## 📊 §2.1 状态表 (按 P0 / P1 / P2 排序)

| 级别 | 项 | 状态 | 证据 / 待办 |
|---|---|---|---|
| **P0** | DeepSeek 余额 ¥1.59 + fallback 未接 | 🔴 今晚必再 402 | balance API 实查 + executions.db 15 天全失败 |
| **P1** | Printful W-8BEN 重传 | 🔴 第 22 天未动 | 8/21 Noelle 要求重传 unreadable 文件；8/30 browser 实读 Pending；`payout_ready=false` = 联盟破零唯一税务闸门 |
| **P1** | filter_senders 漂移 | 🟡 待批准修复 | `gmail_credentials.json` 缺 `creativefabrica.com` / `newsletter.printful.com` / `partners.claid.ai` / `affiliate.printify.com` → 本轮 25 封过滤命中 **0**；本轮改用 domain 全量分组扫描绕过（未动凭证文件） |
| **P1** | Synthesia 邮箱确认 | 🟡 第 32 天待 user | 8/11 确认邮件，SINCE<90d 不自动点击；2x 密码重置待 user 确认是否本人 |
| **P1** | Placeit 催办 | 🟡 pending 超期 29 天 | 草稿 `drafts/placeit-followup-email.md` 版 B 就绪，user 手动发送 |
| **P2** | Printify promo 页 | ⏸️ 码已到未建页 | 码 `AITOOLTOOLS20` 8/24 创建；`/promo/printify-promo-code` 因 402 未建（PUSH_READY 遗留） |
| **P2** | 内容冻结 9/3–9/11 | ⏸️ 待恢复 | 零内容产出；恢复后需补产出 + sitemap/IndexNow 补推 |
| **P2** | Printify 佣金率口径 | 📝 记账 | 8/31 邮件原文称 **5%**/12 个月，与 SSoT 记 20–30% 不符，待 dashboard 实查 |

**已部署核查**: 8 个 approved/active 程序 (NordVPN / Mockey / Gelato / Printify / Claid / Kittl / Printful) **全部 `link_deployed: true`** → P0 部署缺口 = **0**
（out/ 实测：mockey 84 · claid 85 · printify 84 · kittl 80 · printful 74 · CF 54 · gelato 49 · nordvpn 4 文件命中）

---

## 📧 邮件扫描 (IMAP 实拉)

- **通道**: SOCKS5 `127.0.0.1:7892` → `imap.gmail.com:993` 登录 OK
- **窗口**: SINCE 29-Aug-2026，**25 封全量**
- **新审批 0 · 商户回复 0 · 税务邮件 0** —— 自 8/26 起 **16 天 0 新审批**
- 值得记的 6 条：
  1. **Claid 月度绩效 (9/1)**：Clicks **3** / Referrals **1** / Customers 0 / Earnings **$0** — 7 月为 0/0/0，**首次出现 referral 信号**
  2. **Claid manager check-in (8/31)**：Gabriela 主动询问转化与推广反馈（需 user 手动回）
  3. **Printify 唤醒邮件 (8/31)**：`Ready to start earning? Your link is waiting.` — 未活跃提醒，反证结算端无转化
  4. **Printful × Amplified ×3 (9/3、9/4、9/7)**：Q4 假日定价 + **Kittl 50% off 年付** + AI workflows（9/24 免费线上活动，可作 Q4 内容素材；Kittl 折扣可做 promo/内容钩子）
  5. **CF free picks ×4 (8/28、8/29、8/30、9/3)** → 已补解析落盘
  6. Supabase `togthr-life` 暂停 ×3 (9/4、9/6、9/12) — 跨项目，转告

---

## 🎃 CF freebie 解析器 (v5)

- **补解析 4 期**（402 停摆期积压）：8/28 x0🎃 / 8/29 x1🎃 / 8/30 x0🎃 / **9/3 x2–3🎃**
- 9/3 期万圣节：Preppy Boho Fall Pumpkin Clipart · Spooky Book Stack PNG · Retro Vintage Halloween Pumpkin PNG
- 圣诞 🎄 +6 入 BF/Q4 备选池
- **素材池：45 → 49 🎃**
- ⚠️ **9/3 之后 8 天无新 free picks 邮件**（历史常态每日 1 期）= 节奏中断，待观察
- 落盘：`.hermes/logs/cf-freebies/2026-09-12.md`

---

## ✅ 完成标准核对

- [x] `.hermes/affiliate-programs.json` 已更新（`last_updated` = 9/12 12:1x + 6 个新键 + Claid 8 月绩效字段；JSON 校验 PASS，diff 仅 12 增 3 删）
- [x] `AFFILIATE_LOG.md` 今日 entry 落盘
- [x] 本文件 `.hermes/logs/2026-09-12-affiliate-monitor.md` 落盘，§2.1 按 P0/P1/P2 排序
- [x] CF freebie 清单落盘（`.hermes/logs/cf-freebies/2026-09-12.md`）
- [x] 升级消息按 P0/P1/P2 分类，5 要素全
- [x] 新获批商户部署流程：无新获批（P0 部署缺口 = 0）
- [x] 无 push / 无 build / 无自动登录 / 无自动回信（凭证文件未改）

**衍生提示**: 本次停摆期留下未提交工作区（`.cluster/` 全目录 + 8/29–9/2 各任务产物），非本任务范围，留给 daily-content 恢复时一并 commit。
