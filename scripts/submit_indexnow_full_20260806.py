# -*- coding: utf-8 -*-
"""8/6 P0-1: 全量推送 730 URL (sitemap.xml 531 + sitemap-programmatic.xml 199, 去重后应 ≈730)
复用 submit-indexnow.py 的 key 加载与提交逻辑, 合并两个 sitemap 的 URL。"""
import json, re, sys, time
from pathlib import Path

ROOT = Path(r"F:\aitoptools")
SECRETS_DIR = ROOT / ".hermes" / "secrets"
KEY_FILE = SECRETS_DIR / "indexnow-key.txt"
LOG_DIR = ROOT / ".hermes" / "logs"

import urllib.request

def load_api_key():
    if KEY_FILE.exists():
        key = KEY_FILE.read_text(encoding="utf-8").strip()
        if key and not key.startswith("#"):
            return key
    return None

def parse_sitemap(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    urls = re.findall(r"<loc>([^<]+)</loc>", text)
    out = []
    for u in urls:
        u = u.strip()
        if "aitoptools.net" in u:
            out.append(u)
    return out

def submit(urls, api_key, dry_run=False):
    endpoint = "https://api.indexnow.org/indexnow"
    payload = {"host": "aitoptools.net", "key": api_key, "keyLocation": f"https://aitoptools.net/{api_key}.txt", "urlList": urls}
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=body, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    if dry_run:
        return {"status": "dry-run", "url_count": len(urls)}
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return {"status": resp.status, "url_count": len(urls)}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.read().decode("utf-8", errors="replace")[:300], "url_count": len(urls)}
    except Exception as e:
        return {"status": "EXC", "error": str(e)[:200], "url_count": len(urls)}

key = load_api_key()
if not key:
    print("NO KEY — .hermes/secrets/indexnow-key.txt missing or empty")
    sys.exit(1)
print(f"key loaded: {key[:8]}... (len={len(key)})")

s1 = parse_sitemap(ROOT / "out" / "sitemap.xml")
s2 = parse_sitemap(ROOT / "out" / "sitemap-programmatic.xml")
merged = list(dict.fromkeys(s1 + s2))  # 去重保序
print(f"sitemap.xml: {len(s1)} | programmatic: {len(s2)} | merged dedup: {len(merged)}")

dry = "--dry-run" in sys.argv
if dry:
    print("DRY RUN — no POST sent")
    print(json.dumps({"url_count": len(merged), "first_3": merged[:3], "last_3": merged[-3:]}, ensure_ascii=False, indent=1))
    sys.exit(0)

# 分批提交 (IndexNow 单批上限 10000, 730 一批即可; 但为稳妥按 400/批)
BATCH = 400
results = []
for i in range(0, len(merged), BATCH):
    chunk = merged[i:i + BATCH]
    r = submit(chunk, key)
    results.append(r)
    print(f"batch {i//BATCH+1}: {len(chunk)} urls -> status {r.get('status')} {r.get('error','')}")
    if i + BATCH < len(merged):
        time.sleep(2)

ok = sum(1 for r in results if r.get("status") == 200)
total = sum(r.get("url_count", 0) for r in results)
print(f"\nTOTAL: {total} urls | HTTP 200 batches: {ok}/{len(results)}")

# 写日志
LOG_DIR.mkdir(parents=True, exist_ok=True)
log = LOG_DIR / f"indexnow-2026-08-06-full.log"
with log.open("w", encoding="utf-8") as f:
    json.dump({"date": "2026-08-06", "total_urls": total, "batches": results, "url_sample": merged[:5]}, f, ensure_ascii=False, indent=1)
print(f"log: {log}")
