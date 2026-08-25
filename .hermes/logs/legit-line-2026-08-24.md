# legit 信任产线 — 2026-08-24 成稿日志

> 产线: aitoptools legit 信任产线 (PLAN-2026-09-MONTHLY §六 + STRATEGY-2026-08-22 T4; D12/D13 已授权视为拍板, 8/22 激活)
> 任务: 取队列 1-2 篇 -> 成稿 -> (截图) -> 校验 -> 日志 (本次只成稿不 push)

## 幂等检查
- legit-line-2026-08-24.md 不存在 -> 非 NOOP, 正常执行

## 队列取篇
- 已部署 4 篇 (magicdrop/gearlaunch/spocket/kittl); 按任务优先 + GSC imp 取 2 篇:
  - **is-society6-legit** (优先 Society6, imp 59)
  - **is-veed-io-legit** (imp 最高 80)
- 队列剩余: TeePublic(66) / Redbubble(67) / Gelato(26) / PosterMyWall(63.5)

## 事实核实 (web_search 恢复可用 + SmartCustomer 直抓)
- web_search 本次恢复 (非 insufficient_credits), 成功拉取 Trustpilot 关键数据:
  - Society6 Trustpilot: TrustScore 3.5/5, ~2,056 reviews (trustpilot.com/review/www.society6.com)
  - Veed Trustpilot: 4.2/5, ~3,822 reviews, TrustScore 4/5 "Great", 2 周内回复 (trustpilot.com/review/veed.io)
- SmartCustomer (Sitejabber 镜像) 直抓成功:
  - Society6: 1,526 reviews / 3.6/5 + 5 条实名投诉 (artist 佣金 5-10% / 重复扣款退款扣运费 / 错发商品无响应 / 卖家页面 bug / 客服无电话)
  - Veed: 0 reviews (未邀请反馈, 如实标注)
  - Redbubble: 2,130 / 4.2 (备用数据) | TeePublic: 2,329 / 2.9 (备用数据)
- 公司/退款补齐:
  - Veed: veed.io/about (2018-03-20 由 Sabba Keynejad 创立, $35M 融资, 150+ 员工) + GetLatka ($50M ARR / $160M 估值) + veed.io/terms-of-sale (续费前 2 工作日可取消, 当期不退款=标准 SaaS)
  - Society6: Leaf Group 公开公司史 (NYSE: LFMD, 2020 新闻稿 GTV $21.3M) + Graham Holdings 2022 收购 + MediaLab 伞下 + society6.com/pages/terms

## 成稿 (src/data/blog-posts.json)
| slug | wordCount | FAQ | blocks | 主CTA | 次CTA | 来源核验 |
|---|---|---|---|---|---|---|
| is-society6-legit | 2721 | 8 | 41 | Visit Society6 | Try Printify Free | Trustpilot 3.5/5 2056 + Sitejabber 3.6/5 1526 + Leaf Group 公司史 |
| is-veed-io-legit | 2715 | 8 | 42 | Visit Veed.io | Try Kittl Free | Trustpilot 4.2/5 3822 + veed.io/about + terms-of-sale |
- 两篇均按 legit-template-v2.md: 公开 rubric 评分卡 (table) + answer-first + H2 问句式 + FAQ>=5 + 来源 URL 带 rel nofollow + 双向互链 + 替代品 CTA
- 评分 (rubric 30/25/25/20): Society6 62.5/100 (Conditional), Veed 77.5/100 (Conditional, 偏推荐侧)
- 双向互链已补齐: blog-posts.json legit 页链 reviews.json; reviews.json (society6-review/veed-io-review) 已加回链到 legit 页

## 截图
- public/tool-screenshots/blog/ 下共 4 张 (均为 kittl-halloween 旧图), **无 is-society6-legit / is-veed-io-legit 专用截图**
- 记录缺口, 不阻塞成稿; 正文未引用不存在的 screenshot 块

## 校验
- node JSON.parse: blog-posts.json (18 篇) / reviews.json (107 条) 均合法
- python scripts/validate_content_data.py: **[OK] 全部通过** (EXIT=0, PYTHONIOENCODING=utf-8)
- wordCount >= 2500: Society6 2721 / Veed 2715 均达标
- FAQ >= 5: 均为 8
- 18 篇 blog 主CTA 全 ✓

## 产物 (本次只成稿不 push)
- 已改: src/data/blog-posts.json (+2 legit 页, 18 篇)
- 已改: src/data/reviews.json (society6-review / veed-io-review 加 legit 回链)
- **未 push** (攒次日/当次合并 push, 省 build quota)
- git status 确认仅上述 2 个 M 文件为本任务改动

## 下次续跑提示
- 队列剩余: TeePublic(66) / Redbubble(67) / Gelato(26) / PosterMyWall(63.5)
- 备用数据已抓: Redbubble Sitejabber 2,130/4.2 + TeePublic 2,329/2.9; Trustpilot 需 web_search 补拉
- legit 产线进度: 6/10 (9/13 目标 10 篇, 偏差 40%)