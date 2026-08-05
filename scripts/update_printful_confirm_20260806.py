# -*- coding: utf-8 -*-
"""8/6 P0-2: 更新 Printful 状态 — 确认邮件已定位 (7/20, 链接在), 待 user 浏览器点击
纠正此前 'email-unconfirmed' 的误判 (in-house 系统有发确认邮件, 只是脚本窗口 30-Jul 起没查到)。"""
import json, io, datetime

p = r"F:\aitoptools\.hermes\affiliate-programs.json"
with io.open(p, encoding="utf-8") as f:
    d = json.load(f)

progs = d.get("programs", d) if isinstance(d, dict) else d
target = None
if isinstance(progs, list):
    for x in progs:
        if x.get("name", "").lower().startswith("printful"):
            target = x
            break

if target is None:
    print("ERROR: Printful entry not found")
    raise SystemExit(1)

target["verification"] = "confirm-link-located-2026-08-06, pending-user-click"
target["confirm_email_found"] = True
target["confirm_email_date"] = "2026-07-20T17:00:38Z"
target["confirm_email_sender"] = "support@info.printful.com"
target["confirm_email_subject"] = "Confirm email address"
target["confirm_link_note"] = (
    "Link is in Gmail 7/20 17:00 'Confirm email address' (printful.com/verify/0/...?key=...). "
    "Per AGENTS.md §7 user must click manually (Hermes 禁自动点击激活链接). "
    "7/20 发出已 17 天 — 可能已过期, 若 404 则需 Printful 后台重新触发."
)
target["notes"] = target.get("notes", "") + (
    " 8/6 P0-2 修正: 确认邮件并非不存在 — 7/20 17:00 support@info.printful.com 'Confirm email address' 已在 Gmail 定位, "
    "此前 'email-unconfirmed' 是脚本查询窗口 (SINCE 30-Jul) 太窄的误判。链接待 user 手动点击 (或已过期需重发)。"
)
target["last_updated"] = datetime.date.today().isoformat()

with io.open(p, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Printful updated: confirm-link-located-2026-08-06")
print("verification:", target["verification"])
