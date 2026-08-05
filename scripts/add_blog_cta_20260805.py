# -*- coding: utf-8 -*-
"""8/5: 给 blog-posts.json 的 3 篇文章补充 affiliateUrl + CTA 字段 (联盟链接从 affiliates.json SSoT 读取)"""
import json, io, sys

BASE = r"F:\aitoptools"
posts_path = BASE + r"\src\data\blog-posts.json"
aff_path = BASE + r"\src\data\affiliates.json"

with io.open(posts_path, encoding="utf-8") as f:
    posts = json.load(f)
with io.open(aff_path, encoding="utf-8") as f:
    aff = json.load(f)

map_slug = {
    "printful-vs-printify-2026": ("printful", "printify"),
    "how-to-use-ai-for-print-design": ("printify",),
    "ai-packaging-design-tools-2026": ("printify",),
}

for post in posts:
    s = post["slug"]
    tools = map_slug.get(s, ("printify",))
    main = tools[0]
    post["affiliateUrl"] = aff[main]["affiliate_url"]
    post["ctaText"] = "Try " + aff[main]["name"] + " Free"
    if len(tools) > 1:
        post["secondaryAffiliateUrl"] = aff[tools[1]]["affiliate_url"]
        post["secondaryCtaText"] = "Try " + aff[tools[1]]["name"] + " Free"

with io.open(posts_path, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print("updated", len(posts), "posts")
for x in posts:
    print(x["slug"], "->", (x.get("affiliateUrl") or "")[:45], "|", (x.get("secondaryAffiliateUrl") or "")[:45])
