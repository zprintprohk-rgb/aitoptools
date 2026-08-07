# -*- coding: utf-8 -*-
"""8/8 batch A step3 final: 修复 gmail_credentials.json (AppData 密码 + 代理字段)"""
import json, os, socket, ssl, struct, imaplib

BASE = r'F:\aitoptools'
cred_file = os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json')
g = json.load(open(cred_file, encoding='utf-8'))

pw2 = None
env_path = r'C:\Users\Administrator\AppData\Local\hermes\.env'
for line in open(env_path, encoding='utf-8', errors='ignore'):
    ls = line.strip()
    if ls.startswith('IMAP_PASSWORD='):
        pw2 = ls.split('=', 1)[1].strip().strip('"').strip("'")

def socks5_connect(proxy_host, proxy_port, target_host, target_port, timeout=20):
    s = socket.create_connection((proxy_host, proxy_port), timeout=timeout)
    s.sendall(b'\x05\x01\x00')
    if s.recv(2) != b'\x05\x00':
        s.close(); raise RuntimeError('SOCKS5 handshake failed')
    host_b = target_host.encode()
    req = b'\x05\x01\x00\x03' + bytes([len(host_b)]) + host_b + struct.pack('>H', target_port)
    s.sendall(req)
    resp = s.recv(4)
    if len(resp) < 4 or resp[1] != 0:
        s.close(); raise RuntimeError('SOCKS5 connect failed: %r' % resp)
    atyp = resp[3]
    if atyp == 1: s.recv(6)
    elif atyp == 4: s.recv(18)
    else:
        ln = s.recv(1)[0]; s.recv(ln + 2)
    return s

def verify(user, pw):
    sock = socks5_connect('127.0.0.1', 7892, 'imap.gmail.com', 993)
    ssock = ssl.create_default_context().wrap_socket(sock, server_hostname='imap.gmail.com')
    class IMAP(imaplib.IMAP4_SSL):
        def _create_socket(self, timeout=None):
            return ssock
    M = IMAP('imap.gmail.com', 993)
    r = M.login(user, pw)
    M.logout()
    return r[0] == 'OK'

user = g['user']
ok = verify(user, pw2)
print('verify via proxy:', ok)

if ok and pw2:
    g['app_password'] = pw2
    g['imap_proxy'] = 'socks5://127.0.0.1:7892'
    g['imap_requires_proxy'] = True
    g['last_updated'] = '2026-08-08 (auto-fixed from AppData hermes .env, proxy verified)'
    with open(cred_file, 'w', encoding='utf-8') as f:
        json.dump(g, f, ensure_ascii=False, indent=2)
    print('FIXED: gmail_credentials.json updated + proxy config added')
else:
    print('STILL BLOCKED')
