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
