/* 第二篇（2023 Text 4）的冒烟测试：确认「加一篇」的完整链路可用。
   重点验证通用性——不能只对 2016 T1 有效：
     · 切换篇目后数据全部换新
     · 就地展开、成分、链接、悬浮释义照常
     · 非精讲句不给死链
*/
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
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.setViewport({ width: 1100, height: 900, deviceScaleFactor: 1 });
  await p.goto(URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 700));

  // 切到 2023 Text 4
  await p.select('#paper', '2023-4');
  await new Promise(r => setTimeout(r, 1200));

  console.log('--- 切换后的数据 ---');
  const st = await p.evaluate(() => ({
    title: document.querySelector('#p-title').textContent,
    paras: document.querySelectorAll('.para').length,
    sents: document.querySelectorAll('.sent').length,
    insight: document.querySelectorAll('.sent.insight').length,
    anchors: document.querySelectorAll('.en a.sent').length,
    gloss: document.querySelectorAll('.en strong.gloss').length,
    vocabRows: document.querySelectorAll('#vocab tbody tr').length,
    src: (document.querySelector('#p-stats .src-link') || {}).getAttribute
         ? document.querySelector('#p-stats .src-link').getAttribute('href') : '',
  }));
  ok('标题为 2023 Text 4', st.title.indexOf('2023') >= 0 && st.title.indexOf('4') >= 0, st.title);
  ok('7 段', st.paras === 7, String(st.paras));
  ok('24 句', st.sents === 24, String(st.sents));
  ok('9 句精讲带下划线', st.insight === 9, String(st.insight));
  ok('9 句渲染为链接', st.anchors === 9, String(st.anchors));
  ok('加粗词带释义', st.gloss > 20, String(st.gloss));
  ok('词表 48 行', st.vocabRows === 48, String(st.vocabRows));
  ok('来源链接指向 2023 text4',
     st.src.indexOf('2023-english-two') >= 0 && st.src.indexOf('part-a-4') >= 0,
     st.src);

  console.log('\n--- 就地点开一个精讲句 ---');
  // P1S4 很长、跨两行，Range 的矩形 top 可能落在上一句上。
  // 用 elementFromPoint 校验命中后再点，避免点错句子（曾误点 P1S3）
  const pt = await p.evaluate(() => {
    const el = document.querySelector('[data-sent-id="P1S4"]');
    el.scrollIntoView({ block: 'start' });
    window.scrollBy(0, -70);
    const rg = document.createRange();
    rg.selectNodeContents(el);
    const rects = Array.from(rg.getClientRects());
    for (const r of rects) {
      const x = r.left + 20, y = r.top + 8;
      const hit = document.elementFromPoint(x, y);
      if (hit && hit.closest && hit.closest('[data-sent-id="P1S4"]')) {
        return { x, y };
      }
    }
    return null;
  });
  ok('能定位到 P1S4 的可点位置', pt !== null);
  await p.mouse.click(pt.x, pt.y);
  await new Promise(r => setTimeout(r, 600));

  const panel = await p.evaluate(() => {
    const pn = document.querySelector('.inline-panel');
    if (!pn) return null;
    const sr = document.querySelector('.sent.active').getBoundingClientRect();
    const pr = pn.getBoundingClientRect();
    return {
      id: pn.querySelector('.ip-id').textContent,
      chunks: pn.querySelectorAll('.chunk').length,
      skel: pn.querySelectorAll('.skel').length,
      note: pn.querySelectorAll('.note-box').length,
      ext: (pn.querySelector('.ip-ext') || {}).getAttribute
           ? pn.querySelector('.ip-ext').getAttribute('href') : null,
      afterSent: pr.top >= sr.bottom - 2,
      overlap: Array.from(document.querySelectorAll('.sent')).filter(s => {
        const r = s.getBoundingClientRect();
        return !(r.bottom <= pr.top || r.top >= pr.bottom ||
                 r.right <= pr.left || r.left >= pr.right);
      }).length,
    };
  });
  ok('面板已展开', panel !== null);
  ok('面板 id = P1S4', panel && panel.id === 'P1S4', panel ? panel.id : 'null');
  ok('4 个成分', panel && panel.chunks === 4, panel ? String(panel.chunks) : '');
  ok('整句对照存在', panel && panel.skel === 1);
  ok('考点讲解存在', panel && panel.note === 1);
  ok('面板在句子下方', panel && panel.afterSent);
  ok('不遮挡任何句子', panel && panel.overlap === 0, panel ? String(panel.overlap) : '');
  ok('外链指向 p1-s4',
     panel && panel.ext && /\/p1-s4\/$/.test(panel.ext), panel ? String(panel.ext) : '');

  console.log('\n--- 非精讲句不给死链 ---');
  await p.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 250));
  const pt2 = await p.evaluate(() => {
    const el = document.querySelector('[data-sent-id="P1S1"]');
    el.scrollIntoView({ block: 'center' });
    const rg = document.createRange();
    rg.selectNodeContents(el);
    const r = rg.getBoundingClientRect();
    return { x: r.left + 12, y: r.top + 8 };
  });
  await p.mouse.click(pt2.x, pt2.y);
  await new Promise(r => setTimeout(r, 500));
  const n2 = await p.evaluate(() => ({
    ext: document.querySelectorAll('.inline-panel .ip-ext').length,
    note: (document.querySelector('.inline-panel .ip-ext-note') || {}).textContent || '',
    chunks: document.querySelectorAll('.inline-panel .chunk').length,
  }));
  ok('非精讲句无外链', n2.ext === 0, String(n2.ext));
  ok('给出说明', n2.note.indexOf('没有') >= 0, n2.note);
  ok('成分仍在（3 个）', n2.chunks === 3, String(n2.chunks));

  console.log('\n--- 悬浮释义 ---');
  await p.keyboard.press('Escape');
  await new Promise(r => setTimeout(r, 250));
  const g = await p.evaluate(() => {
    const el = document.querySelector('.en strong.gloss');
    el.scrollIntoView({ block: 'center' });
    const r = el.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2, txt: el.textContent };
  });
  await p.mouse.move(g.x, g.y);
  await new Promise(r => setTimeout(r, 350));
  const tipTxt = await p.evaluate(() => {
    const t = document.querySelector('.gloss-tip');
    return t && !t.hidden ? t.textContent : '';
  });
  ok('悬浮显示释义', tipTxt.length > 3, g.txt + ' -> ' + tipTxt);

  console.log('\n--- 切回 2016 T1 ---');
  await p.select('#paper', '2016-1');
  await new Promise(r => setTimeout(r, 1000));
  const back = await p.evaluate(() => ({
    paras: document.querySelectorAll('.para').length,
    sents: document.querySelectorAll('.sent').length,
    vocab: document.querySelectorAll('#vocab tbody tr').length,
    panels: document.querySelectorAll('.inline-panel').length,
  }));
  ok('切回后 6 段', back.paras === 6, String(back.paras));
  ok('切回后 18 句', back.sents === 18, String(back.sents));
  ok('切回后 32 词', back.vocab === 32, String(back.vocab));
  ok('切换后旧面板已清除', back.panels === 0, String(back.panels));

  console.log('\n--- 控制台 ---');
  ok('无运行时错误', errs.length === 0, errs.join(' ; '));

  console.log('\n=============  PASS ' + pass + '  FAIL ' + fail + '  =============');
  await b.close();
  process.exit(fail ? 1 : 0);
})();
