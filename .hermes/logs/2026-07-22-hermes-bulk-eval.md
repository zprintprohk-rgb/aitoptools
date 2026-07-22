# Hermes Bulk Evaluation Report — 2026-07-22

**Task**: Bulk-eval 7 mockup/visual tool candidates for aitoptools.net review pipeline
**Scope**: Mockey excluded (M3's `mockey-vs-placeit` page, separate workstream)
**Operator**: Hermes Agent (deepseek-v4-flash)
**TTL**: 60 min → elapsed: ~55 min
**Status**: ✅ Complete (5 of 7 candidates drafted)

---

## 1. Verdict Matrix

| # | Tool | Slug | Verification | Price Range | Affiliate | Draft | |
|---|------|------|-------------|-------------|-----------|-------|---|
| 1 | MockupHive | mockuphive-review | ⚠️ **partial** | Free / $9-299 | ❌ None | ✅ | New platform, no reviews |
| 2 | Packify.ai | packify-ai-review | ✅ **verified** | $19.90-129/mo | ❌ None (referral icon only) | ✅ | Strong packaging vertical fit |
| 3 | Nightjar | nightjar-review | ✅ **verified** | $25-50/mo | ❌ None | ✅ | Catalog consistency USP |
| 4 | Genlook | — | ❌ **dead** | N/A | N/A | ✗ | Domain parked since 2014 |
| 5 | Dynamic Mockups | dynamic-mockups-review | ✅ **verified** | Free / $15-60k+ | ❌ None | ✅ | API-first, strong POD fit |
| 6 | Goose Ads Remixer | — | ❌ **not found** | N/A | N/A | ✗ | No web presence at all |
| 7 | Mintly | mintly-ai-review | ✅ **verified** | $19-199/mo | ✅ **20% lifetime** | ✅ | Ad creative, not mockups |

**Results**: 4 verified + 1 partial = 5 draftable / 2 excluded (non-existent)

---

## 2. Detailed Findings

### MockupHive (mockuphive.com) — partial
- **Category**: AI Product Photography
- **Pricing**: Free (1 dl/day), Pro $9/mo (30 dl/day), Unlimited $15/mo (unlimited), Lifetime $199-299
- **AI**: Text-to-mockup <15s, auto surface detection, perspective wrapping
- **Library**: 2000+ templates in 9 categories (258 apparel for POD)
- **Integrations**: Figma plugin, Adobe Express add-on
- **Affiliate**: ❌ Not found (`/affiliates` = 404)
- **Risk**: New platform (June 2026), no G2/Capterra, no affiliate path
- **POD fit**: Strong — affordable, commercial license, apparel templates
- **Draft**: `mockuphive-draft.json` (4.9 KB)

### Packify.ai (packify.ai) — verified
- **Category**: AI Print & Packaging Design
- **Pricing**: Free (100 credits one-time), Basic $19.90/mo (1000 credits), Pro $29.90/mo (2500), Business $49.90/mo (3500), Enterprise $129/mo (10000)
- **AI**: Text-to-3D packaging, AI Photoshoot, Smart Edit, dieline export
- **Differentiator**: End-to-end concept → dieline → manufacturer pipeline
- **Affiliate**: ❌ No public program (referral icon in footer, no published terms)
- **POD fit**: Excellent for packaging print shops, less for apparel POD
- **Sources**: 3 URLs (homepage, pricing, features)
- **Draft**: `packify-ai-draft.json` (4.6 KB)

### Nightjar (nightjar.so) — verified
- **Category**: AI Product Photography
- **Pricing**: Free (6 images), Studio $25/mo (150 images), Studio+ $50/mo (400 images)
- **AI**: Catalog-scale consistency, AI fashion models, Virtual Try-On
- **Integrations**: Native Shopify app
- **Affiliate**: ❌ Not found
- **POD fit**: Good for apparel POD with 50+ SKUs needing consistent photography
- **Caveat**: Not a mockup generator — photography only
- **Draft**: `nightjar-draft.json` (3.5 KB)

### Dynamic Mockups (dynamicmockups.com) — verified
- **Category**: AI Product Photography
- **Pricing**: Free (50 credits + daily AI), Pro from $15/mo annual (3600+ credits/yr)
- **API**: RESTful, 10+ endpoints, 4 SDKs, MCP Server, iFrame embed
- **Templates**: 10,000+ with custom PSD upload
- **Affiliate**: ❌ Not found (`/affiliates` = 404)
- **POD fit**: Excellent for bulk/API-driven mockups. Credit system.
- **Caveat**: No webhooks, 24h image link expiry
- **Draft**: `dynamic-mockups-draft.json` (3.8 KB)

### Mintly (usemintly.com) — verified
- **Category**: AI Ad Creative (NOT mockups)
- **Pricing**: Free / Starter $19/mo / Growth $49/mo / Scale $199/mo
- **AI**: Static + video ad creative from product links
- **Marketplace**: Listed on Microsoft Marketplace
- **Affiliate**: ✅ **20% lifetime commission, 90-day cookie** — best in this batch
- **POD fit**: Tangential — good for POD sticker/ad creative, not mockups
- **Caveat**: Not a print/mockup tool. Consider for Phase 2 expansion (AI Video & Digital Humans category)
- **Draft**: `mintly-draft.json` (4.0 KB)

### Genlook (genlook.com) — DEAD
- **Status**: Domain parked on Wix since registration (2014-present)
- **Evidence**: 41 Wayback Machine captures (2014-2025) — all parked pages
- **Action**: 🔴 **Remove from radar**. No product has existed at this domain.
- **Draft**: None

### Goose Ads Remixer — NOT FOUND
- **Status**: Could not locate on the public web after 14+ search queries
- **Evidence**: Searched Product Hunt, Reddit, HN, Bing, direct domain lookups (gooseadsremixer.com, gooseads.ai) — all empty
- **Action**: 🔴 **Remove from radar** unless user can provide a correct URL
- **Draft**: None

---

## 3. Draft Files Created

All in `F:/aitoptools/.hermes/drafts/`:

| File | Size | Status |
|------|------|--------|
| mockuphive-draft.json | 4.9 KB | ✅ Partial — ⚠️ no G2 reviews verified |
| packify-ai-draft.json | 4.6 KB | ✅ Verified |
| nightjar-draft.json | 3.5 KB | ✅ Verified |
| dynamic-mockups-draft.json | 3.8 KB | ✅ Verified |
| mintly-draft.json | 4.0 KB | ✅ Verified |

**Total**: 5 files, ~20.8 KB

---

## 4. Anomalies & Blockers

| Severity | Issue | Action |
|----------|-------|--------|
| 🔴 HIGH | Genlook (genlook.com) never active — domain parked since 2014 | Remove from radar |
| 🔴 HIGH | Goose Ads Remixer not found anywhere on the web | Remove from radar unless user provides URL |
| 🟡 MED | 4 of 5 draftable tools have NO affiliate program | Only Mintly (20% lifetime) has real monetization. MockupHive/Packify.ai/Nightjar/Dynamic Mockups need an alternative monetization strategy (e.g. direct CPM display ads, or wait for affiliate programs) |
| 🟡 MED | Mintly is an ad creative tool, not mockup/print — category mismatch | Consider re-categorizing or deferring to Phase 2 |
| ⚪ LOW | MockupHive has NO third-party reviews (partial verification) | Re-check G2/Capterra after 3 months |

---

## 5. Next Steps (M3 → User)

Per the gate process:

1. **M3 review**: Walk through each draft JSON for content quality, factual accuracy, POD value
2. **User sign-off**: Check fact chain (sources, pricing), approve or revise
3. **Merge into reviews.json**: Only after user approves each draft
4. **Batch push**: Next push window (per 1 push/day rule)

### Recommended pipeline order:
1. Packify.ai (strongest vertical fit, most data) → Priority High
2. Dynamic Mockups (API story is unique, good POD angle) → Priority High
3. MockupHive (new player, partial data, 3-mo revisit) → Priority Medium
4. Nightjar (good but photography-only, limited affiliate path) → Priority Medium
5. Mintly (best affiliate but category mismatch) → Queue Phase 2

### Excluded permanently:
- Genlook — never existed
- Goose Ads Remixer — not found

---

## 6. Timing

- **Start**: ~22:00 CST
- **End**: ~22:55 CST
- **TTL**: 60 min ✅ (under limit)
- **Model**: deepseek-v4-flash
