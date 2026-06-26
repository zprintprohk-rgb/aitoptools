/**
 * Print AI Tools — Global Site Configuration
 * 
 * CENTRALIZED BRAND CONFIG
 * All brand references across the site should import from here.
 * To rebrand entirely (e.g. switch to a pure vertical brand),
 * just change the values below and rebuild.
 */

const siteConfig = {
  brand: 'Print AI Tools',
  domain: 'aitoptools.net',
  tagline: 'AI Tools for Print Shops & Independent Store Owners',
  description: 'Hands-on reviews of the best AI tools for print shops, packaging design, cross-border e-commerce, and independent store owners.',
  
  // Footer
  footerTagline: 'Helping print shops and independent store owners find the right AI tools.',
  
  // Legal
  independentDisclaimer: 'This site is independently operated and is not affiliated with, partnered with, or authorized by aitoptools.com. All content is original and focused on AI tools for print shops, packaging, cross-border e-commerce, and independent store operations.',
  
  // OG metadata
  ogSiteName: 'Print AI Tools',
  
  // Categories for navigation (order matters)
  categories: [
    { name: 'Print & Packaging', slug: 'ai-print-design', icon: '🖨️' },
    { name: 'E-Commerce', slug: 'ai-ecommerce', icon: '🛒' },
    { name: 'AI Writing', slug: 'ai-writing', icon: '✍️' },
    { name: 'AI Image', slug: 'ai-image', icon: '🎨' },
    { name: 'AI Video', slug: 'ai-video', icon: '🎬' },
    { name: 'AI Voice', slug: 'ai-voice', icon: '🎙️' },
  ],
}

export default siteConfig
