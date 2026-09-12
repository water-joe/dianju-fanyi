# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='随着Z世代成员在今春大学毕业——最普遍接受的定义认为这一代人出生于1995年之后，上下浮动一年——近几周来关注度一直在稳步上升。',
    insight=True, note='包含多个高频考点结构：状语从句引导复杂句、宾语从句、并列主句、完成进行时、被动语态、插入语。这些都是四六级和考研阅读理解中的常见句式，掌握后可以迁移到大量类似句子。句子长度和复杂度也符合考试真题特征，具有很强的代表性。',
    bold=['give or take', 'the attention has been rising'],
    chunks=[
        dict(role='状语从句', text='Now that members of Generation Z are graduating college this spring',
             note='now that 引导原因状语从句；现在进行时表将来'),
        dict(role='插入语', text='—the most commonly- accepted definition says this generation was born after 1995, give or take a year—',
             note='破折号内为插入语；says 后接省略 that 的宾语从句；give or take 上下浮动'),
        dict(role='主语', text='the attention',
             note=''),
        dict(role='谓语', text='has been rising',
             note=''),
        dict(role='状语', text='steadily in recent weeks.',
             note='现在完成进行时'),
    ])

A['P1S2'] = dict(
    zh='Z世代即将走上街头，在一个数十年来最为紧俏的劳动力市场中寻找工作。',
    insight=False, note='',
    bold=['hit the streets', 'labor market'],
    chunks=[
        dict(role='主语', text='Gen Zs',
             note=''),
        dict(role='谓语', text='are about to hit the streets',
             note=''),
        dict(role='状语', text="looking for work in a labor market that's tighter than it's been in decades.",
             note='现在分词作伴随状语；that... 定语从句；tighter than... 比较'),
    ])

A['P1S3'] = dict(
    zh='根据美国大学与雇主协会进行的一项调查，雇主们计划今年在美国为应届毕业生提供的工作岗位比去年多约17%。',
    insight=True, note='本句展现了新闻报道和学术写作中的典型结构：现在进行时陈述当前趋势、比较结构说明增长幅度、方式状语引出数据来源。这种"陈述事实+数据对比+出处说明"的句式在四六级和考研阅读中频繁出现,学生掌握后可复用到大量类似语境。虽然比较从句省略较多,但"more...than"结构本身是高频考点,因此结构代表性较强。',
    bold=['hiring', 'conducted by'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='employers',
             note=''),
        dict(role='谓语', text='are planning on hiring about 17 percent more new graduates for jobs in the U.S. this year than last,',
             note='more... than last (year) 比较结构，省略多'),
        dict(role='状语', text='according to a survey conducted by the National Association of Colleges and Employers.',
             note='conducted by... 过去分词短语作后置定语'),
    ])

A['P1S4'] = dict(
    zh='每个人都想知道那些即将入驻空置办公隔间的人将与他们的前辈有何不同。',
    insight=False, note='',
    bold=['cubicles', 'differ from'],
    chunks=[
        dict(role='主语', text='Everybody',
             note=''),
        dict(role='谓语', text='wants to know',
             note=''),
        dict(role='宾语从句', text='how the people who will soon inhabit those empty office cubicles will differ from those who came before them.',
             note='how 引导宾语从句；两个 who 定语从句分别修饰 people 和 those'),
    ])

A['P2S1'] = dict(
    zh='如果说"有权利意识"是最常用来形容千禧一代(出生于1981年至1995年间的人)的形容词，无论公平与否，那么Z世代的关键词则是务实和谨慎。',
    insight=True, note='条件状语从句+主句是四六级和考研阅读中的高频句式,If引导条件从句并包含后置定语和同位语的复杂修饰结构也很常见,这种对比论述的表达方式在议论文中经常出现,属于典型的学术写作句式,掌握后可大量复用。',
    bold=['entitled', 'catchwords'],
    chunks=[
        dict(role='状语从句', text='If "entitled" is the most common adjective, fairly or not, applied to millennials (those born between 1981 and 1995),',
             note='if 引导条件状语从句；applied to... 过去分词作后置定语；括号内为同位语'),
        dict(role='主语', text='the catchwords for Generation Z',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='practical and cautious.',
             note='两个并列表语'),
    ])

A['P2S2'] = dict(
    zh='根据研究他们的职业顾问和专家所言，Z世代是目光清醒的经济实用主义者。',
    insight=True, note='主系表结构搭配限制性定语从句是四六级和考研阅读中的高频句式,句首介词短语Accordingto引出观点来源也是学术和新闻语体的典型用法,掌握后可广泛迁移到类似语境;定语从句修饰状语内部名词的嵌套方式也具有一定代表性。',
    bold=['clear-eyed', 'pragmatists'],
    chunks=[
        dict(role='状语', text='According to the career counselors and experts who study them,',
             note='according to... 信息来源；who... 定语从句修饰 experts'),
        dict(role='主语', text='Generation Zs',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='clear-eyed, economic pragmatists.',
             note=''),
    ])
