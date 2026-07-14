import json, os, datetime

logdir = '/mnt/f/aitoptools/.hermes/logs'
today = datetime.date.today().isoformat()

reviews_path = '/mnt/f/aitoptools/src/data/reviews.json'
issues = []
report_lines = []

report_lines.append("# 联盟链路巡检报告 - " + today)
report_lines.append("")
report_lines.append("## 1. reviews.json 联盟链接检查")

try:
    with open(reviews_path) as f:
        reviews = json.load(f)
    
    total_tools = len(reviews)
    placeholder_affiliate = 0
    missing_affiliate = 0
    broken_candidates = []
    
    for r in reviews:
        slug = r.get('slug', '?')
        aff_url = r.get('affiliateUrl', '') or r.get('affiliate_url', '') or ''
        
        if aff_url and 'fpr=' in aff_url.lower():
            placeholder_affiliate += 1
            broken_candidates.append((slug, aff_url, 'PLACEHOLDER (fpr=partner)'))
        elif not aff_url:
            missing_affiliate += 1
            broken_candidates.append((slug, 'MISSING', 'No affiliate URL'))
    
    report_lines.append("- Total reviews: " + str(total_tools))
    report_lines.append("- Placeholder (fpr=partner): " + str(placeholder_affiliate))
    report_lines.append("- Missing affiliate URL: " + str(missing_affiliate))
    report_lines.append("")
    report_lines.append("### Issues Found:")
    for slug, url, status in broken_candidates:
        report_lines.append("- **" + slug + "**: " + status + " -> " + url)
    
except Exception as e:
    report_lines.append("Error reading reviews.json: " + str(e))
    total_tools = 0
    placeholder_affiliate = 0
    missing_affiliate = 0
    broken_candidates = []

# 2. Check TSX files
report_lines.append("")
report_lines.append("## 2. TSX 组件联盟链接检查")
report_lines.append("")

tsx_files = [f for f in os.listdir(logdir) if f.endswith('.tsx')]
tsx_with_placeholder = 0
tsx_with_sponsored = 0

for fn in sorted(tsx_files):
    fpath = os.path.join(logdir, fn)
    content = open(fpath, encoding='utf-8').read()
    if 'fpr=' in content:
        tsx_with_placeholder += 1
    elif 'nofollow sponsored' in content:
        tsx_with_sponsored += 1

report_lines.append("- TSX files checked: " + str(len(tsx_files)))
report_lines.append("- With sponsored links: " + str(tsx_with_sponsored))
report_lines.append("- With placeholder URLs: " + str(tsx_with_placeholder))

# 3. New tool files
report_lines.append("")
report_lines.append("## 3. 新工具入库文件联盟链检查")
report_lines.append("")

new_json_files = sorted([f for f in os.listdir(logdir) if '新工具入库' in f and f.endswith('.json')])
total_new_empty_aff = 0
total_new_tools = 0

for fn in new_json_files:
    fpath = os.path.join(logdir, fn)
    try:
        with open(fpath) as jf:
            ndata = json.load(jf)
        empty_aff = 0
        count = len(ndata.get('tools', []))
        for t in ndata.get('tools', []):
            aff = t.get('affiliateUrl', '') or t.get('affiliate_url', '') or ''
            if not aff:
                empty_aff += 1
        total_new_tools += count
        total_new_empty_aff += empty_aff
        report_lines.append("- " + fn + ": " + str(count) + " tools, " + str(empty_aff) + " missing affiliate links")
    except:
        report_lines.append("- " + fn + ": ERROR reading")

# Summary
report_lines.append("")
report_lines.append("---")
report_lines.append("## 汇总")
report_lines.append("")

all_issues = placeholder_affiliate + missing_affiliate
report_lines.append("- reviews.json: " + str(all_issues) + "/" + str(total_tools) + " tools with affiliate link issues")
report_lines.append("- 所有新工具入库文件合计: " + str(total_new_empty_aff) + "/" + str(total_new_tools) + " tools missing affiliate links")

report_lines.append("")
report_lines.append("## 替换建议")
report_lines.append("")
report_lines.append("| 工具 | 当前状态 | 建议操作 |")
report_lines.append("|------|---------|---------|")
for slug, url, status in broken_candidates[:20]:
    report_lines.append("| " + slug + " | " + status + " | 注册对应联盟计划并替换真实affiliate ID |")

if all_issues > 5:
    report_lines.append("")
    report_lines.append("⚠️ **异常**: reviews.json 中超过5个联盟链接有问题，需要立即处理！")

outpath = os.path.join(logdir, today + "-联盟巡检.md")
with open(outpath, 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))
print("OK: Audit report written to " + outpath)
