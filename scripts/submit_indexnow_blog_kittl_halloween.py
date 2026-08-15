# -*- coding: utf-8 -*-
"""8/17 辐条① Kittl Halloween: IndexNow 增量推 1 个新 blog URL (模式同 submit_indexnow_boost_0817.py)"""
import json, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(r"F:\aitoptools")
KEY_FILE = ROOT / ".hermes" / "secrets" / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

BLOG_URLS = [
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
        with urllib.request.urlopen(req, timeout=20) as resp:
            print(f"HTTP {resp.status}: {len(BLOG_URLS)} URLs submitted")
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode(errors='replace')[:200]}")
        return 1
    except Exception as e:
        print(f"ERR {e}")
        return 1
    with open(LOG_DIR / "indexnow-2026-08-17.log", "a", encoding="utf-8") as f:
        f.write(f"[spoke1] {', '.join(BLOG_URLS)}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
