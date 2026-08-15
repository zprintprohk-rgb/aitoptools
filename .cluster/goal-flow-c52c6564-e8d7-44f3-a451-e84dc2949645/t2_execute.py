# -*- coding: utf-8 -*-
"""T2 执行：备份 -> 替换 -> 一致性校验 -> 实跑 -> 验证（用户 8/16 05:21 授权现在执行）"""
import os, sys, shutil, hashlib, py_compile, subprocess, re, json
sys.stdout.reconfigure(errors='replace')
ROOT = r'F:\aitoptools'
WB = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645'
PROD = os.path.join(ROOT, 'scripts', 'generate-sitemap.py')
MERGED = os.path.join(WB, 'DELIVERY', 'generate-sitemap_merged.py')
BAK = os.path.join(WB, 'backup_generate-sitemap_preT2.py')

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]

def run(cmd, cwd=ROOT):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or ''), (r.stderr or '')

print('=== 1. 备份 ===')
shutil.copy2(PROD, BAK)
print('backup ->', BAK, os.path.getsize(BAK), 'B | sha256:', sha(BAK))
print('prod before:', os.path.getsize(PROD), 'B | sha256:', sha(PROD))
print('merged     :', os.path.getsize(MERGED), 'B | sha256:', sha(MERGED))

print()
print('=== 2. 替换 ===')
shutil.copy2(MERGED, PROD)
print('prod after :', os.path.getsize(PROD), 'B | sha256:', sha(PROD))
print('identical  :', sha(PROD) == sha(MERGED))
py_compile.compile(PROD, doraise=True)
print('py_compile OK')

print()
print('=== 3. robots 替换前内容快照对比准备 ===')
for sub in ['public', 'out']:
    p = os.path.join(ROOT, sub, 'robots.txt')
    c = open(p, encoding='utf-8').read()
    agents = [a for a in ['Applebot-Extended', 'Amazonbot', 'meta-externalagent', 'cohere-ai', 'GPTBot', 'PerplexityBot', 'Google-Extended'] if a in c]
    print(f'{sub}/robots.txt agents pre-run: {len(agents)} -> {agents}')

print()
print('=== 4. 实跑生产脚本 ===')
rc, out, err = run('python scripts/generate-sitemap.py')
print('rc =', rc)
print(out[-800:])
if err:
    print('STDERR:', err[-500:])
