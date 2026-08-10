# 📊 aitoptools 北极星周报 — 2026-08-09 (周日, Week 32)

> 生成: 2026-08-09 21:0x (Asia/Shanghai) · cron: aitoptools-weekly-report (Hermes 21:00)
> 关联: AutoClaw 07:47 正式版 (.hermes/reports/weekly-2026-08-09.md, commit 9505612) 已出; 本报告为 21:00 交付版, 数据同源
> 数据源: data/gsc_data.json (8/7 导出, 6/28-8/5) · affiliate-programs.json (8/9 16:5x) · AFFILIATE_LOG.md · gsc-indexnow-state.json

## 数据可用性标记
- **GSC**: 🟡 gsc-oauth.json 缺失 (仅 template) → OAuth API 不可用; 用 8/7 本地真实导出 (6/28-8/5, 2044 展示 / 3 点击 / CTR 0.15%, 427 queries)
- **GA4**: 🔴 无 GA4 凭证 → affiliate_click 事件数据不可用; 以 GSC 页面维度 + 联盟后台定性信号近似

## 1. GSC top queries (6/28-8/5, 真实导出 TOP 15)

| # | query | 展示 | 点击 | 排名 | 有专页? | 状态/动作 |
|---|-------|------|------|------|--------|----------|
| 1 | midjourney review | 57 | 0 | 84.6 | ✅ | Boost #5 排 8/17 |
| 2 | jasper ai review | 52 | 0 | 91.5 | ✅ | Boost #6 排 8/17 |
| 3 | printful alternatives | 45 | 0 | 74.9 | ✅ | 内链强化 |
| 4 | runway ml | 42 | 0 | 68.7 | ✅ | Boost #2 DONE (8/8), T+7 观察 |
| 5 | printify vs printful | 35 | 0 | 86.1 | ✅ | 内链强化 |
| 6 | is magicdrop legit | 33 | 0 | 64.6 | ✅ | Boost #3 排 8/11 |
| 7 | sticker mule | 26 | 0 | 37.3 | ✅ | Boost #1 DONE (8/8), T+7 观察 |
| 8 | print price ai tool | 26 | 0 | 69.5 | ✅ | Boost #4 排 8/13 (8/21 ≤30 里程碑) |
| 9 | runwayml | 26 | 0 | 70.6 | ⚠️ typo | 归并 runway-ml-review |
| 10 | best ai background remover | 26 | 0 | 96.8 | ✅ | 内链强化 |
| 11 | omnisend review | 24 | 0 | 84.2 | ✅ | 内链强化 |
| 12 | printify alternatives | 21 | 0 | 82.6 | ✅ | 内链强化 |
| 13 | manychat shopify | 21 | 0 | 90.6 | ✅ | 内链强化 |
| 14 | alternatives to printify | 18 | 0 | 83.3 | ✅ | 内链强化 |
| 15 | kittl | 16 | 0 | 69.6 | ✅ | 8/11 实测日 (Halloween) |

**趋势**: 7/29 起展示爬坡 (131→240/日), 8/1 峰值 241; 全站 3 点击, 品牌词 aitoptools (1) + teelaunch (1, pos 7) + namecheap hosting review (1, pos 50)
**挖矿结论**: 展示≥10 的 27 个 query 全部已有专页或已入队 (8/9 daily-search 已扫) → **无新增队列词**; teelaunch (2 imp/1 clk, pos 7) 低于 10 阈值, 观察不追加

## 2. CTR 榜 (页面维度, GA4 不可用 → GSC 近似)

| 页面 | 展示 | 点击 | CTR | 排名 | 解读 |
|------|------|------|-----|------|------|
| /namecheap-review | 6 | 1 | 16.7% | 66.8 | 偶然点击, 样本小 |
| /elevenlabs-review | 9 | 1 | 11.1% | 47.8 | 偶然点击, 样本小 |
| /best/printify-alternatives | 69 | 1 | 1.4% | 76.8 | 唯一有量页面, 排名深 (Boost 候选) |

**0 点击高展示 Boost 候选池**: /runway-ml-review 201 (63.0) · /stickermule-review 179 (35.1) · /best/printful-alternatives 140 (68.0) · /jasper-ai-review 93 (86.9) · /compare/printful-vs-printify 83 (77.0)
**联盟定性信号** (无数字): Printify 8/7 PartnerStack 主动邮件 "link is getting some activity!" = 归因链路首次工作; NordVPN 3 处跟踪链 8/7 上线可归因

## 3. 联盟状态变化 (本周 8/2-8/9)

| 平台 | 状态 | 本周变化 | 下周动作 |
|------|------|---------|---------|
| Printful | ✅ Active / 7,023 点击 / 1 注册 / $0 | 8/8 邮箱阻塞实证解除 (email_verified=true); **W-8BEN-E 已提交, 8/9 实证 Pending 待审 (≤3 工作日)** | user 签字上传 → 8/12 复核 (T5) |
| Printify | ✅ approved / 首次活动信号 | 8/7 首次点击; 8/8 promo 回信已发 (SMTP 留证) | **8/11 查回复** → 码到建 /promo/printify-promo-code |
| Claid | ✅ approved / 收款全通 (PayPal Net-15, $20 自动) | — | 首个可收款账户维持 |
| Mockey | ✅ approved (30% recurring / 90d cookie) | — | — |
| Kittl | ✅ approved (Impact, 20% 首 12 月) | 14d 基线 1 click / 0 action / $0 | 8/11 实测日 (Fall Halloween Bundle) |
| Gelato | ✅ approved / link deployed | — | PayPal 收款待设 (P2) |
| NordVPN | ✅ approved / 跟踪链上线 | 8/7 link_deployed=true (3 处字节级验证) | GA4 核对 affiliate_click 事件 |
| Placeit | ⏳ pending (Impact) | — | 8/14 催办评估 (草稿就绪, 严禁自动发送) |
| Creative Fabrica | 素材池 (非佣金) | 8/6-8/9 连续 4 天解析, **19 🎃 万圣节素材** | Halloween 辐条① (8/17) 素材源 |
| 北极星 | **$0 / $3000 (0%)** | 冷启动期, 预期内 | 8/14 T+7 首读数 |

**汇总**: 7 approved-active 全部 link_deployed=true (0 缺失); 1 pending (Placeit); 新申请候选维持暂缓 (等 Kittl 跑通)

## 4. 下周 user 手工清单 (≤3 条, 按离钱近排序)

1. **Printful W-8BEN-E 签字上传** — 8/9 实证 Pending 待审, 黄框提示需填第 4/5 行后签名上传; 解锁 payout 链路 (离钱最近) — 约 5 分钟
2. **提供测试收货地址** (BOARD D1, 写入 test-address.json) — Halloween 季节集群下单环节唯一阻塞 (个人地址信息, 执行层不得自造) — 约 2 分钟
3. **GSC OAuth 配置** (BOARD D2, 一次性) — 从手动导出升级为每日自动数据, 8/14 T+7 读数不再依赖人工 — 约 10 分钟

## 优化建议 (3-5 条)

1. **CTR 瓶颈 = 排名深度**: 98% 展示落在 pos≥60 (1119/2044 展示), 唯一有量页 /best/printify-alternatives 排名 76.8 → Boost 节奏 (8/11 #3 / 8/13 #4) 是当前唯一可控杠杆, 维持 2-3 页/周
2. **Printify promo code 是本周最高确定性变现动作**: 8/11 检查回复 → 码到即建 /promo/printify-promo-code 页 + 全站 Printify CTA 挂码 (对标 $150 blog challenge 9/29 截止)
3. **GSC OAuth (D2) 优先于 GA4**: 一个授权解锁每日数据驱动选题 (挖矿/推排名), GA4 无凭证本周不投入
4. **GEO_BLIND 低优先**: CF Web Analytics beacon (D3) 一行代码解锁 AI 爬虫数据, 但相对佣金变现链优先级最低
5. **teelaunch (pos 7, 有点击) 观察**: POD 印刷商品牌词, 若下周展示≥10 可建专页收割 (低投入)

---
*本报告只读生成, 未修改数据文件 / 未 push / 未 build; 选题队列无新增 (gsc-mining-queue.md 8/9 已同步)*
