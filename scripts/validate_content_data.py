"""
validate_content_data.py
========================
校验 src/data/comparisons.json 与 src/data/listicles.json 是否满足
"三级推荐卡 + 功能对照矩阵 + 定价对比表" 的标准数据结构。

任何新增对比页 / 榜单页在合并到数据文件前都必须通过本校验,
否则视为不合格, 不允许构建 (CI/本地 脚本末尾 exit 1)。

校验规则:

  comparisons.json (head-to-head):
    - picks: 恰好 3 项; type 必须在 {top, also, budget} 且三者齐全不重复
    - features: 7~8 行; 每行 a / b 必须在 {yes, no, partial}
    - pricing.betterValue 必须在 {a, b}; pricing.rows 非空 (含 label, a, b)

  listicles.json (best/榜单):
    - items 中 pickType 恰好出现 1 个 top / 1 个 also / 1 个 budget, 不重复
    - featureCols 长度 = 3 (与 picks 推荐数量对齐)
    - features 每行 values 长度 = len(featureCols); 值必须在 {yes, no, partial}

纯标准库实现, 不引入新依赖。

用法:
    python scripts/validate_content_data.py            # 校验, exit 0/1
    python scripts/validate_content_data.py --quiet    # 只在失败时打印
"""

import json
import os
import sys

# 数据根目录 (脚本在 scripts/, 数据在 src/data/)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMPARISONS = os.path.join(ROOT, 'src', 'data', 'comparisons.json')
LISTICLES = os.path.join(ROOT, 'src', 'data', 'listicles.json')

# 合法的三态取值 (与 FeatureMatrix.js 的 SYMBOLS 保持一致)
VALID_FEATURE_VALUES = {'yes', 'no', 'partial'}
REQUIRED_PICK_TYPES = ['top', 'also', 'budget']

# 标准结构常量 (与 add_*.py 模板保持一致)
PICKS_COUNT = 3
FEATURES_MIN = 7
FEATURES_MAX = 8
LISTICLE_FEATURES_COUNT = 6
LISTICLE_COLS_COUNT = 3


def _load(path, label):
    """读取 JSON 数据文件, 失败时打印错误并退出。"""
    if not os.path.exists(path):
        print(f'[FAIL] 缺少数据文件: {path} ({label})', file=sys.stderr)
        sys.exit(1)
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def _check_picks(entry, slug, errors):
    """校验 picks 字段: 数量、type 齐全不重复。"""
    picks = entry.get('picks')
    if not isinstance(picks, list):
        errors.append(f'{slug}: 缺少 picks 字段 (列表)')
        return
    if len(picks) != PICKS_COUNT:
        errors.append(f'{slug}: picks 数量应为 {PICKS_COUNT}, 实际 {len(picks)}')
        return
    types = []
    for p in picks:
        if not isinstance(p, dict):
            errors.append(f'{slug}: picks 元素应为对象: {p!r}')
            continue
        t = p.get('type')
        types.append(t)
        for field in ('name', 'tagline', 'anchor'):
            if not p.get(field):
                errors.append(f'{slug}: pick 缺少字段 {field}: {p!r}')
        # rating 可选, 但如有则必须为数字
        if 'rating' in p and p['rating'] is not None and not isinstance(p['rating'], (int, float)):
            errors.append(f'{slug}: pick.rating 必须是数字, 实际 {type(p["rating"]).__name__}')
    # type 必须齐全 + 不重复
    missing = [t for t in REQUIRED_PICK_TYPES if t not in types]
    if missing:
        errors.append(f'{slug}: picks 缺少 type {missing}, 现有 {types}')
    if len(set(types)) != len(types):
        from collections import Counter
        dup = [t for t, n in Counter(types).items() if n > 1]
        errors.append(f'{slug}: picks 存在重复 type {dup}, 现有 {types}')


def _check_features(entry, slug, errors):
    """校验 features 字段: 行数 + 每行 a/b 取值。"""
    feats = entry.get('features')
    if not isinstance(feats, list) or not feats:
        errors.append(f'{slug}: 缺少 features 字段 (非空列表)')
        return
    if not (FEATURES_MIN <= len(feats) <= FEATURES_MAX):
        errors.append(f'{slug}: features 行数应为 {FEATURES_MIN}~{FEATURES_MAX}, 实际 {len(feats)}')
    for i, row in enumerate(feats):
        if not isinstance(row, dict) or not row.get('feature'):
            errors.append(f'{slug}: features[{i}] 缺少 feature 字段')
            continue
        for col in ('a', 'b'):
            v = row.get(col)
            if v not in VALID_FEATURE_VALUES:
                errors.append(f'{slug}: features[{i}].{col} 取值 {v!r} 不合法, 应在 {sorted(VALID_FEATURE_VALUES)}')


def _check_pricing(entry, slug, errors):
    """校验 pricing 字段: betterValue + rows。"""
    p = entry.get('pricing')
    if not isinstance(p, dict):
        errors.append(f'{slug}: 缺少 pricing 字段 (对象)')
        return
    bv = p.get('betterValue')
    if bv not in ('a', 'b'):
        errors.append(f'{slug}: pricing.betterValue 应为 a/b, 实际 {bv!r}')
    rows = p.get('rows')
    if not isinstance(rows, list) or not rows:
        errors.append(f'{slug}: pricing.rows 为空')
        return
    for i, r in enumerate(rows):
        if not isinstance(r, dict):
            errors.append(f'{slug}: pricing.rows[{i}] 应为对象')
            continue
        for col in ('label', 'a', 'b'):
            if not r.get(col):
                errors.append(f'{slug}: pricing.rows[{i}] 缺少 {col} 字段')


def _check_listicle_picks(l, slug, errors):
    """校验 listicle.items 中 pickType 恰好 1 个 top/also/budget。"""
    items = l.get('items')
    if not isinstance(items, list) or not items:
        errors.append(f'{slug}: items 字段为空')
        return
    types = [it.get('pickType') for it in items if it.get('pickType')]
    from collections import Counter
    counts = Counter(types)
    for t in REQUIRED_PICK_TYPES:
        n = counts.get(t, 0)
        if n != 1:
            errors.append(f'{slug}: items.pickType 期望恰好 1 个 {t!r}, 实际 {n}')
    for t, n in counts.items():
        if t in REQUIRED_PICK_TYPES and n > 1:
            errors.append(f'{slug}: items.pickType 存在重复 {t!r} ({n} 次)')


def _check_listicle_feature_cols(l, slug, errors):
    """校验 featureCols 长度 = 3。"""
    cols = l.get('featureCols')
    if not isinstance(cols, list) or len(cols) != LISTICLE_COLS_COUNT:
        errors.append(f'{slug}: featureCols 应为长度 {LISTICLE_COLS_COUNT} 的列表, 实际 {cols!r}')


def _check_listicle_features(l, slug, errors):
    """校验 features 行数 + 每行 values 长度 = len(featureCols) + 取值合法。"""
    feats = l.get('features')
    cols = l.get('featureCols') or []
    n_cols = len(cols) if isinstance(cols, list) else 0
    if not isinstance(feats, list) or not feats:
        errors.append(f'{slug}: 缺少 features 字段 (非空列表)')
        return
    if len(feats) != LISTICLE_FEATURES_COUNT:
        errors.append(f'{slug}: features 行数应为 {LISTICLE_FEATURES_COUNT}, 实际 {len(feats)}')
    for i, row in enumerate(feats):
        if not isinstance(row, dict) or not row.get('feature'):
            errors.append(f'{slug}: features[{i}] 缺少 feature 字段')
            continue
        vals = row.get('values')
        if not isinstance(vals, list):
            errors.append(f'{slug}: features[{i}].values 应为列表')
            continue
        if n_cols and len(vals) != n_cols:
            errors.append(
                f'{slug}: features[{i}].values 长度 {len(vals)} 与 featureCols 长度 {n_cols} 不一致'
            )
        for j, v in enumerate(vals):
            if v not in VALID_FEATURE_VALUES:
                errors.append(
                    f'{slug}: features[{i}].values[{j}] 取值 {v!r} 不合法, 应在 {sorted(VALID_FEATURE_VALUES)}'
                )


def validate_comparisons(data):
    """校验 comparisons.json, 返回 (errors, summary)。"""
    errors = []
    rows = []
    for c in data:
        slug = c.get('slug', '<no-slug>')
        _check_picks(c, slug, errors)
        _check_features(c, slug, errors)
        _check_pricing(c, slug, errors)
        rows.append({
            'slug': slug,
            'picks': len(c.get('picks') or []),
            'features': len(c.get('features') or []),
            'pricing_rows': len((c.get('pricing') or {}).get('rows') or []),
        })
    return errors, rows


def validate_listicles(data):
    """校验 listicles.json, 返回 (errors, summary)。"""
    errors = []
    rows = []
    for l in data:
        slug = l.get('slug', '<no-slug>')
        _check_listicle_picks(l, slug, errors)
        _check_listicle_feature_cols(l, slug, errors)
        _check_listicle_features(l, slug, errors)
        items = l.get('items') or []
        from collections import Counter
        pts = Counter(it.get('pickType') for it in items if it.get('pickType'))
        rows.append({
            'slug': slug,
            'items': len(items),
            'pickTypes': dict(pts),
            'featureCols': len(l.get('featureCols') or []),
            'features': len(l.get('features') or []),
        })
    return errors, rows


def main(argv):
    quiet = '--quiet' in argv

    comparisons = _load(COMPARISONS, 'comparisons.json')
    listicles = _load(LISTICLES, 'listicles.json')

    comp_errors, comp_rows = validate_comparisons(comparisons)
    list_errors, list_rows = validate_listicles(listicles)

    all_errors = []
    all_errors.extend([f'[comparison] {e}' for e in comp_errors])
    all_errors.extend([f'[listicle]   {e}' for e in list_errors])

    if not quiet or all_errors:
        print('=' * 64)
        print(f'validate_content_data.py — 标准数据结构校验')
        print('=' * 64)
        print(f'\n[comparisons] {len(comparisons)} 条:')
        for r in comp_rows:
            print(
                f'  - {r["slug"]:<28}  picks={r["picks"]}  features={r["features"]}  pricing_rows={r["pricing_rows"]}'
            )
        print(f'\n[listicles]   {len(listicles)} 篇:')
        for r in list_rows:
            print(
                f'  - {r["slug"]:<28}  items={r["items"]}  pickTypes={r["pickTypes"]}  '
                f'featureCols={r["featureCols"]}  features={r["features"]}'
            )

    if all_errors:
        print('\n[FAIL] 数据结构校验未通过, 请补齐缺失字段后再构建:')
        for e in all_errors:
            print(f'  - {e}')
        print(f'\n共 {len(all_errors)} 项错误。退出码 1。')
        return 1

    print('\n[OK] 全部通过 (5 篇对比 + 2 篇榜单均符合标准模板)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
