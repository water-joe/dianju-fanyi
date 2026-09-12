/* 2022 年 Text 1-4 的冒烟测试：确认新增四篇的完整链路可用。
   对每篇验证：切换后数据换新、精讲句带下划线并渲染为链接、加粗词带释义、
   词表行数正确、来源链接正确；并就地展开一个精讲句 + 一个非精讲句，
   确认面板就地下方展开、成分/考点/整句对照齐全、非精讲句不给死链。 */
const puppeteer = require('puppeteer');
const URL = 'http://127.0.0.1:8765/';

let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (extra !== undefined ? '  -> ' + extra : '')); }
}

// 期望：[id, 段数, 句数, 精讲句数, 词表行数, 精讲句 id(用于点开), 非精讲句 id]
const EXPECT = [
  ['2022-1', 6, 19, 6, 56, 'P1S2', 'P1S3'],
  ['2022-2', 8, 24, 9, 61, 'P7S2', 'P2S1'],
  ['2022-3', 6, 17, 7, 72, 'P6S2', 'P1S3'],
  ['2022-4', 5, 18, 9, 69, 'P5S5', 'P2S4'],
];

(async () => {
  const b = await puppeteer.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.setViewport({ width: 1100, height: 900, deviceScaleFactor: 1 });
  await p.goto(URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 700));

  for (const [id, paras, sents, insight, vocabRows, insId, nonInsId] of EXPECT) {
    console.log('\n=== 切换 ' + id + ' ===');
    await p.select('#paper', id);
    await new Promise(r => setTimeout(r, 1200));

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
    ok(id + ' 段数', st.paras === paras, String(st.paras));
    ok(id + ' 句数', st.sents === sents, String(st.sents));
    ok(id + ' 精讲句带下划线', st.insight === insight, String(st.insight));
    ok(id + ' 精讲句渲染为链接', st.anchors === insight, String(st.anchors));
    ok(id + ' 加粗词带释义', st.gloss > 10, String(st.gloss));
    ok(id + ' 词表行数', st.vocabRows === vocabRows, String(st.vocabRows));
    ok(id + ' 来源链接指向 ' + id,
       st.src.indexOf('2022-english-two') >= 0, st.src);

    // 就地点开一个精讲句
    const pt = await p.evaluate((sid) => {
      const el = document.querySelector('[data-sent-id="' + sid + '"]');
      el.scrollIntoView({ block: 'start' });
      window.scrollBy(0, -70);
      const rg = document.createRange();
      rg.selectNodeContents(el);
      for (const r of Array.from(rg.getClientRects())) {
        const x = r.left + 20, y = r.top + 8;
        const hit = document.elementFromPoint(x, y);
        if (hit && hit.closest && hit.closest('[data-sent-id="' + sid + '"]')) return { x, y };
      }
      return null;
    }, insId);
    ok(id + ' 能定位精讲句 ' + insId, pt !== null);
    if (pt) {
      await p.mouse.click(pt.x, pt.y);
      await new Promise(r => setTimeout(r, 550));
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
        };
      });
      ok(id + ' 面板已展开', panel !== null);
      ok(id + ' 面板 id = ' + insId, panel && panel.id === insId, panel ? panel.id : 'null');
      ok(id + ' 成分齐全', panel && panel.chunks >= 2, panel ? String(panel.chunks) : '');
      ok(id + ' 整句对照存在', panel && panel.skel === 1);
      ok(id + ' 考点讲解存在', panel && panel.note === 1, id + ' insight 应有考点');
      ok(id + ' 面板在句子下方(就地)', panel && panel.afterSent);
      ok(id + ' 外链指向 ' + insId.replace('P', '').toLowerCase(),
         panel && panel.ext && new RegExp('/' + insId.toLowerCase().replace('p', 'p').replace('s', '-s') + '/$').test(panel.ext),
         panel ? String(panel.ext) : '');
    }

    // 非精讲句不给死链
    await p.keyboard.press('Escape');
    await new Promise(r => setTimeout(r, 250));
    const pt2 = await p.evaluate((sid) => {
      const el = document.querySelector('[data-sent-id="' + sid + '"]');
      el.scrollIntoView({ block: 'center' });
      const rg = document.createRange();
      rg.selectNodeContents(el);
      const r = rg.getBoundingClientRect();
      return { x: r.left + 12, y: r.top + 8 };
    }, nonInsId);
    if (!pt2) { ok(id + ' 非精讲句定位失败', false, nonInsId); await p.keyboard.press('Escape'); await new Promise(r => setTimeout(r, 200)); continue; }
    await p.mouse.click(pt2.x, pt2.y);
    await new Promise(r => setTimeout(r, 450));
    const n2 = await p.evaluate(() => ({
      ext: document.querySelectorAll('.inline-panel .ip-ext').length,
      note: (document.querySelector('.inline-panel .ip-ext-note') || {}).textContent || '',
      chunks: document.querySelectorAll('.inline-panel .chunk').length,
    }));
    ok(id + ' 非精讲句无外链', n2.ext === 0, String(n2.ext));
    ok(id + ' 非精讲句给出说明', n2.note.indexOf('没有') >= 0, n2.note);
    ok(id + ' 非精讲句成分仍在', n2.chunks >= 1, String(n2.chunks));
    await p.keyboard.press('Escape');
    await new Promise(r => setTimeout(r, 200));
  }

  // 悬浮释义
  await p.select('#paper', '2022-1');
  await new Promise(r => setTimeout(r, 1000));
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

  console.log('\n--- 控制台 ---');
  ok('无运行时错误', errs.length === 0, errs.join(' ; '));

  console.log('\n=============  PASS ' + pass + '  FAIL ' + fail + '  =============');
  await b.close();
  process.exit(fail ? 1 : 0);
})();
