# legit 信任产线 — 2026-08-22 成稿日志

> 产线: aitoptools legit 信任产线 (PLAN-2026-09-MONTHLY §六 + STRATEGY-2026-08-22 T4; D12/D13 已授权视为拍板, 8/22 激活)
> 任务: 取队列 1-2 篇 -> 成稿 -> (截图) -> 校验 -> 日志 (本次只成稿不 push)

## 幂等检查
- legit-line-2026-08-22.md 不存在 -> 非 NOOP, 正常执行

## 队列取篇
- 按 GSC imp 排序取未完成 2 篇 (优先 Spocket/Kittl/Society6):
  - **is-spocket-legit** (GSC imp 74, 队列 #3)
  - **is-kittl-legit** (GSC imp 67 + is kittl worth it 73, 队列 #4)
- 说明: GearLaunch (#2) 已于 8/19 部署 (is-gearlaunch-legit 存在), 跳过

## 事实核实 (Trustpilot 403 -> 用其他源成功)
- legit-factcheck-0819.md 中 Spocket/Kittl/Society6 Trustpilot 均 403 失败
- web_search 本次 insufficient_credits (不可用)
- 其他源成功: **Sitejabber -> SmartCustomer** (可直接抓取):
  - Spocket: 2.1/5, 29 reviews (52% 5星/45% 1星) https://www.smartcustomer.com/reviews/spocket.co
  - Kittl: 0 reviews (0.0, 未邀请客户反馈) https://www.smartcustomer.com/reviews/kittl.com
- 公司/退款补齐:
  - Kittl: kittl.com/about (founders Tobias Saul + Nicolas Heymann / + funding / 120+ 员工 / 500万-1000万用户) + kittl.com/pricing (cancel-anytime / Stripe / 主流卡+PayPal)
  - Spocket: spocket.co 域名 202 反爬, 公司 registry 详情本周期未独立核实 (如实标注)
- 三工具 Trustpilot 均无法独立复拉 -> 页面如实标注来源为 Sitejabber/SmartCustomer, 绝不冒充 Trustpilot

## 成稿 (src/data/blog-posts.json)
| slug | wordCount | FAQ | blocks | 主CTA | 来源核验 |
|---|---|---|---|---|---|
| is-spocket-legit | 2794 | 8 | 43 | Visit Spocket (+ Printify 次CTA) | Sitejabber 2.1/5/29 + 3 条实名投诉 |
| is-kittl-legit | 2770 | 8 | 42 | Try Kittl Free (kittl.pxf.io) | Sitejabber 0 reviews + 官方 About/Pricing |
- 两篇均按 legit-template-v2.md: 公开 rubric 评分卡 (table) + answer-first + H2 问句式 + FAQ>=5 + 来源 URL 带 rel nofollow + 双向互链 + 替代品 CTA
- 评分 (rubric 30/25/25/20): Spocket 22.5/100 (NotRecommended), Kittl 75/100 (Conditional)
- 双向互链已补齐: blog-posts.json legit 页 链 reviews.json; reviews.json (spocket-review/kittl-review) 已加回链到 legit 页

## 截图
- public/tool-screenshots/blog/ 下共 4 张, 均为 kittl-halloween 旧图, **无 is-spocket-legit / is-kittl-legit 专用截图**
- 记录缺口, 不阻塞成稿 (按任务规定); 两篇正文未引用不存在的 screenshot 块

## 校验
- node JSON.parse: blog-posts.json / reviews.json 均合法
- python scripts/validate_content_data.py: **[OK] 全部通过** (EXIT=0; 首跑因 GBK console 无法打印 ✓ 报编码错, 加 PYTHONIOENCODING=utf-8 后确认通过)
- wordCount >= 2500: Spocket 2794 / Kittl 2770 均达标
- FAQ >= 5: 均为 8
- 16 篇 blog 主CTA 全 ✓

## 产物 (本次只成稿不 push)
- 已改: src/data/blog-posts.json (+2 legit 页, 16 篇)
- 已改: src/data/reviews.json (spocket-review / kittl-review 加 legit 回链)
- **未 push** (攒次日/当次合并 push, 省 build quota)
- git status 确认仅上述 2 个 M 文件为本任务改动

## 下次续跑提示
- 队列剩余未完成: Society6(59) / TeePublic(66) / Redbubble(67) / Gelato(26) / PosterMyWall(63.5) / Veed(80)
- Trustpilot 仍 403 + web_search 欠费 -> 下批 Society6 已有 Sitejabber 1,526 reviews 3.6/5 可用; 其余需同法补 Sitejabber/BBB 数据