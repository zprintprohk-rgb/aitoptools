"""Generate TSX review page components for 10 tools"""
import json, os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
log_dir = "/mnt/f/aitoptools/.hermes/logs"

tools = json.load(open(f"{log_dir}/{today}-新工具入库.json"))

# Generate each TSX file
count = 0
for tool in tools:
    s = tool['slug']
    n = tool['name']
    c = tool['category']
    p = tool['pricing']
    v = tool['visit_url']
    
    # Build per-tool content from a function
    tsx = generate_tsx(s, n, c, p, v)
    if tsx is None:
        print(f"  SKIP {s}")
        continue
    
    out = f"{log_dir}/{today}-长尾-{s}.tsx"
    with open(out, 'w', encoding='utf-8') as f:
        f.write(tsx)
    print(f"  OK {s}")
    count += 1

print(f"\nGenerated {count} TSX files")
