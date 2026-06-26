#!/usr/bin/env python3
"""
AI Tool Article Generator — Hermes Cron Pipeline
=======================================================
Daily cron entry point (7AM) for the aitoptools auto-execution system.

Pipeline:
  1. Find next tool from tool-params.json
  2. Output prompt template for LLM to generate article
  3. [--screenshots] Capture homepage + pricing screenshots via Playwright
  4. [--auto-links] Auto-insert internal links from existing reviews
  5. Update reviews.json with new article
  6. Build -> Deploy -> [GSC submit if domain ready]

Usage:
  python generate-article.py                    # Next tool + Template 1 prompt
  python generate-article.py --screenshots      # Capture screenshots for next tool
  python generate-article.py --auto-links       # Show auto-internal-linking analysis
  python generate-article.py --pipeline         # Full pipeline dry-run
  python generate-article.py --type 2            # Comparison mode
  python generate-article.py --status            # Full status report
  python generate-article.py --all               # List all remaining tools
"""

import json, os, sys, argparse, re, subprocess

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_FILE = os.path.join(PROJ, "scripts", "tool-params.json")
REVIEWS_FILE = os.path.join(PROJ, "src", "data", "reviews.json")
SCREENSHOT_DIR = os.path.join(PROJ, "public", "tool-screenshots")


def load_params():
    with open(PARAMS_FILE, encoding="utf-8") as f:
        return json.load(f)


def load_reviews():
    with open(REVIEWS_FILE, encoding="utf-8") as f:
        return json.load(f)


def get_published_slugs():
    return {r["slug"].replace("-review", "") for r in load_reviews()}


def get_published_names():
    """Return dict of {tool_name_lower: slug} for auto-linking."""
    result = {}
    for r in load_reviews():
        name = r["title"].split(" Review")[0].strip().lower()
        result[name] = r["slug"]
    return result


def run_screenshots(tool_name, official_url, slug):
    """Run capture-screenshot.py and return image paths."""
    script = os.path.join(PROJ, "scripts", "capture-screenshot.py")
    if not os.path.exists(script):
        print("  [WARN] capture-screenshot.py not found")
        return []
    try:
        result = subprocess.run(
            [sys.executable, script, "--slug", slug],
            capture_output=True, text=True, timeout=60, cwd=PROJ
        )
        print(result.stdout)
        paths = []
        for line in result.stdout.split("\n"):
            if "/tool-screenshots/" in line:
                for p in line.strip().split():
                    if p.startswith("/tool-screenshots/"):
                        paths.append(p)
        return paths
    except subprocess.TimeoutExpired:
        print("  [WARN] Screenshot capture timed out")
        return []
    except Exception as e:
        print(f"  [WARN] Screenshot failed: {e}")
        return []


def insert_screenshot_images(content_html, img_paths, tool_name):
    """Replace [SCREENSHOT] placeholders with actual image tags."""
    if not img_paths:
        return content_html

    result = content_html
    labels = ["interface", "pricing"]
    caption_texts = [
        f"Screenshot of {tool_name} interface (source: official website)",
        f"{tool_name} pricing plans (source: official website)",
    ]

    for i, (path, caption) in enumerate(zip(img_paths[:2], caption_texts)):
        placeholder = "[SCREENSHOT: Insert screenshot of the tool interface here if available]"
        if placeholder in result:
            img_tag = f'<figure><img src="{path}" alt="{tool_name} screenshot" loading="lazy" style="max-width:100%;border-radius:8px;border:1px solid #e2e8f0"/><figcaption style="font-size:0.8rem;color:#64748b;margin-top:4px">{caption}</figcaption></figure>'
            result = result.replace(placeholder, img_tag, 1)

        placeholder2 = "[SCREENSHOT: Insert pricing page screenshot here if available]"
        if placeholder2 in result:
            if len(img_paths) > 1:
                img_tag = f'<figure><img src="{img_paths[1]}" alt="{tool_name} pricing" loading="lazy" style="max-width:100%;border-radius:8px;border:1px solid #e2e8f0"/><figcaption style="font-size:0.8rem;color:#64748b;margin-top:4px">{caption_texts[1]}</figcaption></figure>'
                result = result.replace(placeholder2, img_tag, 1)

    return result


def auto_internal_links(content_html, exclude_slug=None):
    """
    Scan content for tool names that match already-published reviews.
    Insert <a href> links for matches.
    """
    published = get_published_names()
    links_added = 0
    result = content_html

    for name in sorted(published.keys(), key=len, reverse=True):
        if links_added >= 4:
            break
        slug = published[name]
        if exclude_slug and slug == exclude_slug:
            continue

        # Match word boundary, not already inside an <a> tag
        pattern = re.compile(
            r'(?<!<a[^>]*>)' +
            r'\b' + re.escape(name) + r'\b',
            re.IGNORECASE
        )

        matches = list(pattern.finditer(result))
        if not matches:
            continue

        # Only insert first 2 matches
        offset = 0
        replaced = 0
        for m in matches:
            if replaced >= 2:
                break
            start = m.start() + offset
            end = m.end() + offset
            link = f'<a href="/{slug}">{result[start:end]}</a>'
            result = result[:start] + link + result[end:]
            offset += len(link) - (end - start)
            replaced += 1

        if replaced > 0:
            print(f"  [LINK] +{replaced} internal links: {name} -> /{slug}")
            links_added += replaced

    if links_added == 0:
        print(f"  [LINK] No internal link opportunities found")
    return result, links_added


def check_screenshot_status():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    files = os.listdir(SCREENSHOT_DIR) if os.path.isdir(SCREENSHOT_DIR) else []
    webps = [f for f in files if f.endswith(".webp")]
    total_kb = sum(os.path.getsize(os.path.join(SCREENSHOT_DIR, f)) for f in webps) / 1024 if webps else 0
    return len(webps), total_kb


def main():
    parser = argparse.ArgumentParser(description="AI Tool Article Generator")
    parser.add_argument("--type", type=int, choices=[1, 2, 3], default=1)
    parser.add_argument("--slug", help="Force specific tool slug")
    parser.add_argument("--all", action="store_true", help="List all remaining")
    parser.add_argument("--status", action="store_true", help="Full status report")
    parser.add_argument("--screenshots", action="store_true", help="Capture screenshots")
    parser.add_argument("--auto-links", action="store_true", help="Show auto link analysis")
    parser.add_argument("--pipeline", action="store_true", help="Full pipeline dry-run")
    args = parser.parse_args()

    if args.status:
        data = load_params()
        published = get_published_slugs()
        total = len(data["tools"])
        pub_count = len(published)
        img_count, img_kb = check_screenshot_status()

        print("=" * 60)
        print("  PIPELINE STATUS REPORT")
        print("=" * 60)
        print(f"  Tools in DB:     {total}")
        print(f"  Published:       {pub_count}")
        print(f"  Remaining:       {total - pub_count}")
        print(f"  Screenshots:     {img_count} images ({img_kb:.0f}KB)")

        cat_counts = {}
        for t in data["tools"]:
            c = t["category"]
            if c not in cat_counts:
                cat_counts[c] = {"total": 0, "done": 0}
            cat_counts[c]["total"] += 1
            if t["slug"] in published:
                cat_counts[c]["done"] += 1

        print(f"\n  --- Per Category ---")
        for name, st in sorted(cat_counts.items()):
            bar = "".join(chr(9608) if i < st["done"] else chr(9617) for i in range(st["total"]))
            print(f"  {name:<20} {bar} {st['done']}/{st['total']}")

        print(f"\n  --- Scripts ---")
        for s in ["generate-article.py", "capture-screenshot.py", "schema-generator.py", "gsc-submit.py"]:
            ok = os.path.exists(os.path.join(PROJ, "scripts", s))
            print(f"  {s:<35} {chr(10004) if ok else chr(10007)}")

        remaining = [t for t in data["tools"] if t["slug"] not in published]
        if remaining:
            nxt = remaining[0]
            print(f"\n  Next:  {nxt['name']} [{nxt['category']}] (Queue: {len(remaining)})")
        return

    if args.all:
        data = load_params()
        published = get_published_slugs()
        remaining = [t for t in data["tools"] if t["slug"] not in published]
        if not remaining:
            print("All tools reviewed!")
            return
        print(f"Remaining tools ({len(remaining)}):")
        for i, t in enumerate(remaining, 1):
            print(f"  {i:2}. {t['name']:<25} ${t['price_monthly']:<6} {t['rating']}/5  [{t['category']}]")
        return

    # --- Determine tool ---
    data = load_params()
    published = get_published_slugs()
    remaining = [t for t in data["tools"] if t["slug"] not in published]

    if not remaining and not args.slug:
        print("All tools reviewed! Add new tools to tool-params.json")
        return

    if args.slug:
        tool = next((t for t in data["tools"] if t["slug"] == args.slug), None)
        if not tool:
            for r in load_reviews():
                if r["slug"] in [args.slug, f"{args.slug}-review"]:
                    print(f"Already published: {r['slug']}")
                    return
            print(f"Tool not found: {args.slug}")
            return
    else:
        tool = remaining[0]

    name = tool["name"]
    cat = tool["category"]
    slug = tool["slug"] + "-review"
    price = tool.get("price_monthly", 0)
    rating = tool.get("rating", 4.0)
    aff_link = tool.get("affiliateLink", "")
    official_url = tool.get("official_url", tool.get("visitUrl", ""))
    pros = tool.get("pros", [])
    cons = tool.get("cons", [])
    comp = tool.get("competitor", "")
    desc = tool.get("description", "")

    # === PIPELINE MODE ===
    if args.pipeline:
        print("=" * 70)
        print(f"  PIPELINE DRY-RUN: {name}")
        print("=" * 70)

        print(f"\n  [1/6] ARTICLE (Template {args.type})")
        print(f"    Slug:      {slug}")
        print(f"    Category:  {cat} | Price: ${price}/mo | Rating: {rating}/5")

        print(f"\n  [2/6] SCREENSHOTS")
        if official_url:
            home_path = os.path.join(SCREENSHOT_DIR, f"{tool['slug']}-home.webp")
            if os.path.exists(home_path):
                sz = os.path.getsize(home_path) / 1024
                print(f"    URL:   {official_url}")
                print(f"    Cache: {tool['slug']}-home.webp ({sz:.0f}KB)")
            else:
                print(f"    URL:    {official_url}")
                print(f"    Status: Will capture fresh")
        else:
            print(f"    Status: SKIP (no URL)")

        print(f"\n  [3/6] AUTO INTERNAL LINKS")
        pub_names = get_published_names()
        candidates = [n for n in pub_names if tool["slug"] != pub_names[n].replace("-review", "")]
        if candidates:
            print(f"    Candidates: {len(candidates)}")
            for pn in candidates[:5]:
                print(f"      -> /{pub_names[pn]}")
        else:
            print(f"    No existing reviews to link from yet")

        print(f"\n  [4/6] SCHEMA AUTO-INJECTION (build-time)")
        print(f"\n  [5/6] BUILD & DEPLOY")
        print(f"    npx next build && npx wrangler pages deploy out --project-name aitoptools --branch main")
        print(f"    git add -A && git commit -m \"auto: add {slug}\" && git push")

        print(f"\n  [6/6] GSC INDEX SUBMISSION")
        print(f"    Status:  SKIP (temp domain)")

        print(f"\n  Full pipeline cmd:")
        print(f"    python scripts/generate-article.py --type 1 --screenshots --auto-links")
        print(f"\n  Queue: {len(remaining) - 1} remaining after this")
        return

    # === SCREENSHOTS STANDALONE ===
    if args.screenshots:
        print(f"Capturing screenshots for {name}...")
        paths = run_screenshots(name, official_url, tool["slug"])
        if paths:
            print(f"OK: {len(paths)} images")
            for p in paths:
                print(f"  {p}")
        return

    # === AUTO-LINKS STANDALONE ===
    if args.auto_links:
        pub_names = get_published_names()
        candidates = [(n, s) for n, s in pub_names.items() if tool["slug"] != s.replace("-review", "")]
        print(f"Auto-link candidates for {name}: {len(candidates)}")
        for pn, ps in candidates[:10]:
            print(f"  '/{ps}' <- '{pn}'")
        return

    # === DEFAULT: Template output ===
    print("=" * 70)
    print(f"  NEXT ARTICLE: {name}")
    print("=" * 70)
    print(f"  Slug:       {slug}")
    print(f"  Category:   {cat}")
    print(f"  Price:      ${price}/mo")
    print(f"  Rating:     {rating}/5")
    print(f"  Website:    {official_url}")
    print(f"  Affiliate:  {aff_link}")
    print(f"  Competitor: {comp or '(none)'}")
    print(f"  Description:{desc}")
    print(f"  Pros: {len(pros)} | Cons: {len(cons)}")

    print(f"\n{'=' * 70}")
    print(f"  TEMPLATE {args.type} PROMPT")
    print(f"{'=' * 70}")

    if args.type == 1:
        print(f"""
Act as a senior AI tool reviewer with 6+ years of industry experience.
You have tested {name} for 3 months in real work scenarios.
Write a 1800-2200 word, honest and in-depth review for {cat} audience.

STRUCTURE (DO NOT CHANGE ORDER):
1. FTC disclosure at top
2. H1 Title: {name} Review 2026: Is It Still Worth It? (Honest 3-Month Test)
3. Summary Box (1-sentence verdict, 3 pros / 2 cons, CTA button)
4. Introduction (what it is, who it's for, who should skip)
5. Hands-On Experience & 4-5 Key Features (real examples, 1-2 drawbacks)
6. Pricing & Plans Breakdown (exact prices, best plan for each user type)
7. Pros (6-8) & Cons (3-4) - specific, not generic
8. Quick Comparison: {name} vs {comp} (1 paragraph + internal link)
9. FAQ (4-6 questions from People Also Ask)
10. Final Verdict with CTA to {aff_link}

SEO RULES:
- Primary keyword "{name} review" in H1, first 100 words, 3-4 natural mentions
- Use H2/H3 headings, conversational English, no AI fluff
- 3 affiliate link placements: summary box, mid-content, final verdict
- Output as HTML only (h2/h3/p/ul/ol/table), NO markdown

SCREENSHOT PLACEHOLDERS (will be auto-inserted by pipeline):
[SCREENSHOT: Insert screenshot of the tool interface here if available]
[SCREENSHOT: Insert pricing page screenshot here if available]
""")

    # Queue status
    remaining_after = remaining[1:] if not args.slug else remaining
    print(f"\n  Queue remaining: {len(remaining_after)} tools")
    for i, t in enumerate(remaining_after[:5], 1):
        print(f"    {i}. {t['name']} [{t['category']}]")
    if len(remaining_after) > 5:
        print(f"    ... and {len(remaining_after)-5} more")

    print(f"\n  Pipeline cmd: python scripts/generate-article.py --type 1 --screenshots --auto-links")


if __name__ == "__main__":
    main()
