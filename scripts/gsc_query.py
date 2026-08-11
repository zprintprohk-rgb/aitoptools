"""GSC Search Analytics 查询（Service Account，SOCKS5 代理）

用法:
  python scripts/gsc_query.py days N          # 最近 N 天按日聚合
  python scripts/gsc_query.py queries days N  # 最近 N 天 query 维度
  python scripts/gsc_query.py urls days N     # 最近 N 天 URL 维度

依赖: PyJWT + requests；密钥 .hermes/secrets/gsc-oauth.json（gitignored）
代理: SOCKS5 127.0.0.1:7892（与 gmail IMAP 同链路，Google API 直连被阻）
"""
import json, sys, time
import jwt, requests
from datetime import date, timedelta

KEY = "F:/aitoptools/.hermes/secrets/gsc-oauth.json"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
TOKEN_URL = "https://oauth2.googleapis.com/token"
GSC = "https://searchconsole.googleapis.com/webmasters/v3/sites/sc-domain%3Aaitoptools.net/searchAnalytics/query"
PROXIES = {"https": "socks5h://127.0.0.1:7892"}


def get_token():
    cred = json.load(open(KEY, encoding="utf-8"))
    now = int(time.time())
    payload = {
        "iss": cred["client_email"],
        "scope": SCOPE,
        "aud": TOKEN_URL,
        "iat": now,
        "exp": now + 3600,
    }
    signed = jwt.encode(payload, cred["private_key"], algorithm="RS256")
    r = requests.post(TOKEN_URL, data={
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": signed,
    }, proxies=PROXIES, timeout=30)
    r.raise_for_status()
    return r.json()["access_token"]


def query(token, days, dims):
    end = date.today() - timedelta(days=1)   # GSC 数据 T+1
    start = end - timedelta(days=days - 1)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dims if dims else ["date"],
        "rowLimit": 250,
        "orderBy": "impressions" if dims else "date",
    }
    r = requests.post(GSC, json=body, headers={"Authorization": f"Bearer {token}"},
                      proxies=PROXIES, timeout=30)
    r.raise_for_status()
    return r.json().get("rows", [])


if __name__ == "__main__":
    args = sys.argv[1:]
    days, dims = 7, []
    if args and args[0] in ("queries", "urls"):
        dims = ["query"] if args[0] == "queries" else ["page"]
        args = args[1:]
    if args and args[0] == "days" and len(args) > 1:
        days = int(args[1])
    token = get_token()
    rows = query(token, days, dims)
    print(f"# GSC sc-domain:aitoptools.net | {days}天 | dims={dims or ['date']} | rows={len(rows)}")
    for r in rows[:40]:
        k = r.get("keys", [""])[0]
        print(f"{k}\timp={int(r['impressions'])}\tclick={int(r['clicks'])}\tctr={r['ctr']:.3f}\tpos={r['position']:.1f}")
