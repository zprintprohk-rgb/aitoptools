# AIToolTools Daily-Ops 合并监控 — 2026-08-12 (cron 05:4x)

> 合并: affiliate-monitor + printful-watcher + tax-audit + ai-crawler-monitor
> 前置: 今日无 affiliate-monitor 独立日志 (首次运行); 8/11 affiliate-monitor 已全流程完成
> 标记: [OK]=正常 [SKIP]=跳过 [WARN]=注意 [WAIT]=等待

## AUTOCLAW_PRIMARY

| 模块 | 结果 |
|---|---|
| affiliate-monitor | [OK] IMAP 实拉 (SOCKS5 127.0.0.1:7892, SINCE 30-Jul **135 封全量核实**) — **🆕 新商户批次: Synthesia (Rewardful)** 8/11 3x 邮箱确认邮件 + 2x 密码重置 (jerome@aitoptools.net); 0 其他新审批; 已新增 affiliate-programs.json 条目 |
| Synthesia (新) | [WAIT] **applied-pending-email-confirm** — Welcome to Synthesia Affiliate Program - Personal Plan (Rewardful 网络). 激活邮件 SINCE=1天 < 90天约束 → **不自动点击**; 密码重置 x2 需 user 确认是否本人操作; 确认后取专属链接部署评审 |
| CF freebies | [SKIP] 8/12 freebie 尚未到货 (常规 ~11:00 CST; 8/11 UID 673 已解析, 20 素材 1 🎃); 素材池 6 天累计 26 🎃 (去重 25) 充足 |
| printful-watcher | [SKIP] — 按 8/8 实证 email_verified=true (无验证流程), status=active; 仅状态异常时检查 |
| tax-audit | [NOOP] 8/12 复核窗口: AutoGLM 1.1.8 只读 Printful dashboard/affiliate/tax → **W-8BEN-E 仍 Pending** (8/9 提交后第 3 个工作日窗口内, "documents reviewed in up to 3 business days", Edit 可用, 未做任何操作) — 非 Approved 非 Rejected; 下次复核 **8/13**; Impact LOGIN_REQUIRED (不自动登录) |
| ai-crawler-monitor | [WARN] **GEO_BLIND NODATA** — 无 CF Web Analytics beacon / 无 API token / 无 access log (无 wrangler.toml, src 无 cloudflareinsights 标签); 解锁方法: 部署 CF Web Analytics (免费, 加 script 标签) 或 GraphQL Analytics API token; robots.txt + llms.txt AI 爬虫放行健康 |

## P0 / P1 / P2 表

### P0 (离钱最近)
- [OK] **无** — 7 approved-active 全部 link_deployed=true; Printful tax 无阻塞 (Pending 属正常审核流程); P0 = 0 **连续第 4 天**

### P1 (观察/定时)
| 项 | 状态 | 说明 |
|---|---|---|
| Synthesia 邮箱确认 (新) | [WAIT] AWAITING-USER | 8/11 3x 确认邮件; SINCE<90d 不自动; user 手动点链接 (2min) 或确认忽略; 密码重置 x2 请确认本人操作 |
| Printful W-8BEN-E | [WAIT] Pending 待审 | 8/12 复核仍 Pending (3 工作日窗口最后一天); **8/13 再复核**; 若仍 Pending 需 user 浏览器补第 4/5 行 + 签名上传 |
| Printify promo code | [WAIT] AWAITING-REPLY | 回信 8/8 00:27 已发 5 天, 0 回复; **8/13-14 二次检查**, 无回复则升级 user 走 PartnerStack 站内渠道催 |
| Placeit (Impact) | [WAIT] pending | **8/14** 超期催办评估 (草稿 drafts/placeit-followup-email.md 就绪, user 手动发送) |

### P2 (暂缓, K3 7/30 拍板等 Kittl 跑通)
- 新申请候选: Hostinger / Jasper / Writesonic / Copy.ai
- PartnerStack Network 重试 (8/1 被拒, 待 user 拍板)
- Pinterest scheduler (not-configured) / GSC oauth (optional)
- Impact 登录复查 Kittl/Placeit tax (低优先)
- 跨项目: Supabase zprintpro 暂停 / togthr Deploy 失败 / GSC 索引通知 (均非本域)

## user 动作清单 (≤3)
1. **[2min] Synthesia 确认链接** — 8/11 欢迎邮件 "Please confirm your email address" (affiliates@rewardful.com) 内点确认 → 联盟账号激活; 顺带确认 17:51/17:59 两条密码重置是否本人操作 (若非本人, 检查 rewardful 账号安全)
2. **[留意] W-8BEN-E 审核** — 8/12 仍 Pending, 我 8/13 再复核; 若连续 Pending 需你浏览器补第 4/5 行 + 签名上传
3. **[留意] Printify promo 回复** — 8/13-14 我二次检查, 无回复则升级你走 PartnerStack 站内渠道催

## 文件变更 (本次)
- [OK] .hermes/affiliate-programs.json 更新: Synthesia 新条目 (18 programs) + Printful tax_audit 8/12 + high_signal_findings_24h_8_12 + tax_audit_8_12 + manual_checklist_2026_08_12 + milestone + aging; node 校验 JSON 有效
- [OK] AFFILIATE_LOG.md 追加 8/12 条目
- [OK] 本文件 .hermes/logs/daily-ops-2026-08-12.md + .hermes/logs/2026-08-12-affiliate-monitor.md 落盘 (幂等锚点)
- [NO] 无 git push (监控任务, 遵守约束)

## 约束遵守
- 不自动登录 (Impact LOGIN_REQUIRED 即停) / 不自动点击激活链接 (Synthesia SINCE=1天 < 90天) / 不发信 (Placeit 催办待 8/14 user) / 不付款
- 凭证: gmail_credentials.json PASS (16 字符 app password, imap_requires_proxy=true 走 SOCKS5 127.0.0.1:7892, 实测 login OK); IMAP_PASSWORD 兜底 .env 生效
- 关键激活邮件: Synthesia 8/11 (新, <90d 不动作, 报 user); 其余无
