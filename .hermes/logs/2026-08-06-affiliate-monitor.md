# 联盟申请监控 — 2026-08-06

**任务**: aitoptools-affiliate-monitor (cron 12:05, TTL 30min)
**通道**: Gmail IMAP RESTORED (SOCKS5 127.0.0.1:7892, 68 封拉取)
**模型**: deepseek-v4-flash

## 一、邮件扫描 (fetch_affiliate_mails.py + read_affiliate_mails.py)

68 封 (SINCE 30-Jul-2026)。**0 新审批** (无 Kittl/Gelato/SPOD/Prodigi 获批邮件)。匹配 5 封 (3 LinkedIn 噪音 + PartnerStack 8/1 已知 + Gelato 7/31 已知)。新发现:

| 日期 | 发件人 | 主题 | 信号 |
|---|---|---|---|
| 8/5 09:25+09:30 | partners@claid.ai | Reset password instructions (第二条) | 8/5 11:28 Gabriela 确认首条 token 已过期 (FirstPromoter 核实). **按 v4 基线: user 8/5 已全部办妥, 勿再提醒** |
| 8/5 11:28 | gabriela.d@letsenhance.io | Re: Your Monthly Performance Update | FirstPromoter 确认 token 过期, 建议 forgot-password 重发 — 已由 user 8/5 处理 |
| 8/5 05:05 | supabase.com | zprintpro-production has been paused | ⚠️ 跨项目: zprintpro 免费项目被暂停 (非本域, 提醒 K3) |
| 8/6 01:23 | newsletter.printful.com | Halloween products | 营销邮件, 可作 POD 旺季内容素材 |

## 二、§2.1 状态总览 (按 P0/P1/P2 排序)

### 🔴 P0 (approved + link 未部署/坏链)

| 商家 | 状态 | 问题 | 处置 |
|---|---|---|---|
| **NordVPN** | approved 7/16 | **裸链!** nordvpn-review 页 affiliateUrl + 2 处 CTA 均为 `nordvpn.com/` (无 go.nordvpn.net 跟踪, 点击零归因) — 7/16 获批后链接从未部署 | ✅ **8/6 已手术式修复**: reviews.json 2 行 (affiliateUrl + content 2 CTA → `go.nordvpn.net/aff_c?offer_id=15&aff_id=152693&url_id=902`), JSON 有效 107 条目。**仅剩 build+push 上线** |

### ⚠️ P1 (待 user 行动)

| 项 | 状态 | 天数 | 处置 |
|---|---|---|---|
| **Printful 邮箱确认** | 确认邮件 7/20 17:00 (support@info.printful.com) 已定位 | D17 | **user 浏览器点击验证链接** (printful.com/verify/0/...?key=...); 已 17 天可能过期, 若 404 需 Printful 后台重新触发 (1min) |

### 💡 P2 (暂缓/观察)

- Google 8/3 20:43 "Microsoft apps and services" 授权 — 非自主动作, 已 3 天无反馈, 降 P2 观察 (myaccount.google.com 可查)
- 11 项维持暂缓 (K3 7/30 拍板等 Kittl 跑通): 4 申请候选 + 5 评测候选 + 2 resolved (Impact 系)
- Placeit: 等 Impact Marketplace 后重提 (唯一剩余 pending)
- Supabase zprintpro-production 暂停 (跨项目, 提醒 K3)

## 三、已解决 (本轮)

- ✅ **Printful 坏链 P0 闭环**: 8/5 修复数据 → 8/6 攒批 push 上线。线上字节级验证 (regex 计数, 非终端显示): printful-review 页 2 处真链 (32 位 hash), 0 字面星号
- ✅ **Claid**: v4 基线确认全办妥 (重置密码 + PayPal doolen@126.com + 公司信息), 不再上报
- ✅ **链接部署核查** (9 工具池 + Nord 系): printify/printful/gelato/kittl/claid-ai/mockey/creative-fabrica/nordpass 全部 200 + 真链 ✅; **nordvpn 裸链** → 新 P0 (见上)

## 四、数据变更 (未 commit, 攒批纪律)

1. `src/data/reviews.json` — NordVPN 裸链修复 (2 行: affiliateUrl + content 2 CTA → 跟踪链)
2. `.hermes/affiliate-programs.json` — NordVPN link_deployed:false + link_fix_date + monitoring 8/6 findings + aging as_of

## 五、教训沉淀

- **"已获批" ≠ "链接已部署"**: NordVPN 7/16 获批, my_link_nordvpn 一直存在, 但 review 页 CTA 从未换跟踪链 — 全站 CTA 需定期抽查 (affiliate_link_audit 覆盖的是 affiliates.json 9 工具池, 不含 NordVPN/NordPass 这类独立 review)
- 字节级验证再次证明: 终端 grep 显示 `***` 是脱敏, 线上实际是真链 (regex 计数为准)

## 六、升级 user (P0/P1/P2, 5 要素)

- **P0 (1)**: NordVPN 裸链 — 数据已修, 等 build+push (建议随下次攒批; 属"approved 但 link 未部署"类, 修后 NordVPN $60-100/sale 才能归因)
- **P1 (1)**: Printful 邮箱确认 D17 — 7/20 邮件链接可能已过期, 若 404 需后台重发后重点
- **P2 (3)**: Google 8/3 Microsoft 授权确认 / Supabase zprintpro 暂停 (跨项目) / 维持暂缓清单
