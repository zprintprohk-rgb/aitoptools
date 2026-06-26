import Link from 'next/link'
export default function NotFound() {
  return (
    <div className="not-found">
      <h1>404</h1>
      <p>Page not found. This review hasn&apos;t been published yet, or the link is incorrect.</p>
      <Link href="/" className="cta-button">Back to Home</Link>
    </div>
  )
}
