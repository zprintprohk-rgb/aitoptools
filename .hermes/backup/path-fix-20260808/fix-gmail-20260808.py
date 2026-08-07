# -*- coding: utf-8 -*-
"""8/8 batch A step3: IMAP 双密码源实测 + 自动修复 gmail_credentials.json"""
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
        return f"{label}: FAIL ({str(e)[:80]})"

BASE = r'F:\aitoptools'
g = json.load(open(os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json'), encoding='utf-8'))
user = g['user']
print('user:', user)

r1 = test_login(user, g.get('app_password', ''), 'file app_password')
print('1)', r1)

pw2 = None
env_file = os.path.join(os.path.expanduser('~'), '.hermes', '.env')
if os.path.exists(env_file):
    for line in open(env_file, encoding='utf-8', errors='ignore'):
        ls = line.strip()
        if ls.startswith('IMAP_PASSWORD'):
            pw2 = ls.split('=', 1)[1].strip().strip('"').strip("'")
r2 = test_login(user, pw2 or '', 'hermes .env IMAP_PASSWORD')
print('2)', r2)

# 修复: 若 env 密码可用且文件密码失效 → 更新 gmail_credentials.json
if 'FAIL' in r1 and 'OK' in r2 and pw2:
    g['app_password'] = pw2
    g['last_updated'] = '2026-08-08 (auto-fixed from hermes .env IMAP_PASSWORD)'
    with open(os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json'), 'w', encoding='utf-8') as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
    print('FIXED: gmail_credentials.json updated with working IMAP password')
elif 'OK' in r1:
    print('STATUS: file app_password already works (no change needed)')
else:
    print('BLOCKED_NEED_MANUAL_GMAIL_PASSWORD: both sources failed')
    sys.exit(1)
