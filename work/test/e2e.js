/* 端到端渲染测试：用 jsdom 真正加载 index.html + app.js + 数据，
   验证点击句子、加粗、划线、抽屉、词汇表排序/筛选是否都工作。 */
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const SITE = path.resolve(__dirname, '..', '..', 'site');
const html = fs.readFileSync(path.join(SITE, 'index.html'), 'utf8');

const errors = [];
const dom = new JSDOM(html, {
  runScripts: 'dangerously',
  resources: 'usable',
  url: 'file:///' + SITE.replace(/\\/g, '/') + '/index.html',
  pretendToBeVisual: true,
});
const { window } = dom;
window.addEventListener('error', e => errors.push('window.error: ' + e.message));

// file:// 下 jsdom 不会自动取 <script src>，手动按顺序注入
function runScript(rel) {
  const p = path.join(SITE, rel);
  const code = fs.readFileSync(p, 'utf8');
  const fn = new window.Function(code);
  try { fn.call(window); } catch (e) { errors.push('script ' + rel + ': ' + e.message); }
}

let pass = 0, fail = 0;
function ok(name, cond, extra) {
  if (cond) { pass++; console.log('  PASS  ' + name); }
  else { fail++; console.log('  FAIL  ' + name + (extra ? '  -> ' + extra : '')); }
}

setTimeout(() => {
  runScript('data/library.js');
  runScript('data/2016-text1.js');
  runScript('app.js');

  const d = window.document;
  console.log('\n--- 加载 ---');
  ok('main 区显示', d.querySelector('#main').hidden === false);
  ok('loading 已隐藏', d.querySelector('#loading').hidden === true);
  ok('标题已填', d.querySelector('#p-title').textContent.includes('2016'));

  console.log('\n--- 正文渲染 ---');
  const paras = d.querySelectorAll('.para');
  ok('6 个段落块', paras.length === 6, 'got ' + paras.length);
  const sents = d.querySelectorAll('.sent');
  ok('18 个可点击句子', sents.length === 18, 'got ' + sents.length);
  const ins = d.querySelectorAll('.sent.insight');
  ok('12 句带下划线(精讲)', ins.length === 12, 'got ' + ins.length);
  const strongs = d.querySelectorAll('.en strong');
  ok('加粗已渲染', strongs.length > 20, 'got ' + strongs.length);

  console.log('\n--- 加粗正确性 ---');
  // P2S1: bold = ['early exposure','beneficial']
  const s21 = d.querySelector('[data-sent-id="P2S1"]');
  const s21strong = Array.from(s21.querySelectorAll('strong')).map(e => e.textContent);
  ok('P2S1 加粗=early exposure/beneficial',
     JSON.stringify(s21strong) === JSON.stringify(['early exposure', 'beneficial']),
     JSON.stringify(s21strong));
  ok('加粗项带悬浮释义', Array.from(s21.querySelectorAll('strong')).every(
     e => e.dataset.gloss && e.dataset.gloss.length > 0));
  ok('P2S1 纯文本还原无损',
     s21.textContent === 'However, Cortina said, early exposure is beneficial.',
     JSON.stringify(s21.textContent));

  console.log('\n--- 点击开抽屉 ---');
  const ev = new window.MouseEvent('click', { bubbles: true });
  s21.dispatchEvent(ev);

  ok('面板展开', d.querySelector('.inline-panel') !== null);
  
  ok('句子高亮', s21.classList.contains('active'));

  const dr = d.querySelector('.inline-panel');
  const chunks = dr.querySelectorAll('.chunk');
  ok('面板含 5 个成分', chunks.length === 5, 'got ' + chunks.length);
  const rolesTxt = Array.from(dr.querySelectorAll('.ck-role')).map(e => e.textContent);
  ok('成分角色正确',
     JSON.stringify(rolesTxt) === JSON.stringify(['连接词', '插入语', '主语', '谓语', '表语']),
     JSON.stringify(rolesTxt));
  const ckTxts = Array.from(dr.querySelectorAll('.ck-txt')).map(e => e.textContent);
  ok('成分文本正确', ckTxts.join('|') === 'However|Cortina said|early exposure|is|beneficial', ckTxts.join('|'));

  ok('角色有配色', dr.querySelectorAll('.ck-role')[0].style.background !== '');
  ok('精讲考点框出现', dr.querySelectorAll('.note-box').length === 1);

  console.log('\n--- 关闭行为 ---');
  s21.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  ok('再次点击同一句 → 收起', d.querySelector('.inline-panel') === null);

  const s11 = d.querySelector('[data-sent-id="P1S1"]');
  s11.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  ok('换一句 → 打开', d.querySelector('.inline-panel') !== null);
  const n1 = d.querySelectorAll('.inline-panel .note-box').length;
  ok('P1S1 精讲框出现', n1 === 1, 'got ' + n1);

  d.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  ok('ESC 收起', d.querySelector('.inline-panel') === null);

  // 非精讲句
  const s12 = d.querySelector('[data-sent-id="P1S2"]');
  s12.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const hasNote = d.querySelectorAll('.inline-panel .note-box').length;
  ok('非精讲句无考点框', hasNote === 0, 'got ' + hasNote);
  ok('非精讲句仍有成分', d.querySelectorAll('.inline-panel .chunk').length === 7,
     'got ' + d.querySelectorAll('.inline-panel .chunk').length);
  d.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));

  console.log('\n--- 译文常显（读起来像文章）---');
  const p1 = paras[0];
  const zh = p1.querySelector('.zh');
  // 译文默认就显示，不再需要先点按钮——这是「像文章而不像题面」的关键
  ok('译文默认可见', zh.hidden === false);
  ok('中文内容存在', zh.textContent.includes('诚然'));
  ok('段落内无译文开关按钮', p1.querySelectorAll('.toggle-zh').length === 0);
  ok('全部段落译文都可见',
     Array.from(d.querySelectorAll('.zh')).every(e => e.hidden === false));

  console.log('\n--- 只看英文 ---');
  const all = d.querySelector('#btn-all-zh');
  all.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  ok('点后隐藏全部译文', Array.from(d.querySelectorAll('.zh')).every(e => e.hidden === true));
  ok('按钮改为显示译文', all.textContent === '显示译文', all.textContent);
  all.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  ok('再点恢复全部译文', Array.from(d.querySelectorAll('.zh')).every(e => e.hidden === false));
  ok('按钮回到只看英文', all.textContent === '只看英文', all.textContent);

  console.log('\n--- 词汇表 ---');
  const rows = d.querySelectorAll('#vocab tbody tr');
  // 词表始终完整渲染，靠固定高度 + 内部滚动控制篇幅（不再有折叠/展开按钮）
  ok('32 行全部渲染', rows.length === 32, 'got ' + rows.length);
  ok('默认按真题句频降序，首行=accord(172)',
     rows[0].querySelector('.v-word').textContent === 'accord',
     rows[0].querySelector('.v-word').textContent);
  const badge = rows[0].querySelector('.badge');
  ok('CEFR 徽章', badge && badge.textContent === 'C1', badge ? badge.textContent : 'none');
  ok('等级 class 用于配色', badge.classList.contains('lv-C1'));

  // 按字母排序 —— accord 恰好既是字母序第一、又是句频第一，断言会假通过。
  // 改为断言整列有序 + 切换升降序。
  const thWord = d.querySelector('#vocab th[data-sort="word"]');
  thWord.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const wordsAsc = Array.from(d.querySelectorAll('#vocab tbody tr .v-word')).map(e => e.textContent);
  const sortedAsc = wordsAsc.slice().sort((a, b) => a.localeCompare(b));
  ok('按字母升序整列有序', JSON.stringify(wordsAsc) === JSON.stringify(sortedAsc));
  ok('升序首行=academic', wordsAsc[0] === 'academic', wordsAsc[0]);

  thWord.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const wordsDesc = Array.from(d.querySelectorAll('#vocab tbody tr .v-word')).map(e => e.textContent);
  const sortedDesc = wordsDesc.slice().sort((a, b) => b.localeCompare(a));
  // 默认只显示 12/32：升序给出最小的 12 个、降序给出最大的 12 个，
  // 两者是不同集合，不能断言互为反转。只需各自列内有序。
  ok('降序整列有序', JSON.stringify(wordsDesc) === JSON.stringify(sortedDesc));
  ok('降序首词 > 升序首词', wordsDesc[0] > wordsAsc[0], wordsDesc[0] + ' vs ' + wordsAsc[0]);

  // 数值排序：句频
  const thFreq = d.querySelector('#vocab th[data-sort="freq"]');
  thFreq.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const freqs = Array.from(d.querySelectorAll('#vocab tbody tr td.num:last-child'))
                     .map(e => Number(e.textContent));
  const descFreq = freqs.slice().sort((a, b) => b - a);
  ok('句频降序整列有序', JSON.stringify(freqs) === JSON.stringify(descFreq));
  ok('句频最大值=172 在首行', freqs[0] === 172, String(freqs[0]));

  // 筛选
  const f = d.querySelector('#vocab-filter');
  f.value = 'expos';
  f.dispatchEvent(new window.Event('input', { bubbles: true }));
  const fr = d.querySelectorAll('#vocab tbody tr');
  ok('筛选 "expos" → 1 行', fr.length === 1, 'got ' + fr.length);
  ok('筛选结果正确', fr[0].querySelector('.v-word').textContent === 'exposure');
  f.value = '';
  f.dispatchEvent(new window.Event('input', { bubbles: true }));
  ok('清空筛选恢复 32 行', d.querySelectorAll('#vocab tbody tr').length === 32);

  console.log('\n--- 未捕获错误 ---');
  ok('无 JS 运行时错误', errors.length === 0, errors.join(' ; '));

  console.log('\n=================  PASS ' + pass + '  FAIL ' + fail + '  =================');
  process.exit(fail ? 1 : 0);
}, 300);
