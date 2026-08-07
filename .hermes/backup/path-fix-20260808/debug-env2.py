# -*- coding: utf-8 -*-
"""列出 hermes .env 键名（值脱敏）"""
import os
env_file = os.path.join(os.path.expanduser('~'), '.hermes', '.env')
for line in open(env_file, encoding='utf-8', errors='ignore'):
    ls = line.strip()
    if not ls or ls.startswith('#'):
        continue
    if '=' in ls:
        k, _, v = ls.partition('=')
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        print(f'{k} = len={len(v)}')
    else:
        print('(no =)', ls[:60])
