# -*- coding: utf-8 -*-
import sys, json, time
sys.path.insert(0, "F:/aitoptools/scripts")
import gsc_query as g
import requests
token = g.get_token()
def q(start, end, dims):
    body = {"startDate": start, "endDate": end, "dimensions": dims, "rowLimit": 5000, "orderBy": "impressions"}
    r = requests.post(g.GSC, json=body, headers={"Authorization": "Bearer " + token}, proxies=g.PROXIES, timeout=90)
    r.raise_for_status()
    return r.json().get("rows", [])
base = q("2026-08-04", "2026-08-09", ["query"])
cur  = q("2026-08-10", "2026-08-16", ["query"])
with open("F:/aitoptools/.hermes/tmp/geo-0819-gsc-full.tsv", "w", encoding="utf-8", newline="\n") as f:
    f.write("# GEO-0819 GSC compare | BASE 2026-08-04..08-09 | CUR 2026-08-10..08-16\n")
    for r in sorted(base, key=lambda x: -x["impressions"]):
        k = r["keys"][0].replace("\t", " ")
        f.write("BASE\t%s\timp=%d\tclick=%d\tpos=%.1f\n" % (k, r["impressions"], r["clicks"], r["position"]))
    for r in sorted(cur, key=lambda x: -x["impressions"]):
        k = r["keys"][0].replace("\t", " ")
        f.write("CUR\t%s\timp=%d\tclick=%d\tpos=%.1f\n" % (k, r["impressions"], r["clicks"], r["position"]))
print("OK rows base=%d cur=%d" % (len(base), len(cur)))
