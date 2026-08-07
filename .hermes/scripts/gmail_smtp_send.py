# -*- coding: utf-8 -*-
"""gmail_smtp_send.py — 发送 Printify Promo Code 请求邮件 (指令 #2)
- 收件人: affiliate@printify.com
- Subject: Promo Code Request - aitoptools
- 正文: 指令模板 (2026-08-07 老板指令内置模板)
- 发送成功 → 写 .hermes/tmp/printify-sent.txt (含 Message-ID 留证)
"""
import smtplib, ssl, json, os, sys, time
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate, make_msgid

BASE = r'F:\aitoptools'
CRED = os.path.join(BASE, '.hermes', 'secrets', 'gmail_credentials.json')
OUT = os.path.join(BASE, '.hermes', 'tmp', 'printify-sent.txt')

SUBJECT = 'Promo Code Request - aitoptools'
BODY = """Hi Printify Team,

I'm Jerome from aitoptools.net (AI tools review site, 344 pages,
monthly traffic growing). I'd love a custom promo code for my audience
focused on POD entrepreneurs. Happy to feature it in dedicated content.

Thanks,
Jerome
"""

def load_pw():
    # 1) hermes .env IMAP_PASSWORD (cron 实际在用)
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

def main():
    cred = json.load(open(CRED, encoding='utf-8'))
    user, pw = cred['user'], load_pw()
    to_addr = 'affiliate@printify.com'
    msg = MIMEText(BODY, 'plain', 'utf-8')
    msg['Subject'] = SUBJECT
    msg['From'] = formataddr(('Jerome Tang (aitoptools.net)', user))
    msg['To'] = to_addr
    msg['Date'] = formatdate(localtime=True)
    msg['Message-ID'] = make_msgid(domain='aitoptools.net')

    last_err = None
    # 尝试 1: smtp.gmail.com:465 SSL
    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ctx, timeout=30) as s:
            s.login(user, pw)
            s.sendmail(user, [to_addr], msg.as_string())
        mode = 'smtp-465-ssl'
    except Exception as e:
        last_err = e
        # 尝试 2: smtp.gmail.com:587 STARTTLS
        try:
            with smtplib.SMTP('smtp.gmail.com', 587, timeout=30) as s:
                s.starttls(context=ssl.create_default_context())
                s.login(user, pw)
                s.sendmail(user, [to_addr], msg.as_string())
            mode = 'smtp-587-starttls'
        except Exception as e2:
            raise RuntimeError('465 失败: %r; 587 失败: %r' % (last_err, e2))

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('sent_at: %s\n' % time.strftime('%Y-%m-%d %H:%M:%S %z'))
        f.write('mode: %s\n' % mode)
        f.write('to: %s\n' % to_addr)
        f.write('subject: %s\n' % SUBJECT)
        f.write('message_id: %s\n' % msg['Message-ID'])
    print('✅ 已发送 via', mode)
    print('   to:', to_addr)
    print('   subject:', SUBJECT)
    print('   message_id:', msg['Message-ID'])
    print('   留证:', OUT)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('ERROR:', e)
        sys.exit(1)
