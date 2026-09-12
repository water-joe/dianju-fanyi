# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='生物学家估计，曾有多达200万只小草原松鸡——一种生活在广袤草原上的鸟类——为美国中西部和西南部常常灰暗的景观增添了红色。',
    insight=True, note='主句加that引导宾语从句的结构是四六级和考研阅读中的高频句式，同位语用破折号插入也常见于学术文本；从句内主谓宾加多重修饰的扩展模式具有较强代表性，掌握后可复用到大量类似长句。',
    bold=['estimate', 'lent red to', 'landscape'],
    chunks=[
        dict(role='主语', text='Biologists',
             note=''),
        dict(role='谓语', text='estimate',
             note=''),
        dict(role='宾语从句', text='that as many as 2 million lesser prairie chickens – a kind of bird living on stretching grasslands – once lent red to the often grey landscape of the midwestern and southwestern United States.',
             note='that 引导宾语从句；破折号内为同位语（living on... 现在分词作后置定语）；lend red to 为…增添红色'),
    ])

A['P1S2'] = dict(
    zh='但如今仅剩约22000只鸟，占据该物种历史分布范围的约16%。',
    insight=False, note='',
    bold=['remain today', 'historic range'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语', text='just some 22,000 birds',
             note=''),
        dict(role='谓语', text='remain today,',
             note=''),
        dict(role='状语', text="occupying about 16% of the species' historic range.",
             note='现在分词作伴随状语'),
    ])

A['P2S1'] = dict(
    zh='数量骤减是美国鱼类及野生动物管理局(USFWS)决定正式将该鸟列为受威胁物种的主要原因。',
    insight=False, note='',
    bold=['The crash', 'a major reason'],
    chunks=[
        dict(role='主语', text='The crash',
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='a major reason',
             note=''),
        dict(role='定语从句', text='the U.S.',
             note=''),
    ])

A['P2S2'] = dict(
    zh='（接上句）鱼类及野生动物管理局决定正式将该鸟列为受威胁物种。',
    insight=False, note='',
    bold=['formally list', 'threatened'],
    chunks=[
        dict(role='主语', text='Fish and Wildlife Service (USFWS)',
             note='与上句 The U.S. 合为机构名，被 PDF 分句隔断'),
        dict(role='谓语', text='decided to formally list',
             note=''),
        dict(role='宾语', text='the bird',
             note=''),
        dict(role='宾语补足语', text='as threatened.',
             note='list A as B 把 A 列为 B'),
    ])

A['P2S3'] = dict(
    zh='USFWS局长Daniel Ashe说:"小草原松鸡正处于绝望的境地。"',
    insight=True, note='主系表结构加插入语是考试中常见的句式，however作插入语表转折也是高频考点，具有一定代表性，但因为句子过于简短、无从句，不能代表真题中常见的复杂长难句，典型性中等',
    bold=['desperate situation', 'Director'],
    chunks=[
        dict(role='宾语', text='"The lesser prairie chicken is in a desperate situation,"',
             note='直接引语作 said 的宾语；in a desperate situation 处于绝境'),
        dict(role='谓语', text='said',
             note=''),
        dict(role='主语', text='USFWS Director Daniel Ashe.',
             note='引述分句主语'),
    ])

A['P2S4'] = dict(
    zh='然而，一些环保人士感到失望。',
    insight=False, note='',
    bold=['environmentalists', 'disappointed'],
    chunks=[
        dict(role='主语', text='Some environmentalists,',
             note=''),
        dict(role='插入语', text='however,',
             note=''),
        dict(role='谓语', text='were disappointed.',
             note=''),
    ])

A['P2S5'] = dict(
    zh='他们曾敦促该机构将这种鸟指定为"濒危"物种，这一地位赋予联邦官员更大的监管权力来打击威胁。',
    insight=False, note='',
    bold=['designate', 'crack down on'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='had pushed',
             note=''),
        dict(role='宾语', text='the agency',
             note=''),
        dict(role='宾语补足语', text='to designate the bird as "endangered,"',
             note='push sb. to do 宾补；designate A as B'),
        dict(role='同位语', text='a status that gives federal officials greater regulatory power to crack down on threats.',
             note='a status 为同位语；that... 定语从句修饰 status；crack down on 打击'),
    ])
