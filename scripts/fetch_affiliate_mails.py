"""Fetch emails since 2026-07-30 from Gmail (IMAP), filter for affiliate/partner-related mail.

Reads credentials from .hermes/secrets/gmail_credentials.json (never printed).
Prints: date | from | subject (truncated) — for all matching + a summary of unmatched notable senders.
"""
import imaplib, email, json, re, os
import socks, socket
from email.header import decode_header
from datetime import datetime, timedelta

CRED = r'F:\aitoptools\.hermes\secrets\gmail_credentials.json'
HERMES_ENV = os.path.join(os.environ.get('LOCALAPPDATA', r'C:\Users\Administrator\AppData\Local'), 'hermes', '.env')
SINCE_DATE = '30-Jul-2026'
PROXY = ('127.0.0.1', 7892)  # Clash SOCKS5 (system proxy) — Gmail TLS is MITM'd on direct connect

d = json.load(open(CRED, encoding='utf-8'))
USER = d['user']
# Real App Password lives in hermes .env (IMAP_PASSWORD); credentials file holds an outdated/template value
_env_text = open(HERMES_ENV, encoding='utf-8').read()
_m = re.search(r'^IMAP_PASSWORD=(.*)$', _env_text, re.M)
PWD = _m.group(1).strip().strip('"').strip("'") if _m else d['app_password']
HOST = d['imap_host']; PORT = d['imap_port']
SENDERS = [s.lower() for s in d['filter_senders']]
KEYWORDS = [k.lower() for k in d['filter_keywords']]

def dec(s):
    if not s: return ''
    parts = decode_header(s)
    out = []
    for txt, enc in parts:
        if isinstance(txt, bytes):
            try: out.append(txt.decode(enc or 'utf-8', errors='replace'))
            except Exception: out.append(txt.decode('utf-8', errors='replace'))
        else: out.append(txt)
    return ''.join(out)

def sender_domain(frm):
    if not frm: return ''
    frm = frm.lower()
    for s in SENDERS:
        if s in frm: return s
    # extract domain after @
    import re
    m = re.search(r'@([\w.-]+)', frm)
    return m.group(1) if m else frm

# Route through SOCKS5 proxy (direct connect to Gmail is MITM-blocked on this network)
socks.set_default_proxy(socks.SOCKS5, PROXY[0], PROXY[1])
socket.socket = socks.socksocket
M = imaplib.IMAP4_SSL(HOST, PORT, timeout=30)
M.login(USER, PWD)
M.select('INBOX')

# IMAP date search — covers all mail since cutoff; we re-check Date header locally
status, data = M.search(None, f'(SINCE {SINCE_DATE})')
ids = data[0].split()
print(f'Total messages since {SINCE_DATE}: {len(ids)}')

matches = []
others = []
for i in ids:
    status, msg_data = M.fetch(i, '(RFC822.HEADER)')
    if status != 'OK' or not msg_data or not msg_data[0]: continue
    raw = msg_data[0][1]
    msg = email.message_from_bytes(raw)
    subj = dec(msg.get('Subject', ''))
    frm = dec(msg.get('From', ''))
    date_raw = msg.get('Date', '')
    # local date parse
    try:
        dt = email.utils.parsedate_to_datetime(date_raw)
        date_str = dt.strftime('%Y-%m-%d %H:%M')
    except Exception:
        date_str = date_raw[:25]

    domain = sender_domain(frm)
    text_l = (subj + ' ' + frm).lower()
    kw_hit = [k for k in KEYWORDS if k in text_l]
    is_filter_sender = any(s in frm.lower() for s in SENDERS)

    if is_filter_sender or kw_hit:
        matches.append((date_str, frm[:60], subj[:90], kw_hit))
    else:
        others.append((date_str, domain, subj[:70]))

M.logout()

print(f'\n=== MATCHED (affiliate/partner related): {len(matches)} ===')
for date_str, frm, subj, kw in sorted(matches):
    print(f'[{date_str}] {frm}')
    print(f'    SUBJ: {subj}')
    if kw: print(f'    KW: {",".join(kw)}')

print(f'\n=== OTHER senders (not filtered, for review): {len(others)} ===')
seen = {}
for date_str, dom, subj in others:
    seen.setdefault(dom, []).append((date_str, subj))
for dom, items in sorted(seen.items()):
    print(f'--- {dom} ({len(items)} msgs)')
    for date_str, subj in items[:4]:
        print(f'    [{date_str}] {subj}')
    if len(items) > 4: print(f'    ... +{len(items)-4} more')
