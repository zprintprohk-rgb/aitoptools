# Programmatic SEO Pipeline — Build-Out Summary (Steps 1–4)

> Date: 2026-08-03
> Owner: Hermes (bulk generator) — per M3 SEO_ARCHITECTURE.md v1.0
> Status: **DONE — 199 pages generated, build verified**

## What was built

| Step | Deliverable | Files |
|---|---|---|
| 1 | Data layer validation | `docs/programmatic-validation-report.md` — 199 rows, all checks passed |
| 1 | Affiliate SSoT | `src/data/affiliates.json` (9 tools, pending-flagged for picjam/greenonion) |
| 1 | Tool data | `src/data/tools/{9 tools}.json` (real rating/price from reviews.json) |
| 2 | Master template | `scripts/templates/page.njk` (Nunjucks, 6 sections, inline CSS, zero JS) |
| 2 | Generator | `scripts/generate-pages.js` → `dist/pages/*.html` (199 pages) |
| 3 | Schema.org ×3 | WebPage + ItemList(SoftwareApplication+aggregateRating+offers) + FAQPage, embedded per page |
| 4 | Route registration | `public/best/{slug}/index.html` ×199 (Next.js exports public/ verbatim → live at /best/{slug}/) |
| 4 | Sitemaps | `public/sitemap-programmatic.xml` (199 URLs, priority 0.7, weekly) + main `public/sitemap.xml` (298 URLs, programmatic block appended, idempotent) |

## Design decisions (vs. M3 spec)

1. **Route shape = `/best/{slug}/`** (not `/best-ai-tools-for-{slug}/`): M3's own
   `SEO_ARCHITECTURE.md` §1.2 canonical and `generate_page.py` both emit
   `https://aitoptools.net/best/{slug}/`. Kept consistent with the existing
   `/best/` route family and the 4 listicle pages (no slug overlap — verified).
2. **Affiliate links stay CLEAN in generated HTML**: UTM + `aff-link` class are
   injected post-build by the existing `scripts/inject-aff-link.mjs` (W1-T1 GA4
   pipeline, site-wide convention). Pre-injecting UTM would double-inject.
   Build log confirms: 191 files, 759 aff-links injected, `data-merchant` +
   `utm_source=aitoptools` present in `out/best/*/index.html`.
3. **No fabricated data**: `aggregateRating` only when a real rating exists in
   `reviews.json` (7 tools); picjam/greenonion get no rating, no offers, and no
   affiliate CTA (pending). Prices come from reviews.json, not invented.
4. **199 pages, not 200**: `keywords-200.csv` actually contains 199 data rows
   (+header). JSON matrix and M3 drafts agree (199×3). Flagged for M3 — if the
   missing row exists it should be re-added, then re-run the generator.
5. **Word counts**: M3 spec targets 2500–3500 words/page. Current template
   renders leaner (≈800–1,200 words) — content depth is the trade-off for
   zero-fabrication + speed. Suggest M3 review pass (per SEO_ARCHITECTURE §4
   step 2: 8/4–8/5 Mavis review) before 8/5 攒批 commit.

## Re-run instructions

```bash
node scripts/generate-pages.js          # full regenerate (199 pages)
node scripts/generate-pages.js <slug>   # single page debug
npm run build                           # next build + aff-link inject
```

## Verification evidence

- `npm run build` — **passed** (static export complete, 338 HTML pages in out/)
- sitemap-programmatic.xml — valid XML, 199 URLs, priority 0.7 ×199, weekly ×199
- main sitemap.xml — valid XML, 298 URLs (99 existing + 199 programmatic)
- slug overlap with listicles route — **none**
- 3 JSON-LD blocks per page (WebPage / ItemList / FAQPage) — confirmed in out/
- picjam-vs-greenonion: 0 sponsored links (pending protection works)

## Next steps (awaiting M3 / user)

1. M3: confirm 199 vs 200 rows in keywords CSV
2. M3: content review pass (8/4–8/5) — depth, tone, factual accuracy
3. User: 8/2 攒批 commit (feat: programmatic-seo pipeline) — files staged per
   git status; dist/ is gitignored (regenerable), public/best/ is committed
4. 8/5: GSC sitemap resubmit (sitemap-programmatic.xml) after deploy
