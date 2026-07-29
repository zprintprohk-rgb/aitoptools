"""
submit-gsc-sitemap.py — Submit sitemap to Google Search Console + optionally push
top URLs via Indexing API for faster indexing.

Two modes:
    A) Sitemap submission (PUT) — tells GSC "this is my sitemap URL, please crawl it"
       Endpoint: webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}
       Scope: https://www.googleapis.com/auth/webmasters
       Auth: OAuth 2.0 user-context (one-time setup, refresh token reusable)
    B) Indexing API (POST) — request immediate indexing for individual URLs
       Endpoint: indexing/v3/urlNotifications:publish
       Scope: https://www.googleapis.com/auth/indexing
       Auth: Service account JSON (recommended for automation) OR OAuth user
       Limit: 200 publish + 100 metadataUpdate per day

Auth setup (one-time, user does in browser):
    1. OAuth client: https://console.cloud.google.com/apis/credentials
       - Create OAuth 2.0 Client ID (Desktop app or Web app)
       - Enable Search Console API + Indexing API in same project
    2. Get refresh token (one-time auth flow, e.g. via Google OAuth Playground)
    3. Save to .hermes/secrets/gsc-oauth.json:
       {
         "client_id": "...",
         "client_secret": "...",
         "refresh_token": "...",
         "site_url": "sc-domain:aitoptools.net"
       }
    4. Run: python scripts/submit-gsc-sitemap.py --dry-run  (verify config)
    5. Run: python scripts/submit-gsc-sitemap.py            (real submit)

Output log: .hermes/logs/gsc-submit-YYYY-MM-DD.log

Reference:
    https://developers.google.com/webmasters/v1/sitemaps/submit
    https://developers.google.com/search/apis/indexing-api/v3/quickstart
"""
import re
import sys
import os
import json
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
SITEMAP_PATH = ROOT / "out" / "sitemap.xml"
SITEMAP_URL = "https://aitoptools.net/sitemap.xml"
SECRETS_DIR = ROOT / ".hermes" / "secrets"
OAUTH_FILE = SECRETS_DIR / "gsc-oauth.json"
LOG_DIR = ROOT / ".hermes" / "logs"
DEFAULT_SITE_URL = "sc-domain:aitoptools.net"

TOKEN_URL = "https://oauth2.googleapis.com/token"
GSC_API_BASE = "https://www.googleapis.com/webmasters/v3"
INDEXING_API = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def load_oauth_config():
    """Read OAuth config from .hermes/secrets/gsc-oauth.json (gitignored)."""
    if not OAUTH_FILE.exists():
        raise FileNotFoundError(
            f"OAuth config not found: {OAUTH_FILE}\n"
            f"See header docstring for one-time setup.\n"
            f"Quick path: use Google OAuth Playground (https://developers.google.com/oauthplayground/)\n"
            f"  - Step 1: Select scopes: webmasters + indexing\n"
            f"  - Step 2: Authorize APIs\n"
            f"  - Step 3: Exchange authorization code for tokens\n"
            f"  - Copy the refresh_token into the JSON config file"
        )
    return json.loads(OAUTH_FILE.read_text(encoding="utf-8"))


def get_access_token(cfg):
    """Exchange refresh_token for short-lived access_token (1 hour)."""
    data = urllib.parse.urlencode({
        "client_id": cfg["client_id"],
        "client_secret": cfg["client_secret"],
        "refresh_token": cfg["refresh_token"],
        "grant_type": "refresh_token",
    }).encode("utf-8")
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    return body["access_token"]


def submit_sitemap(token, site_url, feedpath):
    """PUT sitemap to GSC."""
    url = f"{GSC_API_BASE}/sites/{urllib.parse.quote(site_url, safe='')}/sitemaps/{urllib.parse.quote(feedpath, safe='')}"
    req = urllib.request.Request(url, method="PUT",
                                 headers={"Authorization": f"Bearer {token}", "Content-Length": "0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def submit_url_indexing(token, page_url, action="URL_UPDATED"):
    """Publish URL via Indexing API. action in {URL_UPDATED, URL_DELETED}."""
    payload = json.dumps({"url": page_url, "type": action}).encode("utf-8")
    req = urllib.request.Request(INDEXING_API, data=payload, method="POST",
                                 headers={"Authorization": f"Bearer {token}",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def parse_sitemap(path):
    if not path.exists():
        raise FileNotFoundError(
            f"Sitemap not found: {path}\n"
            f"Run `npm run build` first."
        )
    text = path.read_text(encoding="utf-8")
    urls = re.findall(r"<loc>([^<]+)</loc>", text)
    seen = set()
    unique = []
    for u in urls:
        if "aitoptools.net" in u and u not in seen:
            seen.add(u)
            unique.append(u)
    return unique


def write_log(result):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"gsc-submit-{datetime.now().strftime('%Y-%m-%d')}.log"
    ts = datetime.now(timezone.utc).isoformat()
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{ts} {json.dumps(result, ensure_ascii=False)}\n")
    return log_path


def main():
    dry_run = "--dry-run" in sys.argv
    submit_indexing = "--with-indexing" in sys.argv
    site_url = os.environ.get("GSC_SITE_URL", DEFAULT_SITE_URL)
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] GSC sitemap submission starting")
    print(f"  site_url     = {site_url}")
    print(f"  sitemap_url  = {SITEMAP_URL}")
    print(f"  dry_run      = {dry_run}")
    print(f"  with_indexing= {submit_indexing}")
    try:
        cfg = load_oauth_config()
    except FileNotFoundError as e:
        print(f"\nERROR: {e}")
        sys.exit(1)
    if dry_run:
        print(f"\n  Config loaded (no API call):")
        print(f"    client_id     = {cfg.get('client_id', 'MISSING')[:20]}...")
        print(f"    has_secret    = {bool(cfg.get('client_secret'))}")
        print(f"    has_refresh   = {bool(cfg.get('refresh_token'))}")
        print(f"    site_url      = {cfg.get('site_url', site_url)}")
        print(f"  (--dry-run complete — no API call sent)")
        return
    token = get_access_token(cfg)
    print(f"  ✓ Access token acquired (length {len(token)})")
    # Step 1: Sitemap submission
    status, body = submit_sitemap(token, site_url, SITEMAP_URL)
    print(f"  Sitemap PUT: status={status}")
    print(f"    body: {body[:300]}")
    result = {
        "sitemap_submit": {"status": status, "body": body[:500]},
        "indexing_requests": [],
    }
    # Step 2: Indexing API for top URLs (optional)
    if submit_indexing:
        urls = parse_sitemap(SITEMAP_PATH)
        # Top 10 = root + 4 best-* + 4 compare-* + 1 about
        top = [u for u in urls if u.count("/") <= 4][:10]
        print(f"\n  Indexing API: requesting {len(top)} top URLs")
        for u in top:
            status, body = submit_url_indexing(token, u)
            print(f"    {u[:70]:70s} → {status} {body[:80]}")
            result["indexing_requests"].append({"url": u, "status": status, "body": body[:200]})
    log_path = write_log(result)
    print(f"\n  Log: {log_path}")
    if result["sitemap_submit"]["status"] in (200, 204):
        print(f"\n  ✓ Sitemap submitted to Google Search Console")
    else:
        print(f"\n  ⚠ Submission may have failed. Check log.")


if __name__ == "__main__":
    main()
