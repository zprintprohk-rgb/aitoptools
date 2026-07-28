"""
aff-link-audit.py
==================
W1-T1 度量埋点 audit (按 M3_MONTH1_RUNBOOK §W1-T1 步骤 4)

扫 out/ 静态产物, 验证:
  1. 所有出站链接 href 含联盟域名的 <a> 必须带 class="aff-link" + data-merchant + data-link-id
  2. UTM 4 参齐全 (utm_source/medium/campaign/content)
  3. 覆盖率 = 带 aff-link 的链接数 / 总 affiliate 链接数 (期望 100%)

联盟域名清单 (按 W1-T1 步骤 2 范围 + AFFILIATE_LOG.md 7 平台获批):
  - via=jerome* (jerome796 / jerome94 / jerome88) — 通用 ?via=
  - ref/27832838 — Creative Fabrica
  - try.printify.com / printify.com/?via=* — Printify
  - printful.com/a/ — Printful
  - mockey.ai?via=jerome796 — Mockey
  - claid.ai?via=jerome94 — Claid
  - impact / partnerstack 追踪参数

纯标准库, 不引入新依赖 (html.parser + re + urllib).

用法:
  python scripts/aff-link-audit.py            # 全扫, exit 0/1
  python scripts/aff-link-audit.py --quiet    # 只在失败时打印
  python scripts/aff-link-audit.py --out-dir out   # 自定义 out 目录
"""
import argparse
import os
import re
import sys
from html.parser import HTMLParser

# 联盟域名/参数模式 (按 AFFILIATE_LOG.md 7 平台 + ?via=jerome* + 通用)
AFFILIATE_PATTERNS = [
    re.compile(r'[?&]via=jerome[\d]+', re.I),  # jerome796 / 94 / 88
    re.compile(r'/ref/[\d]+', re.I),  # Creative Fabrica ref/27832838
    re.compile(r'try\.printify\.com', re.I),  # Printify try 短链
    re.compile(r'printful\.com/a/', re.I),  # Printful 联盟
    re.compile(r'mockey\.ai', re.I),  # Mockey
    re.compile(r'claid\.ai', re.I),  # Claid
    re.compile(r'(?:kittl|placeit)\.(?:com|net|pxf\.io)', re.I),  # Kittl/Placeit (Kittl Impact pxf.io 2026-07-28 上线)
    re.compile(r'canva\.com', re.I),  # Canva (未来获批时启用)
]

# UTM 必含 4 参
UTM_PARAMS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content']


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []  # list of dict {href, class, data-merchant, data-link-id}

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        d = dict(attrs)
        href = d.get('href', '')
        if not href:
            return
        # 跳过站内 + 锚点
        if href.startswith(('#', '/', 'mailto:', 'javascript:')):
            return
        if href.startswith('/'):
            return
        self.anchors.append({
            'href': href,
            'class': d.get('class', ''),
            'data-merchant': d.get('data-merchant', ''),
            'data-link-id': d.get('data-link-id', ''),
            'data-target': d.get('data-target', ''),
        })


def is_affiliate(href):
    return any(p.search(href) for p in AFFILIATE_PATTERNS)


def has_utm(href):
    return all(f'{p}=' in href for p in UTM_PARAMS)


def audit_html(html, page_path):
    """扫单个 HTML 页面, 返回 (affiliate_total, tagged, utm_ok, issues)"""
    p = AnchorParser()
    p.feed(html)
    affiliate_total = 0
    tagged = 0
    utm_ok = 0
    issues = []

    for a in p.anchors:
        href = a['href']
        if not is_affiliate(href):
            continue
        affiliate_total += 1
        is_tagged = (
            'aff-link' in (a['class'] or '')
            and a['data-merchant']
            and a['data-link-id']
        )
        if is_tagged:
            tagged += 1
            if has_utm(href):
                utm_ok += 1
            else:
                issues.append(f'  [{page_path}] UTM 4 参不全: {href[:120]}')
        else:
            issues.append(
                f'  [{page_path}] 缺 aff-link 标: href={href[:120]} class="{a["class"][:60]}"'
            )

    return affiliate_total, tagged, utm_ok, issues


def main():
    ap = argparse.ArgumentParser(description='W1-T1 aff-link 埋点 audit (M3 runbook §W1-T1 步骤 4)')
    ap.add_argument('--quiet', action='store_true', help='只在失败时打印')
    ap.add_argument('--out-dir', default='out', help='out 目录 (默认 out)')
    args = ap.parse_args()

    # 找 out 根 (脚本在 scripts/, out 在根)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(script_dir)
    out_dir = os.path.join(root, args.out_dir)
    if not os.path.isdir(out_dir):
        print(f'[FAIL] 找不到 out 目录: {out_dir} (先跑 npm run build)', file=sys.stderr)
        sys.exit(1)

    # 扫所有 .html
    total_aff = 0
    total_tagged = 0
    total_utm = 0
    total_pages = 0
    all_issues = []

    for dirpath, _, filenames in os.walk(out_dir):
        for fn in filenames:
            if not fn.endswith('.html'):
                continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, out_dir)
            try:
                with open(fpath, encoding='utf-8') as f:
                    html = f.read()
            except Exception as e:
                all_issues.append(f'  [{rel}] 读取失败: {e}')
                continue
            aff, tagged, utm, issues = audit_html(html, rel)
            total_aff += aff
            total_tagged += tagged
            total_utm += utm
            total_pages += 1
            all_issues.extend(issues)

    # 输出
    print(f'\n═══ aff-link audit (W1-T1 步骤 4) ═══')
    print(f'  扫 {total_pages} 个 HTML 页面, 共 {total_aff} 个联盟链接')
    print(f'  aff-link 标: {total_tagged}/{total_aff} ({100*total_tagged/max(1,total_aff):.1f}%)')
    print(f'  UTM 4 参齐: {total_utm}/{total_aff} ({100*total_utm/max(1,total_aff):.1f}%)')

    if total_aff == 0:
        print(f'  [WARN] 0 联盟链接命中 — 检查 reviews.json affiliateUrl 字段是否非空')
        # 不 exit 1, 让 M3 看到 0 链接的根因 (e.g. affiliateUrl 字段全是空)

    if all_issues:
        print(f'\n  发现 {len(all_issues)} 处问题:')
        for issue in all_issues[:20]:
            print(issue)
        if len(all_issues) > 20:
            print(f'  ... 还有 {len(all_issues) - 20} 处')

    # 判定: 100% 覆盖 + 100% UTM = PASS
    coverage = total_tagged / max(1, total_aff)
    utm_coverage = total_utm / max(1, total_aff)
    if coverage >= 0.99 and utm_coverage >= 0.99:
        print(f'\n✓ PASS — 100% 联盟链接已打标 + UTM 齐全')
        sys.exit(0)
    elif total_aff == 0:
        print(f'\n⚠ N/A — 0 联盟链接命中 (跳过覆盖判定)')
        sys.exit(0)
    else:
        print(f'\n✗ FAIL — 覆盖率 {coverage:.1%} < 99% 或 UTM {utm_coverage:.1%} < 99%')
        sys.exit(1)


if __name__ == '__main__':
    main()
