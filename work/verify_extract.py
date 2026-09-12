# -*- coding: utf-8 -*-
"""比对 extract.py 的输出与已上线数据（site/data/2016-text1.js），
确认提取脚本可靠：句子、译文、精讲句、词表都应一致。"""
import io, json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw = json.load(io.open(os.path.join(ROOT, 'work/raw/2016-text1.json'),
                        encoding='utf-8'))

# 读已上线数据
js = io.open(os.path.join(ROOT, 'site/data/2016-text1.js'),
             encoding='utf-8').read()
js = js[js.index('{'):js.rindex('}') + 1]
live = json.loads(js)

fails, oks = [], []


def chk(name, cond, detail=''):
    (oks if cond else fails).append(name + (('  -> ' + detail) if detail else ''))


print('=== 段落与句子 ===')
chk('段数 6', len(raw['paragraphs']) == 6, str(len(raw['paragraphs'])))
chk('句数 18', sum(len(p['sentences']) for p in raw['paragraphs']) == 18)
chk('与线上句数一致',
    sum(len(p['sentences']) for p in raw['paragraphs']) ==
    sum(len(p['sentences']) for p in live['paragraphs']))

print('=== 英文原文（前 2 段首句逐字比对）===')
for k in range(2):
    a = raw['paragraphs'][k]['sentences'][0]['en']
    b = live['paragraphs'][k]['sentences'][0]['en']
    chk('P%d 首句一致' % (k + 1), a.strip() == b.strip(),
        '\n    提取: ' + a[:80] + '\n    线上: ' + b[:80])

print('=== 中文译文 ===')
for k in range(2):
    a = re.sub(r'\s+', '', raw['paragraphs'][k]['zh'])
    b = re.sub(r'\s+', '', live['paragraphs'][k]['zh'])
    chk('P%d 译文一致' % (k + 1), a == b,
        '\n    提取: ' + a[:60] + '\n    线上: ' + b[:60])

print('=== 精讲句（应 12 句，且能在正文里找到）===')
chk('精讲 12 句', len(raw['insights']) == 12, str(len(raw['insights'])))

# 建立 段落号 -> 句序号 -> 句子id 的映射
idx = {}
for p in raw['paragraphs']:
    pi = int(p['id'][1:])
    for k, s in enumerate(p['sentences']):
        idx[(pi, k + 1)] = s['id']

matched = 0
for it in raw['insights']:
    sid = idx.get((it['para'], it['sent']))
    if sid and it['en'][:40] in dict(
            (s['id'], s['en']) for p in raw['paragraphs'] for s in p['sentences'])[sid]:
        matched += 1
    else:
        print('  未匹配: 第%d段第%d句  %s' % (it['para'], it['sent'], it['en'][:50]))
chk('精讲句均能定位到正文句子', matched == len(raw['insights']),
    '%d/%d' % (matched, len(raw['insights'])))

# 与线上 insight 标记比对
live_ins = set()
for p in live['paragraphs']:
    for s in p['sentences']:
        if s.get('insight'):
            live_ins.add(s['id'])
ext_ins = set(idx[(it['para'], it['sent'])] for it in raw['insights']
              if (it['para'], it['sent']) in idx)
chk('精讲句集合与线上一致', live_ins == ext_ins,
    '线上 %d / 提取 %d / 差集 %s' % (len(live_ins), len(ext_ins),
                                sorted(live_ins ^ ext_ins)[:6]))

print('=== 词表 ===')
chk('32 词', len(raw['vocab']) == 32, str(len(raw['vocab'])))
lv = dict((v['word'], v) for v in live['vocab'])
miss = [v['word'] for v in raw['vocab'] if v['word'] not in lv]
extra = [w for w in lv if w not in set(v['word'] for v in raw['vocab'])]
chk('词集合与线上一致', not miss and not extra,
    '缺 %s / 多 %s' % (miss[:5], extra[:5]))

bad = []
for v in raw['vocab']:
    o = lv.get(v['word'])
    if not o:
        continue
    if o['level'] != v['level']:
        bad.append('%s 等级 %s!=%s' % (v['word'], v['level'], o['level']))
    if v['cn'] and o['cn'] and v['cn'][:4] != o['cn'][:4]:
        bad.append('%s 释义 %s!=%s' % (v['word'], v['cn'], o['cn']))
chk('词表等级/释义一致', not bad, '; '.join(bad[:4]))

# 词性是否成功提取
no_pos = [v['word'] for v in raw['vocab'] if not v['pos']]
chk('词性已提取', not no_pos, '缺词性的词: %s' % no_pos[:8])

print('\n================================')
for o in oks:
    print('  PASS  ' + o)
for f in fails:
    print('  FAIL  ' + f)
print('\n%d 通过 / %d 失败' % (len(oks), len(fails)))
sys.exit(1 if fails else 0)
