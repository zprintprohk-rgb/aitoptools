# -*- coding: utf-8 -*-
"""validate_session_cookies.py — 校验 printful_session_cookie / pinterest_session
来源优先级: 环境变量 HERMES_PRINTFUL_COOKIE / HERMES_PINTEREST_SESSION > .hermes/secrets/{name}.txt
校验: ① 格式 (非空/含= /cookie 对数/长度) ② 连通性 (curl 带 cookie + 浏览器 UA, 直连→代理兜底)
判定: VALID (200 且未跳登录) / EXPIRED (跳登录) / BLOCKED (403/429, 需浏览器注入复核) / NETWORK (超时)
输出全部脱敏; 证据写 .hermes/logs/session-validation-{date}.md
"""
import os, re, subprocess, sys, time, json

BASE = r'F:\aitoptools'
SEC = os.path.join(BASE, '.hermes', 'secrets')
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36')

def mask(s):
    return re.sub(r'=([^;=]{4})[^;]*', r'=\1***', s)

def get_cookie(env_name, fname):
    v = os.environ.get(env_name, '').strip()
    if v:
        return v, 'env:' + env_name
    p = os.path.join(SEC, fname)
    if os.path.isfile(p):
        raw = open(p, encoding='utf-8', errors='ignore').read()
        return raw.strip(), 'file:' + fname
    return None, None

def fmt_check(cookie):
    """返回 (ok, 描述)"""
    if not cookie:
        return False, '空值'
    if len(cookie) < 15:
        return False, '过短(len=%d)' % len(cookie)
    pairs = [p for p in cookie.split(';') if '=' in p]
    if not pairs:
        return False, '不含 cookie 对 (无 =)'
    bad = [p for p in pairs if len(p.split('=', 1)[0].strip()) == 0]
    if bad:
        return False, '存在空键名'
    return True, '%d 对 cookie, len=%d' % (len(pairs), len(cookie))

def curl_test(url, cookie):
    """返回 (code, final_url) — 直连优先, 403 时走代理 7892"""
    results = []
    for label, extra in (('direct', []), ('proxy', ['-x', 'http://127.0.0.1:7892'])):
        cmd = ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}|%{url_effective}',
               '--max-time', '25', '-A', UA, '-H', 'Cookie: ' + cookie, '-L', url] + extra
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
            out = r.stdout.strip()
            if '|' in out:
                code, final = out.split('|', 1)
                results.append((label, code, final))
        except Exception:
            results.append((label, 'ERR', ''))
    for label, code, final in results:
        if code != '403' and code != '429':
            return code, final, label
    return results[0][1], results[0][2], results[0][0]  # 全挡则报第一条

def verdict(name, url, login_marker, cookie, out_lines):
    ok_fmt, desc = fmt_check(cookie)
    out_lines.append('### %s' % name)
    out_lines.append('- 来源: %s' % src_label)
    out_lines.append('- 格式: %s → %s' % ('✅' if ok_fmt else '❌', desc))
    if not ok_fmt:
        out_lines.append('- 判定: ❌ FORMAT-FAIL (不发起连通性测试)')
        return False
    code, final, via = curl_test(url, cookie)
    out_lines.append('- 连通性: HTTP %s (via %s) → 最终URL: %s' % (code, via, final))
    if login_marker in final:
        verdict_txt = '❌ EXPIRED (跳转登录页, session 失效/过期)'
        ok = False
    elif code == '200':
        verdict_txt = '✅ VALID (200, 未跳登录)'
        ok = True
    elif code in ('403', '429'):
        verdict_txt = '⚠️ BLOCKED (403/429 — 可能是反爬, 需浏览器注入 cookie 复核)'
        ok = None
    else:
        verdict_txt = '❌ NETWORK/异常 (HTTP %s)' % code
        ok = False
    out_lines.append('- 判定: %s' % verdict_txt)
    out_lines.append('- 脱敏预览: %s' % (mask(cookie)[:80] + '...'))
    out_lines.append('')
    return ok

def main():
    out_lines = ['# Session Cookie 校验 — %s' % time.strftime('%Y-%m-%d %H:%M:%S'),
                 '> 指令: 8/8 user 提交协议, Hermes 自动校验格式+连通性', '']
    global src_label
    results = {}
    for name, env, fname, url, marker in (
        ('printful_session_cookie', 'HERMES_PRINTFUL_COOKIE', 'printful_session_cookie.txt',
         'https://www.printful.com/dashboard/', '/auth/login'),
        ('pinterest_session', 'HERMES_PINTEREST_SESSION', 'pinterest_session.txt',
         'https://www.pinterest.com/', '/login'),
    ):
        cookie, src_label = get_cookie(env, fname)
        if cookie is None:
            out_lines.append('### %s' % name)
            out_lines.append('- 未提交 (env %s 与 file %s 均无)' % (env, fname))
            out_lines.append('- 判定: ⏳ AWAITING-SUBMISSION')
            out_lines.append('')
            results[name] = None
            continue
        results[name] = verdict(name, url, marker, cookie, out_lines)
    logdir = os.path.join(BASE, '.hermes', 'logs')
    os.makedirs(logdir, exist_ok=True)
    logp = os.path.join(logdir, 'session-validation-%s.md' % time.strftime('%Y-%m-%d'))
    open(logp, 'w', encoding='utf-8').write('\n'.join(out_lines))
    print('\n'.join(out_lines))
    print('证据: %s' % logp)
    any_fail = any(v is False for v in results.values())
    any_blocked = any(v is None and results[k] is not None for k, v in results.items())
    if any_fail:
        sys.exit(2)
    if any_blocked:
        sys.exit(3)
    if all(v is None for v in results.values()):
        print('⏳ 两个 secret 均未提交 — 待 user 落盘后重跑本脚本')
    else:
        print('✅ 校验完成')

if __name__ == '__main__':
    main()
