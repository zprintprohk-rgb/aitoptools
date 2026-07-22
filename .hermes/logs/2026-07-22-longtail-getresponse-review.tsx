import Link from 'next/link';

export default function GetresponseReview() {
  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      <nav className="text-sm text-gray-500 mb-6" aria-label="Breadcrumb">
        <Link href="/">Home</Link>
        <span className="mx-2">/</span>
        <Link href={"/category/ai-e-commerce"}>{AI E-Commerce}</Link>
        <span className="mx-2">/</span>
        <span className="text-gray-800">{Getresponse}</span>
      </nav>

      <h1 className="text-3xl md:text-4xl font-bold mb-4">{GetResponse Review 2026: All-in-One Email Marketing for E-Commerce Sellers}</h1>

      <div className="flex flex-wrap items-center gap-4 mb-6 text-sm">
        <span className="bg-teal-100 text-teal-800 px-3 py-1 rounded-full">{AI E-Commerce}</span>
        <span className="text-amber-500 font-semibold">{★★★★☆} {4.4}</span>
        <span className="text-gray-500">{$15.58/month}</span>
        <a href={"https://www.getresponse.com/?fpr=partner"} target="_blank" rel="nofollow sponsored" className="bg-amber-500 text-white px-4 py-2 rounded hover:bg-amber-600 transition">
          Visit Site &rarr;
        </a>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
        <div className="bg-green-50 p-6 rounded-lg border border-gray-100">
          <h3 className="text-lg font-semibold text-green-800 mb-3">Pros</h3>
          <ul className="space-y-2">
                        <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>All-in-one platform: email + landing pages + webinars</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Conversion funnel builder for e-commerce automation</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>AI email generator creates campaigns from product URLs</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>Unlimited email sends on all paid plans</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✓</span><span>24/7 customer support available</span></li>
          </ul>
        </div>
        <div className="bg-red-50 p-6 rounded-lg border border-gray-100">
          <h3 className="text-lg font-semibold text-red-800 mb-3">Cons</h3>
          <ul className="space-y-2">
                        <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Interface feels outdated compared to newer competitors</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Webinar features are basic compared to dedicated tools</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>A/B testing limited to subject lines on lower tiers</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Growing stores may outgrow the platform's capabilities</span></li>
            <li className="flex items-start gap-2 text-gray-700"><span>✗</span><span>Mobile app lacks full functionality of desktop version</span></li>
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
