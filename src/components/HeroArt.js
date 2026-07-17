export default function HeroArt() {
  // Print-industry illustration: packaging box dieline (die-cut unfold lines),
  // CMYK registration dots, halftone gradient. All strokes, editorial style.
  return (
    <svg viewBox="0 0 340 300" role="img" aria-label="Print and packaging illustration" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="halftone" width="14" height="14" patternUnits="userSpaceOnUse">
          <circle cx="3" cy="3" r="1.6" fill="rgba(255,255,255,0.22)" />
        </pattern>
        <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stopColor="rgba(255,255,255,0.16)" />
          <stop offset="1" stopColor="rgba(255,255,255,0.04)" />
        </linearGradient>
      </defs>

      {/* halftone backdrop */}
      <circle cx="170" cy="150" r="132" fill="url(#halftone)" />
      <circle cx="170" cy="150" r="132" fill="none" stroke="rgba(255,255,255,0.25)" strokeWidth="1" strokeDasharray="3 6" />

      {/* box dieline — unfolded carton, stroke-only line art */}
      <g fill="none" stroke="#ffffff" strokeWidth="1.6" strokeLinejoin="round">
        {/* center panel */}
        <rect x="120" y="95" width="100" height="110" fill="url(#panel)" />
        {/* left panel */}
        <path d="M120 95 L70 82 L70 192 L120 205 Z" fill="rgba(255,255,255,0.06)" />
        {/* right panel */}
        <path d="M220 95 L270 82 L270 192 L220 205 Z" fill="rgba(255,255,255,0.06)" />
        {/* top flaps */}
        <path d="M120 95 L132 62 L208 62 L220 95" />
        <path d="M132 62 L126 44 L214 44 L208 62" strokeDasharray="4 4" />
        {/* bottom flaps */}
        <path d="M120 205 L132 238 L208 238 L220 205" />
        <path d="M132 238 L126 256 L214 256 L208 238" strokeDasharray="4 4" />
        {/* glue tabs */}
        <path d="M70 82 L52 88 L52 186 L70 192" strokeDasharray="4 4" />
        <path d="M270 82 L288 88 L288 186 L270 192" strokeDasharray="4 4" />
        {/* crease lines on center panel */}
        <line x1="145" y1="95" x2="145" y2="205" strokeDasharray="2 5" strokeWidth="1" opacity="0.7" />
        <line x1="195" y1="95" x2="195" y2="205" strokeDasharray="2 5" strokeWidth="1" opacity="0.7" />
      </g>

      {/* design mark on center panel: t-shirt glyph */}
      <g fill="none" stroke="#f59e0b" strokeWidth="2" strokeLinejoin="round" strokeLinecap="round">
        <path d="M155 128 L147 136 L153 144 L153 172 L187 172 L187 144 L193 136 L185 128 L177 132 Q170 138 163 132 Z" fill="rgba(245,158,11,0.12)" />
      </g>

      {/* CMYK registration dots */}
      <g>
        <circle cx="170" cy="30" r="7" fill="#22d3ee" stroke="#fff" strokeWidth="1.4" />
        <circle cx="196" cy="30" r="7" fill="#f472b6" stroke="#fff" strokeWidth="1.4" />
        <circle cx="222" cy="30" r="7" fill="#facc15" stroke="#fff" strokeWidth="1.4" />
        <circle cx="248" cy="30" r="7" fill="#1c1917" stroke="#fff" strokeWidth="1.4" />
      </g>

      {/* registration crosshairs */}
      <g stroke="rgba(255,255,255,0.7)" strokeWidth="1.2" fill="none">
        <circle cx="66" cy="252" r="9" />
        <line x1="66" y1="238" x2="66" y2="266" />
        <line x1="52" y1="252" x2="80" y2="252" />
        <circle cx="274" cy="252" r="9" />
        <line x1="274" y1="238" x2="274" y2="266" />
        <line x1="260" y1="252" x2="288" y2="252" />
      </g>

      {/* measurement ruler */}
      <g stroke="rgba(255,255,255,0.55)" strokeWidth="1" fill="none">
        <line x1="120" y1="278" x2="220" y2="278" />
        <line x1="120" y1="274" x2="120" y2="282" />
        <line x1="145" y1="275" x2="145" y2="281" />
        <line x1="170" y1="274" x2="170" y2="282" />
        <line x1="195" y1="275" x2="195" y2="281" />
        <line x1="220" y1="274" x2="220" y2="282" />
      </g>
    </svg>
  )
}
