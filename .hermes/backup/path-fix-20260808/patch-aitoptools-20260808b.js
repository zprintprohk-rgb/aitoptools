// 8/8 补丁 v2 — 修正两个 anchor
const fs = require('fs');
const ROOT = 'F:/aitoptools';
const log = [];
const ok = (m) => log.push('OK   ' + m);
const fail = (m) => log.push('FAIL ' + m);

// 1. AFFILIATE_LOG.md C2b
{
  const p = ROOT + '/AFFILIATE_LOG.md';
  let s = fs.readFileSync(p, 'utf-8');
  const anchor = '(8/6 \u63d0\u524d\u5b8c\u6210) | 332 URL (\u771f\u5b9e\u552f\u4e00\u6570) | **332/332** | 0 | \u5f85\u9a8c\u8bc1 | \u9996\u6b21\u5168\u91cf\u63a8\u9001 200; \u6b64\u524d"730"\u662f\u91cd\u590d\u8ba1\u6570\u8bef\u4f30 |';
  const row = '\n| 8/8 (D2) | \u589e\u91cf 6 URL (blog \u8865\u63a8) | **6/6** | 0 | sitemap 338 URL \u5df2\u4e0a\u7ebf | sitemap \u8865\u8dd1\u4fee\u590d 6 \u7bc7 Blog \u7f3a\u5931 (332 \u65e7\u552f\u4e00 + 6 blog, \u987a\u5e26\u53bb\u91cd 199 \u91cd\u590d) |';
  if (s.includes(anchor)) {
    s = s.replace(anchor, anchor + row);
    fs.writeFileSync(p, s, 'utf-8');
    ok('AFFILIATE_LOG.md C2b \u8868\u65b0\u589e 8/8 \u884c');
  } else fail('AFFILIATE_LOG.md anchor \u672a\u627e\u5230');
}

// 2. observation.md TWOFORM
{
  const p = ROOT + '/.hermes/discovery/observation.md';
  let s = fs.readFileSync(p, 'utf-8');
  const anchor = '- \u2705 **TWOFORM** (twoform.ai) 8/7 \u5165 medium \u5019\u9009 (\u5305\u88c5\u6a2a\u8bc4\u7b2c 5 \u884c)';
  const add = ' \u2014 **8/8 user \u62cd\u677f: \u6682\u5b58\u89c2\u5bdf\u6c60, \u4e0d\u62a2 Halloween \u6392\u671f**, \u5305\u88c5\u6a2a\u8bc4\u7b2c 5 \u884c\u5019\u9009\u4fdd\u7559 (8/14 \u540e\u8bc4\u4f30)';
  if (s.includes(anchor)) {
    s = s.replace(anchor, anchor + add);
    fs.writeFileSync(p, s, 'utf-8');
    ok('observation.md TWOFORM \u89c2\u5bdf\u6c60\u6807\u6ce8');
  } else fail('observation.md anchor \u672a\u627e\u5230: ' + JSON.stringify(anchor.slice(0, 40)));
}

console.log(log.join('\n'));
