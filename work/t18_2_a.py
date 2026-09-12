# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='尽管化石燃料——煤炭、石油、天然气——仍然产生世界能源供应的大约85%，但可再生能源如风能和太阳能属于未来这一点比以往任何时候都更加清晰。',
    insight=False, note='',
    bold=['fossil fuels', 'generate', 'belongs to'],
    chunks=[
        dict(role='状语从句', text="While fossil fuels – coal, oil, gas – still generate roughly 85 percent of the world's energy supply,",
             note='while 引导让步状语从句；破折号内为同位语'),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text="'s clearer than ever",
             note=''),
        dict(role='主语从句', text='that the future belongs to renewable sources such as wind and solar.',
             note='that 引导主语从句；belong to 属于'),
    ])

A['P1S2'] = dict(
    zh='全球向可再生能源转变的势头正在加快:它们现在占新上线电力来源的一半以上。',
    insight=True, note='冒号连接两个主句进行补充说明是英文写作中的常见手法,现在进行时表示趋势、一般现在时陈述事实的搭配也符合四六级和考研阅读的典型语言风格。后置定语修饰名词的结构在真题中频繁出现,具有一定的代表性和复用价值。',
    bold=['picking up momentum', 'account for'],
    chunks=[
        dict(role='主语', text='The move to renewables',
             note=''),
        dict(role='谓语', text='is picking up momentum',
             note='现在进行时；pick up momentum 势头增强'),
        dict(role='状语', text='around the world:',
             note=''),
        dict(role='主语', text='They',
             note=''),
        dict(role='状语', text='now',
             note=''),
        dict(role='谓语', text='account for more than half of new power sources going on line.',
             note='account for 占；going on line 现在分词作后置定语'),
    ])

A['P2S1'] = dict(
    zh='部分增长源于政府和有远见的企业对清洁能源的资助承诺。',
    insight=True, note='主语+不及物动词+介词短语状语+后置定语修饰状语中的名词，这是四六级和考研阅读中高频出现的句式；尤其是commitmenttodo和commitmentbysb两种后置定语并存的结构，在长难句中非常典型，掌握后可大量迁移到其他类似句子。',
    bold=['stems from', 'farsighted'],
    chunks=[
        dict(role='主语', text='Some growth',
             note=''),
        dict(role='谓语', text='stems from',
             note=''),
        dict(role='宾语', text='a commitment by governments and farsighted businesses to fund cleaner energy sources.',
             note='by... 与 to fund... 均为 commitment 的后置定语；farsighted 有远见的'),
    ])

A['P2S2'] = dict(
    zh='但这个故事越来越多地与可再生能源价格的暴跌有关，尤其是风能和太阳能。',
    insight=True, note='主系表结构是常见句式，表语为介词短语也较典型，但整体过于简单，缺少从句、并列或特殊结构，作为四六级/考研真题句式的代表性一般。',
    bold=['plummeting prices'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语', text='increasingly',
             note=''),
        dict(role='主语', text='the story',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='about the plummeting prices of renewables, especially wind and solar.',
             note='plummeting 暴跌的（现在分词作定语）'),
    ])

A['P2S3'] = dict(
    zh='在过去八年中，太阳能电池板的成本下降了80%，风力涡轮机的成本下降了近三分之一。',
    insight=False, note='',
    bold=['solar panels', 'wind turbines'],
    chunks=[
        dict(role='主语', text='The cost of solar panels',
             note=''),
        dict(role='谓语', text='has dropped by 80 percent',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='the cost of wind turbines',
             note=''),
        dict(role='谓语', text='by close to one-third',
             note=''),
        dict(role='状语', text='in the past eight years.',
             note='and 后省略 has dropped'),
    ])

A['P3S1'] = dict(
    zh='在世界许多地区，可再生能源已经是主要能源来源。',
    insight=False, note='',
    bold=['a principal energy source'],
    chunks=[
        dict(role='状语', text='In many parts of the world',
             note=''),
        dict(role='主语', text='renewable energy',
             note=''),
        dict(role='谓语', text='is already',
             note=''),
        dict(role='表语', text='a principal energy source.',
             note=''),
    ])

A['P3S2'] = dict(
    zh='例如在苏格兰，风力涡轮机提供的电力足以为95%的家庭供电。',
    insight=True, note='覆盖主谓宾加地点状语、插入语、目的状语，成分种类较丰富；但结构简单直接，缺少易错点（如形式主语、双宾语、宾补等），练习收益中等偏下。',
    bold=['wind turbines', 'power 95 percent'],
    chunks=[
        dict(role='状语', text='In Scotland,',
             note=''),
        dict(role='插入语', text='for example,',
             note=''),
        dict(role='主语', text='wind turbines',
             note=''),
        dict(role='谓语', text='provide',
             note=''),
        dict(role='宾语', text='enough electricity',
             note=''),
        dict(role='状语', text='to power 95 percent of homes.',
             note='不定式作目的状语'),
    ])
