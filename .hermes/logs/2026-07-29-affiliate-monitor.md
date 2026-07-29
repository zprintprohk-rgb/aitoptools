# 联盟监控日报 · 2026-07-29 (D7)

> Cron: `affiliate-monitor` (每日 12:00 Asia/Shanghai, TTL 30 min, 攒批纪律)
> SSoT: `F:\aitoptools\.hermes\affiliate-programs.json` + `AFFILIATE_LOG.md`
> 触发窗口: 算力低谷 12:05-13:30, 12:00 略早但 cron 定时必跑

---

## 1. Gmail 通道检查 (硬约束: 重试 ≤ 1 次)

### 1.1 重试结果
- ❌ **D7 仍缺失** (2026-07-22 → 07-29, 7 天空转)
- 凭证文件 `F:\aitoptools\.hermes\secrets\gmail_credentials.json` **不存在**
- 按 cron 硬约束升级 user, 不静默

### 1.2 ⚠️ 新发现 P0 风险 (.gitignore 实际匹配规则)
实测 `.gitignore` 完整内容 (7 行):
```
node_modules/
.next/
out/
*.log
.env
.claude/
credentials.*.local.json
```
- ❌ **不匹配** `gmail_credentials.json` (没有 `.local` 段)
- ❌ **不匹配** `.hermes/secrets/` 目录
- ❌ **不匹配** `.hermes/secrets/*.json`
- 跟 memory 描述"gitignore 已有 credentials.*.local.json 规则覆盖"**不一致**

**真实风险**: 若 user 按 memory 步骤 ② 写 App Password 到 `secrets/gmail_credentials.json` → **会被 git 跟踪并泄露到 GitHub**。

**修复顺序 (必先 1 后 2)**:
1. **先改 `.gitignore`** 加以下任一规则:
   - `.hermes/secrets/` (目录级,推荐) + `gmail_credentials.json` (路径级,兜底)
   - 或重命名 `gmail_credentials.json` → `credentials.gmail.local.json` 走现有 glob
2. **commit + push** (让 .gitignore 生效)
3. 再写 App Password
4. 改 cron 通道

**memory 修正建议**: 本 cron 7/29 发现的 memory 反例应在下次 maintenance 时修 (memory MEMORY.md 写"gitignore 已有 credentials.*.local.json 规则覆盖"是错的,实际只覆盖该 glob 模式)。

---

## 2. 联盟账户状态 (源数据: affiliate-programs.json)

### 2.1 14 个 programs 状态分布 (2026-07-29) (源 = affiliate-programs.json 数组,共 14 个)
| 状态 | 数量 | 列表 |
|---|---|---|
| ✅ approved-active (JSON 数组内) | 3 | NordVPN (7/16) / Claid (7/24) / Printful (7/24) |
| ✅ approved-active (JSON 数组漏, 仅在 milestones 段) | 2 | Mockey (7/22) / Printify (7/24) — **JSON 数组漏 2 个**, 待 user 拍板是否补回数组 (本 cron 暂不动 SSoT) |
| 🟡 pending (超阈值) | 2 | Kittl 14d 🔴 / Impact Marketplace Upgrade 11d 🔴 |
| 🟡 pending (阈值内) | 0 | (Gelato 重申 / PartnerStack Network / Deel 5d 在 JSON `pending_applications_aging` 段, 不在 programs 数组, 算"等响应"而非"待审批") |
| 🟡 pending (等外部依赖) | 1 | Placeit (依赖 Impact Marketplace 升级) |
| ❌ declined-closed (仅在 resolved 段) | 1 | Looka (7/24,program closed) |
| ⚪ not-applied | 9 | Hostinger / Jasper / Writesonic / Copy.ai / Canva / Shopify / Photoroom / Surfer / Bluehost (9 个,per JSON 数组 2026-07-29) |
| **JSON 数组 14 个总数 = 3+2+0+1+1+9 (与 2+1 缺失项合计 16,与外部段 5 个条目有重叠)** | | |

### 2.2 aging 风险 (D7 vs D6 对比)
| 程序 | 7/28 | 7/29 | Δ | 严重度 |
|---|---|---|---|---|
| Kittl | 13d | 14d | +1 | 🔴 超 7d 阈值 7d,卡 Impact 升级 |
| Impact Marketplace Upgrade | 10d | 11d | +1 | 🔴 超阈值 4d,卡 7 个 Impact 系申请 |
| Gelato 重申 | 4d | 5d | +1 | 🟢 正常 7-14d 窗口中段 |
| PartnerStack Network | 4d | 5d | +1 | 🟢 正常窗口 |
| Deel (via PS) | 4d | 5d | +1 | 🟢 正常窗口 |

### 2.3 真实链接 (SSoT = credentials.affiliate.local.json,本 cron 不动)

| 平台 | 链接 | 状态 |
|---|---|---|
| Creative Fabrica | https://www.creativefabrica.com/ref/27832838/ | ✅ 站点已用 |
| NordVPN | https://go.nordvpn.net/aff_c?offer_id=15&aff_id=152693&url_id=902 | ✅ /nordvpn-review/ |
| NordPass | https://go.nordpass.io/aff_c?offer_id=488&aff_id=152693&url_id=9356 | ✅ /nordpass-review/ |
| Mockey AI | https://mockey.ai?via=jerome796 | ✅ |
| Claid AI | https://claid.ai?via=jerome94 | ⚠️ 已获批,等 user 拍板走 `replace_affiliate_links.py --apply` |
| Printify | https://try.printify.com/4fs863rfz2yc | ⚠️ 同上 |
| Printful | https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a | ⚠️ 同上 |
| **Kittl (pxf 短链,7/28 user 给)** | **https://kittl.pxf.io/qWNvPn** | ⚠️ K3 7/28 拍板建议 "不撤+加 organic 出口", user 待拍板 |

→ 站点可立刻激活的"待替换"链接 = 3 (Claid/Printify/Printful),per AGENTS.md §6 需 user 拍板,本 cron 不自动跑
→ Kittl 链接是 K3 7/28 单独议题,不在今日 cron 流程

---

## 3. 联盟获批后续动作 (M3 / 链接替换)

### 3.1 立即评测建议
- **本 cron 内 0 封新邮件 = 0 个新获批程序** (Gmail 通道缺失, 仅按 state file 推断)
- 7/22 入队的 5 个 M3 评测候选 (MockupHive/Packify.ai/Nightjar/Dynamic Mockups/Mintly) 仍在 M3 gate review 队列,本 cron 不动
- **无新 M3 任务触发**

### 3.2 联盟链接替换建议 (3 个待激活)
**优先级** (按 6 月目标 $3000 路径 + 7/24 batch 净增量):
1. **Printful** — 已有 /printful-vs-printify/ 对比页,链接替换收益最快,user 拍板后 1 步跑 `replace_affiliate_links.py --apply`
2. **Claid AI** — 适合补 /claid-review/ 单测页或插入 product photography 工具对比,M3 候选
3. **Printify** — 与 Printful 同主题,建议先 Printful 上线再 Printify,避免一页面内 CTA 互抢
- 本 cron 仅写建议,**不自动跑脚本** (per project.yaml compliance.review_required_for: affiliate_link_replacement)

---

## 4. 异常 / 阻塞

| 级别 | 描述 | 行动 |
|---|---|---|
| 🔴 **P0** | Gmail 通道缺失 D7 (2026-07-22 → 7/29),本 cron 7 天空转,无邮件证据 | 4 步: ① 改 .gitignore 加 `.hermes/secrets/` → ② commit + push → ③ 写 App Password → ④ 改 cron 通道 |
| 🔴 **P0** | Impact Marketplace Upgrade 超阈值 4 天,卡 7 个 Impact 系程序申请 | user 登录 app.impact.com 查 Marketplace 申请,若仍未批发邮件 follow-up 至 partner-support@impact.com;若 7/30 cron 再升 1 次仍不动,本 cron 自动冻结相关申请,转推 in-house 直签 |
| 🔴 P0 | Kittl 14 天未批,但 7/28 user 已主动给 pxf 短链,卡 Impact 升级 | 7/29 仍待 user 拍板 7/28 K3 建议 1/2/3 (K3 推荐建议 1: 不撤+加 organic 出口) |
| 🟡 P1 | Claid / Printful payout method 未设置 (Claid 需 PayPal, Printful 邮箱确认) | user 浏览器手动操作 |
| 🟡 P1 | 3 个新链接 (Claid/Printify/Printful) 待 user 拍板后激活 | 等 user 决定激活顺序 |
| 🟢 P2 | 北极星指标 $0/3000 (5 个月倒计时, 剩 170 天) | 常态,需真实链接 + 评测页流量双轮驱动 |

---

## 5. 完成标准核对 (per cron 任务)

- [x] `.hermes/affiliate-programs.json` 状态字段已更新 (last_updated 2026-07-29 + aging 6 项 days 同步 + monitoring 段加 .gitignore 风险警告)
- [x] `AFFILIATE_LOG.md` 今日 entry 落盘 (2026-07-29 12:00 段,见追加)
- [x] `.hermes/logs/2026-07-29-affiliate-monitor.md` 落盘 (本文件)
- [⚠️] 升级消息 5 要素 — Gmail 通道缺失导致"新获批/新拒绝"两要素 = 0 邮件证据 (按 state file 推断 7/24 已 4 项有动作,但无邮件独立核实);"待审"=2 项超阈值 (Kittl 14d / Impact 11d);"建议立即申请"=0 (暂无新雷达触发);"建议立即评测"=0 (7/22 5 候选还在 M3 队列);"硬阻塞"=1 (Gmail 通道持续 7 天 + .gitignore 风险新发现)

---

**Status**: ⚠️ Partial — Gmail 通道缺失 D7 持续,本 cron 仅完成 state-file 巡检 + aging 更新;真实邮件检查待 user 补凭证 (并先修 .gitignore 风险) 后解锁。
