import re, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
files = glob.glob(r'out/**/*.html', recursive=True)
total_links = 0; pages_with = 0; total_pages = len(files); counts = []
for f in files:
    try:
        html = open(f, encoding='utf-8').read()
    except Exception:
        continue
    links = re.findall(r'href="(/[^"#][^"]*)"', html)
    internal = [l for l in links if not l.startswith('//')]
    internal = [l for l in internal if not l.startswith('http')]
    total_links += len(internal)
    if len(internal) >= 2: pages_with += 1
    counts.append((len(internal), f))
counts.sort(reverse=True)
print('pages:', total_pages, '| total_internal_links:', total_links, '| pages_with>=2:', pages_with)
print('--- top 10 pages by internal links ---')
for c in counts[:10]: print(c[1], c[0])
print('--- pages with <2 internal links (need work):', sum(1 for c in counts if c[1] < 2))
