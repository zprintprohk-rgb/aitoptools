# GSC / IndexNow Submission Log - 2026-09-18

**Task**: gsc-indexnow (daily 12:40 Asia/Shanghai)
**Result**: SKIPPED - sitemap unchanged, no submission performed (API quota preserved)

## Step 1 - sitemap change detection
| file | bytes | locs | sha256 (16) | vs last submission |
|---|---|---|---|---|
| public/sitemap.xml | 44335 | 362 | dee3a09bf579b718 | UNCHANGED (prev DEE3A09B..., case-only diff) |
| public/sitemap-programmatic.xml | 27727 | 199 | dc9fb3558cc65b62 | UNCHANGED |

Live https://aitoptools.net/sitemap.xml -> HTTP 200, 44335 bytes = local byte count -> deployment current.
No git commits since e1b171e / 420127f (9/13); out/ built 2026-09-13 15:28.

## Step 2 - credentials
- IndexNow: .hermes/secrets/indexnow-key.txt present (non-empty)
- GSC: .hermes/secrets/gsc-oauth.json present, service_account mode (aitoptools-505222, siteFullUser)

## Step 3 - submission
Not performed: hash match with 9/13 submission -> nothing new to push. Zero quota spent.

## Step 4 - coverage audit (365 built pages / 362 sitemap locs)
REAL GAPS (2): /best/best-ai-tshirt-design-generators + /best/best-print-on-demand-companies
- Root cause: sitemap-programmatic.xml stale since 8/14 (owner = scripts/generate-pages.js)
- Both live HTTP 200 and already IndexNow-pushed on 2026-09-12 -> no re-push needed
- Fix requires generate-pages.js rerun + build + push; blocked by can_deploy:false
Non-issues: / (homepage) and /404 correctly absent by design.

## Step 5 - P0 ESCALATION: DeepSeek 402 storm
- executions.db: 9/14=10, 9/15=8, 9/16=9, 9/17=8 failed runs, all "HTTP 402: Insufficient Balance" (35 failures / 4 consecutive days)
- 9/18: 3-4 runs completed (partial recovery) but balance = CNY 4.68 < CNY 5 threshold -> repeat 402 imminent tonight
- config.yaml fallback_model: fully commented out -> no failover
- MINIMAX_CN_API_KEY exists in .env but not wired
- USER DECISION REQUIRED: (a) top up DeepSeek, or (b) enable MINIMAX fallback

## Compliance
- can_deploy: false respected - no push, no build
- No full credential contents printed
- Byte-level verification used for all file-content claims
