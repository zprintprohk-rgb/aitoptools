# T14 判定书 — 2026-08-21 (T+14 读数日)

> 任务: STRATEGY-2026-08-10 T+7 Branch A 排期 + STRATEGY-2026-08-19 T5 预案 + STRATEGY-2026-08-20 T2 判定树 | 数据窗口: 8/14-8/20 (7d, GSC API 实时拉取, rowLimit 1000)
> 数据文件: .hermes/tmp/t14-verdict-0821.json / t14-targeted-0821.json / t14-pages-0821.json / gsc-full-0821.json
> 口径: 主判定 = 哨兵/GSC 单查询窗口口径; GEO compare 仅作佐证

## 一、Boost #1/#2 T+14 判定

| 页 | 8/8 基线 | T+7 8/15 | 8/19 预拉 (8/12-18) | **8/21 读数 (8/14-20)** | Δ vs 8/8 | 判定 |
|---|---|---|---|---|---|---|
| #1 /stickermule-review/ | 35.1 | 36.0 | 38.93 | **35.00** @6 imp (页级 40 imp/51.98) | +0.1 | **Branch B** (持平偏改善; vs 8/19 窗口 +3.9 回稳) |
| #2 /runway-ml-review/ | 63.0 | 65.2 | NODATA | **NODATA** 裸词 0 imp (runway ml review 72 @1; 页级 31 imp/71.03) | 无法计算 | **悬置** (NODATA x3 窗口; 前序哨兵 69.09→63.5 曾 Δ-5.6) |

### #1 处置
- 主词 35.0 vs 基线 35.1 = 无显著移动 (C/B 边界), 采 Branch B: 保持四杠杆节奏 + 补外部信号 (Pinterest/社交)
- 8/22 严格 T+14 (8/15-8/21 窗口) 再读一次确认

### #2 处置
- 裸词 3 窗口 NODATA + 页级曝光 43→31 降 = 需排查, 不满足任一 Branch 数据要求 → 悬置
- 8/22 拉 8/15-8/21; 若仍 NODATA → GSC URL Inspection 重爬 + 检查 SSR/内链 + 外部信号 (Branch C 路径)

## 二、#3/#4 T+7 合并读 + print-price <=30 里程碑

| 页 | 8/8 基线 | 8/13 优化 | **8/21 (8/14-20)** | Δ | 目标 | 判定 |
|---|---|---|---|---|---|---|
| #3 /blog/is-magicdrop-legit/ | 64.6 | 8/13 FAQ5+引用链+内链4 | **12.93** @40 imp (页级 16.25 @59) | **-51.7** | <=20 | **达标 + Branch A** (哨兵 25.58→12.93 单窗口再降 12.7) |
| #4 /blog/print-price-ai-tools-2026/ | 69.5 | 8/13 对比表+内链+Schema | **62.75** @8 imp (页级 2 imp) | -6.75 | <=30 | **PARTIAL** (改善方向明确, 距目标 32.75 位) |

### #4 print-price 里程碑判定 → 启用预案方案 A
- 触发条件核对 (t14-check-0819.md 三): 读数 62.75 >= 55 (条件1) 且 >= 60 (条件3) 双命中 → **启用方案 A** (calculator 意图渐进式)
- 分歧记录: daily-ops 08-21 日志建议「维持现状」; 本判定按 K3 预案 (STRATEGY-2026-08-19 T5) 执行方案 A, 8/22 供 K3 复核
- 已执行 (本日部署): title/H1 -> Print Price Calculator 2026; 首段 calculator-first; Quick Verdict 钩子; FAQ +1 (free print price calculator); dateModified 8/21
- 风险控制: 8/28 T+7 复读 — 主词 print price ai tool 跌 >5 位或 calculator 系词无新展示 → 回滚 H1

## 三、20 词 AI 引用审计 (R1 修订后标准)
- 标准: AIO top-10 份额 <54%, pos 17-30 簇即候选; 出现 1-2 条引用即验证成功
- 状态: **NODATA** — GEO beacon 未就位 (D7 第 5 天, CF token 缺) + autoglm credits 耗尽, 无法直接审计 AI 输出
- 代理证据: is magicdrop legit 12.93 (进 top-20 引用候选区间), GEO 词量 323→478 (+48%) — 引用候选簇已形成, 直接验证待 D7/autoglm 恢复

## 四、Bing 收录核查 (R2)
- .hermes/logs/bing-index-check-0819.md 已存在; IndexNow 近 7 天全 200
- BWT 验证 = **user 行动卡 PENDING** (Import from GSC 5 分钟; BWT 后台 URL Inspection 确认 legit2+Halloween2+money3+首页/对比3)

## 五、NORTH-STAR-DATA (8/14-8/20)
- 展示: 7d 1,751 imp (可用 5 日口径日均 ~350; 剔除 8/18 数据滞后假象后 8/14-17 日均 ~430) — 回吐线 250 未触及
- 点击: 1 (8/16) — GA4 未就位, 归因 NODATA
- CTR: ~0.06% — 深度排名期常态
- Boost 完成度: 4/25 (维持); #3 达标里程碑 +1

## 六、8/22 待办
- 8/22 早拉 8/15-8/21 窗口: #1/#2 严格 T+14 正式判定 + #2 NODATA 排查
- 8/22 K3 复核: print-price 方案 A 分歧 (vs daily-ops 维持现状)
- 8/23 复盘 + 合规 push; 8/25 Halloween 素材 push



---

# 8/22 严格复读（T+14 正式判定 · STRATEGY-2026-08-22 T2）

> 执行: daily-search cron 2026-08-22 19:4x | 窗口: 8/15-8/21 (7d) | 数据: .hermes/tmp/t14-targeted-0822.json + rank-sentinel-2026-08-22.md（GSC API 实时, SOCKS5 OK）

## #1 stickermule-review — Branch B 维持（低量噪音, C/B 边界）

| 口径 | 8/8 基线 | 8/21 窗 (8/14-20) | **8/22 复读 (8/15-21)** | 判定 |
|---|---|---|---|---|
| 主词 sticker mule | 35.1 | 35.00 @6 imp | **41.00 @4 imp** | 低量波动 (Δ-6.0 但 imp 4 vs 6, 样本噪声), 不构成趋势 |
| sticker mule review | - | NODATA | **NODATA** (0 imp) | 持续无数据 |
| 页级 | - | 40 imp @51.98 | **39 imp @53.59** | 持平 (Δ-1.6) |

- 结论: 三口径均无显著移动 → **Branch B 维持**（保持四杠杆节奏 + 补外部信号 Pinterest/社交）
- 新发现: 站内入链核查 = 仅 self-ref 1 处（stickermule-review 在 src/data 全量仅 1 引用）→ 与 #2 同病, 列入动作项（hub 页 + POD 集群 blog 加变体锚入链）

## #2 runway-ml-review — 悬置解除, 走 Branch C 路径（确认）

| 口径 | 8/8 基线 | 8/21 窗 | **8/22 复读 (8/15-21)** | 判定 |
|---|---|---|---|---|
| 主词 runway ml review | 63.0 | NODATA x3 | **NODATA x4 连续** | 4 窗口无展示 → 非数据滞后, 进入 Branch C |
| 变体 | - | runway ml review 72 @1 | is runway ai good 81 @1 / runway ai review 77 @1 | 弱信号 |
| 页级 | - | 31 imp @71.03 | **28 imp @70.86** | 持平 |

- **Branch C 路径执行**:
  1. 锚文本/内链核查（本日完成）: **站内入链 = 0**（runway-ml-review 全量仅 self-ref）— 对比 midjourney-review 2 / pika-labs-review 2 → 内链缺失成立
  2. URL Inspection 重爬请求: 本环境 API 端点 404（daily-ops 已记录工具缺口）→ **user 行动卡**: GSC UI → URL Inspection → 请求编入索引/重爬（1 min）
  3. 外部信号: 待 autoglm/D7 恢复后 Pinterest/社交补（现 NODATA）
- 内链补强动作项（排期 8/24 T+7 前, 需 1 次 push）: midjourney-review / pika-labs-review / heygen-review / ai-video hub 页 → /runway-ml-review/ 变体锚入链 (runway alternatives / compared to X)

## 严格复读结论汇总
- #1 Branch B 维持; #2 Branch C 启动（内链 0 + 重爬待 user）; #3 Branch A 维持（13.50 微回撤, 页级 14.21 仍历史最佳）; #4 见 RANK-ALERT（-9.17, 8/23-24 连续窗口确认, 持续 >=5 位则回滚 H1）
- 判定书 8/22 段完成 → T2 幂等键达成