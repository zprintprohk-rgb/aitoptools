// 8/8 P0-P1 批量改动脚本 — aitoptools
// 所有写操作: fs.writeFileSync utf-8, 无 BOM
const fs = require('fs');
const ROOT = 'F:/aitoptools';
const log = [];
const ok = (m) => log.push('OK   ' + m);
const fail = (m) => log.push('FAIL ' + m);

// ---------- 1. AFFILIATE_LOG.md: C2b 计数表插入 8/8 行 ----------
{
  const p = ROOT + '/AFFILIATE_LOG.md';
  let s = fs.readFileSync(p, 'utf-8');
  const anchor = '| \u2757 T0 (8/6 \u63d0\u524d\u5b8c\u6210) | 332 URL (\u771f\u5b9e\u552f\u4e00\u6570) | **332/332** | 0 | \u5f85\u9a8c\u8bc1 | \u9996\u6b21\u5168\u91cf\u63a8\u9001 200; \u6b64\u524d"730"\u662f\u91cd\u590d\u8ba1\u6570\u8bef\u4f30 |';
  const row = '\n| 8/8 (D2) | \u589e\u91cf 6 URL (blog \u8865\u63a8) | **6/6** | 0 | sitemap 338 URL \u5df2\u4e0a\u7ebf | sitemap \u8865\u8dd1\u4fee\u590d 6 \u7bc7 Blog \u7f3a\u5931 (332 \u65e7\u552f\u4e00 + 6 blog, \u987a\u5e26\u53bb\u91cd 199 \u91cd\u590d) |';
  if (s.includes(anchor)) {
    s = s.replace(anchor, anchor + row);
    fs.writeFileSync(p, s, 'utf-8');
    ok('AFFILIATE_LOG.md C2b \u8868\u65b0\u589e 8/8 \u884c');
  } else fail('AFFILIATE_LOG.md anchor \u672a\u627e\u5230');
}

// ---------- 2. observation.md: TWOFORM \u89c2\u5bdf\u6c60\u660e\u786e\u5316 ----------
{
  const p = ROOT + '/.hermes/discovery/observation.md';
  let s = fs.readFileSync(p, 'utf-8');
  const anchor = '- \u2757 **TWOFORM** (twoform.ai) 8/7 \u5165 medium \u5019\u9009 (\u5305\u88c5\u6a2a\u8bc4\u7b2c 5 \u884c)';
  const add = ' \u2014 **8/8 user \u62cd\u677f: \u6682\u5b58\u89c2\u5bdf\u6c60, \u4e0d\u62a2 Halloween \u6392\u671f**, \u5305\u88c5\u6a2a\u8bc4\u7b2c 5 \u884c\u5019\u9009\u4fdd\u7559 (8/14 \u540e\u8bc4\u4f30)';
  if (s.includes(anchor)) {
    s = s.replace(anchor, anchor + add);
    fs.writeFileSync(p, s, 'utf-8');
    ok('observation.md TWOFORM \u89c2\u5bdf\u6c60\u6807\u6ce8');
  } else fail('observation.md anchor \u672a\u627e\u5230');
}

// ---------- 3. \u65b0\u5efa weekly-report \u6a21\u677f (4 \u5757) ----------
{
  const p = ROOT + '/.hermes/cron-prompts/aitoptools-weekly-report.md';
  const content = `# aitoptools weekly-report \u6a21\u677f (2026-08-08 K3 \u62cd\u677f\u56fa\u5b9a\u56db\u5757)

> \u7528\u9014: \u6bcf\u5468\u65e5 weekly-report \u6267\u884c\u65f6\u7167\u672c\u6a21\u677f\u586b\u5199\u3002\u56db\u5757\u5fc5\u987b\u5168\u90e8\u51fa\u73b0, \u4e0d\u5f97\u5220\u51cf\u3002
> \u539f\u5219: \u6570\u636e\u4f18\u5148 (GSC \u5b9e\u6570), \u7ed3\u8bba\u4e00\u53e5\u8bdd, \u5bf9\u52a8\u4f5c\u53ef\u6267\u884c\u3002

# \u5468\u62a5 \u2026 2026-08-09 (Week \u2026)

## \u5757 1 \u2022 GSC top queries
| query | \u5c55\u793a | \u70b9\u51fb | CTR | \u6392\u540d | \u53d8\u52a8 vs \u4e0a\u5468 | \u662f\u5426\u6709\u4e13\u9875 | \u8fdb\u961f\u5217? |
|---|---|---|---|---|---|---|---|
| (top 10 by \u5c55\u793a, \u22655 \u5c55\u793a\u624d\u8bb0) | | | | | | | |

## \u5757 2 \u2022 CTR \u699c (\u6765\u6e90\u00d7\u5546\u6237\u7ec4\u5408)
| \u9875\u9762 | \u5546\u6237 | \u70b9\u51fb | \u5c55\u793a | CTR | \u4e0a\u5468 CTR | \u52a8\u4f5c (\u6740/\u52a0/\u63d0\u6743) |
|---|---|---|---|---|---|---|
| (affiliate_click \u4e8b\u4ef6 GA4 + \u5404\u8054\u76df\u540e\u53f0\u6570\u636e) | | | | | | |

## \u5757 3 \u2022 \u8054\u76df\u72b6\u6001
| \u5e73\u53f0 | \u72b6\u6001 | \u672c\u5468\u53d8\u52a8 | \u4e0b\u5468\u52a8\u4f5c |
|---|---|---|---|
| Printful / Printify / Claid / Mockey / Kittl / Placeit / Creative Fabrica / \u5176\u4ed6 | | | |

## \u5757 4 \u2022 user \u624b\u5de5\u6e05\u5355 (\u22643 \u6761)
1. \u2026\u2026 (2 \u5206\u949f)
2. \u2026\u2026
3. \u2026\u2026

---
## \u9644: \u8f93\u51fa\u89c4\u5219
- \u53d1\u9001\u5730: \u5468\u62a5\u843d\u76d8 .hermes/logs/weekly-report-YYYY-MM-DD.md + \u7ed9 K3 \u4e00\u53e5\u8bdd\u6458\u8981
- GSC \u6570\u636e\u6765\u6e90: \u672c\u5468 gsc_data.csv / GSC API; \u51ed\u8bc1\u7f3a\u5931\u65f6\u586b "blocked_missing_credentials"
- \u5757 4 \u4e0d\u8d85\u8fc7 3 \u6761, \u6bcf\u6761\u5e26\u65f6\u957f; \u4e0d\u591f\u91cd\u8981\u7684\u4e0d\u5199
- \u8f93\u51fa\u540e\u66f4\u65b0 gsc-mining-queue.md (\u5c55\u793a\u226510 \u65e0\u4e13\u9875 \u2192 \u8fdb\u961f\u5217)
`;
  fs.writeFileSync(p, content, 'utf-8');
  ok('\u65b0\u5efa weekly-report \u6a21\u677f (4 \u5757)');
}

// ---------- 4. \u65b0\u5efa Halloween \u7d20\u6750\u94fe\u8ddf\u8e2a ----------
{
  const p = ROOT + '/.hermes/logs/halloween-asset-chain.md';
  const content = `# Halloween \u7d20\u6750\u94fe\u8ddf\u8e2a (2026-08-08 \u542f\u52a8, K3 \u6307\u4ee4)

> \u76ee\u7684: \u8bb0\u5f55 CF 6 \u4e2a \ud83c\udf83 \u7d20\u6750\u4ece\u8bbe\u8ba1\u2192\u4e0b\u5355\u2192\u6536\u8d27\u2192\u62cd\u7167\u7684\u5168\u6d41\u7a0b\u8fdb\u5ea6\u3002\u6bcf\u65e5 brief \u66f4\u65b0\u3002
> \u7d20\u6750\u6765\u6e90: .hermes/logs/cf-freebies/2026-08-06.md + 2026-08-07.md (Creative Fabrica \u6bcf\u65e5\u514d\u8d39\u7d20\u6750\u90ae\u4ef6)
> \u4ef7\u503c\u94fe: \u7d20\u6750\u2192 Kittl/Claid \u8bbe\u8ba1 2-3 \u4e2a \u2192 Printful/Printify \u6d4b\u8bd5\u5355 ($30-50) \u2192 \u6536\u8d27\u62cd\u7167 \u2192 \u7167\u7247\u5899 6 \u56fe + Halloween \u652f\u67f1\u5e16\u6e90\u6587\u4ef6 + \u6bdb\u5229\u6570\u636e

## \u7d20\u6750\u6e05\u5355 (6 \u4e2a \ud83c\udf83, 8/7 \u90ae\u4ef6\u4e3b\u529b)
| # | \u7d20\u6750 | \u7c7b\u578b | \u4e0b\u8f7d | \u8bbe\u8ba1\u9009\u62e9 | \u4e0b\u5355 | \u6536\u8d27 | \u62cd\u7167 |
|---|---|---|---|---|---|---|---|
| 1 | Gothic Skull Rose Bundle PNG (\u4e3b\u63a8) | PNG bundle | \u5f85\u4e0b\u8f7d | \u63a8\u8350 (8/11 Kittl \u5b9e\u6d4b\u9996\u9009) | - | - | - |
| 2 | Halloween Coffee Hand Drawn PNG Bundle | PNG bundle | \u5f85\u4e0b\u8f7d | \u5019\u9009 | - | - | - |
| 3 | Hallowen Bundle 3 | bundle | \u5f85\u4e0b\u8f7d | \u5019\u9009 | - | - | - |
| 4 | Coquette Halloween PNG Bundle Spooky PNG | PNG bundle | \u5f85\u4e0b\u8f7d | \u5019\u9009 (8/11 \u5019\u9009) | - | - | - |
| 5 | Minimal Line Art Mystic Black Cat Face | PNG | \u5f85\u4e0b\u8f7d | \u5019\u9009 | - | - | - |
| 6 | Halloween Skeleton Hand Stripes PNG | PNG | \u5f85\u4e0b\u8f7d | \u5019\u9009 | - | - | - |

## \u65f6\u95f4\u7ebf (\u76ee\u6807 8/18 \u524d Halloween \u96c6\u7fa4\u4e0a\u7ebf)
| \u65e5\u671f | \u91cc\u7a0b\u7891 | \u72b6\u6001 |
|---|---|---|
| 8/9 | weekly-report \u9996\u8dd1\u57fa\u7ebf\u8bfb\u6570 | \u5f85\u6267\u884c |
| 8/10-11 | \u7528\u7d20\u6750\u505a 2-3 \u4e2a\u8bbe\u8ba1 + \u4e0b\u6d4b\u8bd5\u5355 | - |
| 8/11 | Kittl \u5b9e\u6d4b\u65e5: CF \u7d20\u6750\u5f53\u6e90\u6587\u4ef6, \u5b9e\u6d4b\u5e16\u521d\u7a3f | - |
| 8/12-13 | Halloween \u652f\u67f1\u5e16\u300aHalloween POD ideas 2026\u300b\u5199\u4f5c | - |
| 8/14 | T+7 \u9996\u8bfb\u6570 \u2192 \u51b3\u5b9a\u96c6\u7fa4\u662f\u5426\u52a0\u901f | - |
| 8/17 | Halloween \u8f96\u6761\u2460 (CF \u514d\u8d39\u4e07\u5723\u8282\u7d20\u6750\u5b9e\u6d4b) \u4e0a\u7ebf | - |
| 8/18 | \u96c6\u7fa4\u4e0a\u7ebf\u622a\u6b62 | - |

## \u6bcf\u65e5 brief \u66f4\u65b0\u8bb0\u5f55
- 2026-08-08: \u8ddf\u8e2a\u5668\u521b\u5efa; 6 \u7d20\u6750\u5747\u5f85\u4e0b\u8f7d (CF \u767b\u5f55\u540e\u4e0b\u8f7d)
`;
  fs.writeFileSync(p, content, 'utf-8');
  ok('\u65b0\u5efa Halloween \u7d20\u6750\u94fe\u8ddf\u8e2a\u5668');
}

// ---------- 5. CONTENT_PLAN.md: \u4fe1\u4efb\u951a\u70b9\u5019\u9009 ----------
{
  const p = ROOT + '/CONTENT_PLAN.md';
  let s = fs.readFileSync(p, 'utf-8');
  const section = `

---

## \u516d\u3001\u4fe1\u4efb\u951a\u70b9\u5019\u9009 (2026-08-08 \u6807\u8bb0)

> \u601d\u8def: "\u4e0d legit" \u7ed3\u8bba\u672c\u8eab\u5c31\u662f\u9ad8\u4fe1\u4efb\u5185\u5bb9 \u2014 \u7528\u6237\u641c "legit" \u65f6\u6700\u6015\u8f6f\u6587, \u53cd\u5411\u5dee\u5f02\u5316 = \u957f\u5c3e\u4fe1\u4efb\u951a\u70b9\u3002

| \u7bc7\u76ee | \u8def\u5f84 | \u72b6\u6001 | \u51b3\u7b56\u70b9 |
|---|---|---|---|
| is-magicdrop-legit (8/7 \u4e0a\u7ebf) | \u4e0d legit \u7ed3\u8bba + 7 \u9879\u4fe1\u4efb\u6e05\u5355 | \u4fe1\u4efb\u951a\u70b9\u5019\u9009 | 8/14 \u770b GSC \u8868\u73b0\u51b3\u5b9a\u662f\u5426\u542f\u52a8 "POD \u5e73\u53f0\u4fe1\u4efb\u7cfb\u5217" |

\u542f\u52a8\u6761\u4ef6 (8/14 \u540e\u8bc4\u4f30): \u5c55\u793a\u226510 + CTR \u2265 \u57fa\u7ebf 10% \u2192 \u7cfb\u5217\u5316 (e.g. is-printify-legit / is-printful-legit / is-mockey-legit);
\u8868\u73b0\u4e00\u822c \u2192 \u4fdd\u6301\u5355\u7bc7, \u4e0d\u6269\u5c55\u3002
`;
  s = s.trimEnd() + '\n' + section;
  fs.writeFileSync(p, s, 'utf-8');
  ok('CONTENT_PLAN.md \u4fe1\u4efb\u951a\u70b9\u5019\u9009\u6807\u8bb0');
}

// ---------- 6. AGENTS.md: \u4e24\u6761\u65b0\u94c1\u5f8b ----------
{
  const p = ROOT + '/AGENTS.md';
  let s = fs.readFileSync(p, 'utf-8');
  const rules = `

## sitemap \u53d8\u66f4\u5373\u63a8\u94c1\u5f8b (2026-08-08 K3 \u62cd\u677f \u2014 8/8 6 \u7bc7 Blog \u7f3a\u5931 sitemap \u4ea4\u8baf)
- **\u6bcf\u6b21\u65b0\u589e Blog/\u9875\u9762 (\u53d1\u5e03\u786e\u8ba4\u540e), \u5f53\u5929\u5185\u5fc5\u987b\u5b8c\u6210**: \u2460 \u91cd\u8dd1 \`python scripts/generate-sitemap.py\` (\u5408\u5e76\u4fdd\u5e95\u6a21\u5f0f, \u52ff\u624b\u6539 sitemap) \u2461 \u9a8c\u8bc1\u65b0 URL \u5728 public/ \u4e0e out/ \u7684 sitemap.xml \u5747\u5b58\u5728 \u2462 git push \u2463 IndexNow \u589e\u91cf\u63a8\u9001\u65b0 URL (\u53c2\u8003 scripts/submit_indexnow_blog_20260808.py \u6a21\u5f0f) \u2464 \u586b\u5199 AFFILIATE_LOG.md C2b \u8ba1\u6570\u8868
- **\u4e0d\u7b49\u6512\u6279**: sitemap/\u63a8\u9001\u7f3a\u5931\u4f1a\u76f4\u63a5\u5ef6\u8fdf GSC \u6536\u5f55 (T+7 \u8bfb\u6570\u5931\u771f), \u5c5e\u201c\u7d27\u6025\u4fee\u590d\u201d\u7ea7\u522b, \u53ef\u5355\u72ec push
- \u9a8c\u6536: \u6bcf\u6b21\u53d1\u5e03\u540e grep sitemap \u542b\u65b0 slug = 0 \u7f3a\u5931

## \u5b63\u8282\u5185\u5bb9\u542f\u52a8\u6761\u4ef6 (2026-08-08 K3 \u62cd\u677f \u2014 CF \u4e07\u5723\u8282\u7d20\u6750\u7d2f\u79ef\u542f\u52a8)
- **\u7d20\u6750\u843d\u76d8 = \u542f\u52a8\u4fe1\u53f7**: \u5b63\u8282\u96c6\u7fa4\u8bbe\u8ba1\u4e3b\u9898\u7684\u514d\u8d39\u7d20\u6750\u7d2f\u79ef\u22653 \u4e2a (\u5982 CF freebies \u8bb0\u5f55) \u2192 \u542f\u52a8\u201c\u7d20\u6750\u2192\u8bbe\u8ba1\u2192\u4e0b\u5355\u2192\u6536\u8d27\u62cd\u7167\u2192\u5185\u5bb9\u201d\u95ed\u73af, \u4e0d\u7b49\u5b8c\u6574\u8ba1\u5212\u4e66
- \u8ddf\u8e2a\u5668: .hermes/logs/halloween-asset-chain.md (\u6bcf\u65e5 brief \u66f4\u65b0\u8fdb\u5ea6: \u8bbe\u8ba1\u2192\u4e0b\u5355\u2192\u6536\u8d27\u2192\u62cd\u7167)
- \u65f6\u95f4\u7a97: \u5b63\u8282\u524d 6-8 \u5468\u542f\u52a8\u6700\u4f73; \u8fc7\u65f6\u7a97\u5219\u8bc4\u4f30\u662f\u5426\u4e0b\u4e00\u5b63\u8282\u3002\u4f8b: Halloween \u96c6\u7fa4\u76ee\u6807 8/18 \u524d\u4e0a\u7ebf
`;
  s = s.trimEnd() + '\n' + rules;
  fs.writeFileSync(p, s, 'utf-8');
  ok('AGENTS.md \u65b0\u589e 2 \u6761\u94c1\u5f8b');
}

console.log(log.join('\n'));
