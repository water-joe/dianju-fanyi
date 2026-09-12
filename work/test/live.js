// 用真实浏览器打开**线上** Pages 站点，验证渲染与交互。
// 本地 http 测试（httpsmoke.js）用的还是工作区文件，这个走真实 CDN。
const puppeteer = require('puppeteer');

const URL = process.argv[2] || 'https://dianju-fanyi.pages.dev/';

(async () => {
  const b = await puppeteer.launch({
    args: ['--proxy-server=http://127.0.0.1:7890'],
  });
  const p = await b.newPage();
  const errors = [];
  p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  p.on('pageerror', e => errors.push('pageerror: ' + e.message));
  p.on('requestfailed', r => errors.push('requestfailed: ' + r.url() + ' ' + (r.failure() || {}).errorText));

  await p.goto(URL, { waitUntil: 'networkidle0', timeout: 60000 });
  await new Promise(r => setTimeout(r, 1200));

  const first = await p.evaluate(() => ({
    title: document.querySelector('#p-title')?.textContent || '',
    options: document.querySelectorAll('#paper option').length,
    paragraphs: document.querySelectorAll('.para').length,
    sentences: document.querySelectorAll('.sent').length,
    bold: document.querySelectorAll('.en strong.gloss').length,
    vocabRows: document.querySelectorAll('#vocab tbody tr').length,
    ghHref: document.querySelector('#gh-link')?.href || '',
    libLen: (window.LIBRARY || []).length,
  }));

  // 点一个句子的首段文字真实矩形（多行句几何中心会落在行间空白）
  const clicked = await p.evaluate(async () => {
    const s = document.querySelector('.sent');
    if (!s) return { ok: false, why: 'no .sent' };
    const r = document.createRange();
    r.selectNodeContents(s);
    const rect = r.getClientRects()[0] || s.getBoundingClientRect();
    s.dispatchEvent(new MouseEvent('click', {
      bubbles: true, cancelable: true,
      clientX: rect.left + 3, clientY: rect.top + rect.height / 2,
    }));
    await new Promise(r => setTimeout(r, 500));
    return {
      ok: true,
      panels: document.querySelectorAll('.inline-panel').length,
      chunks: document.querySelectorAll('.inline-panel .chunk').length,
      notes: document.querySelectorAll('.inline-panel .note-box').length,
      legend: document.querySelectorAll('.inline-panel .cl-item').length,
    };
  });

  // 切到最后一篇，确认 CDN 上的 data/*.js 按需加载正常
  const switched = await p.evaluate(async () => {
    const sel = document.querySelector('#paper');
    sel.value = sel.options[sel.options.length - 1].value;
    sel.dispatchEvent(new Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 1200));
    return {
      title: document.querySelector('#p-title').textContent,
      paragraphs: document.querySelectorAll('.para').length,
      sentences: document.querySelectorAll('.sent').length,
    };
  });

  console.log(JSON.stringify({ url: URL, first, clicked, switched, errors }, null, 2));
  await p.screenshot({ path: require('path').resolve(__dirname, 'live_home.png') });
  await b.close();
})();
