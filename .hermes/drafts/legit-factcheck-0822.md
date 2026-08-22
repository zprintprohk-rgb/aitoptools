# legit 事实核实 #9-10（T4 续轮 · 2026-08-22 19:3x）

> 任务: STRATEGY-2026-08-22 T4（D12/D13 未拍板，只备不部署）| 候选: legit-queue #9 PosterMyWall / #10 Veed（按 GSC imp 排序取次两位）
> 数据源: web_search 不可用（autoglm credits 缺，重试 2 次 FAIL）→ curl/python requests + SOCKS5 直抓替代；Trustpilot/BBB/Reddit/G2/Capterra 均 403 拦截（与 0819 同环境）

## #9 PosterMyWall（is postermywall safe 63.5 imp 簇）

| 维度 | 实测 | 来源 URL | 抓取时间 |
|---|---|---|---|
| 第三方评分 | SmartCustomer（Sitejabber 跳转）3.0/5，样本仅 2 条（2026） | https://www.smartcustomer.com/reviews/postermywall.com | 2026-08-22 19:3x |
| 官网可达 | postermywall.com 首页 200；/index.php/art/pricing 202（反爬挑战） | https://www.postermywall.com/ | 2026-08-22 |
| Trustpilot | 403 Forbidden（Cloudflare 拦截，与 0819 一致） | https://www.trustpilot.com/review/postermywall.com | 2026-08-22 |
| BBB | 403 Forbidden | bbb.org 搜索页 | 2026-08-22 |
| Reddit | 403 Forbidden（reddit.com/search.json） | reddit.com | 2026-08-22 |

**结论**: 仅 SmartCustomer 3.0/5 一条可引（样本极小，写作时标注 sample size）；Trustpilot/BBB/Reddit 待 D13 拍板后补或 user 手动截图。

## #10 Veed（is veed io safe 80 imp 簇）

| 维度 | 实测 | 来源 URL | 抓取时间 |
|---|---|---|---|
| 官网/产品定位 | AI 视频创作平台：text-to-video / AI avatars / AI 剪辑 / 配音 / 字幕；free tier + 付费版（pricing 页 200） | https://www.veed.io/ + https://www.veed.io/pricing | 2026-08-22 |
| 第三方评分 | SmartCustomer 页面存在（标题 Veed.io Reviews）但评分字段未解析出（Next.js RSC 结构） | https://www.smartcustomer.com/reviews/veed.io | 2026-08-22 |
| Trustpilot | 403 Forbidden | https://www.trustpilot.com/review/veed.io | 2026-08-22 |
| G2 / Capterra | 均 403 Forbidden | g2.com/products/veed/reviews / capterra.com/p/199328/Veed | 2026-08-22 |
| Reddit | 403 Forbidden | reddit.com | 2026-08-22 |

**结论**: 官网产品定位可引（AI 视频工具，非 POD，legit 角度 = 订阅安全/免费层/退款政策核查）；评分数据全缺口，待 D13 拍板后补或 user 手动截图。

## 待补清单（D13 拍板后 / autoglm 恢复后 / user 手动截图）
- Trustpilot 评分+评论数（postermywall.com / veed.io）
- BBB 档案状态（两工具）
- 退款政策页 URL + 要点（两工具官方页）
- 投诉模式核查（Reddit/Trustpilot：扣款不退 / 自动续费投诉）
- whois 域名年限（两工具）

## 执行备注
- web_search 失败原因 = AutoGLM insufficient_credits（daily-ops T1 ② 已记录），重试 ≤2 次后转直抓；
- 幂等键: 本文件存在 → T4 视为完成；下次续轮取 legit-queue 下一批候选。