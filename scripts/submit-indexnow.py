"""
submit-indexnow.py — Push all 99 URLs from out/sitemap.xml to IndexNow
(Bing + Yandex + Seznam + Naver all consume the same API).

Usage:
    1. Generate API key at https://www.indexnow.org/ekit (one-time, free, no signup)
    2. Save key (e.g. "a1b2c3d4e5f6g7h8") to .hermes/secrets/indexnow-key.txt
    3. Verify key ownership: upload a file named "{key}.txt" to https://aitoptools.net/
       (Bing verifies by fetching this URL — return 200 with key as plain text content)
    4. Run: python scripts/submit-indexnow.py --dry-run   (preview, no POST)
    5. Run: python scripts/submit-indexnow.py              (real submission)

Limits: IndexNow allows up to 10,000 URLs per POST. We have 99 — single request covers all.

Output log: .hermes/logs/indexnow-YYYY-MM-DD.log (one line per run, JSON result)

Env (alternative to file):
    INDEXNOW_API_KEY=...  (overrides .hermes/secrets/indexnow-key.txt)

Reference:
    https://www.indexnow.org/documentation
"""
import re
import sys
import os
import json
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone

# Resolve paths relative to this script (F:\aitoptools\scripts\submit-indexnow.py)
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SITEMAP_PATH = ROOT / "out" / "sitemap.xml"
SECRETS_DIR = ROOT / ".hermes" / "secrets"
KEY_FILE = SECRETS_DIR / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

HOST = "aitoptools.net"
ENDPOINT = "https://api.indexnow.org/indexnow"


def load_api_key():
    """Read API key from .hermes/secrets/indexnow-key.txt (gitignored) or INDEXNOW_API_KEY env."""
    if KEY_FILE.exists():
        key = KEY_FILE.read_text(encoding="utf-8").strip()
        if key and not key.startswith("#"):
            return key
    return os.environ.get("INDEXNOW_API_KEY", "").strip()


def parse_sitemap(path):
    """Extract all <loc> URLs from XML sitemap, dedupe, filter to our host."""
    if not path.exists():
        raise FileNotFoundError(
            f"Sitemap not found: {path}\n"
            f"Run `npm run build` first to generate out/."
        )
    text = path.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>([^<]+)</loc>", text)
    # Dedupe (preserve order) + filter to our host
    seen = set()
    unique = []
    for u in urls:
        if HOST in u and u not in seen:
            seen.add(u)
            unique.append(u)
    return unique


def submit(urls, api_key, dry_run=False):
    """POST urls to IndexNow endpoint."""
    if not api_key:
        raise ValueError(
            "API key not set. Either:\n"
            f"  - Save key to {KEY_FILE}\n"
            "  - Or set INDEXNOW_API_KEY env var\n"
            "Get a free key at https://www.indexnow.org/ekit"
        )
    key_location = f"https://{HOST}/{api_key}.txt"
    payload = {
        "host": HOST,
        "key": api_key,
        "keyLocation": key_location,
        "urlList": urls,
    }
    if dry_run:
        return {
            "dry_run": True,
            "host": HOST,
            "keyLocation": key_location,
            "url_count": len(urls),
            "endpoint": ENDPOINT,
            "first_5_urls": urls[:5],
            "last_5_urls": urls[-5:],
        }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = resp.read().decode("utf-8", errors="replace")
            return {"status": status, "body": body, "url_count": len(urls)}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"status": e.code, "error": body, "url_count": len(urls)}


def write_log(result):
    """Append result line to .hermes/logs/indexnow-YYYY-MM-DD.log."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"indexnow-{datetime.now().strftime('%Y-%m-%d')}.log"
    ts = datetime.now(timezone.utc).isoformat()
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{ts} {json.dumps(result, ensure_ascii=False)}\n")
    return log_path


def main():
    dry_run = "--dry-run" in sys.argv
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] IndexNow submission starting")
    print(f"  host    = {HOST}")
    print(f"  sitemap = {SITEMAP_PATH}")
    print(f"  dry_run = {dry_run}")
    urls = parse_sitemap(SITEMAP_PATH)
    print(f"  urls    = {len(urls)} (deduped, host-filtered)")
    api_key = load_api_key()
    if not api_key:
        print(f"\nERROR: API key not set.")
        print(f"  Save to {KEY_FILE}  (e.g. 'a1b2c3d4e5f6g7h8')")
        print(f"  Or set env: INDEXNOW_API_KEY=...")
        print(f"  Get a free key at https://www.indexnow.org/ekit")
        sys.exit(1)
    print(f"  key     = {api_key[:4]}...{api_key[-4:]} (length {len(api_key)})")
    result = submit(urls, api_key, dry_run)
    print(f"\n  Result: {json.dumps(result, indent=2, ensure_ascii=False)[:1500]}")
    log_path = write_log(result)
    print(f"  Log:    {log_path}")
    if isinstance(result, dict) and result.get("status") == 200:
        print(f"\n  ✓ {result['url_count']} URLs submitted to IndexNow (Bing + Yandex + Seznam + Naver)")
    elif dry_run:
        print(f"\n  (dry_run complete — no POST sent)")
    else:
        print(f"\n  ⚠ Submission may have failed. Check log: {log_path}")


if __name__ == "__main__":
    main()
