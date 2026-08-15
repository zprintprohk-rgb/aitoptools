# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(errors='replace')
path = r'C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json'
d = json.load(open(path, encoding='utf-8'))
jobs = d['jobs']
print('TOTAL', len(jobs))
for j in jobs:
    if '11524761611778' in j['id'] or '8/16' in (j.get('name') or '') or 'B 类快修' in (j.get('name') or '') or '合并 push' in (j.get('name') or ''):
        print('FOUND:', j['id'], '|', j.get('agentId'), '| enabled:', j.get('enabled'),
              '| deleteAfterRun:', j.get('deleteAfterRun'),
              '|', (j.get('name') or '')[:50],
              '|', json.dumps(j.get('schedule'), ensure_ascii=False)[:80])
print('--- disabled main jobs ---')
for j in jobs:
    if (j.get('agentId') or '') == 'main' and not j.get('enabled', True):
        print('DISABLED:', j['id'][:8], '|', (j.get('name') or '')[:60])
print('--- de9fad65 (old W1-0816) ---')
for j in jobs:
    if 'de9fad65' in j['id']:
        print(j['id'], '| enabled:', j.get('enabled'), '| state:', json.dumps(j.get('state', {}), ensure_ascii=False)[:120])
