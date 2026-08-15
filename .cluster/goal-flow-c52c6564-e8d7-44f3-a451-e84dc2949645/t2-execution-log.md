# T2 执行留痕（2026-08-16 05:2x · 用户授权「现在执行」）

## 执行结果
- ✅ 备份：scripts/generate-sitemap.py（5150B, sha 6f76c024…）→ backup_generate-sitemap_preT2.py
- ✅ 替换：整文件覆盖为 merged 版（10738B, sha 2dc75ddf…），替换后 sha256 与 DELIVERY/generate-sitemap_merged.py 完全一致
- ✅ py_compile 通过
- ✅ 实跑 `python scripts/generate-sitemap.py` rc=0：public/out 均 343 URLs / 199 programmatic
- ✅ sitemap 验证：public 343/343/0 重复、out 343/343/0、标记恢复 (True,True)、标记缩进 2 空格（generate-pages.js 正则依赖）、/best/=202
- ✅ robots 无损：public/out 均 8 代理（Applebot-Extended/Amazonbot/meta-externalagent/cohere-ai/GPTBot/ClaudeBot/PerplexityBot/Google-Extended）+ Sitemap 行
- ✅ 单测回归 27/27 PASS（基线 343）

## 过程中发现并修复的问题（留痕）
1. 首次单测回归 rc=1：T3 precondition 断言「生产起始状态必须无标记」——T2 实跑治愈后生产已含标记，断言过期 → 修复 T3 自适应双状态（只剥标记注释行、保留 URL 块，精确复现 8/14 事故：无标记 343 + 追加 199 = 542 → 自愈 343）
2. 修复后单测 26/27（T3 构造把标记块整体删除导致 343-199+199=343 非 542）→ 二次修复为只剥注释行 → 27/27 PASS

## 07:15 cron 影响
- T2 幂等键「单测通过→NOOP」已满足：脚本已替换、sitemap 已治愈、单测 27/27
- cron 到点重跑脚本无副作用（幂等：343→343 字节一致，T2 单测已验证）
- 工作区改动待 T7 合并 push：M scripts/generate-sitemap.py + M public/sitemap.xml（+其他 T1/T3 改动）

## 回滚
- `git restore scripts/generate-sitemap.py`（旧版 5150B 在库基线）
- 或整文件恢复 backup_generate-sitemap_preT2.py
