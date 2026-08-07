# Task Card: halloween_asset_chain_execution (P2, 8/10 10:00 触发)

> 2026-08-08 v2 指令集 P2 · 前置检查: .hermes/assets/cf-halloween-2026-08-07/ 有素材 + printful_session_cookie 或 Printify 可用
> 跟踪器: .hermes/logs/halloween-asset-chain.md (每日 brief 更新)

## 前置检查 (缺任一 → 记 blocked + 给 user 清单, 退出)
- [ ] assets 目录有素材 (CF 下载需 user 登录, 素材源: .hermes/logs/cf-freebies/2026-08-07.md)
- [ ] 下单平台可用: printful_session_cookie 或 Printify 联盟链路
- [ ] test-address.json 存在 (收货地址)

## phases
1. design: Kittl API / browser automation; input assets [0:2]; output .hermes/designs/halloween-test-{date}.png
2. order: Printful (if verified) else Printify; T-shirt/Hoodie; budget $25/order $50/day hard limit; record order_id/eta/cost → halloween-asset-chain.md
3. photo: 由收货 watcher 触发 (logistics delivered); user 拍照 OR fallback 官方 mockup; upload public/photos/wall/halloween-{order_id}.jpg
4. 产出: 照片墙 6 图 + 支柱帖源文件 + 毛利数据

## deadline
- 8/18 23:59 集群上线; 8/11 Kittl 实测日 (素材当源文件, 实测帖初稿)
