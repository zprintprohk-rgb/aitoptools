# 执行落地包 — GEO+SEO 战略升级 (2026-08-11, 依据 20260811 规划)

> 规划来源: aitoptools-GEO与SEO战略升级与Agent集群执行规划.md（71 来源交叉验证）

## 一、里程碑修订（M1-M6, 双杠杆模型）

| 月份 | 月访问 | 月联盟点击 | 平均佣金 | 转化率 | 月收入推算 | 备注 |
|---|---|---|---|---|---|---|
| M1 | 300 | 30 | $15 | 2% | 约 $9 | 8/11-9/10（校准前） |
| M2 | 900 | 90 | $18 | 2.5% | 约 $40 | |
| M3 | 2,000 | 200 | $22 | 3% | 约 $132 | 9/10 T+30 全量校准点 |
| M4 | 3,500 | 350 | $25 | 3% | 约 $263 | Shopify $150 申请后 |
| M5 | 5,000 | 500 | $27 | 3.5% | 约 $473 | |
| M6 | 6,500 | 650 | $28 | 3.5% | 约 $637 | 目标月 $800 |

- 6 个月累计约 $1,554（v1.1 按 10% 点击口径修正）；缺口约 $1,446 由高额一次性佣金填补：Placeit / Shopify $150（M3 后申请）/ Printify 博客挑战赛 $150（9/29 截止）/ Kittl Expert $72/单
- 校准点：T+7（8/14 首读数）+ T+30（**9/13**，以 T+7 起算 30 天，全量替换占位参数）——均以 D2 GSC OAuth + D3 CF beacon 为前提
- 双杠杆核心：平均佣金 $13→$27（第一梯队 Mockey 30%/CF 25%/Claid 20%/Jasper 25-30% 加权），流量需求减半

## 二、用户行动卡（对外动作，系统不代做）

| 卡号 | 动作 | 耗时 | 解锁 | 截止 |
|---|---|---|---|---|
| A1 | 安装 CF Web Analytics beacon（Cloudflare 后台 → 站点 → Analytics → 复制脚本 → 通知 AutoClaw 植入 layout.js） | 5min | GEO 数据盲区（D3） | 8/12（T+30 校准前提） |
| A2 | 配置 GSC OAuth（Google Cloud Console → Search Console API → Service Account JSON → .hermes/secrets/gsc-oauth.json） | 10min | 数据自动化（D2） | 8/12 |
| A3 | 提交 Synthesia 联盟申请（synthesia.io/partners/affiliates：25% 首购一次性/60 天 cookie，Rewardful 平台） | 5min | 当前唯一可提交的高佣金申请 | 8/15 窗口 |
| A4 | Jasper 重开监控（程序当前关闭，系统每日只读检查状态页，重开即交 user 提交） | — | 最高价值引擎（25% 循环/14 天 cookie） | 持续 |
| A5 | Impact 登录（可选）→ 复查 Kittl 审核 + Placeit 申请 | 2min | Kittl/Placeit 渠道 | 8/14 |

## 三、主题集群映射表（W2 内链重组依据）

| 集群 | 枢纽页（复用现有） | 辐条页 | 目标关键词 |
|---|---|---|---|
| A POD 平台选型 | /best/printful-alternatives/ + /best/print-on-demand-companies/ | printful-review / printify-review / gelato-review + 两两对比页 | printful alternatives 45imp/74.9 |
| B AI 设计工具 | /best/best-ai-tshirt-design-generators/ | kittl-review / creative-fabrica-review / claid-review / caspa-review（M3 横评后） | ai tshirt design |
| C Mockup 产品摄影 | /best/ 新增或 /compare/（M3 横评 A 发布后挂入） | mockey-review / placeit-review / omi-review（M3） | product photography |
| D 运营长尾 | 4 个枢纽页交叉挂载 | 全部 blog（blog-links.mjs 自动内链） | how-to / best-for |

- 内链机制：blog-links.mjs 自动（blog→工具页）；增量工作 = 枢纽页内指向辐条的工具名（构建期自动注入）+ 辐条页"相关工具"区交叉链（[slug] 页已有同分类 review-grid，需扩展跨集群）
- 注意：集群 B 的 caspa-review / cluster C 的 omi-review 依赖 M3 横评产出（8/12-16 排期）

## 四、E-E-A-T 补强执行记录

| 项 | 规划缺口 | 现状核实 | 动作 |
|---|---|---|---|
| 作者实体页 | byline 无 Person schema 落地页 | 属实（blog Article 有 Person 但无落地页） | 本轮新增 /author/jerome-tang/ 页 + Person schema |
| 最后更新时间可见 | dateModified 不可见 | 属实（blog 页仅显示 datePublished） | 本轮 blog 页加 Last updated 可见行 |
| Organization schema | 规划称缺失 | **已存在**（layout.js，冲突审查确认） | 无需动作（规划误判，已记录） |
| 实测证据档案 | tool-screenshots 无证据页 | 待核（tool-screenshots 目录存在性待确认） | W2 评估证据页 |
