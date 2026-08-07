# -*- coding: utf-8 -*-
"""8/8 batch A step3 v2: 用 AppData\Local\hermes\.env IMAP_PASSWORD 实测 + 修复"""
import imaplib, json, os, sys

def test_login(user, pw, label):
    if not pw:
        return f"{label}: NO_PASSWORD"
    try:
        M = imaplib.IMAP4_SSL('imap.gmail.com', 993, timeout=20)
        r = M.login(user, pw)
        M.logout()
        return f"{label}: OK"
    except Exception as e:
        return f"{label}: FAIL ({str(e)[:60]})"

BASE = r'F:\aitoptools'
cred_file = os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json')
g = json.load(open(cred_file, encoding='utf-8'))
user = g['user']

# 1) 现有 app_password
r1 = test_login(user, g.get('app_password', ''), 'file app_password')
print('1)', r1)

# 2) AppData\Local\hermes\.env IMAP_PASSWORD
pw2 = None
env_path = r'C:\Users\Administrator\AppData\Local\hermes\.env'
print('env exists:', os.path.exists(env_path))
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8', errors='ignore'):
        ls = line.strip()
        if ls.startswith('IMAP_PASSWORD='):
            pw2 = ls.split('=', 1)[1].strip().strip('"').strip("'")
r2 = test_login(user, pw2 or '', 'AppData hermes .env IMAP_PASSWORD')
print('2)', r2)

if 'FAIL' in r1 and 'OK' in r2 and pw2:
    g['app_password'] = pw2
    g['last_updated'] = '2026-08-08 (auto-fixed from AppData hermes .env)'
    with open(cred_file, 'w', encoding='utf-8') as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
    print('FIXED: gmail_credentials.json updated, IMAP login OK')
    sys.exit(0)
elif 'OK' in r1:
    print('STATUS: file app_password works, no change')
    sys.exit(0)
else:
    print('BLOCKED_NEED_MANUAL_GMAIL_PASSWORD')
    sys.exit(1)
