# 联盟申请监控 — 2026-08-05

**任务**: aitoptools-affiliate-monitor (cron 12:05 窗口, 实际 10:28 触发, TTL 30min)
**通道**: Gmail IMAP ✅ RESTORED (SOCKS5 127.0.0.1:7892, 57 封拉取)
**模型**: deepseek-v4-flash

## 一、邮件扫描 (fetch_affiliate_mails.py + read_affiliate_mails.py)

57 封 (SINCE 30-Jul-2026)。匹配 5 封 (2 封 LinkedIn 噪音 + 3 封高价值)。高价值发现:

| 日期 | 发件人 | 主题 | 信号 |
|---|---|---|---|
| 8/4 08:02 | partners@claid.ai | Reset password instructions | **FirstPromoter 手动触发重置邮件已到** — Claid 登录 P1 解决路径就绪 |
| 8/4 10:57 | gabriela.d@letsenhance.io | Re: Your Monthly Performance Update | Gabriela 确认 FirstPromoter 已触发重置邮件, 线索闭环 |
| 8/3 20:43 | accounts.google.com | 安全提醒 | "Microsoft apps and services" 获授权访问 Google 数据 (非自主动作需查) |
| 8/1 13:40 | networkquality@partnerstack.com | PartnerStack Network Application status | 拒绝确认: "not a great fit, but may be in the future" (IMAP 独立核实, 与基线一致) |
| 8/4 14:30 | printify.com | Banners, Logos and Your Promo Guide | 营销物料, $150 blog challenge 素材 |

## 二、§2.1 状态总览 (按 P0/P1/P2 排序)

### 🔴 P0 (approved + 坏链/未部署, 需尽快处理)

| 商家 | 状态 | 问题 | 处置 |
|---|---|---|---|
| **Printful** | approved 7/24 | **联盟链接脱敏泄漏: 线上 out/ 55 文件 110+ 处 15297661:\*\*\* 坏链** (8/3 程序化 push 带入) | ✅ **已完整修复并本地验证**: ① affiliates.json + tools/printful.json 真链 ② 重跑 generate-pages.js 199/199 → public/best 0 坏链/110 真链 ③ npm run build EXIT_CODE=0 (145 页) → out/ 130/130 真链 0 坏链。**仅剩 push 上线**（死链属紧急修复，建议随 8/5 攒批或单独 push） |

### ⚠️ P1 (传感器/aging/待 user 行动)

| 项 | 状态 | 天数 | 处置 |
|---|---|---|---|
| **Claid 重置密码** | 链接已到收件箱 (8/4 08:02) | D12 (7/24 approved 起登录问题) | **user 浏览器点重置链接设新密码** → 更新本地凭证 → 登录 partners.claid.ai 设 PayPal 收款 (5min) |
| **Claid PayPal 收款** | 未设 | D12+ | 同一浏览器会话一并处理 |
| **Printful 邮箱确认** | 未点 | D12+ | Gmail 找 7/24 Printful welcome 邮件点确认 (1min) |
| **Google 8/3 20:43 授权** | Microsoft apps and services | 1d | 非自主动作需检查账号活动 (myaccount.google.com) |

### 💡 P2 (暂缓, K3 7/30 拍板等 Kittl 跑通)

- 4 申请候选 (Hostinger/Jasper/Writesonic/Copy.ai) + 5 评测候选 + 2 resolved (Impact 系) — 维持暂缓
- Placeit: 等 Impact Marketplace 后重提 (唯一剩余 pending)

## 三、已解决 (本轮)

- **Gmail IMAP 通道**: DEGRADED (7/30) → **RESTORED** (8/5, SOCKS5 直连成功) ✅
- **PartnerStack Network membership**: declined 8/1 (已有合作不受影响, 重试需 user 拍板)
- **Deel**: blocked-by-network-decline (自动激活路径失效, user 拍板直签或放弃)
- **Gelato link_deployed**: → true (8/2 攒批 + 8/3 push b0b3d2b)

## 四、数据变更 (未 commit, 攒批纪律)

1. `src/data/affiliates.json` + `src/data/tools/printful.json` — Printful 坏链修复 (2 行)
2. `public/best/` 55 文件 — generate-pages.js 重生成 (199/199, 0 坏链/110 真链) + sitemap.xml/sitemap-programmatic.xml 同步更新
3. `.hermes/affiliate-programs.json` — last_updated / monitoring (RESTORED + 8_5 findings) / aging 更新 / 3 新 milestones / Printful my_link / Gelato link_deployed / Claid notes
4. `AFFILIATE_LOG.md` — 8/5 entry 追加 (含验证补充)

## 五、教训沉淀

- **Hermes 终端输出脱敏**: 疑似密钥的 32 位 hex 串 (affiliate hash) 在 grep/sed 显示层被替换为 `***` — 判定文件内容须用 od -c / Python 计数 / git diff, 勿信 grep 显示 (本轮因它误判"文件被回滚"多次)

## 六、升级 user (P0/P1/P2, 5 要素)

- **P0 (1)**: Printful 坏链 — 数据已修, 等 build+push (建议今天随 8/5 内容攒批一起上线; 若内容 cron 不 push 需手动安排)
- **P1 (4)**: ① Claid 重置密码链接已到 (8/4 邮件), 浏览器点击设新密码 + 更新凭证 ② Claid PayPal 收款 ③ Printful 邮箱确认 ④ Google 8/3 20:43 Microsoft 授权确认
- **P2 (11)**: 维持暂缓; PartnerStack Network 是否重试 + Deel 是否直签 — 需 user 拍板
