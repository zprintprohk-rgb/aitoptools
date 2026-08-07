# Cron 迁移记录 — AutoClaw 取代 Hermes (aitoptools 范围) · 2026-08-08

> 结论: **可以取代**。Hermes 侧 cron 依赖 MiniMax Code app 进程（watchdog 每 5 分钟拉活，7/25-7/27 曾连续漏跑 3 天）；mavis CLI 已损坏（MODULE_NOT_FOUND）→ 侧调度黑盒不可管。AutoClaw cron 由常驻 gateway 调度，可读可改可审计，且产物幂等检查防双跑。

## 一、Hermes 侧 aitoptools cron 还原清单

| 任务 | 原时间 | 调度方 | 证据 |
|---|---|---|---|
| daily-content | 13:30 每日 | Hermes jobs.json (aitoptools-daily-content) | C:\Users\Administrator\.hermes\cron\jobs.json |
| affiliate-monitor | 12:05 每日 | mavis app 内 | .hermes/logs/2026-08-07-affiliate-monitor.md |
| discovery 雷达 (v4) | 一三五 19:00 | mavis app 内 | .hermes/logs/2026-08-07-radar.md "v4 cron 周一/三/五 19:00" |
| gsc-indexnow | 12:40 每日 | mavis app 内 | AFFILIATE_LOG.md C2b "gsc-indexnow cron (12:40)" |
| 联盟审批监控 | 9:12 每日 | mavis app 内 | AGENTS.md "cron 12 9 * * *" |
| weekly-report | 周日 (未注册) | — | gsc-mining-queue.md 提及 |
| pinterest 发布 | 8/8 09:00 一次性 | 全权指令 | browser-auto-2026-08-08.md (#3, 被 session 缺失阻塞) |

## 二、AutoClaw cron 全表（7 个, 2026-08-08 生效）

| 任务 | 时间 | 取代 | 合规 (低谷窗口 + 非整半点) |
|---|---|---|---|
| aitoptools-affiliate-monitor-daily | 每日 12:17 | 12:05 affiliate-monitor + 9:12 审批监控 (合并) | ✅ 午间窗口 12:05-13:30, :17 |
| aitoptools-gsc-mining-daily | 每日 13:07 | 12:40 gsc-indexnow (Step 0 并入) + 13:00 mining | ✅ 午间窗口, :07 |
| aitoptools-weekly-report-2026-08-09 | 8/9 07:47 | weekly-report (原 08:00 整点) | ✅ 夜间窗口 18:00-08:00, :47 |
| aitoptools-halloween-chain-2026-08-10 | 8/10 19:37 | 原 10:00 白天整点 → 晚间低谷 | ✅ 晚间窗口, :37 |
| aitoptools-printful-verify-watcher | 每时 :23 (8-22) | 原整点每小时 | ✅ 轻量检查, :23 |
| aitoptools-discovery-radar | 一三五 19:23 | 19:00 discovery (整点→非整点) | ✅ 晚间窗口, :23 |
| aitoptools-daily-content | 每日 19:47 | 13:30 Hermes daily-content (半点+边界) | ✅ 晚间窗口, :47 |

顺序依赖: discovery 19:23 → daily-content 19:47 (消费当日 radar 素材) ✅

## 三、并存期行为（防双跑设计）

- Hermes 侧 cron 仍在跑（MiniMax app 由 watchdog 保活, 8/8 00:20-00:35 实证存活）
- AutoClaw 每个 cron 首步 = 幂等检查（当天产物文件已存在 → ALREADY DONE 退出）
- 效果: Hermes 先跑 → AutoClaw 跳过; Hermes 停摆/漏跑 → AutoClaw 兜底执行。双保险, 不双写
- 完全接管: 在 MiniMax Code app 内停用 aitoptools-daily-content 后, AutoClaw 独立全量跑（用户可选操作, 不停用也无害）

## 四、不取代范围（跨项目, 保留 Hermes）

- zprintpro-daily-seo (10:15) / SEO 周报 2e7ff9ec5f15 (周一 9:00) — zprintpro 项目职责
- togthr-daily-dev (15:30) / togthr-deploy-verify (17:30) — togthr 项目职责
- daily-report-aggregate (18:30) — 三项目日报汇总, 依赖跨项目上下文, Hermes 侧保留

## 五、遗留风险

- mavis CLI 损坏导致 Hermes 侧 cron 无法远程管理 → 停用需在 MiniMax app 内手工
- gmail_credentials.json app_password 失效 → affiliate-monitor 依赖 .env IMAP_PASSWORD 兜底（已写入 prompt）
- GSC OAuth 未配置 → weekly-report / gsc-mining 的 GSC 块暂 blocked_missing_credentials, 数据驱动选题用本地数据
