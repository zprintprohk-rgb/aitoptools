# Halloween 素材链跟踪 (2026-08-08 启动, K3 指令)

> 目的: 记录 CF 6 个 🎃 素材从设计→下单→收货→拍照的全流程进度。每日 brief 更新。
> 素材来源: .hermes/logs/cf-freebies/2026-08-06.md + 2026-08-07.md (Creative Fabrica 每日免费素材邮件)
> 价值链: 素材→ Kittl/Claid 设计 2-3 个 → Printful/Printify 测试单 ($30-50) → 收货拍照 → 照片墙 6 图 + Halloween 支柱帖源文件 + 毛利数据

## 素材清单 (6 个 🎃, 8/7 邮件主力)
| # | 素材 | 类型 | 下载 | 设计选择 | 下单 | 收货 | 拍照 |
|---|---|---|---|---|---|---|---|
| 1 | Gothic Skull Rose Bundle PNG (主推) | PNG bundle | 待下载 | 推荐 (8/11 Kittl 实测首选) | - | - | - |
| 2 | Halloween Coffee Hand Drawn PNG Bundle | PNG bundle | 待下载 | 候选 | - | - | - |
| 3 | Hallowen Bundle 3 | bundle | 待下载 | 候选 | - | - | - |
| 4 | Coquette Halloween PNG Bundle Spooky PNG | PNG bundle | 待下载 | 候选 (8/11 候选) | - | - | - |
| 5 | Minimal Line Art Mystic Black Cat Face | PNG | 待下载 | 候选 | - | - | - |
| 6 | Halloween Skeleton Hand Stripes PNG | PNG | 待下载 | 候选 | - | - | - |

## 时间线 (v2 指令集关键路径, 2026-08-08 对齐)
| 日期 | 里程碑 | 状态 |
|---|---|---|
| 8/9 | weekly-report 首跑基线读数 | 待执行 |
| 8/10 | 设计阶段: Kittl/Claid 用素材 [0:2] 做 2-3 个设计 → .hermes/designs/halloween-test-{date}.png | ⛔ BLOCKED (8/8 预检: 素材 0 文件 + 无 test-address.json); 正式触发时复查 |
| 8/11 | 下单阶段: Printful (若已 verify) 否则 Printify; 预算硬限 $25/单 $50/日; 记录 order_id/eta/cost | 待触发 |
| 8/11 | Kittl 实测日: CF 素材当源文件, 实测帖初稿 | - |
| 8/12-13 | Halloween 支柱帖《Halloween POD ideas 2026》写作 | - |
| 8/14 | T+7 首读数 → 决定集群是否加速 | - |
| 8/15 | 收货拍照: logistics.status=delivered 触发; user 拍照 OR fallback 官方 mockup → public/photos/wall/halloween-{order_id}.jpg | 待触发 |
| 8/17 | Halloween 辖条① (CF 免费万圣节素材实测) 上线 | - |
| 8/18 | 支柱帖上线 + 集群截止 (23:59) | - |

## 执行参数 (v2 指令集, 2026-08-08)
- 下单平台: Printful (if verified) else Printify
- 预算: $25/order hard limit, $50/day hard limit, 超限暂停+告警
- 收货地址: test-address.json (用户提供)
- 照片: 优先 user 拍照; 用户不可用 → fallback 官方 mockup
- 产出: 照片墙 6 图 + 支柱帖源文件 + 毛利数据

## 每日 brief 更新记录
- 2026-08-08: 跟踪器创建; 6 素材均待下载 (CF 登录后下载)
- 2026-08-10: (cron 提前触发, 实际运行 8/8 01:49 CST) 前置检查 → **BLOCKED**: ① assets/cf-halloween-2026-08-07/ 目录存在但 0 文件 (6 素材均需 user CF 登录下载, 跟踪链在 8/7 邮件); ② printful_session_cookie 缺失, Printify 联盟链可用 (try.printify.com/4fs863rfz2yc) 但无 merchant 会话无法实际下单; ③ test-address.json 缺失 (无收货地址)。design/order 未触发, 无支付操作。User 手工清单已发。

## 8/8 增量动作: 素材前置确认
- .hermes/assets/cf-halloween-2026-08-07/ = **0 文件** (user 尚未从 CF 下载)
- 影响: 8/10 seasonal-exec 将 blocked (素材为 design 前置)
- 动作: user 在 8/10 前从 CF 邮件下载 (清单 .hermes/logs/cf-freebies/2026-08-07.md, 建议 Gothic Skull Rose + Coquette Halloween)
## 8/9 每日 brief
- 8/9 weekly-report 首跑基线读数: ✅ 完成 (cron 07:47, 产物 .hermes/reports/weekly-2026-08-09.md, commit 9505612 16:58)
- 素材池新增 (8/9 CF 邮件, affiliate-monitor 16:3x 解析): +5 🎃 (Fall Halloween Sublimation Bundle / 32 Cute Halloween Ghost Pngs / Spooky Halloween Shop Clipart / Vintage Halloween Ghost Witch / Spooky Pumpkin Chase) → 4 天累计 19 🎃
- 8/11 Kittl 实测首选更新: affiliate-monitor 建议 **Fall Halloween Sublimation Bundle** (8/9 主推) 并列 Gothic Skull Rose (8/7 主推); 实测日二选一或都用
- 8/10 设计阶段前置复查: assets/cf-halloween-2026-08-07/ 仍 **0 文件** (user 未下载) + test-address.json 缺失 → 8/10 seasonal-exec 预期仍 BLOCKED, 已提醒 user
## 8/9 晚间 (Hermes daily-content 19:45)
- 🎃 支柱 blog《25 Halloween POD Ideas for 2026》**提前 6 天上线** (原排期 8/15): src/data/blog-posts.json + build 346 页 + IndexNow 200; 主 CTA Claid / 副 CTA Printful; 2790 字, 内含 8/9 免费素材表 (Fall Halloween Sublimation Bundle 等 5 项) — 8/11 Kittl 实测可直接引用该文素材链接
- 素材下载仍是唯一阻塞点: .hermes/assets/cf-halloween-2026-08-07/ = 0 文件, 待 user 下载 → 8/10 seasonal-exec 状态维持 BLOCKED

## 8/10 每日 brief (2026-08-10 11:38, cron 63a4beaf 19:37 CST)
- seasonal-exec 触发: 8/10 推进模式 → **BLOCKED** (3/3 前置失败)
- ① assets/cf-halloween-2026-08-07/ = 0 文件 (user 未下载 CF 素材, 清单见 .hermes/logs/cf-freebies/2026-08-07.md 含 6 🎃)
- ② printful_session_cookie 缺失 (无 Printful 会话, 无法下单; Printify 联盟链可用但无 merchant 会话)
- ③ test-address.json 缺失 (无收货地址)
- design/order/GEO 均未触发; 无支付操作
- 阻塞解药: user (1) 登录 CF 下载至少 2 🎃 素材到 assets/cf-halloween-2026-08-07/ (建议 Gothic Skull Rose + Coquette Halloween) (2) 提供 test-address.json 收货地址 (3) 提供 Printful 登录 cookie 或确认 Printify 可用
- 下一个触发窗口: 8/11 Kittl 实测日 (原排期), 如素材未就位则顺延

## 8/11 00:15 · 素材策略调整 (CF 付费墙实证)
- **CF 自动化下载路径不存在** (浏览器 4 次尝试实证): 全部 Halloween 素材绑定 All Access 订阅 (免费试用需信用卡, 安全拒绝)
- **设计源切换**: Kittl 内置 Halloween 模板 (Fall Halloween Sublimation Bundle 等) 为主源; CF 素材降级为可选加分项 (user 手动下载时使用)
- **B1 解除硬阻塞**: 8/11 Kittl 实测照常执行 (模板源), 素材链 ①设计 不再依赖 CF 下载
- 影响: Halloween 链 8/18 目标不受影响; 测试单/照片墙/支柱帖全链可正常推进

## 8/14 每日 brief (2026-08-14 05:29, 季节集群 cron D-4 检查)
- 判定: **PARTIAL** (详见 .hermes/logs/halloween-deadline-0818.md)
- 素材链仍 0/4: 设计 0 文件 (8/11 Kittl 实测仅观察, 无产出); 下单无 order_id (printful cookie 仍缺, 唯一硬阻塞); 拍照 0/6; 毛利无
- 进展: test-address.json ✅ 已就位; B1 素材阻塞已解除 (设计源=Kittl 模板)
- 内容: 支柱 halloween-pod-ideas-2026 ✅ (8/9) + 辐条② printful-vs-printify-halloween-2026 ✅ (8/11); 辐条① 排期 8/17 未上线
- sitemap 342 / IndexNow: 支柱 8/9 1/1 200, 辐条② 8/13 4/4 200 ✅; GEO llms.txt 缺 2 条 ❌

## 8/21 每日 brief (2026-08-21 18:4x, 季节集群 cron 补判 — 8/18 19:37 402 失败后 user 立即执行)
- 判定: **PARTIAL** (详见 .hermes/logs/halloween-deadline-0821.md, 3845B)
- 内容: 5/5 全量上线 ✅ (支柱 + 辐条①②③④, 8/17 W3 push commit 3fe94ee); sitemap 347 / IndexNow 8/17 5/5 200 / llms.txt 4 行 / FAQPage 5/5 — 内容侧 LAUNCHED
- 素材链仍 0/4: designs/ MISSING, 无 order_id (printful cookie 仍缺 = D6 唯一硬阻塞), photos/wall/ MISSING, 毛利无
- 8/25 W3 job (98ebd150) 已提前执行完 (halloween-full-0825.md), 排期冗余待 user 确认
