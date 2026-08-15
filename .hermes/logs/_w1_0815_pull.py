# -*- coding: utf-8 -*-
import sys, json, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'F:\aitoptools\scripts')
import gsc_query as gq

TARGETS = ["sticker mule", "runway", "print price", "printful alternatives", "printify alternatives",
           "is magicdrop legit", "kittl", "jasper ai review", "midjourney review", "manychat shopify", "copy ai"]

def pull_queries(start, end):
    body = {
        "startDate": start, "endDate": end,
        "dimensions": ["query"], "rowLimit": 5000, "orderBy": "impressions",
    }
    r = gq.requests.post(gq.GSC, json=body, headers={"Authorization": "Bearer " + gq.get_token()},
                         proxies=gq.PROXIES, timeout=30)
    r.raise_for_status()
    rows = r.json().get("rows", [])
    out = {}
    for row in rows:
        q = row["keys"][0].lower()
        for t in TARGETS:
            if t in q:
                out.setdefault(q, []).append({
                    "imps": row["impressions"], "clicks": row["clicks"],
                    "ctr": row["ctr"], "pos": row["position"]
                })
                break
    return out

def pull_dates(start, end):
    body = {
        "startDate": start, "endDate": end,
        "dimensions": ["date"], "rowLimit": 100, "orderBy": "date",
    }
    r = gq.requests.post(gq.GSC, json=body, headers={"Authorization": "Bearer " + gq.get_token()},
                         proxies=gq.PROXIES, timeout=30)
    r.raise_for_status()
    return r.json().get("rows", [])

def pull_urls(start, end, pages):
    body = {
        "startDate": start, "endDate": end,
        "dimensions": ["page"], "rowLimit": 5000, "orderBy": "impressions",
    }
    r = gq.requests.post(gq.GSC, json=body, headers={"Authorization": "Bearer " + gq.get_token()},
                         proxies=gq.PROXIES, timeout=30)
    r.raise_for_status()
    rows = r.json().get("rows", [])
    out = {}
    for row in rows:
        p = row["keys"][0]
        if any(x in p for x in pages):
            out[p] = {"imps": row["impressions"], "clicks": row["clicks"], "ctr": row["ctr"], "pos": row["position"]}
    return out

tok = gq.get_token()

print("=== W1 window 8/6..8/13 (T+2 merge, T+7 full) ===")
q1 = pull_queries("2026-08-06", "2026-08-13")
for k, v in sorted(q1.items()):
    print(json.dumps({"q": k, "rows": v}, ensure_ascii=False))

print("=== W2 window 8/8..8/14 (T+7 strict for #1/#2, matches sentinel) ===")
q2 = pull_queries("2026-08-08", "2026-08-14")
for k, v in sorted(q2.items()):
    print(json.dumps({"q": k, "rows": v}, ensure_ascii=False))

print("=== DATES 8/6..8/13 ===")
d = pull_dates("2026-08-06", "2026-08-13")
for row in d:
    print(row["keys"][0], "imp=" + str(row["impressions"]), "clk=" + str(row["clicks"]), "pos=" + str(round(row["position"],2)))

print("=== URLS 8/6..8/13 ===")
u1 = pull_urls("2026-08-06", "2026-08-13", ["stickermule-review", "runway-ml-review"])
for p, v in sorted(u1.items()):
    print(p, json.dumps(v))

print("=== URLS 8/8..8/14 ===")
u2 = pull_urls("2026-08-08", "2026-08-14", ["stickermule-review", "runway-ml-review"])
for p, v in sorted(u2.items()):
    print(p, json.dumps(v))
