// halloween tracker 时间线替换 v2 — indexOf 切片法
const fs = require('fs');
const p = 'F:/aitoptools/.hermes/logs/halloween-asset-chain.md';
let s = fs.readFileSync(p, 'utf-8');

const startMarker = '\u65f6\u95f4\u7ebf (\u76ee\u6807 8/18';
const endMarker = '\u96c6\u7fa4\u4e0a\u7ebf\u622a\u6b62 | - |';
const si = s.indexOf(startMarker);
const ei = s.indexOf(endMarker);
if (si === -1 || ei === -1) { console.log('FAIL markers not found', si, ei); process.exit(1); }

const newBlock = `\u65f6\u95f4\u7ebf (v2 \u6307\u4ee4\u96c6\u5173\u952e\u8def\u5f84, 2026-08-08 \u5bf9\u9f50)
| \u65e5\u671f | \u91cc\u7a0b\u7891 | \u72b6\u6001 |
|---|---|---|
| 8/9 | weekly-report \u9996\u8dd1\u57fa\u7ebf\u8bfb\u6570 | \u5f85\u6267\u884c |
| 8/10 | \u8bbe\u8ba1\u9636\u6bb5: Kittl/Claid \u7528\u7d20\u6750 [0:2] \u505a 2-3 \u4e2a\u8bbe\u8ba1 \u2192 .hermes/designs/halloween-test-{date}.png | \u5f85\u89e6\u53d1 (cron 8/10 10:00) |
| 8/11 | \u4e0b\u5355\u9636\u6bb5: Printful (\u82e5\u5df2 verify) \u5426\u5219 Printify; \u9884\u7b97\u786c\u9650 $25/\u5355 $50/\u65e5; \u8bb0\u5f55 order_id/eta/cost | \u5f85\u89e6\u53d1 |
| 8/11 | Kittl \u5b9e\u6d4b\u65e5: CF \u7d20\u6750\u5f53\u6e90\u6587\u4ef6, \u5b9e\u6d4b\u5e16\u521d\u7a3f | - |
| 8/12-13 | Halloween \u652f\u67f1\u5e16\u300aHalloween POD ideas 2026\u300b\u5199\u4f5c | - |
| 8/14 | T+7 \u9996\u8bfb\u6570 \u2192 \u51b3\u5b9a\u96c6\u7fa4\u662f\u5426\u52a0\u901f | - |
| 8/15 | \u6536\u8d27\u62cd\u7167: logistics.status=delivered \u89e6\u53d1; user \u62cd\u7167 OR fallback \u5b98\u65b9 mockup \u2192 public/photos/wall/halloween-{order_id}.jpg | \u5f85\u89e6\u53d1 |
| 8/17 | Halloween \u8f96\u6761\u2460 (CF \u514d\u8d39\u4e07\u5723\u8282\u7d20\u6750\u5b9e\u6d4b) \u4e0a\u7ebf | - |
| 8/18 | \u652f\u67f1\u5e16\u4e0a\u7ebf + \u96c6\u7fa4\u622a\u6b62 (23:59) | - |

## \u6267\u884c\u53c2\u6570 (v2 \u6307\u4ee4\u96c6, 2026-08-08)
- \u4e0b\u5355\u5e73\u53f0: Printful (if verified) else Printify
- \u9884\u7b97: $25/order hard limit, $50/day hard limit, \u8d85\u9650\u6682\u505c+\u544a\u8b66
- \u6536\u8d27\u5730\u5740: test-address.json (\u7528\u6237\u63d0\u4f9b)
- \u7167\u7247: \u4f18\u5148 user \u62cd\u7167; \u7528\u6237\u4e0d\u53ef\u7528 \u2192 fallback \u5b98\u65b9 mockup
- \u4ea7\u51fa: \u7167\u7247\u5899 6 \u56fe + \u652f\u67f1\u5e16\u6e90\u6587\u4ef6 + \u6bdb\u5229\u6570\u636e`;

s = s.slice(0, si) + newBlock + s.slice(ei + endMarker.length);
fs.writeFileSync(p, s, 'utf-8');
console.log('OK tracker timeline v2 aligned');
