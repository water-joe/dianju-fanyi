# -*- coding: utf-8 -*-
"""查 2023（及通用）PDF 里 4 篇 Text 的真实顺序与归属。"""
import io, re, sys

year = int(sys.argv[1]) if len(sys.argv) > 1 else 2023
t = io.open('work/txt/%d.txt' % year, encoding='utf-8', errors='replace').read()
lines = t.split('\n')

heads = [i for i, l in enumerate(lines) if re.match(r'^\s*Text [1-4]\s*$', l)]
print('%d 年：共 %d 处 "Text N" 标题' % (year, len(heads)))
print()

for k, i in enumerate(heads):
    # 往后看 40 行，找特征：是否有 P1 段落标记（= 解析区）
    has_p = False
    sample = ''
    for j in range(i, min(i + 45, len(lines))):
        if re.match(r'^\s{0,6}P\d', lines[j]):
            has_p = True
        if not sample and lines[j].strip() and 'Text' not in lines[j]:
            sample = lines[j].strip()[:66]
    kind = '解析区(有P标记)' if has_p else '题目区'
    print('  [%d] 行%5d  %-14s %s' % (k, i, kind, sample))

print()
print('=== 各 SENTENCE INSIGHTS 区归属检查 ===')
for i, l in enumerate(lines):
    if 'SENTENCE INSIGHTS' not in l:
        continue
    # 往前找最近的 Text 标题
    which = None
    for j in range(i, -1, -1):
        m = re.match(r'^\s*Text ([1-4])\s*$', lines[j])
        if m:
            which = int(m.group(1))
            break
    # 该区第一句英文
    first = ''
    for j in range(i, min(i + 40, len(lines))):
        s = lines[j].strip()
        if s and not any('一' <= c <= '鿿' for c in s) and len(s) > 25:
            first = s[:60]
            break
    print('  行%5d  往前最近标题=Text %s   首句: %s' % (i, which, first))
