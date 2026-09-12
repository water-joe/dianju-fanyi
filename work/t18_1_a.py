# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='令人好奇的是，Stephen Koziatek几乎感到自己必须为努力给学生创造更好未来的行为进行辩护。',
    insight=True, note='形式主语it+be+形容词+that从句是四六级和考研阅读中的高频句式，且本句还嵌套了asthough引导的状语从句，这种"评价+主语从句+内嵌状语"的组合在学术文本和议论文中极为常见，掌握后可大量迁移到其他同类句型。',
    bold=['justify', 'as though'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text='is curious',
             note=''),
        dict(role='主语从句', text='that Stephen Koziatek feels almost as though he has to justify his efforts to give his students a better future.',
             note='that 引导主语从句；as though 方式状语从句；to give... 不定式作目的状语'),
    ])

A['P2S1'] = dict(
    zh='Koziatek先生正参与一项开创性的事业。',
    insight=False, note='',
    bold=['pioneering'],
    chunks=[
        dict(role='主语', text='Mr. Koziatek',
             note=''),
        dict(role='谓语', text='is part of',
             note=''),
        dict(role='宾语', text='something pioneering.',
             note='pioneering 形容词作后置定语'),
    ])

A['P2S2'] = dict(
    zh='他是New Hampshire一所高中的教师，在那里学习不是关于书本、考试和机械记忆的事情，而是实践性的。',
    insight=True, note='主系表+后置定语从句的组合是四六级阅读和考研真题中的高频句式,where引导定语从句修饰地点名词也是典型用法,学习后可迁移到大量同类句子,代表性较强。',
    bold=['mechanical memorization', 'practical'],
    chunks=[
        dict(role='主语', text='He',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a teacher at a New Hampshire high school',
             note=''),
        dict(role='定语从句', text='where learning is not something of books and tests and mechanical memorization, but practical.',
             note='where 引导定语从句修饰 high school；not... but... 对比'),
    ])

A['P2S3'] = dict(
    zh='何时起人们开始普遍认为学生应该能说出美国第十三任总统的名字，却对一条断裂的自行车链条完全束手无策？',
    insight=True, note='形式主语it加后置主语从句、系表结构、情态动词加并列谓语,都是四六级和考研阅读中的高频句式。疑问句形式虽不如陈述句常见,但itbecomeacceptedthat这类结构在议论文中很典型,学会后可大量迁移到类似句型。',
    bold=['accepted wisdom', 'overwhelmed by'],
    chunks=[
        dict(role='状语', text='When',
             note=''),
        dict(role='谓语', text='did',
             note=''),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text='become accepted wisdom',
             note=''),
        dict(role='主语从句', text='that students should be able to name the 13th president of the United States but be utterly overwhelmed by a broken bike chain?',
             note='that 引导主语从句；should be able to... but be... 并列谓语'),
    ])

A['P3S1'] = dict(
    zh='正如Koziatek所知，几乎一切事物中都有学问。',
    insight=False, note='',
    bold=['just about everything'],
    chunks=[
        dict(role='状语', text='As Koziatek knows,',
             note='as 引导方式状语从句'),
        dict(role='谓语', text='there is',
             note=''),
        dict(role='主语', text='learning in just about everything.',
             note='there be 句型真正主语'),
    ])

A['P3S2'] = dict(
    zh='强迫学生在一张涂满涂鸦、粘着几代人丢弃的口香糖的课桌前学习几何，未必能有所收获。',
    insight=False, note='',
    bold=['graffitied', 'discarded chewing gum'],
    chunks=[
        dict(role='主语', text='Nothing',
             note=''),
        dict(role='谓语', text='is necessarily gained',
             note=''),
        dict(role='状语', text='by forcing students to learn geometry at a graffitied desk stuck with generations of discarded chewing gum.',
             note='by + 动名词表方式；force sb. to do 宾补；stuck with... 过去分词作后置定语'),
    ])

A['P3S3'] = dict(
    zh='他们也可以通过组装自行车来学习几何。',
    insight=False, note='',
    bold=['assembling'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='can also learn',
             note=''),
        dict(role='宾语', text='geometry',
             note=''),
        dict(role='状语', text='by assembling a bicycle.',
             note='by + 动名词表方式'),
    ])

A['P4S1'] = dict(
    zh='但他也发现了一种潜在的偏见。',
    insight=False, note='',
    bold=['insidious prejudice'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='he',
             note=''),
        dict(role='状语', text="'s also",
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语', text='a kind of insidious prejudice.',
             note='现在完成时；insidious 潜在的、暗中为害的'),
    ])
