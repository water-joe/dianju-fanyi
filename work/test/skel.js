/* 验证「整句对照」把成分染色的同时，文本内容与原文完全一致（无损）。
   这是该区块可读的前提：未覆盖的词必须原样保留。 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const SITE = path.resolve(__dirname, '..', '..', 'site');
const html = fs.readFileSync(path.join(SITE, 'index.html'), 'utf8');
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  pretendToBeVisual: true,          // 提供 requestAnimationFrame
  url: 'file:///' + SITE.replace(/\\/g, '/') + '/x.html',
});
const RUNTIME_ERRORS = [];
dom.window.addEventListener('error', e => RUNTIME_ERRORS.push(e.message));
const w = dom.window;
['data/library.js', 'data/2016-text1.js', 'app.js'].forEach(f => {
  new w.Function(fs.readFileSync(path.join(SITE, f), 'utf8')).call(w);
});

const norm = x => x.replace(/\s+/g, ' ').trim();

setTimeout(() => {
  const d = w.document;
  const click = id => d.querySelector('[data-sent-id="' + id + '"]')
                        .dispatchEvent(new w.MouseEvent('click', { bubbles: true }));
  let checked = 0, bad = 0, partial = 0;

  w.PASSAGE.paragraphs.forEach(p => p.sentences.forEach(s => {
    click(s.id);
    const sk = d.querySelector('.inline-panel .skel');
    if (!sk) { bad++; console.log('  FAIL ' + s.id + ': no .skel'); return; }
    const got = norm(sk.textContent), exp = norm(s.en);
    const same = got === exp;
    const tags = sk.querySelectorAll('.sk').length;
    const tagOk = tags === s.chunks.length;
    checked++;
    if (!same || !tagOk) {
      bad++;
      console.log('  FAIL ' + s.id + ' text=' + same + ' tags=' + tags + '/' + s.chunks.length);
      if (!same) { console.log('    got: ' + got.slice(0, 120)); console.log('    exp: ' + exp.slice(0, 120)); }
    }
    // 未覆盖词的比例（用于了解有多少词没被划进任何成分）
    const coveredChars = Array.from(sk.querySelectorAll('.sk')).reduce((n, e) => n + e.textContent.length, 0);
    if (coveredChars < s.en.length) partial++;
  }));

  console.log('\n整句对照无损重建: ' + checked + ' 句, ' + bad + ' 失败');
  console.log('含未覆盖词（保留原样）的句子: ' + partial + '/' + checked);
  process.exit((bad || RUNTIME_ERRORS.length) ? 1 : 0);
}, 400);
