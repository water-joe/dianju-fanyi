# -*- coding: utf-8 -*-
"""从考研英语二真题 PDF 中提取一篇阅读（Text N）的原始素材。

    python work/extract.py --year 2017 --text 2

产出 work/raw/{year}-text{n}.json，包含：
  paragraphs  —— 每段的英文原文、中文译文、切分好的句子
  insights    —— PDF「真题句逐层精讲」选中的句子 + 考点文字（需画线的那些）
  vocab       —— PDF「真题高频词」表（词、CEFR、词性、释义、本篇/真题词频）
  source      —— 原站该篇解析页 URL（从 PDF 页脚提取）
  sent_base   —— 句子解析页 URL 前缀（拼 p{段}-s{句} 即得）

注意：**成分划分不在这里**。PDF 里没有逐词成分标注（网页版有，打印时丢了），
那层必须逐句人工写，见 README 的「新增一篇」一节。

PDF 结构要点（11 年真题已验证一致）：
  · 整卷 PDF 前半是题目、后半是解析；每篇 Text 出现两次，
    第二次（索引 4..7）才带 P1/P2 段落标记与中文译文。
  · 译文可能以拉丁字母开头（如「Flatiron School 是一所…」），
    不能靠首字符判断中英，要靠「本段是否已出现首个 CJK 字符」。
  · 提取出的译文里半角逗号要按上下文转全角。
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cjk(ch):
    return '一' <= ch <= '鿿'


def has_cjk(s):
    return any(cjk(c) for c in s)


def norm_zh(s):
    """译文里的半角标点按上下文转全角。"""
    out = []
    for i, ch in enumerate(s):
        prev = s[i - 1] if i > 0 else ''
        nxt = s[i + 1] if i + 1 < len(s) else ''
        if ch == ',' and (has_cjk(prev) or has_cjk(nxt)):
            out.append('，')
        elif ch == '?' and has_cjk(prev):
            out.append('？')
        elif ch == ';' and (has_cjk(prev) or has_cjk(nxt)):
            out.append('；')
        elif ch == '!' and has_cjk(prev):
            out.append('！')
        else:
            out.append(ch)
    return ''.join(out)


def pdf_to_text(pdf, out_txt):
    """pdftotext 提取。必须带 -enc UTF-8，否则中文全丢。"""
    if not os.path.exists(pdf):
        sys.exit('找不到 PDF：%s' % pdf)
    subprocess.check_call(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, out_txt])
    return io.open(out_txt, encoding='utf-8', errors='replace').read()


def text_blocks(lines):
    """返回 4 篇 Text 在解析区的起始行号（跳过前半的题目区）。"""
    all_heads = [i for i, l in enumerate(lines)
                 if re.match(r'^\s*Text [1-4]\s*$', l)]
    if len(all_heads) < 8:
        sys.exit('只找到 %d 个 Text 标题，预期 >= 8；PDF 结构可能不同'
                 % len(all_heads))
    return all_heads[4:8]          # 后 4 个才是带译文与段落标记的解析区


def parse_paragraphs(lines, start, end):
    """解析 P1/P2… 段落：英文行在前，首个含 CJK 的行之后都算译文。"""
    paras = []
    cur = None
    for i in range(start, end):
        raw = lines[i]
        if 'lazynote.cn' in raw or '懒笔记' in raw:
            continue
        if re.match(r'^\s*题目与逐题解析', raw):
            break
        m = re.match(r'^\s{0,25}(P\d+)\s+(.*)$', raw)
        if m:
            cur = {'id': m.group(1), 'en_lines': [m.group(2)],
                   'zh_lines': [], 'zh_started': False}
            paras.append(cur)
            continue
        if cur is None:
            continue
        s = raw.strip()
        if not s:
            continue
        if has_cjk(s):
            cur['zh_started'] = True
        (cur['zh_lines'] if cur['zh_started'] else cur['en_lines']).append(s)
    return paras


def split_sentences(en):
    """按句末标点切句，避免把缩写点号当句末。

    实现要点：先把常见缩写替换成一个不会出现在正文的哨兵字符，
    切句后再还原。替换用 lambda 而非字符串——替换串里的 \\x01
    会被 re 当成转义序列解析并报错（bad escape \\x）。
    """
    guards = [(r'\bMr\.', 'S1'), (r'\bMrs\.', 'S2'), (r'\bMs\.', 'S3'),
              (r'\bDr\.', 'S4'), (r'\bSt\.', 'S5'), (r'\bvs\.', 'S6'),
              (r'\betc\.', 'S7'), (r'\be\.g\.', 'S8'), (r'\bi\.e\.', 'S9'),
              (r'\bJr\.', 'SA'), (r'\bProf\.', 'SB')]
    back = {'S1': 'Mr.', 'S2': 'Mrs.', 'S3': 'Ms.', 'S4': 'Dr.', 'S5': 'St.',
            'S6': 'vs.', 'S7': 'etc.', 'S8': 'e.g.', 'S9': 'i.e.',
            'SA': 'Jr.', 'SB': 'Prof.'}
    # 用不可见控制字符做哨兵，且必须用 lambda 返回，避免 re 解析替换串
    charset = 'Z1Z2Z3Z4Z5Z6Z7Z8Z9ZaZb'
    t = en
    reps = {}
    for i, (pat, _key) in enumerate(guards):
        tok = 'Z%dZ' % (i + 1)
        reps[tok] = back[_key]
        t = re.sub(pat, lambda m, tok=tok: tok, t)
    # 保护小数与序号中的点（如 3.5、No.1）
    t = re.sub(r'(\d)\.(\d)', lambda m: m.group(1) + 'Z0Z' + m.group(2), t)
    reps['Z0Z'] = '.'

    # 句末标点 + 可选的闭合引号 + 空白 + 大写开头。
    # 闭引号要「保留」而不是吃掉（用捕获组拼回），否则
    # `call "reward sensitivity." Decision-making` 会切出缺引号的上半句。
    parts = re.split(r'(?<=[.!?])(["\')\]]?)\s+(?=[A-Z"\'(])', t)
    if len(parts) > 1:
        merged, i = [], 0
        while i < len(parts):
            seg = parts[i]
            nxt = parts[i + 1] if i + 1 < len(parts) else None
            # 奇数位是被单独切出来的闭引号，要接回前一段
            if nxt is not None and len(nxt) <= 1 and (
                    nxt in '"\')]' or nxt == ''):
                merged.append(seg + nxt)
                i += 2
            else:
                merged.append(seg)
                i += 1
        parts = merged

    out = []
    for p in parts:
        for tok, orig in reps.items():
            p = p.replace(tok, orig)
        p = p.strip()
        if p:
            out.append(p)
    return out


def head_for(lines, pos):
    """找出某个行号隶属的 Text 编号。"""
    for j in range(pos, 0, -1):
        m = re.match(r'^\s*Text ([1-4])\s*$', lines[j])
        if m:
            return int(m.group(1))
    return None


def vocab_range(lines, textno, heads):
    """与 insight_range 同理。heads 同样是**全部** 8 个标题的行号。"""
    if len(heads) < 8:
        return None
    blk = heads[4:8]
    a = blk[textno - 1]
    b = blk[textno] if textno < len(blk) else len(lines)
    marks = [i for i, l in enumerate(lines) if 'HIGH-FREQUENCY' in l]
    inside = [i for i in marks if a <= i < b]
    return inside[0] if inside else None


def insight_range(lines, textno, heads):
    """定位第 textno 篇的 SENTENCE INSIGHTS 区。

    heads 必须是**全部** Text 标题的行号（题目区 4 个 + 解析区 4 个，共 8 个），
    不是 text_blocks() 切过的后 4 个——本函数自己取 heads[4:] 作为解析区。
    早期版本误把已切片的 4 个传进来，heads[4+N-1] 越界 → 恒为 None → 抓到 0 句。

    顺带解决归属问题：不能只靠「往前找最近的 Text 标题」——
    2023 年 PDF 在 Text 1 之前还有一个「完形填空」的精讲区，
    它往前找不到 Text 标题，会被误判成 Text 4，导致四篇全部错位。
    """
    if len(heads) < 8:
        return None
    blk = heads[4:8]
    a = blk[textno - 1]
    b = blk[textno] if textno < len(blk) else len(lines)

    marks = [i for i, l in enumerate(lines) if 'SENTENCE INSIGHTS' in l]
    inside = [i for i in marks if a <= i < b]
    if inside:
        return inside[0]

    # 退化：按出现顺序取第 N 个
    titled = []
    for i in marks:
        for j in range(i, 0, -1):
            m = re.match(r'^\s*Text ([1-4])\s*$', lines[j])
            if m:
                titled.append((i, int(m.group(1))))
                break
    cand = [i for i, n in titled if n == textno and i >= (blk[0] if blk else 0)]
    return cand[0] if cand else None


def vocab_range(lines, textno, heads):
    """与 insight_range 同理：词表区也用行号区间定位，
    避免「往前找最近标题」把完形填空的词表误算到某篇 Text 上。"""
    if len(heads) < 8:
        return None
    a = heads[4 + textno - 1]
    b = heads[4 + textno] if 4 + textno < len(heads) else len(lines)
    marks = [i for i, l in enumerate(lines) if 'HIGH-FREQUENCY' in l]
    inside = [i for i in marks if a <= i < b]
    return inside[0] if inside else None


def parse_insights(lines, textno, heads=None):
    """抽 SENTENCE INSIGHTS 一节。

    PDF 中的排布（每个句子一组，顺序固定）：
          缩进3空格  句子的英文（可能跨 2 行，也可能带缩进的续行）
          （空行）
              缩进5空格  第N段，第M句        ← 位置行
          （空行）
            缩进4空格  考点文字（可能多行）
    即「句子在前、位置在后」，早期版本按「位置在前」写导致整体错位一位。
    """
    target = insight_range(lines, textno, heads or [])
    if target is None:
        return []

    # 边界：本区结束于下一个 SENTENCE INSIGHTS / HIGH-FREQUENCY，
    # **或题目解析开始**。后者必须判断——多篇 PDF（如 2023 T1）的
    # 精讲区后面紧跟着「第24题题干 / 第24题，B」这类题目解析行，
    # 不截断会：① 把题目句当成精讲句抓进来；② 挤掉真正的精讲句。
    stop = len(lines)
    for j in range(target + 1, len(lines)):
        l = lines[j]
        if 'HIGH-FREQUENCY' in l or 'SENTENCE INSIGHTS' in l:
            stop = j
            break
        if re.match(r'^\s*第\d+题', l.strip()) or '题干' in l:
            stop = j
            break

    # 只依赖「位置行」这一个无歧义锚点，不依赖缩进
    # （PDF 跨页后缩进会全部变成 0，实测 2016 第 1949 行起）。
    # 以位置行为界：
    #     句子 = 它「上方」连续的、不含 CJK 的行（向上回溯）
    #     考点 = 它「下方」到下一个锚点之间的行
    # 区分不看缩进、也不看「整行是否纯英文」——考点文字常以英文引文开头
    # （如 `"It is true that ..."属于…`），所以判据是「含不含 CJK」。
    body = []                     # (kind, payload)
    for i in range(target + 1, stop):
        raw = lines[i].rstrip()
        if 'lazynote.cn' in raw or '懒笔记' in raw:
            continue
        s = raw.strip()
        if not s:
            continue
        if (s.startswith('下列真题句') or s.startswith('解与真题高频词')
                or re.match(r'^\d+\s*句真题句逐层精讲$', s)):
            continue
        m = re.match(r'^第(\d+)段，第(\d+)句$', s)
        body.append(('loc', (int(m.group(1)), int(m.group(2)))) if m
                    else ('en' if not has_cjk(s) else 'note', s))

    # 按锚点切组：句子在锚点「之前」，考点在锚点「之后」
    groups = []
    for k, (kind, val) in enumerate(body):
        if kind != 'loc':
            continue
        para_no, sent_no = val

        # 句子：锚点上方连续的英文行（遇到 note / loc 即止）
        en_parts = []
        j = k - 1
        while j >= 0 and body[j][0] == 'en':
            en_parts.insert(0, body[j][1])
            j -= 1

        # 考点：锚点下方，直到下一个 loc 之前的 note 行
        note_parts = []
        j = k + 1
        while j < len(body) and body[j][0] == 'note':
            note_parts.append(body[j][1])
            j += 1

        groups.append({
            'para': para_no, 'sent': sent_no,
            'en': re.sub(r'\s+', ' ', ' '.join(en_parts)).strip(),
            'note': re.sub(r'\s+', '', ''.join(note_parts)).strip(),
        })

    return [g for g in groups if g['en']]


def _split_two_cols(line):
    """把「左列        右列」按两个及以上空格切成两半。
    词表是双列排版：career B1            app B1
    注意列内的单个空格必须保留（如 'adj. 感兴趣的'）。"""
    m = re.search(r'\S\s{2,}\S', line)
    if not m:
        return [line.strip()] if line.strip() else []
    cut = m.start() + 1
    return [line[:cut].strip(), line[cut:].strip()]


def parse_vocab(lines, textno, heads=None):
    """抽 HIGH-FREQUENCY 表。

    排版是**双列 × 每词三行**（实测 11 年一致）：
        career B1            app B1              ← 词 + CEFR
        n. 职业               n. 应用程序          ← 词性 + 释义
        本篇2 次 · 真题 42 句   本篇2 次 · 真题 16 句  ← 词频
    所以必须：① 按「2+ 空格」切左右列；② 词性释义在下一行、词频在第三行。
    早期版本只取行内第一个匹配 → 漏掉整个右列（32 词只出 16 个）。
    """
    target = vocab_range(lines, textno, heads or [])
    if target is None:
        return []

    stop = len(lines)
    for j in range(target + 1, len(lines)):
        if 'VOCABULARY' in lines[j] or re.match(r'^\s*Section I', lines[j]):
            stop = j
            break

    def next_nonblank(k):
        """返回 k 之后第一个非空行的下标（词表行之间夹着空行）。"""
        j = k + 1
        while j < stop and not lines[j].strip():
            j += 1
        return j if j < stop else None

    out = []
    i = target
    while i < stop:
        row = lines[i]
        mw = re.match(r'^\s*([a-zA-Z][a-zA-Z\-\']{1,20})\s+([ABC][12])\b', row)
        if not mw:
            i += 1
            continue
        # 当前行是「词 + CEFR」行；词性释义与词频在**之后的两个非空行**
        # （行之间夹着空行，所以不能写死 i+1 / i+2）
        r_pos = next_nonblank(i)
        r_cnt = next_nonblank(r_pos) if r_pos is not None else None

        word_bits = _split_two_cols(row)
        pos_bits = _split_two_cols(lines[r_pos]) if r_pos is not None else []
        cnt_bits = _split_two_cols(lines[r_cnt]) if r_cnt is not None else []

        for k, bit in enumerate(word_bits):
            m = re.match(r'^([a-zA-Z][a-zA-Z\-\']{1,20})\s+([ABC][12])$', bit)
            if not m:
                continue
            word, level = m.group(1), m.group(2)

            pos, cn = '', ''
            if k < len(pos_bits):
                pm = re.match(r'^([a-z]+\.?)\s*(.*)$', pos_bits[k])
                if pm:
                    pos, cn = pm.group(1), pm.group(2).strip()

            count, freq = 1, 0
            if k < len(cnt_bits):
                cm = re.search(r'本篇\s*(\d+)\s*次\s*·\s*真题\s*(\d+)\s*句', cnt_bits[k])
                if cm:
                    count, freq = int(cm.group(1)), int(cm.group(2))

            out.append({'word': word, 'level': level, 'pos': pos,
                        'cn': cn, 'count': count, 'freq': freq})

        # 跳到下一组：至少要越过已消费的 3 行（词/释义/词频）。
        # 用「下一个非空行且匹配词+等级」来定位，比固定 +3 稳。
        j = i + 1
        while j < stop:
            if re.match(r'^\s*[a-zA-Z][a-zA-Z\-\']{1,20}\s+[ABC][12]\b', lines[j]):
                break
            j += 1
        i = j if j < stop else stop
    return out


def parse_source(lines, year, textno):
    """从页脚提取来源 URL；规律 section2-part-a-{N}。"""
    pat = r'https://english-exam\.lazynote\.cn/kaoyan/sections/%d-english-two/section2-part-a-%d/' % (year, textno)
    for l in lines:
        if 'section2-part-a-%d' % textno in l:
            return pat
    # 2016/2026 的 part-a 无页码后缀，退回搜索
    for l in lines:
        m = re.search(r'https://english-exam\.lazynote\.cn\S*section2-part-a[^\s·]*', l)
        if m:
            return m.group(0).rstrip('·')
    return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--year', type=int, required=True)
    ap.add_argument('--text', type=int, required=True, choices=[1, 2, 3, 4])
    ap.add_argument('--pdf-dir', default=ROOT)
    args = ap.parse_args()

    pdf = os.path.join(args.pdf_dir,
                       '考研英语二%d年真题及答案解析（整卷）.pdf' % args.year)
    os.makedirs(os.path.join(ROOT, 'work', 'txt'), exist_ok=True)
    txt = os.path.join(ROOT, 'work', 'txt', '%d.txt' % args.year)
    content = pdf_to_text(pdf, txt)
    lines = content.split('\n')

    # all_heads = 全部 8 个 Text 标题（题目区 4 + 解析区 4）
    # heads4    = 解析区的 4 个，用于圈定段落范围
    # insight_range / vocab_range 需要的是 all_heads（它们自己取 [4:]）
    all_heads = [i for i, l in enumerate(lines)
                 if re.match(r'^\s*Text [1-4]\s*$', l)]
    if len(all_heads) < 8:
        sys.exit('只找到 %d 个 Text 标题，预期 >= 8；PDF 结构可能不同'
                 % len(all_heads))
    heads4 = all_heads[4:8]
    start = heads4[args.text - 1]
    end = heads4[args.text] if args.text < 4 else len(lines)

    paras = parse_paragraphs(lines, start, end)
    if not paras:
        sys.exit('未解析出段落（Text %d）' % args.text)

    result = {'year': args.year, 'text': args.text, 'paragraphs': []}
    for p in paras:
        en = re.sub(r'\s+', ' ', ' '.join(p['en_lines'])).strip()
        en = re.sub(r'\s+([,.;:!?])', r'\1', en)
        zh = norm_zh(re.sub(r'\s+', '', ''.join(p['zh_lines'])).strip())
        sents = [{'id': '%sS%d' % (p['id'], k + 1), 'en': s}
                 for k, s in enumerate(split_sentences(en))]
        result['paragraphs'].append(
            {'id': p['id'], 'en': en, 'zh': zh, 'sentences': sents})

    result['insights'] = parse_insights(lines, args.text, all_heads)
    result['vocab'] = parse_vocab(lines, args.text, all_heads)
    result['source'] = parse_source(lines, args.year, args.text)
    result['sent_base'] = (
        'https://english-exam.lazynote.cn/kaoyan/paper/%d-english-two/'
        'section2-part-a-%d/' % (args.year, args.text))

    outdir = os.path.join(ROOT, 'work', 'raw')
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, '%d-text%d.json' % (args.year, args.text))
    io.open(out, 'w', encoding='utf-8').write(
        json.dumps(result, ensure_ascii=False, indent=1))

    n_sent = sum(len(p['sentences']) for p in result['paragraphs'])
    n_ins = len(result['insights'])
    print('已写出 %s' % os.path.relpath(out, ROOT))
    print('  %d 段 · %d 句 · 精讲 %d 句 · 高频词 %d 个'
          % (len(paras), n_sent, n_ins, len(result['vocab'])))
    print('  来源 %s' % (result['source'] or '(未找到)'))
    if n_ins:
        print('\n精讲句（这些需要画线，且原站有独立解析页）:')
        for it in result['insights'][:6]:
            print('  第%d段第%d句  %s' % (it['para'], it['sent'], it['en'][:64]))
        if n_ins > 6:
            print('  …（共 %d 句）' % n_ins)
    print('\n下一步：在 work/gen.py 里补这一篇的成分划分（PDF 里没有这层数据）')


if __name__ == '__main__':
    main()
