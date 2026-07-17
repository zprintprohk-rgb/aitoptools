# 联盟账号注册操作手册（约 20–30 分钟）

> 注册邮箱统一用：**z-printpro@outlook.com**
> 每完成一个，把后台生成的推广链接粘贴到 `AFFILIATE_LINKS.json` 对应键，全部（或部分）完成后通知 Hermes/我运行替换脚本。
> ⚠️ 密码一律存本地密码管理器，不要写进仓库任何文件。

## 申请表通用答案（直接复制，均为如实填写）

**Website URL:** `https://aitoptools.net`

**Describe your website / business:**
> Print AI Tools (aitoptools.net) is a review site covering AI tools for print-on-demand sellers, print shops, and independent e-commerce store owners. We publish hands-on reviews, side-by-side comparisons, and pricing guides.

**How will you promote / promotional methods:**
> Organic SEO content (in-depth reviews, comparisons, tutorials) targeting high-intent niche keywords, plus a newsletter for print shop owners, Pinterest pins, and genuine participation in POD communities (Reddit r/printondemand).

**Monthly traffic (如被问到):**
> New site launched in 2026, currently growing organic traffic. We focus on high-intent niche queries rather than volume.

**Country / tax info:** 按业主实际情况填写。

---

## 第一批（今天做，4 个，全部即时或快速通过）

### 1. Creative Fabrica — ⭐ 最优先（佣金 25% + 续费 20%，$10 起付）
1. 打开 https://www.creativefabrica.com/affiliates/
2. 用 z-printpro@outlook.com 注册账号 → 后台直接有推广链接，无需等待审批
3. 复制你的 referral link → 粘贴到 `AFFILIATE_LINKS.json` 的 `"creativefabrica.com"`

### 2. Claid.ai（20% 终身循环，60 天 cookie，$20 起付）
1. 打开 https://partners.claid.ai/ （FirstPromoter 平台）
2. Sign up → 用 z-printpro@outlook.com → 验证邮箱
3. Dashboard → Links → 复制默认推广链接（形如 `https://claid.ai/?fpr=你的ID`）→ 粘贴到 `"claid.ai"`

### 3. Printify（销售额 5%×12 月，90 天 cookie）
1. 打开 https://printify.com/affiliate/ → Apply
2. 用上面通用答案填表；审核约 2 个工作日
3. 通过后从 Affiliate Dashboard 复制链接 → `"printify.com"`

### 4. Printful（10%×12 月 + Growth $25，$25 起付）
1. 打开 https://www.printful.com/affiliates → Apply
2. 人工审核 2–5 个工作日
3. 通过后复制链接 → `"printful.com"`

## 第二批（本周内，3 个）

### 5. Looka（25–35% 终身循环，90 天 cookie，$0 起付）
1. https://looka.com/affiliate-program/ → 注册（PartnerStack）
2. 注意：禁品牌词 PPC、禁优惠券站、每 3 个月至少 1 个新客
3. 链接 → `"looka.com"`

### 6. Kittl（前 12 个月 20%）
1. https://www.kittl.com/partners/affiliates → 跳转 Impact 申请
2. **捷径：Kittl 在 Impact 上。Nord 联盟账号（aff_id=152693）也在 Impact——如果 Hermes 保存着那个 Impact 登录，直接在账号内搜 "Kittl" 加项目，无需新邮箱验证**
3. 链接 → `"kittl.com"`

### 7. Placeit / Envato（年付 $50 / 月付 $20，90 天 cookie）
1. https://placeit.net/affiliate-program → 同样走 Impact（Envato 三个项目在一起，可同时加 Envato Elements）
2. 同样可复用 Nord 的 Impact 账号
3. 链接 → `"placeit.net"`

## 暂缓（按计划 M3+ 再做）

- **Photoroom**：走 Awin（商户 #121800），替换现有失效 `?fpr=partner` 链接——P1，下周做
- **Shopify / Gelato**：要求"成熟受众"，有流量后再申请
- **Canva**：大使制已关闭，不申请

## 完成后（交回给 Hermes/我）

1. 确认 `AFFILIATE_LINKS.json` 已填入链接（有几个填几个，不齐也可以先跑）
2. 运行：`python scripts/replace_affiliate_links.py --apply`
3. `npm run build` → git 提交推送 → 自动部署
4. 运行 `python scripts/affiliate_link_audit.py` 验证真实跟踪覆盖率 ≥90%
5. 在 `AFFILIATE_LOG.md` 记录每个项目：注册日期、链接格式、起付额
