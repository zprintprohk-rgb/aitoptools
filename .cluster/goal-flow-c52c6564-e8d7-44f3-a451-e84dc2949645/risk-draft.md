# 风险与异常处理记录（草稿，待全部 subagent 回传后定稿）

> 终稿 = 03-risk-log.md。每条含：编号 / 类型（阻塞|歧义|矛盾|异常）/ 描述 / 证据 / 处置建议 / 回滚或调整方式 / 状态。

## 已确认项（主线核实）

- **R-01 异常·cron 归属与可见性**：cron 调度器共有 26 个任务（sqlite），但 aitoptools 的 14 个任务全部注册在 agentId=main 下，按 agentId=aitoptools 过滤返回 0。8/14 丢失事件后的重建任务实际存在（13 enabled + 1 disabled），**未复发丢失**；但「cron list 按当前 agent 过滤=0」易被误判为再次丢失。
  - 证据：C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json（26 条，main=14）
  - 处置建议：核查 cron 时用 `cron status` 总数 + jobs.json 全量清单，不要只信 agent 过滤的 list；AGENTS.md「定时任务统一管理铁律」的查重步骤应改为读 jobs.json。
  - 回滚/调整：无需回滚；若后续 cron 再丢失，按 STRATEGY-0814 §5 + jobs.json.bak 双源重建。

- **R-02 异常·重复 cron 任务**：`W3-0825 万圣节全量push` 存在两条（98ebd150… 与 d9aacbed…），同为 8/25 07:15 一次性任务，deleteAfterRun=true。
  - 证据：jobs.json main 名下两条同名同调度任务
  - 处置建议：保留一条，删除另一条（删前确认两条 payload 一致；属一次性 at 任务，8/25 07:15 前处理即可，8/16 合并 push 日顺手处理）。
  - 回滚/调整：删除即不可恢复（deleteAfterRun 且无备份）→ 删前先复制 payload 到 STRATEGY 存档（遵守 cron 备份纪律 #7）。

- **R-03 异常·workbench 缺 expert-playbook.md**：集群模式约定 .cluster/expert-playbook.md 存在，实际不存在（.cluster/ 下为平铺业务文件）。
  - 处置：按集群模式通用规则执行（已执行），不阻塞；在交接文档中提示后续补齐。

## 执行准备员回传（subagent_04，待交叉核验员确认后定稿）

- **R-04 歧义·S1 扩写队列规模**：PHASE/STRATEGY 声明「B 级扩写 Top 20 队列已建，8/16 启动（S1）」；实际 content-expansion-queue.md 实载 7 项且均已扩写完成 → 8/16 幂等应判 NOOP。Top 20 队列是否存在另处（.cluster/content-expansion-queue.md vs 其他文件）待交叉核验员裁决。
  - 处置建议：若确认队列仅 7 项，8/16 S1 任务=「复核 7 项产物 + 从 B 级 138 页中按记分卡补建 Top 20 新队列」，需千问/用户补充队列源或授权按 programmatic-audit 排序重建。
- **R-05 矛盾·外链 8/16 预期 vs 实测**：PHASE/STRATEGY 排 8/16「S3 外链首批 8 站（免费可投优先）」；8/14 实测 0/8 成功（6 站 CAPTCHA/登录墙、2 站需回链拍板）。8/16 实际可执行=重试免费 API 入口（AI Toolz Dir 已逆向）+ 2 站回链待 K3 拍板。
  - 处置建议：8/16 外链任务降级为「重试+拍板请求」，产出外链台账；「首批 8 站落地」里程碑日期相应顺延并记录。
- **R-06 阻塞·辐条①素材缺口**：8/17 发布需 Kittl 设计文件 + 截图（public/tool-screenshots/blog/ 目录不存在）+ slug 未定义；printful_session_cookie 缺失只挡下单不挡内容发布。
  - 处置建议：8/16 夜间窗口可完成 Kittl 设计（低谷窗口）+ 截图；slug 由执行层按 blog-posts.json 惯例命名；8/17 发布不依赖 D6。
- **R-07 观察项·快修**：T1 实际待办仅 copy-ai-review（title 66>65、meta 146 偏短）；descript 已修、kittl-vs-canva 词序已对齐、printful alternatives 哨兵 8/15 76.7 +0.4 稳定。
  - 处置：8/16 快修范围收窄为 copy-ai-review 一项 + 附带观察 copy/descript 字数 102-121 词（是否扩写由记分卡 B 级队列决定）。

## 待 subagent 01/02/03 回传后补充
- RESULT 三日齐全性 / NORTH-STAR-DATA / BOARD D 清单 / Boost 4/25 / 哨兵 kittl 数值 / Halloween 链
- generate-sitemap.py 根因 + 修复验证（342 断言）
- 记分卡口径冲突裁决（A=180/138/14 vs A13→15/B39→51/C65→51）、kittl 67.0 vs 63.0、W-8 工作日、push 次数、Printify 门槛
