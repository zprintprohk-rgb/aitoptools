# -*- coding: utf-8 -*-
"""402 与 restart 时间点确认 + 单测最终验证"""
import re, sys, os, subprocess, datetime
sys.stdout.reconfigure(errors='replace')
logdir = r'C:\Users\Administrator\.openclaw-autoclaw\logs'
today = os.path.join(logdir, 'agent-im-api-20260816.log')
c = open(today, encoding='utf-8', errors='replace').read()
lines = c.splitlines()

print('=== 402 lines with timestamps ===')
for l in lines:
    if '402' in l:
        print(l[:220])
print()
print('=== restart lines ===')
for l in lines:
    if 'restart' in l.lower():
        print(l[:180])
print()
print('=== file head (format sample) ===')
for l in lines[:5]:
    print(l[:160])
