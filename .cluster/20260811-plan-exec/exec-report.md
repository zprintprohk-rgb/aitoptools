# GEO+SEO 战略升级执行报告（2026-08-11 · Agent 集群模式）

> 依据: `20260811-042320-e6a260d3/aitoptools-GEO与SEO战略升级与Agent集群执行规划.md`（71 来源）
> 执行方式: 主线编排 + 2 路独立 Agent（数字口径核验 / 落地冲突审查）+ 构建验证

## 一、已执行落地（系统侧，可验证）

| # | 动作 | 证据 |
|---|---|---|
| 1 | **作者实体页** `/author/jerome-tang/`：Person schema（worksFor/knowsAbout/jobTitle）+ 资历 + 最新文章列表 | out 产物 35,653B，`"@type":"Person"` + worksFor 验证 True |
| 2 | **blog Last updated 可见展示**：meta-bar 显示 dateModified（原仅 schema 层） | out/blog/*/index.html 含 "Last updated"（build 重跑后） |
| 3 | **byline 链接作者页**：blog "Reviewed by Jerome Tang" 可点击 | out 产物 `/author/jerome-tang/` 链接 True |
| 4 | 执行工作台 `.cluster/20260811-plan-exec/`：exec-pack（里程碑修订/行动卡/集群映射）+ 2 份核验报告 | 3 文件落盘 |
| 5 | 构建验证 | exit 0，200 文件 775 aff-link |

## 二、核验发现（规划数据修正，重要）

### 数字口径（verify-math）
- ✅ 反推公式三处一致（$500→38.5笔/1,283点击/12,830访问；$27→18.5/617/6,170；4%→463）
- ❌ **M4-M6 里程碑表不自洽**：点击列隐含 11% 点击率（表写 385/550/715，10% 应为 350/500/650）→ 若按 10% 修正，六个月累计 $1,692 → **$1,554**，$3,000 缺口扩至 $1,446
- ⚠️ **$27 平均佣金是假设非计算值**：隐含平均客单价 ≈$100，且加权文本漏列 Claid（20%）

### 联盟条款（verify-math，对照 8/10 我方官方页实证）
| 差异 | 规划 | 实证 | 影响 |
|---|---|---|---|
| Jasper 申请状态 | "立即提交" | **Program Currently Closed** | W1 行动项暂不可执行，第一梯队标注暂不可得 |
| Jasper cookie | 30 天 | 14 天（官方页） | 转化窗口高估 |
| Synthesia 佣金 | 12 个月（疑似循环） | **非循环仅首购** | 双杠杆模型需计为一次性 |
| Runway | 表 2 遗漏 | $15 固定已实证 | 口径不完整 |
| Caspa 20% | 引用 affiliate.caspa.ai | 未经实证（待申请确认） | 降级未证实 |

### 落地冲突（verify-conflict）
- ❌ **页码失真**：规划称 143 页/94 工具，实测 **341 URL / 107 评测 / 199 programmatic 页**——集群重组实际波及 344+ 页
- ❌ **Organization schema 缺口不属实**：layout.js 全局已有 Organization——无需重复建设
- ✅ 属实项：Person 落地页缺失、dateModified 不可见（工具页更严重，连 datePublished 都无）、CF beacon 未装、llms.txt 已部署
- 冲突 8 条 + 遗漏 10 条（详见工作台 verify-conflict.md）

## 三、交付行动卡（需用户执行，系统不代做）

| 卡 | 动作 | 耗时 | 说明 |
|---|---|---|---|
| A1 | **安装 CF Web Analytics beacon**（Cloudflare 后台 → Analytics → 复制脚本 → 告知 AutoClaw 植入 layout.js） | 5min | D3 解锁 GEO 数据盲区；T+30 校准前提 |
| A2 | **GSC OAuth 配置**（Service Account JSON → .hermes/secrets/gsc-oauth.json） | 10min | D2 数据自动化 |
| A3 | **Synthesia 联盟申请**（synthesia.io/partners/affiliates：25% 首购/60 天） | 5min | 唯一当前可提交的高佣金申请（Jasper 已关闭） |
| A4 | **Jasper 申请监控**（程序重开即提交；当前关闭） | — | 25% 循环最高价值，重开窗口监控 |

## 四、下一步建议（规划修正后）

1. W1 剩余：集群枢纽页已现成（4 listicles 就是集群 A 枢纽）→ 增量 = 枢纽页辐条交叉链（blog-links 仅覆盖 blog→工具页单向）
2. W2：工具页 datePublished/dateModified 可见展示（比 blog 缺口更大）
3. T+30（9/10）校准须用真实佣金/AOV 替换 $27 假设，并排除 Jasper（若未重开）
4. 里程碑表修正版（按 10% 点击率 + $1,554 累计）已记入工作台 exec-pack.md

## 交付物

- [GEO+SEO 执行工作台](F:\aitoptools\.cluster\20260811-plan-exec\exec-pack.md) — 里程碑修订/行动卡/集群映射 + 2 份核验报告（verify-math.md / verify-conflict.md）
- [作者实体页代码](F:\aitoptools\src\app\author\jerome-tang\page.js) — Person schema 落地页（commit `f91c6ce`）
- 构建产物验证：out/author/jerome-tang/index.html（Person schema True）
