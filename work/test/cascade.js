/* 自动化环境里 Chromium 会禁用 :visited 样式（隐私保护），
   所以直接访问 URL 测不出来。改为验证「优先级机制」本身：
   注入一条与 `a.sent:visited` 等价的规则（同为 (0,2,1) 优先级），
   看它是否会把 .sent.insight (0,2,0) 的橙色下划线覆盖掉。

   如果覆盖成立，就说明 :visited 生效时下划线确实会消失 —— 即用户的 bug。 */
const puppeteer = require('puppeteer');
const URL = 'http://127.0.0.1:8765/';

(async () => {
  const b = await puppeteer.launch({ args: ['--no-sandbox'] });
  const p = await b.newPage();
  await p.setViewport({ width: 900, height: 900, deviceScaleFactor: 4 });
  await p.goto(URL, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 600));

  // 取 P1S1 下划线像素
  async function px(tag) {
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
    const s = await p.evaluate(async (durl) => {
      const img = new Image();
      await new Promise((res, rej) => { img.onload = res; img.onerror = rej; img.src = durl; });
      const cv = document.createElement('canvas');
      cv.width = img.width; cv.height = img.height;
      const cx = cv.getContext('2d');
      cx.drawImage(img, 0, 0);
      const d = cx.getImageData(0, 0, img.width, img.height).data;
      let orange = 0, dark = 0;
      for (let i = 0; i < d.length; i += 4) {
        const R = d[i], G = d[i + 1], B = d[i + 2];
        if (R > 140 && R - B > 70) orange++;
        else if (R < 100 && G < 100 && B < 100) dark++;
      }
      return { orange, dark };
    }, 'data:image/png;base64,' + b64);
    console.log('  ' + tag + ': 橙色像素=' + s.orange + '  近黑像素=' + s.dark);
    return s;
  }

  console.log('=== 1) 当前状态（:visited 未生效）===');
  const a1 = await px('P1S1 下划线');

  console.log('\n=== 2) 注入与 a.sent:visited 等价优先级的规则 ===');
  await p.evaluate(() => {
    const st = document.createElement('style');
    // [href] 的属性选择器权重与伪类同为 (0,1,0)，
    // 因此 a.sent[href] 也 = (0,2,1)，与 a.sent:visited 同权重。
    // 用它来模拟「:visited 生效时」的层叠结果。
    st.textContent = 'a.sent[href]{ text-decoration:none; }';
    document.head.appendChild(st);
  });
  await new Promise(r => setTimeout(r, 400));
  const a2 = await px('P1S1 下划线');

  console.log('\n================ 判定 ================');
  // 这条测试防的是「已访问链接把精讲句下划线覆盖掉」的回归：
  // 我们注入一条与 a.sent:visited 同优先级 (0,2,1) 的规则来模拟该状态，
  // 正确修好后，精讲句的下划线应当「不受影响」。
  console.log('未访问  : 橙色=' + a1.orange + '  近黑=' + a1.dark);
  console.log('模拟已访问: 橙色=' + a2.orange + '  近黑=' + a2.dark);
  const okFix = a1.orange > 200 && a2.orange > 200;
  const okStable = Math.abs(a2.orange - a1.orange) < 50;
  if (okFix && okStable) {
    console.log('>>> 通过：下划线在「已访问」状态下依然存在且颜色不变。');
  } else {
    console.log('>>> 回归！已访问状态会把下划线覆盖掉（橙色 ' + a1.orange + ' -> ' + a2.orange + '）');
    console.log('    检查 .sent.insight 是否仍带有 a.sent.insight:visited 等显式声明。');
  }
  await b.close();
  process.exit(okFix && okStable ? 0 : 1);
})();
