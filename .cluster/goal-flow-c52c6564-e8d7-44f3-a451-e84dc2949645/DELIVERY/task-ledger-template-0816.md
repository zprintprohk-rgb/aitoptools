# 8/16 执行台账模板（字段化 · 团队可直接执行）

> 生成：2026-08-16 05:10 · 用途：07:15 主任务（84c86e36）执行后逐项验收；也可作为后续每日执行模板
> 依据：STRATEGY-2026-08-16.md T0-T8 + AGENTS.md 铁律
> 约定：✅ 完成 / ⏳ 进行中 / ⚠️ 偏差（附说明）/ ❌ 失败（附原因与处置）

## 1. 任务台账（负责人 = AutoClaw 执行 cron；监督 = K3/千问；验收 = 唐总）

| 任务 | 验收标准（可检查） | 检查命令/方式 | 负责人 | 检查频率 | 异常处理 | 状态 |
|---|---|---|---|---|---|---|
| T0 同步+核对 | origin/main 到最新；AGENTS.md diff 仅 Hermes-Evolution 块 | `git log -1 origin/main` + `git diff AGENTS.md` | cron | 一次性 | diff 含业务改动→暂停核对 | ☐ |
| T1 copy-ai-review 快修 | title≤65 且含主词、meta≥150、dateModified=2026-08-16 | `python scripts/scorecard 或 grep reviews.json copy-ai-review` | cron | 一次性 | 不达标→顺延不带病上线 | ☐ |
| T2 sitemap 脚本替换 | merged 版替换生产脚本；单测 27/27；实跑 public/out 343/343/0+标记+robots 无损 | `python sitemap_fix_test_v2.py` + `python scripts/generate-sitemap.py` | cron | 一次性 | 单测<27→回滚脚本（git restore） | ☐ |
| T3 辐条①补正 | publishedAt/wordCount/status 非空；public/tool-screenshots/blog/ 存在≥3 图；content 引用截图 | `python -c 读 blog-posts.json` + `ls public/tool-screenshots/blog/` | cron | 一次性 | 截图缺失→记缺口明日补 | ☐ |
| T3b 全 11 篇补字段 | 11 篇 publishedAt 非 null、status=published | python 读 blog-posts.json 统计 | cron | 一次性 | 个别无记录→统一 2026-08-10 | ☐ |
| T4 外链提交 | link-building-0816.md 台账更新（每站 SUBMITTED/BLOCKED_*） | `cat .hermes/logs/link-building-0816.md` | cron（user 授权 D9） | 一次性 | CAPTCHA→BLOCKED 记录；dofollow→PENDING_K3_APPROVAL | ☐ |
| T5 排期治理 | 4f19a24a disabled；98ebd150 保留；02fee02d 重建 TODO 入 RESULT；外部实例调查记录 | 读 jobs.json + RESULT 段 | cron | 一次性 | 误禁→恢复 enabled | ☐ |
| T6 根目录卫生 | .gitignore 含 5 Hermes 文件 + GSC数据/ | `grep -E "HEARTBEAT|IDENTITY|SOUL|TOOLS|USER|GSC" .gitignore` | cron | 一次性 | 漏项→补后重跑 | ☐ |
| T7 合并 1 push | build PASS；push-count=1；线上 CSS hash=本地；IndexNow 200 | build 日志 + `git log origin/main --oneline -3` + curl 线上 css hash | cron | 一次性 | build FAIL→修复后当日再 push（仍 1 次） | ☐ |
| T8 RESULT 必写 | RESULT-2026-08-16.md 存在且含 NORTH-STAR-DATA | `ls handoff/results/RESULT-2026-08-16.md` | cron | 每日 | 缺失→补写 | ☐ |

## 2. 核验哨兵（自动，今日已创建）

| 哨兵 | cron id | 触发 | 检查内容 | 产出 | 异常路径 |
|---|---|---|---|---|---|
| 07:20 主任务触发核验 | 08726208 | 07:20 | 84c86e36 state / RESULT-0816 / 今日日志 | probe-0720.md | NOT_RUN→置顶告警+建议重建（本次不重建防双触发） |
| 12:30 午间复核 | d5a45047 | 12:30 | 触发状态 / push 次数=1 / 402 扫描 / RESULT / 外链台账 | probe-1230.md | 任一偏差→告警并记录 |

## 3. 关键状态基线（07:15 执行前实测）

| 项 | 基线值 | 验证时间 |
|---|---|---|
| 生产 sitemap | 343 条 / 唯一 343 / 0 重复 / 无标记（待 T2 治愈） | 05:00 |
| 生产 generate-sitemap.py | 5150 B 旧版（待 T2 替换为 merged 10738 B） | 05:00 |
| 84c86e36 cron | enabled=True / at 07:15 / timeout 1800 / deleteAfterRun | 05:01 |
| 单测 | 27/27 PASS（基线 343，含 541 复现自愈） | 05:09 |
| 外链 | 0/20（首批 8 站 0 提交 + 批2 12 站 0/12，今日 T4 破冰） | 05:00 |
| 402 模型余额 | 第 1 天告警（53646f7f/6db4582b 曾 402；今日日志无新 402） | 05:07 |

## 4. 回滚与复核方式

| 场景 | 回滚/处置 |
|---|---|
| T2 脚本替换后异常 | `git restore scripts/generate-sitemap.py`（当前零改动基线） |
| T7 push 后线上异常 | 死链/404 紧急可单独 push 修复；内容问题 git revert 对应 commit |
| 双触发风险 | 07:20 核验只读不重建；确需重建由主线人工执行（cron add 后 jobs.json 验证落库） |
| 402 复发 | 8/17 仍 402 → 升级 user 二选一（充值 DeepSeek / 接 MINIMAX fallback），勿卡 8/19 GEO |
| cron 视图背离（R-14） | 一律以 jobs.json 为准；变更后用探针自检 |

## 5. 下一步动作（负责人/时限）

| 动作 | 负责人 | 时限 | 验收 |
|---|---|---|---|
| 07:15 主任务触发 | cron 84c86e36 | 07:15 | probe-0720.md |
| D6 cookie / D7 token / D5 数据 / 3 行动卡 | 唐总 | 8/18 / 8/19 / 随时 | action-cards-0816.md 各项 |
| 午间复核 | cron d5a45047 | 12:30 | probe-1230.md |
| 8/17 402 复检 | 执行层 | 8/17 | 按余额规则升级 |
| 9/13 前重建 T30 校准 cron | 执行层 | 9/13 前 | jobs.json 含任务 |
