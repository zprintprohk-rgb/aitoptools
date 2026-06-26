"""
Weekly Self-Audit — Print AI Tools Differentiation Compliance
Run every Monday. Checks content alignment with vertical differentiation strategy.

Usage:
  python scripts/weekly-audit.py                    # Full audit
  python scripts/weekly-audit.py --report           # Generate report only
  python scripts/weekly-audit.py --phase 1          # Audit against specific phase rules
"""
import json, os, sys, re, argparse
from datetime import datetime, timezone

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'data')
LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'content-generation-log.json')
SITE_LAUNCH = datetime(2026, 6, 26, tzinfo=timezone.utc)

def get_current_phase():
    """Determine expansion phase based on months since launch."""
    now = datetime.now(timezone.utc)
    months = (now.year - SITE_LAUNCH.year) * 12 + (now.month - SITE_LAUNCH.month)
    if months < 0: return 0  # pre-launch
    if months <= 3: return 1
    if months <= 8: return 2
    return 3

# Phase keyword requirements
PHASE_KEYWORDS = {
    1: {
        'required_keywords': [
            'print', 'packaging', 'pod', 'print-on-demand', 'shopify',
            'ecommerce', 'e-commerce', 'cross-border', 'product photography',
            'product description', 'mockup'
        ],
        'forbidden_keywords': [
            'best ai tools', 'top ai tools', 'ai tools 2026', 'ai directory',
        ],
        'required_sections': ['for.*(?:print|pod|seller|shop|ecom)', '(?:not|not )friendly for'],
        'max_generic_ratio': 0.0,  # 0% generic in phase 1
    },
    2: {
        'required_keywords': ['print', 'shopify', 'store', 'seller', 'business'],
        'forbidden_keywords': ['best ai tools', 'top ai tools'],
        'required_sections': ['for (?:print|shop|ecom|seller)', 'roi', 'cost'],
        'max_generic_ratio': 0.40,  # max 40% non-core content
    },
    3: {
        'required_keywords': ['print', 'cmyk', 'bleed', 'die.?cut', 'color management'],
        'forbidden_keywords': [],
        'required_sections': ['cmyk', 'bleed', 'die.?cut', 'compliance', 'pre.?press'],
        'max_generic_ratio': 0.30,
    }
}

def load_reviews():
    path = os.path.join(DATA_DIR, 'reviews.json')
    return json.load(open(path, 'r', encoding='utf-8')) if os.path.exists(path) else []

def load_log():
    return json.load(open(LOG_PATH, 'r', encoding='utf-8')) if os.path.exists(LOG_PATH) else []

def check_keyword_in_text(text, keywords):
    """Check if any of the keywords appear in text."""
    text_lower = text.lower()
    found = []
    for kw in keywords:
        if kw.lower() in text_lower:
            found.append(kw)
    return found

def check_section_exists(text, patterns):
    """Check if any required section pattern exists."""
    for pat in patterns:
        if re.search(pat, text, re.I):
            return True
    return False

def run_audit(phase=None):
    if phase is None:
        phase = get_current_phase()
    
    rules = PHASE_KEYWORDS.get(phase, PHASE_KEYWORDS[1])
    reviews = load_reviews()
    log = load_log()
    
    print(f"╔═══ Print AI Tools — Weekly Differentiation Audit ═══╗")
    print(f"  Phase: {phase} (Months {['','1-3','4-8','9+'][phase]})")
    print(f"  Reviews: {len(reviews)} total | Logged: {len(log)}")
    print(f"  Date:    {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"╚══════════════════════════════════════════════════════╝")
    
    results = {
        'total': len(reviews),
        'keyword_pass': 0,
        'keyword_fail': 0,
        'section_pass': 0,
        'section_fail': 0,
        'generic_flag': 0,
        'forbidden_found': [],
        'no_log': [],
    }
    
    print(f"\n📋 ARTICLE-BY-ARTICLE CHECK")
    print(f"{'─'*70}")
    
    for review in reviews:
        slug = review['slug']
        title = review.get('title', '')
        content = review.get('content', '')
        combined = f"{title} {content}"
        
        errors = []
        
        # 1. Check required vertical keywords
        found_kws = check_keyword_in_text(combined, rules['required_keywords'])
        if found_kws:
            results['keyword_pass'] += 1
        else:
            results['keyword_fail'] += 1
            errors.append("NO VERTICAL KEYWORDS")
        
        # 2. Check forbidden broad keywords
        found_forbidden = check_keyword_in_text(combined, rules['forbidden_keywords'])
        if found_forbidden:
            results['generic_flag'] += 1
            results['forbidden_found'].append((slug, found_forbidden))
            errors.append(f"BROAD KEYWORD: {found_forbidden}")
        
        # 3. Check required sections
        has_section = check_section_exists(combined, rules['required_sections'])
        if has_section:
            results['section_pass'] += 1
        else:
            results['section_fail'] += 1
            errors.append(f"MISSING SECTION: {rules['required_sections'][:2]}")
        
        # 4. Check evidence log
        log_entry = next((e for e in log if e['slug'] == slug), None)
        if not log_entry:
            results['no_log'].append(slug)
        
        # Print status
        if errors:
            print(f"  ⚠️  {slug[:35]:35s} | {'; '.join(errors)}")
        else:
            kws_str = ', '.join(found_kws[:2])
            print(f"  ✅ {slug[:35]:35s} | {kws_str}")
    
    # Summary
    print(f"\n{'='*70}")
    print(f"  RESULTS SUMMARY")
    print(f"{'─'*70}")
    print(f"  ✅ Keyword compliance:  {results['keyword_pass']}/{results['total']}")
    print(f"  ❌ Missing keywords:    {results['keyword_fail']}/{results['total']}")
    print(f"  ✅ Required sections:   {results['section_pass']}/{results['total']}")
    print(f"  ❌ Missing sections:    {results['section_fail']}/{results['total']}")
    print(f"  ⚠️  Broad keywords used: {results['generic_flag']}/{results['total']}")
    print(f"  📝 Not in evidence log: {len(results['no_log'])}")
    
    if results['forbidden_found']:
        print(f"\n  ⚠️  FORBIDDEN KEYWORDS FOUND:")
        for slug, kws in results['forbidden_found']:
            print(f"     {slug}: {', '.join(kws)}")
    
    if results['no_log']:
        print(f"\n  ⚠️  NOT LOGGED (run python scripts/content-log.py):")
        for slug in results['no_log']:
            print(f"     - {slug}")
    
    # Phase recommendation
    print(f"\n  💡 PHASE {phase} RECOMMENDATION:")
    if phase == 1:
        print(f"     Continue 100% vertical focus. Next vertical tool to review:")
        print(f"     Check tool-params.json for 'pending' tools with 'vertical' field.")
    elif phase == 2:
        print(f"     Maintain 60%+ core vertical. New content must bind seller scenario.")
    else:
        print(f"     Add blue ocean deep content. Include CMYK/bleed/die-cut details.")
    
    # Overall pass/fail
    total_issues = results['keyword_fail'] + results['section_fail'] + results['generic_flag']
    if total_issues == 0:
        print(f"\n  ✅✅✅ ALL CHECKS PASSED — Course correct!")
    elif total_issues <= 2:
        print(f"\n  ⚠️  {total_issues} minor issues found — address in next content batch.")
    else:
        print(f"\n  ❌❌❌ {total_issues} issues found — review content direction!")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Weekly differentiation audit')
    parser.add_argument('--report', action='store_true', help='Generate report only')
    parser.add_argument('--phase', type=int, choices=[1, 2, 3], help='Override phase')
    args = parser.parse_args()
    
    phase = args.phase if args.phase else get_current_phase()
    current_phase = get_current_phase()
    
    print(f"Current phase: {current_phase} | Audit phase: {phase}")
    
    run_audit(phase)

if __name__ == '__main__':
    main()
