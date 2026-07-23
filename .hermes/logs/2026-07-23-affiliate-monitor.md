# aitoptools.net Affiliate Monitor — 2026-07-23

**Cron**: affiliate-monitor (12:00 Asia/Shanghai, 启动 D2)
**Operator**: Hermes Agent (deepseek-v4-flash)
**TTL**: 30 min → elapsed: ~10 min
**Status**: ⚠️ Partial — Gmail 通道缺失,仅做 state-file 巡检

---

## 1. Gmail 通道 (硬阻塞)

| 项 | 状态 | 证据 |
|---|---|---|
| Gmail API OAuth 凭证 | ❌ 缺失 | `credentials.affiliate.local.json` 无 `gmail` 段 |
| Gmail App Password (IMAP) | ❌ 缺失 | 同上 |
| 本地 mail 客户端 (IMAP/SMTP) | ❌ 缺失 | 项目内 0 个 mail 工具,全 .py/.js 脚本 grep 无 gmail/imap/smtp/oauth.mail |
| web_fetch 直连 Gmail | ❌ 不可行 | Gmail 强制 OAuth,web_fetch 跑会撞登录墙 |
| 重试 1 次 (per cron 规则) | ⏭️ 跳过 | 无工具,重试结果一致;直接升级 user |

**结论**: 此 cron 启动 24h 内 0 封真实邮件被读取。所有"今日新增/拒绝/待审"均无证据,本日志**不报告任何邮件事实**。

## 2. State File 巡检 (替代证据)

### 2.1 申请矩阵 (12 个目标程序)

| # | Program | Network | Status | 应用日 | 距今 | 7天阈值 |
|---|---|---|---|---|---|---|
| 1 | Hostinger | CJ/ShareASale | not-applied | — | — | — |
| 2 | NordVPN | Nord Affiliates (Direct) | **approved** | 2026-07-16 | 7d | — |
| 3 | Jasper AI | Impact | not-applied | — | — | — |
| 4 | Writesonic | PartnerStack | not-applied | — | — | — |
| 5 | Copy.ai | Impact | not-applied | — | — | — |
| 6 | Canva | Impact | not-applied | — | — | — |
| 7 | Shopify | Impact | not-applied | — | — | — |
| 8 | Printful | in-house | **pending** | 2026-07-17 | 6d | 🔴 7/24 触线 |
| 9 | Photoroom | PartnerStack/Awin | not-applied | — | — | — |
| 10 | Claid AI | FirstPromoter | **pending** | 2026-07-17 | 6d | 🔴 7/24 触线 |
| 11 | Kittl | Impact | pending (等 Marketplace 升级) | 2026-07-15 (首次) | 8d+ | 🟡 卡外部依赖 |
| 12 | Placeit | Impact | pending (等 Marketplace 升级) | — | — | 🟡 卡外部依赖 |
| 13 | Surfer SEO | Impact | not-applied | — | — | — |
| 14 | Bluehost | CJ | not-applied | — | — | — |
| 15 | Printify | PartnerStack | **pending** | 2026-07-17 | 6d | 🔴 7/24 触线 |
| 16 | Looka | in-house | **pending (账号已建,推广链接未生成)** | 2026-07-17 | 6d | 🔴 7/24 触线 |
| 17 | Mockey AI | Endorsely | **approved-active** | 2026-07-22 | 1d | — |
| 18 | Impact Marketplace Upgrade | Impact | **awaiting approval** | 2026-07-18 | 5d | 🔴 7/25 触线 |

注: 表中 12 个目标程序 + 2 个"卡外部依赖"项 + 1 个升级依赖,共 18 行。原 affiliate-programs.json 14 个 entry,本表加入 4 个衍生项 (Printify/Looka/Impact Marketplace/Placeit) 以反映真实状态。

### 2.2 真实链接 (3 个)

| 平台 | 链接 | 注册日 | 状态 |
|---|---|---|---|
| Creative Fabrica | https://www.creativefabrica.com/ref/27832838/ | 2026-07-17 | ✅ |
| NordVPN | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=152693&url_id=902 | 2026-07-16 | ✅ |
| NordPass | https://go.nordpass.io/aff_c?offer_id=488&aff_id=152693&url_id=9356 | 2026-07-16 | ✅ |
| Mockey AI | https://mockey.ai?via=jerome796 | 2026-07-22 | ✅ |

→ 全站覆盖率: 4/11 (AFFILIATE_LINKS.json 中真实填充),占 36%,比 7/22 审计 (4.9%) 提升 31pp。
→ 但: AFFILIATE_LINKS.json 中其余 7 项 (claid.ai/looka.com/kittl.com/printful.com/printify.com/placeit.net/photoroom.com/shopify.com/gelato.com) 仍空串,需 user 获批后填入。

### 2.3 待审申请 aging 风险

**4 个应用明日 (7/24) 达 7 天阈值**:
1. **Claid AI** (FirstPromoter) — 6 天。官方页无承诺时长,异常中。1stPromoter 平台小,人工审居多,建议 follow-up 邮件至 partners@claid.ai
2. **Printify** (PartnerStack) — 6 天。PartnerStack 平台自动审承诺 48h,**已严重超期**,强烈建议 user 立即登录 dash.partnerstack.com 查看 (账号在 credentials)
3. **Looka** (in-house) — 6 天。账号已建,推广链接未生成 = 状态"半成品"。Looka 是 25-35% 阶梯终身循环,值得追。建议 user 登录 looka.com 提取推广链接
4. **Printful** (in-house) — 6 天。官方承诺 2-5 工作日人工审批,刚到上限,1 天后再 follow-up 也合理

**1 个依赖项 7/25 达 7 天**:
5. **Impact Marketplace Upgrade** — 5 天。Kittl/Placeit 二次申请前置依赖。超 7 天 = Impact 整体通道卡住

## 3. 联盟获批后续动作 (M3 / 链接替换)

### 3.1 立即评测建议
- **无新增待评测平台**。今日 0 封邮件 = 0 个新获批 = 0 个新 M3 任务触发。
- **7/22 已入队的 5 个候选** (MockupHive/Packify.ai/Nightjar/Dynamic Mockups/Mintly) 仍在 M3 gate review 队列,等 user sign-off。这是 hermes-bulk-eval.md §6 pipeline order,本 cron 不动。

### 3.2 联盟链接替换
- **AFFILIATE_LINKS.json** 当前 4/11 真实链接,新增项需 user 拍板 + 手动跑 `python scripts/replace_affiliate_links.py --apply` (per AGENTS.md §6 + project.yaml compliance.review_required_for)
- **建议优先级** (按 6 月目标 $3000 路径):
  1. **Mockey 链接替换** — 已 approved,2 步走 (user 拍板 + 跑脚本),可立即入评测页 (Mockey vs Placeit 对比页)
  2. **Looka 链接补全** — user 登录 looka.com 提取推广链接后填入
  3. **其余 5 个待审** — 等获批后再走管线
- **本 cron 不动**: 链接替换需 user 拍板,本日志仅写建议

## 4. 异常 / 阻塞

| 级别 | 描述 | 行动 |
|---|---|---|
| 🔴 P0 | Gmail 通道缺失,cron 24h 空转 | user 提供 Gmail API OAuth 或 App Password |
| 🟡 P1 | 4 个待审应用明日达 7 天阈值 | 7/24 前 user 主动 follow-up |
| 🟡 P1 | Looka 推广链接 6 天未提取 | user 登录后台取链接 |
| 🟢 P2 | 北极星指标 $0/3000 (5 个月倒计时) | 常态,需真实链接 + 评测页流量双轮驱动 |

## 5. 完成标准核对 (per cron 任务)

- [x] `.hermes/affiliate-programs.json` 状态字段已更新 (含 `monitoring` 块 + `pending_applications_aging` 块)
- [x] `AFFILIATE_LOG.md` 今日 entry 落盘 (2026-07-23 段)
- [x] `.hermes/logs/2026-07-23-affiliate-monitor.md` 落盘 (本文件)
- [⚠️] 升级消息 5 要素 — Gmail 通道缺失导致"新获批/新拒绝"两要素 = "无"。"待审"=4 项明日触阈值。"建议立即申请"=0 (暂无新雷达触发)。"建议立即评测"=无 (7/22 5 候选还在 M3 队列)。"硬阻塞"=1 (Gmail 通道)

---

**Status**: ⚠️ Partial — Gmail 通道缺失,本 cron 仅完成 state-file 巡检;真实邮件检查待 user 补凭证后解锁。
