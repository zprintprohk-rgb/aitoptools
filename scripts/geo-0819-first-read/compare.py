import re
base, cur = {}, {}
for line in open("F:/aitoptools/.hermes/tmp/geo-0819-gsc-full.tsv", encoding="utf-8"):
    line = line.rstrip("\n")
    if not line or line.startswith("#"): continue
    parts = line.split("\t")
    if len(parts) != 5: continue
    tag, k = parts[0], parts[1]
    imp = int(re.search(r"imp=(\d+)", parts[2]).group(1))
    pos = float(re.search(r"pos=([\d.]+)", parts[4]).group(1))
    (base if tag == "BASE" else cur)[k] = (imp, pos)
rows = []
for k in set(base) | set(cur):
    b, c = base.get(k), cur.get(k)
    if not b or not c: continue
    rows.append((k, b[0], b[1], c[0], c[1], c[1] - b[1]))
rows.sort(key=lambda r: (r[5], -r[3]))
print("=== 位置改善 TOP 12 (d=cur-base, 负=改善) ===")
for r in rows[:12]:
    print("%-55s base imp=%3d pos=%5.1f | cur imp=%3d pos=%5.1f | d=%+5.1f" % (r[0][:55], r[1], r[2], r[3], r[4], r[5]))
print("=== 位置下滑 TOP 10 ===")
for r in rows[-10:][::-1]:
    print("%-55s base imp=%3d pos=%5.1f | cur imp=%3d pos=%5.1f | d=%+5.1f" % (r[0][:55], r[1], r[2], r[3], r[4], r[5]))
print("=== 总览 ===")
print("base queries=%d cur queries=%d overlap=%d" % (len(base), len(cur), len(rows)))
tot_b = sum(v[0] for v in base.values()); tot_c = sum(v[0] for v in cur.values())
print("base total imps=%d cur total imps=%d d=%+d" % (tot_b, tot_c, tot_c - tot_b))
