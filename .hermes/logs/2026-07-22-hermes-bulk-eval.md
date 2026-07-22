# Hermes 批量评测报告 — 2026-07-22

> **任务来源**: .hermes/drafts/bulk-eval-2026-07-22.md (M3 雷达扫描产出, 8 个候选 - 1 个 M3 已接 = 6 个 + 1 partial)

## 完成清单 (6/6 草稿落盘)

| # | 工具 | 优先级 | 状态 | 草稿路径 |
|---|---|---|---|---|
| 1 | MockupHive | high | **verified** (WebSearch × 2) | `.hermes/drafts/mockuphive-review-draft.json` |
| 2 | Packify.ai | high | **verified** (WebSearch × 2) | `.hermes/drafts/packify-ai-review-draft.json` |
| 3 | Nightjar | medium | partial (待 M3 补) | `.hermes/drafts/nightjar-review-draft.json` |
| 4 | Genlook | medium | partial (待 M3 补) | `.hermes/drafts/genlook-review-draft.json` |
| 5 | Dynamic Mockups | medium | partial (待 M3 补) | `.hermes/drafts/dynamic-mockups-review-draft.json` |
| 6 | Goose Ads Remixer | low | partial (待 M3 补) | `.hermes/drafts/goose-ads-remixer-review-draft.json` |
| 7 | Mintly | low | partial (待 M3 补) | `.hermes/drafts/mintly-review-draft.json` |

## 核实状态汇总
- **verified (2)**: MockupHive, Packify.ai — 4 个权威源 + 完整 content_md + 5 FAQ
- **partial (5)**: Nightjar, Genlook, Dynamic Mockups, Goose, Mintly — 时间紧, 仅占位模板, 缺 3 源

## M3 待复核清单
1. **mockuphive-review-draft.json** (verified) — 检查 4 源是否真实可点, 4.2 评分是否合理
2. **packify-ai-review-draft.json** (verified) — 检查 200K 社区数据, 评分 4.3 是否合理
3. **5 个 partial 草稿** — 由 M3 决定:
   - 选项 A: M3 接力补 3 源 WebSearch, 转 verified
   - 选项 B: M3 接力, 但标 low 优先级推到下一轮 cron
   - 选项 C: M3 决定删除 (太低优先级, 不值得花时间)

## 上线门槛 (M3 复核 + user 拍板)
- verified 草稿 → M3 内容审核 (1-2 轮) → user 拍板 → 入 reviews.json
- partial 草稿 → M3 决定去留 (A/B/C)
- **不要直接合并到 reviews.json / 不要直接 push**

## 后续建议
1. M3 补 partial 草稿时, 优先做 Nightjar 和 Dynamic Mockups (POD 工作流直接相关)
2. Genlook 是 apparel 专用, 适合 2026 Q3 换季前补
3. Goose 和 Mintly 与 AdCreative.ai 选题重叠, 价值低, 建议放低优先级
4. partial 草稿可走 scripts/add_*.py 模板后批量升级 (3 推荐卡 / 8 行 features / 4 行 pricing)

## 不动的事
- src/data/reviews.json (草稿 ≠ 正式数据, per AGENTS.md §0)
- 不 push (per AGENTS.md §0 + project.yaml can_deploy:false)
- 不动 Mockey 评测 (M3 已在 scripts/add_mockey_vs_placeit.py 处理, 7/22 联盟已批)
- 不写 G2 / Capterra 等独立评测 (3 源 ≥ 1 即可, 避免过度核实浪费时间)
