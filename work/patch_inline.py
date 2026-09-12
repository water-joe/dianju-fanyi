# -*- coding: utf-8 -*-
"""把「浮层弹窗」改成「就地展开」：
   解析面板插在被点句子的下一行，不再盖住任何文字。
   顺带删掉整套浮层补丁（遮罩/拖拽/高度记忆/重新滚动/底部内边距）。"""
import io

p = 'site/app.js'
s = io.open(p, encoding='utf-8').read()

NEW = '''  /* ================= 就地展开 ================= */
  /* 解析面板直接插在被点句子的下一行（同段落内，块级元素）。
     不遮挡任何文字，因此不需要遮罩、拖拽调高、底部内边距、重新滚动
     这一整套浮层补丁——前几轮踩的坑在结构上不复存在。 */

  function collapsePanel() {
    $$('.inline-panel').forEach(function (el) { el.remove(); });
  }

  function openSentence(id) {
    if (activeSent === id) { closeDrawer(); return; }   // 再点同一句 = 收起
    var s = findSentence(id);
    var el = $('.sent[data-sent-id="' + id + '"]');
    if (!s || !el) return;
    collapsePanel();                 // 同时只开一个，避免页面越撑越长
    activeSent = id;
    highlight(id);
    var panel = buildPanel(s, id);
    panel.dataset.forSent = id;
    el.parentNode.insertBefore(panel, el.nextSibling);
    revealPanel(panel);
  }

  function closeDrawer() {
    activeSent = null;
    highlight(null);
    collapsePanel();
  }

  /* 展开后若面板超出视口，滚到「顶栏下方」能看全的位置 */
  function revealPanel(panel) {
    requestAnimationFrame(function () {
      var r = panel.getBoundingClientRect();
      var topbar = 66;
      if (r.bottom > window.innerHeight - 24 || r.top < topbar) {
        window.scrollTo({
          top: Math.max(0, r.top + window.scrollY - topbar - 12),
          behavior: 'smooth'
        });
      }
    });
  }

  function section(title) {
    var d = document.createElement('div');
    d.className = 'ip-sec';
    var h = document.createElement('h3');
    h.textContent = title;
    d.appendChild(h);
    return d;
  }

  function buildPanel(s, id) {
    var panel = document.createElement('div');
    panel.className = 'inline-panel';

    var head = document.createElement('div');
    head.className = 'ip-head';
    var bid = document.createElement('span');
    bid.className = 'ip-id'; bid.textContent = id;
    head.appendChild(bid);
    var ttl = document.createElement('span');
    ttl.className = 'ip-title';
    ttl.textContent = s.insight ? '真题精讲句' : '逐句精读';
    head.appendChild(ttl);
    var hint = document.createElement('span');
    hint.className = 'ip-hint'; hint.textContent = '↑↓ 换句 · Esc 收起';
    head.appendChild(hint);
    var x = document.createElement('button');
    x.type = 'button'; x.className = 'ip-close'; x.textContent = '\\u00d7';
    x.setAttribute('aria-label', '收起');
    x.addEventListener('click', closeDrawer);
    head.appendChild(x);
    panel.appendChild(head);

    var body = document.createElement('div');
    body.className = 'ip-body';
    var cols = document.createElement('div');
    cols.className = 'ip-cols';
    var colL = document.createElement('div');
    var colR = document.createElement('div');
    cols.appendChild(colL); cols.appendChild(colR);
    body.appendChild(cols);

    /* 左栏：本句译文 + 成分划分。
       不再重复英文原句——它就在面板正上方，重复一遍纯属浪费空间。 */
    if (s.zh) {
      var s0 = section('本句翻译');
      var pz = document.createElement('p');
      pz.className = 'ip-zh';
      pz.textContent = s.zh;
      s0.appendChild(pz);
      colL.appendChild(s0);
    }

    if (s.chunks && s.chunks.length) {
      var s2 = section('成分划分 · ' + s.chunks.length + ' 个成分');
      var box = document.createElement('div');
      box.className = 'chunks';
      s.chunks.forEach(function (c) {
        var col = roleColor(c.role);
        var ch = document.createElement('div');
        ch.className = 'chunk';
        var r = document.createElement('div');
        r.className = 'ck-role';
        r.style.background = col;
        r.textContent = c.role;
        ch.appendChild(r);
        var t = document.createElement('div');
        t.className = 'ck-txt';
        t.textContent = c.text;
        ch.appendChild(t);
        if (c.note) {
          var n = document.createElement('div');
          n.className = 'ck-note';
          n.textContent = c.note;
          ch.appendChild(n);
        }
        box.appendChild(ch);
      });
      s2.appendChild(box);
      colL.appendChild(s2);
    }

    /* 右栏：整句着色对照 + 配色说明 + 考点 */
    if (s.chunks && s.chunks.length) {
      var s3 = section('整句对照');
      var sk = document.createElement('div');
      sk.className = 'skel';
      sk.appendChild(coloredSentence(s, s.chunks));
      s3.appendChild(sk);

      var seen = {}, lg = document.createElement('div');
      lg.className = 'chunk-legend';
      lg.style.marginTop = '14px';
      s.chunks.forEach(function (c) {
        if (seen[c.role]) return;
        seen[c.role] = 1;
        var it = document.createElement('span');
        it.className = 'cl-item';
        var dot = document.createElement('span');
        dot.className = 'cl-dot';
        dot.style.background = roleColor(c.role);
        it.appendChild(dot);
        it.appendChild(document.createTextNode(c.role));
        lg.appendChild(it);
      });
      s3.appendChild(lg);
      colR.appendChild(s3);
    }

    if (s.insight && s.note) {
      var s4 = section('考点讲解');
      var nb = document.createElement('div');
      nb.className = 'note-box';
      var tg = document.createElement('div');
      tg.className = 'nb-tag';
      tg.textContent = 'PDF \\u00b7 真题句逐层精讲';
      nb.appendChild(tg);
      nb.appendChild(document.createTextNode(s.note));
      s4.appendChild(nb);
      colR.appendChild(s4);
    }

    panel.appendChild(body);
    return panel;
  }

  /* ---------- \\u2191\\u2193 换句 ---------- */
  var ORDER = [];
  function buildOrder() {
    ORDER = [];
    P.paragraphs.forEach(function (p) {
      p.sentences.forEach(function (s) { ORDER.push(s.id); });
    });
  }
  function step(delta) {
    if (!ORDER.length) return;
    var i = activeSent ? ORDER.indexOf(activeSent) : -1;
    if (i < 0) { openSentence(ORDER[0]); return; }
    var j = i + delta;
    if (j < 0 || j >= ORDER.length) return;
    openSentence(ORDER[j]);
  }

'''

a = s.index('  /* ================= 抽屉 ================= */')
b = s.index('  /* ================= 词汇表 ================= */')
s = s[:a] + NEW + s[b:]
print('OK 1: 浮层机制整段替换为就地展开')

old_p = "      var en = document.createElement('p');\n      en.className = 'en';"
new_p = ("      // 用 div 而非 p：解析面板是块级元素，要插进这个容器里\n"
         "      var en = document.createElement('div');\n      en.className = 'en';")
assert old_p in s, 'renderPassage 的 <p> 未匹配'
s = s.replace(old_p, new_p, 1)
print('OK 2: 段落容器 <p> 改为 <div>（面板可插入）')

old_h = "    buildOrder();\n    setSheetH(sheetH ? Number(sheetH) : null);   // 恢复上次拖拽的高度\n"
assert old_h in s, 'show() 高度恢复未匹配'
s = s.replace(old_h, "    buildOrder();\n", 1)
print('OK 3: 移除弹窗高度恢复')

a2 = s.index('    // 点弹窗与正文之外的地方关闭')
b2 = s.index("  }\n\n  if (document.readyState === 'loading')")
NEW2 = """    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeDrawer(); return; }
      // \\u2191\\u2193 在句子间移动；输入框里不劫持
      var tag = (e.target && e.target.tagName) || '';
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
      if (activeSent && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
        e.preventDefault();
        step(e.key === 'ArrowDown' ? 1 : -1);
      }
    });
"""
s = s[:a2] + NEW2 + s[b2:]
print('OK 4: 移除遮罩关闭，键盘逻辑改判 activeSent')

io.open(p, 'w', encoding='utf-8').write(s)
print('\napp.js 现在 %d 行' % s.count('\n'))
