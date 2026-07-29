# aitoptools Week 1 30 天日均 100+ UV 任务卡 (K3 7/30 04:20 拍板)

> **背景**: K3 7/30 03:43 战略调整, 北极星指标 #1 从转化率 (commission $3000/5 月) 转移到流量 (日均 UV 100+/30 天).
> 当前: GA4 日均 0 UV. 7/30 目标 5-10 UV, 8/6 目标 30-50 UV, 8/13 目标 70-100 UV, 8/30 目标 100-150 UV.
> **约束**: §0 护栏 (M3 月): 不立新 IA / 不写新内容 (3+1) / 不接 paid placement / 禁给 organic 加 UTM / GEO 标记 geo=1 不污染 organic / 价格不编造 / organic rel=nofollow.

---

## Week 1 (8/3-8/9) — 目标 20-30 UV/天

| # | 任务 | 落地路径 | 工作量 | 阻塞 | 状态 |
|---|---|---|---|---|---|
| W1-1 | 写 GSC submit 脚本 (sitemap + Indexing API) | `scripts/submit-gsc-sitemap.py` | 0.5h | user OAuth 凭证 (半自动) | ✅ DONE 7/30 |
| W1-2 | 写 IndexNow 脚本 (Bing + Yandex + Seznam + Naver) | `scripts/submit-indexnow.py` | 0.5h | user 申请 API key (半自动) | ✅ DONE 7/30 |
| W1-3 | Gmail 通道打通 (Gmail App Password) | `.hermes/secrets/gmail_credentials.json` (gitignored) | 10 min | user 浏览器 16-char (🔴 D8+) | ⏳ 模板 ready |
| W1-4 | 立即提交 99 URLs 到 IndexNow | `python scripts/submit-indexnow.py` | 1 min | user 给 key | ⏳ 模板 ready |
| W1-5 | 立即提交 sitemap 到 GSC | `python scripts/submit-gsc-sitemap.py` | 1 min | user 给 OAuth | ⏳ 模板 ready |
| W1-6 | schema.org markup 扩展 (Product/SoftwareApplication/FAQPage JSON-LD) | `src/app/[slug]/page.js` + `compare/[slug]/page.js` + `page.js` | 3h | **§6 锁需 user 拍板** | ⏳ 草稿在 .hermes/drafts/ |
| W1-7 | 4-5 篇 SEO 文章草稿 (WordPress-style, English, AI tools 评测类) | `.hermes/drafts/articles/*.md` | 4-6h | 内容护栏 §0 (不写新内容) | ⏳ 草稿在 .hermes/drafts/ |
| W1-8 | Reddit 5 帖草稿 (r/printondemand / r/Etsy / r/Shopify / r/sidehustle / r/Entrepreneur) | `.hermes/drafts/social/reddit-*.md` | 2h | 平台护栏 (no self-promo) | ⏳ 草稿 ready |
| W1-9 | Pinterest 10 钉草稿 (评测类图片 + 工具截图) | `.hermes/drafts/social/pinterest-*.md` | 2h | 平台护栏 (no spam) | ⏳ 草稿 ready |
| W1-10 | 3 评测类平台 review 草稿 (G2 / Capterra / ProductHunt) | `.hermes/drafts/reviews/*.md` | 2h | 平台护栏 (no fake review) | ⏳ 草稿 ready |
| W1-11 | 第 1 篇文章上线 (commit + push + 7/31 攒批 1 push) | `src/app/blog/{slug}/page.js` 或 posts 数组 | 2h | W1-7 草稿 + W1-6 schema | ⏳ |

**Week 1 累计估算 UV**: GSC 收录 (3-5 天延迟) + IndexNow 立即触发 Bing 抓取 (24-48h 延迟) + Reddit/Pinterest 长尾 (1-2 周延迟) → 8/9 估算 20-30 UV/天

---

## Week 2 (8/10-8/16) — 目标 40-60 UV/天

| # | 任务 | 工作量 | 状态 |
|---|---|---|---|
| W2-1 | 第 2 篇 SEO 文章上线 ("Printful vs Printify 2026") | 3h | backlog |
| W2-2 | 第 3 篇 SEO 文章上线 ("how to use AI for print design") | 3h | backlog |
| W2-3 | Pinterest 5 钉补增 (10 → 15 累计) | 1h | backlog |
| W2-4 | 双引擎结构改造 (GEO 4 线 + SEO 4 线 + GSC 接入) — W2-T4 已部署待 M3 执行 | 6h | READY |

**Week 2 累计估算 UV**: 2 篇文章收录 + GSC 流量基线 (20-30) + Pinterest 长尾 (10-20) → 8/16 估算 40-60 UV/天

---

## Week 3 (8/17-8/23) — 目标 70-100 UV/天

| # | 任务 | 工作量 | 状态 |
|---|---|---|---|
| W3-1 | 高佣深链补齐 (target_type=product 深链 ≥80%) | 4h | backlog |
| W3-2 | 第 4 篇 SEO 文章上线 ("best mockup generators 2026") | 3h | backlog |
| W3-3 | 5 评测类平台 1-2 个上线 (G2 / Capterra) | 3h | backlog |

**Week 3 累计估算 UV**: 4 篇文章收录 + 评测类外链 + GSC 长尾 → 8/23 估算 70-100 UV/天

---

## Week 4 (8/24-8/30) — 目标 100-150 UV/天

| # | 任务 | 工作量 | 状态 |
|---|---|---|---|
| W4-1 | 第 5 篇 SEO 文章上线 ("AI packaging design tools 2026") | 3h | backlog |
| W4-2 | Pinterest 累计 25-30 钉 | 1h | backlog |
| W4-3 | 外链第 2 波 (Pinterest boards / Reddit 续帖 / 行业目录) | 4h | backlog |
| W4-4 | 交叉榜: 5 工具对比 + 5 类目页补全 | 6h | backlog |

**Week 4 累计估算 UV**: 5 篇文章 + 评测类外链 + 交叉榜内链强化 → 8/30 估算 100-150 UV/天 (达到 30 天目标)

---

## 不做 (K3 7/30 04:20 拍板)

- ❌ 撤按钮 (W1-T2 撤回) — 14 天 1 click 是 baseline 不是问题
- ❌ 6 个 Impact 品牌申请 (Canva/Shopify/Bluehost/Surfer/Copy.ai/Placeit) — 等 Kittl 跑通再说
- ❌ W1-T2 攒批 (CTA 主次反转 + 价格锚点 + 详情页补 CTA + link_id 可读化) — 等 UV > 100/天 再启动
- ❌ 评测类新工具 (不立新 IA, 维持 107 工具不变) — §0 护栏
- ❌ paid placement (破坏中立人设) — §0 护栏
- ❌ 静态编造评价 (Manual Action 不可逆) — §0 护栏

---

## 11 项 Week 1 自动分层 (K3 7/30 04:20 拍板)

### Agent 完全可做 (今晚 / 明天)
- ✅ W1-1 写 GSC submit 脚本
- ✅ W1-2 写 IndexNow 脚本
- ✅ W1-3 写 gmail_credentials.json 模板 (gitignored)
- ✅ W1-7 5 篇 SEO 文章草稿 (.hermes/drafts/)
- ✅ W1-8 5 Reddit 帖草稿 (.hermes/drafts/)
- ✅ W1-9 10 Pinterest 钉草稿 (.hermes/drafts/)
- ✅ W1-10 3 评测类 review 草稿 (.hermes/drafts/)
- ✅ 写 docs/IMPACT_W8BEN_GUIDE.md (智印云 W-8BEN-E 填写指南)
- ✅ 写 .hermes/cron-prompts/aitoptools-week1-30day-traffic.md (本任务卡)

### 半自动 (user 给 token, agent 1 分钟接上)
- 🔴 W1-4 立即提交 99 URLs 到 IndexNow (需 user 给 .hermes/secrets/indexnow-key.txt)
- 🔴 W1-5 立即提交 sitemap 到 GSC (需 user 给 .hermes/secrets/gsc-oauth.json)

### Agent 不能做 (§7.7 红线)
- ❌ 登录 Google / Impact / 邮箱 / Impact Discover (6 品牌)
- ❌ 填 W-8BEN-E / Payout / Gmail App Password (浏览器操作)

### §6 锁待 user 拍板
- ⏸ W1-6 schema.org markup 扩展 (改 src/app/[slug]/page.js + compare/[slug]/page.js + page.js) — 需 user 拍板破 §6 锁

### 内容护栏 §0 风险 (待 user 拍板 commit)
- ⏸ W1-7 5 篇 SEO 文章 — §0 护栏不写新内容, 但 M3 月内 3+1 篇已拍板 (P3 7/30-8/5 + 1 篇 3D = 4 篇), 5 篇超 4 篇
- ⏸ W1-8 Reddit 5 帖 — 平台护栏禁止 self-promo, 草稿需 user 审核
- ⏸ W1-9 Pinterest 10 钉 — 平台护栏禁止 spam, 草稿需 user 审核
- ⏸ W1-10 3 评测类 review — 平台护栏禁止 fake review, 草稿需 user 审核

---

## 攒批 push 计划 (1 push/day 纪律)

| 日期 | 攒批内容 | 紧急例外 |
|---|---|---|
| 7/31 04:00 | 4 文件撤回版 (page.js + programs.json + AFFILIATE_LOG.md + commit_msg.txt) + 2 脚本 (IndexNow + GSC) + 1 文档 (IMPACT_W8BEN_GUIDE) + 1 任务卡 (本文件) | — |
| 8/2 04:00 | schema.org 扩展 (W1-6, §6 锁待破) + 第 1 篇文章 (W1-7 first 1/5) | — |
| 8/5 04:00 | 第 2 篇文章 + 第 3 篇文章 (W1-7 next 2/5) | — |
| 8/8 04:00 | Reddit 5 帖 + Pinterest 10 钉 + 3 评测 review (W1-8/9/10, 入 .hermes/drafts/social/ 等 user 拍板) | — |
| 8/11 04:00 | (W2 启动) 第 4 篇文章 + Pinterest 5 钉补增 (W2-1/2/3) | — |
| 8/14 04:00 | (W2) 双引擎结构改造 (W2-4) | — |
| 8/17 04:00 | (W3 启动) 高佣深链 (W3-1) | — |
| 8/20 04:00 | (W3) 第 4 篇文章 + 5 评测类平台 (W3-2/3) | — |
| 8/23 04:00 | (W4 启动) 第 5 篇文章 + Pinterest 累计 (W4-1/2) | — |
| 8/26 04:00 | (W4) 外链第 2 波 + 交叉榜 (W4-3/4) | — |

---

## K3 7/30 04:20 拍板结论

**做 11 项全部 + 4 周路线, 今晚攒批 1 push (撤回版 + 2 脚本 + 1 文档 + 1 任务卡 = 5 文件), 明天 7/31 早 push.**

**不做**: 撤按钮 / 6 品牌 / W1-T2 / 评测类新工具 / paid placement / 静态编造评价.

**北极星 #1 (流量)**: 0 → 5-10/天 (7/30) → 20-30/天 (8/9) → 40-60/天 (8/16) → 70-100/天 (8/23) → 100-150/天 (8/30).

**北极星 #2 (转化率) 暂缓**: 等 UV > 100/天 再启动 (W4 之后).

**北极星 #3 (决策质量) 永久**: 撤回率 / 拍板响应 / 过度优化零容忍.
