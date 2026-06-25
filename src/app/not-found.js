import Link from 'next/link'
export default function NotFound() {
  return (
    <div style={{ textAlign: 'center', padding: '80px 20px' }}>
      <h1 style={{ fontSize: '3rem', marginBottom: '10px' }}>404</h1>
      <p style={{ color: '#64748b', marginBottom: '20px' }}>Review not found.</p>
      <Link href="/" style={{ color: '#2563eb' }}>← Back to all reviews</Link>
    </div>
  )
}
