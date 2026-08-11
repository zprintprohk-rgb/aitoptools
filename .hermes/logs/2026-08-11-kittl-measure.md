# Kittl 联盟实测日 — 2026-08-11（8/5 预排一次性触发）

**角色**: Hermes 日执行员 | **北极星**: $3000/6月 | **约束**: 只读分析, 无部署
**Kittl 状态**: Impact 平台已获批 (7/30), 20% 首年, pxf 链接 https://kittl.pxf.io/qWNvPn

## 一、实测源文件（Step 0 · CF 免费素材）
素材池: 8/6-8/11 累计 26 个万圣节素材 (去重 25, 远超辐条① 3 个门槛)

| 优先级 | 素材 | 来源 | 类型 |
|---|---|---|---|
| 首选 | Fall Halloween Sublimation Bundle | 8/9 CF 免费清单 | 升华烫画素材包 (POD 强相关) |
| 备选1 | Grandparents Grandma Grandpa Sublimation | 8/11 CF 免费清单 | 升华烫画 (今日新增) |
| 备选2 | Halloween Black Cat Embroidery Design | 8/10 CF 免费清单 | 刺绣设计 |

实测场景建议: Kittl 内用首选素材做 1 件万圣节 T 恤设计 (Kittl 自带模板排版), 输出 PNG 留作 8/17 辐条①素材 + 测试订单照片墙 6 图之一。

## 二、Impact 数据（Step 1）
- 自动登录 app.impact.com 禁止 (AGENTS.md §7) → 未拉取
- 磁盘核查 .hermes/logs/ + affiliate-programs.json: **无 user 提供的 Kittl 点击数据** (截至 8/11 12:2x)

### 手工查询指引（给 user, 约 5 分钟）
1. 打开 https://app.impact.com → 登录 (Impact 专用副邮箱, 凭证在 .hermes/secrets/affiliate-credentials.md §7)
2. 顶部 Reports → 选 Kittl 项目 → 日期范围 2026-08-01 至 08-11
3. 维度选 utm_content / link_id 拆分 clicks / conversions / commission
4. 按链接核对 (link_id 命名 = {slug}-{位置}, 度量新规 2026-07-28):

| link_id | 位置 | 页面 |
|---|---|---|
| kittl-review-card-cta | 首页 review 卡 CTA (垂直区+全量网格共 2 处) | 首页 |
| kittl-review-detail-cta | 详情页 CTA | /kittl-review/ |
| kittl-vs-canva-verdict-cta-a | 对比页胜方 CTA | /compare/kittl-vs-canva/ |
| kittl-vs-placeit-verdict-cta-a | 对比页胜方 CTA | /compare/kittl-vs-placeit/ |

## 三、判定结论（Step 2）
**数据缺失 → 默认「维持现状, 观察 1 周」**（判定线暂缓, 等 user 回填 Impact 数据）

判定线 (待数据):
- 平均 ≥5 点击/天 → 加投: 首页 CTA 位置 + 1-2 个高流量页嵌入
- 1-5 点击/天 → 维持现状, 观察 1 周
- <1 点击/天 → 撤首页 2 个 pxf, 换 Claid/Mockey 测试位

下一数据点: user 提供 Impact 数字后重判 (可在 8/14 周报前回填)。

## 四、CTR 榜 v0（Step 3）
见 .hermes/logs/2026-08-11-ctr-ranking-v0.md — GA4 凭证缺失, 榜单延迟。

## 五、下轮动作建议（Step 4）
1. user 手工查 Impact 一次 (指引见上), 数字回填后我出加投/撤位终判
2. GA4 API 凭证配好后, 下轮拉 affiliate_click × page_view 出 CTR 榜 v0 (W4-T1 基线)
3. 8/17 辐条①用首选素材产万圣节实测设计 (与本次源文件同一素材)
