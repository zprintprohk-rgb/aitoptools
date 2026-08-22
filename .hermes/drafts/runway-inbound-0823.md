# runway-ml-review 入链方案 (STRATEGY-2026-08-23 T3 · 只备不部署)

> 背景: #2 runway Branch C 启动 — 站内入链 = 0 (孤儿页, 8/22 全量 src/data 核查); 主词 runway ml review NODATA x4 连续窗口; 页级 28 imp @70.86 持平
> 状态: **本方案为草稿, 不部署** (T1 判定 Branch B → 攒入下批内容 push 窗口; 仅 Branch C 触发才随紧急修复单独部署)

## 主插入点 (精确)

| 宿主页 | 位置 | 现状 | 动作 |
|---|---|---|---|
| /pika-labs-review/ | Verdict 段尾 | 纯文本: For professional-quality, use Runway ML. | 加链: use Runway ML (锚文本变体, 禁完全匹配 runway ml review) |

## 次级插入点 (执行时定位, 上下文自然)

| 宿主页 | 语境 | 锚文本建议 | 备注 |
|---|---|---|---|
| /midjourney-review/ | AI 视频延伸段落 (执行时找 text-to-video 相关句) | Runway AI video generator / Runway ML | content 5,754 字符, 有扩展空间 |
| /heygen-review/ | 数字人/AI 视频工具对比语境 | Runway ML | content 1,098 字符, 仅在自然对比处插入, 不硬塞 |

## 规则
- 锚文本变体: Runway ML / Runway AI video generator / compared to Runway ML — 禁完全匹配词
- 每页 1 条, 不堆砌; 插入处上下文必须真实相关 (AI 视频/生成工具对比)
- 部署时: reviews.json 改动 -> build PASS -> IndexNow 推 /runway-ml-review/ + 宿主页 -> 合并 push
- 时间窗: 8/24 T+7 观察窗内完成 (与下批内容合并); 若 8/23-24 主词出现回填数据, 按数据再评估

## 幂等键: 本文件存在 -> T3 完成 (草稿态)