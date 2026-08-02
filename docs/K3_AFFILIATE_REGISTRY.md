# K3 Affiliate 联盟账户注册表 — 公开版 (无密码)

> **维护人**: K3 (你, 跨境 EC 创业者)
> **协作 agent**: Mavis
> **截止**: 2026-08-01 10:02 CST (8/1 K3 Gmail webmail 兜底: Gelato approved + 推广链接已取 + Printful 营销邮件)
> **SSoT**: 本文件 (公开版) + `.hermes/secrets/affiliate-credentials.md` (私密版, 含密码, gitignored)
> **关联**: `.hermes/affiliate-programs.json` (agent runtime data), `AFFILIATE_LOG.md` (历史日志)

---

## ✅ 已激活 (6 个) — 7 月新批 5 个 + 8/1 新批 Gelato

| # | 商户 | 平台 | 登录方式 | 账号 / 邮箱 | 推广链接 | 佣金 | 状态 & 待办 |
|---|---|---|---|---|---|---|---|
| 1 | **Creative Fabrica** | in-house | Google OAuth | zprintprohk@gmail.com (Jerome Tang) | 后台取链, `affiliate_id=27832838` | 25% + 订阅续费 20% 循环 | ✅ 注册即用, 无审核 |
| 2 | **Claid.ai** | FirstPromoter | 邮箱+密码 | zprintprohk@gmail.com | https://claid.ai?via=jerome94 | 20% 终身循环, $20 起付 | ✅ 已获批 7/24, ⚠️ **待你进后台设置 PayPal 收款方式** |
| 3 | **Printify** | PartnerStack | 邮箱+密码 | zprintprohk@gmail.com | https://try.printify.com/4fs863rfz2yc | 销售额 5% × 12 个月 | ✅ 已获批 7/24, ToS 已接受 |
| 4 | **Printful** | in-house | 邮箱+密码 | zprintprohk@gmail.com | https://www.printful.com/a/15297661:e946341e64188d00218db2fbabcacc4a | 10% × 12 个月 + $25 Growth 奖励 | ✅ 已获批 7/24, ⚠️ **确认邮件仍未见 (in-house 系统对内部账号可能跳过), 不影响 affiliate 上线** |
| 5 | **Mockey** | Endorsely | 邮箱魔法链接 (无密码) | zprintprohk@gmail.com | https://mockey.ai?via=jerome796 | 30% 循环, 90 天 cookie | ✅ 已激活 7/22 |
| 6 | **Gelato** 🆕 | PartnerStack | 同 Printify 账号 | zprintprohk@gmail.com | https://try.gelato.com/upftmv48rtcl (→ gelato.com/print-on-demand) | TBD (待 dashboard, 标准 15-20% 销售循环) | ✅ **8/1 09:56 批准邮件 + 10:02 K3 取链完成. ⚠️ PayPal 收款仍待设** |

---

## 🟡 审核中 / 等待中 (3 个)

| # | 商户 | 平台 | 登录方式 | 账号 | 状态 |
|---|---|---|---|---|---|
| 7 | **Kittl** | Impact | 邮箱+密码 | username: Jerome88 / email: zprintpro@outlook.com | ✅ **已获批 7/30** (Marketplace 升级连带通过) — pxf.io 链接 7/30 11:34 已上线 19 处 (commit a736bb1) |
| 8 | **Deel** | PartnerStack Network | 同下 | zprintprohk@gmail.com | ⏸ 申请已搁置, 等 PartnerStack Network 审批通过后自动送出 |
| 9 | **PartnerStack Network** | — | — | zprintprohk@gmail.com | 🟡 7/24 提交, 待审批 (Gelato 8/1 已批走 PS, 但 Network 资格仍独立审, 影响 Deel) |

---

## ❌ 已关闭 / 失效 (2 个)

| # | 商户 | 原因 | 建议 |
|---|---|---|---|
| 10 | **Looka** | PartnerStack 侧 program page not found, 计划实际已关闭 | 仅保留 partnerships@looka.com 邮件直签一路, 低优先 |
| 11 | **Photoroom** | 现有 `?fpr=partner` 为伪造参数 (无跟踪), 不产生佣金 | 需你手动走 Awin 重新注册 (商户 #121800), 然后全站替换链接 |

---

## ⏸ 待申请 (1 个)

| # | 商户 | 平台 | 前置条件 |
|---|---|---|---|
| 12 | **Placeit (Envato)** | Impact | 等 Impact Marketplace 升级获批后用 Jerome88 账号申请 (K3 7/30 03:43 暂缓, 等流量 > 100 UV/天 再启动 W1-T2) |

---

## 📋 5 项关键收尾行动 (8/1 上午 P1 任务)

### A. 邮箱验证 (5 min, 你浏览器手点)
| 商户 | 验证邮件发件人 | 收件箱 | 动作 |
|---|---|---|---|
| **Claid** | FirstPromoter / Claid | zprintprohk@gmail.com | 点 "Confirm your account" 链接 |
| **PayPal** (Claid 收款) | paypal.com | zprintprohk@gmail.com | 验证 PayPal 账户 + 绑定 Claid 收款 |
| **Printful** | printful.com | zprintprohk@gmail.com | 点 "Confirm your affiliate account" 链接 |
| **IMPACT** (Kittl) | impact.com | zprintpro@outlook.com | 查验证邮件 (可能没发, 不强制) |

### B. 1 push commit 草稿层 (8/2 攒批执行, 详见 W1 任务卡)
- `.hermes/drafts/articles/` 5 篇 SEO 文章草稿
- `.hermes/drafts/social/reddit-5-posts-2026-07-30.md`
- `.hermes/drafts/social/pinterest-10-pins-2026-07-30.md`
- `.hermes/drafts/reviews/` 3 篇评测
- 2 篇评测 (`picjam-2026.md` / `greenonion-ai-2026.md`) 含 [PENDING USER DATA] 标记, 需你给真数据

### C. 4 封 BD 邮件 (8/1 上午 20 min, 你浏览器发)
- `Picjam` → mailto:sales@vidi.so (P0)
- `GreenOnion` → 官网 contact (P1)
- `Designkit` → 官网 contact (备选)
- `Adject` → 官网 contact (备选)
- 草稿: `.hermes/drafts/social/bd-emails-4-picjam-greenonion-2026-08-01.md` (9401 bytes)

### D. Picjam + GreenOnion 评测填真数据 (8/1 整天, 你给数据)
- 12+ 处 [PENDING USER DATA] 标记
- 需要: workflow 截图 / Listing Score 49→94 演示 / GreenOnion 60s 实测录像 / 最新 pricing 截图 / 平台集成测试
- agent 填完 12+ 处后 commit 评测 ready, 8/5 攒批 publish

### E. 2 凭证待补 (Gmail IMAP 网络修通后)
- `IndexNow` API key (16-char, Bing Webmaster 注册 1 min)
- `GSC` OAuth refresh_token (Google Search Console, 1 min)

---

## 🔒 凭证管理 (分层安全)

| 文件 | 路径 | Git 状态 | 内容 |
|---|---|---|---|
| **公开版 (本文件)** | `docs/K3_AFFILIATE_REGISTRY.md` | ✅ tracked | 平台/账号/链接/佣金/状态 (无密码) |
| **私密版 (含密码)** | `.hermes/secrets/affiliate-credentials.md` | ❌ gitignored | 完整账号密码, 严禁 commit |
| **运行时数据** | `.hermes/affiliate-programs.json` | ✅ tracked | agent runtime data (K3 维护 SSoT) |
| **历史日志** | `AFFILIATE_LOG.md` | ✅ tracked | 7/16-8/1 每日 affiliate 行动日志 |
| **Gmail 凭证** | `.hermes/secrets/gmail_credentials.json` | ❌ gitignored | 16-char App Password (已修 7/30 05:14) |
| **K3 备份版** | `credentials.affiliate.local.json` (原) | ❌ gitignored | 旧版 K3 备份 |

> **警告**: 任何联盟账号密码都**只能**写到 `.hermes/secrets/` 或 `credentials.affiliate.local.json` 这类 gitignored 文件。**绝不能 commit 到 git tracked 文件** (包括 `docs/`、`src/`、`scripts/` 等)。

---

**最后更新**: 2026-08-01 00:59 CST
**版本**: v1 (初次归档)
**下一步**: K3 浏览器手点 3 个邮箱验证链接 → 8/2 攒批 push 6 草稿 + schema.org 扩展
