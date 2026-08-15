# -*- coding: utf-8 -*-
import io, sys, json, os, ssl, urllib.request, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9'}
sites = [
    ('AIxploria', 'https://www.aixploria.com/en/add-tool/'),
    ('AI Tools Directory', 'https://aitoolsdirectory.com/submit-tool'),
    ('AIChief', 'https://aichief.com/submit/'),
    ('AI Hunt List', 'https://aihuntlist.com/submit-tool/'),
    ('AITopTools (aitoptools.com)', 'https://aitoptools.com/submit/'),
    ('AllThingsAI', 'https://allthingsai.com/submit/'),
    ('AI Valley', 'https://aivalley.ai/submit/'),
    ('Insidr AI', 'https://www.insidr.ai/ai-tools/submit'),
    ('OpenTools', 'https://opentools.ai/'),
    ('FutureTools', 'https://www.futuretools.io/submit'),
    ('Startuplist.in (retry)', 'https://startuplist.in/submit'),
    ('ProductCool', 'https://www.productcool.com/submit'),
]
results = []
os.makedirs(r'.hermes\tmp\linkbuild-0823', exist_ok=True)
for name, url in sites:
    r = {'site': name, 'url': url}
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=8, context=ctx) as resp:
            html = resp.read(300000).decode('utf-8', 'ignore')
            r['http'] = resp.status
        low = html.lower()
        markers = []
        if 'captcha' in low or 'turnstile' in low or 'hcaptcha' in low or 'recaptcha' in low: markers.append('CAPTCHA')
        if 'cf-challenge' in low or 'challenge-platform' in low or 'just a moment' in low: markers.append('CF_CHALLENGE')
        if 'login' in low and ('sign in' in low or 'log in' in low): markers.append('LOGIN_WALL')
        if 'submit' in low and ('form' in low or 'action=' in low): markers.append('FORM')
        t = re.search(r'<title[^>]*>([^<]{0,80})', html, re.I)
        r['title'] = (t.group(1).strip() if t else '')
        r['markers'] = markers
        r['verdict'] = 'BLOCKED_BY_CAPTCHA' if ('CAPTCHA' in markers or 'CF_CHALLENGE' in markers) else ('BLOCKED_NEEDS_LOGIN' if 'LOGIN_WALL' in markers else ('PROBE_OK' if 'FORM' in markers or 'submit' in low else 'NO_FORM_DETECTED'))
    except Exception as e:
        r['error'] = str(e)[:120]
        r['verdict'] = 'BLOCKED_CONNECTION'
    results.append(r)
    print(f"{name:34s} {r.get('verdict','?'):24s} http={r.get('http','-')} {r.get('title','')[:50]}")
json.dump(results, open(r'.hermes\tmp\linkbuild-0823\probes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved .hermes/tmp/linkbuild-0823/probes.json')
