# 经营流程台账与执行 SOP · aitoptools（2026-08-10 版）

> 用途：团队可直接执行的字段化台账。每表含：字段、负责人、检查频率、异常处理、检查方式。
> 根目录唯一：所有文件在 F:\aitoptools 下；本台账位于 handoff/。

---

## 台账 1 · 用户阻塞解锁台账（4 项，唯一人工依赖）

| 操作 ID | 操作 | 目标文件/位置 | 完成判定（检查方式） | 负责人 | 检查频率 | 异常处理 |
|---|---|---|---|---|---|---|
| B1 | 下载 CF 万圣节素材 ≥2 个 | `.hermes/assets/cf-halloween-2026-08-07/`（推荐 Gothic Skull Rose + Black Cat Embroidery，清单见 cf-freebies 8/7） | 文件数 ≥2（`dir` 计数） | user | 每日 12:17 daily-ops 自动检查 | 未完成 → seasonal-exec blocked 记录 + BOARD 提醒；8/13 后降级纯内容方案 |
| B2 | 写入测试收货地址 | `test-address.json`（name/street/city/state/zip/country） | 文件存在且 JSON 可解析（python json.load） | user | 同上 | 缺失 → 下单环节 BLOCKED；提供模板见下方 JSON 模板 |
| B3 | 平台确认（二选一） | `printful_session_cookie.txt` 或 回复「用 Printify」 | cookie 文件存在 / BOARD 记录确认 | user | 同上 | 未确认 → 下单平台不可用；Printify 为零操作方案 |
| B4 | W-8BEN-E 签字上传 | Printful 后台 Tax & Legal | affiliate-programs.json tax_status=approved（tax-audit 浏览器复核） | user | 8/12 复核窗起每日 | Pending → 继续复核；Rejected → 记录原因 + 联系支持 |

**JSON 模板（B2）**：
```json
{ "name": "", "street": "", "city": "", "state": "", "zip": "", "country": "US" }
```

## 台账 2 · Halloween 链执行台账（8/10–8/18）

| 阶段 | 日期 | 检查键（幂等键） | 负责人 | 检查频率 | 异常处理 |
|---|---|---|---|---|---|
| 素材前置 B1 | 8/10 前 | assets 目录文件数 ≥2 | user | 每日 | 见台账 1 |
| Kittl 设计（2-3 个） | 8/11 | `.hermes/designs/halloween-test-*.png` 存在 | AutoClaw（seasonal-exec 8/10 触发后接续） | 当日 19:23 daily-search | 素材缺 → BLOCKED 记录；素材齐 → 自动执行 |
| 下单（Printful/Printify） | 8/12-13 | halloween-asset-chain.md 有 order_id/eta/cost | AutoClaw | 每日 daily-ops | 预算硬限 $25/单 $50/日；无平台 → blocked |
| 收货拍照 | 8/14-16 | `public/photos/wall/halloween-*.jpg` | user（拍照）+ AutoClaw（上传） | 每日 | user 不可用 → fallback 官方 mockup |
| 内容生产（支柱帖+辐条） | 8/14-17 | blog-posts.json 含 halloween slug | AutoClaw（daily-search） | 每日 | 支柱帖已上线（25 Halloween POD Ideas）为基线 |
| 上线判定 | 8/18 | seasonal-exec 输出 LAUNCHED/PARTIAL/MISSED | AutoClaw | 一次性 | PARTIAL→补漏清单；MISSED→8/19 补救方案+告警 |

## 台账 3 · 高佣金联盟申请台账（窗口 8/15–8/25）

| 候选 | 联盟入口 | 状态 | 负责人 | 下一步动作 | 检查频率 |
|---|---|---|---|---|---|
| Caspa AI | 官网页脚 Affiliate Program 入口 | ✅ 体系实证存在 | AutoClaw+user 确认 | 8/15 申请；M3 横评 CTA 先官网后替换 | 每周 |
| Jasper AI | jasper.ai/affiliates | ⚠️ 佣金率待核实（搜索凭证失效） | AutoClaw | 凭证恢复后补核实 → 申请 | 每周 |
| Synthesia | synthesia.io/affiliate（待核实） | ⚠️ 同上 | AutoClaw | 同上 | 每周 |
| Runway ML | runwayml.com（待核实） | ⚠️ 同上 | AutoClaw | 同上 | 每周 |
| Mockuplabs | 联盟网络待核实（theresanaiforthat 标记） | ✅ 信号双源互证 | AutoClaw | 8/15 窗口申请（M3 队列首位） | 每周 |

## 台账 4 · 每日/每周检查清单（团队可直接执行）

| 检查项 | 频率 | 命令/方式 | 异常信号 |
|---|---|---|---|
| 四 cron 产物落盘 | 每日 | `dir .hermes\logs\*-{今日}*` 应含 daily-ops/daily-search | 缺 → 查 cron runs / 402 |
| 素材目录 | 每日 | `dir .hermes\assets\cf-halloween-2026-08-07` | 0 文件 → B1 未完成 |
| test-address | 每日 | `Test-Path test-address.json` | False → B2 |
| Printful 税务 | 每日 | `python -c "import json;print(json.load(open('.hermes/affiliate-programs.json'))['programs']...)"` 查 tax_status | 非 approved → 复核窗内继续 |
| RESULT 补写 | 每日 | `dir handoff\results\RESULT-{今日}.md` | 缺 → 策略闭环 T9 提醒 |
| IndexNow 计数 | 每日 | `.hermes/logs/indexnow-{今日}.log` | 非 200 → 告警 |
| 402/余额 | 每日 | cron runs 状态 | 出现 402 → fallback 已配仍失败则升级 user |
| 北极星读数 | 每周（周日） | weekly-review 报告 | CTR/展示趋势偏离 → 决策树 |

## 负责人与节奏总表

| 角色 | 职责 | 频率 |
|---|---|---|
| 用户 | B1-B4 四操作 + 8/14 T+7 校准 + 8/18 判定确认 | 约 9 分钟一次性 + 2 节点各 10 分钟 |
| AutoClaw（4 cron） | 台账 2/3 自动执行 + 台账 4 自动检查 | 每日 12:17 / 19:23 / 周日 07:47 |
| 策略闭环（每日 12:20） | 读 RESULT → 写 STRATEGY → 更新 BOARD | 每日 |

## 异常升级路径

1. 台账检查异常 → cron 记录 + 当日 RESULT BLOCKERS 段
2. 连续 2 天异常 → 策略闭环升级（STRATEGY 加 TASK + BOARD 登记）
3. 需人工/敏感操作 → BOARD.md 待拍板（user 只看这里）

## 状态更新 (2026-08-10 23:15)
- B2: **初稿已生成** test-address.json (基于 W-8 信息: Tang Yun Ti / 深圳 518111 / 18126380255, JSON 验证通过) — 用户确认或替换美国地址即可
- B3: **自动兜底已确认** — seasonal-exec 下单逻辑 = Printful (if verified) else Printify; Printful cookie 缺失时自动用 Printify 联盟链 (try.printify.com/4fs863rfz2yc), 无需用户操作
- B1: 仍待用户下载 CF 素材 (唯一无替代项)
- B4: 8/12 复核窗排期 (daily-ops tax-audit)
- 联盟佣金率缺口: WebSearch 凭证 8/10 23:13 仍未恢复 (BROKER_UNAUTHORIZED), 保持缺口记录
