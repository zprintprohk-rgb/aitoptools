#!/usr/bin/env python3
"""Debug: capture T1 output and T2 output, then show byte diff (non-destructive)."""
import os
import shutil
import subprocess
import sys
import difflib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FIXED = os.path.join(HERE, 'generate-sitemap_fixed.py')
d = os.path.join(HERE, 'dbg2')
os.makedirs(os.path.join(d, 'public'), exist_ok=True)
os.makedirs(os.path.join(d, 'out'), exist_ok=True)
os.makedirs(os.path.join(d, 'src', 'data'), exist_ok=True)
shutil.copy2(os.path.join(ROOT, 'src', 'data', 'reviews.json'), os.path.join(d, 'src', 'data', 'reviews.json'))
shutil.copy2(os.path.join(ROOT, 'src', 'data', 'blog-posts.json'), os.path.join(d, 'src', 'data', 'blog-posts.json'))
shutil.copy2(os.path.join(ROOT, 'public', 'sitemap.xml'), os.path.join(d, 'public', 'sitemap.xml'))
shutil.copy2(os.path.join(ROOT, 'public', 'sitemap.xml'), os.path.join(d, 'out', 'sitemap.xml'))
shutil.copy2(os.path.join(ROOT, 'public', 'sitemap-programmatic.xml'), os.path.join(d, 'public', 'sitemap-programmatic.xml'))

def run():
    r = subprocess.run([sys.executable, FIXED, '--project-dir', d],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    print('rc=', r.returncode, r.stdout[-300:], r.stderr[:200])

run()
p1 = os.path.join(d, 'public', 'sitemap.xml')
with open(p1, encoding='utf-8') as f:
    t1 = f.read()
shutil.copy2(p1, os.path.join(HERE, 't1_capture.xml'))
run()
with open(p1, encoding='utf-8') as f:
    t2 = f.read()
shutil.copy2(p1, os.path.join(HERE, 't2_capture.xml'))
print('len t1:', len(t1), 'len t2:', len(t2))
if t1 != t2:
    for i, (a, b) in enumerate(zip(t1, t2)):
        if a != b:
            print(f'first diff at {i}: t1={a!r} t2={b!r}')
            print('t1 ctx:', repr(t1[max(0,i-60):i+60]))
            print('t2 ctx:', repr(t2[max(0,i-60):i+60]))
            break
    # full diff lines
    dl = list(difflib.unified_diff(t1.splitlines(keepends=True), t2.splitlines(keepends=True), n=1))
    print('diff lines:', len(dl))
    for l in dl[:40]:
        print(repr(l))
else:
    print('IDENTICAL')
