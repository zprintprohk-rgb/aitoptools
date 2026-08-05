"""Read full bodies of high-value affiliate mails since 30-Jul (by sender/subject match)."""
import imaplib, email, json, re, os
import socks, socket
from email.header import decode_header

CRED = r'F:\aitoptools\.hermes\secrets\gmail_credentials.json'
HERMES_ENV = os.path.join(os.environ.get('LOCALAPPDATA', r'C:\Users\Administrator\AppData\Local'), 'hermes', '.env')
PROXY = ('127.0.0.1', 7892)
TARGETS = [  # (sender-substring, subject-substring)
    ('partnerstack.com', 'status of your PartnerStack Network'),
    ('gelato.com', 'Welcome to Gelato Partners'),
    ('claid.ai', 'Monthly Performance'),
    ('letsenhance.io', 'Monthly Performance'),
    ('accounts.google.com', '安全提醒'),
]

d = json.load(open(CRED, encoding='utf-8'))
USER = d['user']
_env = open(HERMES_ENV, encoding='utf-8').read()
_m = re.search(r'^IMAP_PASSWORD=(.*)$', _env, re.M)
PWD = _m.group(1).strip().strip('"').strip("'")

def dec(s):
    if not s: return ''
    out = []
    for txt, enc in decode_header(s):
        if isinstance(txt, bytes):
            try: out.append(txt.decode(enc or 'utf-8', errors='replace'))
            except Exception: out.append(txt.decode('utf-8', errors='replace'))
        else: out.append(txt)
    return ''.join(out)

def get_body(msg):
    if msg.is_multipart():
        # prefer text/plain
        for part in msg.walk():
            if part.get_content_type() == 'text/plain' and not part.get('Content-Disposition'):
                return part.get_payload(decode=True).decode('utf-8', errors='replace')
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode('utf-8', errors='replace')
        return '(multipart, no plain text)'
    return msg.get_payload(decode=True).decode('utf-8', errors='replace') if msg.get_payload(decode=True) else '(empty)'

socks.set_default_proxy(socks.SOCKS5, PROXY[0], PROXY[1])
socket.socket = socks.socksocket
M = imaplib.IMAP4_SSL('imap.gmail.com', 993, timeout=30)
M.login(USER, PWD)
M.select('INBOX')
status, data = M.search(None, '(SINCE 30-Jul-2026)')
ids = data[0].split()

found = {i: False for i in range(len(TARGETS))}
for i in ids:
    status, msg_data = M.fetch(i, '(RFC822)')
    if status != 'OK' or not msg_data or not msg_data[0]: continue
    msg = email.message_from_bytes(msg_data[0][1])
    frm = dec(msg.get('From', '')).lower()
    subj = dec(msg.get('Subject', ''))
    for ti, (snd, sub) in enumerate(TARGETS):
        if snd in frm and sub.lower() in subj.lower() and not found[ti]:
            found[ti] = True
            body = get_body(msg)
            print(f'\n{"="*70}\n[{ti}] FROM: {frm.strip()}')
            print(f'DATE: {msg.get("Date","")}\nSUBJ: {subj}')
            print(f'{"-"*70}\n{body[:2500]}')
M.logout()
print('\nDone.')
