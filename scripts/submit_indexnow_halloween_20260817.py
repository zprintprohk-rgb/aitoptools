# -*- coding: utf-8 -*-
"""8/17 W3 Halloween 集群全量 push 后 IndexNow 增量推 5 篇集群页
复用 submit_indexnow_blog_20260808.py 的 key 加载与提交逻辑。"""
import json, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(r"F:\aitoptools")
KEY_FILE = ROOT / ".hermes" / "secrets" / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

BLOG_URLS = [
    "https://aitoptools.net/blog/halloween-shirt-designs-2026/",
    "https://aitoptools.net/blog/halloween-sublimation-2026/",
    "https://aitoptools.net/blog/halloween-pod-ideas-2026/",
    "https://aitoptools.net/blog/printful-vs-printify-halloween-2026/",
    "https://aitoptools.net/blog/kittl-halloween-template-test-2026/",
]

def load_api_key():
    if KEY_FILE.exists():
        key = KEY_FILE.read_text(encoding="utf-8").strip()
        if key and not key.startswith("#"):
            return key
    return None

def main():
    api_key = load_api_key()
    if not api_key:
        print("ERROR: indexnow key missing")
        return 1
    payload = {
        "host": "aitoptools.net",
        "key": api_key,
        "keyLocation": f"https://aitoptools.net/{api_key}.txt",
        "urlList": BLOG_URLS,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=body,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = {"status": resp.status, "url_count": len(BLOG_URLS), "urls": BLOG_URLS}
    except urllib.error.HTTPError as e:
        result = {"status": e.code, "url_count": len(BLOG_URLS), "error": e.read().decode("utf-8", "replace")[:300]}
    LOG_DIR.mkdir(exist_ok=True)
    log_line = json.dumps({"date": "2026-08-17", "action": "HALLOWEEN-FULL-0825", **result}, ensure_ascii=False)
    (LOG_DIR / "indexnow-2026-08-17-halloween.log").write_text(log_line + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == 200 else 1

if __name__ == "__main__":
    raise SystemExit(main())