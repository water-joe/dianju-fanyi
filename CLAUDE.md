# 点句翻译 — 项目说明

考研英语二阅读精读工具。给用户（中文母语，备考考研英语）阅读真题用。

## 站点形式：纯静态，`file://` 直接打开

**这是硬约束，不是偏好。** 用户要求双击 `site/index.html` 就能用，不装环境、不起服务器。

因此：

- 数据以 `window.PASSAGE = {...}` 的**普通脚本**注入，用 `<script src>` 标签加载。
- **禁止** `fetch()` / `XMLHttpRequest` / `import` / `export` / `require()` / 打包器。
  `file://` 下浏览器会以 CORS 拦截 `fetch` 读本地 JSON，页面会直接白屏。
- 新增篇目 = 加一个数据 js + 在 `site/data/library.js` 加一行，不改 `app.js`。

改动后务必验证：`grep -n "fetch(\|XMLHttpRequest\|^import " site/app.js` 应无命中（注释除外）。

## 数据来源：以本地 PDF 为准，不要去爬网站

**本项目所有内容均来自本地 PDF，不爬取网页。** `work/*.py` 与 `site/` 里
没有任何 `requests` / `urllib` / `fetch` 调用（可用 grep `requests\|urllib\|fetch(` 核验）。

代码里出现的 `https://english-exam.lazynote.cn/...` 都是**字符串而非请求**：
它们由 PDF 页脚正则提取，再按 `p{段}-s{句}` 规律拼出句子解析页地址，
最终只作为 `<a href>` 供点击。唯一一次联网是**校验那 12 个链接是否 200**
（确认不是死链），不做数据抓取；如不需要可去掉，功能不受影响。

PDF 页脚印着 `english-exam.lazynote.cn`，是那个网站打印出来的。**查阅 PDF 足够，不要爬取该站点**——用户已就此明确纠正过一次。

PDF 里**有**且项目直接采用：原文、逐段中文翻译、真题句精讲（SENTENCE INSIGHTS）及其考点文字、高频词表（含 CEFR 等级与词频）。

PDF 里**没有**：逐词的成分划分。网页版句子解析页有结构树，但**打印时丢失了**。PDF 中只有文字点评（如「第二个分句的主语含修饰语需准确切分」）。

**所以「点句划成分」这层数据是逐句生成的，不是从 PDF 提取的。** 不要为了找这层数据去爬网站——找不到，且用户不希望如此。

### 句子链接的规律（已实测）

每篇页脚有 `.../sections/{年}-english-two/section2-part-a-{N}/`，其中 N 即 Text N。
单个句子的解析页是在此基础上加 `p{段}-s{句}`（对应本项目的句子 id `P3S1` → `p3-s1`）。

**只有「真题句逐层精讲」选中的句子有独立页面**（实测 200）；
其余句子 301 → 对象存储 → **404**。所以数据里非精讲句的 `url` 留空，
前端据此不渲染链接——否则就是死链。新增篇目后请抽查几个 URL 是否 200。

**例外：2026 Text 1 的页脚不印分段号。** 它的 source 是
`sections/2026-english-two/section2-part-a/?f=p`（**没有 `-1`**），
其余 43 篇都是 `section2-part-a-{N}/`。若按 TEXT 硬拼 `-1`，13 个精讲句
URL 会**全部 404**（已实测，是踩过的坑）。生成器应改从 `RAW['source']`
推导 `SENT_BASE`（`sections→paper`、去掉 `?查询串`），而不是按 TEXT 拼。
`gen_t26_1.py` 已这样改，可作为新篇模板参考。

## 规模

11 年 × 4 篇 = **44 篇** 已**全部完成**（截至 2026-09-12）：

2016–2026 各 T1–T4，共 44 篇，全部注册进 `site/data/library.js`。

生成器 44/44 通过（`PROBLEMS (0)`），`skel/e2e/inline/cascade` 测试全过，
**44/44 在真实浏览器渲染成功、零页面错误**，抽查精讲句 URL 全部 200。

（注：2016 T1 由最早的 `work/gen.py` 生成，无独立 `gen_t16_1.py`，故生成器数为 43。）

## 成分划分的口径（用户已确认，铺开时不要改）

这两条是 2026-09-11 与用户确认过的取舍，属于**有意为之**，不是疏漏：

1. **嵌套成分合并为一块**，子结构写进 `note`。
   例：`the number of people interested in the field` 整体标为「宾语」，
   在 note 里注明「interested in the field 为过去分词短语作后置定语」。
   不要拆成并排的两块——那样看着像平级，实际是嵌套。
   （最初版本两块都保留，导致字数重复计算、覆盖率超过 100%，是真错。）

2. **引述分句各标各的主谓语**，不整体收进一个「引述分句」块。
   例：`Students ... can catch up, said Tom Cortina, the assistant dean at ...`
   出现两组「主语/谓语」：主句一组，`said` + `Tom Cortina` 一组，
   `the assistant dean...` 标「同位语」。用户认为这样更忠实原文结构，
   即使屏幕上同时出现两个「主语」标签。

## 工作流

## 加一篇的标准流程（用户说「加 20XX Text N」时照做）

```bash
# 1) 提取素材（段落/译文/句子/精讲句/词表/URL），一条命令
python work/extract.py --year 2017 --text 2

# 2) 写成分划分 + 加粗词释义（唯一需要人工的工序）
#    建 work/t{年}_{篇}_a.py / _b.py / _c.py（每文件约 8 句）
#    和 work/t{年}_{篇}_gloss.py，再写一个 gen_t{年}_{篇}.py 生成数据

# 3) 生成 + 校验（每个 bold/chunk 都会校验，有问题会报出来）
python work/gen_t23_4.py          # 参照此文件写新篇的生成器

# 4) 注册
#    在 site/data/library.js 加一行 { id, label, file }

# 5) 验证链接与跑测试
curl -sL -o /dev/null -w '%{http_code}
' "<某句 url>"   # 应为 200
cd work/test && node second.js                            # 26 项冒烟
```

已完成的第二篇：**2023 Text 4**（7 段 24 句，9 句精讲，48 词）。
`work/gen_t23_4.py` 是当前最完整的生成器模板，新篇照抄它。
`work/t23_4_*.py` 是成分数据样例（含两条已确认口径的示范）。

### 常见坑：PDF 声明的精讲句数 > 实际抓到的

`work/audit_extract.py` 会输出「PDF声明 vs 提取到」。若提取的更少，
大概率是 **PDF 本身少印了位置行**（如 2026 T1 第 3 段整段没有「第N段，第M句」，
2023 T4 声明 12 句但只有 9 个位置行）——这是源数据问题，不是解析 bug，
不要为了凑数去猜。确认方法：`python work/probe3.py <年> <篇>` 看该区原始排布。

### 一条命令提取素材（已可用，别再手写脚本）

```bash
python work/extract.py --year 2019 --text 2
```

产出 `work/raw/2019-text2.json`：段落英文/中文译文/切好的句子、
精讲句（含「第N段，第M句」与考点文字）、高频词表、来源 URL。
`work/verify_extract.py` 可比对提取结果与已上线数据（现 14/14 通过）。

提取脚本的几个坑（都已修，改脚本时别退回去）：
- **译文可能以拉丁字母开头**（「Flatiron School 是一所…」），靠「本段是否已出现
  首个 CJK 字符」判断，不能看首字符。
- **精讲句是「句子在前、位置行在后」**，而位置行之后是考点文字。必须只以
  「第N段，第M句」为锚点回溯，不能靠缩进——PDF 跨页后缩进会全部变成 0。
- **考点文字可能以英文引文开头**（`"It is true that ..."属于…`），
  所以判据是「含不含 CJK」而不是「是不是纯英文」。
- **词表是双列 × 每词三行**，且行间夹空行：必须按 2+ 空格切左右列，
  并用「下一个非空行」定位词性行与词频行（写死 i+1/i+2 会错位）。
- 切句要保护缩写点号（Mr. / e.g. / 3.5），否则会被切成两句。

### 然后补成分划分

```bash
python work/gen_t23_4.py          # ← 生成器模板，新篇照抄它
```

`gen.py` 是 2016 Text 1 专用的最早版本，里面的 `SOURCE` / `SENT_BASE` /
`year` / `text` / 输出文件名全是硬编码。**不要拿它当模板**，用 `gen_t23_4.py`：
它按 `work/raw/{年}-text{篇}.json` 读素材，来源 URL 自动拼，校验规则相同。

生成器会校验：每个 `bold` 子串、每个 `chunks.text` 都真实存在于原句、
成分按出现顺序、每个 bold 都有释义。**这是防手写数据打错字的主要防线，不要绕过。**
（2023 T4 就靠它抓出了「状语与定语从句重叠 → 覆盖率 128%」和 `there Is` 顺序颠倒。）

提取时注意两个坑：

- 译文可能以拉丁字母开头（如 `Flatiron School 是一所…`），不能靠首字符判断中英，要靠「本段是否已出现首个 CJK 字符」。
- 中英标点混用：提取出的译文里半角逗号要按上下文转全角。

## 测试

```bash
cd work/test && npm install     # jsdom + puppeteer
node inline.js   # 62 项：就地展开、不遮挡、链接、悬浮释义、↑↓、窄屏
node e2e.js      # 43 项：加粗无损、成分内容、词汇表排序/筛选（jsdom）
node skel.js     # 整句对照无损重建（未覆盖词必须原样保留）
node shot.js     # 截图到 work/test/*.png
```

改 `app.js` / `style.css` 后跑 `inline.js` + `e2e.js`。改成分数据后跑 `skel.js`。

**`:visited` 会打乱精讲句的下划线（真实踩过的坑）。**
句子的 `<a href>` 指向原站解析页，用户 Ctrl/⌘+点击打开过之后，浏览器把该 URL
记为已访问，`a.sent:visited{text-decoration:none}`（优先级 0,2,1）就压过了
`.sent.insight{text-decoration:underline}`（0,2,0），下划线整个消失、看起来是黑色。
因为「已访问」记在**浏览器历史**而非页面/store 里，**刷新不会恢复**，只有悬浮时
短暂复活（`.sent.insight:hover` 为 0,3,0）。这个现象极易被误判成缓存问题。
因此 `.sent.insight` 必须显式带上 `a.sent.insight:visited` / `:link` 一并声明。
回归测试见 `work/test/cascade.js`（注入同权重规则模拟 :visited）。
注意：puppeteer 里 Chromium 会禁用 `:visited` 样式，直接访问 URL 测不出来。

**排查「颜色/样式不对」时，不要只信 `getComputedStyle`。** 它返回的是 CSS 声明值，
不是实际绘制的像素。曾经据此回复「下划线是橙色、没问题」，而用户看到的黑线真实存在
（`border-bottom:dotted currentColor` 在 `color:inherit` 后变成了近黑色）。
正确做法是**截图像素**：`work/test/pixel.js` 用 `page.screenshot({clip})` 取细带、
在页面内用 canvas 读 RGB 来判定。颜色类问题以像素为准。

**写测试时注意**：`puppeteer` 的 `page.click()` 打的是元素**几何中心**，多行句子的
中心会落在行间空白、命中不到任何元素。要先用 `Range` 取首段文字的真实矩形再点
（见 `inline.js` 的 `clickSentence`）。另外**拿到元素坐标后如果又滚动了页面，
坐标就失效了**——必须重新测量，否则测出的是假失败。

一个已踩过的坑：`.legend` 用 `display:flex`，作者样式会盖过浏览器默认的 `[hidden]{display:none}`，导致 `hidden` 属性失效。`style.css` 已用 `[hidden]{display:none !important}` 兜底，保留它。

## 设计约定

- 界面全中文；正文字体用衬线（Georgia），中文用 PingFang SC / 微软雅黑。
- **译文常显，且按正文样式排**（不是灰色脚注、不用点按钮）。
  用户的原话是「要像在看文章，不要像在看题目」——把译文藏起来恰恰是「像题面」的主因。
  顶栏按钮反过来用：默认「只看英文」，点了才隐藏译文（供先自测原文）。
- 段落**按书籍排版**：段号 `¶1` 放左侧页边（sticky），正文占主栏；
  不用卡片描边/投影——卡片感是「像题卡」的另一来源。
  窄屏（≤640px）塌成单栏，**注意 `.en/.zh {grid-column:1}` 的媒体查询必须写在
  `.en{grid-column:2}` 之后**，否则同优先级被覆盖，窄屏会多出一栏、正文只占一半宽。
- 加粗词用**同色加粗 + 淡底纹**，不染橙色：满篇橙色会读成「到处是标记」而非文章。
- **解析面板必须「就地展开」**（插在被点句子的下一行、同段落内）。不要改回浮层
  （右侧抽屉 / 底部弹窗 / 悬浮卡片）。用户明确否决过前两者：浮层必然盖住你正在
  解释的那句话，为此需要遮罩、拖拽调高、高度记忆、重新滚动、底部内边距补偿——
  这些补丁本身就是 bug 来源（曾出现「双击复位把面板关掉」「点另一句被遮罩吃掉」）。
  就地展开没有这些结构性问题。
- 配色：`roleColor()` 对未知成分用 hash 兜底取色，**新增成分类型不会退化成灰色**，不要改成固定白名单。
- 加粗按文本节点处理，不用 `innerHTML` 字符串替换。
- 精讲句渲染为 `<a>`（href 指向原站该句解析页），但**普通左键被 `preventDefault` 拦截**
  改为就地展开；只有 Ctrl/⌘+点击、中键才真正跳转。改 `onPassageClick` 时注意保留这个分工。

## 已知未做的

- 其余 43 篇数据（最大工作量，需用户确认样板效果后再铺开）
- 题目与选项、逐题解析（PDF 有，尚未纳入）
