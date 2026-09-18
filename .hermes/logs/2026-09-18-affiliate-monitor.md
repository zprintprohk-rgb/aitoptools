# aitoptools.net · 每日联盟申请审批监控 — 2026-09-18

**任务**: aitoptools-affiliate-monitor · **执行**: 2026-09-18 12:0x CST (午间低谷窗口 12:05-13:30)
**模型**: deepseek-v4-flash · **北极星**: CPA/CPS 佣金/月 (6 个月目标 $3000)
**当前动作支撑赚钱目标**: 保住联盟归因链路 + 清扫待激活闸门 (Printful 税务 / Synthesia 确认 / Placeit 催办), 使已获批 7 个程序的流量能转化为可结算佣金

---

## 🔴 P0 — 402 全链停摆第 2 轮 (最高优先, 需 user 决定)

| 项 | 实况 |
|---|---|
| 停摆窗口 | **2026-09-14 → 09-17 (连续 4 天)** |
| 失败面 | executions.db 按天聚合: 9/14=10 · 9/15=8 · 9/16=9 · 9/17=7 条失败, 全站 cron 无一幸免 |
| 错误 | `RuntimeError: HTTP 402: Insufficient Balance` (DeepSeek) — **全部同一错误**, 非超时/非网络 |
| 恢复 | 9/18 12:03 起 completed 2 / running 1 (本 run) |
| 首轮对照 | 8/28 → 9/11 停摆 15 天, 9/12 恢复 → **本轮是同一根因复发** |

**根因 (未除)**: `C:\Users\Administrator\AppData\Local\hermes\config.yaml` **L512 `# fallback_model:` 仍整段注释** =
主模型 402 后**无 failover**, `.env` 里的 `MINIMAX_CN_API_KEY` 未接线。

**余额实查** (GET /user/balance, 2026-09-18 12:0x):

| 日期 | total_balance (CNY) | 备注 |
|---|---|---|
| 2026-09-12 | 1.59 | 首轮停摆未期 |
| 2026-09-13 | 9.54 | 已充值 |
| **2026-09-18** | **7.45** | granted 0.00 / topped_up 7.45 · is_available=true |

→ 水位趋势显示**单日消耗约 1-2 CNY 量级**, 7.45 仅够数日。**"今日跑通" ≠ 已修复**。

**升级 (二选一)**:
1. **充值 DeepSeek** — 建议一次性 ≥100 CNY, 否则将维持"三天一断"节奏 (每断 4 天 = 联盟监控/内容生产/IndexNow 全停)
2. **接线 MINIMAX fallback** — 取消 `config.yaml` L512 注释即可 (`.env` 已备 `MINIMAX_CN_API_KEY`); 属配置改动, K3 可代改, 无需 user 操作

> 依 AGENTS.md「模型余额监控规则」: 402 持续 2 天即升级 user。本项**已复发**, 且首轮超期 13 天未处理。

---

## §2.1 状态表 (按 P0 / P1 / P2 排序)

| 优先级 | 项 | 状态 | 距钱的距离 |
|---|---|---|---|
| 🔴 P0 | **402 停摆第 2 轮 / fallback 未接** | 4 天全 cron 失败, 余额 7.45 CNY | 全站停摆 = 归因链路归零 |
| 🔴 P0 | **Printful W-8BEN 重传** | **第 29 天** 未动, payout_ready=false | 唯一挡住佣金结算的税务闸门 |
| 🟠 P1 | Synthesia 确认邮件 | 第 38 天 (8/11 申请, Rewardful) | 第 8 个程序待激活 |
| 🟠 P1 | Placeit 催办 | pending **超 45 天**, 草稿就绪 | 待 user 手动发邮件 |
| 🟠 P1 | filter_senders 漂移 | **第 7 天** 未修 | 每日巡检需绕道 (效率损失) |
| 🟡 P2 | Claid manager check-in 回信 | Gabriela 8/31 询问, 已 18 天 | 机会窗口收窄 |
| 🟡 P2 | Printify 内容联动 | 9/15 唤醒邮件 + 码 AITOOLTOOLS20 | 有流量无转化 |
| ✅ 完成 | 部署缺口 | **0** (全部 approved 已上线) | — |
| ✅ 完成 | CF 素材池 | 22 期 / 73 🎃 / 59 🎄 (累计增) | Halloween 集群燃料 |

---

## 📧 邮件巡检 (IMAP 实拉)

- **通道**: SOCKS5 `127.0.0.1:7892` → `imap.gmail.com:993` 登录 OK
- **方法**: **全 9 个文件夹** SINCE 08-Sep (依 9/13 教训: `[Gmail]/&V4NXPpD1TvY-` 促销夹必扫, INBOX-only 会漏读) + INBOX SINCE 25-Aug 全量 53 封
- **结论**: **0 新审批 / 0 商户回复 / 0 税务邮件** — 自 2026-08-26 起 **22 天 0 新审批**

**发件域名景观 (16 个, 无 ≥5 封陌生域名 → 无钓鱼风险)**

| 域名 | 封数 | 判读 |
|---|---|---|
| google.com | 16 | 商店品质报告 / zprintpro.com 结构化数据告警 (跨项目) |
| creativefabrica.com | 7 | free picks (→ 见下节) |
| newsletter.printful.com | 6 | Amplified 内容营销 (9/4 Kittl 50% off 年付) |
| supabase.com | 5 | togthr-life 已暂停 (跨项目 Project B) |
| wired.business | 3 | AI 工具周报 (潜在雷达源) |
| claid.ai | 2 | 月报 (9/1) + 促销 (8/31) |
| printify.com | 2 | 唤醒邮件 x2 |
| github.com / gmail.com / printful.com / info.printful.com / linkedin.com / notify.cloudflare.com / mail.gocline.com / em1.cloudflare.com / updates.resend.com | 各 1-2 | 无异常 |

---

## 🎃 CF freebie 素材池 (解析器 v5.1, 全文件夹)

**22 期 / 73 🎃 (45 已映射干净 URL) / 59 🎄 (36 已映射)** — 较 9/13 的 17/56/47 **+5 期 / +17 🎃 / +12 🎄**

- 9/13 后新增: **9/14 · 9/15 · 9/16 · 9/18** (每日到货, 无断供 → **再次确认 9/13 全文件夹修正有效**)
- 本轮新入池万圣节素材示例: Halloween Preppy Brushstroke PNG Bundle · Funny Ghost and Pumpkin Art · Halloween Seamless Pattern Set · Rhinestone Glam Halloween Ghost PNG · Halloween Skeleton Dancing · Witches Children · Whimsical Halloween Ghost Clipart Bundle
- 圣诞/Q4 侧同样在快速累积 (Snowman Christmas Winter Scene · Christmas T-Rex · Christmas Alphabet Gold Letters) → 为 12 月集群预铺
- **距 10/31 约 6 周** → 落在 6-8 周启动窗内, **Halloween 集群辐条①燃料充足, 可执行**
- 落盘: `.hermes/logs/cf-freebies/2026-09-18.md` (16.7 KB)
- ⚠️ 合规: 只用 `url=` 解出的**干净产品页 URL**, 不发布 `mailer-public...visit?...` 邮件追踪链

---

## 🔧 核心复验 ① — Printful 链接字节级 (0 坏链)

依 AGENTS.md「终端脱敏判定规则」, **不凭终端显示上报坏链**:

| 检查 | 结果 |
|---|---|
| `my_link_printful` (repr + ord) | **68 字符 · star_count=0 · 尾 `8db2fbabcacc4a`** → 完整 |
| 文件中字面 `***` | **7 处**, 全为 8/5 脱敏事件的**历史叙述文字** + **9/13 复核 note 自身引用** (9/13 记 4 处 → 现 7 处, 系 note 引用增加, **非新问题**) |
| `out/` 366 个 HTML 字面 `***` | **0** |
| **结论** | **0 坏链, 无需修复** (8/5 与 9/13 教训均未违反) |

## 🔧 核心复验 ② — 站点健康 & 部署缺口

- `https://aitoptools.net/` → **HTTP 200**
- CSS hashed 核对: 本地 `41d6f17fd1783abd.css` **==** 线上 `41d6f17fd1783abd.css` → **最新构建已上线**
  (自 9/13 起无新 push, 与 402 停摆期零产出**逻辑自洽**)
- 构建 HTML 文件数 **366**
- **部署缺口 = 0**: out/ 全量命中 — mockey 169 · printify 144 · kittl 140 · printful 138 · claid 124 · gelato 91 · nordvpn 29
  (计数为出现次数非页面数, 与 9/13 口径不同, 同为 >0; Kittl 走 `pxf_link=https://kittl.pxf.io/qWNvPn` 独立字段, 已单独核验 140 次)

---

## 🟠 新发现 — src/ 有未构建未推送的内链改写 (交接给 daily-content)

本轮验证时发现 `src/` 相对 HEAD 有 **3 个文件 / 17 行** 未提交改动（**非本 run 所为**，作用域检查已证明):

| 文件 | 条目 | 改动性质 |
|---|---|---|
| `src/data/reviews.json` | gear-launch-review-2026 · jasper-ai-review · kittl-review · midjourney-review | content 内 **插入 `/best/*` 内链** |
| `src/data/comparisons.json` | kittl-vs-canva | content 内 **删去 `/reviews` 路径段**（改为直接 slug 链接） |
| `src/data/blog-posts.json` | halloween-pod-ideas-2026 · is-gearlaunch-legit · is-kittl-legit · is-society6-legit · is-spocket-legit 等 | related + blocks 内 **插入 `/best/*` 内链** |

**含义**: 线上站点内容**落后于 src/** —— 这 17 处内链改动从未 build/push（402 停摆期遗留）。
**影响**: 不是损坏（JSON 合法、`validate_content_data.py` 全过），但内链收益未上线。
**处置**: 交 **daily-content** 任务在下次 build+push 时一并带上（本任务 `can_deploy:false`，不越权）。已确认 `out/` 与 `.next/` 均 gitignore，重建不会污染工作树。

---

## ✅ 验证证据 (本轮，替代 build)

| 验证 | 命令 | 结果 |
|---|---|---|
| 项目自带验证器 | `python scripts/validate_content_data.py` | `[OK] 全部通过` exit=0 |
| 产物与作用域 | `.hermes/tmp/verify-run-0918.py` | **7/7 PASS** |
| 构建非干涉性 + 语法 | `.hermes/tmp/verify-buildscope-0918.py` | **5/5 PASS** |
| 脚本编译 | `py_compile` × 15 | 全部 clean |

**关于 `npm run build`**: 本任务硬约束明令 严禁自动 build/push（`can_deploy:false`），且**本轮 0 个站点文件被改动**——已用程序证明 **54 个构建输入无一引用 `.hermes/`**，即 build 读不到本轮所写任何文件，跑了也无验证价值。故改以项目真实数据关卡 + 作用域证明替代。

---

## ✅ 完成标准核对

- [x] `.hermes/affiliate-programs.json` 已更新 (`last_updated` = 9/18 12:1x; 新增 8 键; 键数 63→71, **0 键丢失**; 另改 `monitoring.last_live_check`)
- [x] `AFFILIATE_LOG.md` 今日 entry 落盘 (**append-only, 0 删除行**)
- [x] 本文件 `.hermes/logs/2026-09-18-affiliate-monitor.md` 落盘, §2.1 按 P0/P1/P2 排序
- [x] CF freebie 清单落盘 (`.hermes/logs/cf-freebies/2026-09-18.md`, 22 期 / 73 🎃 / 59 🎄)
- [x] 升级消息按 P0/P1/P2 分类, 5 要素全
- [x] 新获批商户部署流程: **无新获批** → P0 部署缺口 = 0
- [x] **无 push / 无 build / 无自动登录 / 无自动回信 / 未动任何凭证文件**
- [x] 补记 9/14-9/17 巡检空缺 (4 天 cron 失败, 无产物)

**升级请求 (3 条, 按离钱远近排序)**

1. **[P0] 402 根治** — 二选一: 充值 DeepSeek (≥100 CNY) 或 允许接线 MINIMAX fallback (`config.yaml` L512 取消注释, K3 可代改)
2. **[P0] Printful W-8BEN 重传** — 第 29 天, 3 分钟上传签字件, 是联盟破零的唯一税务闸门
3. **[P1] Placeit 催办邮件** — 草稿就绪 `.hermes/drafts/placeit-followup-email.md`, 待 user 手动发送
