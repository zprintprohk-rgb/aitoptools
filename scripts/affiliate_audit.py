import json, os, re, datetime

logdir = '/mnt/f/aitoptools/.hermes/logs'
today = datetime.date.today().isoformat()

# 1. Check reviews.json for affiliate links
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
    has_affiliate = 0
    placeholder_affiliate = 0
    missing_affiliate = 0
    broken_candidates = []
    
    for r in reviews:
        slug = r.get('slug', '?')
        aff_url = r.get('affiliateUrl', '') or r.get('affiliate_url', '') or ''
        visit_url = r.get('visitUrl', '') or r.get('visit_url', '') or ''
        
        if aff_url and 'fpr=' in aff_url.lower():
            placeholder_affiliate += 1
            broken_candidates.append((slug, aff_url, 'PLACEHOLDER (fpr=partner)'))
        elif aff_url:
            has_affiliate += 1
        else:
            missing_affiliate += 1
            broken_candidates.append((slug, 'MISSING', 'No affiliate URL set'))
    
    report_lines.append(f"- Total reviews: {total_tools}")
    report_lines.append(f"- Has affiliate URL: {has_affiliate}")
    report_lines.append(f"- Placeholder (fpr=partner): {placeholder_affiliate}")
    report_lines.append(f"- Missing affiliate URL: {missing_affiliate}")
    report_lines.append("")
    report_lines.append("### Issues Found:")
    for slug, url, status in broken_candidates:
        report_lines.append(f"- **{slug}**: {status} -> {url}")
    
except Exception as e:
    report_lines.append(f"Error reading reviews.json: {e}")

# 2. Check TSX files for affiliate links
report_lines.append("")
report_lines.append("## 2. TSX 组件联盟链接检查")
report_lines.append("")

tsx_files = [f for f in os.listdir(logdir) if f.endswith('.tsx')]
tsx_with_affiliate = 0
tsx_without_affiliate = 0
tsx_with_placeholder = 0

for fn in sorted(tsx_files):
    fpath = os.path.join(logdir, fn)
    content = open(fpath, encoding='utf-8').read()
    
    has_sponsored = 'nofollow sponsored' in content
    has_fpr = 'fpr=' in content
    has_aff_url = 'href="http' in content and ('nofollow' in content)
    
    if has_fpr:
        tsx_with_placeholder += 1
    elif has_sponsored:
        tsx_with_affiliate += 1
    else:
        tsx_without_affiliate += 1

report_lines.append(f"- TSX files checked: {len(tsx_files)}")
report_lines.append(f"- With real affiliate links: {tsx_with_affiliate}")
report_lines.append(f"- With placeholder URLs: {tsx_with_placeholder}")
report_lines.append(f"- Without affiliate links: {tsx_without_affiliate}")

# 3. Check new tools JSON for affiliate links
report_lines.append("")
report_lines.append("## 3. 新工具入库联盟链接检查")
report_lines.append("")

new_json_files = sorted([f for f in os.listdir(logdir) if '新工具入库' in f and f.endswith('.json')])
for fn in new_json_files:
    fpath = os.path.join(logdir, fn)
    try:
        with open(fpath) as jf:
            ndata = json.load(jf)
        empty_aff = 0
        total_new = len(ndata.get('tools', []))
        for t in ndata.get('tools', []):
            aff = t.get('affiliateUrl', '') or t.get('affiliate_url', '') or ''
            if not aff:
                empty_aff += 1
        pct = round(100 * empty_aff / total_new) if total_new > 0 else 0
        report_lines.append(f"- {fn}: {total_new} tools, {empty_aff} missing affiliate links ({pct}%)")
    except:
        report_lines.append(f"- {fn}: ERROR reading file")

# Summary
report_lines.append("")
report_lines.append("---")
report_lines.append("## 汇总")
report_lines.append("")

all_missing = placeholder_affiliate + missing_affiliate
report_lines.append(f"- reviews.json 中 {all_missing}/{total_tools} 个工具联盟链接有问题")
report_lines.append(f"- 今日新增 {len(new_tools_in)} 个工具均无联盟链接" if True else "")

# Recommendations
report_lines.append("")
report_lines.append("## 替换建议")
report_lines.append("")
report_lines.append("| 工具 | 当前链接 | 建议替换 |")
report_lines.append("|------|---------|---------|")
for slug, url, status in broken_candidates:
    report_lines.append(f"| {slug} | {url} | 注册对应联盟计划并替换为真实ID |")

if placeholder_affiliate + missing_affiliate > 5:
    report_lines.append("")
    report_lines.append("⚠️ **异常**: 超过5个联盟链接有问题，需要立即处理！")

outpath = os.path.join(logdir, today + "-联盟巡检.md")
with open(outpath, 'w', encoding='utf-8') as f:
    f.write("\n".join(report_lines))
print("OK: Audit report written to " + outpath)
