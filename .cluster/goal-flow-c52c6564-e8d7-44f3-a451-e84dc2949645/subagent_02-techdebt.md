# subagent_02 — generate-sitemap.py 技术债审计报告

- 角色: 技术债审计员（代码审计视角）
- 日期: 2026-08-15 20:28 CST
- 范围: 只读生产 + 沙盒验证；**未修改任何生产文件、未执行 git 操作、未联网**
- 任务来源: PHASE 路线图 T2（8/16 修复 generate-sitemap.py 重复追加 bug + 单测，断言 URL 数=342 且无重复）

---

## 一、根因定位（8/14 事故: sitemap 541 条 / 唯一 342 条）

### 1.1 事故链（已在沙盒单测 T3 精确复现）

sitemap 由**两个脚本接力维护**：

| 脚本 | 职责 | 幂等机制 |
|---|---|---|
| `scripts/generate-sitemap.py`（合并保底模式） | 重生成 133 条自有 URL ∪ 保留未知 URL | 按 `<loc>` 精确字符串去重 |
| `scripts/generate-pages.js`（L351-358） | 把 199 条 `/best/` 程序化页追加进 sitemap | 用正则删除旧块再追加: `main.replace(/  <!-- PROGRAMMATIC-SEO-START -->[\s\S]*?<!-- PROGRAMMATIC-SEO-END -->\n/, '')` |

**根因**: `generate-sitemap.py` 的合并解析用原始字符串切分，**丢弃了 `<url>` 块之间的所有内容——包括 generate-pages.js 幂等所依赖的 PROGRAMMATIC-SEO 注释标记**。标记一旦丢失，generate-pages.js 的正则匹配失败（JS 的 replace 无匹配 = no-op），于是直接追加一份新的 199 条 → 342 + 199 = **541**。

事故链（generate-sitemap.py 现行代码）:
1. `scripts/generate-pages.js` 写入 `<!-- PROGRAMMATIC-SEO-START -->…199 条…<!-- PROGRAMMATIC-SEO-END -->` → 342 条（含标记）
2. `generate-sitemap.py` 合并 → **标记被剥掉**（只保留 `<url>` 块）→ 342 条、无标记 ← 8/14 05:38 恢复后的当前状态即此
3. `generate-pages.js` 再次运行 → 正则找不到标记 → **直接追加 199 条** → 541 条 ← 8/14 04:52 产物
4. 每循环一次 +199，且 **generate-sitemap.py 自身无防御**（精确字符串去重对"同一 URL 出现两次"虽能修，但事故发生在 generate-pages.js 追加之后、下次 generate-sitemap.py 之前，去重永远轮不到执行）

### 1.2 现行代码缺陷定位（scripts/generate-sitemap.py）

| 行号 | 代码 | 缺陷 |
|---|---|---|
| L92-96 | `for block in content.split('<url>')[1:]: block = '<url>' + block.split('</url>')[0] + '</url>' …` | 按 `<url>` 切分，块与块之间的注释标记被**静默丢弃**（生成文件不含 `<!-- PROGRAMMATIC-SEO-START/END -->`，generate-pages.js 幂等正则失效）→ **8/14 541 事故主因** |
| L98 | `seen = set(new_urls)` | 仅对"已有"块去重；`new_urls` 自身不去重——数据源（reviews.json/blog-posts.json）一旦出现重复 slug 或 slug 碰撞，输出即含重复 URL（潜在 bug，T5 已补防御） |
| L98-101 | `if loc not in seen:` | 去重为**精确字符串**比较：`&amp;` 转义、尾斜杠缺失等格式差异可绕过去重（潜在 bug，已补规范化） |
| L109 | `f.write('\n'.join(merged_lines) + '\n')` | 本身无缺陷；但合并结果无标记 → 与 L92 缺陷联动 |

**generate-pages.js 侧约束**（修复必须遵守）: L355 的正则要求 START 标记行前缀**恰好两个空格**、块后紧跟换行——任何缩进/格式漂移都会让正则失配，重新触发 541。

### 1.3 数据核实（无重复 slug，当前脚本幂等性 OK 的唯一原因）

- reviews.json: 107 项 / 107 slug / 重复 0
- blog-posts.json: 10 篇 / 10 slug / 重复 0；无 slug 与固定页/分类/blog 索引碰撞
- 当前 sitemap 342 条 = 133 新增 + 209 保留（199 程序化 + 7 compare/best-ai-tools + 3 条 /best/ 附加页），脚本自身合并模拟结果 = 342 ✓（说明 8/14 恢复后文件是"合并模式"产物，**标记缺失状态会永久存在**，541 复发只是时间问题——8/16 修复前 generate-pages.js 绝不可再运行）

---

## 二、当前 sitemap 状态统计（2026-08-15 20:30 实测）

| 文件 | total | unique | 重复项 | lastmod | /blog/ 条目 | 大小/时间 |
|---|---|---|---|---|---|---|
| `public/sitemap.xml` | **342** | **342** | 0 | 无（全站 0 条） | 11（10 文 + 1 索引） | 42305 B / 08-14 05:38 |
| `out/sitemap.xml` | **342** | **342** | 0 | 无 | 11 | 42305 B / 08-14 05:38 |
| `public/sitemap-programmatic.xml` | 199 | 199 | 0 | 无 | — | 27727 B / 08-14 04:52 |

- `src/data/blog-posts.json` 数组长度 = **10**（10/10 有 slug）；sitemap /blog/ = 10 文章 + 1 索引 = 11 ✓ 对账一致
- sitemap.xml 与 sitemap-programmatic.xml 的 199 条完全重合（199/199），另 3 条 /best/（`/best/`、`/best/printful-alternatives/`、`/best/printify-alternatives/`，priority 0.9）**不属于** generate-pages.js 管辖，修复时必须留在标记块外
- 8/14 日志佐证: daily-search-2026-08-14.md L24-28（"541 条但唯一仅 342 — 199 条 /best/ 页被重复追加…恢复 HEAD 版本 342 条 sha256 58E31E"）

---

## 三、最小修复补丁

### 3.1 修复策略（3 层防御，最小改动面）

1. **保留 + 治愈标记块**（主修复）:
   - 正则提取现有 `<!-- PROGRAMMATIC-SEO-START -->…<!-- PROGRAMMATIC-SEO-END -->` 块，原样保留（`strip('\n')` 只剥换行、**保留两空格缩进**——generate-pages.js 正依赖它）
   - 标记缺失时（当前状态）→ 按 `public/sitemap-programmatic.xml` 的 loc 集合识别 199 条程序化条目（文件缺失时回退签名 `/best/` + `priority 0.7`），**重新包进标记块**——一次运行即治愈现状
   - 非程序化的 7 条 compare/best-ai-tools 与 3 条 /best/ 附加页继续按单块保留（避免被 generate-pages.js 的正则误删）
2. **规范化去重**: `_norm_loc()`（strip / `&amp;` 反转义 / 补尾斜杠），覆盖 new + existing + programmatic 三源；`new_urls` 自身先去重（防数据源 slug 碰撞）
3. **可测试性**: `--project-dir` 参数 + stdout 编码容错（GBK 控制台打印 ✓ 会崩，原脚本同隐患）

### 3.2 产物

- **补丁**: `.cluster/goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645/sitemap_fix.patch`（unified diff，4 hunks / 268 行）
  - hunk1: `@@ -3,21 +3,172 @@` 文档 + imports + 新增 `PROGRAMMATIC_RE` / `_norm_loc` / `_parse_blocks` / `_load_programmatic_locs` / `_extract_programmatic_block` / `_is_programmatic_block` / `build_sitemap_content`
  - hunk2: `@@ -25,7 +176,7 @@` blog 加载块 `PROJECT_DIR` → `root`（支持 --project-dir）
  - hunk3: `@@ -64,51 +215,27 @@` main() 合并写循环整体替换（标记保留/治愈 + 规范化去重 + 真实 URL 计数）
  - hunk4: `@@ -120,12 +247,12 @@` robots 块 + 收尾打印
- **修复后脚本副本**: `generate-sitemap_fixed.py`（9967 B / 9815 字符）
- **补丁可应用性验证**: 4 个 hunk 的偏移/行数/上下文内容与原文件逐一比对全部吻合；倒序应用后与修复版**逐字节一致**（9815 == 9815 字符，UTF-8 字节一致）
- 生产文件 `scripts/generate-sitemap.py` **未改动**

---

## 四、单测结果（真实输出，20/20 PASS）

测试文件: `.cluster/goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645/sitemap_fix_test.py`
（非破坏性: 时间戳唯一沙盒目录，无任何删除 API；生产文件只读；修复脚本以 `--project-dir` 指向沙盒端到端运行，无网络）

```
T1: fixed script on current (markerless restored) state
  [PASS] T1 exit 0 rc=0
  [PASS] T1 public total==342 total=342
  [PASS] T1 public unique==342 unique=342
  [PASS] T1 public no dups dups=[]
  [PASS] T1 out matches public out=(342,342,[])
  [PASS] T1 markers restored
  [PASS] T1 /best/ count==202 count=202
T2: consecutive second run
  [PASS] T2 exit 0 rc=0
  [PASS] T2 byte-identical (no re-append) len1=42026 len2=42026
T3: 8/14 failure reproduction -> self-heal
  [PASS] T3 precond broken==541 broken state total=541 unique=342
  [PASS] T3 exit 0 rc=0
  [PASS] T3 healed to 342 unique total=342 unique=342
  [PASS] T3 no dups dups=[]
  [PASS] T3 markers restored
T4: full cycle (generate-pages.js append on healed file) -> stays 342
  [PASS] T4 precond cycle==342 total=342 unique=342
  [PASS] T4 exit 0 rc=0
  [PASS] T4 stays 342 unique, no dups total=342 unique=342 dups=[]
  [PASS] T4 markers preserved
T5: regression — dup slug + review/blog slug collision
  [PASS] T5 exit 0 rc=0
  [PASS] T5 no duplicate URLs despite poisoned data total=343 unique=343 dups=[]
SUMMARY: 20/20 passed
```

验收对照（PHASE §9: 断言 URL 数=342 且无重复）:
- ✅ 342 条且无重复（T1/T3/T4）
- ✅ 连续运行两次不产生重复追加，输出逐字节一致（T2，42026 B 两次相同）
- ✅ 8/14 事故精确复现（541/342）并被修复版自愈回 342（T3）
- ✅ generate-pages.js 完整循环后仍 342、标记保留（T4）——541 复发机制已被根治
- ✅ 数据源污染（重复 slug、固定页碰撞）不再产生重复 URL（T5）；343 = 342 + 1 合法 URL `blog/blog/`（blog 索引 `blog/` 与文章 slug `blog` 是不同 URL，非重复）
- 修复过程中额外发现并修复: ① 标记块 `.strip()` 会剥掉两空格缩进导致 generate-pages.js 正则失配（verbatim 路径二次运行时）——已改为 `strip('\n')`；② 合并输出 URL 计数打印不实（标记块含内嵌换行）——已改为真实 `<url>` 计数

---

## 五、调用方清单（谁在跑 generate-sitemap.py / 消费 sitemap）

| # | 调用方 | 触发 | 证据 | 状态 |
|---|---|---|---|---|
| 1 | Hermes aitoptools-daily-content（MiniMax app） | 13:30 cron | `.hermes/logs/2026-08-09-cron.md` L29-33: `python scripts/generate-sitemap.py` → validate → `npm run build` → IndexNow + C2b | 并存期（AGENTS.md: 8/12 切换检查后建议停用） |
| 2 | AutoClaw cron「每日搜索增长」(daily-search 19:23) | 19:23 cron | `.hermes/logs/daily-search-2026-08-14.md` L24-28（8/14 04:52 "重新生成产物 541" 即此管线）; daily-search-2026-08-15.md 核验 sha58E31E | **PHASE §9: 修复通过前 sitemap 操作一律人工确认，通过后 cron 恢复自动调用** |
| 3 | `scripts/generate-pages.js`（共犯，非直接调用者） | 程序化页重建（Step 2-3-4 管线） | 自身头部注释 + L351-358 追加逻辑 | **修复落地前禁止运行**（当前文件无标记，一跑即 541） |
| 4 | 发布流程（人工/操作员） | 每篇 Blog 上线后 | AGENTS.md「sitemap 变更即推铁律」: 重跑 generate-sitemap.py + IndexNow 增量推送 | 8/16 修复后照常 |
| 5 | `scripts/submit-indexnow.py` / `submit_indexnow_full_20260806.py` / `submit_indexnow_blog_20260808.py` | 下游消费 | 读取 `out/sitemap.xml` 提取 `<loc>` | 只读，无风险 |
| 6 | `scripts/submit-gsc-sitemap.py` / `scripts/verify-deploy-v2.py` | 下游消费 | 读取 `out/sitemap.xml` | 只读，无风险 |

注: Hermes cron jobs.json（5 个任务）中无 generate-sitemap 直接引用；AutoClaw cron 配置目录未发现显式命令串（由 cron prompt 引导执行层调用），故以日志实证为准。

---

## 六、产物与注意事项

**交付物**（均在 `.cluster/goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645/`）:
- `sitemap_fix.patch` — unified diff（4 hunks，已验证可干净应用）
- `generate-sitemap_fixed.py` — 修复后脚本完整副本
- `sitemap_fix_test.py` — 单测（20/20 PASS，可重复运行）
- `subagent_02-techdebt.md` — 本报告

**辅助/临时**（可清理）: `analyze_sitemap.py` / `probe_rootcause.py` / `probe_preserved.py` / `dbg_idempotent.py` / `dbg/` `dbg2/` `test_sandbox/`（沙盒副本与捕获文件，均在 goal-flow 目录内，未触碰生产）

**上线建议**（交主控/8/16 T2 执行）:
1. `git apply sitemap_fix.patch` 或整文件替换（先 diff 复核）
2. 沙盒外再跑一次 `python scripts/generate-sitemap.py` → 断言 public/ 与 out/ 均 342 条、无重复、含 PROGRAMMATIC-SEO 标记（验收命令见 analyze_sitemap.py）
3. 修复后**首次**运行会治愈标记（342 → 342，内容微变：标记块恢复）；此后 generate-pages.js 可安全运行
4. 未跑单测前勿让任何 cron 自动调用 generate-pages.js

**已确认非问题**: sitemap 无 lastmod（全站 0 条）——不影响本次修复；`&amp;` 反转义为去重规范化，不改写任何 URL 实体。
