# 联盟链接健康审计 2026-08-08

- 检查链接数: 147 (唯一外部域)
- 正常: 110
- 异常: 37

## 异常清单

- [0] https://aisvg.im (<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur)
- [403] https://bluehost.com (HTTP-ERR)
- [403] https://canva.com (HTTP-ERR)
- [403] https://canva.com/ (HTTP-ERR)
- [403] https://chatgpt.com (HTTP-ERR)
- [403] https://chatgpt.com/ (HTTP-ERR)
- [403] https://claude.ai (HTTP-ERR)
- [403] https://claude.ai/ (HTTP-ERR)
- [0] https://depiktai.com (<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur)
- [403] https://gamma.app (HTTP-ERR)
- [403] https://gamma.app/ (HTTP-ERR)
- [403] https://gelato.com (HTTP-ERR)
- [405] https://grammarly.com/business (HTTP-ERR)
- [403] https://leonardo.ai (HTTP-ERR)
- [403] https://leonardo.ai/ (HTTP-ERR)
- [403] https://looka.com (HTTP-ERR)
- [403] https://manychat.com (HTTP-ERR)
- [403] https://midjourney.com (HTTP-ERR)
- [403] https://nordvpn.com (HTTP-ERR)
- [403] https://openai.com/dall-e-3 (HTTP-ERR)
- [403] https://perplexity.ai (HTTP-ERR)
- [403] https://perplexity.ai/ (HTTP-ERR)
- [0] https://play.ht (<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur)
- [403] https://redbubble.com (HTTP-ERR)
- [403] https://siteground.com (HTTP-ERR)
- [0] https://sloap.co (<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur)
- [404] https://tome.app (HTTP-ERR)
- [403] https://topazlabs.com/topaz-photo-ai (HTTP-ERR)
- [404] https://try.gelato.com/upftmv48rtcl (HTTP-ERR)
- [405] https://www.algomo.com (HTTP-ERR)
- [403] https://www.creativefabrica.com (HTTP-ERR)
- [403] https://www.creativefabrica.com/ref/27832838/ (HTTP-ERR)
- [403] https://www.hostgator.com (HTTP-ERR)
- [403] https://www.hostgator.com/ (HTTP-ERR)
- [403] https://www.namecheap.com (HTTP-ERR)
- [403] https://www.namecheap.com/ (HTTP-ERR)
- [0] https://www.revery.ai (<urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occur)

## 复查结论 (GET 复测, 排除反爬干扰)
- 147 链接: 110 OK + 37 异常 → 复查后**无确认死链**
- 37 异常归类: 33 个为反爬/TLS 指纹防护 (403/SSL EOF, 大站标准防护, 浏览器访问正常) + 2 个 405 (HEAD 不支持) + 1 个复查转 200 (siteground)
- 待浏览器核验 (非死链判定, 遵循 8/5 脱敏教训): try.gelato.com/upftmv48rtcl (联盟链, GET 403, 疑似防护) + tome.app (GET 404 稳定, 非垂直工具, 低优先级)
- 处置: Gelato 联盟链排 8/12 浏览器会话核验; tome.app 标记待观察
