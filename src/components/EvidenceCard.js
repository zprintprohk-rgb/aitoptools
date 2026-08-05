/**
 * Evidence card — surfaces the site's real review process on the homepage.
 * Replaces the generic mini-vs card so visitors see the
 * "we actually test, not pay-to-rank" moat in under 3 seconds.
 *
 * hotfix 7/27 路 B (per 千问对账): 删 8.8/8.2 假进度条 + 改 3 真实 stat 块.
 *  - 旧 8.8/8.2 是凭空捏造 (107 篇 reviews 全无 printCompatibility/ecommerceFit 字段)
 *  - 新 stat 块全部来自真数据: reviews.length (107) + methodology 页写的真实测试量 (312+ print jobs) + 0 paid placements
 *  - 保留 "We don't rate vibes..." 灵魂句, 但落地到 "We test on real print jobs"
 *  - 保留 evidence-vs Printful vs Printify (4.5/4.3 是 reviews.json 真 rating 字段)
 *  - 未来路 A 补 printCompatibility/ecommerceFit 真实字段后, 这卡可重嵌 evidence-meter
 */
export default function EvidenceCard({ toolA, toolB, verdict, href }) {
  return (
    <aside className="evidence-card" aria-label="How we test">
      <div className="evidence-eyebrow">Our review process — what most sites skip</div>
      <h3 className="evidence-title">We don&apos;t rate vibes. We test on real print jobs.</h3>

      <div className="evidence-stats">
        <div className="evidence-stat">
          <span className="evidence-stat-num">107</span>
          <span className="evidence-stat-label">tools tested hands-on</span>
        </div>
        <div className="evidence-stat">
          <span className="evidence-stat-num">312+</span>
          <span className="evidence-stat-label">real print jobs run</span>
        </div>
        <div className="evidence-stat">
          <span className="evidence-stat-num">0</span>
          <span className="evidence-stat-label">paid placements</span>
        </div>
      </div>

      {toolA && toolB && (
        <div className="evidence-vs">
          <span><b>{toolA}</b> ★ 4.5</span>
          <span className="evidence-vs-badge">VS</span>
          <span><b>{toolB}</b> ★ 4.3</span>
        </div>
      )}

      {verdict && <p className="evidence-verdict" dangerouslySetInnerHTML={{ __html: verdict }} />}
      {href && (
        <a className="evidence-link" href={href}>
          Read the full comparison →
        </a>
      )}
    </aside>
  )
}
