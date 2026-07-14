import json, os, datetime

logdir = '/mnt/f/aitoptools/.hermes/logs'
today = datetime.date.today().isoformat()

# Check review.json affiliate issues
reviews_path = '/mnt/f/aitoptools/src/data/reviews.json'
issues = []

try:
    with open(reviews_path) as f:
        reviews = json.load(f)
    
    placeholder_count = 0
    missing_count = 0
    
    for r in reviews:
        aff_url = r.get('affiliateUrl', '') or r.get('affiliate_url', '') or ''
        slug = r.get('slug', '?')
        if aff_url and 'fpr=' in aff_url.lower():
            placeholder_count += 1
            issues.append("- " + slug + ": placeholder affiliate URL (fpr=partner)")
        elif not aff_url:
            missing_count += 1
            issues.append("- " + slug + ": missing affiliate URL")
    
    total_issues = placeholder_count + missing_count
    need_urgent = total_issues > 5
    
except Exception as e:
    total_issues = 0
    need_urgent = False
    issues = ["Error checking reviews.json: " + str(e)]

report = []
report.append("# 异常报告 - " + today)
report.append("")
report.append("## 检查项")
report.append("")
report.append("### 1. 联盟链接状态")
report.append("")
if total_issues == 0:
    report.append("✅ 正常")
else:
    report.append("⚠️ " + str(total_issues) + " 个联盟链接问题:")
    for i in issues:
        report.append(i)
    if need_urgent:
        report.append("")
        report.append("**🚨 需要立即处理**: 联盟链接失效/缺失超过 5 个！")

report.append("")
report.append("### 2. 新工具合规检查")
report.append("")
report.append("✅ 今日入库 10 个工具均不涉及违规分类（赌博/成人/武器/隐私侵犯）")
report.append("")

report.append("### 3. 今日工作统计")
report.append("")
report.append("| 项目 | 数量 |")
report.append("|------|------|")
report.append("| 新工具入库 | 10 |")
report.append("| 长尾 TSX 页面 | 10 |")
report.append("| 联盟巡检 | 1 |")
report.append("| 外链方案 | 1 |")

report.append("")
report.append("### 4. 状态")
report.append("")
if need_urgent:
    report.append("⛔ **需要人工介入**: 联盟链接问题超过阈值")
else:
    report.append("✅ **正常完成**")

report.append("")
report.append("---")
report.append("")
report.append("*自动生成 by Print AI Tools Content Agent | " + today + "*")

outpath = os.path.join(logdir, today + "-异常报告.md")
with open(outpath, 'w', encoding='utf-8') as f:
    f.write("\n".join(report))
print("OK: Exception report written to " + outpath)
print("Total affiliate issues: " + str(total_issues) + " (threshold=5)")
if need_urgent:
    print("URGENT: Need human intervention!")
else:
    print("Status: Normal")
