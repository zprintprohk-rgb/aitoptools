# -*- coding: utf-8 -*-
"""Build generate-sitemap_merged.py = fixed(修复逻辑) + 生产版 robots 4 代理 + heal 去重修正。

来源：
- base: generate-sitemap_fixed.py（subagent_02 修复版，含标记治愈/规范化去重/--project-dir/真实计数/stdout 容错）
- 合并入: 当前生产版 robots 模板（Applebot-Extended/Amazonbot/meta-externalagent/cohere-ai，外部进程 20:45 已并入生产）
- 顺手修复: 复核员 review-code.md #5 —— heal 路径 prog_blocks 内部按 loc 去重（防 542-markerless 边缘残留 199 dups）
"""
import re

fixed = open(r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\generate-sitemap_fixed.py', encoding='utf-8').read()

# --- 1. robots 模板替换为生产版（含 4 个 AI 爬虫代理）---
prod_robots = (
    "# Explicitly welcome AI crawlers — this site's content is meant to be cited.\n"
    'User-agent: GPTBot\nAllow: /\n\n'
    'User-agent: ClaudeBot\nAllow: /\n\n'
    'User-agent: PerplexityBot\nAllow: /\n\n'
    'User-agent: Google-Extended\nAllow: /\n\n'
    'User-agent: Applebot-Extended\nAllow: /\n\n'
    'User-agent: Amazonbot\nAllow: /\n\n'
    'User-agent: meta-externalagent\nAllow: /\n\n'
    'User-agent: cohere-ai\nAllow: /\n\n'
    f'User-agent: *\nAllow: /\nSitemap: {fixed[fixed.index("DOMAIN") and 0:0] or "https://aitoptools.net"}/sitemap.xml\n'
)
# 上面表达式过于花哨，直接写死 DOMAIN 拼接
prod_robots = (
    "# Explicitly welcome AI crawlers — this site's content is meant to be cited.\n"
    'User-agent: GPTBot\nAllow: /\n\n'
    'User-agent: ClaudeBot\nAllow: /\n\n'
    'User-agent: PerplexityBot\nAllow: /\n\n'
    'User-agent: Google-Extended\nAllow: /\n\n'
    'User-agent: Applebot-Extended\nAllow: /\n\n'
    'User-agent: Amazonbot\nAllow: /\n\n'
    'User-agent: meta-externalagent\nAllow: /\n\n'
    'User-agent: cohere-ai\nAllow: /\n\n'
    'User-agent: *\nAllow: /\nSitemap: https://aitoptools.net/sitemap.xml\n'
)

old_robots_start = fixed.index('    robots = (')
old_robots_end = fixed.index("    for subdir in ('public', 'out'):\n        robots_path", old_robots_start)
# 每行转成带引号的 Python 字符串字面量（隐式拼接）
body = '\n'.join('        ' + repr(l + '\n') for l in prod_robots.splitlines())
merged = fixed[:old_robots_start] + '    robots = (\n' + body + '\n    )\n' + fixed[old_robots_end:]

# --- 2. heal 路径去重修正（review-code.md #5）---
old_heal = """        healed = ['  <!-- PROGRAMMATIC-SEO-START -->']
        healed.extend('  ' + b for loc, b in prog_blocks if loc not in seen_new)
        healed.append('  <!-- PROGRAMMATIC-SEO-END -->')
        merged.append('\\n'.join(healed))"""
new_heal = """        healed = ['  <!-- PROGRAMMATIC-SEO-START -->']
        healed_locs = set(seen_new)
        for loc, b in prog_blocks:
            if loc not in healed_locs:  # dedupe inside prog_blocks too (edge: 542-markerless)
                healed.append('  ' + b)
                healed_locs.add(loc)
        healed.append('  <!-- PROGRAMMATIC-SEO-END -->')
        merged.append('\\n'.join(healed))"""
assert old_heal in merged, 'heal 段未找到'
merged = merged.replace(old_heal, new_heal)

# --- 3. 版本注释更新 ---
merged = merged.replace('FIX 2026-08-16 (tech-debt audit, see subagent_02-techdebt.md):',
                        'FIX 2026-08-16 v2 (tech-debt audit + code review, see review-code.md):\n'
                        '- v2 = 修复版 + 生产 robots 4 AI 代理(Applebot-Extended/Amazonbot/meta-externalagent/cohere-ai) 合并\n'
                        '- v2 = heal 路径 prog_blocks 内部按 loc 去重（542-markerless 边缘）')

out = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\generate-sitemap_merged.py'
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write(merged)
print('written:', out, len(merged), 'chars')
# 验证 robots 4 代理都在
for a in ['Applebot-Extended', 'Amazonbot', 'meta-externalagent', 'cohere-ai']:
    print(a, '->', a in merged)
# 语法检查
import py_compile
py_compile.compile(out, doraise=True)
print('py_compile OK')
