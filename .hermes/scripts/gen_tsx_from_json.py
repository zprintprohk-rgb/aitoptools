"""Generate TSX files from JSON content data"""
import json, os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_dir = "/mnt/f/aitoptools/.hermes/logs"

tools = json.load(open(f"{log_dir}/{today}-新工具入库.json"))
content = json.load(open("/mnt/f/aitoptools/.hermes/scripts/data/tsx_content.json"))

count = 0
for tool in tools:
    s = tool["slug"]
    n = tool["name"]
    c = tool["category"]
    p = tool["pricing"]
    v = tool["visit_url"]
    d = content.get(s)
    if not d:
        print(f"  SKIP {s} - no content data")
        continue
    
    rp = d["rel"].split("|")
    rn = d["reln"].split("|")
    related_links = "\n".join(
        f'          <Link href="/reviews/{a}" className="text-blue-600 hover:underline">{b}</Link>'
        for a, b in zip(rp, rn)
    )
    
    sw = "<span>" + "\u2605 " * d["rs"] + "\u2606 " * (5 - d["rs"]) + "</span>"
    
    tsx = f'''import type {{ Metadata }} from "next";
import Link from "next/link";

export const metadata: Metadata = {{
  title: "{d['title']}",
  description: "{d['desc']}",
  keywords: "{d['kw']}",
  openGraph: {{
    title: "{d['title']}",
    description: "{d['desc']}",
    type: "article",
  }},
}};

export default function {s.replace("-","").title().replace("Ai","AI").replace("Io","IO")}Page() {{
  return (
    <article className="max-w-4xl mx-auto px-4 py-8">
      <nav className="text-sm text-gray-500 mb-6" aria-label="Breadcrumb">
        <ol className="list-none p-0 inline-flex">
          <li className="flex items-center"><Link href="/">Home</Link><span className="mx-2">/</span></li>
          <li className="flex items-center"><Link href="/reviews">Reviews</Link><span className="mx-2">/</span></li>
          <li className="text-gray-800 font-medium">{n}</li>
        </ol>
      </nav>

      <header className="mb-10">
        <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{d["title"]}</h1>
        <p className="text-lg text-gray-600 leading-relaxed">{d["short"]}</p>
        <div className="flex flex-wrap gap-4 mt-6">
          <a href="{v}" target="_blank" rel="nofollow sponsored"
             className="inline-flex items-center px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition-colors">
            Try {n} Free &rarr;
          </a>
          <div className="flex items-center text-amber-500">
            {sw}
            <span className="ml-2 text-gray-600 text-sm">{d["r"]}/5</span>
          </div>
        </div>
      </header>

      <section className="bg-gray-50 rounded-xl p-6 mb-10">
        <h2 className="text-xl font-semibold mb-4">Quick Facts</h2>
        <dl className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div><dt className="text-gray-500 text-sm">Category</dt><dd className="font-medium">{c}</dd></div>
          <div><dt className="text-gray-500 text-sm">Best For</dt><dd className="font-medium">{d["best"]}</dd></div>
          <div><dt className="text-gray-500 text-sm">Pricing</dt><dd className="font-medium">{p}</dd></div>
          <div><dt className="text-gray-500 text-sm">Free Trial</dt><dd className="font-medium">{d["free"]}</dd></div>
        </dl>
      </section>

      <section className="prose prose-lg max-w-none mb-10">
        <h2>What Is {n}?</h2>
        <p>{d["intro"]}</p>

        <h2>Key Features for Print Businesses</h2>
        <ul>{d["feats"]}</ul>

        <h2>{n} vs Competitors</h2>
        <p>{d["ct"]}</p>
        <div className="overflow-x-auto my-6">
          <table className="min-w-full border-collapse border border-gray-300">
            <thead><tr className="bg-gray-100">
              <th className="border border-gray-300 px-4 py-2 text-left">Feature</th>
              <th className="border border-gray-300 px-4 py-2 text-left">{n}</th>
              <th className="border border-gray-300 px-4 py-2 text-left">{d["c1"]}</th>
              <th className="border border-gray-300 px-4 py-2 text-left">{d["c2"]}</th>
            </tr></thead>
            <tbody>{d["tbl"]}</tbody>
          </table>
        </div>

        <h2>Pros &amp; Cons</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 my-4">
          <div className="bg-green-50 p-4 rounded-lg">
            <h3 className="font-semibold text-green-800 mb-2">Pros</h3>
            <ul className="space-y-1">{d["pros"]}</ul>
          </div>
          <div className="bg-red-50 p-4 rounded-lg">
            <h3 className="font-semibold text-red-800 mb-2">Cons</h3>
            <ul className="space-y-1">{d["cons"]}</ul>
          </div>
        </div>

        <h2>Who Should Use {n}?</h2>
        <p>{d["who"]}</p>

        <h2>Pricing Breakdown</h2>
        <p>{d["price_p"]}</p>
      </section>

      <section className="bg-blue-50 rounded-xl p-6 mb-8">
        <h2 className="text-xl font-semibold mb-4">Related Reviews</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
{related_links}
        </div>
      </section>

      <section className="text-center bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl p-8 mb-10">
        <h2 className="text-2xl font-bold mb-3">Ready to Try {n}?</h2>
        <p className="mb-6 opacity-90">Start your free trial today and transform your print business workflow.</p>
        <a href="{v}" target="_blank" rel="nofollow sponsored"
           className="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-bold rounded-lg hover:bg-gray-100 transition-colors">
          Get Started with {n} &rarr;
        </a>
      </section>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-6">Frequently Asked Questions</h2>
        <div className="space-y-4">
          <details className="border rounded-lg p-4"><summary className="font-semibold cursor-pointer">{d["fq1"]}</summary><p className="mt-2 text-gray-600">{d["fa1"]}</p></details>
          <details className="border rounded-lg p-4"><summary className="font-semibold cursor-pointer">{d["fq2"]}</summary><p className="mt-2 text-gray-600">{d["fa2"]}</p></details>
          <details className="border rounded-lg p-4"><summary className="font-semibold cursor-pointer">{d["fq3"]}</summary><p className="mt-2 text-gray-600">{d["fa3"]}</p></details>
        </div>
      </section>
    </article>
  );
}}
'''
    out = f"{log_dir}/{today}-长尾-{s}.tsx"
    with open(out, "w", encoding="utf-8") as f:
        f.write(tsx)
    print(f"  OK {s}")
    count += 1

print(f"\nGenerated {count} TSX files")
