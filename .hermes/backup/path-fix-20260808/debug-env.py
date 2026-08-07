# -*- coding: utf-8 -*-
"""调试: 检查 hermes .env IMAP_PASSWORD 解析"""
import os

env_file = os.path.join(os.path.expanduser('~'), '.hermes', '.env')
print('env_file exists:', os.path.exists(env_file))
if os.path.exists(env_file):
    lines = open(env_file, encoding='utf-8', errors='ignore').readlines()
    print('total lines:', len(lines))
    for i, line in enumerate(lines):
        ls = line.strip()
        if 'IMAP' in ls.upper() or 'PASSWORD' in ls.upper() or 'GMAIL' in ls.upper() or 'EMAIL' in ls.upper():
            k = ls.split('=', 1)[0] if '=' in ls else ls
            v = ls.split('=', 1)[1] if '=' in ls else ''
            print(f'line {i}: key={k!r} len={len(v.strip())} first2={v.strip()[:2]!r} last2={v.strip()[-2:]!r}')
