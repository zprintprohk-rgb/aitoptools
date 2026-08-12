# C 级 16 页修复状态登记（2026-08-12/13）

> 依据: T13 记分卡正式版（v1.1）C 级清单。原则：**无真实 affiliate URL 来源不编造 URL**（诚实登记原则）。
> 相关台账: `.cluster/programmatic-audit-0813.md` / `-full.json`

## 分类处置

| 组 | 页数 | 页 | 处置 |
|---|---|---|---|
| A. affiliateUrl="#" 占位符（-2026 批） | 10 | playht-review-2026 / topaz-photo-ai-review-2026 / pebblely-review-2026 / gorgias-ai-review-2026 / wix-ai-review-2026 / grammarly-business-review-2026 / fliki-ai-review-2026 / squarespace-ai-review-2026 / bluehost-review-2026 / reconvert-upsell-review-2026 | ⏳ **待真实 URL**：affiliates.json（9 工具 SSoT）与 affiliate-programs.json（18 程序）均无这些工具的个人 affiliate URL 记录 → 不编造。修复路径：各工具官方联盟后台申请获批后回填（8/16 快修时复查，若仍无来源则保持"观察不动"） |
| B. 内容真实短板 | 2 | gear-launch-review-2026（wc=472, score=1）/ packify-ai-review（wc=754, score=2） | 🔧 8/16 快修：正文扩写 ≥800 词 + 补 FAQ schema（内容工作，不需要外部 URL） |
| C. keyword 标点变体 | 2 | dalle-review（DALL-E 3）/ removebg-review（Remove.bg） | ℹ️ 记分卡口径误判为主（v1.1 已宽容匹配）；removebg wc=114 真实偏短 → 8/16 一并扩写 |
| D. affiliate pending | 2 | greenonion / picjam | ⏸️ 保持（pending 是真实状态，文档已声明；无 CTA 不造假） |

## 行动项归属
- 8/16 B 类快修 cron 追加：组 B（gear-launch + packify 扩写）+ 组 C（removebg 扩写）
- 组 A 不编造 URL，8/16 复查联盟后台；无来源则记"观察不动"
- 组 D 等待 Impact/PartnerStack 审批（无时间承诺）

## 备注
- 本轮（8/12-8/13）已同步完成 T11/T14 内链 Boost（见 SPRINT-LEDGER），C 级中除组 A/D 外不阻塞任何页面线上表现（C 级页面本就不承担主流量）。
