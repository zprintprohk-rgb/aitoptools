"""Affiliate link audit for today's tools + persistent issues"""
import json
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_dir = "/mnt/f/aitoptools/.hermes/logs"

tools = json.load(open(f"{log_dir}/{today}-新工具入库.json"))

# Count issues
missing_links = []
for t in tools:
    has_affiliate = bool(t.get("affiliate_url") and t["affiliate_url"].strip())
    status = "MISSING" if not has_affiliate else "OK"
    missing_links.append((t["name"], t["slug"], t.get("affiliate_program","N/A"), t.get("affiliate_url",""), status))
    if not has_affiliate:
        pass  # all tracked

# Persistent issues from context
persistent = """
- 31/33 entries in reviews.json use placeholder ?fpr=partner URLs
- No affiliate program registrations completed since launch
- All 110+ TSX component CTA links point to visitURL (not affiliate URLs)
"""

report = f"""# 联盟链路巡检报告 - {today}

## 今日新工具联盟链接状态

| 工具 | Slug | 推荐联盟 | 状态 |
|------|------|---------|------|
"""
for name, slug, prog, url, status in missing_links:
    report += f"| {name} | {slug} | {prog} | {status} |\n"

report += f"""
### 汇总
- 今日新工具总数: {len(tools)}
- 缺少联盟链接: {sum(1 for _,_,_,_,s in missing_links if s == 'MISSING')}
- 已有联盟链接: {sum(1 for _,_,_,_,s in missing_links if s == 'OK')}

## 新工具联盟计划注册建议

| 工具 | 推荐联盟计划 | 注册链接 |
|------|------------|---------|
| Leonardo AI | Impact | https://impact.com/ |
| Runway Gen-3 | Impact | https://impact.com/ |
| ElevenLabs | Impact | https://impact.com/ |
| HeyGen | Impact | https://impact.com/ |
| Jasper AI | Impact / PartnerStack | https://impact.com/ |
| Copy.ai | Impact / PartnerStack | https://impact.com/ |
| Typeface | N/A (Enterprise) | Contact sales |
| Frase.io | Impact / ShareASale | https://shareasale.com/ |
| Writesonic | Impact / PartnerStack | https://impact.com/ |
| Canva Print | Impact | https://impact.com/ |

## 持久问题（沿用至今）
{persistent}

## 异常状态
"""
num_missing = sum(1 for _,_,_,_,s in missing_links if s == 'MISSING')
if num_missing > 5:
    report += f":warning: **异常上报**: 今日 {num_missing} 个新工具缺少联盟链接（超过5个阈值），建议优先注册联盟账号。\n"
    report += f"累计未解决: reviews.json 中 31/33 个 placeholder 链接 + {num_missing} 个新工具无链接\n"

report += """
## 建议操作
1. 优先注册 Impact Radius 联盟账号（覆盖 20+ 工具）
2. 注册 ShareASale（覆盖 10+ 工具）
3. 注册 PartnerStack（覆盖 SaaS 工具）
4. 获取联盟 ID 后批量更新所有 TSX 组件中的 CTA 链接
"""

with open(f"{log_dir}/{today}-联盟巡检.md", "w") as f:
    f.write(report)
print(f"Affiliate audit saved to {today}-联盟巡检.md")
print(f"Missing links: {num_missing} / {len(tools)}")
if num_missing > 5:
    print("WARNING: Missing links exceed threshold of 5!")
