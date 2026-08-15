import json, io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
data = json.load(open(r'src\data\comparisons.json', encoding='utf-8'))
print('total comparisons:', len(data))
for c in data:
    words = len(re.sub(r'<[^>]+>', ' ', c.get('content','')).split())
    print(c['slug'], '| words:', words, '| faqs:', len(c.get('faqs',[])), '| dateModified:', c.get('dateModified'), '| relatedLinks:', bool(c.get('relatedLinks')))
