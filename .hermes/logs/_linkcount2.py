import re, glob, io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def count_links(f):
    html = open(f, encoding='utf-8').read()
    links = re.findall(r'href="(/[^"#][^"]*)"', html)
    return [l for l in links if not l.startswith('//') and not l.startswith('http')]
# review pages = out/*-review/index.html + others under root
root_pages = [f for f in glob.glob(r'out/*/index.html')]
rev = [f for f in root_pages if '-review' in f]
cmp = [f for f in glob.glob(r'out/compare/*/index.html')]
best = [f for f in glob.glob(r'out/best/*/index.html')]
def total(files): return sum(len(count_links(f)) for f in files)
print('review pages:', len(rev), '| internal links:', total(rev))
print('compare pages:', len(cmp), '| internal links:', total(cmp))
print('best pages:', len(best), '| internal links:', total(best))
print('review+compare:', total(rev)+total(cmp))
