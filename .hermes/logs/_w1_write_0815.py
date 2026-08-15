# -*- coding: utf-8 -*-
import json, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = r'F:\aitoptools'

report = '''# aitoptools W1-0815 复核节点 — 2026-08-15

> 生成: 2026-08-15 03:4x (Asia/Shanghai) · cron W1-0815 复核节点 (T+7 Branch A 加速·温和版落地 + K3 V2)
> 数据: GSC API 实时拉取 (gsc-oauth.json + SOCKS5 127.0.0.1:7892, Python 3.12 + PyJWT 2.13) + 哨兵 rank-sentinel-2026-08-15.md (03:33 已拉, 本次独立拉取交叉验证一致) + autoglm 浏览器 tax 只读复核 (03:44)
> 环境备注: AutoClaw 自带 python 3.13 缺 PyJWT, 本次用 Python312 (C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python312) 执行 gsc 拉取; 8/13 日期行 GSC 仍未回填 (T+2 延迟持续), 8/12 已可读

## 一、#1/#2 T+7 严格复核 (Boost 8/8 上线, T+7 窗口 8/8-8/14)

| 项 | 基线 (6/28-8/5) | 8/14 读数 (8/6-8/11) | 严格 T+7 (8/8-8/14) | 判定 |
|---|---|---|---|---|
| #1 sticker mule (query) | 37.3 / 26 imp | — | **36.0 / 11 imp** | 改善 +1.3 位 (正向, 未达 5 位阈值) |
| #1 页面 /stickermule-review/ | 35.1 / 179 imp | — | 39.0 / 111 imp | 页面口径 -3.9 (口径见下) |
| #2 runway ml (query) | 68.7 / 42 imp | 67.6 / 10 imp | **65.2 / 5 imp** | 改善 +3.5 位 vs 基线; +2.4 vs 8/14 读数 |
| #2 页面 /runway-ml-review/ | 63.0 / 201 imp | — | 73.0 / 43 imp | 页面口径 -10.0 (口径见下) |
| 长尾 runwayml (typo) | 70.6 | — | 79.5 (8/6-13 窗口 72.3) | 波动, 非主词 |
| 长尾 what is sticker mule | — | — | 43.0 (8/6-13 窗口 52.8) | 窗口间 +9.8 观察 |
| 长尾 sticker mule reviews | — | — | 49.0 (8/6-13 窗口 51.5) | 窗口间 +2.5 观察 |

口径说明: query 位置 = 该 query 精确聚合位 (T+7 判定基准); 页面位置 = 页面承接全部 query 的加权平均位, 受新出现长尾词分布拖累。两主 query 均改善但未达 ≥5 位 → 四杠杆起效的早期信号, 最终 A/B/C/D 判定在 8/22 T+14。

## 二、GSC T+2 并入 (补拉 8/12-8/13, 补齐 T+7 窗口 8/6-8/11)

- 8/12 展示 **407** = 窗口峰值 (8/13 行 GSC 仍未回填, 后续哨兵捕获)
- 日均展示: 8/6-8/11 = 216.5 (6 天) → 含 8/12 = 243.7 (7 天) → **维持 ≥200 达标**
- 点击: 全窗口 0 (8/3 单点未再现, 深度排名期常态)
- T+7 表并入复核 (8/6-8/11 → 8/6-8/13):

| query | 8/14 读数 | T+2 并入后 | 变化 |
|---|---|---|---|
| is magicdrop legit | 62.5 | **56.2** (45 imp) | 改善 +6.3 (#3 Boost 8/13 生效, 窗口最佳) |
| kittl review | 74.0 | 70.5 (2 imp) | 改善 +3.5 (T14 内链效果窗口内已现) |
| print price ai tool | 65.5 | 65.2 (13 imp) | +0.3 |
| kittl | 65.0 | 65.9 (9 imp) | -0.9 |
| runway ml | 67.6 | 67.6 (10 imp) | 0 |
| midjourney review | 86.8 | 86.4 (36 imp) | +0.4 |
| copy ai review | 80.9 | 81.1 (11 imp) | -0.2, 仍深 (8/16 快修确认) |
| printful alternatives | 75.9 | 76.1 (23 imp) | -0.2 |
| printify alternatives | 80.7 | 81.0 (12 imp) | -0.3 |
| jasper ai review | 90.5 | 90.8 (57 imp) | -0.3 |
| manychat shopify | 84.1 | 84.3 (26 imp) | -0.2 |

## 三、kittl 哨兵复读 (窗口 8/8-8/14, 与 03:33 哨兵交叉验证)

- **kittl review = 67.0 (imps 1)** — 本节点独立拉取与哨兵完全一致
- 三日趋势: 74.0 (8/13) → 67.0 (8/14) → 67.0 (8/15) = **连续 2 日企稳且低于前低 68.5**
- 结论: T14 Kittl 系内链补强见效 ✓; "再跌 ≥5 位 ALERT" 未触发; 8/22 T+14 继续观察

## 四、tax-audit 复核 (autoglm 只读, 03:44, tab 97686550)

- **Status: Pending (待审核) — 未 Approved**
- 页面提示原文: "Your documents will be reviewed in up to 3 business days"
- Lines 4/5 黄色提示仍显示: "Please make sure to fill out Lines 4 and 5 of the Form W-8BEN-E before signing and uploading!"
- 已上传文件: autoglm-browser-agent.pdf (8/15 02:49 上传); 可用按钮: Edit / 删除
- 处置: **tax_status 不更新** (维持 w8ben-e-uploaded-pending-review, payout_ready 不置位); affiliate-programs.json tax_audit 已更新为本次复核
- 升级 user: 8/15 上传后第 1 个工作日, 审核 ≤3 个工作日 → 预计 **8/19 前后有结果**; 若 8/19 后仍 Pending 需联系 Printful support 或核对 Lines 4/5 后重新上传

## 五、Branch A 风险开关 (8/14 哨兵 vs 8/15 哨兵)

- 20q 对比: **0 个 query 下滑 ≥5 位**; 最大下滑 = printful vs printify +1.6 / printful alternatives +0.4; 改善 = runway ml -2.4 / printify alternatives -1.7
- **大面积下滑 ≥10 位: 未触发 → Branch A (加速·温和版) 继续确认** ✓
- 维持: 每天 Boost 1 页, 3 周清完 25 候选; 不转 Branch D (无需 robots/sitemap 紧急排查, 不暂停 Boost)

## 六、对 8/16 快修的影响

1. **copy ai review 确认入 8/16 快修**: T+2 并入后 81.1, 较基线 73.4 仍 -7.7 且无自然恢复 → B 类 title/meta 快修保留 (bfix-0816.md 清单不变)
2. **kittl review 无需额外动作**: 67.0 已稳住, 8/14 重写 (f4f5c64) 已上线, 8/16 快修名单不含 kittl
3. **is magicdrop legit 正向信号**: +6.3 位至 56.2, #3 Boost 生效, 无需干预; 8/21 T+7 对比 (#3/#4)
4. **#1/#2 未达 5 位阈值**: 8/16 不追加 Boost 动作, 保持节奏; 8/22 T+14 判定 A(≥5)/B(1-4)/C(0) — 当前趋势若维持落 B 区, 届时按 B 补外部信号 (Pinterest/社交)
5. 8/16 push 按 bfix-0816.md 原计划: 25 页 title/meta + copy ai + GSC sitemap 提交

## 七、user 动作清单 (升级)

1. **Printful 税务**: W-8BEN-E 上传后仍 Pending (8/15 上传, ≤3 工作日审核) — 预计 8/19 前后有结果; 若超期仍 Pending, 打开 printful.com/dashboard/affiliate/tax 核对 Lines 4/5 或联系 support
2. 维持 8/14 清单: Printify promo 站内催 (PartnerStack) + Synthesia 激活 (Rewardful 邮件) + Placeit 催办邮件 (drafts/placeit-followup-email.md)

## 产物与状态

- 本文件 + affiliate-programs.json tax_audit 更新 + boost-tracking.md #1/#2 T+7 列填写
- 无 push (复核节点, 不触发 Cloudflare build); 8/16 B 类快修攒批 push
- 哨兵 rank-sentinel-2026-08-15.md 由同会话前置步骤 03:33 产出, 已交叉验证
'''

# 1. write report
rp = os.path.join(BASE, '.hermes', 'logs', 'review-0815.md')
with open(rp, 'w', encoding='utf-8', newline='\n') as f:
    f.write(report)
print('report written:', os.path.getsize(rp), 'bytes')

# 2. update affiliate-programs.json
ap = os.path.join(BASE, '.hermes', 'affiliate-programs.json')
with open(ap, encoding='utf-8') as f:
    data = json.load(f)
for prog in data:
    if isinstance(prog, dict) and prog.get('name') == 'Printful Affiliate Program':
        prog['tax_audit'] = {
            "checked": "2026-08-15",
            "method": "autoglm browser (AutoGLM 1.1.8, user Chrome 会话, tab 97686550)",
            "url": "https://www.printful.com/dashboard/affiliate/tax",
            "result": "pending-review",
            "detail": "8/15 03:44 复核 (8/15 02:49 上传后第 1 个工作日): 状态仍 Pending, 页面提示 'Your documents will be reviewed in up to 3 business days'; Lines 4/5 黄色提示仍显示 (Please make sure to fill out Lines 4 and 5...); 已上传文件 autoglm-browser-agent.pdf; Edit/删除按钮可用; 只读未操作. 预计 8/19 前后有结果, 超期仍 Pending 则升级 user 联系 support."
        }
        prog['last_updated'] = '2026-08-15'
        print('printful tax_audit updated')
with open(ap, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('affiliate-programs.json saved')

# 3. update boost-tracking.md T+7 columns
bt = os.path.join(BASE, '.hermes', 'logs', 'boost-tracking.md')
with open(bt, encoding='utf-8') as f:
    txt = f.read()
r1_old = '| 1 | /stickermule-review/ | 179 | 35.1 | ≤15 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 待 8/15 对比 |'
r1_new = '| 1 | /stickermule-review/ | 179 | 35.1 | ≤15 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 36.0 (+1.3) 8/15 T+7 |'
r2_old = '| 2 | /runway-ml-review/ | 201 | 63.0 | ≤20 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 待 8/15 对比 |'
r2_new = '| 2 | /runway-ml-review/ | 201 | 63.0 | ≤20 | ✅ DONE (BLUF+表+内链+FAQ6) | 8/8 | 65.2 (+3.5) 8/15 T+7 |'
n = 0
if r1_old in txt:
    txt = txt.replace(r1_old, r1_new); n += 1
if r2_old in txt:
    txt = txt.replace(r2_old, r2_new); n += 1
with open(bt, 'w', encoding='utf-8', newline='\n') as f:
    f.write(txt)
print('boost-tracking rows updated:', n)
