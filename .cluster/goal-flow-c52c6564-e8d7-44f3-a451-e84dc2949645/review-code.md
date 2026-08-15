# review-code.md — 代码复核员独立验证报告（反方视角）

- 角色: 代码复核员（subagent_05，独立重跑全部断言，不信任自报结果）
- 日期: 2026-08-15 20:43–20:50 CST
- 范围: 只读生产 + 沙盒写；未修改任何生产文件、未 git 操作、未联网
- 复核对象: subagent_02-techdebt.md 全部断言 + sitemap_fix.patch / generate-sitemap_fixed.py / sitemap_fix_test.py

---

## 总结论: **需修正（不能按现状合入）**

审计员对**根因的分析完全正确**，修复方案逻辑本身经独立验证**有效**（343 条无重复、标记恢复、幂等），但存在 **4 个阻断性交付问题**：

1. **补丁文件行尾为 CRLF，`git apply` 直接失败**（--ignore-whitespace 亦失败）；LF 归一化后可干净应用 → 审计员"可干净应用"断言对交付物本身不成立。
2. **生产文件已与补丁基线（HEAD）分叉**：20:45:43 外部进程对 `scripts/generate-sitemap.py` 做了部分修改（+10/-2：new_urls 自身去重 + robots 模板新增 4 个 AI 爬虫代理），补丁 hunk 3/4 上下文失配，**对当前生产应用失败**。
3. **单测重跑为 14/20 而非 20/20**：blog-posts.json 在审计后 20:44:56 新增第 11 篇（kittl-halloween-template-test-2026），基数由 342 → 343，6 个失败全部是硬编码计数断言（342 vs 343），逻辑断言全部通过。审计员 20/20 在其运行时刻成立，但测试对数据漂移脆弱。
4. **修复版 robots 模板为旧版**（无 Applebot-Extended / Amazonbot / meta-externalagent / cohere-ai），直接运行会覆盖生产 robots.txt、丢失未提交的 4 个代理条目。

---

## 复核项逐项结果

### 1. 生产文件未被修改 — **FAIL（复核时点已被外部修改）**

| 断言 | 结果 | 证据 |
|---|---|---|
| `git status --short scripts/` 为空 | FAIL | 20:43 首查时仅 5 个 untracked 无关文件；**20:49 复查出现 `M scripts/generate-sitemap.py`** |
| `git diff --stat scripts/generate-sitemap.py` 为空 | FAIL | 20:49: `1 file changed, 10 insertions(+), 2 deletions(-)` |
| 文件 SHA256 | 变化 | 20:44: `1c95f815...` → 20:49: `6f76c024...` |

**时间线**（mtime 证据）:
- 20:43:40 首查：clean（审计员窗口 20:28–20:39 确实未改生产，其断言当时成立）
- **20:45:43 `scripts/generate-sitemap.py` mtime 更新**（外部进程；改动内容=部分修复：new_urls 自去重 + robots 模板 4 代理，**未含标记修复**）
- 20:45:56 public/out/sitemap.xml + robots.txt 被重新生成（343 条、仍无标记）
- 20:47–20:50 我的全部操作：仅沙盒写入 + repo 内 `git apply --check`（check-only，exit 1，无写）；复查 mtime 确认 20:45:56 后生产零变更 → **非本次复核导致**

**关键影响**: 补丁基于 HEAD 生成，当前生产已分叉 → 补丁无法直接合入（见第 2 项）。另注意：外部部分修复**没有修复根因**（标记仍被剥除，20:45:56 产物即证据），541/542 复发风险依旧活跃。

### 2. 补丁可干净应用 — **FAIL（as-delivered）／内容本身正确**

| 子项 | 结果 | 证据 |
|---|---|---|
| 原补丁 `git apply --check`（沙盒） | FAIL | `patch does not apply`，报错上下文行尾含 `?` = CR 字符 |
| 原补丁 `git apply --check --ignore-whitespace` | FAIL | 同样失败 |
| 原补丁 `git apply --check`（真实 repo 根，check-only） | FAIL | `scripts/generate-sitemap.py: patch does not apply` |
| 字节检查 | 行尾问题 | 补丁 268 行全 CRLF；生产文件 140 行全 LF（`i/lf w/lf`，无 eol 属性） |
| CRLF→LF 归一化后应用（对 HEAD 副本） | PASS | 4 个 hunk 全部命中：`@@ -3,21 +3,172 @@` / `-25,7 +176,7` / `-64,51 +215,27` / `-120,12 +247,12` |
| 应用结果 vs generate-sitemap_fixed.py | PASS | EOL 归一化后**逐字节一致**（9967 == 9967 B；git apply 受全局 autocrlf=true 影响输出 CRLF，内容一致） |
| 对**当前生产**文件应用（LF 补丁） | FAIL | `patch failed: ...:64`（hunk 3 上下文失配：生产该处已被改为去重循环；hunk 4 robots 上下文同样失配） |

### 3. 单测独立重跑 — **FAIL（14/20，非 20/20）**

命令: `python sitemap_fix_test.py`（goal-flow 目录运行，其沙盒在 `test_sandbox/<时间戳>/`）
真实输出摘录:

```
T1: [PASS] exit 0 | [FAIL] total==342 total=343 | [FAIL] unique==342 unique=343
    [PASS] no dups | [PASS] markers restored | [PASS] /best/ count==202
T2: [PASS] byte-identical (no re-append) len1=42145 len2=42145
T3: [FAIL] precond broken==541 → total=542 unique=343 | [PASS] exit 0
    [FAIL] healed to 342 → total=343 unique=343 | [PASS] no dups | [PASS] markers restored
T4: [FAIL] precond cycle==342 → 343 | [FAIL] stays 342 → 343 | [PASS] markers preserved
T5: [PASS] no duplicate URLs despite poisoned data (344/344, 无重复)
SUMMARY: 14/20 passed
```

**失败原因（独立查证）**: `blog-posts.json` mtime 20:44:56（审计 20/20 之后）新增第 11 篇 `kittl-halloween-template-test-2026` → 脚本生成基数 134（107 评测+9 静态+6 分类+1 blog 索引+11 博客），342 断言全部 +1。6 个失败**全部是硬编码计数断言**；所有逻辑不变量（无重复、标记恢复、二次运行字节一致、自愈后 unique==total、标记保留）均 PASS。→ 修复逻辑在**当前数据**下独立验证为正确（见证据：livecheck 343/343/0、标记 (True,True)、/best/=202）。

**测试脚本卫生检查**:
- 写操作仅限 `HERE/test_sandbox/<时间戳>/`（沙盒区，mtime 证实）；生产文件只读（shutil.copy2 从 ROOT 复制）
- imports = json/os/re/shutil/subprocess/sys/time/xml.etree → **无 requests/urllib/socket，无联网**
- 子进程调用仅 `python generate-sitemap_fixed.py --project-dir <沙盒>` → 不触生产
- 缺陷：`prog_urls()` 硬断言 199、T1/T3/T4 硬编码 342/541 → 数据漂移即红

### 4. 根因推理验证 — **PASS**

| 断言 | 对照代码 | 结果 |
|---|---|---|
| generate-sitemap.py 合并按 `<url>` 切分、丢弃块间内容（含标记） | 生产 L92-96: `for block in content.split('<url>')[1:]: block = '<url>' + block.split('</url>')[0] + '</url>'` | ✅ 一致 |
| generate-pages.js 幂等正则依赖标记 + 两空格缩进 | 生产 L355: `main.replace(/  <!-- PROGRAMMATIC-SEO-START -->[\s\S]*?<!-- PROGRAMMATIC-SEO-END -->\n/, '')` | ✅ 一致（L351-358 区间内） |
| 标记缺失 → replace no-op → 追加 199 → 342+199=541 | 已在沙盒复现（当前基数下 343+199=542，机制相同） | ✅ 一致 |
| 审计员"8/14 恢复后文件无标记会永久存在" | 20:45:56 新产物仍无标记（`markers=(False,False)`） | ✅ 佐证 |

补充证据: 修复版对当前生产状态（343 无标记）运行 → 343/343/0、标记 (True,True)、/best/=202，且 **343 个 `<url>` 块与生产逐块内容 0 差异**（仅恢复标记 + 程序化块移至末尾）→ 修复行为与设计一致。

### 5. 当前 sitemap 状态独立核对 — **PASS（数字已更新）**

| 文件 | total | unique | 重复 | 标记 | /blog/ | 备注 |
|---|---|---|---|---|---|---|
| public/sitemap.xml | **343** | 343 | 0 | 无 | 12 | mtime 08-15 20:45:56（重新生成） |
| out/sitemap.xml | 343 | 343 | 0 | 无 | 12 | 与 public 一致 |
| public/sitemap-programmatic.xml | 199 | 199 | 0 | 无 | — | mtime 08-14 04:52 |

- 审计员 20:30 快照（342/342/0）当时正确；**20:45:56 重新生成后为 343**（新增第 11 篇博客）→ "无标记"断言仍成立
- 交叉核对: 数据生成 134 个新 URL，其中 0 个不在当前 sitemap（无缺失）、209 个保留条目（199 程序化 + 10 其他：7 compare/best-ai-tools + 3 条 priority 0.9 的 /best/ 附加页，均不在 programmatic 文件内，与审计员 §二 一致）
- **PHASE §9 验收数字 "342" 已过期**，应以 "unique==total、0 重复、标记恢复" 为验收标准

### 6. 风险补充评估

**a) 首次运行"治愈标记"对 8/16 T2 的影响** — 低风险，已验证:
- 343 → 343；loc 多重集与生产**完全一致**（0 差异块、无 & 实体、无 URL 增删改），仅恢复标记块 + 程序化块移到文件末尾
- 治愈后 generate-pages.js 的 strip+append 可安全运行（T4 机制在 343 基数下验证：标记保留）
- **但**: 若直接部署审计版修复脚本，其 robots 模板为旧版 → 首次运行覆盖 robots.txt 丢失 Applebot-Extended/Amazonbot/meta-externalagent/cohere-ai（当前生产 robots.txt 未提交但已含此 4 条；当前生产脚本模板已同步，修复版未同步）→ **必须把 4 个代理条目并入修复版模板再上线**

**b) &amp; 反转义** — PASS: `_norm_loc()` 中 `.replace('&amp;','&')` 仅用于去重比较（set/dict 键）；输出写回走原块 verbatim + 新 URL 原样拼接。实测修复版输出 343 个 `<loc>` 中 0 个含 `&`，与生产一致。

**c) 新发现的残留缺口（低概率）**: 542-**无标记**状态（旧脚本在 542 状态上再跑一次产生）下，修复版只恢复标记、**不去重**：独立探针结果 `POST fixed: total=542 unique=343 dups=199 markers=(True,True)`。原因: 治愈路径 `healed.extend('  ' + b for loc, b in prog_blocks if ...)` 对 prog_blocks 内部重复无 set 去重。当前生产（343 无标记）不受影响；修复落地后旧脚本不再运行，该状态不可达 → 建议顺手加去重（一行 set），不阻断。

**d) 统计打印误导（轻微）**: `+343 preserved` 实际统计了全部既有块（含将重新生成的 134 个新 URL），非真实保留数（209）。仅打印问题，不影响输出。

---

## 结论: **需修正** — 合入前必须处理的清单

| # | 问题 | 严重度 | 修正建议 |
|---|---|---|---|
| 1 | 补丁 CRLF 行尾，`git apply` 失败 | 阻断 | 交付前归一化 LF；或改为整文件替换（推荐，见 #2） |
| 2 | 生产文件已分叉（20:45:43 外部部分修复），补丁上下文失配 | 阻断 | 以 generate-sitemap_fixed.py 为基础手动合并：① 保留外部修复的 robots 模板 4 代理；② new_urls 去重在修复版 build_sitemap_content 已内置，外部改动可弃；③ 合并后对当前生产做 `git apply --check` 或 diff 复核 |
| 3 | 单测硬编码 342/541，数据漂移即红 | 阻断（验收口径） | 断言改为 unique==total 且无重复 + 标记恢复；计数期望改为与当前数据动态计算（134+209=343）或从生产 sitemap 读取基线 |
| 4 | 修复版 robots 模板缺 4 个 AI 爬虫代理 | 阻断（数据丢失风险） | 并入模板后再上线；上线首跑后 diff public/robots.txt 确认无损 |
| 5 | 治愈路径 prog_blocks 内部不去重（542-markerless 边缘） | 低 | heal 时按 loc 去重（一行修复） |
| 6 | PHASE §9 "342" 验收数字过期 | 低 | 更新为动态断言 |

## 风险提示（8/16 T2 执行前必读）

1. **修复落地前 `generate-pages.js` 绝不可再运行**: 当前生产 sitemap 无标记，一跑即 542（20:45:56 已再次确认无标记状态）。
2. **不要直接 `git apply sitemap_fix.patch`**: 双重失败（CRLF + 上下文分叉）。正确路径: 合并 #2 后整文件替换 → 沙盒跑单测（改后断言）→ 生产运行 → 验证 343/343/0 + 标记 + robots.txt 无损 → 再允许 generate-pages.js。
3. 外部进程在 20:45:43 修改了生产脚本（部分修复）且已运行产生 343 无标记 sitemap —— 该修改未提交（`M` 状态），合入时注意与补丁三方协调，勿互相覆盖。
4. 复核期间生产零写入（mtime 证据），全部验证在沙盒完成。

## 附录: 独立验证命令清单（可复现）

- `git -C F:\aitoptools status --short -- scripts/generate-sitemap.py` / `git diff --stat -- ...` / `git ls-files --eol -- ...`
- `git apply --check sitemap_fix.patch`（原样）与 LF 归一化版（沙盒 + repo check-only）
- `python sitemap_fix_test.py` → 14/20（原因: 数据漂移）
- 修复版对当前生产状态 livecheck（--project-dir 沙盒）→ 343/343/0、标记恢复、块级 0 差异
- 542-markerless 边缘探针（probe_edge542.py）→ 542/343/199dups 残留
- 生产解析: public/out sitemap 343/343/0 无标记；programmatic 199/199/0
