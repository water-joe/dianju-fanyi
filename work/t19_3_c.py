# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S2'] = dict(
    zh='即便如此，雇主仍抱怨他们没有得到所需的全部工人。',
    insight=True, note='本句的"主句+宾语从句+定语从句"结构是四六级和考研阅读中的高频句式,宾语从句省略引导词、定语从句省略关系代词作宾语都是常考考点,且被动语态在宾语从句中的使用也很典型。学生掌握此句型后可大量迁移到其他真题句,典型性较高。',
    bold=['Even so', 'complain'],
    chunks=[
        dict(role='状语', text='Even so,',
             note=''),
        dict(role='主语', text='employers',
             note=''),
        dict(role='谓语', text='complain',
             note=''),
        dict(role='宾语从句', text="they aren't given all the workers they need.",
             note='省略 that 的宾语从句；被动语态；(that) they need 省略关系词的定语从句'),
    ])

A['P6S3'] = dict(
    zh='这一过程繁琐、昂贵且不可靠。',
    insight=False, note='',
    bold=['cumbersome'],
    chunks=[
        dict(role='主语', text='The process',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='cumbersome, expensive, and unreliable.',
             note='三个并列表语'),
    ])

A['P6S4'] = dict(
    zh='一项调查发现，官僚主义的延误导致H-2A工人平均晚到岗22天。',
    insight=False, note='',
    bold=['bureaucratic delays', 'on the job'],
    chunks=[
        dict(role='主语', text='One survey',
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语从句', text='that bureaucratic delays led the average H-2A worker to arrive on the job 22 days late.',
             note='that 引导宾语从句；lead sb. to do 宾补；on the job 到岗'),
    ])

A['P6S5'] = dict(
    zh='联邦移民突击检查加剧了短缺，这些检查驱逐了一些工人并迫使其他工人转入地下。',
    insight=False, note='',
    bold=['compounded', 'raids', 'drive others underground'],
    chunks=[
        dict(role='主语', text='The shortage',
             note=''),
        dict(role='谓语', text='is compounded by federal immigration raids,',
             note='被动语态；compound 加剧'),
        dict(role='定语从句', text='which remove some workers and drive others underground.',
             note='which 引导非限制性定语从句；并列谓语'),
    ])

A['P7S1'] = dict(
    zh='在2012年的一项调查中，71%的果树种植者和近80%的葡萄干和浆果种植者表示他们劳动力短缺。',
    insight=True, note='本句是典型的主语+said+宾语从句结构,在四六级和考研阅读中频繁出现,复合主语和省略that的宾语从句也是常考点,掌握后可大量复用到类似的调查报告、研究陈述类句子中。',
    bold=['raisin and berry growers', 'short of labor'],
    chunks=[
        dict(role='状语', text='In a 2012 survey,',
             note=''),
        dict(role='主语', text='71 percent of tree-fruit growers and almost 80 percent of raisin and berry growers',
             note=''),
        dict(role='谓语', text='said',
             note=''),
        dict(role='宾语从句', text='they were short of labor.',
             note='省略 that 的宾语从句；be short of 缺少'),
    ])

A['P7S2'] = dict(
    zh='一些西部农民的应对方式是将业务转移到墨西哥。',
    insight=False, note='',
    bold=['have responded by', 'moving operations'],
    chunks=[
        dict(role='主语', text='Some western farmers',
             note=''),
        dict(role='谓语', text='have responded',
             note=''),
        dict(role='状语', text='by moving operations to Mexico.',
             note='by + 动名词表方式'),
    ])

A['P7S3'] = dict(
    zh='从1998年到2000年，美国人消费的水果中有14.5%是进口的。',
    insight=False, note='',
    bold=['imported'],
    chunks=[
        dict(role='状语', text='From 1998 to 2000,',
             note=''),
        dict(role='主语', text='14.5 percent of the fruit Americans consumed',
             note=''),
        dict(role='谓语', text='was imported.',
             note='(that) Americans consumed 省略关系词的定语从句；被动语态'),
    ])

A['P7S4'] = dict(
    zh='仅仅十多年后，进口份额达到了25.8%。',
    insight=False, note='',
    bold=['Little more than', 'the share of imports'],
    chunks=[
        dict(role='状语', text='Little more than a decade later,',
             note=''),
        dict(role='主语', text='the share of imports',
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='25.8 percent.',
             note=''),
    ])

A['P8S1'] = dict(
    zh='实际上，美国可以进口食品，或者可以进口采摘食品的工人。',
    insight=False, note='',
    bold=['In effect', 'import the workers'],
    chunks=[
        dict(role='状语', text='In effect,',
             note=''),
        dict(role='主语', text='the U.S.',
             note=''),
        dict(role='谓语', text='can import',
             note=''),
        dict(role='宾语', text='food',
             note=''),
        dict(role='连接词', text='or',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='can import',
             note=''),
        dict(role='宾语', text='the workers who pick it.',
             note='who... 定语从句修饰 workers'),
    ])
