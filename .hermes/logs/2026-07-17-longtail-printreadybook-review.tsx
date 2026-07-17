import Link from "next/link";

export default function printreadybook_review() {
  const tool = {
    slug: "printreadybook-review",
    title: "PrintReadyBook Review 2026: AI Book Printing Platform for Self-Publishers",
    metaDesc: "PrintReadyBook review for self-publishers and print shops. AI-powered book printing platform that automates layout, formatting, and print-ready PDF generation.",
    category: "AI Print & Packaging",
    rating: 4.5,
    price: "5/month",
    affiliateUrl: "https://printreadybook.com",
    visitUrl: "https://printreadybook.com",
    pros: ["Automates book layout and formatting for print-ready PDF output", "Supports multiple book sizes including trade, digest, and A4 formats", "AI checks bleed margins, spine width, and trim marks automatically", "Direct PDF export compatible with KDP, IngramSpark, and offset printers", "Batch processing for multi-title publishing workflows"],
    cons: ["Limited to book printing — no business card or flyer layout support", "AI auto-formatting sometimes misplaces images in complex layouts", "No CMYK color space verification for professional print accuracy", "Free tier limited to 10 pages per project"],
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      {/* Breadcrumb */}
      <nav className="text-sm mb-6 text-gray-500">
        <Link href="/">Home</Link>
        <span className="mx-2">/</span>
        <Link href="/category/ai-print-&-packaging">AI Print & Packaging</Link>
        <span className="mx-2">/</span>
        <span className="text-gray-700">{tool.title}</span>
      </nav>

      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center gap-3 mb-2">
          <span className="bg-teal-100 text-teal-800 text-xs font-medium px-2.5 py-0.5 rounded">
            {tool.category}
          </span>
          <span className="text-amber-600 font-semibold">{tool.rating} / 5</span>
          <span className="text-gray-500">{tool.price}</span>
        </div>
        <h1 className="text-3xl font-bold text-gray-900 mb-4">{tool.title}</h1>
        <p className="text-lg text-gray-600">{tool.metaDesc}</p>
        <a
          href={tool.affiliateUrl}
          target="_blank"
          rel="nofollow sponsored"
          className="inline-block mt-4 bg-amber-500 hover:bg-amber-600 text-white font-semibold px-6 py-3 rounded-lg transition"
        >
          Try PrintReadyBook Free →
        </a>
      </div>

      {/* Pros/Cons */}
      <div className="grid md:grid-cols-2 gap-6 mb-10">
        <div className="bg-green-50 border border-green-200 rounded-lg p-6">
          <h2 className="text-xl font-bold text-green-800 mb-4">Pros</h2>
          <ul className="space-y-2">
            {tool.pros.map((p, i) => (
              <li key={i} className="flex gap-2">
                <span className="text-green-600 mt-1">✓</span>
                <span>{p}</span>
              </li>
            ))}
          </ul>
        </div>
        <div className="bg-red-50 border border-red-200 rounded-lg p-6">
          <h2 className="text-xl font-bold text-red-800 mb-4">Cons</h2>
          <ul className="space-y-2">
            {tool.cons.map((c, i) => (
              <li key={i} className="flex gap-2">
                <span className="text-red-600 mt-1">✗</span>
                <span>{c}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Footer disclaimer */}
      <div className="mt-12 border-t pt-6">
        <p className="text-sm text-gray-400 italic">
          *This site is independently operated and not affiliated with aitoptools.com.*
        </p>
        <p className="text-xs text-gray-400 mt-2">
          We may earn a commission if you purchase through our affiliate links, at no extra cost to you.
        </p>
      </div>
    </div>
  );
}
