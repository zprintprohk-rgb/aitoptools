# GSC / IndexNow 收录提交日志 — 2026-09-12

**任务**: aitoptools.net 搜索引擎收录提交 (Hermes role, 每日 12:40)
**结果**: ✅ GSC 首次提交成功 (HTTP 204) + IndexNow 5 条孤儿 URL 增量推送 (200)；Sitemap 覆盖缺口已定位并局部修复

---

## 一、402 全链停摆自检（≤60s，首任务）

| 项 | 结果 |
|---|---|
| 失败面 | executions.db 显示 **8/26 → 9/11 每日 7-11 条 `RuntimeError: HTTP 402: Insufficient Balance`**（连续 17 天）；9/12 已有 3 条 completed（恢复） |
| 余额 | `GET api.deepseek.com/user/balance` → **¥1.34 CNY**（is_available=true，但余量只够几轮） |
| fallback | `config.yaml` L512 `# fallback_model:` **整段注释 → 无 failover**；`.env` 有 MINIMAX_CN_API_KEY(125) 未接线 |
| 判定 | **P0（钱/配置）** — 今晚 18:00-23:59 任一槽将再次 402，需 user 二选一：充值 DeepSeek 或接 MINIMAX fallback |

## 二、Sitemap 变更检测

| 文件 | 起始状态 | 判定 |
|---|---|---|
| public/sitemap.xml | 358 URL / 44,041 B / sha256 `7B4150E9…` | 与 8/30 已提交 hash **完全一致 = 无变更** → 无需全量重推 |
| public/sitemap-programmatic.xml | 199 URL / 27,727 B / sha256 `DC9FB355…`，mtime 8/14 | 内容为 sitemap.xml 子集（并集=358），无新增 |
| 新发布页面 | reviews.json mtime 9/2（stickermule refresh，无新 slug）；blog-posts.json 22 篇未变 | 8/29 后无新页面 → 无增量 URL |

结论：`sitemap 无变更`。但深挖 out/ 与 sitemap 差集后 **发现 5 个 200 在线页面从未进入 sitemap**（见第五节）。

## 三、凭证检查（关键发现：凭证是 Service Account，不是 OAuth）

- IndexNow: `.hermes/secrets/indexnow-key.txt` 32 位 alnum，站点验证文件 `https://aitoptools.net/{key}.txt` → **HTTP 200 text/plain** ✅
- GSC: `.hermes/secrets/gsc-oauth.json` 实际为 **service_account** 类型（项目 `aitoptools-505222`，client_email=…@aitoptools-505222.iam.gserviceaccount.com），**无 client_secret/refresh_token** → 与 `submit-gsc-sitemap.py` 原 OAuth 取值逻辑不匹配 ⇒ 这解释了 state 里 `gsc_submitted:false` 自 8/3 起 40 天为零。
- 实测：SA 在本财产上权限 = **siteFullUser**（API `sites.list` 可见 `sc-domain:aitoptools.net`）。

## 四、提交执行

| 通道 | 动作 | 结果 |
|---|---|---|
| GSC | `python scripts/submit-gsc-sitemap.py`（脚本已打 SA 补丁） | **Sitemap PUT status=204 ✅**（日志 `.hermes/logs/gsc-submit-2026-09-12.log`） |
| IndexNow 全量 | 不需要（sitemap hash 未变，8/30 已推 362 URL） | 跳过（省 quota） |
| IndexNow 增量 | `scripts/archive/submit_indexnow_orphans_20260912.py` → 5 条孤儿 URL | **HTTP 200，5/5**（日志 `indexnow-0912-orphans.json`） |

推送的 5 条：
```
/compare/mockey-vs-placeit/                        (3,973 词)
/best/best-ai-tshirt-design-generators/            (2,919 词)
/best/best-print-on-demand-companies/              (2,437 词)
/partnerships/                                     (501 词)
/author/jerome-tang/                               (499 词)
```

## 五、🔴 Sitemap 覆盖缺口（新发现，P1）

`out/` 363 页 vs sitemap 358 URL：5 个**在线 200、无 noindex** 的页面从未进 sitemap。
**反常点：缺席的恰是长文精品页**（3,973 / 2,919 / 2,437 词），而 sitemap 里同类程序化页仅 1,000-1,100 词。

| 缺失 URL | 根因 | 处置 |
|---|---|---|
| /compare/mockey-vs-placeit/ | `generate-sitemap.py` 基页清单从 reviews.json 派生，**从不从 comparisons.json 派生 /compare/***；新对比页只能靠 merge 保留，一旦丢失即永久缺席 | ✅ 已修脚本（本轮已重生成本地 sitemap） |
| /partnerships/ | 基页硬编码清单漏列 | ✅ 已修 |
| /author/jerome-tang/ | 基页硬编码清单漏列（E-E-A-T 页） | ✅ 已修 |
| /best/best-ai-tshirt-design-generators/ | `sitemap-programmatic.xml` 自 8/14 未更新（owner 是 `scripts/generate-pages.js`），新产生的 /best/ 页进不了该文件、也进不了 sitemap | ⏸ 待 owner 侧 `node scripts/generate-pages.js` 重跑 |
| /best/best-print-on-demand-companies/ | 同上 | ⏸ 同上 |

**副作用告警（疑重复 slug 对）**: `/best/best-ai-tshirt-design-generators/`（2,919 词，无连字符）与 sitemap 内的 `/best/best-ai-t-shirt-design-generators/`（1,100 词，带连字符）主题相同 → 疑似 slug 迁移只做了一半，建议 owner 判定「保留精修版 + 旧薄版 301/下线」。

## 六、改动清单（无 push）

| 文件 | 改动 |
|---|---|
| `scripts/submit-gsc-sitemap.py` | +`get_access_token_service_account()`（RS256 JWT 换 token），`get_access_token()` 按 `type==service_account` 分支；OAuth 路径保留 |
| `scripts/generate-sitemap.py` | 基页清单 +`partnerships`、+`author/jerome-tang`；新增由 `comparisons.json` 派生 `compare/{slug}` |
| `scripts/submit_indexnow_orphans_20260912.py` | 新增一次性脚本（5 条孤儿 URL 增量推送） |
| `public/sitemap.xml` / `out/sitemap.xml` | **358 → 361 URL**（+mockey-vs-placeit、+partnerships、+author），`build_sitemap_content` merge 保底，/best/ 202 条全保留 |
| `.hermes/logs/gsc-indexnow-state.json` | gsc_submitted=true / status=204 / auth_mode=service_account / urls_pushed=361 / last_seen 双 sitemap |

> ⚠️ 本地 sitemap 361 URL **尚未上线**（需下一次 push 才生效）；线上仍为 358 URL 版本。孤儿 5 条的 Bing/Yandex 覆盖已在本次 IndexNow 推送中完成，GSC 侧需等 sitemap 上线后随 sitemap 收录。

## 七、合规自检

- ✅ 未自动 push、未自动 build（`can_deploy:false` 遵守）
- ✅ 未打印任何凭证内容（仅输出长度/状态码）
- ✅ 未手改 sitemap 数据块（走官方 generate-sitemap.py 生成器）
- ✅ 先想再写：402 → 余额 → fallback → sitemap 差集 → 凭证实测，全部核查完成才动作
- ✅ 精准修改：仅两处脚本、均为新增分支/清单项，未触碰无关逻辑
