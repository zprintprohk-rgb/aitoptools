# Schema 覆盖审计（续）— 2026-08-29

> 触发: wake「继续」· 前序: schema-audit-2026-08-28.md（031b609 前的修复线）
> 数据来源: ① git status/log/show 实查 ② 线上 fetch 实测（aitoptools.net 3 页） ③ npm run build 实跑输出 ④ reviews.json 重扫描脚本

## 一、开工状态核查（04:56）

- 昨日 3 文件修复已被 57f6fa4（ops 0828 凌晨窗口）并入并 push，线上实测 nordvpn-review 页 authorUrl=true / imageObject=true → S6 主线已部署生效
- 工作区 2 个 M 文件（blog-posts.json 15477 行重写 / reviews.json 38 行）属并行会话在途改动，本次不碰不并
- reviews.json 重扫: text_bare=0 / url_bare=4 / 107 条 → 昨日 &amp; 修复完好未被覆盖

## 二、本次续做（S6 遗留项）

| 文件 | 改动 |
|---|---|
| src/app/about/page.js | 页面级 AboutPage JSON-LD：mainEntity=Organization(name/url/logo ImageObject/description) + founder=Person(Jerome Tang, url=/author/jerome-tang/)；组件包 <> fragment |
| src/app/methodology/page.js | 页面级 WebPage JSON-LD：author=Person(url 锚点) + publisher=Organization(name/url/logo) + dateModified=2026-07-27（取自页面 update log 首条） |

- 改前备份: .hermes/backups/schema-audit-0829/（2 原件）
- 技术注记: about 页工作副本为 CRLF、methodology 为 LF，补丁按文件实际行尾构造匹配串（首跑 LF 串撞 CRLF 被 count=0 安全阀拦截，无半写）

## 三、校验与交付链

- build: PASS（Next.js 15.5.19 · 167/167 页 · 本地含并行会话未提交新稿 1 页；CF 端按已提交状态 166 页）· aff-link 798 注入
- 提交: 031b609（仅 2 个页面文件，+56/-4；提交消息 UTF-8 存储验证 MSG_UTF8_OK=true）
- 并行冲突处置: 提交前 remote 已被并行会话推进至 e789387（0829 daily-search：is-gelato-legit 部署 + reviews 拼接残留修复 + blog-posts 换行规范化），本地共享仓库 HEAD 同步移动，031b609 落其上，push 为 fast-forward（e789387..031b609），零重叠
- push: 成功 · 单 push 单 build（本任务 build 消耗 1 次）
- 线上验证（push 后首轮即过）: /about/ AboutPage=true founder=true authorUrl=true · /methodology/ WebPage=true authorUrl=true → LIVE_VERIFIED

## 四、S6 终态

布局层 Organization（name/url/logo）+ Review 页（author url + publisher logo）+ Article 页（author url）+ AboutPage（founder 锚点）+ WebPage methodology（author/publisher 锚点）+ /author/jerome-tang Person/Organization + best/compare 全套 → Organization/Author 实体链全站闭环，无已知缺口。
