# -*- coding: utf-8 -*-
"""R-14 调查 v2：git 提交者 + 今日 gateway 日志 cron 痕迹"""
import subprocess, os, sys, re, time
sys.stdout.reconfigure(errors='replace')
ROOT = r'F:\aitoptools'

def run(cmd, cwd=ROOT):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()

print('=== git log 8/14+ (hash|author|date) ===')
out = run('git log --since=2026-08-14 --pretty=format:%h%%7c%an%%7c%ad%%7c%s --date=short')
for line in out.splitlines():
    print(line[:170])
print('distinct authors (all):')
print(run('git log --pretty=format:%an | sort | uniq -c | sort -rn')[:600])
print()
print('=== today log file cron lines ===')
logdir = r'C:\Users\Administrator\.openclaw-autoclaw\logs'
today = os.path.join(logdir, 'agent-im-api-20260816.log')
if os.path.exists(today):
    c = open(today, encoding='utf-8', errors='replace').read()
    print('size:', len(c))
    for pat in ['cron', 'job', 'created', 'add', 'restart', 'error', '402']:
        n = len(re.findall(pat, c, re.I))
        print(f'  {pat}: {n}')
    # 找 cron 相关行
    lines = [l for l in c.splitlines() if 'cron' in l.lower() or 'job' in l.lower()]
    print('cron/job lines:', len(lines))
    for l in lines[:40]:
        print('  ', l[:180])
else:
    print('no today log')
print()
print('=== yesterday log tail cron lines ===')
y = os.path.join(logdir, 'agent-im-api-20260815.log')
if os.path.exists(y):
    c = open(y, encoding='utf-8', errors='replace').read()
    lines = [l for l in c.splitlines() if 'cron' in l.lower()]
    print('cron lines 8/15:', len(lines))
    for l in lines[-30:]:
        print('  ', l[:180])
