# -*- coding: utf-8 -*-
"""update_ssot_20260808.py — 手术式更新 affiliate-programs.json (8/8 自动化结果)
改动:
  printful.verification      -> verify-link-expired-2026-08-08 (browser 实测)
  printful.confirm_link_note -> 更新为过期证据 + 重发待 cookie
  printful.last_updated      -> 2026-08-08
  printify.promo_request_sent -> 2026-08-08 发送留证
  printify.last_updated      -> 2026-08-08
仅触碰上述字段, 其余不动。保持 indent=2 + ensure_ascii=False + 原尾部换行。
"""
import json, io

P = r'F:\aitoptools\.hermes\affiliate-programs.json'
raw = io.open(P, encoding='utf-8').read()
had_nl = raw.endswith('\n')
d = json.loads(raw)

for p in d['programs']:
    name = p.get('name', '')
    if name == 'Printful Affiliate Program':
        p['verification'] = ('verify-link-expired-2026-08-08 (headless browser 实测: '
                             'printful.com/auth/login 页 alert "Email confirmation request does not exist"; '
                             '7/17+7/20 两封同 token 均已失效), resend-pending-cookie')
        p['confirm_link_note'] = ('8/8 Hermes 全权指令 #1: IMAP 实拉两封 Confirm email address (7/17 15:25Z, 7/20 17:00Z, '
                                  '同 token), headless GET verify 链接 -> 重定向 auth/login + "Email confirmation request '
                                  'does not exist" = 已过期。需 printful_session_cookie 登录后台 Resend verification -> '
                                  '轮询新邮件(3 次/60s) -> 重试。')
        p['last_updated'] = '2026-08-08'
    elif name == 'Printify Affiliate Program':
        p['promo_request_sent'] = ('2026-08-08 via SMTP 465 SSL (gmail_credentials 通道, 真密码 .env IMAP_PASSWORD), '
                                   'subject "Promo Code Request - aitoptools", Message-ID <178612007459.38260.17414933324366495799@aitoptools.net>, '
                                   '留证 .hermes/tmp/printify-sent.txt; 72h 后检查回复 (monitor cron 已覆盖 mail.printify.com)')
        p['last_updated'] = '2026-08-08'

out = json.dumps(d, ensure_ascii=False, indent=2)
if had_nl:
    out += '\n'
io.open(P, 'w', encoding='utf-8', newline='').write(out)
print('✅ SSoT 已更新 (printful.verification + printify.promo_request_sent)')
