# -*- coding: utf-8 -*-
"""主线就绪度核查（替代异常终止的就绪核验员）— 7 项只读检查，输出 subagent_06-readiness.md"""
import json, os, re, sys, subprocess, time
sys.stdout.reconfigure(errors='replace')

OUT = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\subagent_06-readiness.md'
ROOT = r'F:\aitoptools'
WB = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645'
rows = []

def row(item, status, evidence):
    rows.append((item, status, evidence))

# 1. T2 前置
d = os.path.join(WB, 'DELIVERY')
for f in ['generate-sitemap_merged.py', 'sitemap_fix_test_v2.py']:
    p = os.path.join(d, f)
    row(f'T2 {f}', '就绪' if os.path.exists(p) else '缺失', f'{os.path.getsize(p)} B' if os.path.exists(p) else '不存在')
row('T2 生产脚本现状', '旧版(未替换)', f'{os.path.getsize(os.path.join(ROOT,"scripts","generate-sitemap.py"))} B')
c = open(os.path.join(ROOT, 'public', 'sitemap.xml'), encoding='utf-8').read()
locs = re.findall(r'<loc>(.*?)</loc>', c)
row('T2 public/sitemap.xml', f'{len(locs)} 条 / 唯一 {len(set(locs))}', '0 重复' if len(locs) == len(set(locs)) else f'重复 {len(locs)-len(set(locs))}')

# 2. T3 前置
bp = json.load(open(os.path.join(ROOT, 'src', 'data', 'blog-posts.json'), encoding='utf-8'))
row('T3 blog-posts 总数', str(len(bp)), [p.get('slug') for p in bp][-3:])
t = next((x for x in bp if x.get('slug') == 'kittl-halloween-template-test-2026'), None)
row('T3 辐条①字段', '均 null' if t and not (t.get('publishedAt') or t.get('wordCount') or t.get('status')) else '部分已补',
    f"publishedAt={t.get('publishedAt')} wordCount={t.get('wordCount')} status={t.get('status')}" if t else '未找到')
row('T3 截图目录', '存在' if os.path.isdir(os.path.join(ROOT, 'public', 'tool-screenshots', 'blog')) else '不存在',
    str(os.listdir(os.path.join(ROOT, 'public', 'tool-screenshots', 'blog'))) if os.path.isdir(os.path.join(ROOT, 'public', 'tool-screenshots', 'blog')) else '需新建')
row('T3 out 部署', '已部署' if os.path.isdir(os.path.join(ROOT, 'out', 'blog', 'kittl-halloween-template-test-2026')) else '未部署', '')

# 3. T4 前置
row('T4 link-directory-list.md', '存在' if os.path.exists(os.path.join(WB, 'link-directory-list.md')) else '缺失', f"{os.path.getsize(os.path.join(WB,'link-directory-list.md'))} B" if os.path.exists(os.path.join(WB,'link-directory-list.md')) else '')
lb = os.path.join(ROOT, '.hermes', 'logs', 'link-building-0816.md')
row('T4 link-building-0816.md', '存在' if os.path.exists(lb) else '缺失', time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(lb))) if os.path.exists(lb) else '')
ab = os.path.join(ROOT, '.hermes', 'tmp', 'linkbuild-0816', 'aitoolzdir-body.json')
row('T4 aitoolzdir-body.json', '存在' if os.path.exists(ab) else '缺失', f"{os.path.getsize(ab)} B" if os.path.exists(ab) else '')

# 4. T5 前置（jobs.json）
jobs = json.load(open(r'C:\Users\Administrator\.openclaw-autoclaw\cron\jobs.json', encoding='utf-8'))['jobs']
for jid, name in [('4f19a24a', 'W1-0814'), ('98ebd150', 'W3-0825a'), ('d9aacbed', 'W3-0825b')]:
    j = next((x for x in jobs if x['id'].startswith(jid)), None)
    row(f'T5 {name} enabled', str(j.get('enabled')) if j else '缺失', j['id'][:8] if j else '')

# 5. T6 前置
root_files = ['HEARTBEAT.md', 'IDENTITY.md', 'SOUL.md', 'TOOLS.md', 'USER.md']
present = [f for f in root_files if os.path.exists(os.path.join(ROOT, f))]
row('T6 根目录 Hermes 文件', f'{len(present)}/5 存在', ', '.join(present) or '无')
row('T6 GSC数据/ 目录', '存在' if os.path.isdir(os.path.join(ROOT, 'GSC数据')) else '不存在', '')
gi = open(os.path.join(ROOT, '.gitignore'), encoding='utf-8').read()
row('T6 .gitignore 覆盖', '已含' if any(f in gi for f in root_files) else '未含',
    [f for f in root_files if f in gi] or '需补充')

# 6. T7 前置
r = subprocess.run(['git', '-C', ROOT, 'status', '--short'], capture_output=True, text=True, encoding='utf-8', errors='replace')
st = r.stdout.strip()
row('T7 git status', f'{len(st.splitlines())} 行未提交', st.splitlines()[:8] if st else 'clean')
r = subprocess.run(['git', '-C', ROOT, 'log', '--oneline', '-3', 'origin/main'], capture_output=True, text=True, encoding='utf-8', errors='replace')
row('T7 origin/main', 'HEAD 确认', r.stdout.strip().replace('\n', ' | '))

# 7. T8 前置
row('T8 RESULT-0816', '不存在(待写)' if not os.path.exists(os.path.join(ROOT, 'handoff', 'results', 'RESULT-2026-08-16.md')) else '已存在', '')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('# 执行就绪核验报告（主线代跑）\n\n> 生成 2026-08-16 03:5x · 只读核查 · 替代异常终止的核验子代理\n\n| 核查项 | 状态 | 证据 |\n|---|---|---|\n')
    for item, status, ev in rows:
        f.write(f'| {item} | {status} | {ev} |\n')
    f.write('\n## 阻塞项汇总\n')
    blocks = [r for r in rows if '缺失' in r[1] or '未' in r[1]]
    if blocks:
        for b in blocks:
            f.write(f'- {b[0]}: {b[1]} — {b[2]}\n')
    else:
        f.write('- 无硬阻塞\n')
print('written', OUT)
for r_ in rows:
    print(r_[0], '|', r_[1], '|', r_[2])
