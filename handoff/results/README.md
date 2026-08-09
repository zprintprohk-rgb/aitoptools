# results/ 回写规范（AutoClaw 读）

- 命名：`RESULT-YYYY-MM-DD.md`，一天一文件；同一天多个 cron **追加段落**，不覆写。
- 每段结构（见 PROTOCOL.md §3）：META（cron 名 + 已执行策略 id）→ PER-TASK（id/结果/关键数据/文件变更）→ BLOCKERS（归属：自解 / 交千问登记 BOARD）→ NORTH-STAR-DATA（当日可得：展示/点击/CTR/联盟状态变化；无则 NODATA）。
- 只写事实与数据，不写策略建议（策略是千问的职责）。
- 旧格式日志（`.hermes/logs/daily-*.md`）继续保留，本目录是闭环交接的**摘要层**，不替代原日志。
