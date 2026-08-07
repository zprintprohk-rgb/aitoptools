// 8/8 robots.txt 回归修复 — generate-sitemap.py 硬编码覆盖丢 AI 爬虫放行段
const fs = require('fs');
const ROOT = 'F:/aitoptools';

const robots = `# Explicitly welcome AI crawlers — this site's content is meant to be cited.
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: *
Allow: /
Sitemap: https://aitoptools.net/sitemap.xml
`;

// 1. 恢复 public/ + out/ 的 robots.txt
for (const sub of ['public', 'out']) {
  fs.writeFileSync(`${ROOT}/${sub}/robots.txt`, robots, 'utf-8');
  console.log('restored', sub + '/robots.txt');
}

// 2. 修复脚本: robots 模板带 AI 爬虫段
const sp = ROOT + '/scripts/generate-sitemap.py';
let s = fs.readFileSync(sp, 'utf-8');
const oldLine = `    robots = f'User-agent: *\\nAllow: /\\nSitemap: {DOMAIN}/sitemap.xml\\n'`;
const newBlock = `    robots = (
        '# Explicitly welcome AI crawlers — this site\'s content is meant to be cited.\\n'
        'User-agent: GPTBot\\nAllow: /\\n\\n'
        'User-agent: ClaudeBot\\nAllow: /\\n\\n'
        'User-agent: PerplexityBot\\nAllow: /\\n\\n'
        'User-agent: Google-Extended\\nAllow: /\\n\\n'
        f'User-agent: *\\nAllow: /\\nSitemap: {DOMAIN}/sitemap.xml\\n'
    )`;
if (s.includes(oldLine)) {
  s = s.replace(oldLine, newBlock);
  fs.writeFileSync(sp, s, 'utf-8');
  console.log('patched scripts/generate-sitemap.py');
} else {
  console.log('SCRIPT ANCHOR NOT FOUND, raw check:');
  const i = s.indexOf('robots = ');
  console.log(JSON.stringify(s.slice(i, i + 120)));
}
