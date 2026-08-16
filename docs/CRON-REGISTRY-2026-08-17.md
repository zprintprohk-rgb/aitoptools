# Aitoptools 定时任务注册表（CRON REGISTRY）

> 更新：2026-08-17 04:05 CST · 数据来源：AutoClaw 定时面板实查 + 产物文件核读
> 项目：F:\\aitoptools（aitoptools.net — Print AI Tools 联盟站）· 关联路线图：handoff/strategy/PHASE-2026-08-13-09-13.md

## 一、总览（10 个任务）

| # | 任务名 | 调度 | 类型 | 职责一句话 | 状态 |
|---|---|---|---|---|---|
| 1 | 每日联盟运营 | 每天 12:17 | 每日 | 联盟邮件监控 + Printful 税审 + AI 爬虫监控 + 排名哨兵 | ✅ 运行中 |
| 2 | 每日搜索增长 | 每天 19:23 | 每日 | GSC 选题 + 工具雷达 + 内容生产/Boost + GEO 检查 + 当日 push | ✅ 运行中 |
| 3 | 每周复盘 | 每周日 07:47 | 每周 | 数据质量门 + 五块周报 + 里程碑检查 + 北极星复盘 + push 纪律核对 | ✅ 运行中 |
| 4 | W1-0816 B类快修push | 8/16 07:15（一次性） | 节点 | 25 页 title/meta 修正 + 扩写 + kittl 重写 + 外链首批 | ✅ 实质完成（8/14 提前） |
| 5 | W2-0817 Boost56 | 8/17 08:41（一次性） | 节点 | Boost #5-6 + 辐条① + geo-technical | ✅ 实质完成（8/14 提前），今日幂等 |
| 6 | W2-0819 GEO首读数 | 8/19 07:15（一次性） | 节点 | beacon 7 天读数 + GSC 对比 + AI 引用状态 + GEO 决策 | 🔄 补跑中 |
| 7 | W2-0823 集群合并push | 8/23 07:15（一次性） | 节点 | 集群页 + 内链第二轮 200+ + E-E-A-T + 外链第 2 批 | ✅ 提前完成（8/15） |
| 8 | W3-0825 万圣节全量push | 8/25 07:15（一次性） | 节点 | 万圣节集群全量 + Kittl 联动 + GEO 词覆盖 | 🔄 补跑中 |
| 9 | W3-0831 IndexNow全推 | 8/31 07:15（一次性） | 节点 | IndexNow 增量全推 + sitemap 核验 + 月末收口 | ✅ 提前完成（8/15） |
| 10 | W4-0913 T30全量校准 | 9/13 07:15（一次性） | 节点 | 三源汇总 + K3 KPI 六项核验 + 决策树 + Phase 3 产出 | 🔄 补跑中 |

## 二、每日任务详情（3 个，长期运行）

### 1. 每日联盟运营（ID cf28f53d）
- **调度**：每天 12:17（Asia/Shanghai）· 单次最长 25 分钟
- **作用**：联盟变现侧的每日看护，产出当日联盟状态快照
- **步骤**：
  - Step 0：消费 PHASE 路线图，确认当日节点
  - Step 0b：**排名哨兵**——20 个核心 query 逐日排名（GSC API + SOCKS5 代理），变动 ≥5 位告警
  - Step 1：IMAP 拉邮件（gmail，SOCKS5 代理）→ 解析审批/商户邮件/CF free picks → 更新台账
  - Step 2b：**tax-audit**——Printful W-8BEN-E 审核状态跟踪（浏览器后台，Approved → payout_ready）
  - Step 3：AI 爬虫监控（beacon 数据源，无 token 则 GEO_BLIND NODATA）
- **产物**：.hermes/logs/daily-ops-{日期}.md（P0/P1/P2 表 + user 动作 ≤3 + PUSH_READY 标记）
- **推送联动**：不直接 push；哨兵 ALERT/修复 → 产物标 PUSH_READY，由每日搜索增长当日消费 push

### 2. 每日搜索增长（ID 78e5671a）
- **调度**：每天 19:23 · 单次最长 30 分钟
- **作用**：流量侧的每日增长引擎 + 当日部署执行者
- **步骤**：
  - Step 0：消费 STRATEGY 文件当日 TASKS（幂等）
  - Step 1：IndexNow 增量推送 + GSC mining（展示≥10 且 CTR<0.05 无专页 → 内容队列）
  - Step 2：discovery-radar 工具雷达（周一/三/五，10 源扫描）
  - Step 3：content-production 内容生产（GEO 规则：BLUF/数据锚点/FAQ/引用链/author schema）
  - Step 4：geo-technical（周一：robots/llms.txt/schema/引用抽查）
  - **Push 纪律（8/15 拍板）**：每日 ≤5 次 push；重点内容当日 build 验证后即 push；消费 PUSH_READY
- **产物**：.hermes/logs/daily-search-{日期}.md（含 push-count）

### 3. 每周复盘（ID c3a11910）
- **调度**：每周日 07:47 · 单次最长 30 分钟
- **作用**：周度数据质量门 + 决策复盘 + 里程碑检查
- **步骤**：
  - Step 0：data-quality-gate（日志缺口 >2 天告警）
  - Step 0b：**push 纪律核对**（git log 统计每日 push 次数，>5 告警）
  - Step 1：五块周报（GSC top queries / CTR 榜 / 联盟状态 / 待执行项 / GEO 状态）
  - Step 2：milestone-check（8/18 万圣节 deadline / 8/21 print-price / T+14 Boost 验证）
  - Step 3：北极星复盘（每月 1 日，佣金 vs ,200/,000 曲线）
- **产物**：.hermes/reports/weekly-{日期}.md

## 三、一次性节点详情（7 个，deleteAfterRun）

### 4. W1-0816 B类快修push（ID de9fad65，8/16 07:15）
- **作用**：B 级页批量快修 + 内容扩写 + kittl 重写 + 外链首批
- **内容**：bfix-plan 高优先 25 页 title/meta（50-60/150-160 字符）+ 扩写 Top 10（≥1,200 词）+ kittl-review 重写（消费诊断）+ copy ai 快修 + C 级组 B 补充 + 外链首批 8 站 + 当日主 push
- **状态**：✅ 实质工作 8/14 提前完成（commit f4f5c64，记分卡 A13→15/B39→51/C65→51）；8/16 07:15 自动轮幂等 NOOP
- **产物**：.hermes/logs/bfix-0816.md / link-building-0816.md

### 5. W2-0817 Boost56（ID 6db4582b，8/17 08:41）
- **作用**：排名 Boost（T+7 Branch A：每天 Boost 1 页节奏）
- **内容**：Boost #5 midjourney-review（四杠杆：内容 1022→5754 字符/引用链 3/内链 6/FAQ 5）+ #6 jasper-ai-review（1220→5092）+ 辐条① Halloween + geo-technical（周一）
- **状态**：✅ 实质工作 8/14 提前完成（commit b7df3ab，autoLinkTools 11/11，build PASS）；今日 08:41 自动轮幂等 NOOP
- **产物**：.hermes/logs/boost-0817.md

### 6. W2-0819 GEO首读数（ID 53646f7f，8/19 07:15）
- **作用**：GEO 效果首读（决策：AI 引荐流量 >0 → 持续投入；=0 → 降维护级）
- **内容**：CF Web Analytics beacon 7 天读数（GPTBot/ClaudeBot/PerplexityBot UA）+ GSC query 对比基线 + 20 query AI 引擎引用状态（浏览器）+ 基线表更新
- **状态**：🔄 8/15 提前跑失败（zai 402 billing + deepseek 401 双 fallback 全挂）；8/17 04:04 补跑中；原排期 8/19 07:15 仍有效
- **产物**：.hermes/logs/geo-0819.md + handoff/results/RESULT-2026-08-19.md

### 7. W2-0823 集群合并push（ID 1727c0ce，8/23 07:15）
- **作用**：集群页 + 存量改造 + 内链第二轮 + E-E-A-T 合并 push
- **内容**：枢纽交叉链四层代码级落地（reviews 84/84 + compare 6/6 + best 203/203 = 6,792 内链，350 页 ≥2）+ 辐条补全 + A 类页改造 + E-E-A-T（author Person: Jerome Tang + 方法论声明）+ 外链第 2 批
- **状态**：✅ 8/15 提前完成（cluster-push-0823.md；当日 push-count=6，超 5 上限 1 次已如实记录，属计划节点例外）
- **产物**：.hermes/logs/cluster-push-0823.md

### 8. W3-0825 万圣节全量push（ID d9aacbed，8/25 07:15）
- **作用**：万圣节集群全量上线（9/1 前最后窗口）+ Kittl 联盟联动
- **内容**：Halloween 集群全部页面检查补全 + Kittl 系互链（UTM: halloween2026）+ GEO 三词覆盖（halloween shirt designs / print on demand / sublimation）+ 全量 build + push + IndexNow 即推
- **状态**：🔄 8/15 提前跑被 gateway restart 中断；8/17 04:04 补跑中；原排期 8/25 07:15 仍有效；内容 2/3 已上线（halloween-pod-ideas-2026 + printful-vs-printify-halloween-2026）
- **产物**：.hermes/logs/halloween-full-0825.md

### 9. W3-0831 IndexNow全推（ID 26a0ac2a，8/31 07:15）
- **作用**：IndexNow 增量全推 + sitemap 核验 + 月末 push 收口
- **内容**：增量对比推送 + 342 URL 全量核验 + 未推 commit 收口 + C2b 表更新
- **状态**：✅ 8/15 提前完成（indexnow-0831.md：342/342 URL 200，FULL-PUSH 200，verify-deploy PASS，ahead 1→0）
- **产物**：.hermes/logs/indexnow-0831.md

### 10. W4-0913 T30全量校准（ID 02fee02d，9/13 07:15）
- **作用**：T+30 全量校准出 Phase 3（K3 V2 修正目标）
- **内容**：三源汇总（GSC 30 天 + beacon 30 天 + 联盟后台）+ K3 KPI 六项核验（title/meta 100%、扩写 50%、内链 200+、20 query +5 位、展示 197→500+/UV 100-150、外链 ≥20）+ 决策树（≥ 提强度 / -400 重排 / < 战略复审）+ Phase 3 文档
- **状态**：🔄 8/15 提前跑失败（PowerShell 引号嵌套）；8/17 04:04 补跑中；原排期 9/13 07:15 仍有效
- **产物**：.hermes/logs/t30-0913.md + handoff/strategy/PHASE-2026-09-14-*.md

## 四、执行链路（依赖关系）

每日联盟运营(12:17) → PUSH_READY → 每日搜索增长(19:23) → 当日 push
每周复盘(周日) → 消费全部产物 → 周报
8/15 复核 → 8/16 快修 → 8/17 Boost → 8/19 GEO 决策 → 8/23 集群 → 8/25 万圣节 → 8/31 IndexNow → 9/13 T+30 → Phase 3

## 五、故障与恢复记录

| 日期 | 问题 | 根因 | 处置 |
|---|---|---|---|
| 8/15 | 复核/快修/Boost/GEO/集群/IndexNow/T30 首轮全超时 | timeoutSeconds=300（重任务 5 分钟不够）+ 10 并发模型排队 | 全部调至 1800s（面板可再调） |
| 8/15 | GEO 补跑失败 | zai 402（billing 欠费时点）+ deepseek 401（key c493 无效）双 fallback 全挂 | 8/17 zai 恢复后补跑；deepseek key 待 user 更新 |
| 8/15 | 万圣节补跑中断 | gateway restart | 8/17 补跑 |
| 8/15 | T30 补跑失败 | PowerShell 引号嵌套（内联 python） | 8/17 补跑 |
| 8/15 | 万圣节任务 ID 脱敏无法触发 | 系统 ID mask | 重建（d9aacbed，排期/内容一致） |

## 六、使用说明

- **查看执行结果**：AutoClaw 桌面端「定时」面板，每个任务有最近执行状态与耗时
- **调整频率/时限**：面板中进入任务设置修改（单次最长执行时间、调度表达式）
- **产物位置**：F:\\aitoptools\\.hermes\\logs\（每日/节点日志）、.hermes\\reports\（周报）、handoff\\results\（RESULT 序列）
- **幂等原则**：产物已存在且非空 → 任务 NOOP 不重复劳动（git log / 产物文件双查）
- **push 纪律**：每日 ≤5 次；重点内容当日部署；微小改动攒批
