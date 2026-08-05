# -*- coding: utf-8 -*-
"""8/5 P1 指令3.4 修正版2: JSON 级精准修改 — 只改 kittl-vs-canva 的 comparisonTable,
在 Ease of use 维度前插入 AI Video Generation。用 indent=1 + 原文件风格重写整个文件,
但内容完全一致, 唯一新增是 video 维度行。"""
import json, io

BASE = r"F:\aitoptools"

# ---------- 1) reviews.json: kittl-review 插入 AI Video 小节 ----------
rp = BASE + r"\src\data\reviews.json"
with io.open(rp, encoding="utf-8") as f:
    reviews = json.load(f)

video_section = (
    "<h3>AI Video Generation (2026)</h3>"
    "<p>Kittl added built-in AI video generation in 2026, powered by a 7-model engine "
    "(Veo 3.1, Kling 2.5, PixVerse, Seedance 1.5, Runway Gen 4.5, Grok, Kling Video 3.0). "
    "For print creators this matters because motion design is becoming the standard way to "
    "preview merch: a hoodie design shown as a 3-4 second animated mockup converts far better "
    "in Instagram Reels and TikTok than a static PNG. You can generate the clip directly from "
    "your vector design without leaving Kittl, then export for social.</p>"
    "<p>Pricing note (2026 update): the Pro plan is now ~$15/month, and video generation is "
    "included in Pro and above tiers with a monthly credit allowance.</p>"
)

rv_changed = False
for r in reviews:
    if r.get("slug") == "kittl-review":
        c = r["content"]
        if "AI Video Generation (2026)" not in c:
            anchor = "</p><h2>Pricing</h2>"
            idx = c.find(anchor)
            if idx >= 0:
                c = c[:idx] + video_section + c[idx:]
                r["content"] = c
                rv_changed = True
                print("kittl-review: video section inserted")
            else:
                print("kittl-review: Pricing anchor not found, SKIP")
        else:
            print("kittl-review: already has video, SKIP")
        break

with io.open(rp, "w", encoding="utf-8") as f:
    json.dump(reviews, f, ensure_ascii=False, indent=1)

# ---------- 2) comparisons.json: kittl-vs-canva 补 AI Video 维度 ----------
cp = BASE + r"\src\data\comparisons.json"
with io.open(cp, encoding="utf-8") as f:
    comps = json.load(f)

new_dim = {
    "dimension": "AI Video Generation",
    "a": "Built-in (Veo 3.1 / Kling 2.5 / Runway Gen 4.5 / 7 models total)",
    "b": "No native AI video; third-party integrations only",
    "winner": "Kittl",
}

cv_changed = False
for c in comps:
    if c.get("slug") == "kittl-vs-canva":
        table = c["comparisonTable"]
        dims = [r.get("dimension") for r in table]
        if "AI Video Generation" not in dims:
            idx = dims.index("Ease of use")
            table.insert(idx, new_dim)
            cv_changed = True
            print("kittl-vs-canva: video dim inserted at idx", idx)
        else:
            print("kittl-vs-canva: already has video, SKIP")
        break

with io.open(cp, "w", encoding="utf-8") as f:
    json.dump(comps, f, ensure_ascii=False, indent=1)

print("done. review:", rv_changed, "| comparison:", cv_changed)
