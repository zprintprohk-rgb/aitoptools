# -*- coding: utf-8 -*-
import subprocess, os, re

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout.strip() + r.stderr.strip()

print('=== git log for scripts/generate-sitemap.py ===')
print(run('git -C F:\\aitoptools log --oneline -8 -- scripts/generate-sitemap.py'))
print()
print('=== git status short ===')
print(run('git -C F:\\aitoptools status --short scripts/'))
print()
print('=== robots agents in current script ===')
src = open(r'F:\aitoptools\scripts\generate-sitemap.py', encoding='utf-8').read()
for agent in ['Applebot', 'Amazonbot', 'meta-external', 'cohere', 'GPTBot', 'OAI-SearchBot', 'PerplexityBot', 'ClaudeBot']:
    lines = [i + 1 for i, l in enumerate(src.splitlines()) if agent in l]
    print(agent, '->', lines)
print()
print('=== file size / eol ===')
print('len:', len(src), 'CRLF:', src.count('\r\n'), 'LF-only:', src.count('\n') - src.count('\r\n'))
