# 2026-08-01 22:55 · affiliate-monitor cron 12:00 window

> **触发**: mavis cron `affiliate-monitor` 12:00 Asia/Shanghai 攒批窗口 (实际触发 22:55, 偏离 11h, mavis cron schedule 待 user 校准 — 跟 7/30 5:02/5:16 同样偏离, 3 次出现)
> **TTL**: 30 min
> **窗口**: 12:05-13:30 / 18:00-08:00 算力低谷 (per AGENTS.md, 但 22:55 触发已是晚间, 仍在 18:00-08:00 内)
> **SSoT 链**: AGENTS.md §5 + .hermes/affiliate-programs.json + credentials.affiliate.local.json + AFFILIATE_LOG.md

---

## §1 状态总览 (8/1 22:55)

| 维度 | 值 | 备注 |
|---|---|---|
| **approved-active 总数** | **7** | 6 link_deployed + Gelato 部分部署 |
| **Gmail IMAP 通道** | 🟡 DEGRADED v3 | 网络层 8.8.8.8 窗口期 OK, 凭证层 D7 缺 |
| **24h 高信号邮件** | 0 (agent 独立) + 2 (K3 兜底) | Gelato approval + Printful marketing |
| **Aging 7d+** | 2 (PartnerStack Network 8d / Deel 8d) | 都挂 PartnerStack, 网络批后 Deel 自动跟出 |
| **攒批 push** | 8/2 攒批 (1 commit 1 push) | Gelato 38+ 替换 + 5 文件 cron 改动一起 |

## §2 P0/P1/P2 排序 (per 7/29 user 拍板 v2)

### §2.1 状态表

| 优先级 | 类别 | 数量 | 详情 |
|---|---|---|---|
| **P0 🔴** | approved + link_deployed:false 连续 2d | **0** | ✅ Gelato 8/1 10:02 link + commit 86756b9 5 处替换, 1 天内不算 2 天全裸链 |
| **P1 ⚠️** | 传感器离线 / aging 超阈值 | **5** | Gmail IMAP D14 / Claid PayPal D8+ / Printful 邮箱 D8+ / PartnerStack 8d / Deel 8d |
| **P2 💡** | 新申请候选 / 评测候选 / resolved 暂缓 | **11** | 4 申请 + 5 评测 + 2 resolved (K3 7/30 拍板等 Kittl 跑通) |

### §2.2 P0 详情 (无)

```
P0 = 0 ✅
- 无 approved + link_deployed:false 连续 2d 未上线的程序
- Gelato 8/1 10:02 K3 兜底取链 + commit 86756b9 5 处替换 (部分部署) + 8/2 攒批 38+ 处补齐
- 攒批纪律维持: 8/1 1 push (commit 86756b9), 8/2 攒批 1 push, 0 违规
```

### §2.3 P1 详情 (5 项)

| # | 项目 | 状态 | 已 | user 必做 | 耗时 |
|---|---|---|---|---|---|
| 1 | **Gmail IMAP 通道** | 🟡 DEGRADED v3 | 14d | 补 App Password (16 字符, Google 账号 → 安全 → 两步验证 → 应用专用密码) + 写入 .hermes/secrets/gmail_credentials.json | 5min |
| 2 | **Claid PayPal 收款** | ⚠️ D8+ | 8d | K3 浏览器登 partners.claid.ai → 5min | 5min |
| 3 | **Printful 邮箱确认** | ⚠️ D8+ | 8d | K3 浏览器 Gmail → 找 7/24 Printful welcome 邮件 → 点确认链接 | 1min |
| 4 | **PartnerStack Network membership** | ⚠️ 8d | 8d | 等 K3 7/24 申请 5-7d 周期到, 8/2 仍无回应可发邮件问 partnerships@partnerstack.com | 2min |
| 5 | **Deel (pending PartnerStack 网络)** | ⚠️ 8d | 8d | 跟 PartnerStack 绑, 网络批后 Deel 自动激活, 不用单独 follow-up | 0min (自动) |

### §2.4 P2 详情 (11 项, 暂缓)

| 类别 | 数量 | 程序 | K3 拍板 |
|---|---|---|---|
| 申请候选 (high 优先级) | 4 | Hostinger ($60-100/sale) / Jasper (20-30% 循环) / Writesonic (20-30% 循环) / Copy.ai (20-30% 循环) | 7/30 03:43 暂缓, 等 Kittl 跑通 |
| 评测候选 (M3 gate) | 5 | M3 数据已填 (M3_MONTH1_DATA.md), 暂缓 | 7/30 03:43 暂缓 |
| Resolved 暂缓 (Impact 系) | 6 | Canva / Shopify / Bluehost / Surfer / Copy.ai / Placeit (6 个都挂 Impact, 等 Marketplace 升级) | 7/30 03:43 暂缓, Marketplace 7/30 已悄悄过, 但 K3 拍板等 Kittl 跑通再启用 |

## §3 Gmail IMAP 通道详细诊断 (本轮核心)

### §3.1 多 DNS resolver 实测 (22:55:43)

| 解析器 | 解析 IP | TCP 993 | 状态 |
|---|---|---|---|
| default getaddrinfo | 108.177.125.108 | 3s timeout | ❌ 重污染段 (7/30 142.250.157.x → 7/31 64.233.187.x → 8/1 108.177.125.x) |
| 8.8.8.8 | 142.251.8.109 | 60ms OK | ✅ **新! 首次返回可达 IP, 端口 993 通, 窗口期** |
| 1.1.1.1 | (命令 timeout) | n/a | ❌ UDP 53 仍挡 |
| 9.9.9.9 | 2a00:1450:400c:c0b::6d (IPv6) | getaddrinfo failed | ❌ IPv4 connect failed |

### §3.2 根因链 (3 个连续踩坑)

1. **7/22 启动 Gmail API 凭证 D7 缺** — `gmail_app_password` 字段不在 credentials.affiliate.local.json
2. **7/30 5:14 user 修 App Password 空格** — 凭证落盘 .hermes/secrets/gmail_credentials.json, 5min verify PASS
3. **7/30 5:16 IMAP 网络层挡** — 凭证 PASS + IMAP 端口全 timeout (smtp.gmail.com OK), 根因 GFW 周期性重污染

### §3.3 7/30 → 8/1 跨 3 天重污染模式

| 日期 | default 段 | 8.8.8.8 段 | 状态 |
|---|---|---|---|
| 7/30 12:00 | 142.250.157.x TCP OK ✅ | n/a | fix 模式生效 |
| 7/30 5:19 | n/a (5:19 改 default 强制 IP) | n/a | IMAP 端口全 timeout |
| 7/31 15:11 | 64.233.187.x TCP timeout ❌ | 64.233.187.x 同步污染 ❌ | 4 resolver 全 fail |
| 8/1 22:55 | 108.177.125.x TCP timeout ❌ | **142.251.8.109 TCP 60ms OK ✅** | 8.8.8.8 窗口期 |

### §3.4 7/30 教训 二次确认 (memory 应升级)

- 7/30 5:02 那轮: 5:01 user 报"凭证已填" → 5:05 cron 5min verify STILL_MISSING
- 7/30 5:16 这轮: 5:14 user 报"凭证修好" → 5:15 verify PASS (存盘 OK) → 5:16 IMAP TIMEOUT (网络层 fail)
- 8/1 22:55 这轮: 8.8.8.8 窗口期 OK + 凭证仍 D7 缺 → 通道仍不可用
- **教训升级**: 凭证 PASS ≠ 通道 PASS ≠ 通道 PERSISTENT. 必须 3 段都过: 凭证 OK + IMAP connect test OK + 持续 OK (跨 24h 仍 OK)

## §4 K3 8/1 webmail 兜底 (agent 不能独立核实)

### §4.1 09:56 K3 报告 Gelato approval

```
From: partnerships@gelato.com (Alex)
Subject: Welcome to the Gelato Partner Program
Date: 2026-08-01
Signal: ✅ Gelato 批准! 7/24 重申 → 8 天出结果 (正常 7-14 天窗口内)
```

### §4.2 10:02 K3 取推广链接

```
Portal: https://dash.partnerstack.com/
Link obtained: try.gelato.com/upftmv48rtcl (重定向 gelato.com/print-on-demand)
```

### §4.3 8/1 commit 86756b9 落地

```
feat(gelato): 联盟链接 GA4 埋点 + 5 处替换 (8/1 攒批)
- 5 处站内 gelato.com 链接 → try.gelato.com/upftmv48rtcl
- GA4 affiliate_click 事件 + utm_campaign=gelato
- 8/2 攒批 38+ 处补齐
```

### §4.4 8/1 Printful 营销邮件 (非验证)

```
From: printful.com
Subject: Winter's coming. Your lineup should too.
Signal: 📢 AOC 卫衣/运动衫新品 = 内容素材 (Picjam/GreenOnition 评测可提)
       Printful verification 邮件仍未见 (in-house 系统对内部账号可能跳过)
```

## §5 联盟账户矩阵 (8/1 22:55)

| # | 商家 | 网络 | 状态 | approved | link | link_deployed | 备注 |
|---|---|---|---|---|---|---|---|
| 1 | NordVPN/NordPass | Nord Affiliates | ✅ approved | 7/16 | go.nordvpn.net + go.nordpass.io | ✅ | /nordvpn-review/ + /nordpass-review/ |
| 2 | Mockey | Endorsely | ✅ approved | 7/22 | mockey.ai?via=jerome796 | ✅ | 30% 循环 / 90d cookie / PayPal monthly |
| 3 | Claid | FirstPromoter | ✅ approved | 7/24 | claid.ai?via=jerome94 | ✅ | 20% 循环 lifetime / 60d cookie / PayPal 待设 (P1) |
| 4 | Printify | PartnerStack | ✅ approved | 7/24 | try.printify.com/4fs863rfz2yc | ✅ | 20-30% 循环 / $150 博客挑战 9/29 截止 |
| 5 | Printful | in-house | ✅ approved | 7/24 | printful.com/a/15297661:e94634... | ✅ | 10% × 12mo / 邮箱确认待点 (P1) |
| 6 | Kittl | Impact | ✅ approved | 7/30 | kittl.pxf.io/qWNvPn | ✅ | 20% first 12mo / 30d referral / 14d 1 click 0 conv |
| 7 | **Gelato** | **PartnerStack** | **✅ approved** | **8/1** | **try.gelato.com/upftmv48rtcl** | **🟡 部分 5/38+** | **15-20% 销售循环 (待 dashboard 查) / PayPal 待设** |

**Sum**: 7 approved-active 全部 link 到位, 6 全 link_deployed, Gelato 8/2 攒批 38+ 处补齐 → 7 link_deployed

## §6 升级 user 行动 (按 P0/P1/P2 排序, K3 必做 vs agent 能帮)

### P0 (无, 攒批纪律维持)
- ✅ 无. Gelato 8/2 攒批 38+ 处 1 commit 1 push 解决

### P1 (5 项, 全部需 user 浏览器 1-5min 行动)
- 🔴 **P1-A 补 Gmail App Password (今天 23:00 前窗口期)** — 5min
  - Google 账号 → 安全 → 两步验证 → 应用专用密码 → 选"邮件 + Windows 计算机" → 16 字符生成
  - 写入 `F:\aitoptools\.hermes\secrets\gmail_credentials.json` (跟 7/30 5:14 user 修空格同位置)
  - agent 自动 strip-spaces 验证 (5min verify 模式, 7/30 教训: 凭证 PASS + IMAP connect test PASS + 持续 OK 三段)
  - 之后 IMAP 用 8.8.8.8 IP 142.251.8.109 强制连 (现在窗口期可达)
- ⚠️ **P1-B Claid PayPal 收款设** — K3 浏览器登 partners.claid.ai → 5min
- ⚠️ **P1-C Printful 邮箱确认点** — K3 浏览器 Gmail → 找 7/24 Printful welcome 邮件 → 点确认链接 1min
- ⚠️ **P1-D 8.8.8.8 IP 窗口期 6-12h 行动** — 补 App Password 后 cron 立即试 login, 错过窗口要等下个 GFW 放行周期
- ⚠️ **P1-E PartnerStack Network + Deel aging 8d** — 等 5-7d 周期到, 8/2 仍无回应可发邮件问 partnerships@partnerstack.com

### P2 (11 项, 暂缓, K3 7/30 03:43 拍板)
- 💡 维持暂缓: 4 申请 (Hostinger/Jasper/Writesonic/Copy.ai) + 5 评测 (M3 gate) + 2 resolved (6 个 Impact 系)
- 等 Kittl 跑通 (14d 1 click 0 conv) → 验证流量基础建设 → 再启用

## §7 关键警告 (K3 升级, 不静默, 不重复 spam)

- 🟡 **Gmail IMAP 通道 D14 出现窗口期, 错过需等下个 GFW 放行周期** — 建议今天 (8/1 23:00 前) 补 App Password, cron 8/2 12:00 验证
- 🟡 **3 个 P1 aging 全部 ≥8d, 全部需 user 浏览器 1-5min 行动** — Claid PayPal + Printful 邮箱 + Gmail App Password
- 🟡 **cron 触发时间偏离 12:00 窗口 11h** (今日 22:55 vs 计划 12:00), mavis cron schedule 待 user 校准 (跟 7/30 5:02/5:16 同样问题, 3 次出现)
- 🟡 **Gelato 8/2 攒批 38+ 处替换** — 待 8/2 1 commit 1 push, build PASS 后 link_deployed:true
- 🟡 **7/30 教训二次确认**: 凭证 PASS ≠ 通道 PASS ≠ 通道 PERSISTENT. memory 应在下次 maintenance 更新: 5min verify 流程加 "凭证 OK + IMAP connect test OK + 持续 OK 跨 24h" 三段校验

## §8 后续 cron 触发计划

- **8/2 12:00** (攒批窗口) — agent cron + K3 攒批 1 push 一起
  - 替换 38+ 处站内 gelato.com 链接为 affiliate 链接
  - 验证 5 步真 verify 流水线 (sitemap mtime / curl 200+body / schema / IndexNow)
  - 修 .gitignore 凭证覆盖实测 (8.8.8.8 窗口期 + 凭证补 = 通道激活)
- **8/2 18:00** (晚间攒批) — 看 8/2 12:00 push 后 CF Pages 部署状态
- **8/3 12:00** — affiliate-monitor cron 下一窗口, 续扫 24h 邮件

## §9 commit hash

- 本轮动: `.hermes/affiliate-programs.json` (monitoring 段 8/1 22:55 状态更新 + network_diag_8_1_22_55 + high_signal_findings_24h_8_1_22_55) + AFFILIATE_LOG.md (本 entry) + `.hermes/logs/2026-08-01-affiliate-monitor.md` (本文件, §2.1 P0/P1/P2 状态表)
- **未 commit** (per cron 攒批纪律 + project.yaml can_deploy:false), 待 8/2 攒批 push 一起入 (跟 Gelato 38+ 替换同批)
- 7/30 5:02 + 5:16 + 8/1 22:55 三次都未 commit, 攒批 push 1 push/天 违规 0 次 ✅
- 7/30 K3 已 push commit 42cad0a (4 撤回 + 4 新文件) + 8/1 K3 已 push commit 86756b9 (Gelato 5 处替换 + GA4 埋点) — 当日 1 push, 违规 0 次 ✅
