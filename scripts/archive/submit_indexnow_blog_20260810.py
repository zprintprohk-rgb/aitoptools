# -*- coding: utf-8 -*-
"""8/10: IndexNow 增量推新 blog URL (printful-printify-merger-fyul-2026) + 更新对比页
复用 submit_indexnow_blog_20260808.py 的 key 加载与提交逻辑。"""
import json, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(r"F:\aitoptools")
KEY_FILE = ROOT / ".hermes" / "secrets" / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

BLOG_URLS = [
    "https://aitoptools.net/blog/printful-printify-merger-fyul-2026/",
    "https://aitoptools.net/compare/printful-vs-printify/",
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
    log_path = LOG_DIR / "indexnow-2026-08-10.log"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("\n=== hermes 19:5x 增量推送 (blog+compare) ===\n")
        f.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("IndexNow result:", json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
