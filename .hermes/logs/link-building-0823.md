# 外链提交记录 — 第 2 批 12 站 (2026-08-15)

> 执行: W2-0823 集群合并push cron (提前执行轮) | 依据: .cluster/link-directory-list.md P0/P1 清单 (批 1 8 站 0/8 后顺延)
> 统一实体描述: aitoptools.net — Print AI Tools review site specializing in AI-powered solutions for print shops, packaging design, and e-commerce store operations. Founded by Jerome Tang of Shenzhen Cai Long Printing
> 邮箱: jerome@aitoptools.net | 目标 URL: https://aitoptools.net
> 原则: CAPTCHA/登录墙/连接拦截 → 记录 BLOCKED_* 不硬闯 (批 1 同纪律); 探测存档 .hermes/tmp/linkbuild-0823/probes.json

## 提交结果总表 (urllib GET, 8s 超时, 2026-08-15 20:5x CST)

| # | 站点 | URL | 结果 | 说明 |
|---|------|-----|------|------|
| 1 | AIxploria | https://www.aixploria.com/en/add-tool/ | BLOCKED_CONNECTION | 边缘拦截/超时, 换时段重试 |
| 2 | AI Tools Directory | https://aitoolsdirectory.com/submit-tool | BLOCKED_JS_FORM (200) | 页面 200 但表单 JS 驱动, 无 action 可提交 |
| 3 | AIChief | https://aichief.com/submit/ | BLOCKED_CONNECTION | 边缘拦截/超时 |
| 4 | AI Hunt List | https://aihuntlist.com/submit-tool/ | BLOCKED_CONNECTION | 边缘拦截/超时 |
| 5 | AITopTools (aitoptools.com) | https://aitoptools.com/submit/ | BLOCKED_CONNECTION | 竞品同名站, 提交时勿混 (清单已注明) |
| 6 | AllThingsAI | https://allthingsai.com/submit/ | BLOCKED_CONNECTION | 边缘拦截/超时 |
| 7 | AI Valley | https://aivalley.ai/submit/ | BLOCKED_BY_CAPTCHA | 200, 含 captcha 标记; 需人工浏览器 |
| 8 | Insidr AI | https://www.insidr.ai/ai-tools/submit | PROBE_OK (200) | "Submit News About AI" 表单存在, JS 提交 → 待浏览器 |
| 9 | OpenTools | https://opentools.ai/ | BLOCKED_NEEDS_LOGIN | 200 目录 2500+ 工具; 提交需 Google 登录 (清单备注) |
| 10 | FutureTools | https://www.futuretools.io/submit | BLOCKED_CONNECTION | 口碑最佳免费目录之一, 反机器人验证; 待重试 |
| 11 | Startuplist.in (批1重试) | https://startuplist.in/submit | BLOCKED_CONNECTION | 二次重试仍超时 (批 1 同), 站点边缘防护 |
| 12 | ProductCool | https://www.productcool.com/submit | PROBE_OK (200) | 24-48h 上线; 表单 JS → 待浏览器 |

## 小结
- **成功提交: 0/12** (全部被验证码/JS 表单/连接拦截, 按"不硬闯"原则全部记录 BLOCKED)
- 两批累计: 0/20 直接提交; 真实提交路径 = 浏览器自动化 (autoglm) + 人工 CAPTCHA + 回链决策
- **待浏览器提交池 (PROBE_OK + 批1)**: insidr.ai / productcool.com / opentools.ai (需 Google 登录) / findly.tools / toolpilot.ai / thenextai.com / launchboosts.com + AI Valley (CAPTCHA 人工)
- **回链决策待办 (K3)**: aitoolzdir.com (免费 API 已逆向, 请求体存档) + wired.business 免费档需站内回链
- 下次重试建议: FutureTools / AIxploria / AllThingsAI 换时段或换网络