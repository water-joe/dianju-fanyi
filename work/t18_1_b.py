# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S2'] = dict(
    zh='用双手工作几乎被视为低人一等的标志。',
    insight=False, note='',
    bold=['inferiority'],
    chunks=[
        dict(role='主语', text='Working with your hands',
             note=''),
        dict(role='谓语', text='is seen as',
             note=''),
        dict(role='宾语', text='almost a mark of inferiority.',
             note='be seen as 被视为；inferiority 低人一等'),
    ])

A['P4S3'] = dict(
    zh='他说，职业教育体系中的学校"有那种刻板印象……认为那是给学业上不行的孩子准备的"。',
    insight=False, note='',
    bold=['vocational education', 'stereotype', 'academically'],
    chunks=[
        dict(role='主语', text='Schools in the family of vocational education',
             note=''),
        dict(role='谓语', text='"have that stereotype…',
             note=''),
        dict(role='定语从句', text='that it\'s for kids who can\'t make it academically,"',
             note='that 从句说明 stereotype 内容；who... 定语从句修饰 kids'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P5S1'] = dict(
    zh='一方面，这种观点是美国演变的逻辑产物。',
    insight=False, note='',
    bold=['logical product'],
    chunks=[
        dict(role='状语', text='On one hand,',
             note=''),
        dict(role='主语', text='that viewpoint',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text="a logical product of America's evolution.",
             note=''),
    ])

A['P5S2'] = dict(
    zh='制造业不再是曾经的经济引擎。',
    insight=False, note='',
    bold=['economic engine'],
    chunks=[
        dict(role='主语', text='Manufacturing',
             note=''),
        dict(role='谓语', text='is not',
             note=''),
        dict(role='表语', text='the economic engine that it once was.',
             note='that 引导定语从句（was 后省略 the economic engine）'),
    ])

A['P5S3'] = dict(
    zh='美国经济曾经为高中毕业生提供的工作保障已在很大程度上消失了。',
    insight=False, note='',
    bold=['job security', 'evaporated'],
    chunks=[
        dict(role='主语', text='The job security that the US economy once offered to high school graduates',
             note=''),
        dict(role='谓语', text='has largely evaporated.',
             note='现在完成时；evaporate 消失'),
    ])

A['P5S4'] = dict(
    zh='接受更多教育成为新的原则。',
    insight=False, note='',
    bold=['More education'],
    chunks=[
        dict(role='主语', text='More education',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='the new principle.',
             note=''),
    ])

A['P5S5'] = dict(
    zh='我们为孩子们想要更多，这理所应当。',
    insight=False, note='',
    bold=['rightfully so'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text='want',
             note=''),
        dict(role='宾语', text='more for our kids,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='状语', text='rightfully so.',
             note='理所应当'),
    ])

A['P6S1'] = dict(
    zh='但不顾一切地推动所有人获得学士学位——以及对任何更低学历的微妙贬低——忽略了重要的一点:这并非美国经济需要的唯一东西。',
    insight=True, note='主句带同位语从句、同位语从句内嵌套定语从句的结构是四六级和考研阅读中的高频句式。破折号分隔并列主语、冒号引出同位语、省略关系代词的定语从句都是真题常见手法，掌握后可大量复用到同类长难句分析。',
    bold=['headlong push', 'devaluing', 'misses an important point'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text="the headlong push into bachelor's degrees for all – and the subtle devaluing of anything less –",
             note='两个并列名词短语作主语；破折号分隔'),
        dict(role='谓语', text='misses an important point:',
             note=''),
        dict(role='同位语从句', text="That's not the only thing the American economy needs.",
             note='冒号引出同位语从句；(that) the American economy needs 省略关系词的定语从句'),
    ])
