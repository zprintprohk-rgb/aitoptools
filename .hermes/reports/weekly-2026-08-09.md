# 周报 2026-08-09 (Week 32) — aitoptools.net

> 生成: 2026-08-08 01:49 (Asia/Shanghai) · 首次周报基线 (weekly-report 首跑)
> 数据源状态: GSC 凭证缺失 (gsc-oauth.json 不存在, 本地无 gsc_data.csv) → 块 1 如实标注 blocked_missing_credentials; GA4 affiliate_click 无凭证 → 块 2 定性信号 + blocked

## 块 1 — GSC top queries

**blocked_missing_credentials** (F:\aitoptools\.hermes\secrets\gsc-oauth.json 不存在, data/ 仅有 keywords-200.csv 选题库, 非流量数据; 不编造数字)

| query | 展示 | 点击 | CTR | 排名 | 变动 vs 上周 | 是否有专页 | 进队列? |
|---|---|---|---|---|---|---|---|
| (无 GSC 数据, 待 user 配置 OAuth) | - | - | - | - | - | - | 否 |

已知流量锚点 (gsc-mining-queue 8/7 记录, 非本轮新数据): print price ai tools — 23 展示 / 排名 70 / 有专页 / 已在 Boost Queue。

## 块 2 — CTR 榜 (来源×商户组合)

**blocked_missing_credentials** (GA4 affiliate_click 事件无凭证, 各联盟后台无点击数字)

| 页面 | 商户 | 点击 | 展示 | CTR | 上周 CTR | 动作 (杀/加/提权) |
|---|---|---|---|---|---|---|
| (无 GA4 affiliate_click 数据) | - | - | - | - | - | - |

定性信号 (联盟后台邮件, 无数字):
- **Printify** 8/7 "Your Printify link is getting some activity!" (PartnerStack 主动邮件) — 首次点击信号, 归因链路开始工作 → 等 8/11 promo code 回复, 码到建 /promo/printify-promo-code
- **NordVPN** 8/7 闭环: 线上 3 处 go.nordvpn.net 跟踪链, 点击可归因 (后台无数字)
- **Printful** 坏链已修复上线, 但邮箱未确认 → 点击仍零归因风险

## 块 3 — 联盟状态

| 平台 | 状态 | 本周变动 | 下周动作 |
|---|---|---|---|
| Printful | approved / link deployed / 邮箱未激活 | 8/8 headless 实测确认 7/17+7/20 确认链接均已过期; 后台重发被阻 (缺 printful_session_cookie) | user 补录 cookie → 重发确认; 否则 10%×12 佣金无法结算 |
| Printify | approved / deployed | 8/7 首次点击信号; 8/8 00:50 promo code 回信已发 (SMTP 留证) | 8/11 查回复; 码到即建 /promo/ 页 |
| Claid | approved / 收款链路全通 (PayPal doolen@126.com, Net-15) | 无 | 重置密码收尾 (若 8/4 链接未点) |
| Mockey | approved / deployed (30% recurring, 90-day cookie) | 无 | — |
| Kittl | approved / deployed (7/30) | 无 | 8/11 实测日 (Halloween 素材当源文件) |
| Gelato | approved / deployed (8/2 攒批 38+ 处替换已上线) | 无 | PayPal 收款设置 (dash.partnerstack.com) |
| Placeit | pending (Impact) | 无 | 8/14 超期催促邮件 (草稿已就绪) |
| Creative Fabrica | freebies 管道活跃 (素材, 非佣金) | 8/7 新邮件 20 素材, 含 6 个万圣节 | 支撑 8/10-8/18 Halloween 素材链 |
| NordVPN | approved / deployed 闭环 | 8/7 link_deployed=true (3 处跟踪链字节级验证) | — |
| PartnerStack Network / Deel | declined / blocked | 8/1 拒绝确认 (IMAP 独立核实) | 重试需 user 拍板 |
| 新申请候选 (Hostinger/Jasper/Writesonic/Copy.ai 等) | 暂缓 | — | 等 Kittl 跑通 (7/30 拍板) |

北极星: **$0 / $3000 by 2027-01-15 (0%)**

## 块 4 — user 手工清单 (≤3 条)

1. **Printful 确认邮件重发**: 补录 printful_session_cookie 到 .hermes/secrets (硬阻塞; 否则 Printful 佣金无法结算) — 5 分钟
2. **Gelato PayPal 收款设置**: dash.partnerstack.com 绑定收款方式 (佣金到账前提) — 5 分钟
3. **Claid 重置密码**: 若 8/4 重置邮件链接未点 → 设新密码 + 更新本地凭证 — 3 分钟

---
## 附: Halloween 进度 (halloween-asset-chain.md)

**进度: 5%** (8/9 weekly-report 基线读数, 里程碑达成)

- 素材识别: 6/6 ✅ (8/7 CF 邮件解析落盘)
- 下载: 0/6 (待 CF 登录后下载)
- 设计选择: 预推荐 6/6 (Gothic Skull Rose 主推, 8/11 Kittl 实测首选)
- 下单 / 收货 / 拍照: 0
- 下一里程碑: 8/10 10:00 设计阶段 (Kittl/Claid, 素材 [0:2] → 2-3 个设计, 预算 $25/单 $50/日)

## 后处理记录

- print price ai tool 排名 70 > 50 → **已在** CONTENT_PLAN.md Boost Queue (2026-08-07 条目, in-progress) → 幂等跳过, 不重复追加
- GSC 无数据 → 无 query 满足「展示≥10 且无专页」→ Data-Driven Queue 无追加
- gsc-mining-queue.md 已更新 (见该文件尾部)
