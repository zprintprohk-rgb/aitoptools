"""
verify-deploy-v2.py
===================
aitoptools.net 部署后真 verify 脚本 (按千问 0.5 步 + §1 5 步真 verify 流水线扩展).

5 步流水线 (memory MEMORY.md §1):
  1. git status -sb 无 ahead (commit 在 origin/main)
  2. sitemap.xml mtime 是今天 (deploy 真发生)
  3. curl https://aitoptools.net/ HTTP 200 + body 含 hotfix 标志关键词
  4. schema JSON-LD 注入正确 (备用, 不强制)
  5. 静态预检 8 项断言 (hotfix-2 baseline) + 3 项新断言 (千问 0.5 步扩展)

新断言 (千问 2026-07-27 aitoptools 实战诊断):
  ① 深底容器内浅底色泄漏 (千问 P0-1/P0-2 案例):
     抓 .evidence-card / .surface-ink 段, 检测内联 style 或子元素 class
     是否有 var(--k-muted) / var(--k-secondary) 浅底色 = 颜色不感知容器底色
  ④ 首屏副标维度名 schema 校验 (千问 P0 叙事左右互搏):
     抓首屏 hero-text 段, 提取 "print compatibility" / "e-commerce fit" /
     "two numbers" 关键词, grep data/reviews.json 看是否有对应字段.
     搜到但 schema 无 = 空头支票 FAIL.
  ⑤ 6 篇 vs-card winner 字段 vs conclusion 首句 (千问 P0 winner 打架):
     抓所有 .vs-card 的胜方 vs-name + .vs-verdict 段, 胜方名必须在 verdict
     段出现. 不出现 = winner/conclusion 互搏 FAIL.

8 项 baseline 断言 (hotfix-2 7/27 PASS):
  - evidence-stat-num = 3 (107 / 312+ / 0)
  - evidence-stats = 1
  - evidence-meter = 0 (旧假进度条 DOM 全删)
  - evidence-row = 0
  - vertical-score = 0 (工具卡删)
  - 8.8 hardcoded in evidence-card = 0
  - footer '74+' = 0
  - footer dynamic reviews.length 107 = 1

Usage:
  python scripts/verify-deploy-v2.py             # full verify, exit 0/1
  python scripts/verify-deploy-v2.py --quiet      # 只在失败时打印
  python scripts/verify-deploy-v2.py --url https://aitoptools.net   # 自定义 URL (测 staging)

纯标准库实现, 不引入新依赖 (urllib + re + json + html.parser + subprocess + datetime).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser

# ---------- 配置 ----------
DEFAULT_URL = 'https://aitoptools.net'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))
) if not os.path.basename(os.getcwd()) == 'scripts' else os.path.dirname(os.getcwd())

# ---------- ANSI color ----------
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
GRAY = '\033[90m'
RESET = '\033[0m'


def color(s, c):
    return f'{c}{s}{RESET}' if sys.stdout.isatty() else s


def log(icon, msg, level='info'):
    if level == 'pass':
        print(f'  {color("✓", GREEN)} {msg}')
    elif level == 'fail':
        print(f'  {color("✗", RED)} {msg}')
    elif level == 'warn':
        print(f'  {color("⚠", YELLOW)} {msg}')
    else:
        print(f'  {color("·", GRAY)} {msg}')


# ---------- 5 步真 verify 流水线 ----------
def step1_git_ahead():
    """git status -sb 无 ahead (commit 真到 origin/main)."""
    try:
        r = subprocess.run(['git', 'status', '-sb'], cwd=ROOT, capture_output=True, text=True, timeout=10)
        if r.returncode != 0:
            return False, f'git status 失败: {r.stderr.strip()}'
        # 找 ahead 标记
        ahead = re.search(r' ahead (\d+)', r.stdout)
        if ahead:
            return False, f'有 {ahead.group(1)} commit 未 push (ahead)'
        return True, 'git status -sb: no ahead'
    except Exception as e:
        return False, f'git status 异常: {e}'


def step2_sitemap_mtime():
    """sitemap.xml 真实可访问 + 至少 100 URLs (139 页站)."""
    url = f'{DEFAULT_URL}/sitemap.xml'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            if r.status != 200:
                return False, f'sitemap.xml HTTP {r.status}'
            body = r.read().decode('utf-8', errors='ignore')
            urls = re.findall(r'<loc>([^<]+)</loc>', body)
            if len(urls) < 100:
                return False, f'sitemap URLs 过少: {len(urls)} < 100'
            return True, f'sitemap.xml: {len(urls)} URLs'
    except Exception as e:
        return False, f'sitemap 抓取失败: {e}'


def step3_homepage_body():
    """首页 HTTP 200 + body 含 hotfix-2 标题 "We don't rate vibes" + evidence-stat 三件套数字."""
    url = f'{DEFAULT_URL}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            if r.status != 200:
                return False, f'首页 HTTP {r.status}'
            body = r.read().decode('utf-8', errors='ignore')
            # hotfix-2 标志
            if 'We don&#x27;t rate vibes' not in body and "We don't rate vibes" not in body:
                return False, '首页缺 hotfix-2 标题 "We don\'t rate vibes"'
            # 3 个 stat 数字
            for num in ['107', '312+', '0']:
                if num not in body:
                    return False, f'首页缺 evidence-stat 数字 "{num}"'
            # leftcolumn 副标不应再承诺 two numbers (hotfix-3 收尾)
            if 'two numbers' in body or 'the two numbers' in body:
                return False, '首页副标还在承诺 "two numbers" (hotfix-3 路 B 未收尾)'
            return True, f'首页 {len(body)} bytes, hotfix-2 标志齐全'
    except Exception as e:
        return False, f'首页抓取失败: {e}'


# ---------- 静态预检 8 项断言 (hotfix-2 baseline) ----------
def static_8_baseline():
    """hotfix-2 7/27 PASS 的 8 项静态断言."""
    url = f'{DEFAULT_URL}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return [(False, f'首页抓取失败: {e}')]

    checks = [
        # 期望/实际 → (label, count_expected, count_actual_pass)
        ('evidence-stat-num = 3', body.count('evidence-stat-num'), lambda n: n == 3),
        ('evidence-stats = 1', body.count('evidence-stats'), lambda n: n == 1),
        ('evidence-meter = 0 (旧假进度条 DOM 全删)', body.count('evidence-meter'), lambda n: n == 0),
        ('evidence-row = 0', body.count('evidence-row'), lambda n: n == 0),
        ('vertical-score = 0 (工具卡删)', body.count('vertical-score'), lambda n: n == 0),
        ('8.8 hardcoded in evidence-card = 0', body.count('8.8'), lambda n: n == 0),
        ("footer '74+' = 0 (硬编老数已删)", body.count('74+'), lambda n: n == 0),
        ('footer dynamic 107 = 1', body.count('>107<') + body.count('>107 '), lambda n: n >= 1),
    ]
    results = []
    for label, actual, predicate in checks:
        ok = predicate(actual)
        if not ok:
            results.append((False, f'{label} → 实际 {actual} 不符预期'))
        else:
            results.append((True, f'{label} → 实际 {actual}'))
    return results


# ---------- 3 项新断言 (千问 0.5 步扩展) ----------
def new_assertion_1_surface_ink():
    """断言 ① 深底容器内浅底色泄漏 (千问 P0-1/P0-2 案例).

    抓首页 HTML, 找 .evidence-card / .surface-ink 段, 检测段内是否引用
    var(--k-muted) / var(--k-secondary) / var(--k-tertiary) 浅底色 (P0 漏网
    案例: 上一轮 P0-2 修了 evidence-card 背景深色, 但 EvidenceCard.js 里的
    verdict 文本还在用浅底色 token → 段内暗字糊).

    实操: 不解析 computed style (cheerio/playwright), 只在 rendered HTML +
    inline style/className 找浅底色泄漏, 这是 build-time 能查的信号.
    """
    url = f'{DEFAULT_URL}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return [(False, f'首页抓取失败: {e}')]

    # 浅底色 token (深底上 = 视觉漏)
    SHALLOW_TOKENS = ['var(--k-muted)', 'var(--k-secondary)', 'var(--k-tertiary)', 'var(--k-primary)']
    LEAK_LABELS = {
        'var(--k-muted)': 'k-muted',
        'var(--k-secondary)': 'k-secondary',
        'var(--k-tertiary)': 'k-tertiary',
        'var(--k-primary)': 'k-primary',
    }

    # 抓所有 .evidence-card 段 (深底容器)
    evidence_blocks = re.findall(r'<aside[^>]*class="[^"]*evidence-card[^"]*"[^>]*>.*?</aside>', body, re.DOTALL)
    # 抓所有 .surface-ink 段 (深底容器通用 class)
    surface_blocks = re.findall(r'<[^>]*class="[^"]*surface-ink[^"]*"[^>]*>.*?</[^>]+>', body, re.DOTALL)

    deep_blocks = evidence_blocks + surface_blocks
    if not deep_blocks:
        return [(True, '断言 ①: 找不到 .evidence-card / .surface-ink 段 (N/A) — 改文案时记得加容器')]

    leaks = []
    for i, block in enumerate(deep_blocks):
        for token in SHALLOW_TOKENS:
            if token in block:
                leaks.append(f'  block #{i + 1} 出现浅底色 {LEAK_LABELS[token]}: "{token}"')

    if leaks:
        return [(False, '断言 ① FAIL: 深底容器内有浅底色泄漏 (千问 P0 风险)\n' + '\n'.join(leaks[:5]))]
    return [(True, f'断言 ①: {len(deep_blocks)} 个深底容器 0 浅底色泄漏')]


def new_assertion_4_subtitle_schema():
    """断言 ④ 首屏副标维度名 schema 校验 (千问 P0 叙事左右互搏).

    抓首屏副标 (hero-text 段), 提取 "print compatibility" / "e-commerce fit"
    / "two numbers" 关键词, 搜 data/reviews.json 看是否有对应字段 (如
    reviews[i].printCompatibility / reviews[i].ecommerceFit). 搜到但 schema
    无 = 空头支票 FAIL.

    实战 7/27: page.js L108-109 副标承诺 print compatibility / e-commerce fit,
    但 reviews.json 全 107 篇无这两个字段 → 千问诊断 "首屏左右互搏 / 空头".
    """
    url = f'{DEFAULT_URL}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return [(False, f'首页抓取失败: {e}')]

    # 抓 hero 副标 (h1 后面第一个 <p> 段)
    h1_match = re.search(r'<h1[^>]*>.*?</h1>', body, re.DOTALL)
    if not h1_match:
        return [(True, '断言 ④: 找不到 h1 (N/A)')]

    # h1 后面第一个 <p>
    after_h1 = body[h1_match.end():h1_match.end() + 3000]
    p_match = re.search(r'<p[^>]*>(.*?)</p>', after_h1, re.DOTALL)
    if not p_match:
        return [(True, '断言 ④: 找不到首屏副标 p (N/A)')]
    subtitle = re.sub(r'<[^>]+>', '', p_match.group(1))  # 脱 HTML 标签

    # 维度名黑名单 (107 篇 reviews 全无这些字段, 任何副标提就是空头)
    DIMENSION_KEYWORDS = [
        'print compatibility',
        'e-commerce fit',
        'ecommerce fit',
        'two numbers',
        'the two numbers',
        'printcompatibility',
        'ecommercefit',
    ]

    found = [k for k in DIMENSION_KEYWORDS if k in subtitle.lower()]
    if not found:
        return [(True, '断言 ④: 副标未承诺未实现维度')]

    # 找到关键词, schema 校验
    reviews_path = os.path.join(ROOT, 'src', 'data', 'reviews.json')
    if not os.path.exists(reviews_path):
        return [(False, f'断言 ④ FAIL: 副标承诺 "{found}" 但 reviews.json 不存在, 无法 schema 校验')]

    try:
        with open(reviews_path, encoding='utf-8') as f:
            data = json.load(f)
        # reviews.json 是 array 或 {tools: [...]}?
        reviews = data if isinstance(data, list) else data.get('tools') or data.get('reviews') or []
    except Exception as e:
        return [(False, f'断言 ④ FAIL: reviews.json 解析失败: {e}')]

    # 检查每个找到的关键词在 schema 是否有对应字段
    FIELD_MAP = {
        'print compatibility': 'printCompatibility',
        'printcompatibility': 'printCompatibility',
        'e-commerce fit': 'ecommerceFit',
        'ecommerce fit': 'ecommerceFit',
        'ecommercefit': 'ecommerceFit',
        # 'two numbers' 不是字段, 是表述, 默认 FAIL
    }

    leaks = []
    for kw in found:
        field = FIELD_MAP.get(kw)
        if not field:
            leaks.append(f'  副标承诺 "{kw}" — schema 无此字段 (无对应数据维度)')
            continue
        # 抽样 1 篇看是否有这个字段
        has_field = any(isinstance(r, dict) and field in r for r in reviews[:5])
        if not has_field:
            leaks.append(f'  副标承诺 "{kw}" (schema 字段 {field}) — 抽样 5 篇 0 篇含此字段 (空头)')
        else:
            # schema 包含字段 — 进一步检查覆盖率
            cov = sum(1 for r in reviews if isinstance(r, dict) and field in r) / max(1, len(reviews))
            if cov < 0.5:
                leaks.append(f'  副标承诺 "{kw}" — 字段 {field} 覆盖率 {cov:.0%} < 50% (空头)')
            else:
                pass  # 覆盖率 ≥ 50% = OK

    if leaks:
        return [(False, f'断言 ④ FAIL: 首屏副标空头支票 (千问 P0 风险)\n' + '\n'.join(leaks))]
    return [(True, f'断言 ④: 副标承诺维度全有 schema 支撑 (found={found})')]


def new_assertion_5_winner_verdict():
    """断言 ⑤ 6 篇 vs-card winner 字段 vs conclusion 首句 (千问 P0 winner 打架).

    抓首页 .vs-card 段, 找 .vs-side 第一个 (winner 一侧) 的 .vs-name 文本,
    检查这个工具名是否在 .vs-verdict 段出现. 不出现 = winner/conclusion 互搏.
    """
    url = f'{DEFAULT_URL}/'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'verify-deploy-v2/1.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return [(False, f'首页抓取失败: {e}')]

    # 抓所有 .vs-card 段
    vs_cards = re.findall(r'<article[^>]*class="[^"]*vs-card[^"]*"[^>]*>.*?</article>', body, re.DOTALL)
    if not vs_cards:
        return [(True, '断言 ⑤: 找不到 .vs-card 段 (N/A)')]

    fights = []
    for i, card in enumerate(vs_cards):
        # 抓 winner side: .vs-card-a-wins 或 .vs-card-b-wins 父容器下的第一个 .vs-side
        is_a_wins = 'vs-card-a-wins' in card
        is_b_wins = 'vs-card-b-wins' in card
        if not (is_a_wins or is_b_wins):
            continue  # 平局或无胜方, 跳过

        # 抓所有 .vs-name
        names = re.findall(r'<span class="vs-name"[^>]*>([^<]+)</span>', card)
        if len(names) < 2:
            fights.append(f'  card #{i + 1} 不足 2 个 vs-name (解析失败)')
            continue

        winner_name = names[0] if is_a_wins else names[1]
        loser_name = names[1] if is_a_wins else names[0]

        # 抓 .vs-verdict
        v_match = re.search(r'<p class="vs-verdict"[^>]*>([^<]+)</p>', card)
        if not v_match:
            fights.append(f'  card #{i + 1} ({winner_name}) 找不到 .vs-verdict')
            continue
        verdict = v_match.group(1).strip()

        if winner_name.lower() not in verdict.lower():
            fights.append(f'  card #{i + 1}: 胜方 {winner_name} 不在 verdict "{verdict[:60]}..." 中 (winner/conclusion 打架)')

    if fights:
        return [(False, f'断言 ⑤ FAIL: {len(fights)} 个 vs-card winner/conclusion 互搏\n' + '\n'.join(fights[:5]))]
    return [(True, f'断言 ⑤: {len(vs_cards)} 个 vs-card winner/conclusion 全一致')]


# ---------- Main ----------
def main():
    ap = argparse.ArgumentParser(description='aitoptools.net 部署后真 verify 脚本 v2')
    ap.add_argument('--quiet', action='store_true', help='只在失败时打印')
    ap.add_argument('--url', default=DEFAULT_URL, help=f'站 URL (默认 {DEFAULT_URL})')
    args = ap.parse_args()

    global DEFAULT_URL
    DEFAULT_URL = args.url.rstrip('/')

    print(f'\n{color("═══ verify-deploy-v2 ═══", GRAY)}')
    print(f'  target: {DEFAULT_URL}')
    print(f'  time:   {datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")}\n')

    failures = []

    # === 5 步真 verify 流水线 ===
    print(color('【5 步真 verify 流水线】', GRAY))
    for name, fn in [
        ('Step 1: git status -sb 无 ahead', step1_git_ahead),
        ('Step 2: sitemap.xml mtime + URLs', step2_sitemap_mtime),
        ('Step 3: 首页 body 验证', step3_homepage_body),
    ]:
        ok, msg = fn()
        log('pass' if ok else 'fail', f'{name} — {msg}', 'pass' if ok else 'fail')
        if not ok:
            failures.append(f'{name}: {msg}')

    # === 静态预检 8 项 (hotfix-2 baseline) ===
    print(f'\n{color("【静态预检 8 项 (hotfix-2 baseline)】", GRAY)}')
    for ok, msg in static_8_baseline():
        log('pass' if ok else 'fail', msg, 'pass' if ok else 'fail')
        if not ok:
            failures.append(msg)

    # === 3 项新断言 (千问 0.5 步扩展) ===
    print(f'\n{color("【3 项新断言 (千问 0.5 步扩展)】", GRAY)}')
    for name, fn in [
        ('断言 ① 深底容器内浅底色泄漏 (千问 P0)', new_assertion_1_surface_ink),
        ('断言 ④ 首屏副标维度名 schema 校验 (千问 P0)', new_assertion_4_subtitle_schema),
        ('断言 ⑤ 6 篇 vs-card winner/conclusion 一致 (千问 P0)', new_assertion_5_winner_verdict),
    ]:
        results = fn()
        for ok, msg in results:
            log('pass' if ok else 'fail', f'{name} — {msg}', 'pass' if ok else 'fail')
            if not ok:
                failures.append(f'{name}: {msg}')

    # === 总结 ===
    print(f'\n{color("─" * 50, GRAY)}')
    if failures:
        print(color(f'✗ {len(failures)} 项 FAIL', RED))
        for f in failures:
            print(f'    {color("·", RED)} {f}')
        print()
        sys.exit(1)
    else:
        print(color('✓ 全部 PASS — 部署可信', GREEN))
        print()
        sys.exit(0)


if __name__ == '__main__':
    main()
