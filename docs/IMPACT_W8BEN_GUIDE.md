# Impact W-8BEN-E + Payout 填写指引 (K3 7/30 写)

> **何时填**: user 浏览器登录 https://app.impact.com/ → Settings → Tax Info (W-8BEN-E) + Settings → Payout
> **为何现在填**: Kittl 已获批 7/30, Placeit 待申请, 5 个 approved 商家累计佣金门槛 $10 即可提现, 不填表提不出钱
> **W-8BEN-E**: 美国国税局 (IRS) 表格, 证明非美国税务居民身份. 智印云主体 (深圳公司) 不是美国公司, 必须填.
> **关键提示**: 选错 entity 类型 / Chapter 4 status / TIN 都会卡审批 30 天.

---

## 第 1 步: W-8BEN-E 表单填写

登录 https://app.impact.com/ → 右上角头像 → Settings → Tax Information → Start / Edit

### Line 1: Name of organization
- 填: **深圳市彩龙印刷包装有限公司**
- 英文: **SHEN ZHEN SHI CAI LONG YIN SHUA BAO ZHUANG YOU XIAN GONG SI** (匹配 .hermes/affiliate-programs.json payment_account.beneficiary_name)
- ❌ 错误: 填个人名 (e.g. 唐运提) → 表格类型应该是 W-8BEN (个人), 选错会被 IRS 退回
- ❌ 错误: 填 "ZprintPro" 品牌名 → 不是法定实体名

### Line 2: Country of incorporation
- 选: **China (中国)**
- ⚠️ 如果下拉找不到, 选 "Other countries" → 输入 "China"

### Line 3: Type of entity — ⚠️ 关键
- 选: **Corporation (公司法人)**
- ❌ 不要选: Individual / Sole proprietorship / Partnership / Trust / LLC / Limited partnership
- 理由: 智印云是深圳有限公司 (营业执照 91440300MA5DXXXXXX), 是 Corporation 不是其他类型
- IRS W-8BEN-E 第 2 页有详细 entity 分类, 选错会被 IRS 退回重填

### Line 4a: Chapter 4 Status — ⚠️ 关键
- 选: **Corporation** (不是 NFFE, 不是 Passive NFFE, 不是 Active NFFE)
- 理由: W-8BEN-E 的 Chapter 4 是 FATCA 分类, Corporation 默认就是 Corporation
- ❌ 错误: 选 Active NFFE → 需要额外 GIIN 编号, 没有会卡 30 天审批
- ❌ 错误: 选 Individual → 跟 Line 3 entity 类型冲突

### Line 5: Permanent residence address — ⚠️ 用深圳公司地址
- **Number, street, apt**: 嘉城路 1 号
- **City or town, state or province**: 深圳市龙岗区平湖街道
- **Country**: China
- **Postal code**: **518111**
- ❌ 错误: 填美国地址 (哪怕有仓库/办公室) → IRS 视为美国税务居民, 反要交税
- ❌ 错误: 填香港地址 → 视为 HK 税务居民, 触发 HK 居民申报

### Line 6: U.S. taxpayer identification number (TIN) — ⚠️ 关键
- 填: **91440300MA5DXXXXXX** (中国统一社会信用代码, 18 位)
- ⚠️ 注意: 不是美国 EIN (Employer Identification Number, 9 位 XX-XXXXXXX)
- 智印云没有美国 EIN, 也没有申请 (深圳主体不能直接申请美国 EIN, 要先注册美国分公司)
- IRS 接受中国统一社会信用代码作为外国 TIN (per IRS Notice 2017-46)
- ❌ 错误: 留空 → IRS 视为 incomplete, 退回
- ❌ 错误: 填个人身份证号 → 跟 entity 冲突
- ❌ 错误: 编造 9 位 EIN (e.g. 12-3456789) → IRS 查不到, 30 天后被打回

### Line 7: Foreign tax identifying number (FTIN) — 可选
- 中国公司可填: 91440300MA5DXXXXXX (跟 Line 6 一样)
- 也可以留空, IRS 不强制

### Line 8: Reference number(s) — 可选
- 留空即可

### Line 9a-9c: Mailing address (如果跟 Line 5 不一样) — 选 "Same as Line 5"
- 选: **Same as Permanent Residence Address**

### Line 10: Date of formation
- 填: **2018-XX-XX** (查营业执照上的成立日期)
- 找路径: 营业执照 PDF (F:\zprintpro-credentials\营业执照.pdf 或类似路径)

### Line 11-13: 签字
- 签字人: **唐运提** (法定代表人)
- Title: **法定代表人 / Legal Representative**
- Date: 填表当天

### Part XX Chapter 4 Status (Fatca) — 3 选 1
- 选: **(a) Corporation** (最简单, 智印云是 Corp)
- ❌ 错误: 选 (b) NFFE / Active / Passive → 复杂分类, 选错要补 GIIN

### Part XX Substantial U.S. Owners — 通常 N/A
- 智印云没有美国股东, 选 **N/A** 或留空

### Certify + Submit
- 勾选 "I certify the information above is true and correct"
- 点 Submit → IRS 通常 1-7 天 approve, Impact 同步通过

---

## 第 2 步: Payout (收款方式) 填写

登录 https://app.impact.com/ → Settings → Payment → Add Payment Method

### 选项 A: PayPal (推荐, 最快)
- **Payment type**: PayPal
- **PayPal email**: **zprintpro@outlook.com** (跟 affiliate-programs.json 业务邮箱一致)
- ⚠️ 注意: PayPal 账户必须 verified (中国大陆 PayPal 也能收 affiliate 款, 提现到银行卡)
- 最低提现门槛: **$10** (Kittl/Printify/Printful/Claid/NordVPN 都累积到 $10 自动打)
- 时长: approve 后 30-60 天首打 (Impact 付款周期 NET-30 / NET-60)

### 选项 B: Bank Wire (备选, 适合金额大)
- **Payment type**: International Wire Transfer
- **Bank name**: DBS Bank (Hong Kong) Limited
- **SWIFT/BIC**: DHBKHKHH
- **Account number / IBAN**: 7949835442
- **Routing (ABA)**: 016
- **Beneficiary name**: SHEN ZHEN SHI CAI LONG YIN SHUA BAO ZHUANG YOU XIAN GONG SI
- **Beneficiary address**: Ground Floor, The Center, 99 Queen's Road Central, Central, Hong Kong SAR (DBS HK 地址)
- ⚠️ 注意: 每笔 wire 手续费 $25-35, 低于 $100 不划算
- 时长: approve 后 5-7 工作日 (NET-30 周期)

### ❌ 不推荐: Airwallex 卡支付
- 2026-06-25 永久下线 (深圳主体无法开通 Airwallex 收单, 只能 HK 主体)
- 见 user memory "zprintpro 支付架构硬约束 2026-06-25"

---

## 第 3 步: 提交后验证

填完后 1-2 天回 Impact 后台 → Settings → Tax Information 应该看到:
- Tax Form Status: **Approved**
- Effective Date: 填表日期
- Next Renewal: 3 年后 (W-8BEN-E 有效 3 年, 第 3 年 Q4 要续)

如果 Status = Pending > 7 天 → 升级 user 检查 (可能 Line 3 / Line 4a / Line 6 选错).

---

## 4 个填错最常见的后果 (帮 user 避开)

1. **Line 3 选错 entity** (错选 Individual) → IRS 退回 30 天, 期间累计佣金累积但提不出
2. **Line 6 留空 TIN 或编 EIN** → IRS 视为 incomplete, 退回重填, 1 个月延迟
3. **Line 5 填美国地址** (即使有海外仓) → 视为美国税务居民, 收 30% withholding tax
4. **Payout 填错 PayPal email** (跟品牌邮箱不一致) → PayPal 拒收 → 款退回 Impact → 重新填, 30 天延迟

---

## 验证清单 (填完确认)

- [ ] W-8BEN-E Line 1: 深圳市彩龙印刷包装有限公司 ✓
- [ ] W-8BEN-E Line 2: China ✓
- [ ] W-8BEN-E Line 3: Corporation ✓
- [ ] W-8BEN-E Line 4a: Corporation (Chapter 4) ✓
- [ ] W-8BEN-E Line 5: 嘉城路 1 号 / 深圳市龙岗区 / China / 518111 ✓
- [ ] W-8BEN-E Line 6: 91440300MA5DXXXXXX (中国统一社会信用代码) ✓
- [ ] W-8BEN-E Part XX: Corporation (NFFE 不选) ✓
- [ ] W-8BEN-E Sign: 唐运提 / 法定代表人 / 当天日期 ✓
- [ ] Payout: PayPal 选 zprintpro@outlook.com (推荐) / Wire 选 DBS HK (备选) ✓
- [ ] 提交后 1-2 天回查 Tax Form Status = Approved ✓

---

## 上次失败参考 (避免)

- **2026-06-25 Impact 申请提交时** (zprintpro memory): 卡 11 天, 因 entity 选错 (误选 Sole proprietorship). 后 user 拍板转 HK 主体方案, **最终不开 HK 子公司**, 改 W-8BEN-E Corporation 方案 → 智印云是 Corp 直接填
- **2026-06-25 PayPal 申请时** (zprintpro memory): 商业账户审核中, 用 zprintpro@outlook.com personal PayPal 也能收 affiliate 款, 不需要商业账户升级
- **2026-06-29 CF token 权限坑** (user memory): 当时只给 aitoptools.net zone 权限, Impact 跟域名无关, 这次无影响

---

**预计总耗时**: 10-15 min (user 浏览器操作)
**预计审核时长**: 1-7 天 (IRS W-8BEN-E) + 立即激活 (Payout)
**最关键风险**: 实体类型选错 / TIN 留空 / 填美国地址 → 30 天延迟
