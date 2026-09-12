# -*- coding: utf-8 -*-
"""批量自检：对每一年每一篇，比对 extract.py 抓到的精讲句数
与 PDF 自己声明的「N 句真题句逐层精讲」是否一致。

    python work/audit_extract.py           全部年份
    python work/audit_extract.py 2019      指定年份
"""
import io, os, re, subprocess, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEARS = list(range(2016, 2027))


def declared_counts(txt_path):
    """从纯文本里读 PDF 声明的精讲句数，按篇目顺序返回。"""
    lines = io.open(txt_path, encoding='utf-8', errors='replace').read().split('\n')
    out = {}
    heads = [i for i, l in enumerate(lines)
             if re.match(r'^\s*Text [1-4]\s*$', l)]
    if len(heads) < 8:
        return out
    marks = [i for i, l in enumerate(lines) if 'SENTENCE INSIGHTS' in l]
    for i in marks:
        # 该 SENTENCE INSIGHTS 属于哪个 Text（往前找最近的 Text 标题）
        which = None
        for j in range(i, 0, -1):
            m = re.match(r'^\s*Text ([1-4])\s*$', lines[j])
            if m:
                which = int(m.group(1))
                break
        if which is None:
            continue
        for j in range(i, min(i + 6, len(lines))):
            m = re.search(r'(\d+)\s*句真题句逐层精讲', lines[j])
            if m:
                out.setdefault(which, []).append(int(m.group(1)))
                break
    # 解析区是后 4 个（索引 4..7），取第二次出现的那个
    return dict((k, v[1] if len(v) > 1 else v[0]) for k, v in out.items())


def main():
    args = sys.argv[1:]
    years = [int(a) for a in args] if args else YEARS

    bad = 0
    print('year text  PDF声明  提取到   判定')
    print('-' * 44)
    for y in years:
        txt = os.path.join(ROOT, 'work', 'txt', '%d.txt' % y)
        if not os.path.exists(txt):
            pdf = os.path.join(ROOT, '考研英语二%d年真题及答案解析（整卷）.pdf' % y)
            if not os.path.exists(pdf):
                print('%d  —— 缺少 PDF，跳过' % y)
                continue
            subprocess.check_call(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, txt])
        decl = declared_counts(txt)
        for t in (1, 2, 3, 4):
            rj = os.path.join(ROOT, 'work', 'raw', '%d-text%d.json' % (y, t))
            if not os.path.exists(rj):
                subprocess.call([sys.executable,
                                 os.path.join(ROOT, 'work', 'extract.py'),
                                 '--year', str(y), '--text', str(t)],
                                stdout=subprocess.DEVNULL)
            if not os.path.exists(rj):
                print('%d  T%d  提取失败' % (y, t))
                bad += 1
                continue
            d = json.load(io.open(rj, encoding='utf-8'))
            got = len(d['insights'])
            want = decl.get(t)
            if want is None:
                mark = 'SKIP(无声明)'
            elif want == got:
                mark = 'OK'
            elif got < want:
                # 少抓：可能是 PDF 少印了位置行（如 2026 T1 第3段整段无位置行），
                # 也可能是解析漏了——需要人工看一眼，故记为 WARN 而非 FAIL
                mark = 'WARN 少%d' % (want - got)
                bad += 1
            else:
                mark = 'FAIL 多%d' % (got - want)
                bad += 1
            print('%d  T%d   %4s    %4d     %s'
                  % (y, t, want if want is not None else '?', got, mark))

    print('-' * 44)
    print('不一致 %d 项' % bad)
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
