# 千问 × AutoClaw 交接闭环协议（PROTOCOL v1 · 2026-08-09 千问拟定）

> 目的：策略层与执行层通过项目内文件自动交接，**user 不做复制粘贴中转**，只拍板 BOARD.md 事项、只看结果。

## 0. 角色分工

| 角色 | 是谁 | 职责 |
|---|---|---|
| 策略大脑 | 千问 3.8-Max（千问办公助理） | 读执行结果 → 对齐北极星分析 → 写下一阶段策略与可执行任务 → 维护 BOARD |
| 执行层 | AutoClaw（4 个合并 cron） | 每次开跑读最新策略 → 执行当日 TASKS → 结束时回写结果 |
| 用户 | 老板 | 只拍板 BOARD.md 事项；看周报与里程碑读数 |

## 1. 目录约定（全部在 `F:\aitoptools\handoff\`）

| 路径 | 写方 | 读方 | 命名 |
|---|---|---|---|
| `strategy/` | 千问 | AutoClaw | `STRATEGY-YYYY-MM-DD.md`，AutoClaw 只认日期最新一份 |
| `results/` | AutoClaw | 千问 | `RESULT-YYYY-MM-DD.md`，一天一文件，多个 cron 追加各自段落 |
| `BOARD.md` | 千问 | 用户 | 拍板事项清单（唯一需要用户看的地方） |
| `PROTOCOL.md` | 千问拟 | 双方 | 本协议；变更须 user 拍板 |

## 2. 策略文件模板（千问写）

```
# STRATEGY-YYYY-MM-DD
META: 日期 / 作者=千问3.8-Max / 依据结果文件列表 / 北极星现状(展示·点击·CTR·佣金)
CONTEXT: ≤10 条关键结论（诚实版，含缺口）
TASKS: 表格，列 = id / 日期 / 动作 / 产出要求(写哪个结果文件或改哪个文件) / 当前动作支撑赚钱目标 / 幂等键
DECISIONS: 需 user 拍板项 → 同步登记 BOARD.md
NOTES: 铁律提醒（攒批1push/天、低谷窗口、不自动登录/发信/付款、事实核实、sitemap即推）
```

## 3. 结果文件模板（AutoClaw 写）

```
# RESULT-YYYY-MM-DD
META: 日期 / 已执行策略=STRATEGY-xxxx / 各cron状态
PER-TASK: id / 结果(DONE|NOOP|SKIP|BLOCKED) / 关键数据 / 文件变更
BLOCKERS: 阻塞项 + 归属（AutoClaw 可自行解决 / 需 user 拍板→交千问登记 BOARD）
NORTH-STAR-DATA: 当日可得数据（展示/点击/CTR/联盟状态变化），无则写 NODATA
```

## 4. 节奏

- **千问**：每日 07:23（cron「每日策略复盘」）读昨日 RESULT + `.hermes/logs/` 当日日志 → 写当日 STRATEGY → 更新 BOARD → 有拍板项才打扰 user，无则静默。
- **AutoClaw**：现有 4 个 cron（每日联盟运营 12:17 / 每日搜索增长 19:23 / 每周复盘 周日 07:47 / 季节集群执行）开跑第一步读 `handoff/strategy/` 最新文件，执行当日 TASKS；跑完追加 RESULT。
- **每周复盘**结果是千问周一策略升级（两周滚动计划）的主输入。

## 5. 兜底与幂等

- 当日无新 STRATEGY → AutoClaw 按最近一份 STRATEGY + 原职责执行（不空转）。
- 当日无 RESULT → 千问先查 `.hermes/logs/` 是否真跑了（日志在而 RESULT 缺 = 提醒 AutoClaw 补写；日志也无 = 执行缺口，升级 user）。
- TASK 幂等：执行前查产出文件/日志，已存在即记 NOOP，不重复劳动。
- **闭环不改变任何现有铁律**：不自动登录、不自动发信、不自动付款、敏感操作交 user；攒批 1 push/天；低谷窗口调度。

## 6. 生效条件

user 拍板本协议 → 千问把「交接闭环铁律」写入 AGENTS.md（AutoClaw 进场必读，自动遵守）+ 建千问侧「每日策略复盘」cron。AutoClaw 无需改 cron 配置，读 AGENTS.md 即接入。
