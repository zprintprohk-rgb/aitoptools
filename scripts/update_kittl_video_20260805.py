# -*- coding: utf-8 -*-
"""8/5 P1 指令3.4 修正版: 文本级精准替换 — 只插入 video 片段, 其他字节完全不动 (避免 json.dump 全量重排)"""
import io

BASE = r"F:\aitoptools"

# ---------- 1) reviews.json: kittl-review 插入 AI Video 小节 ----------
rp = BASE + r"\src\data\reviews.json"
with io.open(rp, encoding="utf-8") as f:
    text = f.read()

anchor = "<p>Built-in vector editor with SVG export."
if anchor in text and "AI Video Generation (2026)" not in text:
    idx = text.find(anchor)
    end = text.find("</p>", idx) + len("</p>")
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
    text = text[:end] + video_section + text[end:]
    with io.open(rp, "w", encoding="utf-8") as f:
        f.write(text)
    print("reviews.json: video section inserted (text-level)")
else:
    print("reviews.json: skip (anchor missing or already has video)")

# ---------- 2) comparisons.json: kittl-vs-canva 补 AI Video 维度 ----------
cp = BASE + r"\src\data\comparisons.json"
with io.open(cp, encoding="utf-8") as f:
    ctext = f.read()

# 找 kittl-vs-canva 的 comparisonTable 中 "Ease of Use" 维度前插入
if "kittl-vs-canva" in ctext and '"dimension": "AI Video Generation"' not in ctext:
    # 定位 kittl-vs-canva 条目内的 Ease of Use 行 (它唯一出现在该条目的 comparisonTable)
    eou = ctext.find('"dimension": "Ease of use"')
    if eou >= 0:
        # 找到该行的结束 "}," 位置, 在其后插入新维度行 (保持 1-space indent 风格)
        line_end = ctext.find("\n", eou)
        # 向前找该行的起始 (从上一个 \n 之后)
        line_start = ctext.rfind("\n", 0, eou) + 1
        old_line = ctext[line_start:line_end]
        new_dim = (
            '  {\n'
            '   "dimension": "AI Video Generation",\n'
            '   "a": "Built-in (Veo 3.1 / Kling 2.5 / Runway Gen 4.5 / 7 models total)",\n'
            '   "b": "No native AI video; third-party integrations only",\n'
            '   "winner": "Kittl"\n'
            '  },\n'
        )
        ctext = ctext[:line_start] + new_dim + old_line + "\n" + ctext[line_end:]
        with io.open(cp, "w", encoding="utf-8") as f:
            f.write(ctext)
        print("comparisons.json: AI Video Generation row inserted before Ease of Use")
    else:
        print("comparisons.json: Ease of Use row not found, SKIP")
else:
    print("comparisons.json: skip (already has video or entry missing)")
