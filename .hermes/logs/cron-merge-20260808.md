# Cron 合并 + 路径隔离记录 — 2026-08-08 (10→4)

> 依据: 用户 8/8 02:12 指令（路径锁定 + cron 合并 + GEO 嵌入）

## 一、路径审计结论（P0 澄清）

- **git repo 正确**: origin = git@github.com:zprintprohk-rgb/aitoptools.git，5 commit 全在 aitoptools 仓库
- **主副本完整**: 所有项目产物（reports/logs/audit/discovery）均在 F:\aitoptools 正确位置，md5 验证与 tmp 副本一致
- **实际污染面**: cron agent 的 write 工具将产物双写到 F:\zprintpro-nextjs\.openclaw\tmp（沙盒内允许），exec 主副本同时成功 → tmp 是冗余副本非唯一副本
- **已清理**: 23 个 aitoptools 文件移入 F:\aitoptools\.hermes\backup\path-fix-20260808\（工作痕迹保留），6 个 zprintpro 自身文件保留原位
- **根因防护**: 所有 cron prompt 头部强制"路径铁律"（PROJECT_ROOT=F:\aitoptools / cd /d 开头 / 禁读写 zprintpro / 写文件必须 exec）

## 二、Cron 10→4 合并（2026-08-08 02:15 生效）

| 新 cron | 时间 | 合并内容 | 备注 |
|---|---|---|---|
| aitoptools-daily-ops | 每日 12:17 | affiliate-monitor + printful-watcher(条件) + ai-crawler-monitor(GEO 新增) | 输出 daily-ops-{date}.md |
| aitoptools-daily-search | 每日 19:23 | gsc-mining+IndexNow + discovery(一三五) + content-production(GEO 规则) + geo-technical(周一) | 输出 daily-search-{date}.md |
| aitoptools-weekly-review | 周日 07:47 | weekly-report(5 块+GEO) + milestone-check(done_flag×4) + north-star(每月1日) | 输出 weekly-{date}.md |
| aitoptools-seasonal-exec | 8/10 + 8/18 19:37 | halloween 推进(8/10) + deadline 判定(8/18) + 自删 | 跟踪器 halloween-asset-chain.md |

旧 10 cron 全部删除（f313701c/914720a2/f43a7b76/28423876/f08752ad/57a765d4/5c776baa/9b93e1d9/ce4fee08/69cb2ffc）。

## 三、里程碑覆盖（weekly-review done_flag 机制）

| 里程碑 | 日期 | done_flag | 触发 |
|---|---|---|---|
| 迁移切换检查 | 8/12 | .hermes/logs/milestone-switch-done | 周日跑，今天≥8/12 且无 flag |
| T+7 首读数 | 8/14 | milestone-t7-done | 同上（8/16 周日首次覆盖） |
| Halloween deadline | 8/18 | milestone-halloween-done | seasonal-exec 8/18 主判定 + weekly 兜底 |
| print-price ≤30 | 8/21 | milestone-printprice-done | 同上 |

注意: 8/16（周日）weekly-review 首跑即覆盖 8/12/8/14 里程碑（done_flag 不存在 → 执行）。

## 四、GEO 嵌入清单

- daily-search Step 4 geo-technical（周一）: robots_txt_audit + llms_txt_check + schema_coverage + citation_spot_check
- daily-search Step 3 content-production: BLUF/数据锚点/列表优先/FAQ≥3/引用链/author schema
- daily-ops Step 3 ai-crawler-monitor: AI 爬虫 UA 统计, 连续 3 天 0 → 告警
- weekly-review 块 5: GEO 状态（AI 爬虫量/citation/schema 覆盖率）
- seasonal-exec: 内容模板 BLUF + 数据表格 + FAQ≥5 + FAQPage/HowTo/ItemList schema

## 五、攒批 push（Phase 3）

- 旧 commit: 75c4c88 / 18431a0(amend) / 0dffea9 / 38e2ba2 / f261049 / e88bf3f / b9aa1bd / 2ed579c / 860c90f（9 个，未 push）
- 本次新增: 路径隔离 + cron 合并记录
- 单次 push 触发 1 次 CF build

## 六、清理记录 (2026-08-08 03:25 user 指令)
- 删除 Hermes 侧 aitoptools-daily-content (13:30) — 职责已被 AutoClaw daily-search 完全覆盖, 合并后不需要
- jobs.json 6->5; 备份: .hermes/backup/hermes-jobs-20260808.json
- 保留: 2e7ff9ec5f15 (zprintpro) / zprintpro-daily-seo / togthr-daily-dev / togthr-deploy-verify / daily-report-aggregate (跨项目)
- AutoClaw 侧无残留: 仅 4 个合并 cron
