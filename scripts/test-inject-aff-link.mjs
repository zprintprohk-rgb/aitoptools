#!/usr/bin/env node
/**
 * test-inject-aff-link.mjs — REWRITE_URL_MAP 单测 (K3 7/28 拍板)
 *
 * 覆盖: REWRITE_URL_MAP 字典 (kittl.com → pxf.io) 输入断言
 * 目的: 字典改动 (扩 entry/改 entry) 立刻有单测兜底, 堵住新单点
 *
 * 用法: node scripts/test-inject-aff-link.mjs
 * 接入: package.json scripts.test:rewrite-url
 * 不依赖: 纯 stdlib + import inject-aff-link.mjs 复用 rewriteAffUrl/inferMerchant
 */

import assert from 'node:assert/strict';
import { rewriteAffUrl, inferMerchant, injectUtm, REWRITE_URL_MAP, REWRITE_DOMAINS } from './inject-aff-link.mjs';

let pass = 0, fail = 0;
const results = [];

function test(name, fn) {
  try {
    fn();
    results.push({ name, status: '✓ PASS' });
    pass++;
  } catch (e) {
    results.push({ name, status: `✗ FAIL: ${e.message}` });
    fail++;
  }
}

console.log('═══ REWRITE_URL_MAP 单测 (K3 7/28) ═══\n');

// === 1. 字典本身 ===
test('REWRITE_URL_MAP 字典包含 kittl.com → pxf.io', () => {
  assert.equal(REWRITE_URL_MAP['kittl.com'], 'https://kittl.pxf.io/qWNvPn');
});

test('REWRITE_DOMAINS 是字典 key 列表', () => {
  assert.deepEqual([...REWRITE_DOMAINS].sort(), ['kittl.com']);
});

// === 2. rewriteAffUrl 行为 ===
test('rewrite: https://kittl.com/ → pxf.io', () => {
  assert.equal(rewriteAffUrl('https://kittl.com/'), 'https://kittl.pxf.io/qWNvPn');
});

test('rewrite: https://kittl.com/?fpr=partner → pxf.io (丢 ?fpr=partner, 走 pxf)', () => {
  assert.equal(rewriteAffUrl('https://kittl.com/?fpr=partner'), 'https://kittl.pxf.io/qWNvPn');
});

test('rewrite: https://kittl.com/pricing → pxf.io (path 丢)', () => {
  assert.equal(rewriteAffUrl('https://kittl.com/pricing'), 'https://kittl.pxf.io/qWNvPn');
});

test('rewrite: https://www.kittl.com/ → pxf.io (www 子域也覆盖)', () => {
  assert.equal(rewriteAffUrl('https://www.kittl.com/'), 'https://kittl.pxf.io/qWNvPn');
});

test('rewrite: https://kittl.com?utm_source=test → pxf.io (query 丢)', () => {
  assert.equal(rewriteAffUrl('https://kittl.com?utm_source=test'), 'https://kittl.pxf.io/qWNvPn');
});

// === 3. negative case: 不在字典内的域名不动 ===
test('no rewrite: https://mockey.ai?via=jerome796 → 原样返回 (mockey.ai 不在 REWRITE_DOMAINS)', () => {
  assert.equal(rewriteAffUrl('https://mockey.ai?via=jerome796'), 'https://mockey.ai?via=jerome796');
});

test('no rewrite: https://printful.com/a/... → 原样', () => {
  assert.equal(rewriteAffUrl('https://printful.com/a/15297661'), 'https://printful.com/a/15297661');
});

test('no rewrite: https://example.com/kittl.com-in-path → 原样 (path 里含 kittl.com 不算 host)', () => {
  // new URL() 解析 host 是 example.com, 不触发 rewrite
  assert.equal(rewriteAffUrl('https://example.com/kittl.com-in-path'), 'https://example.com/kittl.com-in-path');
});

test('no rewrite: 非法 URL (garbage) → 原样', () => {
  assert.equal(rewriteAffUrl('not-a-url'), 'not-a-url');
});

// === 4. 端到端: rewrite + injectUtm + merchant 推断 ===
test('E2E: kittl.com 完整链路 rewrite → UTM 注入 → merchant=kittl', () => {
  const raw = 'https://kittl.com/';
  const rewritten = rewriteAffUrl(raw);
  const merchant = inferMerchant(rewritten);
  const linkId = 'kittl-review-card-cta';
  const finalHref = injectUtm(rewritten, merchant, linkId);
  // 验证最终 href 包含 pxf.io + 4 参 UTM
  assert.match(finalHref, /^https:\/\/kittl\.pxf\.io\/qWNvPn\?/);
  assert.match(finalHref, /utm_source=aitoptools/);
  assert.match(finalHref, /utm_medium=affiliate/);
  assert.match(finalHref, /utm_campaign=kittl/);
  assert.match(finalHref, /utm_content=kittl-review-card-cta/);
});

test('E2E: 字典新增 entry (假设 mockey.ai → m.pxf.io) 时, mockey 链接也走 rewrite — 字典可扩展性测试', () => {
  // 当前字典只有 kittl.com, mockey.ai 不在 REWRITE_DOMAINS → 验证 negative E2E
  const raw = 'https://mockey.ai?via=jerome796';
  const rewritten = rewriteAffUrl(raw);
  // 期望: 原样返回 (mockey.ai 不在 REWRITE_DOMAINS)
  assert.equal(rewritten, raw);
  // 这个测试是为了未来扩 REWRITE 字典时, 单测自动 fail 提醒 "扩后还要加新 case"
});

// === 输出 ===
console.log(results.map(r => `  ${r.status}  ${r.name}`).join('\n'));
console.log(`\n${'═'.repeat(40)}`);
console.log(`  ${pass} pass / ${fail} fail / ${pass + fail} total`);
console.log('═'.repeat(40));

if (fail > 0) process.exit(1);
process.exit(0);
