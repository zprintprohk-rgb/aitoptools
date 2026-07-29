# aitoptools.net Affiliate Monitor — 2026-07-28

**Cron**: affiliate-monitor (12:00 Asia/Shanghai, 启动 D6)
**Operator**: Hermes Agent (deepseek-v4-flash)
**TTL**: 30 min → elapsed: ~10 min
**Status**: ⚠️ Partial — Gmail 通道仍缺失 (D6),仅做 state-file 巡检 + 5 天回填

---

## 1. Gmail 通道 (硬阻塞 · D6 持续)

| 项 | 状态 | 证据 |
|---|---|---|
| Gmail API OAuth 凭证 | ❌ 缺失 (D6) | `credentials.affiliate.local.json` (8 平台账号) 无 `gmail` 段 |
| Gmail App Password (IMAP) | ❌ 缺失 (D6) | 同上 |
| 本地 mail 客户端 | ❌ 缺失 | 项目内 0 个 mail 工具 |
| web_fetch 直连 Gmail | ❌ 不可行 | Gmail 强制 OAuth,直连撞登录墙 |
| 重试 1 次 (per cron 规则) | ⏭️ 跳过 (D6) | 凭证缺失为持久 blocker,重试结果一致;直接升级 user |

**结论**: D1-D6 (2026-07-22 启动至今) 共 0 封真实邮件被读取。本日 (7/28) cron 仍仅完成 state-file 巡检,所有"今日新增/拒绝/待审"均**无邮件证据**,仅以 AGENTS.md §5 + credentials.affiliate.local.json 7/24 batch 记录为来源回填。

## 2. State File 巡检 (5 天回填 · 7/23 → 7/28)

### 2.1 申请矩阵当前快照 (2026-07-28)

**全口径 approved (5 个, 跨 programs[] + credentials)**:
| # | 平台 | Network | Status | 批准日 | Cookie/付款 |
|---|---|---|---|---|---|
| 1 | NordVPN | Nord Affiliates (Direct) | ✅ approved | 2026-07-16 | 40%+ recurring, manager 颜 (Yan) |
| 2 | NordPass | (同 Nord 账号覆盖) | ✅ approved | 2026-07-16 | 同上 |
| 3 | Mockey AI | Endorsely | ✅ approved-active | 2026-07-22 | 30% recurring, 90-day cookie, PayPal 月付 |
| 4 | Claid AI | FirstPromoter | ✅ approved-active | 2026-07-24 | 20% lifetime, 60-day cookie, min $20 |
| 5 | Printify | PartnerStack | ✅ approved-active | 2026-07-24 | default link, $150/月博客挑战(deadline 9/29) |
| 6 | Printful | in-house | ✅ approved-active | 2026-07-24 | 10% × 12 月, 邮箱待确认 |
| 7 | Creative Fabrica | Direct | ✅ approved | 2026-07-17 | ref/27832838 |

**全口径 declined/closed (1 个)**:
| # | 平台 | Network | Status | 关闭日 | 备注 |
|---|---|---|---|---|---|
| 1 | Looka | in-house | ❌ declined-closed | 2026-07-24 | program page not found,二次确认 partner program 已关;仅留 partnerships@looka.com 直邮渠道,优先级低 |

**pending (programs[] 内 2 个)**:
- Kittl (Impact, 7/15 首次提交, 13 天)
- Placeit (Impact, 待 Marketplace 升级)

**not-applied (programs[] 内 9 个, 暂无申请)**:
- Hostinger / Jasper AI / Writesonic / Copy.ai / Canva / Shopify / Photoroom / Surfer SEO / Bluehost

### 2.2 5 天变化 (vs 7/23 巡检)

| 变化类型 | 平台 | 日期 | 来源 |
|---|---|---|---|
| pending → approved | Claid AI | 2026-07-24 | AGENTS.md §5 + credentials.claid.ai |
| pending → approved | Printify (PartnerStack) | 2026-07-24 | AGENTS.md §5 + credentials.partnerstack |
| pending → approved | Printful | 2026-07-24 | AGENTS.md §5 + credentials.printful.com |
| pending → declined-closed | Looka | 2026-07-24 | AGENTS.md §5 (二次确认) |
| 新增申请 | Gelato (PartnerStack 重申) | 2026-07-24 | credentials.gelato.com (首申 identity mismatch 被拒,本次修复后重提) |
| 新增申请 | PartnerStack Network membership | 2026-07-24 | credentials.partnerstack-network |
| 新增申请 | Deel (挂 PartnerStack 网络) | 2026-07-24 | credentials.deel.com |
| 依赖卡 | Impact Marketplace Upgrade | 7/18 → 7/28 = 10 天 | 在 pending_applications_aging |
| 依赖卡 | Kittl 首次申请 | 7/15 → 7/28 = 13 天 | 在 pending_applications_aging |

### 2.3 待审申请 aging 风险 (D6)

| 平台 | 距今 | 阈值 | 风险 | 建议动作 |
|---|---|---|---|---|
| 🔴 **Kittl** (Impact 首次) | 13 天 | 7 天 | 超阈值 6 天,卡 Impact 升级依赖 | **user 拍板**: (a) 等 Impact Marketplace 升级 (b) 走 in-house kittl.com/affiliates 绕过 Impact 平台 |
| 🔴 **Impact Marketplace Upgrade** | 10 天 | 7 天 | 超阈值 3 天,卡 Kittl/Placeit/Copy.ai/Canva/Shopify/Surfer/Bluehost 全部 Impact 系申请 | **user 登录 app.impact.com** 查看 Marketplace 申请状态,或发邮件 follow-up 至 partner-support@impact.com |
| 🟢 Gelato (PartnerStack 重申) | 4 天 | 7-14 天 | 正常窗口 | 等,无需动作 |
| 🟢 PartnerStack Network membership | 4 天 | 7-14 天 | 正常窗口 | 等,Deel 自动激活 |
| 🟢 Deel (挂 PartnerStack 网络) | 4 天 | 7-14 天 | 正常窗口 | 等网络批准 |
| 🟡 Placeit (待 Impact 升级) | — | — | 卡外部依赖 | 同 Impact Marketplace |

### 2.4 真实链接 (SSoT = credentials.affiliate.local.json,本 cron 不动)

| 平台 | 链接 | 状态 |
|---|---|---|
| Creative Fabrica | https://www.creativefabrica.com/ref/27832838/ | ✅ 站点已用 |
| NordVPN | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=152693&url_id=902 | ✅ /nordvpn-review/ |
| NordPass | https://go.nordpass.io/aff_c?offer_id=488&aff_id=152693&url_id=9356 | ✅ /nordpass-review/ |
| Mockey AI | https://mockey.ai?via=jerome796 | ✅ |
| Claid AI | https://claid.ai?via=jerome94 | ⚠️ 已获批,等 user 拍板走 `replace_affiliate_links.py --apply` |
| Printify | https://try.printify.com/4fs863rfz2yc | ⚠️ 同上 |
| Printful | https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a | ⚠️ 同上 |

→ 站点可立刻激活的"待替换"链接 = 3 (Claid/Printify/Printful),per AGENTS.md §6 需 user 拍板,本 cron 不自动跑。

## 3. 联盟获批后续动作 (M3 / 链接替换)

### 3.1 立即评测建议
- **本 cron 内 0 封新邮件 = 0 个新获批程序** (仅按 state file 推断,无邮件证据)
- 7/22 入队的 5 个 M3 评测候选 (MockupHive/Packify.ai/Nightjar/Dynamic Mockups/Mintly) 仍在 M3 gate review 队列,本 cron 不动
- **无新 M3 任务触发**

### 3.2 联盟链接替换建议 (3 个待激活)
**优先级** (按 6 月目标 $3000 路径 + 7/24 batch 净增量):
1. **Printful** — 已有 /printful-vs-printify/ 对比页,链接替换收益最快,user 拍板后 1 步跑 `replace_affiliate_links.py --apply`
2. **Claid AI** — 适合补 /claid-review/ 单测页或插入 product photography 工具对比,M3 候选
3. **Printify** — 与 Printful 同主题,建议先 Printful 上线再 Printify,避免一页面内 CTA 互抢
- 本 cron 仅写建议,**不自动跑脚本** (per project.yaml compliance.review_required_for: affiliate_link_replacement)

## 4. 异常 / 阻塞

| 级别 | 描述 | 行动 |
|---|---|---|
| 🔴 **P0** | Gmail 通道缺失 D6 (2026-07-22 → 7/28),本 cron 6 天空转,无邮件证据 | user 提供 Gmail App Password (16 字符, Google Account → Security → App passwords,选 "aitoptools-monitor") → 写入 `F:\aitoptools\.hermes\secrets\gmail_credentials.json` (已 gitignore 覆盖) → 改 cron 通道 |
| 🔴 **P0** | Impact Marketplace Upgrade 超阈值 3 天,卡 7 个 Impact 系程序申请 | user 登录 app.impact.com 查 Marketplace 申请状态 |
| 🔴 P0 | Kittl 13 天未批,卡 Impact 升级 | user 拍板: 等升级 vs 绕道 in-house |
| 🟡 P1 | Claid / Printful payout method 未设置 (Claid 需 PayPal, Printful 邮箱确认) | user 浏览器手动操作 |
| 🟡 P1 | 3 个新链接 (Claid/Printify/Printful) 待 user 拍板后激活 | 等 user 决定激活顺序 |
| 🟢 P2 | 北极星指标 $0/3000 (5 个月倒计时, 剩 171 天) | 常态,需真实链接 + 评测页流量双轮驱动 |

## 5. 完成标准核对 (per cron 任务)

- [x] `.hermes/affiliate-programs.json` 状态字段已更新 (5 天回填 + last_updated 2026-07-28)
- [x] `AFFILIATE_LOG.md` 今日 entry 落盘 (2026-07-28 段,见追加)
- [x] `.hermes/logs/2026-07-28-affiliate-monitor.md` 落盘 (本文件)
- [⚠️] 升级消息 5 要素 — Gmail 通道缺失导致"新获批/新拒绝"两要素 = 0 邮件证据 (按 state file 推断 7/24 已 4 项有动作,但无邮件独立核实);"待审"=2 项超阈值;"建议立即申请"=0 (暂无新雷达触发);"建议立即评测"=0 (7/22 5 候选还在 M3 队列);"硬阻塞"=1 (Gmail 通道,持续 6 天)

---

**Status**: ⚠️ Partial — Gmail 通道缺失 D6 持续,本 cron 仅完成 state-file 巡检 + 5 天回填;真实邮件检查待 user 补凭证后解锁。
