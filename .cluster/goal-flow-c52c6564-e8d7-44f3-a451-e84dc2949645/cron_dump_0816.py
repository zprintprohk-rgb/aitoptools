# -*- coding: utf-8 -*-
import json, sys, time
sys.stdout.reconfigure(errors='replace')
path = r'C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json'
d = json.load(open(path, encoding='utf-8'))
jobs = d['jobs']
print('TOTAL', len(jobs), '| file mtime:', time.strftime('%m-%d %H:%M', time.localtime(__import__('os').path.getmtime(path))))
print()
print('=== ALL main-agent jobs (name | enabled | schedule | lastRunStatus | lastError) ===')
for j in jobs:
    if (j.get('agentId') or '') == 'main':
        st = j.get('state', {})
        err = (st.get('lastError') or '')[:80].replace('\n', ' ')
        print(j['id'][:8], '|', j.get('enabled'), '|', (j.get('name') or '')[:34],
              '|', json.dumps(j.get('schedule'), ensure_ascii=False)[:44],
              '|', st.get('lastRunStatus', '-'), '|', err)
print()
print('=== non-main jobs ===')
for j in jobs:
    if (j.get('agentId') or '') != 'main':
        print(j.get('agentId'), '|', j['id'][:8], '|', (j.get('name') or '')[:40], '| enabled:', j.get('enabled'))
