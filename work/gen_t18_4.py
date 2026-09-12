# -*- coding: utf-8 -*-
"""生成 2023 考研英语二 Text 4 的数据文件 site/data/2023-text4.js。

用法：  python work/gen_t23_4.py

校验规则与 work/gen.py 完全一致：
  · 每个 bold 子串必须真实存在于原句
  · 每个 chunk.text 必须真实存在且按出现顺序
  · 每个 bold 必须有释义（Gloss）
  · PDF 精讲句（insight）才生成原站解析页 URL，其余留空避免死链
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'work'))

from t18_4_a import A as A1
from t18_4_b import A as A2
from t18_4_c import A as A3
from t18_4_gloss import GLOSS

A = {}
A.update(A1)
A.update(A2)
A.update(A3)

YEAR, TEXT = 2018, 4
RAW = json.load(io.open(os.path.join(ROOT, 'work/raw/%d-text%d.json' % (YEAR, TEXT)),
                        encoding='utf-8'))

SOURCE = ('https://english-exam.lazynote.cn/kaoyan/sections/%d-english-two/'
          'section2-part-a-%d/' % (YEAR, TEXT))
SENT_BASE = ('https://english-exam.lazynote.cn/kaoyan/paper/%d-english-two/'
             'section2-part-a-%d/' % (YEAR, TEXT))


def sent_url(sid):
    """'P3S1' -> '.../p3-s1/'"""
    m = re.match(r'^P(\d+)S(\d+)$', sid)
    return SENT_BASE + 'p%s-s%s/' % (m.group(1), m.group(2)) if m else ''


problems = []
report = []

for para in RAW['paragraphs']:
    for s in para['sentences']:
        sid = s['id']
        if sid not in A:
            problems.append('MISSING analysis for %s' % sid)
            continue
        a = A[sid]
        s.update(a)

        bolded = []
        for b in a['bold']:
            if b.lower() not in s['en'].lower():
                problems.append('BOLD not found in %s: %r' % (sid, b))
            if b not in GLOSS:
                problems.append('NO GLOSS for %r (in %s)' % (b, sid))
            bolded.append(dict(text=b, gloss=GLOSS.get(b, '')))
        s['bold'] = bolded

        covered = 0
        pos = 0
        for c in a['chunks']:
            i = s['en'].find(c['text'], pos)
            if i < 0:
                i = s['en'].find(c['text'])
                if i < 0:
                    problems.append('CHUNK not found in %s: %r' % (sid, c['text']))
                    continue
                problems.append('CHUNK out-of-order in %s: %r' % (sid, c['text']))
            pos = i + len(c['text'])
            covered += len(c['text'])
        s['cover'] = round(100.0 * covered / max(1, len(s['en'])))
        s['url'] = sent_url(sid) if a['insight'] else ''

        report.append('%-6s cover=%3d%% chunks=%2d bold=%d %s'
                      % (sid, s['cover'], len(a['chunks']), len(a['bold']),
                         'INSIGHT' if a['insight'] else ''))

# 精讲考点文字：从 PDF 提取的 insights 按「第N段第M句」回填
ins_map = {}
for it in RAW['insights']:
    ins_map[(it['para'], it['sent'])] = it['note']

for para in RAW['paragraphs']:
    pi = int(para['id'][1:])
    for k, s in enumerate(para['sentences']):
        if s.get('insight'):
            note = ins_map.get((pi, k + 1), '')
            if note:
                s['note'] = note
            elif not s.get('note'):
                problems.append('insight %s 缺考点文字（PDF 未印位置行）' % s['id'])

PASSAGE = dict(
    year=YEAR, text=TEXT,
    title='%d 考研英语二 · Text %d' % (YEAR, TEXT),
    subtitle='深度工作：战胜分心，也要拥抱闲散',
    source=SOURCE,
    paragraphs=[dict(id=p['id'], zh=p['zh'], sentences=p['sentences'])
                for p in RAW['paragraphs']],
    vocab=[dict(word=v['word'], level=v['level'], pos=v['pos'], cn=v['cn'],
                count=v['count'], freq=v['freq']) for v in RAW['vocab']],
)

print('\n'.join(report))
n_sent = sum(len(p['sentences']) for p in PASSAGE['paragraphs'])
n_ins = sum(1 for p in PASSAGE['paragraphs'] for s in p['sentences'] if s['insight'])
print('\n%d 段 · %d 句 · %d 句精讲 · %d 个高频词'
      % (len(PASSAGE['paragraphs']), n_sent, n_ins, len(PASSAGE['vocab'])))
print('平均成分覆盖 %.1f%%'
      % (sum(s['cover'] for p in PASSAGE['paragraphs'] for s in p['sentences']) / n_sent))

print('\nPROBLEMS (%d):' % len(problems))
for x in problems:
    print('  ! ' + x)

outdir = os.path.join(ROOT, 'site', 'data')
os.makedirs(outdir, exist_ok=True)
js = 'window.PASSAGE = ' + json.dumps(PASSAGE, ensure_ascii=False, indent=1) + ';\n'
io.open(os.path.join(outdir, '%d-text%d.js' % (YEAR, TEXT)), 'w',
        encoding='utf-8').write(js)
print('\nwrote site/data/%d-text%d.js  (%d bytes)'
      % (YEAR, TEXT, len(js.encode('utf-8'))))

sys.exit(1 if problems else 0)
