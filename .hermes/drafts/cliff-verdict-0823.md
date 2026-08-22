# 悬崖判定书 — 2026-08-23 (STRATEGY-2026-08-23 T1)

> 执行: daily-search cron 2026-08-23 04:3x CST | 数据: .hermes/tmp/cliff-0823.json (GSC API 实时, SOCKS5 OK) + 本地 out/ 审计 + 线上 HTTP 抽查

## 一、数据位 (T1 ①-④)

| 维度 | 实测 | 结论 |
|---|---|---|
| ① 回填 (8/21-8/22) | 日期维度仅到 8/20: 8/18=33 / 8/19=29 / 8/20=29; 8/21+8/22 NODATA (T+2 窗已关) | **Branch A 排除** (无回填, 与 8/22 修正结论一致) |
| ② 页型分解 (8/18-22) | 24 页在场: 首页 12 / review 类 (gempages 14, manychat 15, stickermule 15, CF 4...) / best 类 (printful-alt 5, tshirt 4) / blog 2 / compare 1; 全类型均匀低展示, 无选择性掉页 | **Branch B 特征** (均匀低展示) |
| ③ query 轨迹 | 7d 窗口 (8/16-22) 201 query (日均 ~29) vs 悬崖前 321+; imp>=10 仅 4 词 | query 数随展示同步塌缩, 无异常新词 |
| ④ 本地索引审计 | out/ top-10 页 noindex=全部 False, canonical 全部正确; 线上 6 URL 抽查 6/6 HTTP 200; robots.txt AI 爬虫段+ sitemap 声明正常; sitemap.xml 线上 200 (347 URL) | 索引层无本地故障信号 |
| ⑤ git 状态 | b58cb7d 与 2365ad4 均在 main 且 AHEAD=0 (已推); b58cb7d 消息中「含未推 2365ad4」为 8/15 当日快照, 2365ad4 已于当日后续 push 上线 | 无重复执行风险 |

## 二、判定: **Branch B — 核心更新曝光测试结束 / 均匀低展示**

- 依据: 位置稳定 (magicdrop 13.4 / society6 pos 2 / 哨兵 20q 仅 print price 告警) + 页在索引 (canonical/noindex/200 全过) + 均匀低展示 (页型分解无选择性) → 三者齐备, 指向算法曝光层而非站点故障
- 排除项: Branch A (8/21 无回填, T+2 已关) / Branch C (无掉页、无 noindex、无 manual action 线索)
- 处置: **滚动期纪律延长 2 周 (至 9/6)**; 产线节奏不变; 不做任何恐慌性改版/改模板/改内链架构 (STRATEGY NOTES 1)
- 独立旁证 (user 动作): GSC UI 端 sitemap lastDownloaded 停 7/17 + indexed 0 — 线上文件正常但提交记录失联, user GSC 重提 sitemap.xml (1 min), 与悬崖排查联动
- 测量纪律: 悬崖类判定以连续 >=4 天 + T+3 回填为准; 8/23-24 观察 8/21-8/22 数据是否出现

## 三、T2 print-price Day-1 (回滚确认窗)

| 窗口 | 主词 print price ai tool | Δ vs 基线 62.75 |
|---|---|---|
| 8/14-20 (8/21 读) | 62.75 @8 | 基线 (方案 A 部署前) |
| 8/15-21 (8/22 复读) | 71.92 @13 | -9.17 |
| 8/16-22 (8/23 Day-1) | **72.92 @12** | **-10.17** (连续 2 窗下跌, >=5 位) |

- **Day-1 结论: 下跌持续确认** (2 连续窗口均跌 >=5 位) → 回滚方案备好 (只备不改), 8/24 Day-2 再确认后执行
- 回滚方案 (git revert 备选, 不执行): 恢复 print-price-ai-tools-2026 title/H1/metaDesc 至 8/20 前版本 (git show 55bb1a2^:src/data/blog-posts.json 取原值), 首段 calculator-first 表述还原, dateModified 保持; FAQ 新增条目保留 (无害); 回滚后 IndexNow 重推
- 风险对冲: 8/23-24 若 8/22 数据回填且主词回升 -> 视为噪音, 不执行回滚

## 四、幂等键: 本判定书存在 -> T1/T2 Day-1 视为完成