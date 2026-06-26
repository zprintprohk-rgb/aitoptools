#!/usr/bin/env python3
"""
Playwright Auto Screenshot Capture for AI Tool Reviews
======================================================
Captures homepage + pricing page screenshots of tool websites,
compresses to lightweight WebP, returns image paths.

Usage:
  python scripts/capture-screenshot.py                    # Default: Jasper AI
  python scripts/capture-screenshot.py --slug synthesia   # Specific tool
  python scripts/capture-screenshot.py --all              # All unpublished tools
  python scripts/capture-screenshot.py --status           # Check screenshot dir
"""

import asyncio, json, os, sys, argparse

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_FILE = os.path.join(PROJ, "scripts", "tool-params.json")
REVIEWS_FILE = os.path.join(PROJ, "src", "data", "reviews.json")
IMG_DIR = os.path.join(PROJ, "public", "tool-screenshots")


def load_params():
    with open(PARAMS_FILE, encoding="utf-8") as f:
        return json.load(f)


def load_reviews():
    with open(REVIEWS_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_published_slugs():
    reviews = load_reviews()
    slugs = set()
    for r in reviews:
        slug = r["slug"]
        if slug.endswith("-review"):
            slug = slug[:-7]
        slugs.add(slug)
    return slugs


def compress_webp(input_path: str, output_path: str = None, quality=70):
    """Compress image to lightweight WebP."""
    try:
        from PIL import Image
        im = Image.open(input_path)
        out = output_path or input_path
        im.save(out, "webp", quality=quality)
        size_kb = os.path.getsize(out) / 1024
        return size_kb
    except Exception as e:
        print(f"  [ERR] WebP compress failed: {e}")
        return 0


async def capture_tool_images(tool_name: str, official_url: str, slug: str) -> list:
    """
    Capture 2 screenshots: homepage + pricing page.
    Returns list of relative paths like ["/tool-screenshots/xxx-home.webp", ...]
    """
    safe_name = slug or tool_name.lower().replace(" ", "-").replace(".", "")
    img_paths = []

    os.makedirs(IMG_DIR, exist_ok=True)

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print(f"  ⚠ Playwright not installed. Run: pip install playwright && playwright install chromium")
        return []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        try:
            # Screenshot 1: Homepage
            print(f"  [CAP] Capturing homepage: {official_url}")
            await page.goto(official_url, timeout=20000, wait_until="domcontentloaded")
            await asyncio.sleep(2)  # Let animations settle

            png_path = os.path.join(IMG_DIR, f"{safe_name}-home.png")
            webp_path = os.path.join(IMG_DIR, f"{safe_name}-home.webp")
            await page.screenshot(path=png_path, full_page=False)
            compress_webp(png_path, webp_path)
            os.remove(png_path)
            rel_path = f"/tool-screenshots/{safe_name}-home.webp"
            img_paths.append(rel_path)
            size_kb = os.path.getsize(webp_path) / 1024
            print(f"     [OK] Homepage: {rel_path} ({size_kb:.0f}KB)")

            # Screenshot 2: Pricing page
            pricing_urls = [
                official_url.rstrip("/") + "/pricing",
                official_url.rstrip("/") + "/plans",
                official_url.rstrip("/") + "/plans-pricing",
            ]
            pricing_captured = False
            for pu in pricing_urls:
                try:
                    print(f"  [CAP] Trying pricing: {pu}")
                    await page.goto(pu, timeout=10000, wait_until="domcontentloaded")
                    await asyncio.sleep(1.5)
                    png_path = os.path.join(IMG_DIR, f"{safe_name}-pricing.png")
                    webp_path = os.path.join(IMG_DIR, f"{safe_name}-pricing.webp")
                    await page.screenshot(path=png_path, full_page=False)
                    compress_webp(png_path, webp_path)
                    os.remove(png_path)
                    rel_path = f"/tool-screenshots/{safe_name}-pricing.webp"
                    img_paths.append(rel_path)
                    size_kb = os.path.getsize(webp_path) / 1024
                    print(f"     [OK] Pricing: {rel_path} ({size_kb:.0f}KB)")
                    pricing_captured = True
                    break
                except Exception:
                    continue

            if not pricing_captured:
                # Fallback: try clicking "Pricing" link on homepage
                try:
                    print(f"  [CAP] Trying click 'Pricing' link on homepage")
                    await page.goto(official_url, timeout=10000, wait_until="domcontentloaded")
                    pricing_link = page.locator('a:has-text("Pricing")').first
                    if await pricing_link.count() > 0:
                        await pricing_link.click(timeout=5000)
                        await asyncio.sleep(2)
                        png_path = os.path.join(IMG_DIR, f"{safe_name}-pricing.png")
                        webp_path = os.path.join(IMG_DIR, f"{safe_name}-pricing.webp")
                        await page.screenshot(path=png_path, full_page=False)
                        compress_webp(png_path, webp_path)
                        os.remove(png_path)
                        rel_path = f"/tool-screenshots/{safe_name}-pricing.webp"
                        img_paths.append(rel_path)
                        size_kb = os.path.getsize(webp_path) / 1024
                        print(f"     [OK] Pricing (click): {rel_path} ({size_kb:.0f}KB)")
                    else:
                        print(f"     [SKIP] No pricing link found")
                except Exception as e:
                    print(f"     ⚠ Pricing click failed: {e}")

        except Exception as e:
            print(f"  ❌ Screenshot failed for {tool_name}: {e}")

        await browser.close()

    return img_paths


def get_tool_screenshots(tool_name: str, official_url: str, slug: str = None) -> list:
    """Synchronous entry point called from generate-article.py."""
    return asyncio.run(capture_tool_images(tool_name, official_url, slug))


def status_report():
    """Show screenshot directory status."""
    os.makedirs(IMG_DIR, exist_ok=True)
    files = [f for f in os.listdir(IMG_DIR) if f.endswith(".webp")]
    total_kb = sum(os.path.getsize(os.path.join(IMG_DIR, f)) for f in files) / 1024
    print(f"📸 Screenshot Directory: {IMG_DIR}")
    print(f"   Total images: {len(files)}")
    print(f"   Total size:   {total_kb:.0f}KB")
    if files:
        print(f"\n   Files:")
        for f in sorted(files):
            sz = os.path.getsize(os.path.join(IMG_DIR, f)) / 1024
            print(f"     {f:<45} {sz:.0f}KB")


def main():
    parser = argparse.ArgumentParser(description="AI Tool Screenshot Capturer")
    parser.add_argument("--slug", help="Tool slug to capture (e.g. 'synthesia')")
    parser.add_argument("--all", action="store_true", help="Capture all unpublished tools")
    parser.add_argument("--status", action="store_true", help="Show screenshot directory status")
    args = parser.parse_args()

    if args.status:
        status_report()
        return

    if args.all:
        data = load_params()
        published = get_published_slugs()
        pending = [t for t in data["tools"] if t["slug"] not in published]
        print(f"📸 Capturing screenshots for {len(pending)} unpublished tools...")
        for t in pending:
            print(f"\n--- {t['name']} ---")
            paths = get_tool_screenshots(t["name"], t.get("official_url", t.get("visitUrl", "")), t["slug"])
            print(f"   Result: {len(paths)} images captured")
        return

    if args.slug:
        data = load_params()
        tool = next((t for t in data["tools"] if t["slug"] == args.slug), None)
    else:
        data = load_params()
        tool = data["tools"][0]  # Default: first tool

    if not tool:
        print(f"Tool '{args.slug}' not found")
        sys.exit(1)

    print(f"📸 Capturing: {tool['name']}")
    url = tool.get("official_url") or tool.get("visitUrl", "")
    print(f"   URL: {url}")
    paths = get_tool_screenshots(tool["name"], url, tool["slug"])
    print(f"\n✅ Result: {len(paths)} images")
    for p in paths:
        full = os.path.join(PROJ, "public", p.lstrip("/"))
        size = os.path.getsize(full) / 1024 if os.path.exists(full) else 0
        print(f"   📍 {p} ({size:.0f}KB)")


if __name__ == "__main__":
    main()
