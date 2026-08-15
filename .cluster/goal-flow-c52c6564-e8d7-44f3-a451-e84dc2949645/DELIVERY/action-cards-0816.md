# 8/16 User 行动卡清单（中文逐步说明）

> 生成：2026-08-16 05:05 · 依据千问 8/16 指令 + BOARD 待拍板项 + AGENTS.md 铁律（登录/凭证/回填一律 user 操作）
> 总耗时估算：约 15-20 分钟，可分次完成。优先级：D6 > D7 > D5 > 行动卡 1/2/3。

## ⚠️ 操作前须知

- 以下全部需要**你本人**操作（涉及登录账号/邮箱/资金数据），AI 不代操作。
- 涉及英文网站时，下面每步都给了中文翻译，照着点即可。
- 完成后告诉我一声，我会核验并更新台账（幂等键：D6 cookie 文件存在 / D7 token 存在 / D5 数据回填 / 行动卡按邮件-后台核实）。

---

## D6 · 补 printful_session_cookie（最高优先，8/18 判定前）

**用途**：Halloween 素材链下单的唯一阻塞（test-address 已就绪，就差登录态）。

1. 打开 <https://www.printful.com/dashboard>，用你的 Printful 账号登录（邮箱 zprintpro@outlook.com）。
2. 登录成功后，按键盘 **F12** 打开开发者工具 → 点顶部 **Application**（应用）标签 → 左侧展开 **Cookies** → 点 `https://www.printful.com`。
3. 在 Cookie 列表里找到名为 `session` 或 `connect.sid`（通常是 `session`）的那一行，双击 **Value** 列，全选复制整串值。
4. 把值发给我（或自行存到 `F:\aitoptools\.hermes\secrets\printful_session_cookie.txt`，只存值，不带引号）。
5. 我收到后验证可用性，8/18 判定即可 GO。

⚠️ 别复制错：只要 `session`/`connect.sid` 这一个 cookie 的值，不要整个列表。

## D7 · 配 Cloudflare API Token（8/19 GEO 首读数前置）

**用途**：GEO 首读数需要读 CF Analytics（AI 爬虫引荐流量），无 token 则数据拿不到（目前 NODATA）。

1. 打开 <https://dash.cloudflare.com/profile/api-tokens>，登录（域名 aitoptools.net 所在账号）。
2. 点 **Create Token**（创建令牌）→ 选模板 **Read analytics**（读取分析）→ 点 **Continue to summary**（继续）→ 点 **Create Token**。
3. 复制生成的 token（只显示一次），发给我，我存入 `F:\aitoptools\.hermes\secrets\`（gitignore 已覆盖）。
4. 不想配 token 的话，备选方案：8/19 当天你手动登录 CF Dashboard → Analytics 截图/导出给我（需要 5 分钟人工导出）。

## D5 · 回填 3 个经营数据（BOARD 待拍板，5 分钟）

| 数据项 | 说明 | 怎么提供 |
|---|---|---|
| Printful 佣金比例 | 当前 affiliate 计划实际佣金 % | 告诉我数值即可（或截图联盟后台） |
| 月运营成本 | 网站/工具/域名等月度固定支出（$） | 给我一个估算数（如 $30/月） |
| Pinterest 做不做 | 是否投入 Pinterest 渠道（素材已有 11/16） | 回「做 / 不做 / 再议」 |

## 行动卡 1 · Synthesia 邮件确认（2 分钟）

1. 打开邮箱（zprintpro@outlook.com），搜索发件人 **Synthesia** 或主题 **confirm/approval**。
2. 找到申请获批/确认邮件，点正文里的 **Confirm / Activate my account** 按钮（确认激活）。
3. 完成后告诉我，我核验审批状态流转。

## 行动卡 2 · Kittl Impact 数据回填（5 分钟）

1. 打开 Impact 后台（<https://impact.com>），登录账号（Kittl 计划）。
2. 导出/截图 8/1-8/15 的 **Clicks / Conversions / Earnings** 数据（点左侧 Reports → Performance）。
3. 把数字发我（或截图），我更新 Kittl 加投/撤位判定（判定线：≥5 点击/天加投、1-5 维持、<1 撤首页）。

## 行动卡 3 · Printify PartnerStack 站内催（3 分钟）

1. 打开 <https://partners.printify.com>，登录。
2. 进入 **Support / Messages**（支持/消息）→ 新建会话，用英文留言：
   > "Hi, I submitted the $150 blog challenge on Jul 24 and haven't received any response about promo tracking (email #497). Could you confirm if my submission is under review? — Jerome, aitoptools.net"
3. 发送后告诉我，我登记催办时间线（8/14 已收口，此为站内正式催办）。

---

## 核验闭环（我这边做，你无需操作）

- 07:20 自动核验 8/16 主任务是否触发（probe-0720.md）
- 12:30 午间复核（cron 触发/push 次数/402 余额，probe-1230.md）
- 你完成任一行动卡后告诉我，我即时核验并更新 03-risk-log.md / BOARD
