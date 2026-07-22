import Link from 'next/link';

export default function ActivecampaignReview() {
  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      <nav className="text-sm text-gray-500 mb-6" aria-label="Breadcrumb">
        <Link href="/">Home</Link>
        <span className="mx-2">/</span>
        <Link href={"/category/ai-customer-service"}>{AI Customer Service}</Link>
        <span className="mx-2">/</span>
        <span className="text-gray-800">{Activecampaign}</span>
      </nav>

      <h1 className="text-3xl md:text-4xl font-bold mb-4">{ActiveCampaign Review 2026: Marketing Automation for Print Shop Customer Retention}</h1>

      <div className="flex flex-wrap items-center gap-4 mb-6 text-sm">
        <span className="bg-teal-100 text-teal-800 px-3 py-1 rounded-full">{AI Customer Service}</span>
        <span className="text-amber-500 font-semibold">{★★★★☆} {4.5}</span>
        <span className="text-gray-500">{$15/month}</span>
        <a href={"https://www.activecampaign.com/?fpr=partner"} target="_blank" rel="nofollow sponsored" className="bg-amber-500 text-white px-4 py-2 rounded hover:bg-amber-600 transition">
          Visit Site &rarr;
        </a>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
        <div className="bg-green-50 p-6 rounded-lg border border-gray-100">
          <h3 className="text-lg font-semibold text-green-800 mb-3">Pros</h3>
          <ul className="space-y-2">
                        <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Industry-leading automation builder with conditional logic</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Built-in CRM for managing customer relationships</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Predictive sending and AI content optimization</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Deep e-commerce integrations with Shopify and WooCommerce</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Split automation paths for personalized customer journeys</span></li>
          </ul>
        </div>
        <div className="bg-red-50 p-6 rounded-lg border border-gray-100">
          <h3 className="text-lg font-semibold text-red-800 mb-3">Cons</h3>
          <ul className="space-y-2">
                        <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Steep learning curve compared to simpler email tools</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Expensive for basic email-only use cases</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>No free tier - 14-day trial only</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Email editor less intuitive than Mailchimp's</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Customer support can be slow on lower-tier plans</span></li>
          </ul>
        </div>
      </div>

      <div>
        <p className="text-gray-500 italic">
          Full review content loaded from our reviews database. This is a placeholder page template.
        </p>
      </div>

      <div className="mt-8 p-6 bg-gray-50 rounded-lg border border-gray-200">
        <p className="text-sm text-gray-500">
          *This site is independently operated and not affiliated with aitoptools.com.
        </p>
      </div>
    </article>
  );
}
