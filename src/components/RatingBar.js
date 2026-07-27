export default function RatingBar({ rating, max = 5, showValue = true }) {
  const full = Math.floor(rating)
  const stars = '★'.repeat(full) + '☆'.repeat(max - full)
  // hotfix 7/27: 删 rating-track + rating-fill 进度条 (千问 P1-1 尾巴清理)。
  // 原因：进度条数据是 rating/max 真值不是假数据，但视觉上和 ★ + 4.0 文字 100% 冗余，
  // 在卡片里纯装饰无刻度无数字，看着像"评分进度"却什么都不是 (千问诊断的"无意义进度条噪音")。
  // 保留 stars + value 已足够。CSS 同步在 globals.css 删 .rating-bar .rating-track / .rating-fill。
  return (
    <span className="rating-bar" role="img" aria-label={`Rated ${rating} out of ${max}`}>
      <span className="rating-stars" aria-hidden="true">{stars}</span>
      {showValue && <span className="rating-value">{rating.toFixed(1)}</span>}
    </span>
  )
}
