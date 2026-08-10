# 联盟审批监控 — 2026-08-10

**执行**: Hermes affiliate-monitor cron 12:1x Asia/Shanghai
**IMAP**: SOCKS5 127.0.0.1:7892 → imap.gmail.com:993 ✅ (SINCE 09-Aug 28 封全量核实)
**北极星**: CPA/CPS 佣金/月 → $3000/6月 (当前 $0, 7 approved-active 等待流量)

## §1 邮件扫描结果
- **0 新审批 / 0 新商户邮件** (28 封全量核实)
- 新到 2 封相关: CF freebie 8/10 (UID 662, 已解析) + Printify 8/9 营销邮件 (非 promo 回复)
- 噪音: togthr CI 失败 x10 / GSC x8 / GBP 月报 x1 / LinkedIn x1 (全跨项目)

## §2 状态表 (P0/P1/P2 排序)

### P0 = 0 🔴→✅
- Printful cookie BLOCKER 已于 8/9 解除 (email_verified=true); 7 approved-active 全 link_deployed (8/10 affiliates.json 字节级核查: printify/printful/gelato/kittl/creative-fabrica/claid/mockey 真链, picjam/greenonion pending 空链 = 已知基线)
- 自 8/9 起 P0 首次清空 — 无阻塞项

### P1 = 2
| 项 | 状态 | 行动 | 截止 |
|---|---|---|---|
| Printify promo code 回复 | AWAITING-REPLY (回信 8/8 00:27 已发) | 8/11 monitor 检查回复; 码到即建 /promo/printify-promo-code 页 | 8/11 |
| Placeit Impact pending | pending (Impact Marketplace 已过, 7/15 申请) | 8/14 超期催办评估 — 草稿 drafts/placeit-followup-email.md 已就绪, 当天评估发送 (user 手动) | 8/14 |

### P2 = 7 (维持暂缓)
- 新申请候选: Hostinger / Jasper / Writesonic / Copy.ai (K3 7/30 拍板等 Kittl 跑通)
- PartnerStack Network 重试 (待 user 拍板) / Pinterest scheduler (未配置) / GSC oauth (optional) / Supabase zprintpro 暂停 (跨项目)

## §3 CF freebie (v5 解析器)
- 8/10: UID 662 "Handmade & 19 more" → 21 素材落盘 .hermes/logs/cf-freebies/2026-08-10.md
- 🎃 x6 (Black Cat Embroidery=印刷垂直强相关 / Witch Cat Coven / Spooky Bundle / Camo Ghost Boo / Preppy Frames / Skeletons Dancing 重复)
- 素材池 5 天累计 25 🎃 (去重 24) — 远超辐条①门槛; 8/11 Kittl 实测建议: Fall Halloween Sublimation Bundle 或 Black Cat Embroidery

## §4 链接部署核查
- 无新获批 → 无新部署动作; 7/7 已部署 ✅

## §5 下个检查点
- **8/11**: Printify promo 回复检查 (mail.printify.com) + Kittl 实测日 (素材就绪)
- **8/12**: tax-audit 复核 (Printful W-8BEN-E Pending <=3 工作日)
- **8/14**: Placeit 超期催办 (草稿就绪, user 手动发)

**Status**: ✅ Complete (P0=0, 无阻塞, 无 push)
