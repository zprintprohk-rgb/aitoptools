# -*- coding: utf-8 -*-
"""2026-09-12 一次性: 推送 sitemap 遗漏但在线可索引的 URL 到 IndexNow。

背景: generate-sitemap.py 基页清单未含 /compare/* (comparisons.json 派生缺失) 与
partnerships/author 页, 导致 5 个 200 页面从未进入 sitemap 与 IndexNow 队列。
本脚本只做增量提交, 不改 sitemap、不 build、不 push。
"""
import json, re, sys
from pathlib import Path
import urllib.request, urllib.error
from datetime import datetime, timezone

ROOT = Path(r"F:\aitoptools")
KEY_FILE = ROOT / ".hermes" / "secrets" / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

URLS = [
    "https://aitoptools.net/compare/mockey-vs-placeit/",
    "https://aitoptools.net/best/best-ai-tshirt-design-generators/",
    "https://aitoptools.net/best/best-print-on-demand-companies/",
    "https://aitoptools.net/partnerships/",
    "https://aitoptools.net/author/jerome-tang/",
]

key = KEY_FILE.read_text(encoding="utf-8").strip()
if not (key and key.isalnum()):
    print("IndexNow key unavailable/invalid — aborting")
    sys.exit(1)

payload = {
    "host": "aitoptools.net",
    "key": key,
    "keyLocation": "https://aitoptools.net/%s.txt" % key,
    "urlList": URLS,
}
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
result = {"date": "2026-09-12", "run": "orphan-page increment push",
          "url_count": len(URLS), "urls": URLS}
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        result["status"] = resp.status
        result["body"] = resp.read().decode("utf-8", "replace")[:200]
except urllib.error.HTTPError as e:
    result["status"] = e.code
    result["body"] = e.read().decode("utf-8", "replace")[:200]
except Exception as e:
    result["status"] = "error"
    result["body"] = "%s: %s" % (type(e).__name__, str(e)[:200])

LOG_DIR.mkdir(parents=True, exist_ok=True)
out = LOG_DIR / "indexnow-0912-orphans.json"
out.write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
print("status=%s urls=%d log=%s" % (result["status"], len(URLS), out))
