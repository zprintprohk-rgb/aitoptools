# -*- coding: utf-8 -*-
"""R-14 异常源调查：git 提交者身份 + gateway 日志扫描"""
import subprocess, os, sys, re, time, glob
sys.stdout.reconfigure(errors='replace')
ROOT = r'F:\aitoptools'

def run(cmd, cwd=ROOT):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()

print('=== git authors of recent commits (8/14-8/16) ===')
out = run('git log --since=2026-08-14 --pretty=format:%h|%an|%ae|%ad|%s --date=format:%m-%d\\ %H:%M')
for line in out.splitlines():
    print(line[:170])
print()
print('=== all distinct authors ===')
print(run('git shortlog -sne --all | head -20'))
print()
print('=== gateway log locations ===')
cands = []
for base in [r'C:\Users\Administrator\.openclaw-autoclaw', r'C:\Users\Administrator\.openclaw-autoclaw\logs',
             r'C:\Users\Administrator\.openclaw-autoclaw\state', r'C:\Users\Administrator\.openclaw\logs']:
    if os.path.isdir(base):
        for f in os.listdir(base)[:30]:
            fp = os.path.join(base, f)
            if os.path.isfile(fp) and (f.endswith('.log') or 'log' in f.lower()):
                cands.append(fp)
print('\n'.join(cands[:20]) if cands else 'no log files found in candidate dirs')
print()
print('=== grep 178x invalid add / job created / restart markers ===')
for fp in cands[:6]:
    try:
        size = os.path.getsize(fp)
        if size > 30_000_000:
            print(f'skip {fp} ({size/1e6:.1f}MB)')
            continue
        c = open(fp, encoding='utf-8', errors='replace').read()
        for pat in ['cron: job created', 'invalid', 'past', 'gateway restart', 'restart']:
            n = len(re.findall(pat, c))
            if n:
                print(f'{os.path.basename(fp)} | {pat}: {n}')
    except Exception as e:
        print(fp, 'ERR', e)
