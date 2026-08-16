#!/usr/bin/env node
/**
 * inject-aff-link.mjs �?W1-T1 post-build inject (Node 跨平台版)
 *
 * �?out/ 静�?HTML, 给所有缺 aff-link 标的联盟链接自动注入
 *   class="aff-link" + data-merchant + data-link-id + data-target + UTM 4 �? *
 * 为什�?Node �? package.json build �?next build && node scripts/inject-aff-link.mjs
 * �?Windows / macOS / Linux / CF Pages build env 都一�?(Python 不一�?
 *
 * 为什么不�?src/: 这是 build artifact post-processor, 不进 src bundle
 * 为什么放 scripts/: SSoT 模式 (跟其�?build script 同位�?
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.dirname(__dirname);
const OUT_DIR = (process.argv[2] && !process.argv[2].startsWith('--')) ? process.argv[2] : path.join(ROOT, 'out');

// 联盟域名 �?merchant 映射 (顺序敏感, 先匹配先�?
const DOMAIN_MAP = [
  [/creativefabrica\.com/i, 'creative-fabrica'],
  [/try\.printify\.com|printify\.com/i, 'printify'],
  [/printful\.com/i, 'printful'],
  [/mockey\.ai/i, 'mockey'],
  [/claid\.ai/i, 'claid'],
  [/kittl\.com|kittl\.pxf\.io/i, 'kittl'],
  [/placeit\.net/i, 'placeit'],
  [/canva\.com/i, 'canva'],
  [/try\.gelato\.com/i, 'gelato'], // K3 8/1 批准, GA4 埋点 + UTM 注入
  [/[?&]via=jerome[\d]+/i, 'unknown'],
];

// 联盟域名 �?canonical 联盟 URL 重写 (扫到 raw 商家域名时改�?deep link)
// merchant 推断仍走 DOMAIN_MAP, 不变; link_id 基于 rewrite �?URL �?// 上线日志: 2026-07-28 W1-T3 user 拍板 kittl.pxf.io/qWNvPn 立刻上线 (10 push 破例)
const REWRITE_URL_MAP = {
  'kittl.com': 'https://kittl.pxf.io/qWNvPn',
};
const REWRITE_DOMAINS = Object.keys(REWRITE_URL_MAP);

function inferMerchant(href) {
  for (const [pat, m] of DOMAIN_MAP) if (pat.test(href)) return m;
  return null;
}

function rewriteAffUrl(href) {
  try {
    const u = new URL(href);
    for (const dom of REWRITE_DOMAINS) {
      if (u.hostname === dom || u.hostname.endsWith('.' + dom)) {
        return REWRITE_URL_MAP[dom];
      }
    }
  } catch (e) { /* 非法 URL 不动 */ }
  return href;
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
    if (/\baff-link\b/.test(attrs)) return match; // 已打�?
    // K3 7/28 护栏: organic (rel=nofollow 无 sponsored) 不打 aff-link 标, 不加 UTM, 保护 organic SEO
    const relM = attrs.match(/rel=["']([^"']+)["']/);
    const rel = relM ? relM[1].toLowerCase() : "";
    if (!/\bsponsored\b/.test(rel)) return match;
    const merchant = inferMerchant(href);
    const isPlaceholder = href.includes('fpr=partner');
    if (!merchant && !isPlaceholder) return match; // 非联�? 跳过

    const m = merchant || 'placeholder';
    // URL 重写 (kittl.com �?pxf.io �? merchant 推断不变, link_id �?rewrite �?URL �?
    const finalHref = rewriteAffUrl(href);
    const h = crypto.createHash('sha1').update(finalHref).digest('hex').slice(0, 8);
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
    // 2026-08-17 halloween 集群: 已带 UTM 的 sponsored 链接 (如
    // ?utm_source=aitoptools&utm_medium=blog&utm_campaign=halloween2026) 不再追加,
    // 避免双重 utm_ 参数; aff-link 标记与 data-* 照常注入。
    const hasUtm = /[?&]utm_/.test(finalHref);
    const newHref = hasUtm ? finalHref : injectUtm(finalHref, m, linkId);
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
    console.error(`[FAIL] 找不�?out 目录: ${OUT_DIR} (先跑 npm run build)`);
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
  console.log(`\n══�?inject-aff-link (${dryRun ? 'DRY-RUN' : 'APPLIED'}) ═══`);
  console.log(`  �?${totalFiles} 个文件含联盟链接`);
  console.log(`  注入 ${totalInjected} �?aff-link �?(${dryRun ? '未改文件' : `${filesChanged} 个文件已改`})`);
  if (dryRun) console.log('  重跑 (去掉 --dry-run) 应用注入');
  else console.log('  �?注入完成, 重跑 npm run aff-link-audit 验证 100% 覆盖');
}

// 守卫: 只在 CLI 直接调用时跑 main(), 避免 import 时触�?// 单测脚本 scripts/test-inject-aff-link.mjs import 本文件复�?REWRITE_URL_MAP / rewriteAffUrl / inferMerchant
const isCLI = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isCLI) main();

// 导出供单测复�?(K3 7/28 单测要求)
export {
  REWRITE_URL_MAP,
  REWRITE_DOMAINS,
  rewriteAffUrl,
  inferMerchant,
  injectUtm,
  injectHtml,
  DOMAIN_MAP,
};
