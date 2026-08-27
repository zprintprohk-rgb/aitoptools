# legit-line 日志 — 2026-08-28

> 产线: aitoptools legit 信任产线 (PLAN-2026-09-MONTHLY §六 + STRATEGY-2026-08-22 T4)
> Broker: AutoClaw cron 42f8dbcb | model=deepseek-v4-flash
> 状态: **新成稿 2 篇完成（本次不 push，攒批合并）**

## 一、幂等判断
- 当日日志 legit-line-2026-08-28.md 初始不存在 → 非 NOOP，执行。
- 队列: Spocket/Kittl/Society6/Veed 已完成（8/26-8/27 轮次）；本次取 GSC imp 剩余最高两位 **Redbubble (67) + TeePublic (66)**，factcheck-0820 备料在案。

## 二、本次篇目（新建 2 篇）
### is-teepublic-legit — 2,571 词 — 65/100 Conditional — datePub 8/28
- 数据复核（web_search 8/28 官方快照）: Trustpilot **4.4/5, 642,673 reviews**, 回复 98% 负评 24h 内（factcheck-0820 记 640,587 → 8/28 滚动至 642,673，更新引用）
- 拼写混淆域说明: teerepublic.com (2.8/5, 11 reviews) 为独立小档案，非 TeePublic 本体，正文显式区分
- 评分卡: 声誉 2 / 退款 1（trendlytic 证实流程但官方政策页未直抓，如实扣分）/ 透明度 1（2013 年至今运营，注册实体未核）/ 实测 1（二手带源）→ 65/100
- Exclusive Test: 如实声明未实测下单 + 5 行二手表带源
- FAQ 7 条（legit/safe/trustpilot/scam/worth it/refunds/alternatives）
- related: teepublic-review + redbubble-review + is-redbubble-legit + is-society6-legit

### is-redbubble-legit — 2,791 词 — 60/100 Conditional（压线）— datePub 8/28
- 数据复核（web_search 8/28 官方快照）: Trustpilot 拼写域 redbuble.com **1.5/5, 118 reviews**（8/20 记 ~117 条未记分值 → 8/28 确认 1.5 分值）；BBB **NOT Accredited**（San Francisco 档案, 112 投诉/3 年, 19 closed/12mo）官方确认
- 90 天无条件退款保证: mywifequitherjob + trendlytic (Jun 2026) 双源证实 — 系列最强退款窗口
- 评分卡: 声誉 0（1.5 < 3.0 阈值，如实打 0 + 小样本/拼写域 caveat 显式标注）/ 退款 2 / 透明度 2（2006 至今 ~19 年 + BBB 档案可查）/ 实测 1 → 60/100 压线 Conditional
- Exclusive Test: 如实声明未实测 + 5 行二手表带源
- FAQ 8 条（legit/safe/trustpilot/scam/BBB/refunds/artists/alternatives）
- related: redbubble-review + teepublic-review + is-teepublic-legit + is-society6-legit
- metaDescription 精简 161→139 字符（≤155 军规）

## 三、校验结果（全部 PASS）
| 检查项 | TeePublic | Redbubble |
|---|---|---|
| 字数 ≥2500 | 2,571 ✅ | 2,791 ✅ |
| FAQ ≥5 | 7 ✅ | 8 ✅ |
| meta ≤155 | 148 ✅ | 139 ✅ |
| 来源 URL 必带 | TP + trendlytic ✅ | TP + BBB + mywifequitherjob + trendlytic ✅ |
| rubric 表 + 评分唯一 | 65/100 ✅ | 60/100 ✅ |
| Exclusive Test (§6.1) | ✅ | ✅ |
| answer-first + 替代品 CTA | ✅ | ✅ |
| 双向互链 (review 页 + legit 互链) | 4 ✅ | 4 ✅ |
| validate_content_data.py | PASS | PASS |
| JSON 有效性 | ✅ | ✅ |

## 四、图片截图
- 缺口: public/tool-screenshots/blog/ 下无 is-teepublic-legit-*.webp / is-redbubble-legit-*.webp（系列共 6 篇缺截图）
- 不阻塞成稿（两篇无 screenshot 块），记录待补

## 五、legit 系列整体状态（8/28）
| 篇目 | GSC imp | 状态 | 评分 | 字数 |
|---|---|---|---|---|
| is-magicdrop-legit | 120+ | 已部署 | Not Operating 特判 | 3,549 |
| is-gearlaunch-legit | 75 | 已部署 | - | 2,575 |
| is-spocket-legit | 74 | 成稿未部署 | 52.5/100 | 2,947 |
| is-kittl-legit | 67 | 成稿未部署 | 90/100 | 2,716 |
| is-redbubble-legit | 67 | **本次新成稿** | 60/100 | 2,791 |
| is-teepublic-legit | 66 | **本次新成稿** | 65/100 | 2,571 |
| is-society6-legit | 59 | 成稿未部署 | 62.5/100 | 2,942 |
| is-veed-io-legit | 80 | 成稿未部署 | 77.5/100 | 2,930 |

## 六、数据来源
- Trustpilot: trustpilot.com/review/www.teepublic.com + redbuble.com + teerepublic.com 官方页 web_search 快照 (8/28)
- BBB: bbb.org/us/ca/san-francisco/profile/online-retailer/redbubble-1116-365090 (8/28)
- 退款保证: mywifequitherjob.com/is-redbubble-legit + trendlytic.io (Jun 2026)
- factcheck 基线: legit-factcheck-0820.md (TeePublic/Redbubble/Gelato 备料)
- GSC imp: STRATEGY-2026-08-17.md (未二次拉取)

## 七、待办（下次）
- 部署 legit 系列 6 页（spocket/kittl/society6/veed-io/teepublic/redbubble）— generate-sitemap + 攒批 push（本次不 push）
- 新建篇目仍缺: PosterMyWall (63.5 imp, factcheck-0822 数据缺口大: 仅 SmartCustomer 3.0/5 样本 2 条, 需先补核实或 SKIP) / Gelato (26 imp, factcheck-0820 备料可用)
- 截图 6 篇待补；methodology-legit-ratings 方法页仍未建（模板 §3 前置项）
- 审计遗留: d17 明文密码脚本清理待 user 授权删除（8/27 Safety Guard 拦截, P0 安全悬置项）