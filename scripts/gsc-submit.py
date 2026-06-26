#!/usr/bin/env python3
"""
Google Search Console URL Index Submission
=========================================
Submits new article URLs to Google Indexing API for instant indexing.
Only active when production domain is bound - auto-skips pages.dev domain.

Setup (after domain is bought + verified in GSC):
  1. Go to https://console.cloud.google.com/apis/credentials
  2. Create Service Account -> download JSON key
  3. In GSC -> Settings -> Users -> Add service account as Owner
  4. Set GSC_API_KEY below or as env var GSC_API_KEY

Usage:
  python scripts/gsc-submit.py                              # Status check (dry run)
  python scripts/gsc-submit.py --slug synthesia-review      # Submit single page
  python scripts/gsc-submit.py --all                        # Submit all published pages
  python scripts/gsc-submit.py --enable                     # Print setup guide
"""

import json, os, sys, argparse

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEWS_FILE = os.path.join(PROJ, "src", "data", "reviews.json")

# ========================
# CONFIG - Fill after domain bound + GSC verified
# ========================
GSC_API_KEY = os.environ.get("GSC_API_KEY", "")
PRODUCTION_DOMAIN = os.environ.get("SITE_DOMAIN", "https://aitoptools.net")


def is_production_ready():
    if "pages.dev" in PRODUCTION_DOMAIN or "localhost" in PRODUCTION_DOMAIN:
        return False
    if not GSC_API_KEY:
        return False
    return True


def load_reviews():
    with open(REVIEWS_FILE, encoding="utf-8") as f:
        return json.load(f)


def submit_url(page_url):
    if not is_production_ready():
        return {"status": "skipped", "reason": "domain_not_ready", "url": page_url}

    import requests
    try:
        resp = requests.post(
            f"https://indexing.googleapis.com/v3/urlNotifications:publish?key={GSC_API_KEY}",
            json={"url": page_url, "type": "URL_UPDATED"},
            timeout=15
        )
        if resp.status_code == 200:
            print(f"  [GSC] Submitted: {page_url}")
            return {"status": "submitted", "url": page_url}
        else:
            print(f"  [GSC] Error {resp.status_code}: {resp.text[:200]}")
            return {"status": "error", "code": resp.status_code, "url": page_url}
    except Exception as e:
        print(f"  [GSC] Failed: {e}")
        return {"status": "error", "error": str(e), "url": page_url}


def submit_all():
    reviews = load_reviews()
    results = []
    ready = is_production_ready()

    print(f"\nGSC Index Submission")
    print(f"  Domain: {PRODUCTION_DOMAIN}")
    print(f"  Pages:  {len(reviews)}")
    print(f"  Status: {'ACTIVE' if ready else 'SKIPPED (domain not ready)'}")

    for r in reviews:
        results.append(submit_url(f"{PRODUCTION_DOMAIN}/{r['slug']}"))

    sub = sum(1 for r in results if r.get("status") == "submitted")
    skp = sum(1 for r in results if r.get("status") == "skipped")
    err = sum(1 for r in results if r.get("status") == "error")
    print(f"\n  Summary: {sub} submitted, {skp} skipped, {err} errors")
    return results


def print_setup_guide():
    print("""
GSC Indexing API Setup Guide:
  1. Go to https://console.cloud.google.com/
  2. Create a project (or select existing)
  3. Enable the Indexing API (search 'Indexing API' -> Enable)
  4. Create Service Account: APIs & Services -> Credentials -> Create Credentials -> Service Account
  5. Download the JSON key (contains client_email)
  6. In Google Search Console: Settings -> Users and permissions -> Add user
     Enter the service account email -> Permission: Owner (full)
  7. Export the API key: set GSC_API_KEY=...
  8. Update PRODUCTION_DOMAIN to your domain (e.g. https://aitoptools.net)
  9. Run: python scripts/gsc-submit.py --all
""")


def main():
    parser = argparse.ArgumentParser(description="GSC URL Index Submitter")
    parser.add_argument("--slug", help="Single review slug (e.g. 'synthesia-review')")
    parser.add_argument("--all", action="store_true", help="Submit all pages")
    parser.add_argument("--enable", action="store_true", help="Print setup guide")
    parser.add_argument("--status", action="store_true", help="Check config status")
    args = parser.parse_args()

    if args.enable:
        print_setup_guide()
        return

    if args.status:
        ready = is_production_ready()
        print(f"\nGSC Config:")
        print(f"  Domain:     {PRODUCTION_DOMAIN}")
        print(f"  API Key:    {'SET' if GSC_API_KEY else 'NOT SET'}")
        print(f"  Temp pages.dev: {'YES (skip)' if 'pages.dev' in PRODUCTION_DOMAIN else 'NO'}")
        print(f"  Ready:      {'GREEN' if ready else 'RED'}")
        if not ready:
            print(f"\n  Need to do:")
            if "pages.dev" in PRODUCTION_DOMAIN:
                print(f"    1. Buy domain (aitoptools.net)")
                print(f"    2. Set env SITE_DOMAIN=https://aitoptools.net")
            if not GSC_API_KEY:
                print(f"    3. Set GSC_API_KEY env var")
                print(f"    4. Run 'python scripts/gsc-submit.py --enable' for guide")
        return

    if args.slug:
        print(json.dumps(submit_url(f"{PRODUCTION_DOMAIN}/{args.slug}"), indent=2))
        return

    if args.all:
        submit_all()
        return

    # Default: show status
    if not is_production_ready():
        print(f"\nGSC submission: SKIPPED (domain {PRODUCTION_DOMAIN} not production)")
        print(f"Run 'python scripts/gsc-submit.py --status' for details")
    else:
        submit_all()


if __name__ == "__main__":
    main()
