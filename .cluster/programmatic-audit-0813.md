# T13 记分卡正式版（2026-08-12 全量，口径 v1.1）

> 333 programmatic 页 = best 199 + reviews 107 + comparisons 6 + listicles 4 + blog 10 + category 6
> 标准: A≥5 / B=3-4 / C≤2（六项: title 含目标词 / H1 / 正文≥800 词 / 内链≥2 / schema/FAQ / CTA）

## 汇总
| 组 | 数 | A | B | C |
|---|---|---|---|---|
| best | 199 | 149 | 50 | 0 |
| review | 107 | 5 | 88 | 14 |
| comparison | 6 | 6 | 0 | 0 |
| listicle | 4 | 4 | 0 | 0 |
| tool | 9 | 7 | 0 | 2 |
| blog | 10 | 10 | 0 | 0 |
| category | 6 | 6 | 0 | 0 |

**合计: 341 页 | A=187 | B=138 | C=16**

## C 级 14 页（8/16 快修最高优先）
- `bluehost-review-2026`
- `dalle-review`
- `fliki-ai-review-2026`
- `gear-launch-review-2026`
- `gorgias-ai-review-2026`
- `grammarly-business-review-2026`
- `greenonion`
- `packify-ai-review`
- `pebblely-review-2026`
- `picjam`
- `playht-review-2026`
- `reconvert-upsell-review-2026`
- `removebg-review`
- `squarespace-ai-review-2026`
- `topaz-photo-ai-review-2026`
- `wix-ai-review-2026`

## B 级内容最短 20 页（正文扩写队列）
- `postermywall-review` — 75 词
- `hostinger-review` — 78 词
- `perplexity-pro-review` — 86 词
- `notion-ai-review` — 89 词
- `claid-ai-review` — 90 词
- `midjourney-review` — 92 词
- `logoai-review` — 93 词
- `gamma-ai-review` — 95 词
- `rytr-review` — 97 词
- `elevenlabs-review` — 100 词
- `suno-ai-review` — 101 词
- `descript-review` — 102 词
- `synthesia-review` — 104 词
- `pika-labs-review` — 104 词
- `looka-review` — 104 词
- `vistacreate-review` — 104 词
- `cursor-review` — 108 词
- `zmo-ai-review` — 109 词
- `leonardo-ai-review` — 110 词
- `best-ai-writing-tools-comparison` — 114 词

## 口径修正记录（v0→v1.1，依据 scorecard-sample-audit-0812.md）
1. listicle 词数用 introContent+closingContent+items 全文（v0 wc=0 假象 → 4 页 B→A）
2. comparison 的 affiliateUrl 嵌套在 toolA/toolB（via=/fpr=/pxf.io）→ 6 页 aff 补判
3. affiliateUrl="#" 占位符视为无 CTA（-2026 批 10 页 B→C 真实状态）
4. keyword 标点变体宽容匹配（DALL-E 3 / Remove.bg）
5. best 199 页按生成 HTML 产物检查（非数据源代理）

## 数据文件
- .cluster/programmatic-audit-0813.json（v1.1 数据源 142 页）
- .cluster/best-pages-audit-0812.json（best 199 页）
- .cluster/programmatic-audit-0813-summary.json（合并汇总）
- .cluster/programmatic-audit-0813.html（可视化报告）
- .cluster/scorecard-sample-audit-0812.md（抽样核验报告）
