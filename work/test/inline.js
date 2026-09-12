/* 就地展开模型测试。
   结构上与浮层的关键差别：
   - 面板插在句子「之后、同段落内」，不遮挡任何文字
   - 没有遮罩/拖拽/高度记忆，因此那些 bug 类的断言不再适用
   - 判据：面板与句子的位置关系、正文是否仍可读、点击行为 */
const puppeteer = require('puppeteer');

const URL = 'http://127.0.0.1:8765/';
let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (extra !== undefined ? '  -> ' + extra : '')); }
}

(async () => {
  const b = await puppeteer.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.setViewport({ width: 1280, height: 900, deviceScaleFactor: 1 });
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });

  await p.goto(URL, { waitUntil: 'networkidle0' });
  await p.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await p.reload({ waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 500));

  /* 取句子首段文字的真实矩形再点（多行句子的几何中心会落在行间空白） */
  async function clickSentence(id) {
    const pt = await p.evaluate(sid => {
      const el = document.querySelector('[data-sent-id="' + sid + '"]');
      if (!el) return null;
      el.scrollIntoView({ block: 'center' });
      const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const n = walk.nextNode();
      if (!n || !n.length) return null;
      const rg = document.createRange();
      rg.setStart(n, 0); rg.setEnd(n, Math.min(4, n.length));
      const r = rg.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }, id);
    if (!pt) throw new Error('cannot locate ' + id);
    await p.mouse.click(pt.x, pt.y);
  }

  console.log('\n--- 初始 ---');
  ok('无面板', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 0));
  ok('无浮层残留（drawer/backdrop 已删）',
     await p.evaluate(() => !document.querySelector('#drawer') && !document.querySelector('#backdrop')));

  console.log('\n--- 点句 → 就地展开 ---');
  await clickSentence('P3S1');
  await new Promise(r => setTimeout(r, 500));

  ok('出现 1 个面板', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 1));

  const rel = await p.evaluate(() => {
    const panel = document.querySelector('.inline-panel');
    const sent = document.querySelector('.sent.active');
    const para = sent.closest('.para');
    const pr = panel.getBoundingClientRect(), sr = sent.getBoundingClientRect();
    return {
      panelInsideSamePara: para.contains(panel),
      panelAfterSent: pr.top >= sr.bottom - 2,
      gap: Math.round(pr.top - sr.bottom),
      sharedLeft: Math.abs(pr.left - sr.left) < 40,
    };
  });
  ok('面板在句子所在段落内', rel.panelInsideSamePara);
  ok('面板在句子下方', rel.panelAfterSent, 'gap=' + rel.gap);
  ok('面板与句子左缘对齐（就地感）', rel.sharedLeft);

  console.log('\n--- 关键：不遮挡任何文字 ---');
  const occl = await p.evaluate(() => {
    const panel = document.querySelector('.inline-panel').getBoundingClientRect();
    // 面板矩形是否与任何句子文字重叠
    let hits = 0;
    document.querySelectorAll('.sent').forEach(s => {
      const r = s.getBoundingClientRect();
      const overlap = !(r.bottom <= panel.top || r.top >= panel.bottom ||
                        r.right <= panel.left || r.left >= panel.right);
      if (overlap) hits++;
    });
    return { hits, panelTop: Math.round(panel.top) };
  });
  ok('面板不与任何句子重叠', occl.hits === 0, 'overlap=' + occl.hits);

  console.log('\n--- 面板内容 ---');
  const c = await p.evaluate(() => ({
    id: document.querySelector('.ip-id').textContent,
    title: document.querySelector('.ip-title').textContent,
    chunks: document.querySelectorAll('.inline-panel .chunk').length,
    zh: !!document.querySelector('.inline-panel .ip-zh'),
    skel: document.querySelectorAll('.inline-panel .skel').length,
    note: document.querySelectorAll('.inline-panel .note-box').length,
    legend: document.querySelectorAll('.inline-panel .cl-item').length,
    // 不再重复英文原句
    dupEn: document.querySelectorAll('.inline-panel .dr-en, .inline-panel .ip-en').length,
  }));
  ok('面板 id = P3S1', c.id === 'P3S1', c.id);
  ok('标题为真题精讲句', c.title === '真题精讲句', c.title);
  ok('13 个成分', c.chunks === 13, String(c.chunks));
  ok('本句翻译存在', c.zh);
  ok('整句对照存在', c.skel === 1);
  ok('考点讲解存在', c.note === 1);
  ok('配色说明存在', c.legend > 0, String(c.legend));
  ok('成分块横向流式排布', await p.evaluate(() => {
    const box = document.querySelector('.inline-panel .chunks');
    return getComputedStyle(box).display === 'flex';
  }));
  ok('不再重复英文原句', c.dupEn === 0);

  console.log('\n--- 再点同一句 = 收起 ---');
  await clickSentence('P3S1');
  await new Promise(r => setTimeout(r, 400));
  ok('面板消失', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 0));
  ok('高亮清除', await p.evaluate(() => document.querySelectorAll('.sent.active').length === 0));

  console.log('\n--- 换句：只保留一个面板 ---');
  await clickSentence('P1S1');
  await new Promise(r => setTimeout(r, 400));
  await clickSentence('P5S3');
  await new Promise(r => setTimeout(r, 400));
  const sw = await p.evaluate(() => ({
    n: document.querySelectorAll('.inline-panel').length,
    id: document.querySelector('.inline-panel .ip-id').textContent,
    inPara5: document.querySelector('.inline-panel').closest('.para')
              .querySelector('.para-id').textContent,
  }));
  ok('仍只有 1 个面板', sw.n === 1, String(sw.n));
  ok('面板换到 P5S3', sw.id === 'P5S3', sw.id);
  ok('插在 P5 段落内', sw.inPara5 === '¶5', sw.inPara5);

  console.log('\n--- ↑↓ 换句 ---');
  await p.keyboard.press('ArrowDown');
  await new Promise(r => setTimeout(r, 400));
  ok('↓ → P6S1', (await p.evaluate(() => document.querySelector('.ip-id').textContent)) === 'P6S1');
  await p.keyboard.press('ArrowUp');
  await new Promise(r => setTimeout(r, 400));
  ok('↑ → 回 P5S3', (await p.evaluate(() => document.querySelector('.ip-id').textContent)) === 'P5S3');

  await clickSentence('P6S4');
  await new Promise(r => setTimeout(r, 400));
  await p.keyboard.press('ArrowDown');
  await new Promise(r => setTimeout(r, 350));
  ok('末句 ↓ 不越界', (await p.evaluate(() => document.querySelector('.ip-id').textContent)) === 'P6S4');

  console.log('\n--- 关闭方式 ---');
  await p.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 300));
  ok('Esc 收起', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 0));

  await clickSentence('P2S2');
  await new Promise(r => setTimeout(r, 400));
  ok('重新打开', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 1));
  await p.evaluate(() => document.querySelector('.ip-close').click());
  await new Promise(r => setTimeout(r, 300));
  ok('× 按钮收起', await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 0));

  console.log('\n--- 非精讲句 ---');
  await clickSentence('P1S2');
  await new Promise(r => setTimeout(r, 400));
  const n = await p.evaluate(() => ({
    title: document.querySelector('.ip-title').textContent,
    note: document.querySelectorAll('.inline-panel .note-box').length,
    chunks: document.querySelectorAll('.inline-panel .chunk').length,
  }));
  ok('标题为逐句精读', n.title === '逐句精读', n.title);
  ok('无考点框', n.note === 0, String(n.note));
  ok('成分仍在（7 个）', n.chunks === 7, String(n.chunks));

  console.log('\n--- 加粗词悬浮释义 ---');
  await p.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 250));
  const ng = await p.evaluate(() => ({
    gloss: document.querySelectorAll('.en strong.gloss').length,
    all: document.querySelectorAll('.en strong').length,
  }));
  ok('全部加粗词可悬浮', ng.gloss === ng.all && ng.all > 40, ng.gloss + '/' + ng.all);

  /* 取元素中心点，先滚进视口再测——否则拿到的是滚动前的旧坐标，
     悬停会落在空白处（曾因此误判「气泡不出现」）。 */
  async function centerOf(sel) {
    return p.evaluate(s => {
      const el = document.querySelector(s);
      if (!el) return null;
      el.scrollIntoView({ block: 'center' });
      const r = el.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }, sel);
  }

  const gb = await centerOf('.en strong.gloss');
  await p.mouse.move(gb.x, gb.y);
  await new Promise(r => setTimeout(r, 350));
  const tip = await p.evaluate(() => {
    const t = document.querySelector('.gloss-tip');
    if (!t || t.hidden) return null;
    const r = t.getBoundingClientRect();
    return { text: t.textContent, top: r.top, left: r.left, w: r.width,
             vw: window.innerWidth, vh: window.innerHeight };
  });
  ok('气泡出现且有释义', tip && tip.text.length > 3, tip ? tip.text : '');
  ok('气泡不出屏', tip && tip.left >= 0 && tip.left + tip.w <= tip.vw + 1 && tip.top >= 0,
     tip ? JSON.stringify([tip.left, tip.w, tip.vw]) : '');
  await p.mouse.move(5, 5);
  await new Promise(r => setTimeout(r, 250));
  ok('移开后消失', await p.evaluate(() => {
    const t = document.querySelector('.gloss-tip'); return !t || t.hidden;
  }));

  // 点加粗词 = 点该句，应当展开
  await p.mouse.click(gb.x, gb.y);
  await new Promise(r => setTimeout(r, 400));
  ok('点加粗词能展开所属句',
     await p.evaluate(() => document.querySelectorAll('.inline-panel').length === 1));

  console.log('\n--- 加粗词不应有下划线 ---');
  // 曾出过的 bug：加粗词用 `border-bottom:1px dotted currentColor`，
  // 而 color 改成 inherit（近黑）后，虚线跟着变黑 ——
  // 用户看到的现象是「第一句下划线是黑的」。
  // 现在加粗词不加任何线，全篇只保留「精讲句橙色实线」一种下划线。
  const ul = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.en strong.gloss').forEach(st => {
      const c = getComputedStyle(st);
      out.push({ bw: c.borderBottomWidth, bs: c.borderBottomStyle, td: c.textDecorationLine });
    });
    const s = getComputedStyle(document.querySelector('.sent.insight'));
    return {
      n: out.length,
      anyBorder: out.some(o => parseFloat(o.bw) > 0 && o.bs !== 'none'),
      anyDeco: out.some(o => o.td !== 'none'),
      sentLine: s.textDecorationLine,
      sentColor: s.textDecorationColor,
    };
  });
  ok('加粗词无下边框', !ul.anyBorder, '有 ' + ul.n + ' 个加粗词');
  ok('加粗词无 text-decoration', !ul.anyDeco);
  ok('精讲句仍是实线下划线', ul.sentLine === 'underline', ul.sentLine);
  // 不硬编码色值（主题可能换色）：只要求「是暖色」且「明显不是黑/灰」。
  // 曾出过的 bug 正是下划线绘成近黑，所以这里断言色相而非具体 RGB。
  const rgb = (ul.sentColor.match(/\d+/g) || []).map(Number);
  const isWarm = rgb.length >= 3 && rgb[0] > rgb[2] + 60 && rgb[0] > 120;
  const isNearBlack = rgb.length >= 3 && rgb[0] < 110 && rgb[1] < 110 && rgb[2] < 110;
  ok('下划线是暖色（非黑非灰）', isWarm, ul.sentColor);
  ok('下划线不是近黑', !isNearBlack, ul.sentColor);

  console.log('\n--- 加粗词悬浮只加深底纹、不换色 ---');
  await p.mouse.move(5, 5);                       // 先移开，确保测的是「未悬浮」态
  await new Promise(r => setTimeout(r, 250));
  const beforeHover = await p.evaluate(() =>
    getComputedStyle(document.querySelector('.en strong.gloss')).backgroundColor);
  const g2 = await centerOf('.en strong.gloss');
  await p.mouse.move(g2.x, g2.y);
  await new Promise(r => setTimeout(r, 350));
  const afterHover = await p.evaluate(() => {
    const c = getComputedStyle(document.querySelector('.en strong.gloss'));
    return { bg: c.backgroundColor, color: c.color };
  });
  ok('悬浮后底纹加深', afterHover.bg !== beforeHover, beforeHover + ' -> ' + afterHover.bg);
  const hc = (afterHover.color.match(/\d+/g) || []).map(Number);
  ok('悬浮后字色仍是正文色（不跳成橙色）',
     hc.length >= 3 && hc[0] < 110 && Math.abs(hc[0] - hc[1]) < 20, afterHover.color);
  await p.mouse.move(5, 5);
  await new Promise(r => setTimeout(r, 200));

  console.log('\n--- 译文常显（像一篇文章）---');
  await p.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 250));
  ok('译文默认可见', await p.evaluate(() =>
    !document.querySelectorAll('.para')[0].querySelector('.zh').hidden));
  ok('段落内无译文开关按钮', await p.evaluate(() =>
    document.querySelectorAll('.toggle-zh').length === 0));
  ok('全部段落译文可见', await p.evaluate(() =>
    Array.from(document.querySelectorAll('.zh')).every(e => !e.hidden)));

  // 译文必须是「正文」而非「灰色脚注」——与英文同色系、字号够大
  const zs = await p.evaluate(() => {
    const z = document.querySelector('.zh'), e = document.querySelector('.en');
    const cz = getComputedStyle(z), ce = getComputedStyle(e);
    return { zc: cz.color, ec: ce.color, zs: parseFloat(cz.fontSize) };
  });
  ok('译文与正文同色（非灰色）', zs.zc === zs.ec, zs.zc + ' vs ' + zs.ec);
  ok('译文字号够大（>=15px）', zs.zs >= 15, String(zs.zs));

  // 段落不该是「题卡」：无卡片描边
  const card = await p.evaluate(() => {
    const p0 = document.querySelector('.para');
    const cs = getComputedStyle(p0);
    return { border: cs.borderTopWidth, shadow: cs.boxShadow };
  });
  ok('段落无卡片描边', card.border === '0px', card.border);
  ok('段落无投影', card.shadow === 'none', card.shadow);

  console.log('\n--- 只看英文 ---');
  await p.evaluate(() => document.querySelector('#btn-all-zh').click());
  await new Promise(r => setTimeout(r, 300));
  ok('点后隐藏全部译文', await p.evaluate(() =>
    Array.from(document.querySelectorAll('.zh')).every(e => e.hidden)));
  ok('按钮改为显示译文', (await p.evaluate(() =>
    document.querySelector('#btn-all-zh').textContent)) === '显示译文');
  await p.evaluate(() => document.querySelector('#btn-all-zh').click());
  await new Promise(r => setTimeout(r, 300));
  ok('再点恢复全部译文', await p.evaluate(() =>
    Array.from(document.querySelectorAll('.zh')).every(e => !e.hidden)));

  console.log('\n--- 词汇表：始终完整渲染 + 内部滚动 ---');
  const v = await p.evaluate(() => {
    const w = document.querySelector('.vocab-wrap');
    const row = document.querySelector('#vocab tbody tr');
    const rh = row.getBoundingClientRect().height;
    return {
      rows: document.querySelectorAll('#vocab tbody tr').length,
      first: document.querySelector('#vocab tbody tr .v-word').textContent,
      count: document.querySelector('#vocab-count').textContent,
      innerScroll: w.scrollHeight > w.clientHeight + 2,
      sticky: getComputedStyle(document.querySelector('#vocab thead th')).position,
      rowH: Math.round(rh),
      visible: Math.floor(w.clientHeight / rh),
      hasToggle: !!document.querySelector('#vocab-toggle'),
      hasMore: !!document.querySelector('#vocab-more'),
    };
  });
  ok('32 行全部渲染', v.rows === 32, String(v.rows));
  ok('默认按句频降序', v.first === 'accord', v.first);
  ok('表格内部滚动', v.innerScroll);
  ok('表头吸顶', v.sticky === 'sticky', v.sticky);
  ok('已移除「展开全部」按钮', !v.hasToggle);
  ok('已移除「还有 N 个词」提示', !v.hasMore);
  ok('计数说明可滚动', v.count.indexOf('滚动') >= 0, v.count);
  // 关键：一屏必须能看到足够多行，否则不如给按钮。
  // 手机上曾因列窄、释义换行把行高撑到 146px，一屏只看得到 2 行。
  ok('一屏可见 >= 6 行', v.visible >= 6, v.visible + ' 行（行高 ' + v.rowH + 'px）');

  console.log('\n--- 词汇表：筛选 ---');
  await p.evaluate(() => {
    const f = document.querySelector('#vocab-filter');
    f.value = 'a'; f.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await new Promise(r => setTimeout(r, 250));
  const f1 = await p.evaluate(() => ({
    rows: document.querySelectorAll('#vocab tbody tr').length,
    count: document.querySelector('#vocab-count').textContent,
  }));
  ok('筛选后行数减少但仍可滚动', f1.rows > 1 && f1.rows < 32, String(f1.rows));
  ok('计数显示匹配数', f1.count.indexOf('匹配') >= 0, f1.count);

  await p.evaluate(() => {
    const f = document.querySelector('#vocab-filter');
    f.value = 'expos'; f.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await new Promise(r => setTimeout(r, 250));
  ok('精确筛选为 1 行',
     await p.evaluate(() => document.querySelectorAll('#vocab tbody tr').length === 1));

  await p.evaluate(() => {
    const f = document.querySelector('#vocab-filter');
    f.value = ''; f.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await new Promise(r => setTimeout(r, 250));
  ok('清空筛选恢复 32 行',
     await p.evaluate(() => document.querySelectorAll('#vocab tbody tr').length === 32));


  console.log('\n--- 窄屏单列 ---');
  await p.setViewport({ width: 420, height: 820, deviceScaleFactor: 1 });
  await new Promise(r => setTimeout(r, 250));
  // 段落是 grid：宽屏「页边段号 + 正文」两栏，窄屏必须真塌成单栏。
  // 曾因媒体查询写在 .en{grid-column:2} 之前而被覆盖，
  // 结果窄屏仍生成 2 列、正文只占一半宽。
  const mob = await p.evaluate(() => {
    const para = document.querySelector('.para');
    const en = document.querySelector('.en');
    return {
      cols: getComputedStyle(para).gridTemplateColumns.split(' ').length,
      enCol: getComputedStyle(en).gridColumnStart,
      enWidth: Math.round(en.getBoundingClientRect().width),
      bodyWidth: document.body.clientWidth,
    };
  });
  ok('窄屏段落塌成单栏', mob.cols === 1, 'cols=' + mob.cols);
  ok('窄屏正文 grid-column 归 1', mob.enCol === '1', mob.enCol);
  ok('窄屏正文占满宽度（>85%）',
     mob.enWidth / mob.bodyWidth > 0.85,
     mob.enWidth + '/' + mob.bodyWidth);

  await clickSentence('P4S1');
  await new Promise(r => setTimeout(r, 450));
  const m = await p.evaluate(() => ({
    overflowX: document.documentElement.scrollWidth <= window.innerWidth + 1,
    hint: !!document.querySelector('.ip-hint'),
    // 成分块是横向流式排布（flex wrap），窄屏会自动折行
    chunksFlex: getComputedStyle(document.querySelector('.inline-panel .chunks')).flexWrap,
  }));
  ok('窄屏成分块自动折行', m.chunksFlex === 'wrap', String(m.chunksFlex));
  ok('无横向溢出', m.overflowX);

  console.log('\n--- 句子超链接（精讲句 → 原站解析页）---');
  const links = await p.evaluate(() => {
    const a = Array.from(document.querySelectorAll('.en a.sent'));
    const sp = Array.from(document.querySelectorAll('.en span.sent'));
    return {
      anchors: a.length,
      spans: sp.length,
      sampleHref: a.length ? a[0].getAttribute('href') : null,
      targetBlank: a.length ? a.every(x => x.target === '_blank') : false,
      relOk: a.length ? a.every(x => (x.rel || '').indexOf('noopener') >= 0) : false,
      // 精讲句是否全部是 <a>
      insightAllAnchors: Array.from(document.querySelectorAll('.sent.insight'))
        .every(x => x.tagName === 'A'),
      // 非精讲句必须不是 <a>（原站那边是 404，不能给死链）
      normalNoneAnchor: Array.from(document.querySelectorAll('.sent:not(.insight)'))
        .every(x => x.tagName !== 'A'),
    };
  });
  ok('12 个句子渲染为链接', links.anchors === 12, String(links.anchors));
  ok('6 个非精讲句仍是 span', links.spans === 6, String(links.spans));
  ok('href 指向 p{段}-s{句} 解析页',
     links.sampleHref && /\/p\d+-s\d+\/$/.test(links.sampleHref), String(links.sampleHref));
  ok('新标签打开', links.targetBlank);
  ok('带 noopener', links.relOk);
  ok('精讲句全部是链接', links.insightAllAnchors);
  ok('非精讲句无死链', links.normalNoneAnchor);

  console.log('\n--- 链接样式未被默认样式污染 ---');
  const st = await p.evaluate(() => {
    const a = document.querySelector('.en a.sent');
    const cs = getComputedStyle(a);
    return { color: cs.color, deco: cs.textDecorationLine, tc: cs.textDecorationColor };
  });
  const bodyColor = await p.evaluate(() => getComputedStyle(document.body).color);
  ok('链接颜色继承正文（非蓝色）', st.color === bodyColor, st.color + ' vs ' + bodyColor);

  console.log('\n--- 普通左键仍是就地展开（不跳转）---');
  await p.evaluate(() => { window.__nav = 0; });
  // 拦截真实导航：一旦发生说明拦截失败
  await p.evaluateOnNewDocument(() => {});
  const pt2 = await p.evaluate(() => {
    const el = document.querySelector('[data-sent-id="P2S1"]');
    el.scrollIntoView({ block: 'center' });
    const rg = document.createRange(); rg.selectNodeContents(el);
    const r = rg.getBoundingClientRect();
    return { x: r.left + 20, y: r.top + 8, href: el.getAttribute('href') };
  });
  await p.mouse.click(pt2.x, pt2.y);
  await new Promise(r => setTimeout(r, 600));
  ok('仍在原页面（未跳走）', p.url().indexOf('127.0.0.1') >= 0, p.url());
  ok('就地面板已展开', await p.evaluate(() =>
    document.querySelectorAll('.inline-panel').length === 1));
  ok('面板是该句 P2S1', (await p.evaluate(() =>
    document.querySelector('.ip-id').textContent)) === 'P2S1');

  console.log('\n--- 面板内「完整解析」链接 ---');
  const ext = await p.evaluate(() => {
    const a = document.querySelector('.inline-panel .ip-ext');
    if (!a) return null;
    return { href: a.getAttribute('href'), text: a.textContent,
             target: a.target, rel: a.rel,
             note: (document.querySelector('.inline-panel .ip-ext-note') || {}).textContent };
  });
  ok('面板含原站链接', ext && /\/p2-s1\/$/.test(ext.href), ext ? ext.href : 'none');
  ok('链接文案清晰', ext && ext.text.indexOf('原站') >= 0, ext ? ext.text : '');
  ok('同样新标签 + noopener', ext && ext.target === '_blank' && ext.rel.indexOf('noopener') >= 0);
  ok('附说明文字', ext && ext.note && ext.note.length > 8, ext ? ext.note : '');

  console.log('\n--- 非精讲句：不给死链，给说明 ---');
  await clickSentence('P5S1');
  await new Promise(r => setTimeout(r, 500));
  const noLink = await p.evaluate(() => ({
    ext: document.querySelectorAll('.inline-panel .ip-ext').length,
    note: (document.querySelector('.inline-panel .ip-ext-note') || {}).textContent || '',
    id: document.querySelector('.ip-id').textContent,
  }));
  ok('当前为 P5S1', noLink.id === 'P5S1', noLink.id);
  ok('无外链', noLink.ext === 0, String(noLink.ext));
  ok('给出「无解析页」说明', noLink.note.indexOf('没有') >= 0, noLink.note);

  console.log('\n--- 篇目来源链接 ---');
  const src = await p.evaluate(() => {
    const a = document.querySelector('#p-stats .src-link');
    return a ? { href: a.getAttribute('href'), text: a.textContent } : null;
  });
  ok('页头含来源链接', src && /section2-part-a-1/.test(src.href), src ? src.href : 'none');

  console.log('\n--- 控制台 ---');
  ok('无运行时错误', errs.length === 0, errs.join(' ; '));

  console.log('\n=============  PASS ' + pass + '  FAIL ' + fail + '  =============');
  await b.close();
  process.exit(fail ? 1 : 0);
})();
