import config from '@/config'

export const metadata = {
  title: 'Resources & Partner Directory | Print AI Tools',
  description: 'Where Print AI Tools is listed: AI tool directories, launch platforms and industry resources. All outbound links are nofollow.',
  alternates: { canonical: 'https://aitoptools.net/resources/' },
}

const DIRECTORIES = [
  { name: 'AI Toolz Dir', url: 'https://www.aitoolzdir.com/', note: 'AI tools directory (DR66)' },
  { name: 'Wired Business', url: 'https://wired.business/', note: 'Business & web directory (DR77)' },
  { name: 'Findly.tools', url: 'https://findly.tools/', note: 'AI tools directory (DR80)' },
  { name: 'ToolPilot', url: 'https://www.toolpilot.ai/', note: 'AI tool discovery platform (DR78)' },
  { name: 'Dofollow.Tools', url: 'https://dofollow.tools/', note: 'Dofollow directory exchange (DR73)' },
  { name: 'TheNextAI', url: 'https://thenextai.com/', note: 'AI tools directory' },
  { name: 'LaunchBoosts', url: 'https://launchboosts.com/', note: 'Product launch platform' },
  { name: 'Startuplist.in', url: 'https://startuplist.in/', note: 'Startup & tool directory' },
]

export default function ResourcesPage() {
  return (
    <div className="resources-page container" style={{ maxWidth: 760, margin: '0 auto', padding: '32px 0 64px' }}>
      <h1>Resources &amp; Partner Directory</h1>
      <p>
        {config.brand} is listed in the following AI tool directories and launch platforms.
        These pages exist so readers and search engines can find independent review sites like ours
        through multiple channels. All outbound links on this page are <code>rel=&quot;nofollow&quot;</code>.
      </p>

      <ul style={{ listStyle: 'none', padding: 0, margin: '24px 0' }}>
        {DIRECTORIES.map((d) => (
          <li key={d.url} style={{ padding: '12px 0', borderBottom: '1px solid rgba(23,32,28,0.08)' }}>
            <a href={d.url} target="_blank" rel="nofollow noopener noreferrer" style={{ fontWeight: 600 }}>
              {d.name}
            </a>
            <span style={{ color: 'var(--k-tertiary)', fontSize: '0.9rem', marginLeft: 8 }}>{d.note}</span>
          </li>
        ))}
      </ul>

      <p style={{ fontSize: '0.9rem', color: 'var(--k-tertiary)' }}>
        Want to list your directory here or suggest a resource? Contact us via the <a href="/contact/">contact page</a>.
      </p>
    </div>
  )
}
