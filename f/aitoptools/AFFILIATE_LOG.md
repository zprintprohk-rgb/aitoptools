# AFFILIATE_LOG.md — aitoptools.net 联盟项目状态

> 位置：`src/data/` 目录下由 JSON 引用，组件渲染。
> 更新规则：每次新增/修改联盟链接，在此记录。

## ✅ 已注册（可计佣）

| 项目 | 平台 | 链接格式 | 注册日期 | 状态 | 备注 |
|------|------|----------|----------|------|------|
| NordVPN | Impact | `go.nordvpn.net/aff_c?offer_id=...&aff_id=152693&url_id=...` | — | ✅ 活跃 | 唯一真实计佣链接 |
| NordPass | Impact | `go.nordpass.io/aff_c?offer_id=488&aff_id=152693&url_id=9356` | — | ✅ 活跃 | 已验证 302 跳转计佣 |

## 🔄 待注册（P0 — 本周）

| 项目 | 平台 | 注册链接 | 预计时效 | 状态 |
|------|------|----------|----------|------|
| Creative Fabrica | In-house | creativefabrica.com/affiliates | 即时 | ⏳ |
| Claid.ai | FirstPromoter | partners.claid.ai | — | ⏳ |
| Looka | PartnerStack | looka.com/partners | — | ⏳ |
| Kittl | Impact | — | — | ⏳ |
| Printful | In-house | printful.com/affiliates | 25 工作日 | ⏳ |
| Printify | In-house | printify.com/affiliates | 2 工作日 | ⏳ |
| Placeit | Impact (Envato) | — | — | ⏳ |

## 🔄 待注册（P1 — 两周内）

| 项目 | 平台 | 备注 |
|------|------|------|
| Photoroom | Awin | 替换当前 `?fpr=partner` 假跟踪 |
| Shopify | Shopfy Affiliates | 需成熟受众 |
| Gelato | Gelato Affiliates | 需成熟受众 |

## ❌ 已放弃 / 不推荐

| 项目 | 原因 |
|------|------|
| Canva | 无联盟计划 / 佣金低，已从主推位移除 |

## 全站链接策略

- **禁止**使用 `?fpr=partner` 等假跟踪参数
- **原则**：宁可裸链（plain URL），不可装饰假参数
- **真实链接特征**：参数值为唯一 ID，或走跟踪域（`go.*` / `*.pxf.io` / `awin1.com` 等）
- **验证命令**：`curl -sL -o /dev/null -w "%{url_effective} %{http_code}" <链接>` → 应经跟踪域跳转并落地 200
