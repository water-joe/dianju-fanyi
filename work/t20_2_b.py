# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='CEO必须对金融市场有良好的认识，甚至可能还要了解公司应该如何在这些市场中进行交易。',
    insight=False, note='',
    bold=['a good sense of', 'trade in'],
    chunks=[
        dict(role='主语', text='CEOs',
             note=''),
        dict(role='谓语', text='must have',
             note=''),
        dict(role='宾语', text='a good sense of financial markets and maybe even how the company should trade in them.',
             note='how... 疑问词引导宾语从句作 of 的并列宾语'),
    ])

A['P3S3'] = dict(
    zh='他们还需要比前任更好的公关技能，因为即使是小失误的代价也可能很大。',
    insight=True, note='主句+原因状语从句的结构在四六级和考研阅读中较为常见，比较结构"better...than"也是高频考点，情态动词表推测是基础语法点。虽然这个句子本身不算特别复杂，但它展现的"主句陈述+as引导原因"这一模式具有较高的复用价值',
    bold=['public relations', 'slipup'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='need better public relations skills than their predecessors,',
             note='better... than... 比较结构'),
        dict(role='状语从句', text='as the costs of even a minor slipup can be significant.',
             note='as 引导原因状语从句'),
    ])

A['P3S4'] = dict(
    zh='此外，美国大公司比以往任何时候都更加全球化，供应链遍布更多国家。',
    insight=False, note='',
    bold=['globalized', 'supply chains'],
    chunks=[
        dict(role='谓语', text="Then there's the fact",
             note=''),
        dict(role='同位语从句', text='that large American companies are much more globalized than ever before,',
             note='that 引导同位语从句说明 fact'),
        dict(role='状语', text='with supply chains spread across a larger number of countries.',
             note='with 复合结构作伴随状语'),
    ])

A['P3S5'] = dict(
    zh='在这样的体系中领导需要相当惊人的知识储备。',
    insight=False, note='',
    bold=['mind-boggling'],
    chunks=[
        dict(role='主语', text='To lead in that system',
             note='不定式短语作主语'),
        dict(role='谓语', text='requires',
             note=''),
        dict(role='宾语', text='knowledge that is fairly mind-boggling.',
             note='that... 定语从句修饰 knowledge'),
    ])

A['P3S6'] = dict(
    zh='而且，几乎所有美国大公司都在以这样或那样的方式成为科技公司。',
    insight=True, note='主系表结构配合现在进行时是考试中常见的基础句型，"bebecoming"表达趋势变化的用法在四六级阅读和写作中频繁出现；句首副词"Plus"和句末状语"onewayoranother"的搭配也具有一定代表性，掌握后可迁移到类似表达中。',
    bold=['virtually', 'one way or another'],
    chunks=[
        dict(role='状语', text='Plus,',
             note=''),
        dict(role='主语', text='virtually all major American companies',
             note=''),
        dict(role='谓语', text='are becoming',
             note=''),
        dict(role='表语', text='tech companies,',
             note=''),
        dict(role='状语', text='one way or another.',
             note='以这样或那样的方式'),
    ])

A['P3S7'] = dict(
    zh='除此之外，大公司CEO仍然必须完成他们一直以来要做的所有日常工作。',
    insight=True, note='主句加限制性定语从句修饰宾语是四六级和考研阅读中的高频句式。定语从句省略关系代词的现象在真题中非常常见，学生掌握这种结构后可以大量复用到其他句子的理解中。句子结构简洁但典型，代表性强。',
    bold=['Beyond this', 'day-to-day work'],
    chunks=[
        dict(role='状语', text='Beyond this,',
             note=''),
        dict(role='主语', text='major CEOs',
             note=''),
        dict(role='状语', text='still',
             note=''),
        dict(role='谓语', text='have to do',
             note=''),
        dict(role='宾语', text='all the day-to-day work they have always done.',
             note='(that) they have always done 省略关系词的定语从句'),
    ])
