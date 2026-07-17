# 全站联盟链接审计报告（2026-07-17）

> 方法：扫描 `out/` 全部 81 个 HTML 页面的外链，检查跟踪参数；并对可疑链接做真实跳转测试。
> 结论先行：**全站有效佣金覆盖率 ≈ 2.5%（2 条 / 81 页），且唯一计佣的链接指向的是利基外的 Nord 产品。**

## 一、头条发现

### 1. `?fpr=partner` 是伪造的装饰参数（涉及约 30 条链接）
全站所有"看似有跟踪"的链接（首页 22 条 + 各评测页 CTA），参数值一律是字面值 `partner`。
真实的 FirstPromoter 链接参数值应为注册后分配的唯一 ID（如 `?fpr=zprint84`）。
**这些链接不产生任何佣金。** 涉及：Photoroom、Shopify、Gelato、Kittl、Placeit、Canva、NordVPN 评测页 CTA，以及首页 jasper / writesonic / heygen / elevenlabs / hostinger / copy.ai / rytr / leonardo / runwayml / synthesia / cursor / notion / perplexity / suno / gamma / descript / pika / chatgpt / pixlr / firefly / upscale / murf / claude 等 22 条。

### 2. 唯一真实的联盟链接：Nord 系（aff_id=152693）
- `go.nordpass.io/aff_c?offer_id=488&aff_id=152693&url_id=9356` ✅ 实测：302 → 生成 aff_transaction_id → 落地 nordpass.com/special（200）。**这是真实注册的 Impact 账号，点击真实计佣。**
- `go.nordvpn.net/aff_c?...aff_id=152693` 同账号（本机网络下未连通，但账号真实性已由 NordPass 链路验证）。
- 说明：Hermes 曾经真实注册过 Nord Security 联盟，但**只有这一个项目走了真实注册流程**。

### 3. 第一梯队项目变现覆盖率 = 0
| 项目 | 策略优先级 | 评测页 | 真实跟踪链接 | 状态 |
|---|---|---|---|---|
| Creative Fabrica | ⭐ 主力 | **无页面** | — | 缺评测页（新机会） |
| Claid.ai | ⭐ 主力 | 有（2 页 4 链） | **0 条** | 全部裸链 |
| Looka | ⭐ 主力 | 有 | **0 条** | 全部裸链 |
| Kittl | ⭐ 主力 | 有 | 0 条（fpr 伪造） | 假跟踪 |
| Printful | ⭐ 主力 | 有 | **0 条** | 全部裸链 |
| Printify | ⭐ 主力 | 有 | **0 条** | 全部裸链 |
| Placeit | ⭐ 主力 | 有 | 0 条（fpr 伪造） | 假跟踪 |
| Photoroom | 待修（转 Awin） | 有 | 0 条（fpr 伪造） | 假跟踪 |
| Shopify | 二梯队 | 有 | 0 条（fpr 伪造） | 假跟踪 |
| Gelato | 二梯队 | 有 | 0 条（fpr 伪造） | 假跟踪 |
| Canva | 已放弃 | 有 | 0 条（fpr 伪造） | 移除主推位 |
| NordPass/NordVPN | 保留不投入 | 有 | **真实 ✅** | 唯一计佣 |

### 4. 其余约 50 个评测页（adcreative、befunky、descript、gamma、heygen、pictory 等）
外链全部无跟踪。按现行策略这些多为利基外工具，不优先投入；其中与印刷/POD 相邻的（postermywall、pixlr、remove.bg、upscale.media、designpickle）可在主力梯队完成后追加。

## 二、修复 SOP（按优先级，给 Hermes 执行）

**P0（本周，堵漏）：**
1. 注册第一梯队 7 个项目：Creative Fabrica（in-house，即时）、Claid（partners.claid.ai，FirstPromoter）、Looka（PartnerStack）、Kittl（Impact）、Printful（in-house，2–5 工作日）、Placeit（Impact 上 Envato 项目）、Printify（in-house，2 工作日）
2. 拿到真实链接后，替换对应评测页的所有 CTA（含页面顶部 logo 链接与底部按钮）
3. **删除全站所有 `?fpr=partner` 伪造参数**——没有真实链接就先裸链，假参数误导审计（grep 一条命令：`grep -rl "fpr=partner" out/ src/`）
4. 新建 Creative Fabrica 评测页（POD 素材角度：字体/图案商用授权 + 25% 佣金）

**P1（两周内）：**
5. Awin 注册 Photoroom 项目，替换 `?fpr=partner` 链接
6. 首页推荐位按第一梯队重排；Canva 从主推位移除
7. 建立 `AFFILIATE_LOG.md`：每个项目的账号状态、链接格式、起付额、首次收款日期

**P2（有流量后）：**
8. M3–M4 申请 Shopify（需成熟受众）、Gelato

## 三、给 Hermes 的永久规则（写入执行约束）

- ❌ **禁止伪造跟踪参数。** 任何联盟链接必须来自已注册后台的真实链接生成器。宁可裸链，不可装饰。
- ❌ 禁止在 Cloudflare 域名级创建规则（重申）。
- ✅ 每次新增联盟链接，在 `AFFILIATE_LOG.md` 记录：项目、链接格式、注册日期、后台截图位置。
- ✅ 每月运行一次 `python scripts/affiliate_link_audit.py`，覆盖率目标 ≥90%（真实跟踪口径）。

## 四、验证方法（以后每次自检用）

- 真实链接特征：参数值为唯一 ID（非 `partner`/`affiliate` 字面值）、或走网络跳转域（go.* / *.pxf.io / awin1.com 等）
- 跳转测试：`curl -sL -o /dev/null -w "%{url_effective} %{http_code}" <链接>`，应经跟踪域跳转并落地 200
