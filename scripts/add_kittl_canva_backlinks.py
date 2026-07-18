import json

p = 'F:/aitoptools/src/data/reviews.json'
d = json.load(open(p, encoding='utf-8'))

for x in d:
    if x['slug'] == 'kittl-review':
        old = '<p><em>Choosing your design stack? See our head-to-head <a href="/compare/kittl-vs-placeit/">Kittl vs Placeit comparison (2026)</a> — design creation vs mockups, pricing and AI features tested side by side.</em></p>'
        new = ('<p><em>Choosing your design stack? See our head-to-head <a href="/compare/kittl-vs-placeit/">Kittl vs Placeit comparison (2026)</a>'
               ' — design creation vs mockups — and <a href="/compare/kittl-vs-canva/">Kittl vs Canva (2026)</a>'
               ' — typography and print-ready output vs general-purpose design.</em></p>')
        assert old in x['content']
        x['content'] = x['content'].replace(old, new, 1)
        print('kittl-review updated')
    elif x['slug'] == 'canva-ai-review':
        assert '/compare/kittl-vs-canva/' not in x['content']
        note = ('<p><em>Sell print-on-demand or design merchandise? See our head-to-head'
                ' <a href="/compare/kittl-vs-canva/">Kittl vs Canva comparison (2026)</a>'
                ' — which tool wins for typography, vector control, and print-ready output.</em></p>\n')
        x['content'] = note + x['content']
        print('canva-ai-review updated')

json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
