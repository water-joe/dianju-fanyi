// 验证站点在 http:// 协议下（而非 file://）能正常渲染。
// Pages 走的是 http，而 CLAUDE.md 记录的所有验证都在 file:// 下做的。
const http = require('http');
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const ROOT = path.resolve(__dirname, '../../site');
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8' };

const server = http.createServer((req, res) => {
  let rel = decodeURIComponent(req.url.split('?')[0]);
  if (rel === '/') rel = '/index.html';
  const f = path.join(ROOT, rel);
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) {
    res.writeHead(404); return res.end('404');
  }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const base = `http://127.0.0.1:${port}/`;

  const b = await puppeteer.launch();
  const p = await b.newPage();
  const errors = [];
  p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  p.on('pageerror', e => errors.push('pageerror: ' + e.message));
  p.on('requestfailed', r => errors.push('requestfailed: ' + r.url()));

  await p.goto(base, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 900));

  const info = await p.evaluate(() => ({
    libLen: (window.LIBRARY || []).length,
    title: document.querySelector('#p-title')?.textContent || '',
    paragraphs: document.querySelectorAll('.para').length,
    sentences: document.querySelectorAll('.sent').length,
    chapters: document.querySelectorAll('#paper option').length,
    mainHidden: document.querySelector('#main')?.hidden,
    ghHref: document.querySelector('#gh-link')?.href || '',
  }));

  // 切换篇目，确认 data/*.js 能在 http 下按需加载（这正是 file:// 必须内联的原因）
  const okSwitch = await p.evaluate(async () => {
    const sel = document.querySelector('#paper');
    sel.value = sel.options[sel.options.length - 1].value;
    sel.dispatchEvent(new Event('change', { bubbles: true }));
    await new Promise(r => setTimeout(r, 900));
    return {
      title: document.querySelector('#p-title').textContent,
      paragraphs: document.querySelectorAll('.para').length,
      sentences: document.querySelectorAll('.sent').length,
    };
  });

  console.log(JSON.stringify({ ...info, afterSwitch: okSwitch, errors }, null, 2));
  await p.screenshot({ path: path.resolve(__dirname, 'http_smoke.png'), fullPage: false });
  await b.close();
  server.close();
})();
