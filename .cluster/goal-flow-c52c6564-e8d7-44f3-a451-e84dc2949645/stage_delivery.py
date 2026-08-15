# -*- coding: utf-8 -*-
import os, shutil

WB = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645'
DEST = os.path.join(WB, 'DELIVERY')
os.makedirs(DEST, exist_ok=True)
files = ['00-overview.md', '01-task-ledger.md', '02-artifacts.md', '03-risk-log.md',
         '04-review-record.md', '05-handoff.md', 'generate-sitemap_merged.py',
         'sitemap_fix_v2.patch', 'sitemap_fix_test_v2.py']
for f in files:
    shutil.copy2(os.path.join(WB, f), os.path.join(DEST, f))
print('=== DELIVERY ===')
for f in sorted(os.listdir(DEST)):
    p = os.path.join(DEST, f)
    print(f, os.path.getsize(p))
