// 8/8 v2 指令集落地脚本 — aitoptools
const fs = require('fs');
const ROOT = 'F:/aitoptools';
const log = [];
const ok = (m) => log.push('OK   ' + m);
const fail = (m) => log.push('FAIL ' + m);

// 0. 建目录
fs.mkdirSync(ROOT + '/.hermes/reports', { recursive: true });
fs.mkdirSync(ROOT + '/.hermes/assets/cf-halloween-2026-08-07', { recursive: true });
ok('.hermes/reports/ + .hermes/assets/cf-halloween-2026-08-07/ 已建');

// 1. CONTENT_PLAN.md: Data-Driven Queue 段
{
  const p = ROOT + '/CONTENT_PLAN.md';
  let s = fs.readFileSync(p, 'utf-8');
  if (!s.includes('## Data-Driven Queue')) {
    const section = `

---

## Data-Driven Queue (GSC 数据驱动选题队列, 2026-08-08 v2 指令启用)

> 由 gsc-mining-daily (每日 13:00) 自动追加; weekly-report (周日) 补充; daily-content Step 0 消费。
> 规则: 展示≥10 且无专页 query → 进队列; 排期优先级 = 矩阵 P0 > 本队列高意图词 > 推排名优化。

| 日期 | query | 展示 | 点击 | CTR | 排名 | 现状 | 排期 | 状态 |
|------|-------|------|------|-----|------|------|------|------|
| (由 gsc-mining-daily 追加) | | | | | | | | |

## Boost Queue (推排名清单: 有页, 排名 20-70, 内链/FAQ/pin 强化)
| 日期 | page | 展示 | 排名 | 目标 | 动作 | 状态 |
|------|------|------|------|------|------|------|
| 2026-08-07 | /blog/print-price-ai-tools-2026/ | 23 | 70 | ≤30 | 内链+FAQ+2 pin | in-progress |
`;
    s = s.trimEnd() + '\n' + section;
    fs.writeFileSync(p, s, 'utf-8');
    ok('CONTENT_PLAN.md Data-Driven Queue + Boost Queue');
  } else ok('CONTENT_PLAN.md 队列已存在, 跳过');
}

// 2. halloween-asset-chain.md: 时间线对齐 v2 关键路径 + 预算 + 平台决策 + 照片 fallback
{
  const p = ROOT + '/.hermes/logs/halloween-asset-chain.md';
  let s = fs.readFileSync(p, 'utf-8');
  const oldTimeline = `## 时间线 (目标 8/18 前 Halloween 集群上线)
| 日期 | 里程碑 | 状态 |
|---|---|---|
| 8/9 | weekly-report 首跑基线读数 | 待执行 |
| 8/10-11 | 用素材做 2-3 个设计 + 下测试单 | - |
| 8/11 | Kittl 实测日: CF 素材当源文件, 实测帖初稿 | - |
| 8/12-13 | Halloween 支柱帖《Halloween POD ideas 2026》写作 | - |
| 8/14 | T+7 首读数 → 决定集群是否加速 | - |
| 8/17 | Halloween 辐条① (CF 免费万圣节素材实测) 上线 | - |
| 8/18 | 集群上线截止 | - |`;
  const newTimeline = `## 时间线 (v2 指令集关键路径, 2026-08-08 对齐)
| 日期 | 里程碑 | 状态 |
|---|---|---|
| 8/9 | weekly-report 首跑基线读数 | 待执行 |
| 8/10 | 设计阶段: Kittl/Claid 用素材 [0:2] 做 2-3 个设计 → .hermes/designs/halloween-test-{date}.png | 待触发 (cron 8/10 10:00) |
| 8/11 | 下单阶段: Printful (若已 verify) 否则 Printify; 预算硬限 $25/单 $50/日; 记录 order_id/eta/cost | 待触发 |
| 8/11 | Kittl 实测日: CF 素材当源文件, 实测帖初稿 | - |
| 8/12-13 | Halloween 支柱帖《Halloween POD ideas 2026》写作 | - |
| 8/14 | T+7 首读数 → 决定集群是否加速 | - |
| 8/15 | 收货拍照: logistics.status=delivered 触发; user 拍照 OR fallback 官方 mockup → public/photos/wall/halloween-{order_id}.jpg | 待触发 |
| 8/17 | Halloween 辐条① (CF 免费万圣节素材实测) 上线 | - |
| 8/18 | 支柱帖上线 + 集群截止 (23:59) | - |

## 执行参数 (v2 指令集, 2026-08-08)
- 下单平台: Printful (if verified) else Printify
- 预算: $25/order hard limit, $50/day hard limit, 超限暂停+告警
- 收货地址: test-address.json (用户提供)
- 照片: 优先 user 拍照; 用户不可用 → fallback 官方 mockup
- 产出: 照片墙 6 图 + 支柱帖源文件 + 毛利数据`;
  if (s.includes(oldTimeline)) {
    s = s.replace(oldTimeline, newTimeline);
    fs.writeFileSync(p, s, 'utf-8');
    ok('halloween-asset-chain.md 时间线 v2 对齐');
  } else fail('halloween tracker 时间线 anchor 未找到');
}

// 3. AFFILIATE_LOG.md: 8/8 条目
{
  const p = ROOT + '/AFFILIATE_LOG.md';
  let s = fs.readFileSync(p, 'utf-8');
  const entry = `

---

## 2026-08-08 00:50 · v2 指令集执行 (K3 orchestrator)
- **Printify promo code 回信**: 已由 Hermes 发出 (SMTP 465, Message-ID <178612007459.38260.17414933324366495799@aitoptools.net>, 留证 .hermes/tmp/printify-sent.txt); 8/11 检查回复 (affiliate-monitor 覆盖 mail.printify.com)
- **Printful 邮箱确认**: 7/20 verify 链接已确认过期 (IMAP 重跑 + headless GET → 302 login + "Email confirmation request does not exist", 截图留证); 后台重发被阻 = printful_session_cookie 缺失 (硬阻塞, 待 user 补录)
- **硬阻塞清单**: ① printful_session_cookie ② pinterest_session ③ gmail_credentials.json app_password 失效 (AUTHENTICATIONFAILED, Hermes 改用 .env IMAP_PASSWORD)
- **安全与审计铁律**: AGENTS.md 已追加 (Hermes 8/7 指令 #6, 5 条) + .hermes/audit/ 已建
- **定时任务注册 (OpenClaw cron)**: weekly-report 8/9 08:00 / halloween-chain 8/10 10:00 / gsc-mining 每日 13:00 / printful-verify watcher 每时 8-22 (cookie 就绪即执行)
- **sitemap 补跑**: 8/8 00:2x 已完成 (338 URL, 6 blog 入图, IndexNow 6/6 200, C2b 已记)`;
  s = s.trimEnd() + '\n' + entry + '\n';
  fs.writeFileSync(p, s, 'utf-8');
  ok('AFFILIATE_LOG.md 8/8 条目');
}

// 4. 任务卡 1: printful-verify-resend
{
  const p = ROOT + '/.hermes/cron-prompts/aitoptools-printful-verify-resend.md';
  const content = `# Task Card: printful_verify_resend (P0, cookie 解锁后立即执行)

> 2026-08-08 v2 指令集 P0 · 前置: .hermes/secrets/printful_session_cookie (user 补录)
> 安全边界: 仅做邮箱重发验证, 不碰支付/资金/改密; 异常立即停止 + 告警 (AGENTS.md 安全与审计铁律)

## 幂等检查 (R4, 先做)
- affiliate-programs.json 的 printful.email_verified=true → 输出 "ALREADY DONE" 退出

## 步骤
1. cookie 文件存在且有效 (HEAD https://www.printful.com/dashboard 不 302 到 login)
2. headless login Affiliate Dashboard (cookie 通道, 不输密码)
3. navigate Settings → Email Verification → Resend
4. poll Gmail IMAP 新 verify 邮件 (max 3 次, 60s 间隔; 用 .env IMAP_PASSWORD, 勿用失效的 app_password)
5. 提取链接 → GET → 验证响应含 "verified"
6. 更新 affiliate-programs.json: email_verified=true, status=approved
7. 触发 aff-link scanner: 裸 printful.com 链接替换为跟踪 URL (scripts/replace_affiliate_links.py 模式)
8. log 到 .hermes/audit/printful-verify-{timestamp}.json + browser-auto log
9. 删除本 watcher cron (自清理)

## fallback
- 任一 403/CAPTCHA/超时 (2 次重试后) → 停止 + 告警 user (附截图 + 手动重发指引)
- timeout: 5 min
`;
  fs.writeFileSync(p, content, 'utf-8');
  ok('任务卡 printful-verify-resend');
}

// 5. 任务卡 2: halloween-chain
{
  const p = ROOT + '/.hermes/cron-prompts/aitoptools-halloween-chain.md';
  const content = `# Task Card: halloween_asset_chain_execution (P2, 8/10 10:00 触发)

> 2026-08-08 v2 指令集 P2 · 前置检查: .hermes/assets/cf-halloween-2026-08-07/ 有素材 + printful_session_cookie 或 Printify 可用
> 跟踪器: .hermes/logs/halloween-asset-chain.md (每日 brief 更新)

## 前置检查 (缺任一 → 记 blocked + 给 user 清单, 退出)
- [ ] assets 目录有素材 (CF 下载需 user 登录, 素材源: .hermes/logs/cf-freebies/2026-08-07.md)
- [ ] 下单平台可用: printful_session_cookie 或 Printify 联盟链路
- [ ] test-address.json 存在 (收货地址)

## phases
1. design: Kittl API / browser automation; input assets [0:2]; output .hermes/designs/halloween-test-{date}.png
2. order: Printful (if verified) else Printify; T-shirt/Hoodie; budget $25/order $50/day hard limit; record order_id/eta/cost → halloween-asset-chain.md
3. photo: 由收货 watcher 触发 (logistics delivered); user 拍照 OR fallback 官方 mockup; upload public/photos/wall/halloween-{order_id}.jpg
4. 产出: 照片墙 6 图 + 支柱帖源文件 + 毛利数据

## deadline
- 8/18 23:59 集群上线; 8/11 Kittl 实测日 (素材当源文件, 实测帖初稿)
`;
  fs.writeFileSync(p, content, 'utf-8');
  ok('任务卡 halloween-chain');
}

// 6. 任务卡 3: gsc-mining-daily
{
  const p = ROOT + '/.hermes/cron-prompts/aitoptools-gsc-mining-daily.md';
  const content = `# Task Card: gsc_mining_daily (P3, 每日 13:00 触发 — gsc-indexnow 12:40 之后)

> 2026-08-08 v2 指令集 P3 · 数据源: GSC (gsc-oauth.json 若已配置; 否则 gsc_data.csv 或 blocked_missing_credentials)

## logic
1. mining: query 展示≥10 AND CTR<0.05 AND 无专页 → 追加 CONTENT_PLAN.md "## Data-Driven Queue"
2. boosting: 现有页排名 20-70 AND 展示≥5 → 动作: ① top 3 相关帖注入内链 ② 追加目标 query 的 FAQ schema ③ 生成 2 个指向该 URL 的 Pinterest pin
3. report: 写入每日 brief "🎯 GSC Opportunities" 段

## 幂等检查 (R4)
- CONTENT_PLAN.md 队列已有同 query 同日期行 → 跳过 (只追加不重复)
`;
  fs.writeFileSync(p, content, 'utf-8');
  ok('任务卡 gsc-mining-daily');
}

console.log(log.join('\n'));
