/* 验证「整句对照」是否包含完整句子。
   截图发现 2023 T4 的 P1S4 只显示了后半句——前两个成分（状语 + 主语）没渲染出来。
   这里逐句对比 .skel 的文本与句子原文，找出所有丢失成分的句。 */
const puppeteer = require('puppeteer');
const URL = 'http://127.0.0.1:8765/';

const norm = s => s.replace(/\s+/g, ' ').trim();

(async () => {
  const b = await puppeteer.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.setViewport({ width: 1100, height: 900 });
  await p.goto(URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 700));

  const norm_ = null;

  // 取全部句子 id
  const ids = await p.evaluate(() => Array.from(
    document.querySelectorAll('.sent')).map(e => e.dataset.sentId));

  let bad = 0;
  for (const id of ids) {
    const pt = await p.evaluate(sid => {
      const el = document.querySelector('[data-sent-id="' + sid + '"]');
      el.scrollIntoView({ block: 'center' });
      const rg = document.createRange();
      rg.selectNodeContents(el);
      for (const r of rg.getClientRects()) {
        const x = r.left + 15, y = r.top + 8;
        const hit = document.elementFromPoint(x, y);
        if (hit && hit.closest && hit.closest('[data-sent-id="' + sid + '"]')) {
          return { x, y };
        }
      }
      return null;
    }, id);
    if (!pt) { console.log('  ?? ' + id + ' 无法定位'); continue; }
    await p.mouse.click(pt.x, pt.y);
    await new Promise(r => setTimeout(r, 260));

    const r = await p.evaluate(sid => {
      const sk = document.querySelector('.inline-panel .skel');
      const sent = document.querySelector('[data-sent-id="' + sid + '"]');
      if (!sk) return { miss: 'no-skel' };
      return {
        got: sk.textContent,
        exp: sent.textContent,
        spans: sk.querySelectorAll('.sk').length,
        chunks: document.querySelectorAll('.inline-panel .chunk').length,
      };
    }, id);

    if (r.miss) { console.log('  !! ' + id + ' ' + r.miss); bad++; continue; }
    if (norm(r.got) !== norm(r.exp)) {
      bad++;
      console.log('  !! ' + id + ' 整句对照缺失');
      console.log('       得到: ' + norm(r.got).slice(0, 90));
      console.log('       应为: ' + norm(r.exp).slice(0, 90));
      console.log('       着色片段 ' + r.spans + ' / 成分 ' + r.chunks);
    }
    await p.keyboard.press('Escape');
    await new Promise(r2 => setTimeout(r2, 120));
  }

  console.log('\n共 ' + ids.length + ' 句，' + bad + ' 句整句对照不完整');
  await b.close();
  process.exit(bad ? 1 : 0);
})();
