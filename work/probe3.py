# -*- coding: utf-8 -*-
"""查某篇「PDF 声明 N 句但只抓到 M 句」时，漏掉的是哪些。"""
import io, re, sys

year, text = int(sys.argv[1]), int(sys.argv[2])
t = io.open('work/txt/%d.txt' % year, encoding='utf-8', errors='replace').read()
lines = t.split('\n')

all_heads = [i for i, l in enumerate(lines) if re.match(r'^\s*Text [1-4]\s*$', l)]
blk = all_heads[4:8]
a = blk[text - 1]
b = blk[text] if text < len(blk) else len(lines)

# 该篇的 SENTENCE INSIGHTS 区
marks = [i for i, l in enumerate(lines) if 'SENTENCE INSIGHTS' in l]
ins = [i for i in marks if a <= i < b]
if not ins:
    print('该区间无 SENTENCE INSIGHTS')
    sys.exit()
target = ins[0]

declared = None
for j in range(target, target + 6):
    m = re.search(r'(\d+)\s*句真题句逐层精讲', lines[j])
    if m:
        declared = int(m.group(1))
        break

print('%d Text %d: 区间 %d..%d, SENTENCE INSIGHTS @%d, PDF 声明 %s 句'
      % (year, text, a, b, target, declared))
print('=' * 70)

# 打印该区原始内容，标出位置行
stop = len(lines)
for j in range(target + 1, len(lines)):
    if 'HIGH-FREQUENCY' in lines[j] or 'SENTENCE INSIGHTS' in lines[j]:
        stop = j
        break

n_loc = 0
for i in range(target, stop):
    raw = lines[i].rstrip()
    if 'lazynote.cn' in raw or '懒笔记' in raw:
        continue
    s = raw.strip()
    if not s:
        continue
    isloc = bool(re.match(r'^第(\d+)段，第(\d+)句$', s))
    if isloc:
        n_loc += 1
    cjk = any('一' <= c <= '鿿' for c in s)
    print('%5d %s%s %s' % (i, '★' if isloc else ' ',
                           '中' if cjk else '英', s[:78]))

print('=' * 70)
print('位置行总数 = %d, PDF 声明 = %s' % (n_loc, declared))
