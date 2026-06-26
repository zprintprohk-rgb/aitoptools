"""
Content Generation Log — Print AI Tools
Records evidence of content originality and generation history.
Each generated article creates an entry in the log with:
- timestamp, slug, model used, prompt template, character count
- SHA-256 hash of content for provenance
This log serves as evidence of independent content creation.

Usage:
  python scripts/content-log.py --log <slug>    # Log a new article
  python scripts/content-log.py --verify <slug> # Verify content integrity
  python scripts/content-log.py --report        # Generate generation report
"""
import json, os, sys, hashlib, datetime, argparse

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'content-generation-log.json')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'data')

def load_log():
    if os.path.exists(LOG_PATH):
        return json.load(open(LOG_PATH, 'r', encoding='utf-8'))
    return []

def save_log(log):
    json.dump(log, open(LOG_PATH, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    print(f"  Log saved ({len(log)} entries)")

def content_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def log_article(slug, model="deepseek-v4-flash", template_type="single-review"):
    """Log a newly generated article to the evidence chain."""
    reviews = json.load(open(os.path.join(DATA_DIR, 'reviews.json'), 'r', encoding='utf-8'))
    review = next((r for r in reviews if r['slug'] == slug), None)
    if not review:
        print(f"❌ Review '{slug}' not found in reviews.json")
        return False
    
    content = review.get('content', '')
    entry = {
        'slug': slug,
        'title': review.get('title', ''),
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'model': model,
        'template_type': template_type,
        'char_count': len(content),
        'word_count': len(content.split()),
        'content_sha256': content_hash(content),
        'pros_count': len(review.get('pros', [])),
        'cons_count': len(review.get('cons', [])),
        'category': review.get('category', ''),
        'has_screenshots': 'tool-screenshots' in content or '<img' in content,
        'verified': False,
    }
    
    log = load_log()
    # Remove existing entry for same slug if exists
    log = [e for e in log if e['slug'] != slug]
    log.append(entry)
    save_log(log)
    print(f"✅ Logged: {slug} ({entry['word_count']} words, SHA256: {entry['content_sha256'][:16]}...)")
    return True

def verify_article(slug):
    """Verify content integrity by comparing current hash with logged hash."""
    log = load_log()
    entry = next((e for e in log if e['slug'] == slug), None)
    if not entry:
        print(f"❌ No log entry for '{slug}'")
        return False
    
    reviews = json.load(open(os.path.join(DATA_DIR, 'reviews.json'), 'r', encoding='utf-8'))
    review = next((r for r in reviews if r['slug'] == slug), None)
    if not review:
        print(f"❌ Review '{slug}' not found in reviews.json")
        return False
    
    current_hash = content_hash(review.get('content', ''))
    original_hash = entry['content_sha256']
    
    if current_hash == original_hash:
        print(f"✅ INTEGRITY VERIFIED: {slug}")
        print(f"   Original: {original_hash[:16]}...")
        print(f"   Current:  {current_hash[:16]}...")
        print(f"   Created:  {entry['timestamp']}")
        print(f"   Model:    {entry['model']}")
        print(f"   Words:    {entry['word_count']}")
        entry['verified'] = True
        entry['last_verified'] = datetime.datetime.utcnow().isoformat() + 'Z'
        save_log(log)
        return True
    else:
        print(f"❌ INTEGRITY FAILED: {slug}")
        print(f"   Original: {original_hash[:16]}...")
        print(f"   Current:  {current_hash[:16]}...")
        print(f"   ⚠️  Content has been modified since generation!")
        return False

def generate_report():
    """Generate a full generation evidence report."""
    log = load_log()
    if not log:
        print("No generation log entries found.")
        return
    
    print(f"╔═══ Content Generation Evidence Report ═══╗")
    print(f"  Total articles logged: {len(log)}")
    print(f"  Date range: {log[0]['timestamp'][:10]} to {log[-1]['timestamp'][:10]}")
    print(f"╚═══════════════════════════════════════════╝")
    
    total_words = sum(e['word_count'] for e in log)
    total_chars = sum(e['char_count'] for e in log)
    with_screenshots = sum(1 for e in log if e['has_screenshots'])
    verified = sum(1 for e in log if e.get('verified'))
    
    print(f"\n  📊 STATISTICS")
    print(f"  Total words:    {total_words:,}")
    print(f"  Total chars:    {total_chars:,}")
    print(f"  Avg word count: {total_words//len(log):,}")
    print(f"  With screenshots: {with_screenshots}/{len(log)}")
    print(f"  Integrity verified: {verified}/{len(log)}")
    
    print(f"\n  📋 ARTICLES BY CATEGORY")
    cats = {}
    for e in log:
        cats[e.get('category', 'Unknown')] = cats.get(e.get('category', 'Unknown'), 0) + 1
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat:25s}: {count}")
    
    print(f"\n  📋 FULL LOG")
    for e in sorted(log, key=lambda x: x['timestamp']):
        verified_icon = '🔒' if e.get('verified') else '📝'
        ss_icon = '📸' if e.get('has_screenshots') else '  '
        print(f"  {verified_icon}{ss_icon} {e['slug'][:30]:30s} {e['word_count']:5}w  {e['timestamp'][:19]}")

def main():
    parser = argparse.ArgumentParser(description='Content generation evidence log')
    parser.add_argument('--log', help='Log a new article (provide slug)')
    parser.add_argument('--verify', help='Verify content integrity (provide slug)')
    parser.add_argument('--report', action='store_true', help='Generate generation report')
    parser.add_argument('--model', default='deepseek-v4-flash', help='Model used for generation')
    parser.add_argument('--template', default='single-review', help='Prompt template type')
    args = parser.parse_args()
    
    if args.log:
        log_article(args.log, args.model, args.template)
    elif args.verify:
        verify_article(args.verify)
    elif args.report:
        generate_report()
    else:
        parser.print_help()
        print("\n📋 Logging all published articles for evidence...")
        log = load_log()
        already_logged = {e['slug'] for e in log}
        reviews = json.load(open(os.path.join(DATA_DIR, 'reviews.json'), 'r', encoding='utf-8'))
        count = 0
        for r in reviews:
            if r['slug'] not in already_logged and r.get('content'):
                log_article(r['slug'], args.model, args.template)
                count += 1
        if count == 0:
            print(f"All {len(reviews)} articles already logged. Run --report to view.")

if __name__ == '__main__':
    main()
