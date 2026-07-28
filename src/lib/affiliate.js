/**
 * buildAffLinkAttrs — W1-T1 度量埋点 helper (按 M3_MONTH1_RUNBOOK §W1-T1 步骤 2)
 *
 * 给带 affiliateUrl 的 review/tool 生成 GA4 埋点属性 (aff-link class + 3 data + UTM)
 * 66 条 review 自动全打标, 不需改 reviews.json 数据层。
 *
 * @param {Object} item - review 或 tool 对象 (有 slug + affiliateUrl)
 * @param {string} position - 链接位置 (用于 link_id 后缀, e.g. 'card-cta' / 'detail-cta' / 'verdict-cta-a')
 * @returns {Object|null} 链接属性对象 { href, className, data-merchant, data-link-id, data-target } 或 null (无 affiliateUrl)
 *
 * 用法:
 *   const aff = buildAffLinkAttrs(review, 'card-cta')
 *   if (aff) return <a {...aff} className={`${aff.className} card-cta card-cta-deal`} target="_blank" rel="nofollow sponsored">Check Deal ↗</a>
 *
 * 设计选择:
 * 1. merchant 优先用 item.merchant 字段, fallback slug 第一段 (vs-* slug 也能解析出主商家)
 * 2. UTM 4 参固定: utm_source=aitoptools / utm_medium=affiliate / utm_campaign=<merchant> / utm_content=<link_id>
 *    双保险: utm_campaign 冗余 merchant, utm_content 冗余 link_id (runbook 附录 A 命名规范)
 * 3. target_type 默认 'product' (runbook 附录 A enum, 大多数 affiliate 链跳产品页)
 * 4. 不改 affiliateUrl 原追踪参数, 只在 URL 末尾 append UTM (URL constructor 自动 merge)
 * 5. visitUrl 走非 aff-link 路径, 此 helper 只处理 affiliateUrl
 */
export function buildAffLinkAttrs(item, position) {
  if (!item || !item.affiliateUrl) return null
  // K3 7/28 修复 (compare 页 toolA/toolB 用 reviewSlug 不是 slug, 原代码 'undefined-verdict-cta-a'): slug 兜底 reviewSlug
  const slug = item.slug || item.reviewSlug || 'unknown'
  const merchant = String(item.merchant || (slug !== 'unknown' ? slug.split('-')[0] : 'unknown')).toLowerCase()
  const linkId = `${slug}-${position}`
  let url
  try {
    url = new URL(item.affiliateUrl)
  } catch (e) {
    // 非法 URL fallback: 原样返回, 不打标 (避免埋点污染)
    return null
  }
  url.searchParams.set('utm_source', 'aitoptools')
  url.searchParams.set('utm_medium', 'affiliate')
  url.searchParams.set('utm_campaign', merchant)
  url.searchParams.set('utm_content', linkId)
  return {
    href: url.toString(),
    className: 'aff-link',
    'data-merchant': merchant,
    'data-link-id': linkId,
    'data-target': 'product',
  }
}
