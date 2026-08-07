# -*- coding: utf-8 -*-
"""gmail_imap_search.py — 搜 Printful 确认邮件并提取 verify 链接 (指令 #1 第一步)
- 全量窗口: SINCE 01-Jun-2026 (关键激活邮件全量搜索铁律, 禁 30 天窄窗)
- 直连失败(超时) → SOCKS5 127.0.0.1:7892 兜底 (pysocks 可用)
- 输出: 摘要到 stdout (链接 key 脱敏), 完整链接写 .hermes/tmp/printful-verify-link.txt
"""
import imaplib, ssl, socket, re, sys, json, os, email
from email.header import decode_header, make_header

BASE = r'F:\aitoptools'
CRED = os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json')
OUT = os.path.join(BASE, '.hermes', 'tmp', 'printful-verify-link.txt')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def mask_url(u):
    # 只脱敏 key= 参数, 保留 scheme/host/path 供判断
    return re.sub(r'(key=)[^&\s]+', r'\1***', u)

def dec(s):
    if not s:
        return ''
    try:
        return str(make_header(decode_header(s)))
    except Exception:
        return str(s)

def load_cred():
    # 1) hermes .env IMAP_PASSWORD (cron 实际在用, 8/3 起验证有效)
    env_path = r'C:\Users\Administrator\AppData\Local\hermes\.env'
    try:
        for line in open(env_path, encoding='utf-8'):
            if line.startswith('IMAP_PASSWORD='):
                return line.split('=', 1)[1].strip()
    except Exception:
        pass
    # 2) 项目 gmail_credentials.json app_password (可能过期)
    cred = json.load(open(CRED, encoding='utf-8'))
    return cred['app_password']

def connect():
    cred = json.load(open(CRED, encoding='utf-8'))
    host, port = cred['imap_host'], cred['imap_port']
    user, pw = cred['user'], load_cred()
    last_err = None
    # 尝试 1: 直连 SSL
    try:
        ctx = ssl.create_default_context()
        M = imaplib.IMAP4_SSL(host, port, ssl_context=ctx, timeout=20)
        M.login(user, pw)
        return M, 'direct'
    except Exception as e:
        last_err = e
    # 尝试 2: SOCKS5 兜底 (pysocks)
    try:
        import socks
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, '127.0.0.1', 7892)
        s.settimeout(30)
        s.connect((host, port))
        ctx = ssl.create_default_context()
        raw = ctx.wrap_socket(s, server_hostname=host)
        M = imaplib.IMAP4(host, port)
        M._create_socket = None
        M.sock = raw
        M.file = raw.makefile('rb')
        typ, dat = M._get_response()
        if typ != 'OK':
            raise RuntimeError('SOCKS5 IMAP greeting failed: %r' % dat)
        M.login(user, pw)
        return M, 'socks5'
    except Exception as e2:
        raise RuntimeError('直连失败: %r; SOCKS5 失败: %r' % (last_err, e2))

def main():
    M, mode = connect()
    print('IMAP 连接模式:', mode)
    M.select('INBOX', readonly=True)
    # 全量搜索铁律: 发件人 domain + 90 天窗口
    typ, data = M.search(None, '(FROM "printful.com" SINCE "01-Jun-2026")')
    ids = data[0].split()
    print('printful.com 邮件总数(6/1 起):', len(ids))
    hits = []
    for i in ids:
        typ, msg_data = M.fetch(i, '(BODY.PEEK[HEADER])')
        raw = msg_data[0][1] if isinstance(msg_data[0], tuple) else b''
        msg = email.message_from_bytes(raw)
        subj = dec(msg.get('Subject', ''))
        frm = str(msg.get('From', ''))
        date = str(msg.get('Date', ''))
        is_confirm = 'confirm' in subj.lower()
        if is_confirm or 'verif' in subj.lower():
            typ2, body_data = M.fetch(i, '(RFC822)')
            raw_full = b''
            for part in body_data:
                if isinstance(part, tuple):
                    raw_full += part[1]
            msg_full = email.message_from_bytes(raw_full)
            texts = []
            for part in msg_full.walk():
                if part.get_content_type() in ('text/plain', 'text/html'):
                    try:
                        texts.append(part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', 'ignore'))
                    except Exception:
                        pass
            body_text = '\n'.join(texts)
            urls = re.findall(r'https?://[^\s<>"\')\]]+', body_text)
            verify_urls = sorted(set(u for u in urls if 'printful.com/verify' in u), key=len, reverse=True)
            hits.append({'id': i.decode(), 'from': frm, 'date': date, 'subject': subj,
                         'urls': verify_urls})
            print('- [%s] %s | %s | %s' % (i.decode(), date[:31], frm, subj))
            for u in verify_urls:
                print('    URL:', mask_url(u))
    M.logout()
    # 选定目标: 最新一封 confirm 邮件中的 verify 链接 (QP 解码后按长度降序取最完整)
    target = None
    confirm_hits = [h for h in hits if 'confirm' in h['subject'].lower()][::-1]
    for h in confirm_hits:
        if h['urls']:
            target = h['urls'][0]
            break
    if not target:
        for h in hits:
            if h['urls']:
                target = h['urls'][0]
                break
    if target:
        with open(OUT, 'w', encoding='utf-8') as f:
            f.write(target)
        print('\n✅ verify 链接已写入:', OUT)
        print('   (脱敏):', mask_url(target))
    else:
        print('\n❌ 未找到 verify 链接 — 需要检查或走后台重发路径')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('ERROR:', e)
        sys.exit(1)
