# -*- coding: utf-8 -*-
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ap = r'F:\aitoptools\.hermes\affiliate-programs.json'
with open(ap, encoding='utf-8') as f:
    data = json.load(f)

assert isinstance(data, dict), 'top-level must be dict'
progs = data['programs']
assert isinstance(progs, list)
target = None
for prog in progs:
    if isinstance(prog, dict) and prog.get('name') == 'Printful Affiliate Program':
        target = prog
        break
assert target is not None, 'Printful entry not found'

old = target.get('tax_audit', {})
print('old checked:', old.get('checked'), '| old result:', old.get('result'))

target['tax_audit'] = {
    "checked": "2026-08-15",
    "method": "autoglm browser (AutoGLM 1.1.8, user Chrome 会话, tab 97686550)",
    "url": "https://www.printful.com/dashboard/affiliate/tax",
    "result": "pending-review",
    "detail": "8/15 03:44 复核 (8/15 02:49 上传后第 1 个工作日): 状态仍 Pending, 页面提示 'Your documents will be reviewed in up to 3 business days'; Lines 4/5 黄色提示仍显示 (Please make sure to fill out Lines 4 and 5 of the Form W-8BEN-E before signing and uploading!); 页面上传文件名显示 kutoolm-browser-agent.pdf; Edit/删除按钮可用; 只读未操作. 预计 8/19 前后有结果; 若 8/19 后仍 Pending, 升级 user 核对 Lines 4/5 或联系 Printful support."
}
target['last_updated'] = '2026-08-15'

with open(ap, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')

# verify
with open(ap, encoding='utf-8') as f:
    d2 = json.load(f)
t2 = [x for x in d2['programs'] if isinstance(x, dict) and x.get('name') == 'Printful Affiliate Program'][0]
print('VERIFY checked:', t2['tax_audit']['checked'], '| result:', t2['tax_audit']['result'])
print('VERIFY detail has 预计8/19:', '预计 8/19' in t2['tax_audit']['detail'])
print('VERIFY tax_status:', t2['tax_status'], '| last_updated:', t2['last_updated'])
print('VERIFY top-level last_updated:', d2.get('last_updated'))
print('VERIFY monitoring.next_action kept:', '8/16' in d2.get('monitoring', {}).get('next_action', ''))
