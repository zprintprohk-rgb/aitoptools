# D17 · Gmail 应用专用密码轮换（P0 安全 · 中文逐步指引 · 5 分钟）

> 背景：旧 app password 在公开仓库历史暴露 18 天（已脱敏 b268b7d，但根治靠轮换）。不换则任何人可从公开历史提取，且 IMAP 联盟审批监控链随时可能被恶意触发改密后中断。
> 用户完成下列步骤后，把新密码告诉我（或直接存到 `F:\aitoptools\.hermes\secrets\gmail_credentials.json`），我立即更新本地凭证并做 IMAP/SMTP 冒烟测试。

## 第一步：删除旧应用专用密码（约 1 分钟）

1. 打开 <https://myaccount.google.com/apppasswords>（若提示登录，用 zprintpro@outlook.com 对应的 Google 账号登录）
2. 页面上会列出已生成的应用专用密码（App passwords）
3. 找到名称含 **AutoClaw** / **IMAP** / **SMTP** / **aitoptools** 的那一条（旧密码用于本项目邮件读写）
4. 点该条右侧的 **垃圾桶图标 / Revoke（撤销）** → 确认删除
5. ⚠️ 删除后旧密码立即失效（这正是我们要的——废掉泄漏的密码）

## 第二步：新建应用专用密码（约 2 分钟）

1. 仍在 <https://myaccount.google.com/apppasswords> 页面
2. 下方 **App name（应用名称）** 输入框 → 填 `AutoClaw IMAP`（或你记得住的名字）
3. 点 **Create（创建）**
4. 弹出 16 位形如 `xxxx xxxx xxxx xxxx` 的密码 → 点 **复制**（只显示一次！）
5. 粘贴发给我，或自己存入 `F:\aitoptools\.hermes\secrets\gmail_credentials.json`（password 字段，不带空格）

## 第三步（我来做，你无需操作）

收到新密码后我执行：
1. 更新 `F:\aitoptools\.hermes\secrets\gmail_credentials.json` 的 password 字段（gitignore 已覆盖，不提交）
2. IMAP 冒烟测试：imap.gmail.com:993 登录 + 读最新 1 封 → 通过则监控链恢复
3. SMTP 冒烟测试：smtp.gmail.com:465 发送测试 → 通过则发信链路恢复（W-8 第二封/Printify 催办不受影响）
4. 更新 AFFILIATE_LOG.md：D17 已闭环（时间 + 新密码指纹前 4 位）
5. BOARD D17 状态 → ✅ 已闭环

## 注意事项

- 若提示「两步验证未开启」无法生成 app password：先到 <https://myaccount.google.com/security> → 开启 **2-Step Verification（两步验证）** → 再回来创建 app password
- 若提示「App passwords 不可用（企业账号限制）」：说明该 Google 账号受组织策略管控，需联系管理员或改用其他邮箱通道——告诉我，我评估替代方案
- 新密码只发本项目会话（webchat），不要发到其他渠道
