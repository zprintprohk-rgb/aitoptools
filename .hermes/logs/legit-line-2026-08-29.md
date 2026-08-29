# legit-line 日志 — 2026-08-29

> 产线: aitoptools legit 信任产线 (PLAN-2026-09-MONTHLY §六 + STRATEGY-2026-08-22 T4)
> Broker: AutoClaw cron 42f8dbcb | model=deepseek-v4-flash
> 状态: **新成稿 2 篇完成（is-gelato-legit 接管并发会话半成品 + is-postermywall-legit 全新成稿）；本次不 push，攒批合并**

## 一、幂等判断与取数
- 当日日志 legit-line-2026-08-29.md 初始不存在 → 非 NOOP，执行。
- 队列核对: Spocket/Kittl/Society6/Veed/Redbubble/TeePublic 均已在 8/24-8/28 轮次完成；剩余未完成 = **PosterMyWall (63.5 imp) + Gelato (26 imp)**，本次两篇全做。
- factcheck 缺口处理: factcheck-0822 对 PosterMyWall 仅有 SmartCustomer 3.0/5 (n=2)，TP/BBB/Reddit 均 403 → 按 cron 指令先补事实核实（web_search 8/29 成功，见下），数据齐 → 不 SKIP。

## 二、并发会话事件（如实披露）
- 本 session 04:55 检查 blog-posts.json 时无 is-gelato-legit；05:12:49 执行写入时发现另一会话已写入 is-gelato-legit 初稿（2,416 词，缺模板 §6.1 Exclusive Test 模块，related[0] 标题与 reviews.json 不一致，TP/Shopify 数据更精确: 4.3/3,313 + 4.8/1,014）。
- 处置: 接管补齐（保留其更精确数据 + 注入 Exclusive Test 表格与收尾段 + 修 related 标题），未回滚其内容；05:12 后两文件 mtime 稳定无再写入。
- 若后续并发会话再次覆盖，以本日志 + git diff 为准。

## 三、本次篇目（2 篇）
### is-gelato-legit — 2,573 词 — 90/100 Recommended — datePub 8/29
- 数据（web_search 8/29 官方快照）: Trustpilot **4.3/5 star (TrustScore 4.5 Excellent), 3,313 reviews, 98% 负评回复 <=48h**; Shopify App Store 4.8/5 (1,014 reviews); G2 4.5/5
- 公司透明: 2007 年创立于奥斯陆，创始人 CEO Henrik Müller-Hansen 在任约 19 年，Series D（gelato.com/leadership + 新闻页 + 独立报道）
- 退款: 官方质量保证条款（defective/damaged → Gelato 承担新订单成本, 无理由退货不适用 = POD 常规）
- 评分卡: 声誉 2 / 退款 2 / 透明 2 / 实测 1（desk-research + 二手带源，如实声明未实测下单）→ (2×0.30+2×0.25+2×0.25+1×0.20)×50 = **90/100**
- 投诉 4 条全带源: TP 客服触达难 / printkk 跟进失效汇总 / Shopify App 客服+可靠性 / ecommercetrix 目录与集成广度
- Exclusive Test (§6.1): 如实声明未下单 + 5 行二手数据表（TP/Shopify/质量条款/公司档案/未实测声明）
- FAQ 7 条（legit/safe/trustpilot/worth it/scam/refunds/alternatives）

### is-postermywall-legit — 2,659 词 — 62.5/100 Conditional — datePub 8/29
- 数据（web_search 8/29 补核实）: Trustpilot **4.5/5 TrustScore (Excellent), 约 103 reviews**（77-103 随镜像/页浮动, 如实标注小样本）; G2 档案 71 reviews; worthepenny 4.7/22
- BBB: **NOT Accredited**（bbb.org/us/ca/foster-city/profile/news-services/poster-my-wall-1116-904739, Foster City, CA 档案存在）
- 退款: 官方退款政策页（postermywall.com/index.php/info/refundpolicy）+ 3 篇官方帮助中心文章（订阅随时取消 / 试用取消转免费 / 续费前可取消）; 打印订单退款: 退运费不退 + 收货后 2 周处理（如实列为摩擦点）
- 评分卡: 声誉 1（4.5 分但样本 <500, 按规则封顶 1 + 小样本 caveat 显式）/ 退款 2 / 透明 1（BBB 档案可查但非 accredited, 注册号/WHOIS 未核）/ 实测 1 → (1×0.30+2×0.25+1×0.25+1×0.20)×50 = **62.5/100**
- GSC 主词 "is postermywall safe" 已覆盖（FAQ + Quick Answer + Red Flags 节）; FAQ 8 条含 BBB/free/worth it 变体
- 新增 3 节过字数: What Does PosterMyWall Cost?（表）/ How Does PosterMyWall Compare to Kittl? / Which Red Flags Did We Check For?

## 四、校验结果（全部 PASS）
| 检查项 | Gelato | PosterMyWall |
|---|---|---|
| 字数 >=2500（page.js countWords 口径） | 2,573 ✓ | 2,659 ✓ |
| FAQ >=5 | 7 ✓ | 8 ✓ |
| meta <=155 | 145 ✓ | 145 ✓ |
| 来源 URL 必带 | TP+Shopify+support.gelato.com+leadership ✓ | TP+BBB+refundpolicy+support 3 篇+G2+worthepenny ✓ |
| rubric 表 + 评分唯一 | 90/100 ✓ | 62.5/100 ✓ |
| Exclusive Test (§6.1) | ✓（接管补齐） | ✓ |
| answer-first + 替代品 CTA | Printify 副CTA ✓ | Kittl 副CTA ✓ |
| 双向互链 | gelato-review 已加回链 ✓ | postermywall-review 已加回链 ✓ |
| validate_content_data.py | **PASS (EXIT 0, 22 篇全过)** | **PASS** |
| JSON 有效性 | ✓ | ✓ |

## 五、图片截图
- 缺口: public/tool-screenshots/blog/ 下无 is-gelato-legit-*.webp / is-postermywall-legit-*.webp（系列共 8 篇缺截图，仅 kittl 有 4 张旧图）
- 不阻塞成稿（两篇无 screenshot 块），记录待补

## 六、legit 系列整体状态（8/29）
| 篇目 | GSC imp | 状态 | 评分 | 字数 |
|---|---|---|---|---|
| is-magicdrop-legit | 120+ | 已部署 | Not Operating 特判 | 3,549 |
| is-gearlaunch-legit | 75 | 已部署 | - | 2,575 |
| is-veed-io-legit | 80 | 成稿未部署 | 77.5/100 | 2,930 |
| is-spocket-legit | 74 | 成稿未部署 | 52.5/100 | 2,947 |
| is-kittl-legit | 67 | 成稿未部署 | 90/100 | 2,716 |
| is-redbubble-legit | 67 | 成稿未部署 | 60/100 | 2,791 |
| is-teepublic-legit | 66 | 成稿未部署 | 65/100 | 2,571 |
| is-society6-legit | 59 | 成稿未部署 | 62.5/100 | 2,942 |
| **is-postermywall-legit** | 63.5 | **本次新成稿** | 62.5/100 | 2,659 |
| **is-gelato-legit** | 26 | **本次新成稿（接管并发稿）** | 90/100 | 2,573 |

首批 10 篇 legit 队列 **10/10 全部成稿** ✅

## 七、数据来源
- Trustpilot: trustpilot.com/review/gelato.com + trustpilot.com/review/www.postermywall.com 官方页 web_search 快照 (8/29)
- BBB: bbb.org/us/ca/foster-city/profile/news-services/poster-my-wall-1116-904739 (8/29)
- 退款/取消: postermywall.com/index.php/info/refundpolicy + support.postermywall.com 3 篇 (360027203631/360035740672/360032612592) + support.gelato.com 8996072/8996049 (8/29)
- 公司档案: gelato.com/leadership + gelato.com news (2024-01) + impactloop (2025-01) + tracxn
- 第三方: apps.shopify.com/gelato-print-on-demand/reviews + g2.com/products/postermywall/reviews + postermywall.worthepenny.com + dodropshipping/printkk/ecommercetrix/mydesigns 评测
- factcheck 基线: legit-factcheck-0819.md (8/24 补充) / 0820 / 0822; 本轮 8/29 web_search 为最新值
- GSC imp: STRATEGY-2026-08-17.md（未二次拉取，转抄口径）

## 八、待办（下次）
- 部署 legit 系列 8 页（spocket/kittl/society6/veed-io/teepublic/redbubble/gelato/postermywall）— generate-sitemap + 攒批 1 push（本次不 push，含 reviews.json 2 条回链）
- 截图 8 篇待补; methodology-legit-ratings 方法页仍未建（模板 §3 前置项）
- 数据卫生观察: postermywall-review content 存在 9 处价格占位异常（D-pattern，107 条 reviews 中 9 条含此模式，存量问题非本次引入，待 user 拍板是否修复）
- 审计遗留: d17 明文密码脚本清理待 user 授权（8/27 Safety Guard 拦截, P0 安全悬置项）; 本轮 .hermes/tmp-legit-*.js 临时脚本亦待授权清理（Safety Guard 拦截删除操作）
