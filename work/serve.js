/* 本地预览服务器（开发用）。站点本身不需要服务器 —— 双击 index.html 即可。
   这个脚本只是为了在浏览器里以 http:// 方式预览，方便你调试和看效果。 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', 'site');
const PORT = Number(process.argv[2] || 8765);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
};

http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/' || p === '') p = '/index.html';

  // 阻止路径穿越
  const file = path.join(ROOT, path.normalize(p).replace(/^([/\\])+/, ''));
  if (!file.startsWith(ROOT)) {
    res.writeHead(403).end('Forbidden');
    return;
  }

  fs.readFile(file, (err, buf) => {
    if (err) {
      res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' });
      res.end('404 Not Found: ' + p);
      console.log('404 ' + p);
      return;
    }
    res.writeHead(200, {
      'content-type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream',
      'cache-control': 'no-store',
    });
    res.end(buf);
    console.log('200 ' + p);
  });
}).listen(PORT, '127.0.0.1', () => {
  console.log('点句翻译已启动:  http://127.0.0.1:' + PORT + '/');
  console.log('服务目录: ' + ROOT);
  console.log('按 Ctrl+C 停止');
});
