# -*- coding: utf-8 -*-
"""定位 IMAP_PASSWORD 真实来源"""
import os, glob

candidates = [
    r'F:\hermes-config\.env',
    r'F:\aitoptools\.hermes\.env',
    r'F:\aitoptools\.env.local',
    r'F:\aitoptools\.env.example',
    r'F:\hermes-config\config.yaml',
]
for p in candidates:
    if os.path.exists(p):
        print('===', p)
        for line in open(p, encoding='utf-8', errors='ignore'):
            ls = line.strip()
            if ls.startswith('#') or not ls:
                continue
            if '=' in ls:
                k = ls.split('=', 1)[0].strip()
                if any(t in k.upper() for t in ('IMAP', 'MAIL', 'GMAIL', 'PASSWORD', 'SMTP')):
                    v = ls.split('=', 1)[1].strip()
                    print(f'  {k} len={len(v)}')
            else:
                low = ls.lower()
                if any(t in low for t in ('imap', 'mail', 'password', 'smtp')):
                    print('  (yaml?)', ls[:100])
