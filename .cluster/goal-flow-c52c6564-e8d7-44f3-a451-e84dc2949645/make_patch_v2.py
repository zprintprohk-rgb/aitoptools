# -*- coding: utf-8 -*-
"""生成 LF 归一化 v2 补丁（基于当前生产 HEAD 基线），并验证可应用性。"""
import difflib
import subprocess
import os

PROD = r'F:\aitoptools\scripts\generate-sitemap.py'
MERGED = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\generate-sitemap_merged.py'
PATCH = r'F:\aitoptools\.cluster\goal-flow-c52c6564-e8d7-44f3-a451-e84dc2949645\sitemap_fix_v2.patch'

with open(PROD, encoding='utf-8') as f:
    old = f.read().splitlines(keepends=True)
with open(MERGED, encoding='utf-8') as f:
    new = f.read().splitlines(keepends=True)

diff = difflib.unified_diff(old, new, fromfile='a/scripts/generate-sitemap.py',
                            tofile='b/scripts/generate-sitemap.py', lineterm='\n')
lines = [l if l.endswith('\n') else l + '\n' for l in diff]
patch_text = ''.join(lines)
with open(PATCH, 'w', encoding='utf-8', newline='\n') as f:
    f.write(patch_text)
print('patch written:', PATCH, len(patch_text), 'bytes')
print('CRLF count:', patch_text.count('\r\n'))
print('hunks:', patch_text.count('@@'))
