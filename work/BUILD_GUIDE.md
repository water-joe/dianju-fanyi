# 加一篇的「成分划分」工序指南（给本次批处理用）

本项目是考研英语二精读站，纯静态。每篇需要你**逐句手写**语法成分划分与重点词释义，
这是唯一无法自动化的部分（PDF 无逐词成分标注，网页版结构树打印时丢失）。

你被指派负责 **一篇** text。最终产物 = 5 个文件 + 跑通生成器（0 个问题）。

## 必读：项目口径（用户已确认，照做别改）

1. **嵌套成分合并为一块**，子结构写进该 chunk 的 `note`。
   - 例：`the number of people interested in the field` 整体标「宾语」，note 注
     「interested in the field 为过去分词短语作后置定语」。
   - **不要**拆成并排两块（会导致字数重复计算、覆盖率 >100%）。
   - 注意：方式状语若与定语从句重叠，必须把方式状语放进定语从句 chunk 内部，
     否则覆盖率会算成 128%（这是踩过的真错）。
2. **引述分句各标各的主谓语**，不整体收进一个「引述分句」块。
   - 例：`Students ... can catch up, said Tom Cortina, the assistant dean...`
     出现两组「主语/谓语」：主句一组，`said` + `Tom Cortina` 一组，
     `the assistant dean...` 标「同位语」。屏幕上同时出现两个「主语」标签是允许的。

## 输入素材

读 `work/raw/{YEAR}-text{N}.json`（绝对路径：`C:/Users/Joseph/Downloads/点句翻译/work/raw/`）。结构：
- `paragraphs`: 每段的 `id`（P1..）、`en`（英文）、`zh`（中文译文）、`sentences`（含 `id` P1S1.. 和 `en`）。
- `insights`: 列表，每项 `{para, sent, en, note}` —— **这是 PDF 精讲句标记**。
  `note` 是考点文字，已提取好，直接填进对应句子的 `note`。
- `vocab`: 高频词表 `[{word, level, pos, cn, count, freq}]`，生成器自动采用，你不用管。

你的任务只处理 `sentences`。句子英文和中文译文都以 `raw` 为准，**不要自己翻译或改写英文**。

## 产物文件（放在 `work/` 下，绝对路径 `C:/Users/Joseph/Downloads/点句翻译/work/`）

把 ~8 句分成三份文件，避免单文件过大：

- `t{YY}_{N}_a.py`  —— 前半句子
- `t{YY}_{N}_b.py`  —— 中间句子
- `t{YY}_{N}_c.py`  —— 后半句子
- `t{YY}_{N}_gloss.py` —— 所有 bold 词的释义表（集中一个文件）
- `gen_t{YY}_{N}.py` —— 生成器（见下）

### 单个成分数据文件格式（`_a/_b/_c.py`）

```python
# -*- coding: utf-8 -*-
# 2021 考研英语二 Text 3 —— 成分划分（前半）
A = {}
A['P1S1'] = dict(
    zh='<本句中文译文，从 raw 的 zh/句子上下文照搬，不要自己译>',
    insight=False, note='',
    bold=['paradoxical'],          # 重点词/词组，必须是 en 的连续子串（大小写不敏感匹配）
    chunks=[
        dict(role='主语', text='Teenagers'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='paradoxical'),
    ])
A['P1S2'] = dict(
    zh='...',
    insight=True,                 # 仅当 (para,sent) 在 insights 列表里时为 True
    note='<从 raw insights 里搬对应 note 文字>',
    bold=['detached', 'express'],
    chunks=[...])
```

要点：
- `zh`：每个 `_a/_b/_c.py` 里的 `zh` 必须是该句对应的中文译文。译文在 raw 的段落 `zh` 里（整段译文），
  你需要把整段译文按句子切分，给每句配正确的那句译文。若拿不准某句译文边界，
  就以 raw 段落 `zh` 为准、合理断句；保证每句都有通顺的中文。
- `insight`：仅当该句 `(para 序号, 句序)` 出现在 raw `insights` 列表中才 `True`。
- `note`：当 `insight=True`，把 raw `insights` 中对应项的 `note` 原文搬入；
  当 `insight=False`，`note=''`。
- `bold`：选 2–5 个本句重点词/词组（考研核心词、搭配、易错结构词）。**必须是 `en` 里的连续子串**
  （允许大小写差异，生成器用 `lower()` 比对）。例：`take care of`、`published`、`go hand in hand`。
  不要选纯标点或空格。每个 bold 都必须在 `gloss` 里有释义。
- `chunks`：按英文**出现顺序**排列。每个 `text` 必须是 `en` 里的连续子串（**精确、含标点与空格**）。
  常见 role 值：主语 / 谓语 / 宾语 / 表语 / 定语 / 定语从句 / 状语 / 同位语(从句) / 连接词 /
  宾语从句 / 主语从句 / 同位语从句 / 插入语 / 补语。未知成分用中文描述性 role 即可，
  `app.js` 的 `roleColor` 会 hash 兜底取色，不会退化成灰色。
- 覆盖率（`cover`）越高越好，但**绝不能 >100%**。合并嵌套成分就能避免超限。
  正常应在 60%–100% 之间。生成器会打印每句 cover。

### 释义文件（`_gloss.py`）

```python
# -*- coding: utf-8 -*-
# 2021 考研英语二 Text 3 —— 重点词释义
GLOSS = {
    'paradoxical': 'adj. 矛盾的；似非而是的',
    'detached': 'adj. 超然的；客观的；分离的',
    'express': 'v. 表达；表示',
    # ... 覆盖本 text 所有 _a/_b/_c 里出现的 bold
}
```
要求：字典 key 与 `_a/_b/_c` 里每个 `bold` 字符串**完全一致**（含大小写、空格），
否则生成器报 `NO GLOSS`。释义写「词性 + 中文义」，考研语境优先。

## 强烈建议：用「repr 转义生成器」写数据（避免引号踩坑）

直接手写 `_a/_b/_c.py` 里的 `text='...'` 时，原文中的撇号（`students'`、`don't`）
和引文里的双引号会把 Python 字符串截断，产生一堆 `SyntaxError` 且极难逐条修。
**推荐做法**：写一个临时脚本 `work/_tmp_t{YY}_{N}.py`，在**内存里用 dict 定义**
所有句子，再用 `repr()` 写出 `_a/_b/_c.py` 与 `_gloss.py`。`repr` 会自动转义，
彻底杜绝引号问题。写完后删除临时脚本。骨架：

```python
# -*- coding: utf-8 -*-
import io
A = {}
A['P1S1'] = dict(
    zh=u'……', insight=True, note=u'……',
    bold=['…'],
    chunks=[dict(role='主语', text='…', note='…'), ...])
# …… 所有句子 ……

def dump(name, d):
    lines = ['# -*- coding: utf-8 -*-', 'A = {}', '']
    for k, v in d.items():
        lines.append('A[%r] = dict(' % k)
        lines.append('    zh=%r,' % v['zh'])
        lines.append('    insight=%r, note=%r,' % (v['insight'], v.get('note', '')))
        lines.append('    bold=%r,' % (v['bold'],))
        lines.append('    chunks=[')
        for c in v['chunks']:
            lines.append('        dict(role=%r, text=%r,' % (c['role'], c['text']))
            lines.append('             note=%r),' % c.get('note', ''))
        lines.append('    ])'); lines.append('')
    io.open(name, 'w', encoding='utf-8').write('\n'.join(lines))

dump('t{YY}_{N}_a.py', {k: A[k] for k in [...]})   # 前 1/3
dump('t{YY}_{N}_b.py', {k: A[k] for k in [...]})   # 中 1/3
dump('t{YY}_{N}_c.py', {k: A[k] for k in [...]})   # 后 1/3
# GLOSS 同理：用 repr 写出 t{YY}_{N}_gloss.py
```

**两个极易踩的坑（现有 29 篇都遇到过）**：
- `bold` 必须是原文的**连续子串**。不要写 `tie... to`、`perceived... as`、
  `bring... to life` 这种省略号写法——直接写 `tie CEO pay to` 或 `perceived`。
- 状语插在谓词中间（`are often not connected to`、`has largely fizzled out`）时，
  要么整段作为一个 chunk，要么拆成「谓语 + 插入语 + 谓语」，**不能**只取中间片段，
  否则不是子串。同理，`as expected,` 这类插入语在原文里的位置要按实际顺序排 chunk。

### 生成器（`gen_t{YY}_{N}.py`）

照抄 `gen_t23_4.py`（绝对路径 `C:/Users/Joseph/Downloads/点句翻译/work/gen_t23_4.py`），
改动点：
- 顶部 `from t{YY}_{N}_a import A as A1` / `_b` / `_c`；`from t{YY}_{N}_gloss import GLOSS`
- `YEAR, TEXT = {YY}, {N}`
- `subtitle='<本 text 的中文主题，一两句概括，参考已有 data 文件的 subtitle 风格>'`
- 其余（校验、写文件）原样保留。

## 完成标准（必须自检）

在 `C:/Users/Joseph/Downloads/点句翻译` 目录下运行：
```
python work/gen_t{YY}_{N}.py
```
要求：
1. 退出码 0（即 `PROBLEMS (0)`）。
2. 没有 `BOLD not found` / `CHUNK not found` / `CHUNK out-of-order` / `NO GLOSS` / `MISSING analysis` / `缺考点文字`。
3. 每句 `cover` 都在合理范围（不要 >100%）。若有 >100%，回去合并重叠 chunk。
4. 文件已写入 `site/data/{YY}-text{N}.js`（生成器会自动写）。
5. 把所有句子 id 都覆盖了——`MISSING analysis` 必须为 0。

如果生成器报错，逐条修数据文件直到 0 问题。**不要**为了消除报错而去改 raw 或生成器。
报错的真实含义是：你写的 `bold`/`chunk` 文本与 PDF 原文对不上（多/少空格、标点、大小写、漏词）。

完成后，用一句话向我汇报：text 编号、段数、句数、精讲句数、重点词数、平均覆盖率，以及退出码。
