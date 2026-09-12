# -*- coding: utf-8 -*-
"""2026-09-12 daily-content: IndexNow increment for the new Q4 Black Friday pillar.
Reuses the key-loading / state-updating pattern of submit_indexnow_blog_20260829.py.
"""
import json
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(r"F:\aitoptools")
KEY_FILE = ROOT / ".hermes" / "secrets" / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"
STATE = LOG_DIR / "gsc-indexnow-state.json"

BLOG_URLS = [
    "https://aitoptools.net/blog/black-friday-pod-strategy-2026/",
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
        "keyLocation": "https://aitoptools.net/%s.txt" % api_key,
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
        result = {"status": e.code, "url_count": len(BLOG_URLS),
                  "error": e.read().decode("utf-8", "replace")[:300]}
    except Exception as e:
        result = {"status": 0, "url_count": len(BLOG_URLS), "error": str(e)[:300]}

    LOG_DIR.mkdir(exist_ok=True)
    (LOG_DIR / "indexnow-0912-content.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print("INDEXNOW_RESULT:", json.dumps(result, ensure_ascii=False))

    if result.get("status") in (200, 202):
        try:
            st = json.loads(STATE.read_text(encoding="utf-8"))
            st["indexnow_urls_pushed"] = int(st.get("indexnow_urls_pushed", 0)) + len(BLOG_URLS)
            st["indexnow_status_200"] = int(st.get("indexnow_status_200", 0)) + len(BLOG_URLS)
            st["last_run"] = datetime.now(timezone.utc).isoformat()
            st["last_run_status"] = "ok"
            st["content_cron_0912"] = "black-friday-pod-strategy-2026 pushed via IndexNow"
            STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding="utf-8")
            print("STATE_UPDATED: indexnow_urls_pushed =", st["indexnow_urls_pushed"])
        except Exception as e:
            print("STATE_UPDATE_ERR:", e)
            return 2
    return 0 if result.get("status") in (200, 202) else 3


if __name__ == "__main__":
    raise SystemExit(main())
