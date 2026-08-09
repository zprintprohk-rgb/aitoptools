# 联盟审批监控 — 2026-08-09 (cron, 16:3x 执行)

**状态**: ✅ 完成 · Gmail IMAP RESTORED (SOCKS5 127.0.0.1:7892) · 0 新审批
**扫描窗口**: SINCE 08-Aug-2026, 23 封全量核实 (含跨项目噪音)

## §2.1 状态表 (P0/P1/P2 排序)

### P0 (离钱最近, 需 user 行动)
| 项 | 状态 | 天数 | 说明 |
|---|---|---|---|
| Printful 邮箱确认 | 🔴 BLOCKER | D20 | 7/20 确认链接已过期 (8/8 headless 实测 "Email confirmation request does not exist"), 后台重发被阻 = `printful_session_cookie` 缺失. **user 二选一**: A) 装 AutoGLM Chrome 扩展 (2min) → AutoClaw 自动提取; B) 手动 F12 复制 cookie → `.hermes/secrets/printful_session_cookie.txt` → watcher (每时 8-22) 自动重发. 佣金结算前置, 唯一未激活项 |

### P1 (观察/定时触发)
| 项 | 状态 | 说明 |
|---|---|---|
| Printify promo code | ⏳ AWAITING-REPLY | 回信 8/8 00:27 已发 (SMTP 465 留证); 今日无回复属正常 — **8/11 检查窗口** (monitor cron 覆盖 mail.printify.com) |
| Placeit (Impact) | ⏸ pending | 8/14 超期催办: 草稿 `drafts/placeit-followup-email.md` 就绪 (中英各一版), 8/14 当天评估, 严禁自动发送 |

### P2 (暂缓清单, K3 7/30 拍板等 Kittl 跑通)
- 新申请候选: Hostinger / Jasper / Writesonic / Copy.ai
- PartnerStack Network 重试 (8/1 被拒, 待 user 拍板)
- Pinterest scheduler (not-configured, 不影响佣金)
- GSC oauth (optional, 数据管线降级本地 csv)
- Supabase zprintpro 暂停 (跨项目)

## 今日扫描结果

- **0 新审批 / 0 新商户邮件** (SINCE 08-Aug 23 封: togthr CI 失败 x12 + GSC 通知 x7 + LinkedIn x1 + CF freebie x1)
- **✅ CF freebie 8/9 已解析** (UID 640 "Fall Halloween Sublimation Bundle & 19 more", 提前 23:24 到达): 20 素材 → `.hermes/logs/cf-freebies/2026-08-09.md`
  - 🎃 万圣节 x5 (Fall Halloween Sublimation Bundle / Ghost Pngs / Spooky Shop / Vintage Ghost Witch / Pumpkin Chase)
  - 🍂 秋季 x1 (Coquette Fall) / 🎄 圣诞早鸟 x1 (Retro Holly) / 📦 x13
  - **素材池 4 天累计 19 🎃** — 远超 Halloween 辐条①门槛; 8/11 Kittl 实测建议用 Fall Halloween Sublimation Bundle (升华烫画 = Kittl 主要场景)
- **链接部署核查**: 7 approved-active 全部 link_deployed=true, 0 缺失 (NordVPN/Printful/Mockey/Gelato/Printify/Claid/Kittl)
- **5 要素**: P0=1 (Printful cookie, 已批准未激活) / P1=2 (Printify 8/11 / Placeit 8/14) / P2=7 (暂缓) / 新申请=0 / 新获批=0

## 已完成

- ✅ `.hermes/affiliate-programs.json` 更新 (last_updated 2026-08-09 + high_signal_findings_24h_8_9 + manual_checklist_2026_08_09)
- ✅ `AFFILIATE_LOG.md` 今日 entry 追加
- ✅ `.hermes/logs/cf-freebies/2026-08-09.md` 落盘 (20 素材)
- ✅ 无新获批 → 无需部署流程 (24h 规则 N/A)
- ✅ 今日无 push (监控任务, 无紧急修复; 攒批纪律维持)

## 异常上报

- ❌ 无 (Gmail 通道 OK, 无钓鱼/陌生域名 ≥5, 无 approved→declined 跳变)
- 跨项目提醒 (非本域): togthr Deploy to Workers 失败 x12 (8/7-8/8); GSC zprintpro.com 索引问题通知 x7; Supabase zprintpro 暂停 (8/5 已报)
