# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S6'] = dict(
    zh='过多的快乐可能具有破坏性。',
    insight=False, note='',
    bold=['destructive'],
    chunks=[
        dict(role='主语', text='Too much happiness',
             note=''),
        dict(role='谓语', text='can be',
             note=''),
        dict(role='表语', text='destructive.',
             note=''),
    ])

A['P3S1'] = dict(
    zh='而内疚，通过促使我们更深入地思考自己的善良，可以鼓励人类弥补错误和修复关系。',
    insight=True, note='"主语+插入状语+情态动词+谓语+宾语+宾语补足语"的结构在四六级和考研阅读中非常典型，插入状语的使用和"encouragesbtodosth"的搭配都是高频考点。掌握本句的分析方法后，可以迁移到大量类似句式，代表性较强。',
    bold=['prompting', 'make up for'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='guilt,',
             note=''),
        dict(role='状语', text='by prompting us to think more deeply about our goodness,',
             note='by + 动名词表方式；prompt sb. to do 宾补'),
        dict(role='谓语', text='can encourage',
             note=''),
        dict(role='宾语', text='humans',
             note=''),
        dict(role='宾语补足语', text='to make up for errors and fix relationships.',
             note='encourage sb. to do 宾补；make up for 弥补'),
    ])

A['P3S2'] = dict(
    zh='换句话说，内疚可以帮助维系一个合作型物种。',
    insight=True, note='本句覆盖了主语、谓语（情态动词结构）、宾语、宾语补足语、状语（插入语）五种成分，成分种类较为丰富。特别是"canhelphold"这个三词谓语结构和"together"作宾语补足语的用法，对学习者有一定练习价值。但句子整体较短，缺少定语从句、状语从句等更复杂的修饰成分，训练深度有限。',
    bold=['hold a cooperative species together', 'cooperative species'],
    chunks=[
        dict(role='主语', text='Guilt,',
             note=''),
        dict(role='插入语', text='in other words,',
             note=''),
        dict(role='谓语', text='can help hold',
             note=''),
        dict(role='宾语', text='a cooperative species',
             note=''),
        dict(role='宾语补足语', text='together.',
             note='hold... together 使…凝聚'),
    ])

A['P3S3'] = dict(
    zh='它是一种社会黏合剂。',
    insight=False, note='',
    bold=['social glue'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a kind of social glue.',
             note=''),
    ])

A['P4S1'] = dict(
    zh='从这个角度来看，内疚是一个机会。',
    insight=False, note='',
    bold=['Viewed in this light'],
    chunks=[
        dict(role='状语', text='Viewed in this light,',
             note='过去分词短语作条件/方式状语'),
        dict(role='主语', text='guilt',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='an opportunity.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='多伦多大学心理学教授Tina Malti的研究表明，内疚可能弥补情感上的不足。',
    insight=True, note="本句的'主语+谓语+宾语从句'结构在四六级和考研阅读中极为常见，特别是学术类文章中引述研究结果时经常使用这种句式，具有较高的典型性和复用价值。",
    bold=['compensate for', 'emotional deficiency'],
    chunks=[
        dict(role='主语', text='Work by Tina Malti, a psychology professor at the University of Toronto,',
             note=''),
        dict(role='谓语', text='suggests',
             note=''),
        dict(role='宾语从句', text='that guilt may compensate for an emotional deficiency.',
             note='that 引导宾语从句；compensate for 弥补'),
    ])

A['P4S3'] = dict(
    zh='在多项研究中，Malti和其他研究者已经表明，内疚和同情可能代表通往合作和分享的不同途径。',
    insight=False, note='',
    bold=['pathways to'],
    chunks=[
        dict(role='状语', text='In a number of studies,',
             note=''),
        dict(role='主语', text='Malti and others',
             note=''),
        dict(role='谓语', text='have shown',
             note=''),
        dict(role='宾语从句', text='that guilt and sympathy may represent different pathways to cooperation and sharing.',
             note='that 引导宾语从句；pathways to 通往…的途径'),
    ])

A['P4S4'] = dict(
    zh='一些同情心较低的孩子可能通过体验更多内疚来弥补这一缺陷，这可以约束他们更恶劣的冲动。',
    insight=True, note='句子结构是典型的"主句加双定语从句"模式,限制性与非限制性定语从句并存,方式状语用介词by加动名词表达,这些都是四六级和考研阅读中高频出现的句式。掌握这个句子的拆分方法,可以直接迁移到大量类似长句的分析,代表性很强。',
    bold=['shortfall', 'rein in', 'impulses'],
    chunks=[
        dict(role='主语', text='Some kids who are low in sympathy',
             note='who... 定语从句修饰 kids'),
        dict(role='谓语', text='may make up for',
             note=''),
        dict(role='宾语', text='that shortfall',
             note=''),
        dict(role='状语', text='by experiencing more guilt,',
             note='by + 动名词表方式'),
        dict(role='定语从句', text='which can rein in their nastier impulses.',
             note='which 引导非限制性定语从句；rein in 约束'),
    ])
