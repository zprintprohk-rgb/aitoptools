# GEO Citation Weekly Audit - 2026-08-30

> 执行: weekly-review run 13:18 补落盘 | 试点查询由 13:03-13:14 前序 weekly-review 会话经 autoglm-browser-agent 只读完成 (session_pool.json + 各 session task_result.md 双重实证, 13:2x 本 run 逐字提取核验)
> 覆盖: rank-sentinel-20q 清单 (20 核心词) | 本轮试点: 首词 "best AI tools for print on demand" x 3 引擎
> 状态: PILOT_DONE (1/20 词 x 3 引擎, 3/3 均 0 引用) — 全量 20x3 待夜窗分批 (18:00-08:00 窗口, autoglm 已恢复)

## 审计结果 (query #1: best AI tools for print on demand)
| query | ChatGPT | Perplexity | Gemini | 引用 URL |
|---|---|---|---|---|
| best AI tools for print on demand | 否 - 纯品牌推荐无引用列表 (提及 Etsy/Shopify/Amazon Merch/Redbubble/Printful/Printify + 工具名 Kittl/Ideogram/Midjourney/Canva/Adobe Firefly/MyDesigns/Placeit) | 否 - 引 10 源/9 域, 全部为第三方内容站 (podvector.ai x3 + ecommerceparadise + mydesigns.io + aitrendtool + podbase + sellerstacked.co + dodropshipping + profitlab360) | 否 - 无来源引用列表, 纯品牌推荐 (ChatGPT/Claude/Midjourney/Kittl AI/Canva Pro/MyDesigns/Magnific/Krea/Mockey/Placeit/Etsy/Shopify) | 无本站引用 |
| 剩余 19 词 | PENDING (夜窗分批) | PENDING | PENDING | - |

**结论 (3/3 引擎 0 引用 aitoptools.net)**:
- **Perplexity 是唯一带外链引用列表的引擎** — 9 个内容域中 podvector.ai 单域占 3 席 (同题文章矩阵垄断该 query) → GEO 引用攻坚主战场 = Perplexity 型引用引擎; 竞对可抄样板 = podvector.ai 同题结构
- **ChatGPT/Gemini 对该 query 纯品牌名作答** (无引用/无外链) → 这类引擎的收录路径是品牌词/信任词直接问答 (如 is-magicdrop-legit 型), 而非 listicle 引用; 我方 magicdrop 页 GSC 页级 pos 2.0 (8/30, 1 imp 低样本) 已处引用候选区间上沿, 下一批夜窗优先验证 "is magicdrop legit" 词
- 无登录墙: ChatGPT/Gemini/Perplexity 三站本次均可匿名完成问答 (CAPTCHA 0 次), 夜窗全量分批可行

## 证据链
- Perplexity: session 1d6d109f-e44e-4567-9113-627f0a674238 / tab 97688857 / permalink perplexity.ai/search/051b0a23-c099-45ba-9afa-683e20cc63b8 (10 源全 URL 明细在 task_result.md)
- ChatGPT: session 540efdc2-f3c7-460c-a48c-504d54802821 / tab 97688858 / conversation chatgpt.com/uc/6a93baa6-03dc-83ea-9cdb-4c23ca5047fb
- Gemini: session b3a1827d-b808-4994-898f-e545c6c5e843 / tab 97688860 / conversation gemini.google.com/app/f1d5132108e50b60 (另有首试 tab 97688859 / e6c049d68c865c32 未出分析)
- 原始结果文件: C:/Users/Administrator/.openclaw-autoclaw/sessions/{session_id}/task_result.md (session pool TTL 12h 内可复查)
- 提取时间: 2026-08-30 13:2x Asia/Shanghai, [result] 段逐字核对, 与 weekly-2026-08-30.md 块 5 声称一致

## 幂等键
- 本文件 = geo-citation-weekly-2026-08-30.md; 当日已存在非空 -> 后续 NOOP; 全量 20x3 夜窗分批进度以本文件为台账 (每批完成后在表中补行)

## 批次 2 (2026-08-30 19:2x-19:4x, daily-search 夜窗) — query: 「is magicdrop legit」
| query | ChatGPT | Perplexity | Gemini | 引用 URL |
|---|---|---|---|---|
| is magicdrop legit | 完成 - 区分多域名风险(magicdrop.com POD 停服/magicdrop.store 诈骗警告/magicdrop.io 正常/magicdrop.link+.win 钓鱼), 引 scamadviser/gristock 等 7 域, **0 引用本站** | LOGIN_REQUIRED - 匿名配额耗尽弹注册墙, 查询已提交但结果不可读, 按铁律不绕过 (NODATA) | 完成 - 拆 3 无关服务(magicdrop.link 皮肤开箱=钓鱼/dropmagic.ai 店铺构建=合法/MagicSchool=教育), 引 gridinsoft/shopify app store/ecommerce platforms 等 4 域, **0 引用本站** | 无本站引用 |

**批次 2 洞察**:
1. is magicdrop legit 的 ChatGPT/Gemini 答案空间被**同名品牌混淆**主导 (钓鱼站/其他 MagicDrop 服务), 我方 is-magicdrop-legit 页 (GSC 页级 pos 2.0) 正是该混淆的正解但未被引用 → 需强化实体锚定信号 (background remover/print on demand 实体词 + 外部信任信号), 单纯页面质量不足
2. 引用来源画像: ChatGPT 偏安全评分站 (scamadviser), Gemini 偏安全扫描+应用商店 (gridinsoft/shopify) — 第三方信任背书是共同引用偏好, 我方缺此类外部信任信号
3. Perplexity 匿名配额当日耗尽 (上午试点 1 词后), 后续批次 Perplexity 读数可能持续 NODATA, 直至匿名窗口重置或 user 登录
4. 会话证据: ChatGPT session 1c60a69f (tab 97689061, chatgpt.com/uc/6a941574); Gemini session 42e15a39 (tab 97689062, gemini.google.com/app/0c4a31313bb685e3); Perplexity session 17b12f22 (查询 URL perplexity.ai/search/4e503b5e 但结果被墙)
