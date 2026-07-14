import json

with open('/mnt/f/aitoptools/.hermes/logs/hn_trends.json') as f:
    data = json.load(f)

keywords = ['ai','gpt','llm','tool','print','design','image','photo','video','generate','model','launch','stable diffusion','midjourney','canva','adobe']
for t in data:
    title = t.get('title','')
    url = t.get('url','')
    tl = title.lower()
    if any(k in tl for k in keywords):
        print(title)
        print(f'  {url}')
        print()
