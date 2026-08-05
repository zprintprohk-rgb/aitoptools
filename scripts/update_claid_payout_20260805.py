# -*- coding: utf-8 -*-
"""8/5: 更新 Claid 联盟记录 — 收款链路全通 (PayPal 已绑定, 公司信息已验证)"""
import json, io

p = r"F:\aitoptools\.hermes\affiliate-programs.json"
with io.open(p, encoding="utf-8") as f:
    d = json.load(f)

progs = d.get("programs", d) if isinstance(d, dict) else d
target = None
if isinstance(progs, list):
    for x in progs:
        if x.get("name", "").lower().startswith("claid"):
            target = x
            break
elif isinstance(progs, dict):
    for k, v in progs.items():
        if "claid" in k.lower():
            target = v
            break

if target is None:
    print("ERROR: Claid entry not found")
    raise SystemExit(1)

target["payout_ready"] = True
target["payout_method"] = "PayPal"
target["paypal_email"] = "doolen@126.com"
target["payout_terms"] = "Net-15 monthly, auto-pay at $20+"
target["company_name"] = "Shenzhen Cailong Printing Packaging Co., Ltd."
target["company_number"] = "914403000561993977"
target["vat_id"] = "left-blank (CN credit code fails format check; optional field)"
target["verification"] = "account-fully-configured-2026-08-05"
target["notes"] = ("✅ APPROVED 2026-07-24 (per AGENTS.md §5). 20% recurring lifetime, 60-day cookie, min $20 payout. "
                   "8/5 user completed backend setup: PayPal doolen@126.com bound (Net-15, auto-pay $20+), company info saved "
                   "(Shenzhen Cailong Printing Packaging Co., Ltd. / 914403000561993977), VAT left blank (optional). "
                   "Claid = first affiliate with full payout chain — commissions land directly in PayPal. Link live: https://claid.ai?via=jerome94")

with io.open(p, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Claid updated: payout_ready=True, paypal=" + target["paypal_email"])
