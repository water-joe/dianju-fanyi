# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 4 —— 逐句成分划分与重点词释义。

这是全项目唯一无法自动化的部分：PDF 里没有逐词成分标注
（网页版有结构树，打印时丢失），只能逐句人工判断。

口径（与用户确认过，见 CLAUDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""

# key = 句子 id (段落 P1..P7 + 句序)
# zh        : 本句中文翻译
# insight   : 是否为 PDF「真题句逐层精讲」选中的句子（需画线 + 有原站解析页）
# note      : 精讲考点文字（取自 PDF）
# bold      : 重点单词/词组（须为 en 的子串）
# chunks    : 成分划分，按出现顺序；role 见 app.js 的 ROLE_COLORS
A = {}

A['P1S1'] = dict(
    zh='青少年是充满矛盾的。',
    insight=False, note='',
    bold=['paradoxical'],
    chunks=[
        dict(role='主语', text='Teenagers'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='paradoxical'),
    ])

A['P1S2'] = dict(
    zh='这是一种温和而超然的说法，而父母们在表达同样的事情时，往往会用强烈得多的语言。',
    insight=False, note='',
    bold=['detached', 'express'],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text="'s"),
        dict(role='表语', text='a mild and detached way of saying something',
             note='of saying something 为介词短语作后置定语'),
        # 方式状语必须放在定语从句内部，否则会与定语从句重叠重复计数
        # （原写法两个 chunk 都含 with...language，覆盖率算出 128%）
        dict(role='定语从句',
             text='that parents often express with considerably stronger language',
             note='修饰 something'),
    ])

A['P1S3'] = dict(
    zh='但这种矛盾既是科学层面的，也是个人层面的。',
    insight=False, note='',
    bold=['paradox'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='the paradox'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='scientific as well as personal',
             note='as well as 连接两个并列表语'),
    ])

A['P1S4'] = dict(
    zh='在青春期，那些几乎所有事情都依赖成年人的无助且依赖他人的孩子，会变成能够照顾自己并互相帮助的独立个体。',
    insight=True,
    note='本句主干是「children become independent people」，中间插入了两个定语从句分别修饰主语和表语，'
         '是典型的「长主语 + 系动词 + 长表语」结构。难点在于：主语和表语都带定语从句，'
         '容易把从句里的谓语误当成主句谓语。先抓主干（children become people），再看两个从句。',
    bold=['In adolescence', 'relied on', 'take care of'],
    chunks=[
        dict(role='状语', text='In adolescence', note='时间状语'),
        dict(role='主语', text='helpless and dependent children who have relied on grown-ups for just about everything',
             note='内含定语从句 who have relied on... 修饰 children'),
        dict(role='谓语', text='become'),
        dict(role='表语', text='independent people who can take care of themselves and help each other',
             note='内含定语从句 who can take care of... 修饰 people'),
    ])

A['P1S5'] = dict(
    zh='与此同时，曾经快乐顺从的孩子变成了叛逆的、爱冒险的青少年。',
    insight=False, note='',
    bold=['compliant', 'rebellious', 'risk-takers'],
    chunks=[
        dict(role='状语', text='At the same time'),
        dict(role='主语', text='once cheerful and compliant children',
             note='once 此处为形容词「曾经的」'),
        dict(role='谓语', text='become'),
        dict(role='表语', text='rebellious teenage risk-takers'),
    ])

A['P2S1'] = dict(
    zh='莱顿大学的 Eveline Crone 及其同事发表在《儿童发展》期刊上的一项新研究表明，青少年的积极面与消极面是相伴而生的。',
    insight=True,
    note='主句被多重后置定语（published in... / by Eveline Crone...）拉长，'
         '谓语 suggests 一直拖到句子后半段才出现，后面接 that 宾语从句。'
         '这是学术英语最典型的「长主语 + 后置修饰 + 引述动词」结构，'
         '练习先跳过中间修饰、直接定位谓语 suggests。',
    bold=['published', 'suggests', 'go hand in hand'],
    chunks=[
        dict(role='主语', text='A new study published in the journal Child Development, by Eveline Crone of the University of Leiden and colleagues',
             note='published in... 为过去分词短语作后置定语；by Eveline Crone... 说明发表者'),
        dict(role='谓语', text='suggests', note='引述动词'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='主语', text='the positive and negative sides of teenagers',
             note='宾语从句的主语'),
        dict(role='谓语', text='go hand in hand',
             note='固定搭配：相伴而生、密切相关'),
    ])

A['P2S2'] = dict(
    zh='这项研究是关于青春期的新一轮思考的一部分。',
    insight=False, note='',
    bold=['a new wave of'],
    chunks=[
        dict(role='主语', text='The study'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='part of a new wave of thinking about adolescence'),
    ])

A['P2S3'] = dict(
    zh='长期以来，科学家和政策制定者都聚焦于这样一种观念：青少年是一个需要被解决的问题。',
    insight=True,
    note='concentrate on the idea that... 里 that 引导的是同位语从句（说明 idea 的具体内容），'
         '不是定语从句——这是四六级和考研的高频易错点：'
         '同位语从句的 that 不做成分、不能省略，而定语从句的 that 要充当成分。'
         '从句内又嵌套一个 that 定语从句修饰 problem。',
    bold=['concentrated on', 'policy makers'],
    chunks=[
        dict(role='状语', text='For a long time'),
        dict(role='主语', text='scientists and policy makers'),
        dict(role='谓语', text='concentrated'),
        dict(role='状语', text='on the idea'),
        dict(role='同位语从句', text='that teenagers were a problem that needed to be solved',
             note='说明 idea 的内容；其中 that needed to be solved 是定语从句修饰 problem'),
    ])

A['P2S4'] = dict(
    zh='这项新的研究则强调，青春期既是一个充满风险的时期，也是一个充满机遇的时期。',
    insight=False, note='',
    bold=['emphasizes', 'as well as'],
    chunks=[
        dict(role='主语', text='The new work'),
        dict(role='谓语', text='emphasizes'),
        dict(role='连接词', text='that'),
        dict(role='主语', text='adolescence', note='宾语从句的主语'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='a time of opportunity as well as risk'),
    ])
