/* 点句翻译 — 逻辑
   纯静态：不使用 fetch / import / XMLHttpRequest，双击 index.html 即可运行。
   数据通过 <script> 标签注入全局变量。 */
(function () {
  'use strict';

  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ================= 成分 → 颜色 ================= */
  var ROLE_COLORS = {
    '主语': '#2563eb', '谓语': '#dc2626', '宾语': '#059669', '表语': '#7c3aed',
    '定语': '#0891b2', '状语': '#ca8a04', '补语': '#db2777', '同位语': '#4f46e5',
    '插入语': '#78716c', '连接词': '#94a3b8',
    '形式主语': '#1d4ed8', '形式宾语': '#1d4ed8',
    '宾语从句': '#16a34a', '定语从句': '#06b6d4', '状语从句': '#eab308',
    '主语从句': '#3b82f6', '表语从句': '#a855f7', '同位语从句': '#6366f1',
    '主语补足语': '#ec4899', '宾语补足语': '#f43f5e',
    '关系代词': '#0d9488', '关系副词': '#0e7490',
    '非谓语': '#f97316', '独立主格': '#a16207'
  };
  var FALLBACK = ['#0ea5e9', '#22c55e', '#f59e0b', '#a855f7', '#ef4444',
                  '#14b8a6', '#f97316', '#3b82f6', '#84cc16', '#e11d48'];

  function hash(s) {
    var h = 0;
    for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) >>> 0; }
    return h;
  }
  // 未知成分也能拿到稳定颜色，新增成分不会退化成灰色
  function roleColor(role) {
    return ROLE_COLORS[role] || FALLBACK[hash(role) % FALLBACK.length];
  }

  /* ================= 加粗 + 悬浮释义 ================= */
  /* bold 现为 [{text, gloss}]。同样按文本节点走，不用 innerHTML。
     大小写不敏感；同一子串只取首次出现；重叠的跳过。 */
  function normalizeBold(bolds) {
    return (bolds || []).map(function (b) {
      return (typeof b === 'string') ? { text: b, gloss: '' } : b;
    }).filter(function (b) { return b && b.text; });
  }

  function splitBold(text, bolds) {
    var hay = text.toLowerCase();
    var marks = [];
    normalizeBold(bolds).forEach(function (b) {
      var t = String(b.text);
      var i = hay.indexOf(t.toLowerCase());
      if (i >= 0) marks.push({ start: i, end: i + t.length, gloss: b.gloss || '' });
    });
    marks.sort(function (a, b) { return a.start - b.start || b.end - a.end; });
    var picked = [], last = -1;
    marks.forEach(function (m) {
      if (m.start >= last) { picked.push(m); last = m.end; }
    });
    var out = [], pos = 0;
    picked.forEach(function (m) {
      if (m.start > pos) out.push({ t: text.slice(pos, m.start), b: false });
      out.push({ t: text.slice(m.start, m.end), b: true, gloss: m.gloss });
      pos = m.end;
    });
    if (pos < text.length) out.push({ t: text.slice(pos), b: false });
    return out;
  }

  function sentenceNodes(s) {
    var frag = document.createDocumentFragment();
    splitBold(s.en, s.bold).forEach(function (p) {
      if (!p.t) return;
      if (p.b) {
        var st = document.createElement('strong');
        st.textContent = p.t;
        if (p.gloss) {
          st.classList.add('gloss');
          st.dataset.gloss = p.gloss;
          st.tabIndex = 0;                  // 键盘也能聚焦查看
        }
        frag.appendChild(st);
      } else {
        frag.appendChild(document.createTextNode(p.t));
      }
    });
    return frag;
  }

  /* 把整句按成分染色：返回 DocumentFragment。
     未被子串覆盖的词（标点、冠词等）按原文保留，所以读出来仍是完整句子。 */
  function coloredSentence(s, chunks) {
    var text = s.en, frag = document.createDocumentFragment();
    var marks = [], pos = 0;
    chunks.forEach(function (c) {
      var i = text.indexOf(c.text, pos);
      if (i < 0) i = text.indexOf(c.text);        // 兜底：乱序时从头找
      if (i < 0) return;
      marks.push({ start: i, end: i + c.text.length, c: c });
      pos = i + c.text.length;
    });
    pos = 0;
    marks.forEach(function (m) {
      if (m.start > pos) frag.appendChild(document.createTextNode(text.slice(pos, m.start)));
      var col = roleColor(m.c.role);
      var sp = document.createElement('span');
      sp.className = 'sk';
      sp.title = m.c.role + (m.c.note ? ' · ' + m.c.note : '');
      sp.style.background = hexA(col, .18);
      sp.style.borderBottomColor = col;
      sp.textContent = text.slice(m.start, m.end);
      frag.appendChild(sp);
      pos = m.end;
    });
    if (pos < text.length) frag.appendChild(document.createTextNode(text.slice(pos)));
    return frag;
  }

  /* #rrggbb → rgba()，用于低透明度底纹 */
  function hexA(hex, a) {
    var h = hex.replace('#', '');
    if (h.length === 3) h = h[0] + h[0] + h[1] + h[1] + h[2] + h[2];
    var n = parseInt(h, 16);
    return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')';
  }

  /* ================= 悬浮释义（自定义 tooltip） ================= */
  /* 不用原生 title：它要悬停约 1 秒才出现，读句子时太慢。 */
  var tip = null;
  function ensureTip() {
    if (!tip) {
      tip = document.createElement('div');
      tip.className = 'gloss-tip';
      tip.setAttribute('role', 'tooltip');
      tip.hidden = true;
      document.body.appendChild(tip);
    }
    return tip;
  }

  function showTip(el) {
    var g = el.dataset.gloss;
    if (!g) return;
    var t = ensureTip();
    t.textContent = g;
    t.hidden = false;

    var r = el.getBoundingClientRect();
    var tw = t.offsetWidth, th = t.offsetHeight;
    var vw = window.innerWidth, vh = window.innerHeight;

    // 默认在词下方；下方放不下就翻到上方
    var top = r.bottom + 8;
    if (top + th > vh - 8) top = r.top - th - 8;
    if (top < 4) top = 4;

    var left = r.left + r.width / 2 - tw / 2;
    left = Math.max(8, Math.min(vw - tw - 8, left));

    t.style.top = top + 'px';
    t.style.left = left + 'px';
    t.classList.toggle('above', top < r.top);
  }

  function hideTip() { if (tip) tip.hidden = true; }

  function wireGloss() {
    document.addEventListener('mouseover', function (e) {
      var el = e.target.closest ? e.target.closest('.gloss') : null;
      if (el) showTip(el);
    });
    document.addEventListener('mouseout', function (e) {
      var el = e.target.closest ? e.target.closest('.gloss') : null;
      if (el) hideTip();
    });
    // 键盘可达
    document.addEventListener('focusin', function (e) {
      var el = e.target.closest ? e.target.closest('.gloss') : null;
      if (el) showTip(el); else hideTip();
    });
    document.addEventListener('focusout', hideTip);
    window.addEventListener('scroll', hideTip, true);
    window.addEventListener('resize', hideTip);
  }

  /* ================= 状态 ================= */
  var P = null;                 // 当前篇目数据
  var activeSent = null;        // 当前选中句 id

  /* ================= 渲染正文 ================= */
  function renderPassage() {
    var host = $('#passage');
    host.textContent = '';

    P.paragraphs.forEach(function (para) {
      var sec = document.createElement('section');
      sec.className = 'para';

      var head = document.createElement('div');
      head.className = 'para-head';
      var pid = document.createElement('span');
      pid.className = 'para-id';
      // 用 ¶ 段落符而非 "P1"：P1 容易被读成「第 1 题」
      pid.textContent = '¶' + String(para.id).replace(/^P/, '');
      head.appendChild(pid);
      sec.appendChild(head);

      // 用 div 而非 p：解析面板是块级元素，要插进这个容器里
      var en = document.createElement('div');
      en.className = 'en';
      para.sentences.forEach(function (s, i) {
        // 精讲句渲染成真链接（href 指向原站该句解析页）：
        // 于是右键、中键、状态栏预览都是原生行为；
        // 普通左键则在 onPassageClick 里被拦截，改为就地展开成分。
        var span;
        if (s.url) {
          span = document.createElement('a');
          span.href = s.url;
          span.target = '_blank';
          span.rel = 'noopener noreferrer';
        } else {
          span = document.createElement('span');
        }
        span.className = 'sent' + (s.insight ? ' insight' : '');
        span.dataset.sentId = s.id;
        span.appendChild(sentenceNodes(s));
        span.title = (s.insight ? '真题精讲句 · ' : '') +
                     '点击展开成分划分' +
                     (s.url ? '\nCtrl/⌘+点击 或中键 → 打开原站解析页' : '');
        en.appendChild(span);
        if (i < para.sentences.length - 1) en.appendChild(document.createTextNode(' '));
      });
      sec.appendChild(en);

      // 译文常显，且按正文样式排（不是灰色脚注）。
      // 目标是读起来就是一篇正常的中英对照文章，而不是"要操作才能看"的题面。
      var zh = document.createElement('p');
      zh.className = 'zh';
      zh.textContent = para.zh;
      sec.appendChild(zh);

      host.appendChild(sec);
    });
  }

  function onPassageClick(e) {
    var el = e.target.closest ? e.target.closest('.sent') : null;
    if (!el) return;
    // 精讲句是 <a>：带修饰键的点击（新标签打开）交给浏览器原生处理，
    // 只拦截普通左键，改为就地展开成分。
    if (el.tagName === 'A' && (e.metaKey || e.ctrlKey || e.shiftKey)) return;
    // 加粗词同样属于句子：悬浮看释义，点击照常展开本句成分。
    // （早先这里对 .gloss 提前 return，导致点到加粗词什么都不发生——
    //   而加粗词遍布全篇，等于大半个句子点不动。）
    e.preventDefault();          // 阻止 <a> 默认跳转
    openSentence(el.dataset.sentId);
  }

  function findSentence(id) {
    for (var i = 0; i < P.paragraphs.length; i++) {
      var ss = P.paragraphs[i].sentences;
      for (var j = 0; j < ss.length; j++) if (ss[j].id === id) return ss[j];
    }
    return null;
  }

  function highlight(id) {
    $$('.sent').forEach(function (el) {
      el.classList.toggle('active', el.dataset.sentId === id);
    });
  }

  /* ================= 就地展开 ================= */
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
    keepAnchorVisible(el, panel);
  }

  function closeDrawer() {
    activeSent = null;
    highlight(null);
    collapsePanel();
  }

  /* rAF 兜底：极少数嵌入环境（老 WebView、jsdom 等）没有它，
     缺了就会在展开时抛错。退化成 setTimeout 即可。 */
  var raf = (typeof window !== 'undefined' && window.requestAnimationFrame)
    ? window.requestAnimationFrame.bind(window)
    : function (f) { return setTimeout(f, 16); };

  /* 面板就地展开后，以「被点的那句」为锚，保证它仍在视口内。
     不滚到面板顶部：长面板比视口还高时，那样会把锚句推到屏幕外，
     反而让人不知道在看哪一句。 */
  function keepAnchorVisible(el, panel) {
    raf(function () {
      var topbar = 70;
      var r = el.getBoundingClientRect();
      var anchorVisible = r.top >= topbar && r.top < window.innerHeight - 40;
      if (anchorVisible) return;                 // 锚句已在视野内，不动
      // 锚句被遮住或在视口下方 → 滚到顶栏下方一点的位置
      var want = r.top + window.scrollY - topbar - 10;
      window.scrollTo({ top: Math.max(0, want), behavior: 'smooth' });
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
    x.type = 'button'; x.className = 'ip-close'; x.textContent = '\u00d7';
    x.setAttribute('aria-label', '收起');
    x.addEventListener('click', closeDrawer);
    head.appendChild(x);
    panel.appendChild(head);

    var body = document.createElement('div');
    body.className = 'ip-body';

    /* 单栏全宽。
       曾用左右两栏，结果长句成分块被挤成竖条（每栏仅约 370px），
       「主语」「宾语」这些长成分几乎没法读。
       成分块本来就是横向流式排布，给足宽度才排得开。 */
    var colL = body;
    var colR = body;

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
      tg.textContent = 'PDF \u00b7 真题句逐层精讲';
      nb.appendChild(tg);
      nb.appendChild(document.createTextNode(s.note));
      s4.appendChild(nb);
      colR.appendChild(s4);
    }
    /* 该句在原站的完整解析页。只有「真题句逐层精讲」选中的句子
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
      ar.textContent = '\u2197';
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
    colR.appendChild(s5);

    panel.appendChild(body);
    return panel;
  }

  /* ---------- \u2191\u2193 换句 ---------- */
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

  /* ================= 词汇表 ================= */
  var vSort = { key: 'freq', desc: true };

  function renderVocab() {
    var q = ($('#vocab-filter').value || '').trim().toLowerCase();
    var all = (P.vocab || []).filter(function (v) {
      if (!q) return true;
      return (v.word + ' ' + v.cn + ' ' + v.level + ' ' + v.pos).toLowerCase().indexOf(q) >= 0;
    });
    all.sort(function (a, b) {
      var x = a[vSort.key], y = b[vSort.key], r;
      if (typeof x === 'number') r = x - y;
      else r = String(x).localeCompare(String(y));
      return vSort.desc ? -r : r;
    });

    // 词表始终完整渲染，靠固定高度 + 内部滚动控制篇幅。
    // 滚动条本身就是「还有更多」的提示，比按钮更直观，也少一个控件。
    var rows = all;

    var tb = $('#vocab tbody');
    tb.textContent = '';
    if (!all.length) {
      var tr0 = document.createElement('tr');
      var td0 = document.createElement('td');
      td0.colSpan = 6; td0.className = 'empty'; td0.textContent = '没有匹配的单词';
      tr0.appendChild(td0); tb.appendChild(tr0);
      $('#vocab-count').textContent = '· 无匹配';
      return;
    }
    rows.forEach(function (v) {
      var tr = document.createElement('tr');

      var w = document.createElement('td');
      var ws = document.createElement('span');
      ws.className = 'v-word'; ws.textContent = v.word;
      w.appendChild(ws); tr.appendChild(w);

      var l = document.createElement('td');
      var bd = document.createElement('span');
      bd.className = 'badge lv-' + v.level; bd.textContent = v.level;
      l.appendChild(bd); tr.appendChild(l);

      var p = document.createElement('td');
      p.className = 'v-pos'; p.textContent = v.pos || '';
      tr.appendChild(p);

      var c = document.createElement('td');
      c.textContent = v.cn || ''; tr.appendChild(c);

      var n = document.createElement('td');
      n.className = 'num'; n.textContent = v.count; tr.appendChild(n);

      var f = document.createElement('td');
      f.className = 'num'; f.textContent = v.freq; tr.appendChild(f);

      tb.appendChild(tr);
    });

    var total = (P.vocab || []).length;
    var n = $('#vocab-count');
    n.textContent = q
      ? '· 匹配 ' + all.length + ' / ' + total + ' 词'
      : '· ' + total + ' 词（按真题句频，可滚动）';
    syncVocabFadeNextFrame();
  }

  /* 底部渐隐：内容还能往下滚时显示，滚到底就隐藏。
     没有它的话，被切断的半行看起来像渲染错误。
     注意：刚渲染完那一瞬间表格还没完成布局（scrollHeight === clientHeight），
     此时算出来「已到底」是错的，所以要等一帧再算一次。 */
  function syncVocabFade() {
    var frame = $('.vocab-frame');
    var wrap = $('.vocab-wrap');
    if (!frame || !wrap) return;
    var more = wrap.scrollHeight - wrap.scrollTop - wrap.clientHeight > 4;
    frame.classList.toggle('at-end', !more);
  }
  function syncVocabFadeNextFrame() {
    syncVocabFade();
    raf(function () { raf(syncVocabFade); });
  }

  var vocabWired = false;
  function wireVocab() {
    if (vocabWired) return;      // show() 每次切换篇目都会调用，避免重复绑定
    vocabWired = true;
    $$('#vocab th.sortable').forEach(function (th) {
      th.addEventListener('click', function () {
        var k = th.dataset.sort;
        if (vSort.key === k) vSort.desc = !vSort.desc;
        else { vSort.key = k; vSort.desc = (k === 'count' || k === 'freq'); }
        $$('#vocab th.sortable').forEach(function (o) {
          o.classList.toggle('sorted', o === th);
          o.classList.toggle('desc', o === th && vSort.desc);
        });
        renderVocab();
      });
    });
    // 默认高亮排序表头
    var dth = $('#vocab th[data-sort="freq"]');
    if (dth) { dth.classList.add('sorted', 'desc'); }
    $('#vocab-filter').addEventListener('input', renderVocab);
    // 滚动时更新底部渐隐
    var wrap = $('.vocab-wrap');
    if (wrap) wrap.addEventListener('scroll', syncVocabFade, { passive: true });
    window.addEventListener('resize', syncVocabFade);
  }

  /* ================= 载入篇目 ================= */
  function show(P_data) {
    P = P_data;
    var nSent = 0, nIns = 0;
    P.paragraphs.forEach(function (p) {
      nSent += p.sentences.length;
      p.sentences.forEach(function (s) { if (s.insight) nIns++; });
    });
    $('#p-title').textContent = P.title || '';
    $('#p-sub').textContent = P.subtitle || '';
    var stats = $('#p-stats');
    stats.textContent = '';
    stats.appendChild(document.createTextNode(
      P.paragraphs.length + ' 段 · ' + nSent + ' 句 · 其中 ' + nIns + ' 句真题精讲 · ' +
      (P.vocab || []).length + ' 个高频词'));
    if (P.source) {
      stats.appendChild(document.createTextNode(' · 来源 '));
      var sa = document.createElement('a');
      sa.className = 'src-link';
      sa.href = P.source;
      sa.target = '_blank';
      sa.rel = 'noopener noreferrer';
      sa.textContent = '原站本篇解析页 ↗';
      stats.appendChild(sa);
    }

    renderPassage();
    renderVocab();
    wireVocab();
    buildOrder();
    closeDrawer();
    $('#loading').hidden = true;
    $('#main').hidden = false;
  }

  function loadByScript(file, done) {
    var sc = document.createElement('script');
    sc.src = file;
    sc.onload = done;
    sc.onerror = function () {
      $('#loading').textContent = '载入失败：' + file;
    };
    document.body.appendChild(sc);
  }

  function boot() {
    var lib = window.LIBRARY || [];
    var sel = $('#paper');
    if (!lib.length) {
      // 没有清单时退化为直接使用已注入的 PASSAGE
      lib = [{ id: 'current', label: (window.PASSAGE && window.PASSAGE.title) || '当前篇目' }];
    }
    lib.forEach(function (it) {
      var o = document.createElement('option');
      o.value = it.id; o.textContent = it.label;
      sel.appendChild(o);
    });

    function use(entry) {
      var d = (entry && entry.file) ? null : window.PASSAGE;
      if (!d) return;
      show(d);
    }

    function pick(entry, first) {
      if (!entry || !entry.file) { use(entry); return; }
      if (window.PASSAGE && window.PASSAGE._src === entry.file && !first) { show(window.PASSAGE); return; }
      $('#loading').hidden = false;
      $('#loading').textContent = '正在载入 ' + entry.label + '…';
      $('#main').hidden = true;
      loadByScript(entry.file, function () {
        if (window.PASSAGE) { window.PASSAGE._src = entry.file; show(window.PASSAGE); }
        else { $('#loading').textContent = '数据文件未设置 window.PASSAGE：' + entry.file; }
      });
    }

    sel.addEventListener('change', function () {
      var e = lib.filter(function (x) { return x.id === sel.value; })[0];
      pick(e, false);
    });

    // 首个篇目
    var first = lib[0];
    if (first && first.file) {
      if (window.PASSAGE) { window.PASSAGE._src = first.file; show(window.PASSAGE); }
      else pick(first, true);
    } else { show(window.PASSAGE); }

    /* 全局控件 */
    $('#passage').addEventListener('click', onPassageClick);
    wireGloss();

    // 译文默认常显（读起来像一篇对照文章）。这个按钮用来「只看英文」——
    // 想自己先读一遍原文、不被译文带跑时用得上。
    var zhHidden = false;
    $('#btn-all-zh').addEventListener('click', function () {
      zhHidden = !zhHidden;
      this.classList.toggle('on', zhHidden);
      this.textContent = zhHidden ? '显示译文' : '只看英文';
      $$('.para .zh').forEach(function (zh) { zh.hidden = zhHidden; });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeDrawer(); return; }
      // \u2191\u2193 在句子间移动；输入框里不劫持
      var tag = (e.target && e.target.tagName) || '';
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
      if (activeSent && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) {
        e.preventDefault();
        step(e.key === 'ArrowDown' ? 1 : -1);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else { boot(); }
})();
