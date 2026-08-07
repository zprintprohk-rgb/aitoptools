# -*- coding: utf-8 -*-
"""AutoClaw gsc-mining-daily 2026-08-08: 同步 IndexNow 状态文件 + 追加 mining 运行记录 (只追加, 不覆盖)"""
import json, datetime, hashlib, os, sys

BASE = r"F:\aitoptools"
STATE = os.path.join(BASE, r".hermes\logs\gsc-indexnow-state.json")
QUEUE = os.path.join(BASE, r".hermes\logs\gsc-mining-queue.md")
SITEMAP = os.path.join(BASE, r"public\sitemap.xml")

now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# --- Step 0: 状态文件同步 (Hermes 00:21 已推送, 本 run 不重复推送) ---
st = os.stat(SITEMAP)
h = hashlib.sha256(open(SITEMAP, "rb").read()).hexdigest().upper()
mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%dT%H:%M:%S")

with open(STATE, "r", encoding="utf-8") as f:
    state = json.load(f)

state["last_seen"]["public/sitemap.xml"] = {
    "mtime": mtime, "bytes": st.st_size, "sha256": h
}
state["last_run"] = now
state["last_run_status"] = ("autoclaw 2026-08-08 复查: no-new-urls (Hermes 00:21 已推 6 blog 6/6 200, "
                            "sitemap 338 URL), gsc-pending(oauth missing), "
                            "mining=static-fallback no-qualifying, boost=existing-row-only")
state["indexnow_submitted"] = True
state["gsc_submitted"] = False
# 当前 sitemap 全部 URL 已覆盖推送 (8/6 全量 332 + 8/8 增量 6), 记录基线
state["last_submitted_mtime"] = mtime
state["last_submitted_hash"] = h
state["last_check_hash_match"] = True

with open(STATE, "w", encoding="utf-8", newline="\n") as f:
    json.dump(state, f, ensure_ascii=False, indent=1)
    f.write("\n")
print("STATE OK:", h, mtime, st.st_size)

# --- Step 1/2: gsc-mining-queue.md 追加运行记录 (AUTOCLAW_PRIMARY) ---
entry = (
    "\n## 2026-08-08 运行记录 (AUTOCLAW_PRIMARY)\n"
    "- Step 0 IndexNow: Hermes 00:21-00:23 已完成 (commit 75c4c88) — sitemap 338 URL 修复 + 6 blog 增量推送 6/6 HTTP 200; AFFILIATE_LOG.md C2b 8/8 行已记; 本次复查无新增 URL, 不重复推送; 状态文件已同步基线。\n"
    "- Step 1 mining: 数据源=③ keywords-200.csv 静态兜底 (gsc-oauth.json 缺失, gsc_data.csv 缺失); 静态表无 展示/CTR 指标 → 无 query 满足 展示≥10 且 CTR<0.05 → Data-Driven Queue 无新增。\n"
    "- Step 2 boosting: 无 GSC 排名数据; /blog/print-price-ai-tools-2026/ Boost Queue 行已存在 (2026-08-07, in-progress, 8/21 目标 ≤30), 无新增登记。\n"
    "- Daily brief: .hermes/logs/2026-08-08-cron.md 不存在 → 未写入 GSC Opportunities 段。\n"
    "- 凭证缺口: .hermes/secrets/gsc-oauth.json 缺失 (仅 template) — 补录后解锁真实 GSC mining。\n"
)
with open(QUEUE, "a", encoding="utf-8", newline="\n") as f:
    f.write(entry)
print("QUEUE APPEND OK")

# --- 约束: IndexNow 推送前 py_compile (本 run 未推送, 仅例行校验) ---
import py_compile
py_compile.compile(os.path.join(BASE, r"scripts\submit_indexnow_blog_20260808.py"), doraise=True)
print("PY_COMPILE OK")
