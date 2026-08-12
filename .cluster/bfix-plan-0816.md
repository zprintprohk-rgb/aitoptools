# B 类快修方案（8/16 预生成，2026-08-13）

> 来源: T13 记分卡正式版 B 类 88 个 review 页（A=5/B=88/C=14）· 自动化规则诊断 title/metaDesc
> 消费: 8/16 B 类快修 cron（e3145d3b）执行时优先按本方案修改，改后重跑记分卡验证

## 问题统计

| 问题 | 页数 |
|---|---|
| title title | 54 |
| meta meta | 77 |

## 修正规则

1. title 超长/偏短: 压缩至 50-60 字符，主关键词前置，品牌 ZprintPro 不用（aitoptools 无品牌词），结尾保留年份 2026
2. title 缺目标词: 将 slug 主词（如 postermywall → Postermywall）插入 title 前部
3. metaDesc 缺失/超长/偏短: 重写 150-160 字符，含数字（价格/评分/字数） + CTA 词（read/compare/free trial）
4. meta 无数字: 从 rating/price 字段取数嵌入
5. 改后: node scripts/check-i18n 无此脚本则 JSON 语法校验 + npm run build + 记分卡重跑

## 高优先 25 页（问题数最多）

| slug | title_len | meta_len | title 问题 | meta 问题 |
|---|---|---|---|---|
| redbubble-review | 72 | 114 | title 超长 72>65 | meta 偏短 114<120; meta 无数字锚点 |
| fiverr-logo-maker-review | 70 | 166 | title 超长 70>65 | meta 超长 166>165; meta 无数字锚点 |
| predis-ai-review | 77 | 169 | title 超长 77>65 | meta 超长 169>165; meta 无数字锚点 |
| munch-ai-review | 72 | 166 | title 超长 72>65 | meta 超长 166>165; meta 无数字锚点 |
| stickermule-review | 66 | 158 | title 超长 66>65; title 缺目标词 ['stickermule'] | meta 无数字锚点 |
| mailchimp-review | 76 | 133 | title 超长 76>65 | meta 无数字锚点; meta 缺 CTA 词 |
| sellhound-review-2026 | 78 | 169 | title 超长 78>65 | meta 超长 169>165; meta 缺 CTA 词 |
| elevenlabs-review | 68 | 143 | title 超长 68>65 | meta 无数字锚点 |
| suno-ai-review | 66 | 144 | title 超长 66>65 | meta 无数字锚点 |
| descript-review | 66 | 164 | title 超长 66>65 | meta 无数字锚点 |
| pika-labs-review | 69 | 162 | title 超长 69>65 | meta 无数字锚点 |
| best-ai-writing-tools-comparison | 76 | 174 | title 超长 76>65 | meta 超长 174>165 |
| photoroom-review | 71 | 180 | title 超长 71>65 | meta 超长 180>165 |
| adobe-firefly-review | 69 | 189 | title 超长 69>65 | meta 超长 189>165 |
| upscale-media-review | 66 | 170 | title 超长 66>65 | meta 超长 170>165 |
| murf-ai-review | 66 | 182 | title 超长 66>65 | meta 超长 182>165 |
| designpickle-review | 77 | 165 | title 超长 77>65 | meta 无数字锚点 |
| durable-ai-review | 82 | 149 | title 超长 82>65 | meta 无数字锚点 |
| capcut-ai-review | 76 | 148 | title 超长 76>65 | meta 无数字锚点 |
| looka-review | 64 | 94 | - | meta 偏短 94<120; meta 无数字锚点 |
| logoai-review | 60 | 93 | - | meta 偏短 93<120; meta 无数字锚点 |
| shopify-magic-review | 61 | 93 | - | meta 偏短 93<120; meta 无数字锚点 |
| pictory-review | 72 | 158 | title 超长 72>65 | meta 无数字锚点 |
| spocket-review | 68 | 159 | title 超长 68>65 | meta 无数字锚点 |
| klaviyo-review | 67 | 157 | title 超长 67>65 | meta 无数字锚点 |

## 其余 54 页（问题较轻，8/16 按序处理）

befunky-review, lucidchart-review, adcreative-ai-review, tidio-ai-review, manychat-ai-review, omnisend-review, sellerpic-review, revery-ai-review, depikt-ai-review, viralcraft-ai-review, printreadybook-review, persify-review, seede-ai-review-2026, vestia-ai-review-2026, sloap-review-2026, alttextgenerator-review-2026, namecheap-review, getresponse-review, activecampaign-review, zoho-review, heygen-review, copy-ai-review, leonardo-ai-review, claid-ai-review, synthesia-review, perplexity-pro-review, gamma-ai-review, canva-ai-review, placeit-review, pixlr-ai-review, claude-review, gemini-review, ai-image-upscaler-comparison, society6-review, b12-ai-review