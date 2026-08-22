# W-8BEN 个人表填写指引（中文逐步 · 2026-08-22）

> 文件：`F:\aitoptools\.hermes\tmp\W8BEN-Jerome-Tang-prefilled.pdf`（IRS 官方个人表，已预填姓名/国籍）
> 为什么换个人表：你上传的是 W-8BEN-**E**（实体表），第 4 项没有 Individual 选项，个人无法正确勾选（OCR 实测确认）。个人经营联盟应用 W-8BEN（个人表）——Printful 接受，Noelle 只要求"能读出来的有效税务表"。

## 已替你填好
- 第 1 行 姓名：`Jerome Tang` ✅
- 第 2 行 国籍：`China` ✅

## 需要你补填（PDF 阅读器打开直接填，如 Edge/Chrome/Adobe）

| 行 | 填什么 | 中文说明 |
|---|---|---|
| 3 | 永久居住地址 | 街道地址 + 城市 + 州/省（香港留空）+ 邮编（香港可留空）+ 国家 `China` |
| 4 | 邮寄地址（若不同） | 与 3 相同则填 Same as 或留空 |
| 5 | 美国税号（SSN/ITIN） | **留空**（中国个人没有） |
| 6 | 外国税号（可选） | 留空或填香港身份证号（非必须） |
| 8 | 出生日期 | 月/日/年 |
| 9 | Chapter 3 Status（必须勾一个） | **勾选写着 `Individual` 的复选框**——个人表这里有 Individual 选项（这就是换表的理由） |
| 11 | 签名（Signature of beneficial owner） | 电子/手写签名 |
| 日期 | Date | 当天日期 |

⚠️ 若第 9 行看到的选项文字不是 Individual（例如只有实体类），把英文选项打字发我。

## 上传（约 3 分钟）

1. <https://www.printful.com/dashboard> → 登录 → **Tax & Legal** → Tax Documents
2. 删除旧的 `autoglm-browser-agent.pdf`
3. 上传 `W8BEN-Jerome-Tang-prefilled.pdf`（文件名可改 `W8BEN-Jerome-Tang.pdf`）
4. 等 Approved（最多 3 个工作日）；完成后告诉我，8/25 仍 Pending 我发第二封跟进

## 备注
- 中美无个人所得税协定优惠，第 10 行税率相关选项不用管（默认不适用）
- 文件在本机 `.hermes/tmp/`（gitignore 覆盖，不提交）；上传用你自己电脑最稳
