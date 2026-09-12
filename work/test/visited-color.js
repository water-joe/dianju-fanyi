/* 验证「已访问 → 下划线变淡灰」。
   headless Chromium 默认禁用 :visited 样式，故用 CDP 的 CSS.forcePseudoState 强制该状态。

   读颜色的方法：找出「整行 75% 以上同色」的行（下划线的特征）并取其主色。
   比按 RGB 区间猜「什么是灰」可靠——文字的抗锯齿边缘会污染区间统计，
   曾因此得出「未访问时也有很多灰像素」的错误结论。 */
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
  await p.setViewport({ width: 900, height: 900, deviceScaleFactor: 4 });
  await p.goto(URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 600));

  const client = await p.target().createCDPSession();
  await client.send('DOM.enable');
  await client.send('CSS.enable');
  const { root } = await client.send('DOM.getDocument', { depth: -1 });
  const { nodeId } = await client.send('DOM.querySelector', {
    nodeId: root.nodeId, selector: '[data-sent-id="P1S1"]',
  });

  async function underlineColor() {
    const clip = await p.evaluate(() => {
      const a = document.querySelector('[data-sent-id="P1S1"]');
      window.scrollTo(0, 0);
      const rg = document.createRange();
      rg.selectNodeContents(a);
      const rr = rg.getBoundingClientRect();
      return { x: Math.max(0, rr.left - 4), y: Math.max(0, rr.top - 6),
               width: Math.min(rr.width + 8, window.innerWidth - 20),
               height: rr.height + 26 };
    });
    const b64 = await p.screenshot({ clip, encoding: 'base64' });
    return p.evaluate(async (durl) => {
      const img = new Image();
      await new Promise((r2, j) => { img.onload = r2; img.onerror = j; img.src = durl; });
      const cv = document.createElement('canvas');
      cv.width = img.width; cv.height = img.height;
      const cx = cv.getContext('2d');
      cx.drawImage(img, 0, 0);
      const d = cx.getImageData(0, 0, img.width, img.height).data;
      const hits = [];
      for (let y = 0; y < img.height; y++) {
        const t = new Map();
        for (let x = 0; x < img.width; x++) {
          const i = (y * img.width + x) * 4;
          const R = d[i], G = d[i + 1], B = d[i + 2];
          if (R > 235 && G > 233 && B > 225) continue;            // 背景
          const k = R + ',' + G + ',' + B;
          t.set(k, (t.get(k) || 0) + 1);
        }
        if (!t.size) continue;
        const top = Array.from(t.entries()).sort((a, b2) => b2[1] - a[1])[0];
        const total = Array.from(t.values()).reduce((a, b2) => a + b2, 0);
        if (top[1] / total > 0.75) hits.push(top);                 // 整行同色 → 下划线
      }
      if (!hits.length) return null;
      const best = hits.sort((a, b2) => b2[1] - a[1])[0];
      const [R, G, B] = best[0].split(',').map(Number);
      return { rgb: [R, G, B], n: best[1],
               hex: '#' + [R, G, B].map(v => v.toString(16).padStart(2, '0')).join('') };
    }, 'data:image/png;base64,' + b64);
  }

  console.log('\n--- 未访问状态 ---');
  const normal = await underlineColor();
  console.log('  下划线: ' + (normal ? normal.hex + ' ×' + normal.n : 'null'));
  ok('未访问时下划线存在', normal && normal.n > 1000, normal ? String(normal.n) : 'null');
  ok('未访问时为橙色',
     normal && normal.rgb[0] > 140 && normal.rgb[0] - normal.rgb[2] > 70,
     normal ? normal.hex : 'null');

  console.log('\n--- 强制 :visited（模拟已去原站看过）---');
  await client.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['visited'] });
  await new Promise(r => setTimeout(r, 500));
  const visited = await underlineColor();
  console.log('  下划线: ' + (visited ? visited.hex + ' ×' + visited.n : 'null'));

  console.log('\n================ 判定 ================');
  ok('已访问后下划线仍然存在（不能消失）', visited && visited.n > 1000,
     visited ? String(visited.n) : 'null');
  ok('已访问后颜色确实改变',
     normal && visited && normal.hex !== visited.hex,
     (normal ? normal.hex : '?') + ' -> ' + (visited ? visited.hex : '?'));
  ok('已访问后为灰调（R≈G≈B）',
     visited && Math.abs(visited.rgb[0] - visited.rgb[1]) < 20 &&
     Math.abs(visited.rgb[1] - visited.rgb[2]) < 20,
     visited ? visited.hex : 'null');
  ok('已访问后不再是橙色',
     visited && !(visited.rgb[0] - visited.rgb[2] > 70),
     visited ? visited.hex : 'null');

  console.log('\n=============  PASS ' + pass + '  FAIL ' + fail + '  =============');
  await b.close();
  process.exit(fail ? 1 : 0);
})();
