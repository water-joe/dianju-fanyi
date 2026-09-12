# -*- coding: utf-8 -*-
"""在解析面板里加入「完整解析」区块：链接到该句在原站的解析页。
   只有真题精讲句才有这种页面（实测 200），其余句子是 404，故渲染成说明文字。"""
import io

p = 'site/app.js'
s = io.open(p, encoding='utf-8').read()

# 用行锚点定位，避开文件里的 \\u00b7 转义字面量
lines = s.split('\n')
start = None
for i, ln in enumerate(lines):
    if ln.strip() == 'if (s.insight && s.note) {':
        start = i
        break
assert start is not None, '未找到 note-box 区块'
end = start
while lines[end].strip() != '}':
    end += 1
print('note-box 区块: 第 %d - %d 行' % (start + 1, end + 1))

NEW = '''    /* 该句在原站的完整解析页。只有「真题句逐层精讲」选中的句子
       才有这种页面（其余实测 404），所以非精讲句不渲染链接。 */
    var s5 = section('完整解析');
    if (s.url) {
      var a5 = document.createElement('a');
      a5.className = 'ip-ext';
      a5.href = s.url;
      a5.target = '_blank';
      a5.rel = 'noopener noreferrer';
      a5.appendChild(document.createTextNode('打开本句的原站解析页'));
      var ar = document.createElement('span');
      ar.className = 'ip-ext-arrow';
      ar.textContent = '\\u2197';
      a5.appendChild(ar);
      s5.appendChild(a5);
      var tip5 = document.createElement('p');
      tip5.className = 'ip-ext-note';
      tip5.textContent = '原站含结构树、成分与时态详解、真题例句。';
      s5.appendChild(tip5);
    } else {
      var q5 = document.createElement('p');
      q5.className = 'ip-ext-note';
      q5.textContent = '本句未被 PDF 选入「真题句逐层精讲」，原站没有对应的解析页。';
      s5.appendChild(q5);
    }
    colR.appendChild(s5);'''.split('\n')

lines[end + 1:end + 1] = NEW
s = '\n'.join(lines)
io.open(p, 'w', encoding='utf-8').write(s)
print('OK: 已插入「完整解析」区块')
