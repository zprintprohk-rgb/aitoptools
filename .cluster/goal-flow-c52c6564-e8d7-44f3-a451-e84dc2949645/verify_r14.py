# -*- coding: utf-8 -*-
"""R-14 核实：jobs.json 主任务/探针状态 vs cron 工具视图"""
import json, os, sys, time
sys.stdout.reconfigure(errors='replace')
path = r'C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json'
d = json.load(open(path, encoding='utf-8'))
jobs = d['jobs']
print('TOTAL', len(jobs), '| mtime:', time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(path))))
print()
print('=== 84c86e36 (8/16 main job) ===')
for j in jobs:
    if j['id'] == '84c86e36-fd6f-479b-9f6c-b05699945bb9':
        print('id:', j['id'])
        print('enabled:', j.get('enabled'), '| deleteAfterRun:', j.get('deleteAfterRun'))
        print('schedule:', json.dumps(j.get('schedule'), ensure_ascii=False))
        print('state:', json.dumps(j.get('state', {}), ensure_ascii=False)[:200])
        print('agentId:', j.get('agentId'), '| sessionKey:', j.get('sessionKey'))
        break
else:
    print('NOT FOUND IN jobs.json !!!')
print()
print('=== all main jobs (name | enabled | at/cron) ===')
for j in jobs:
    if (j.get('agentId') or '') == 'main':
        print(j['id'][:8], '|', j.get('enabled'), '|', (j.get('name') or '')[:38],
              '|', json.dumps(j.get('schedule'), ensure_ascii=False)[:50],
              '| state:', json.dumps(j.get('state', {}), ensure_ascii=False)[:60])
print()
print('=== jobs created after 03:50 today (probe?) ===')
cutoff = 1786823400000  # ~03:50
for j in jobs:
    if j.get('createdAtMs', 0) > cutoff:
        print('NEW:', j['id'][:8], '|', (j.get('name') or '')[:50], '| enabled:', j.get('enabled'),
              '|', json.dumps(j.get('schedule'), ensure_ascii=False)[:60])
print()
print('=== R-14 in risk log? ===')
rl = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\03-risk-log.md'
if os.path.exists(rl):
    c = open(rl, encoding='utf-8').read()
    print('R-14 in 03-risk-log.md:', 'R-14' in c)
else:
    print('risk log missing')
