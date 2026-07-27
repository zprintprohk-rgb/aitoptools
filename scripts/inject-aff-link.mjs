#!/usr/bin/env node
/**
 * inject-aff-link.mjs — W1-T1 post-build inject (Node 跨平台版)
 *
 * 扫 out/ 静态 HTML, 给所有缺 aff-link 标的联盟链接自动注入
 *   class="aff-link" + data-merchant + data-link-id + data-target + UTM 4 参
 *
 * 为什么 Node 版: package.json build 链 next build && node scripts/inject-aff-link.mjs
 * 跨 Windows / macOS / Linux / CF Pages build env 都一致 (Python 不一定)
 *
 * 为什么不放 src/: 这是 build artifact post-processor, 不进 src bundle
 * 为什么放 scripts/: SSoT 模式 (跟其他 build script 同位置)
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.dirname(__dirname);
const OUT_DIR = process.argv[2] || path.join(ROOT, 'out');

// 联盟域名 → merchant 映射 (顺序敏感, 先匹配先胜)
const DOMAIN_MAP = [
  [/creativefabrica\.com/i, 'creative-fabrica'],
  [/try\.printify\.com|printify\.com/i, 'printify'],
  [/printful\.com/i, 'printful'],
  [/mockey\.ai/i, 'mockey'],
  [/claid\.ai/i, 'claid'],
  [/kittl\.com/i, 'kittl'],
  [/placeit\.net/i, 'placeit'],
  [/canva\.com/i, 'canva'],
  [/[?&]via=jerome[\d]+/i, 'unknown'],
];

function inferMerchant(href) {
  for (const [pat, m] of DOMAIN_MAP) if (pat.test(href)) return m;
  return null;
}

function injectUtm(href, merchant, linkId) {
  const sep = href.includes('?') ? '&' : '?';
  return `${href}${sep}utm_source=aitoptools&utm_medium=affiliate&utm_campaign=${merchant}&utm_content=${linkId}`;
}

const A_RE = /<a\b([^>]*?)>/gs;

function injectHtml(html) {
  return html.replace(A_RE, (match, attrs) => {
    // 解析 href
    const hrefM = attrs.match(/href=["']([^"']+)["']/);
    if (!hrefM) return match;
    const href = hrefM[1];
    if (href.startsWith('#') || href.startsWith('/') || href.startsWith('mailto:') || href.startsWith('javascript:')) return match;
    if (/\baff-link\b/.test(attrs)) return match; // 已打标

    const merchant = inferMerchant(href);
    const isPlaceholder = href.includes('fpr=partner');
    if (!merchant && !isPlaceholder) return match; // 非联盟, 跳过

    const m = merchant || 'placeholder';
    const h = crypto.createHash('sha1').update(href).digest('hex').slice(0, 8);
    const linkId = `global-injected-${h}`;

    // 注入 class
    let newAttrs;
    if (/\bclass=["']/.test(attrs)) {
      newAttrs = attrs.replace(/class=(["'])(.*?)\1/, (_c, q, cls) => `class=${q}${cls} aff-link${q}`);
    } else {
      newAttrs = ` class="aff-link"${attrs}`;
    }
    // 注入 data-*
    newAttrs += ` data-merchant="${m}" data-link-id="${linkId}" data-target="product"`;
    // href 替换 (注入 UTM)
    const newHref = injectUtm(href, m, linkId);
    newAttrs = newAttrs.replace(/href=["'][^"']+["']/, `href="${newHref}"`);

    return `<a${newAttrs}>`;
  });
}

function walk(dir) {
  const out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walk(p));
    else if (e.isFile() && e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

function main() {
  if (!fs.existsSync(OUT_DIR)) {
    console.error(`[FAIL] 找不到 out 目录: ${OUT_DIR} (先跑 npm run build)`);
    process.exit(1);
  }
  const dryRun = process.argv.includes('--dry-run');
  const files = walk(OUT_DIR);
  let totalFiles = 0, totalInjected = 0, filesChanged = 0;
  for (const f of files) {
    const html = fs.readFileSync(f, 'utf8');
    const newHtml = injectHtml(html);
    if (newHtml === html) continue;
    totalFiles++;
    const injected = (newHtml.match(/aff-link/g) || []).length - (html.match(/aff-link/g) || []).length;
    totalInjected += injected;
    filesChanged++;
    if (!dryRun) fs.writeFileSync(f, newHtml);
  }
  console.log(`\n═══ inject-aff-link (${dryRun ? 'DRY-RUN' : 'APPLIED'}) ═══`);
  console.log(`  扫 ${totalFiles} 个文件含联盟链接`);
  console.log(`  注入 ${totalInjected} 处 aff-link 标 (${dryRun ? '未改文件' : `${filesChanged} 个文件已改`})`);
  if (dryRun) console.log('  重跑 (去掉 --dry-run) 应用注入');
  else console.log('  ✓ 注入完成, 重跑 npm run aff-link-audit 验证 100% 覆盖');
}

main();
