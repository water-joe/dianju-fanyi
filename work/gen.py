# -*- coding: utf-8 -*-
"""Merge hand-authored 成分划分/译文/加粗 with the extracted English text,
then emit site/data/2016-text1.js  (plain script, sets window.PASSAGE)."""
import io, json, re, os

RAW = json.load(io.open('work/t1_raw.json', encoding='utf-8'))


# ---- 加粗词条的释义（鼠标悬浮显示） --------------------------------------
GLOSS = {
    'essential': 'adj. 必不可少的；本质的',
    'coding': 'n. 编程；编码',
    'catch up': '赶上；追上（catch up after 在…之后补上）',
    'introductory courses': '入门课程（introductory adj. 入门的）',
    'assistant': 'adj. 副的｜这里 assistant dean = 副院长（不是"助手"）',
    'early exposure': '早期接触（exposure n. 接触；暴露）',
    'beneficial': 'adj. 有益的',
    'confusing': 'adj. 令人困惑的',
    'endless string of': '无穷无尽的（一串）…（string n. 一连串）',
    'build apps': '构建应用程序（app 为 application 的缩写）',
    'test hypotheses': '检验假设（hypothesis n. 假设，复数为 hypotheses）',
    'transform': 'v. 使转变；彻底改变',
    'thought processes': '思维过程（process n. 过程）',
    'Breaking down': '分解；拆解（break down 拆开、细分为）',
    'bite-sized chunks': '小块（bite-sized adj. 一口大小的；chunk n. 块）',
    'increase': 'v. 增加；提高',
    'interested in': '对…感兴趣（be interested in）',
    'fill the jobs gap': '填补就业缺口（gap n. 缺口、差距）',
    'benefit from': '从…中受益',
    'packed to the brim': '挤得满满当当（brim n. 边缘）',
    'drive': 'v. 驱使；迫使｜drive sb away 把某人赶走',
    'less-determined': 'adj. 决心不够坚定的（determined adj. 坚决的）',
    'started as': '起初是…；以…起家',
    'coding bootcamps': '编程训练营（bootcamp n. 集训营）',
    'career change': '职业转变',
    'curriculum': 'n. 课程（体系）',
    'gear lessons toward': '使课程面向…（gear v. 使适应、调整）',
    'instructor': 'n. 讲师；教员',
    'For instance': '例如（= for example，instance n. 例子）',
    'suggests': 'v. 推荐；建议｜此处指"推荐"影片',
    'based on': '基于；根据',
    'drop out of': '从…辍学；退出',
    'build the next Facebook': '创建下一个 Facebook｜喻指创办下一家巨头公司',
    'quick turnover': '快速更替（turnover n. 更新换代、人员流动）',
    'relevant': 'adj. 相关的；有用的',
    'job market': '就业市场',
    'think logically': '有逻辑地思考（副词 logically 修饰 think）',
    'organize the results': '梳理、组织结果',
    'apply to': '适用于；应用于',
    'education consultant': '教育顾问（consultant n. 顾问）',
    'go into': '进入（某行业）',
    'at all': '根本、全然｜用于加强否定语气',
    'army of coders': '程序员大军（army n. 大批、军团）',
    'sole purpose': '唯一目的（sole adj. 唯一的）',
    'surrounded by': '被…包围（be surrounded by）',
    'for the rest of their lives': '在他们的余生',
    'coax': 'v. 哄劝；诱使｜coax sb into doing 哄某人做某事',
    'the power to do that': '做那件事的能力（power n. 能力）',
}

# ---- per-sentence analysis, keyed by sentence id -------------------------
# zh        : 本句中文翻译
# insight   : 是否入选 PDF 的「真题句逐层精讲」(需在原文下画线)
# note      : 精讲考点原文（取自 PDF SENTENCE INSIGHTS 一节）
# bold      : 重点单词/词组（须为 en 的子串）
# chunks    : 成分划分，按出现顺序
A = {}

A['P1S1'] = dict(
    zh='诚然，高中编程课程对于在大学学习计算机科学并非必不可少。',
    insight=True,
    note='"It is true that ..."属于英语中非常常见的评价框架，考试阅读和写作里都很典型。掌握后可迁移到"It is clear that"等大量同类句式。',
    bold=['essential', 'coding'],
    chunks=[
        dict(role='形式主语', text='It', note='指代后文 that 从句'),
        dict(role='谓语', text="'s", note='is 的缩写'),
        dict(role='表语', text='true'),
        dict(role='连接词', text='that', note='引导主语从句'),
        dict(role='主语', text='high-school coding classes', note='主语从句的主语'),
        dict(role='谓语', text="aren't", note='主语从句的谓语'),
        dict(role='表语', text='essential', note='主语从句的表语'),
        dict(role='状语', text='for learning computer science', note='目的状语'),
        dict(role='状语', text='in college', note='地点状语'),
    ])

A['P1S2'] = dict(
    zh='卡内基梅隆大学计算机科学学院的副院长 Tom Cortina 表示，没有经验的学生在学习几门入门课程后就能赶上进度。',
    insight=False, note='', bold=['catch up', 'introductory courses', 'assistant'],
    chunks=[
        dict(role='主语', text='Students'),
        dict(role='定语', text='without experience', note='介词短语作后置定语'),
        dict(role='谓语', text='can catch up', note='情态动词 + 动词短语'),
        dict(role='状语', text='after a few introductory courses', note='时间状语'),
        dict(role='谓语', text='said', note='引述动词，倒装于句末'),
        dict(role='主语', text='Tom Cortina', note='引述分句的主语'),
        dict(role='同位语', text="the assistant dean at Carnegie Mellon's School of Computer Science", note='说明 Tom Cortina 的身份'),
    ])

A['P2S1'] = dict(
    zh='然而，Cortina 说，早期接触是有益的。',
    insight=True,
    note='“某人说＋后接一个完整判断内容”是非常常见的阅读句式，后半段又是典型主系表。掌握这种识别路径后，能迁移到大量类似句子。',
    bold=['early exposure', 'beneficial'],
    chunks=[
        dict(role='连接词', text='However', note='转折'),
        dict(role='插入语', text='Cortina said'),
        dict(role='主语', text='early exposure'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='beneficial'),
    ])

A['P2S2'] = dict(
    zh='当年幼的孩子学习计算机科学时，他们会了解到这不仅仅是令人困惑的、无穷无尽的字母和数字串，而是构建应用程序、创作艺术作品或检验假设的工具。',
    insight=False, note='',
    bold=['confusing', 'endless string of', 'build apps', 'test hypotheses'],
    chunks=[
        dict(role='状语从句', text='When younger kids learn computer science', note='时间状语从句'),
        dict(role='主语', text='they'),
        dict(role='谓语', text='learn'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='主语', text='it', note='宾语从句的主语'),
        dict(role='谓语', text="'s", note='宾语从句的谓语'),
        dict(role='表语', text='not just a confusing, endless string of letters and numbers', note='not just ... but ... 并列'),
        dict(role='连接词', text='but'),
        dict(role='表语', text='a tool'),
        dict(role='定语', text='to build apps, or create artwork, or test hypotheses', note='不定式作后置定语'),
    ])

A['P2S3'] = dict(
    zh='对他们来说，转变思维过程并不像对年龄较大的学生那样困难。',
    insight=False, note='',
    bold=['transform', 'thought processes'],
    chunks=[
        dict(role='形式主语', text='It'),
        dict(role='谓语', text="'s"),
        dict(role='表语', text='not as hard', note='as ... as 比较结构'),
        dict(role='状语', text='for them', note='不定式的逻辑主语'),
        dict(role='主语', text='to transform their thought processes', note='真主语，不定式短语'),
        dict(role='状语从句', text='as it is for older students', note='比较状语从句'),
    ])

A['P2S4'] = dict(
    zh='将问题分解成小块并使用代码解决它们成为常态。',
    insight=True,
    note='“动名词短语作主语 + 系动词 + 表语”是英语里很常见、也很值得掌握的句型。句首并列两个动作来充当主语，也有较强迁移价值。',
    bold=['Breaking down', 'bite-sized chunks'],
    chunks=[
        dict(role='主语', text='Breaking down problems into bite-sized chunks', note='动名词短语作主语'),
        dict(role='连接词', text='and'),
        dict(role='主语', text='using code to solve them', note='并列的动名词短语'),
        dict(role='谓语', text='becomes'),
        dict(role='表语', text='normal'),
    ])

A['P2S5'] = dict(
    zh='Cortina 说，让更多儿童接受这种训练可以增加对该领域感兴趣的人数，并有助于填补就业缺口。',
    insight=True,
    note='"引述动词 + 宾语从句" 和 "动名词短语作主语 + 情态动词谓语 + 并列结构" 都是四六级和考研阅读中的高频句式，掌握后可在大量真题中复用，具有较强的代表性。',
    bold=['increase', 'interested in', 'fill the jobs gap'],
    chunks=[
        dict(role='主语', text='Giving more children this training', note='动名词短语作主语，后接双宾语'),
        dict(role='谓语', text='could increase', note='情态动词'),
        dict(role='宾语', text='the number of people interested in the field', note='interested in the field 为过去分词短语作后置定语'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='help fill the jobs gap', note='并列谓语'),
        dict(role='插入语', text='Cortina said'),
    ])

A['P3S1'] = dict(
    zh='学生在上大学之前学习一些编程知识也会受益，因为大学的计算机科学入门课程人满为患，这可能会让经验较少或决心不够坚定的学生望而却步。',
    insight=True,
    note='本句覆盖主语、谓语、宾语（含动名词短语作宾语）、状语（时间状语从句、程度状语、方式状语）、定语从句（非限制性）等多种成分。动名词短语 "learning something about coding" 作宾语、"be packed to the brim" 的被动结构、关系副词 where 和关系代词 which 的区分、情态动词 can 的识别，都是值得练习的知识点。成分种类丰富，适合作为划分练习句。',
    bold=['benefit from', 'packed to the brim', 'drive', 'less-determined'],
    chunks=[
        dict(role='主语', text='Students'),
        dict(role='状语', text='also'),
        dict(role='谓语', text='benefit'),
        dict(role='状语', text='from learning something about coding', note='介词短语作状语，动名词作宾语'),
        dict(role='状语从句', text='before they get to college', note='时间状语从句'),
        dict(role='关系副词', text='where', note='非限制性定语从句'),
        dict(role='主语', text='introductory computer-science classes', note='定语从句的主语'),
        dict(role='谓语', text='are packed', note='被动语态'),
        dict(role='状语', text='to the brim', note='程度状语'),
        dict(role='关系代词', text='which', note='非限制性定语从句，which 作主语'),
        dict(role='谓语', text='can drive', note='情态动词'),
        dict(role='宾语', text='the less-experienced or less-determined students'),
        dict(role='状语', text='away', note='结果'),
    ])

A['P4S1'] = dict(
    zh='Flatiron School 是一所人们付费学习编程的学校，最初是众多编程训练营之一，这些训练营在寻求职业转变的成年人中变得流行起来。',
    insight=True,
    note='主句嵌套两层定语从句的结构在四六级和考研阅读中高频出现，非限制性与限制性定语从句的对比、关系副词 where 和关系代词 that 的用法都是典型考点，学习迁移价值高。',
    bold=['started as', 'coding bootcamps', 'career change'],
    chunks=[
        dict(role='主语', text='The Flatiron School'),
        dict(role='关系副词', text='where', note='非限制性定语从句'),
        dict(role='主语', text='people', note='定语从句的主语'),
        dict(role='谓语', text='pay'),
        dict(role='状语', text='to learn programming', note='目的状语'),
        dict(role='谓语', text='started'),
        dict(role='状语', text='as one of the many coding bootcamps', note='as 短语作状语'),
        dict(role='关系代词', text='that', note='限制性定语从句'),
        dict(role='谓语', text='have become'),
        dict(role='表语', text='popular'),
        dict(role='状语', text='for adults looking for a career change', note='looking for... 为现在分词短语作后置定语'),
    ])

A['P4S2'] = dict(
    zh='高中生接受同样的课程，但教师 Victoria Friedman 说，“我们试图让课程面向他们感兴趣的事物”。',
    insight=True,
    note='“事实陈述 + but 转折 + 直接引语/引述来源”是新闻报道和说明文里很常见的句式；名词后接限制性修饰结构也极有代表性，学会后迁移性强。',
    bold=['curriculum', 'gear lessons toward', 'instructor'],
    chunks=[
        dict(role='主语', text='The high-schoolers'),
        dict(role='谓语', text='get'),
        dict(role='宾语', text='the same curriculum'),
        dict(role='连接词', text='but'),
        dict(role='主语', text='we', note='引语分句的主语'),
        dict(role='谓语', text='try'),
        dict(role='宾语', text='to gear lessons toward things', note='不定式作宾语'),
        dict(role='定语从句', text="they're interested in", note='省略关系代词 that'),
        dict(role='谓语', text='said', note='引述动词'),
        dict(role='主语', text='Victoria Friedman'),
        dict(role='同位语', text='an instructor'),
    ])

A['P4S3'] = dict(
    zh='例如，学生正在开发的一个应用程序根据你的心情推荐电影。',
    insight=True,
    note='这句结构典型、难度适中，既不会简单到没有训练价值，也不会复杂到一上来就劝退。对于练习抓主干、识别定语从句和区分两个时态，很值得优先纳入训练。',
    bold=['For instance', 'suggests', 'based on'],
    chunks=[
        dict(role='插入语', text='For instance'),
        dict(role='主语', text='one of the apps the students are developing', note='内含定语从句 the students are developing，省略关系代词 that'),
        dict(role='谓语', text='suggests'),
        dict(role='宾语', text='movies'),
        dict(role='定语', text='based on your mood', note='过去分词短语作后置定语'),
    ])

A['P5S1'] = dict(
    zh='Flatiron 班级的学生可能不会从高中辍学去创建下一个 Facebook。',
    insight=False, note='',
    bold=['drop out of', 'build the next Facebook'],
    chunks=[
        dict(role='主语', text='The students in the Flatiron class', note='in the Flatiron class 为介词短语作后置定语'),
        dict(role='状语', text='probably'),
        dict(role='谓语', text="won't drop out of high school", note='情态动词否定'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='build the next Facebook', note='并列谓语'),
    ])

A['P5S2'] = dict(
    zh='编程语言更新换代很快，因此他们学习的 Ruby on Rails 语言到他们进入就业市场时甚至可能已经不再相关。',
    insight=True,
    note='因果并列句 + 定语从句 + 时间状语从句的组合是四六级和考研阅读中的高频句式。情态动词推测、定语从句省略关系代词、时间从句用一般现在时代替将来时，这些都是标准考点，掌握后可迁移到大量类似句子。',
    bold=['quick turnover', 'relevant', 'job market'],
    chunks=[
        dict(role='主语', text='Programming languages'),
        dict(role='谓语', text='have'),
        dict(role='宾语', text='a quick turnover'),
        dict(role='连接词', text='so', note='因果并列连词'),
        dict(role='主语', text='the "Ruby on Rails" language they learned', note='内含定语从句 they learned，省略关系代词 that'),
        dict(role='谓语', text='may not even be'),
        dict(role='表语', text='relevant'),
        dict(role='状语从句', text='by the time they enter the job market', note='时间状语从句'),
    ])

A['P5S3'] = dict(
    zh='但北卡罗来纳州教育顾问 Deborah Seehorn 说，他们学到的技能——如何从逻辑上思考问题并组织结果——适用于任何编程语言。',
    insight=True,
    note='本句的结构特征（主语含定语从句修饰、插入同位语说明、主句陈述观点）在四六级和考研阅读中较为常见，尤其是定语从句嵌入主语、关系代词省略的用法是高频考点。转折连词 "But" 开头也是典型的论述句式。掌握本句结构对理解类似长难句有较好的迁移价值。',
    bold=['think logically', 'organize the results', 'apply to', 'education consultant'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='the skills they learn', note='内含定语从句 they learn，省略关系代词 that'),
        dict(role='同位语', text='how to think logically through a problem and organize the results', note='插入同位语，解释 skills'),
        dict(role='谓语', text='apply'),
        dict(role='状语', text='to any coding language'),
        dict(role='谓语', text='said', note='引述动词'),
        dict(role='主语', text='Deborah Seehorn'),
        dict(role='同位语', text='an education consultant for the state of North Carolina'),
    ])

A['P6S1'] = dict(
    zh='事实上，Flatiron 的学生可能根本不会进入 IT 行业。',
    insight=True,
    note='“主语 + 情态动词 + 否定 + 动词原形 + 介词短语”是很常见、可迁移的英语句型。掌握这种骨架后，处理大量含可能性判断的句子都会更顺手。',
    bold=['go into', 'at all'],
    chunks=[
        dict(role='状语', text='Indeed'),
        dict(role='主语', text='the Flatiron students'),
        dict(role='谓语', text='might not go', note='情态动词否定'),
        dict(role='状语', text='into IT'),
        dict(role='状语', text='at all', note='加强否定语气'),
    ])

A['P6S2'] = dict(
    zh='但培养未来的程序员大军并非这些课程的唯一目的。',
    insight=False, note='',
    bold=['army of coders', 'sole purpose'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='creating a future army of coders', note='动名词短语作主语'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='not the sole purpose of the classes'),
    ])

A['P6S3'] = dict(
    zh='这些孩子在他们余生中都将被计算机包围——在他们的口袋里、办公室里、家里。',
    insight=False, note='',
    bold=['surrounded by', 'for the rest of their lives'],
    chunks=[
        dict(role='主语', text='These kids'),
        dict(role='谓语', text='are going to be surrounded', note='一般将来时被动语态'),
        dict(role='状语', text='by computers', note='施动者'),
        dict(role='同位语', text='in their pockets, in their offices, in their homes', note='插入成分，补充说明 computers'),
        dict(role='状语', text='for the rest of their lives', note='时间状语'),
    ])

A['P6S4'] = dict(
    zh='他们越早学会计算机如何思考，如何哄骗机器产出他们想要的东西——越早学会他们有能力做到这一点——就越好。',
    insight=True,
    note='覆盖主语、谓语、宾语、状语、表语等多种成分，且存在省略主语和系动词、宾语从句充当宾语、不定式作定语等多个易错点，非常适合作为成分划分的综合练习句。',
    bold=['coax', 'the power to do that'],
    chunks=[
        dict(role='状语从句', text='The younger they learn', note='the + 比较级，引导状语从句'),
        dict(role='宾语从句', text='how computers think'),
        dict(role='宾语从句', text='how to coax the machine into producing what they want', note='疑问词 + 不定式'),
        dict(role='状语从句', text='the earlier they learn'),
        dict(role='宾语从句', text='that they have the power to do that'),
        dict(role='表语', text='the better', note='主句：the + 比较级'),
    ])

# ---- vocabulary (PDF HIGH-FREQUENCY 表，2016 Text 1 节选出 32 词) ----------
VOCAB = [
    ('career', 'B1', 'n.', '职业', 2, 42), ('app', 'B1', 'n.', '应用程序', 2, 16),
    ('exposure', 'B2', 'n.', '暴露', 2, 12), ('interested', 'A1', 'adj.', '感兴趣的', 2, 12),
    ('accord', 'C1', 'n.', '（国家、团体间的）协议', 1, 172), ('power', 'A2', 'n.', '权力', 1, 90),
    ('benefit', 'B1', 'n.', '好处', 1, 88), ('process', 'B1', 'n.', '过程', 1, 80),
    ('better', 'A1', 'adj.', '更好的（good 的比较级）', 1, 70), ('challenge', 'B1', 'n.', '挑战', 1, 57),
    ('gap', 'B1', 'n.', '间隙', 1, 45), ('base', 'A2', 'n.', '基础', 1, 43),
    ('production', 'B1', 'n.', '生产', 1, 42), ('apply', 'A2', 'v.', '申请', 1, 33),
    ('thinking', 'A2', 'n.', '思考', 1, 33), ('academic', 'B2', 'adj.', '学术的', 1, 28),
    ('essential', 'B1', 'adj.', '必不可少的', 1, 27), ('prospect', 'B2', 'n.', '可能性', 1, 25),
    ('indeed', 'B1', 'adv.', '确实，的确（强调肯定）', 1, 24), ('instance', 'B2', 'n.', '例子', 1, 17),
    ('solve', 'A2', 'v.', '解决（问题、困难）', 1, 16), ('upgrade', 'B2', 'v.', '升级', 1, 16),
    ('code', 'B1', 'n.', '代码', 1, 15), ('enable', 'B1', 'v.', '使能够', 1, 15),
    ('deliver', 'B1', 'v.', '递送，运送', 1, 14), ('relevant', 'B2', 'adj.', '相关的', 1, 14),
    ('transform', 'B2', 'v.', '使彻底改变；使转变', 1, 14), ('mood', 'A2', 'n.', '心情', 1, 12),
    ('compete', 'B1', 'v.', '竞争', 1, 10), ('innovative', 'B2', 'adj.', '创新的', 1, 10),
    ('assistant', 'A2', 'n.', '助手', 1, 9), ('organize', 'B1', 'v.', '组织，安排', 1, 8),
]

# 来源链接：从 PDF 页脚提取，对应本篇的解析页（已校验可达）。
# 规律：section2-part-a-N 即 Text N。
SOURCE = 'https://english-exam.lazynote.cn/kaoyan/sections/2016-english-two/section2-part-a-1/'

# 单句解析页：在 SOURCE 基础上加 p{段}-s{句}。
# 注意——只有「真题句逐层精讲」选中的句子才有独立页面，
# 其余句子实测 301 → 对象存储 → 404。所以非精讲句不给 url，
# 前端据此决定是否渲染为链接（否则就是死链）。
SENT_BASE = 'https://english-exam.lazynote.cn/kaoyan/paper/2016-english-two/section2-part-a-1/'

def sent_url(sid):
    """'P3S1' -> '.../p3-s1/'；非精讲句返回 ''。"""
    import re as _re
    m = _re.match(r'^P(\d+)S(\d+)$', sid)
    return SENT_BASE + 'p%s-s%s/' % (m.group(1), m.group(2)) if m else ''

# ---- merge + validate ----------------------------------------------------
report, problems = [], []
for p in RAW:
    for s in p['sentences']:
        sid = s['id']
        if sid not in A:
            problems.append('MISSING analysis for %s' % sid); continue
        a = A[sid]
        s.update(a)
        # bold 由纯字符串升级为 {text, gloss}，gloss 供鼠标悬浮显示
        bolded = []
        for b in a['bold']:
            if b.lower() not in s['en'].lower():
                problems.append('BOLD not found in %s: %r' % (sid, b))
            if b not in GLOSS:
                problems.append('NO GLOSS for %r (in %s)' % (b, sid))
            bolded.append(dict(text=b, gloss=GLOSS.get(b, '')))
        s['bold'] = bolded
        covered = 0
        pos = 0
        for c in a['chunks']:
            i = s['en'].find(c['text'], pos)
            if i < 0:
                i = s['en'].find(c['text'])
                if i < 0:
                    problems.append('CHUNK not found in %s: %r' % (sid, c['text'])); continue
                problems.append('CHUNK out-of-order in %s: %r' % (sid, c['text']))
            pos = i + len(c['text'])
            covered += len(c['text'])
        s['cover'] = round(100.0 * covered / max(1, len(s['en'])))
        # 只有精讲句有独立解析页，其余留空 → 前端不渲染成链接
        s['url'] = sent_url(sid) if a['insight'] else ''
        report.append('%-6s cover=%3d%% chunks=%2d bold=%d %s' % (
            sid, s['cover'], len(a['chunks']), len(a['bold']),
            'INSIGHT' if a['insight'] else ''))

PASSAGE = dict(
    year=2016, text=1, title='2016 考研英语二 · Text 1',
    subtitle='高中编程课与 Flatiron School',
    source=SOURCE,
    paragraphs=[dict(id=p['id'], zh=p['zh'], sentences=p['sentences']) for p in RAW],
    vocab=[dict(word=w, level=l, pos=p_, cn=c, count=n, freq=f) for (w, l, p_, c, n, f) in VOCAB],
)

os.makedirs('site/data', exist_ok=True)
js = 'window.PASSAGE = ' + json.dumps(PASSAGE, ensure_ascii=False, indent=1) + ';\n'
io.open('site/data/2016-text1.js', 'w', encoding='utf-8').write(js)

print('\n'.join(report))
print('\nsentences=%d  paragraphs=%d  vocab=%d' % (
    sum(len(p['sentences']) for p in PASSAGE['paragraphs']),
    len(PASSAGE['paragraphs']), len(PASSAGE['vocab'])))
print('avg chunk coverage = %.1f%%' % (
    sum(s['cover'] for p in PASSAGE['paragraphs'] for s in p['sentences'])
    / sum(len(p['sentences']) for p in PASSAGE['paragraphs'])))
print('\nPROBLEMS (%d):' % len(problems))
for x in problems: print('  !', x)
print('\nwrote site/data/2016-text1.js  (%d bytes)' % len(js.encode('utf-8')))
