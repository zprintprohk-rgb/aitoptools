import json, os, datetime

logdir = '/mnt/f/aitoptools/.hermes/logs'
today = datetime.date.today().isoformat()

with open(os.path.join(logdir, f"{today}-新工具入库.json")) as f:
    data = json.load(f)

def make_tsx(tool):
    slug = tool['slug']
    name = tool['name']
    cat = tool['category']
    desc = tool['description']
    rating = tool['rating']
    price = tool['price']
    visit_url = tool['visitUrl']
    pros = tool['pros']
    cons = tool['cons']
    
    # Generate TDK
    title = f"{name} Review 2026: AI-Powered Print Design Tool for Small Print Shops"
    meta_desc = f"Read our honest {name} review for print shops. Features, pricing, pros/cons, and how this AI tool helps print businesses create better materials faster."
    
    # Build pros/cons JSX
    pros_jsx = '\n'.join([f'      <li>{p}</li>' for p in pros])
    cons_jsx = '\n'.join([f'      <li>{c}</li>' for c in cons])
    
    tsx = f'''import React from 'react';
import Link from 'next/link';
import Head from 'next/head';

export default function {name.replace(/\s+/g, '').replace(/[^a-zA-Z0-9]/g, '')}Review() {{
  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="description" content="{meta_desc}" />
        <meta property="og:title" content="{title}" />
        <meta property="og:description" content="{meta_desc}" />
        <meta name="robots" content="index, follow" />
      </Head>
      <article className="max-w-4xl mx-auto px-4 py-8">
        <nav className="text-sm text-gray-500 mb-6" aria-label="Breadcrumb">
          <Link href="/">Home</Link>
          <span className="mx-2">/</span>
          <Link href="/category/{cat.lower().replace(/\s+/g, '-')}">{cat}</Link>
          <span className="mx-2">/</span>
          <span className="text-gray-800">{name}</span>
        </nav>

        <h1 className="text-3xl md:text-4xl font-bold mb-4">{title}</h1>

        <div className="flex flex-wrap items-center gap-4 mb-6 text-sm">
          <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full">{cat}</span>
          <span className="text-yellow-500 font-semibold">{"★".repeat(Math.round({rating}))}{"☆".repeat(5 - Math.round({rating}))} {rating}</span>
          <span className="text-gray-500">{price}</span>
        </div>

        <p className="text-lg text-gray-700 mb-6">{desc}</p>

        <a
          href="{visit_url}"
          target="_blank"
          rel="nofollow sponsored"
          className="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition mb-8"
        >
          Try {name} Free →
        </a>

        <div className="grid md:grid-cols-2 gap-6 mb-8">
          <div className="bg-green-50 p-6 rounded-lg">
            <h2 className="text-xl font-bold mb-3 text-green-800">Pros ✅</h2>
            <ul className="space-y-2">
{pros_jsx}
            </ul>
          </div>
          <div className="bg-red-50 p-6 rounded-lg">
            <h2 className="text-xl font-bold mb-3 text-red-800">Cons ❌</h2>
            <ul className="space-y-2">
{cons_jsx}
            </ul>
          </div>
        </div>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">What is {name}?</h2>
          <p className="text-gray-700 mb-4">{desc} This AI-powered platform helps print shops, packaging businesses, and e-commerce sellers create professional-grade materials without hiring a designer.</p>
          <p className="text-gray-700">Whether you are running a small print-on-demand store or a full-service print shop, {name} provides the tools you need to streamline your design workflow and deliver better results to your customers.</p>
        </section>

        <section className="mb-8 bg-gray-50 p-6 rounded-lg">
          <h2 className="text-2xl font-bold mb-4">Who Is {name} For?</h2>
          <ul className="space-y-3 text-gray-700">
            <li><strong>Print Shop Owners</strong> — Create print-ready designs for walk-in customers</li>
            <li><strong>POD Sellers</strong> — Design mockups and product graphics for t-shirts, mugs, and more</li>
            <li><strong>Packaging Designers</strong> — Prototype packaging with AI-assisted layout tools</li>
            <li><strong>Marketing Teams</strong> — Produce consistent branded materials at scale</li>
            <li><strong>Freelance Designers</strong> — Speed up client project turnaround with AI features</li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">Pricing & Plans</h2>
          <p className="text-gray-700 mb-4">Starting at {price}, {name} offers flexible pricing to match different needs and budgets.</p>
          <p className="text-gray-700">We recommend trying the free tier or free trial before committing to a paid plan to ensure the tool meets your specific print workflow requirements.</p>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">Alternatives to {name}</h2>
          <ul className="space-y-2 text-gray-700">
            <li><Link href="/canva-ai-review" className="text-blue-600 hover:underline">Canva AI</Link> — Best all-around design tool with extensive template library</li>
            <li><Link href="/adobe-firefly-review" className="text-blue-600 hover:underline">Adobe Firefly</Link> — Professional-grade AI image generation for print</li>
            <li><Link href="/kittl-review" className="text-blue-600 hover:underline">Kittl</Link> — Specialized print design tool for t-shirts and merchandise</li>
            <li><Link href="/photoroom-review" className="text-blue-600 hover:underline">Photoroom</Link> — AI product photography for e-commerce and POD</li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-bold mb-4">Final Verdict</h2>
          <div className="flex items-center gap-2 mb-4">
            <span className="text-3xl text-yellow-500">{"★".repeat(Math.round({rating}))}{"☆".repeat(5 - Math.round({rating}))}</span>
            <span className="text-xl font-bold">{rating}/5</span>
          </div>
          <p className="text-gray-700 mb-4">{name} earns a {rating}/5 rating for its {cat.lower()} capabilities. It is a solid choice for print businesses looking to improve their design workflow with AI assistance.</p>
          <a
            href="{visit_url}"
            target="_blank"
            rel="nofollow sponsored"
            className="inline-block bg-green-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-700 transition"
          >
            Get Started with {name} →
          </a>
        </section>
      </article>
    </>
  );
}}
'''
    return tsx

# Generate all 10 TSX files
for tool in data['tools']:
    slug = tool['slug']
    tsx_content = make_tsx(tool)
    filename = f"{today}-长尾-{slug}.tsx"
    outpath = os.path.join(logdir, filename)
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(tsx_content)
    print(f"OK: Generated {filename} ({len(tsx_content)} bytes)")

print("\nDone generating all 10 TSX files.")
