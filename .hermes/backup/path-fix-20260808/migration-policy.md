# Migration Policy — AutoClaw 接管 aitoptools 调度 (v3, 2026-08-08)

> 依据: 2026-08-08 用户策略 (北极星: 6 个月 $3000 CPA/CPS 佣金, 目标 2027-01-15)
> 状态: **coexistence**（并存期）→ 8/12 确认后切换 **autoclaw_primary**

## 一、迁移阶段

| 阶段 | 时间 | 状态 | 说明 |
|---|---|---|---|
| 1 解锁 | 8/8 | 进行中 | 等 user 补录 secrets（见 §三） |
| 2 首跑验证 | 8/9-8/11 | 待触发 | weekly-report 首跑 + halloween 执行 + Printify 回信检查 |
| 3 切换主导权 | 8/12 起 | 待确认 | 连续 3 天正常 → user 停用 Hermes aitoptools cron |
| 4 数据驱动 | 8/14 起 | 待触发 | T+7 首读数 → 选题权重全面切 GSC 数据 |

## 二、并存期规则（每个 AutoClaw cron 必须遵守）

1. **首步幂等**: 检查当日产物文件是否已存在
2. **标记约定**:
   - Hermes 已执行 → 输出 `SKIPPED_HERMES_ALREADY_DONE` 并退出
   - AutoClaw 执行 → 产物标注 `AUTOCLAW_PRIMARY`
3. 8/12 后: 移除 SKIPPED 逻辑, AutoClaw 为唯一执行者（由主会话统一更新 cron prompts）

## 三、Secrets 状态表（解锁清单, 用户补录）

| # | secrets | 路径 | 状态 | 解锁效果 |
|---|---|---|---|---|
| 1 | Printful session cookie | .hermes/secrets/printful_session_cookie.txt | 🔴 缺失 | verify-watcher 自动重发 → 变现闭环 |
| 2 | Pinterest session | .hermes/secrets/pinterest_session.txt | 🔴 缺失 | pin 发布恢复 |
| 3 | Gmail App Password | .hermes/secrets/gmail_credentials.json | 🔴 失效 | affiliate-monitor IMAP 恢复（现用 .env 兜底） |
| 4 | GSC OAuth (强烈建议) | .hermes/secrets/gsc-oauth.json | 🔴 缺失 | 周报真实数据 + 选题引擎激活 |

校验: `python .hermes/scripts/validate_session_cookies.py`（格式+连通性, 输出脱敏, 证据 session-validation-{date}.md）
补录完成后用户回"已提交" → 主会话重跑校验 → 通过则全链路解锁

## 四、里程碑守护（AutoClaw 一次性 cron）

| 里程碑 | cron 时间 | 检查内容 | 输出 |
|---|---|---|---|
| 8/12 切换检查 | 20:17 | 8/9-8/11 产物完整度 + Hermes 执行记录 | 切换建议（停用 Hermes / 回退） |
| 8/14 T+7 读数 | 20:07 | GSC 展示 + IndexNow 计数 + 联盟点击 + is-magicdrop-legit 表现 | .hermes/reports/t7-reading-2026-08-14.md |
| 8/18 Halloween 上线 | 20:07 | 素材链 4 阶段完成度 + 支柱帖 + 照片墙 | 缺口清单 |

## 五、GSC 数据管道优先级（gsc-mining-daily 使用）

1. GSC API (gsc-oauth.json 有效) — 实时完整
2. 本地 gsc_data.csv (最近 7 天) — 降级兜底
3. keywords-200.csv (静态) — 最后兜底

OAuth 就绪后首跑: 拉最近 28 天 → retroactive mining → CONTENT_PLAN.md 追加并标注 `DATA_BACKFILL_28D`

## 六、回退预案

- AutoClaw 连续 2 天失败 → 回退 Hermes 执行 + 告警 user
- Hermes 停用后 AutoClaw 故障 → 优先修复 AutoClaw, 不重启 Hermes（除非修复超 48h）

## 七、北极星对齐

- 周报四块模板含联盟状态 → 每周期检查 $ 进度
- 8/21 目标: print price ai tool 排名 ≤30（Boost Queue 动作持续注入）
- 每月 1 日: 北极星复盘（累计佣金 vs $3000/6 月曲线）
