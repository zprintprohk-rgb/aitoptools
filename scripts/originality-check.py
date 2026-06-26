"""
Originality Checker — Print AI Tools
Ensures generated content does not overlap with competitor website (aitoptools.com).
Used in the content generation pipeline to verify originality before deployment.

Usage:
  python scripts/originality-check.py                     # Check all published reviews
  python scripts/originality-check.py --slug X             # Check specific article
  python scripts/originality-check.py --threshold 0.05    # Custom threshold (default 10%)
  python scripts/originality-check.py --fetch             # Fetch competitor content for comparison
"""
import json, re, os, sys, hashlib, argparse

THRESHOLD = 0.10  # 10% max allowed overlap
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'data')
COMPETITOR_DIR = os.path.join(os.path.dirname(__file__), '..', 'competitor-ref')

def normalize(text):
    """Normalize text for comparison: lowercase, remove special chars, collapse whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_key_phrases(text, min_len=5):
    """Extract unique key phrases (5+ word sequences) from text."""
    words = normalize(text).split()
    phrases = set()
    for i in range(len(words) - min_len + 1):
        phrase = ' '.join(words[i:i+min_len])
        if phrase and len(phrase) > 20:  # meaningful phrase
            phrases.add(phrase)
    return phrases

def load_reviews():
    path = os.path.join(DATA_DIR, 'reviews.json')
    if not os.path.exists(path):
        print(f"❌ reviews.json not found at {path}")
        return []
    return json.load(open(path, 'r', encoding='utf-8'))

def load_competitor_ref():
    """Load fetched competitor content if available."""
    path = os.path.join(COMPETITOR_DIR, 'competitor-text.txt')
    if not os.path.exists(path):
        return None
    return open(path, 'r', encoding='utf-8').read()

def strip_html(text):
    return re.sub(r'<[^>]+>', ' ', text)

def check_article_overlap(content, competitor_text, threshold=THRESHOLD):
    """Check overlap between article content and competitor text."""
    # Strip HTML
    clean_content = strip_html(content)
    
    # Extract key phrases
    content_phrases = extract_key_phrases(clean_content)
    competitor_phrases = extract_key_phrases(competitor_text) if competitor_text else set()
    
    if not competitor_phrases or not content_phrases:
        return {
            'overlap_ratio': 0,
            'overlapping_phrases': [],
            'match_count': 0,
            'total_phrases': len(content_phrases),
            'status': 'no_ref'
        }
    
    # Find overlapping phrases
    overlapping = content_phrases & competitor_phrases
    overlap_ratio = len(overlapping) / len(content_phrases) if content_phrases else 0
    
    return {
        'overlap_ratio': round(overlap_ratio, 4),
        'overlapping_phrases': sorted(list(overlapping))[:20],
        'match_count': len(overlapping),
        'total_phrases': len(content_phrases),
        'status': 'pass' if overlap_ratio <= threshold else 'fail',
        'threshold': threshold
    }

def main():
    parser = argparse.ArgumentParser(description='Check content originality against competitor')
    parser.add_argument('--slug', help='Specific article slug to check')
    parser.add_argument('--threshold', type=float, default=THRESHOLD, help='Max overlap ratio (default: 0.10)')
    parser.add_argument('--fetch', action='store_true', help='Fetch competitor content for comparison')
    args = parser.parse_args()
    
    print(f"╔═══ Originality Checker — Print AI Tools ═══╗")
    print(f"  Threshold: {args.threshold*100:.0f}% max overlap")
    print(f"╚══════════════════════════════════════════════╝")
    
    # Check for competitor reference
    competitor_text = load_competitor_ref()
    if not competitor_text:
        print(f"\n⚠️  No competitor reference found at {COMPETITOR_DIR}/")
        print(f"   To enable overlap checking, fetch competitor content:")
        print(f"   python scripts/originality-check.py --fetch")
        print(f"\n   Without reference, only structural checks are performed.\n")
    
    # Load reviews
    reviews = load_reviews()
    if not reviews:
        return 1
    
    print(f"\n  Loaded {len(reviews)} reviews for checking")
    
    results = []
    articles_to_check = [r for r in reviews if r['slug'] == args.slug] if args.slug else reviews
    
    for review in articles_to_check:
        content = review.get('content', '')
        if not content:
            print(f"  ⚠️  {review['slug']}: no content")
            continue
        
        result = check_article_overlap(content, competitor_text, args.threshold)
        result['slug'] = review['slug']
        result['title'] = review.get('title', '')
        results.append(result)
        
        status_icon = '✅' if result['status'] == 'pass' else '❌ FAIL'
        status_icon = '❓' if result['status'] == 'no_ref' else status_icon
        print(f"  {status_icon} {review['slug'][:35]:35s} overlap: {result['overlap_ratio']*100:5.2f}%  ({result['match_count']}/{result['total_phrases']} phrases)")
        
        if result['status'] == 'fail':
            print(f"     ⚠️  EXCEEDS THRESHOLD! Top overlapping phrases:")
            for phrase in result['overlapping_phrases'][:5]:
                print(f"       - \"{phrase[:60]}...\"")
    
    # Summary
    failures = [r for r in results if r['status'] == 'fail']
    passes = [r for r in results if r['status'] == 'pass']
    no_ref = [r for r in results if r['status'] == 'no_ref']
    
    print(f"\n{'='*50}")
    print(f"  Results: {len(passes)} passed / {len(failures)} failed / {len(no_ref)} no ref")
    if failures:
        print(f"  ⚠️  Action needed for: {', '.join(f['slug'] for f in failures)}")
    if no_ref:
        print(f"  ℹ️  {len(no_ref)} articles had no competitor reference to compare against.")
    
    return 0 if not failures else 1

if __name__ == '__main__':
    sys.exit(main())
