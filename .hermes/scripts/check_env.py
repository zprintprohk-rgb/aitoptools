"""Check Python environment"""
import sys
print(f"Python {sys.version}")
for mod in ['json', 'requests', 're']:
    try:
        __import__(mod)
        print(f"{mod}: OK")
    except ImportError:
        print(f"{mod}: MISSING")
