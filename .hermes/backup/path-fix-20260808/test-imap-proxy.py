# -*- coding: utf-8 -*-
"""SOCKS5 代理测试 IMAP 连通 + 登录"""
import socket, ssl, struct, json, os

def socks5_connect(proxy_host, proxy_port, target_host, target_port, timeout=20):
    """手动 SOCKS5 握手, 返回已连接 socket"""
    s = socket.create_connection((proxy_host, proxy_port), timeout=timeout)
    # 握手: 无认证
    s.sendall(b'\x05\x01\x00')
    resp = s.recv(2)
    if resp != b'\x05\x00':
        s.close()
        raise RuntimeError('SOCKS5 handshake failed: %r' % resp)
    # 连接请求 (域名)
    host_b = target_host.encode()
    req = b'\x05\x01\x00\x03' + bytes([len(host_b)]) + host_b + struct.pack('>H', target_port)
    s.sendall(req)
    resp = s.recv(4)
    if len(resp) < 4 or resp[1] != 0:
        s.close()
        raise RuntimeError('SOCKS5 connect failed: %r' % resp)
    # 读剩余地址 (ATYP)
    atyp = resp[3]
    if atyp == 1:
        s.recv(4 + 2)
    elif atyp == 4:
        s.recv(16 + 2)
    else:
        ln = s.recv(1)[0]
        s.recv(ln + 2)
    return s

def test_via_proxy(user, pw, label):
    try:
        sock = socks5_connect('127.0.0.1', 7892, 'imap.gmail.com', 993)
        ctx = ssl.create_default_context()
        ssock = ctx.wrap_socket(sock, server_hostname='imap.gmail.com')
        # 用 imaplib 复用这个 socket
        import imaplib
        class IMAP(imaplib.IMAP4_SSL):
            def _create_socket(self, timeout=None):
                return ssock
        M = IMAP('imap.gmail.com', 993)
        r = M.login(user, pw)
        M.logout()
        return f'{label}: OK'
    except Exception as e:
        return f'{label}: FAIL ({str(e)[:80]})'

BASE = r'F:\aitoptools'
g = json.load(open(os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json'), encoding='utf-8'))
user = g['user']

print('1)', test_via_proxy(user, g.get('app_password', ''), 'file app_password via proxy'))

pw2 = None
env_path = r'C:\Users\Administrator\AppData\Local\hermes\.env'
if os.path.exists(env_path):
    for line in open(env_path, encoding='utf-8', errors='ignore'):
        ls = line.strip()
        if ls.startswith('IMAP_PASSWORD='):
            pw2 = ls.split('=', 1)[1].strip().strip('"').strip("'")
print('2)', test_via_proxy(user, pw2 or '', 'AppData .env IMAP_PASSWORD via proxy'))
