# -*- coding: utf-8 -*-
import json
path = r'C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json'
d = json.load(open(path, encoding='utf-8'))
jobs = d['jobs']
print('=== ALL main-agent jobs ===')
for j in jobs:
    if (j.get('agentId') or '') == 'main':
        sched = json.dumps(j.get('schedule'), ensure_ascii=False)
        print(j['id'], '|', j.get('enabled'), '|', (j.get('name') or '')[:70], '|', sched[:120])
print()
print('=== ALL jobs with enabled=false or deleteAfterRun ===')
for j in jobs:
    if not j.get('enabled', True) or j.get('deleteAfterRun'):
        print(j['id'][:8], '|', j.get('agentId'), '|', j.get('enabled'), '|', j.get('deleteAfterRun'), '|', (j.get('name') or '')[:60])
