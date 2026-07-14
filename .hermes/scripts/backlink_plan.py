"""Generate backlink promotion plan for today's 10 tools"""
import json
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_dir = "/mnt/f/aitoptools/.hermes/logs"
tools = json.load(open(f"{log_dir}/{today}-新工具入库.json"))

promos = {
    "leonardo-ai-review": {
        "platforms": "Reddit r/StableDiffusion, r/printondemand, Quora",
        "keywords": "AI image generator POD, best AI for product mockups, Leonardo AI print quality",
        "quora": "What is the best AI image generator for print-on-demand product mockups in 2026?",
        "reddit": "r/printondemand: What tools do you use for product mockups? - Recommend Leonardo for batch generation of POD mockups with consistent branding"
    },
    "runway-gen3-review": {
        "platforms": "Reddit r/videography, r/printondemand, HN",
        "keywords": "AI video for small business, print shop video ads, Runway Gen-3",
        "quora": "How can print shops create professional video ads without a production team?",
        "reddit": "r/videography: Best AI tools for creating product demo videos? - Runway Gen-3 is great for print business showcases"
    },
    "elevenlabs-review": {
        "platforms": "Reddit r/voiceover, r/smallbusiness, Quora",
        "keywords": "AI voiceover for ads, best text to speech for business, ElevenLabs review",
        "quora": "What is the most realistic AI voice generator for commercial use?",
        "reddit": "r/smallbusiness: What tools help you scale content creation? - ElevenLabs for professional video voiceovers"
    },
    "heygen-review": {
        "platforms": "Reddit r/marketing, r/Entrepreneur, Quora",
        "keywords": "AI avatar for marketing, HeyGen vs Synthesia, video marketing AI",
        "quora": "Do AI avatar videos actually work for marketing?",
        "reddit": "r/marketing: Any experience with AI avatar video tools? - HeyGen works well for product marketing"
    },
    "jasper-ai-review": {
        "platforms": "Reddit r/copywriting, r/printondemand, Quora, HN",
        "keywords": "AI copywriting for e-commerce, Jasper vs Copy.ai, product description AI",
        "quora": "Is Jasper AI worth it for e-commerce product descriptions?",
        "reddit": "r/copywriting: Best AI tools for product descriptions? - Jasper handles bulk descriptions well for POD"
    },
    "copy-ai-review": {
        "platforms": "Reddit r/Entrepreneur, r/smallbusiness, Quora",
        "keywords": "free AI writing tool, Copy.ai review, best AI for social media",
        "quora": "What is the best free AI writing tool for small businesses?",
        "reddit": "r/Entrepreneur: Best free tools for creating marketing content? - Copy.ai free tier is generous"
    },
    "typeface-ai-review": {
        "platforms": "LinkedIn, HN, Reddit r/marketing",
        "keywords": "enterprise AI content, brand content platform, Typeface AI",
        "quora": "How do large print companies scale content production with AI?",
        "reddit": "r/marketing: Enterprise AI content tools? - Typeface is purpose-built for brand governance"
    },
    "frase-io-review": {
        "platforms": "Reddit r/SEO, r/bigseo, Quora, HN",
        "keywords": "SEO content AI, Frase.io review, best SEO writing tool",
        "quora": "What is the best AI tool for SEO content writing?",
        "reddit": "r/SEO: Best AI tools for content optimization? - Frase.io SERP-driven approach works well"
    },
    "writesonic-review": {
        "platforms": "Reddit r/blogging, r/SEO, Quora",
        "keywords": "Writesonic vs Jasper, affordable AI writing, best AI blog writer",
        "quora": "What is the most affordable AI writing tool with good quality?",
        "reddit": "r/blogging: Best AI writing tool on a budget? - Writesonic free plan offers 10K words/month"
    },
    "canva-print-review": {
        "platforms": "Reddit r/graphic_design, r/smallbusiness, r/printondemand, Quora",
        "keywords": "Canva Print review, AI print design, Canva vs Vistaprint",
        "quora": "Canva Print vs Vistaprint: Which is better for small business print needs?",
        "reddit": "r/printondemand: Canva Print for POD? - Design with Canva AI tools, print directly, great for small runs"
    }
}

report = f"""# 外链推广方案 - {today}

## 今日新工具推广策略
"""

for t in tools:
    s = t["slug"]
    n = t["name"]
    d = promos.get(s, {})
    if not d:
        continue
    
    report += f"""
---

### {n}
**目标平台**: {d['platforms']}
**关键词**: {d['keywords']}

**软植入策略**:
- **Quora**: "{d['quora']}"
  -> 在回答中自然推荐{n}，突出其对打印/印刷/电商的实际价值，附aitoptools.net评测链接。

- **Reddit**: {d['reddit']}
  -> 以第一人称分享使用体验，不直接发链接，引导有兴趣的用户访问你的个人资料或后续回复。

"""

report += f"""
## 通用策略

### 注意事项
- 不发纯链接，提供真实价值
- 每个平台每天不超过2-3条，避免刷屏
- 优先回复24小时内的热门问题
- 使用自然语言，不复制粘贴
- 在Reddit使用第一人称个人体验口吻

### Quora 目标问题
1. "What are the best AI tools for print-on-demand businesses in 2026?"
2. "How can AI help small print shops compete online?"
3. "What AI tools does every POD seller need?"
4. "Best free AI tools for e-commerce product descriptions?"
5. "How to create video marketing for a print business without experience?"

### Reddit 目标子版块
- r/printondemand — 核心
- r/smallbusiness — 通用
- r/Entrepreneur — 创业者
- r/SEO — SEO优化
- r/graphic_design — 设计社区
- r/marketing — 营销

### HackerNews
关注 ShowHN 中 AI工具、印刷科技、电商相关帖子，在评论中提供真实使用体验。
"""

with open(f"{log_dir}/{today}-外链推广.md", "w") as f:
    f.write(report)
print(f"Backlink plan saved to {today}-外链推广.md")
