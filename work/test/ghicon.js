const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const b = await puppeteer.launch();
  const p = await b.newPage();
  await p.setViewport({ width: 1100, height: 420, deviceScaleFactor: 2 });
  const url = 'file:///' + path.resolve(__dirname, '../../site/index.html').split(path.sep).join('/');
  await p.goto(url, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 800));

  const info = await p.evaluate(() => {
    const a = document.querySelector('#gh-link');
    const r = a.getBoundingClientRect();
    const svg = a.querySelector('svg');
    const sr = svg.getBoundingClientRect();
    const cs = getComputedStyle(a);
    return {
      href: a.href,
      target: a.target,
      rel: a.rel,
      rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
      svgSize: [Math.round(sr.width), Math.round(sr.height)],
      iconRenders: sr.width > 10 && sr.height > 10,
      color: cs.color,
    };
  });
  console.log(JSON.stringify(info, null, 2));

  await p.screenshot({ path: path.resolve(__dirname, 'gh_icon.png'), clip: { x: 620, y: 0, width: 470, height: 58 } });
  await b.close();
})();
