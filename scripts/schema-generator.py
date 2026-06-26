#!/usr/bin/env python3
"""
Schema JSON-LD Generator for AI Tool Review Site
Generates Review + Product + FAQ Schema for Google Rich Results.
Injected into <head> for 20-50% CTR lift on search results.

Usage:
  python schema-generator.py                    # Test with Jasper AI
  python schema-generator.py --slug writesonic  # Generate for specific tool
  python schema-generator.py --inject           # Inject Schema into all published reviews.json
"""

import json, os, sys, argparse

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_FILE = os.path.join(PROJ, "scripts", "tool-params.json")
REVIEWS_FILE = os.path.join(PROJ, "src", "data", "reviews.json")


def load_tool_params():
    with open(PARAMS_FILE, encoding="utf-8") as f:
        return json.load(f)


def load_reviews():
    with open(REVIEWS_FILE, encoding="utf-8") as f:
        return json.load(f)


def find_tool(slug):
    data = load_tool_params()
    for t in data["tools"]:
        if t["slug"] == slug:
            return t
    # Fall back to reviews.json
    for r in load_reviews():
        if r["slug"].replace("-review", "") == slug:
            return r
    return None


def generate_review_schema(
    tool_name: str,
    rating: float,
    price_monthly: float,
    author_name: str = "AI Tool Reviews",
    date_published: str = "2026-01-01",
    pros: list = None,
    cons: list = None,
    url: str = None,
    description: str = None,
) -> str:
    """Generate Review + Product combined Schema markup."""
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Review",
                "name": f"{tool_name} Review 2026",
                "author": {"@type": "Organization", "name": author_name},
                "datePublished": date_published,
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": str(rating),
                    "bestRating": "5",
                    "worstRating": "1",
                },
                "itemReviewed": {
                    "@type": "SoftwareApplication",
                    "name": tool_name,
                    "applicationCategory": "AIApplication",
                    "operatingSystem": "All",
                    "offers": {
                        "@type": "Offer",
                        "price": str(price_monthly),
                        "priceCurrency": "USD",
                        "priceSpecification": {
                            "@type": "UnitPriceSpecification",
                            "price": str(price_monthly),
                            "priceCurrency": "USD",
                            "billingIncrement": 1,
                            "billingPeriod": "month",
                        },
                    },
                },
            }
        ],
    }
    if pros:
        schema["@graph"][0]["positiveNotes"] = [
            {"@type": "ListItem", "position": i + 1, "text": p}
            for i, p in enumerate(pros)
        ]
    if cons:
        schema["@graph"][0]["negativeNotes"] = [
            {"@type": "ListItem", "position": i + 1, "text": c}
            for i, c in enumerate(cons)
        ]
    if description:
        schema["@graph"][0]["description"] = description
    if url:
        schema["@graph"][0]["url"] = url

    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'


def generate_faq_schema(faq_list: list) -> str:
    """Generate FAQ Schema.
    faq_list: [{"question": "xxx", "answer": "xxx"}, ...]
    """
    if not faq_list:
        return ""
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [],
    }
    for item in faq_list:
        schema["mainEntity"].append({
            "@type": "Question",
            "name": item["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["answer"],
            },
        })
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'


def generate_software_schema(tool: dict) -> str:
    """Generate SoftwareApplication Schema for the tool itself."""
    schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": tool.get("name", tool.get("slug", "")),
        "applicationCategory": "AIApplication",
        "operatingSystem": "All",
        "description": tool.get("description", ""),
        "offers": {
            "@type": "Offer",
            "price": str(tool.get("price_monthly", 0)),
            "priceCurrency": "USD",
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": str(tool.get("rating", 0)),
            "bestRating": "5",
            "worstRating": "1",
            "ratingCount": "1",
        },
    }
    if tool.get("affiliateLink"):
        schema["url"] = tool["affiliateLink"]
    return f'<script type="application/ld+json">\n{json.dumps(schema, indent=2)}\n</script>'


def generate_page_schema(tool: dict) -> str:
    """Generate WebPage + BreadcrumbList Schema."""
    name = f"{tool['name']} Review 2026"
    slug = tool["slug"]
    return f'''<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": name,
    "description": tool.get("description", f"Honest {tool['name']} review with pros, cons, pricing and features."),
    "breadcrumb": {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://aitoptools.pages.dev/"},
            {"@type": "ListItem", "position": 2, "name": tool["category"], "item": "https://aitoptools.pages.dev/?category=" + tool["category"]},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"https://aitoptools.pages.dev/{slug}-review"}
        ]
    }
}, indent=2)}
</script>'''


def inject_schema_to_html(html_content: str, schema_code: str) -> str:
    """Inject Schema code before </head> tag."""
    if "</head>" in html_content:
        return html_content.replace("</head>", f"{schema_code}\n</head>")
    return html_content + schema_code


def generate_faq_for_tool(tool: dict) -> list:
    """Generate common FAQs for a tool review."""
    name = tool["name"]
    cat = tool["category"]
    price = tool.get("price_monthly", 0)
    return [
        {
            "question": f"Is {name} worth it?",
            "answer": f"{name} is {'recommended' if tool.get('rating', 0) >= 4 else 'a decent option'} for {cat} use cases. "
                      f"With a rating of {tool.get('rating', 0)}/5 and starting at ${price}/month, "
                      f"it {'offers good value' if price <= 20 else 'is a premium option worth considering'} "
                      f"for users who need its specific features."
        },
        {
            "question": f"How much does {name} cost?",
            "answer": f"{name} starts at ${price}/month. Pricing varies by plan and features selected. "
                      "Check their official website for the most current pricing and any available discounts."
        },
        {
            "question": f"Does {name} have a free trial?",
            "answer": f"Most {cat} tools like {name} offer either a free trial or a free tier. "
                      "Visit their website to check current trial availability."
        },
        {
            "question": f"What is {name} best for?",
            "answer": f"{name} is best suited for users who need {tool.get('description', 'its specific features')}. "
                      f"It excels in {cat} use cases and is particularly good for {'professional users' if price > 20 else 'budget-conscious users'}."
        },
        {
            "question": f"Alternatives to {name}?",
            "answer": f"Top alternatives include {tool.get('competitor', 'other tools in the same category')}. "
                      f"The best choice depends on your specific needs, budget, and workflow requirements."
        },
    ]


def main():
    parser = argparse.ArgumentParser(description="Schema JSON-LD Generator")
    parser.add_argument("--slug", help="Tool slug to generate Schema for (e.g. 'jasper-ai')")
    parser.add_argument("--inject", action="store_true", help="Inject Schema info (prints instructions)")
    parser.add_argument("--all", action="store_true", help="Generate Schema for all tools")
    args = parser.parse_args()

    if args.all:
        data = load_tool_params()
        for t in data["tools"]:
            print(f"=== {t['name']} ===")
            print(generate_review_schema(
                tool_name=t["name"],
                rating=t["rating"],
                price_monthly=t["price_monthly"],
                date_published=t.get("datePublished", "2026-06-25"),
                pros=t["pros"],
                cons=t["cons"],
                description=t.get("description", ""),
                url=t.get("affiliateLink", ""),
            ))
            print()
        return

    if args.slug:
        tool = find_tool(args.slug)
    else:
        tool = find_tool("jasper-ai")

    if not tool:
        print(f"Tool not found: {args.slug or 'jasper-ai'}")
        sys.exit(1)

    name = tool.get("name") or tool.get("title", "").split(" Review")[0]
    rating = float(tool.get("rating", 4.0))
    price = tool.get("price_monthly") or float(tool.get("price", "$0").replace("$", "").split("/")[0])
    pros = tool.get("pros", [])
    cons = tool.get("cons", [])

    print("=== Review + Product Schema ===")
    print(generate_review_schema(
        tool_name=name,
        rating=rating,
        price_monthly=price,
        date_published=tool.get("datePublished", "2026-06-25"),
        pros=pros,
        cons=cons,
        description=tool.get("description", ""),
        url=tool.get("affiliateLink", ""),
    ))

    print("\n=== Software Schema ===")
    print(generate_software_schema(tool))

    print("\n=== Page + Breadcrumb Schema ===")
    print(generate_page_schema(tool))

    faqs = generate_faq_for_tool(tool)
    print("\n=== FAQ Schema ===")
    print(generate_faq_schema(faqs))

    print(f"\n=== Combined (all schemas merged) ===")
    all_schemas = "\n".join([
        generate_review_schema(name, rating, price, pros=pros, cons=cons,
                               date_published=tool.get("datePublished", "2026-06-25"),
                               description=tool.get("description", ""),
                               url=tool.get("affiliateLink", "")),
        generate_faq_schema(faqs),
    ])
    print(all_schemas)

    print(f"\n=== Instructions ===")
    print(f"Copy the 'Combined' section above and inject it into the page <head>.")
    print(f"Or modify src/app/[slug]/page.js to auto-generate Schema from reviews.json data.")


if __name__ == "__main__":
    main()
