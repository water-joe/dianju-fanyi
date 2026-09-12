# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='2023年，芝加哥失去了最受欢迎的街头节日之一。',
    insight=False, note='',
    bold=['beloved', 'street festivals'],
    chunks=[
        dict(role='状语', text='In 2023,',
             note=''),
        dict(role='主语', text='Chicago',
             note=''),
        dict(role='谓语', text='lost',
             note=''),
        dict(role='宾语', text='one of its most beloved street festivals.',
             note=''),
    ])

A['P1S2'] = dict(
    zh='由Hyde Park社区领袖Eric Williams举办的Silver Room街区派对宣布不会在2024年回归。',
    insight=False, note='',
    bold=['community leader'],
    chunks=[
        dict(role='主语', text='The Silver Room Block Party, staged by Hyde Park community leader Eric Williams,',
             note='staged by... 过去分词短语作后置定语'),
        dict(role='谓语', text='announced',
             note=''),
        dict(role='宾语从句', text='it would not return in 2024.',
             note='省略 that 的宾语从句'),
    ])

A['P1S3'] = dict(
    zh='这个节日最初只是一个小型社区聚会，后来发展成为一项大规模文化活动，在近二十年间每年迎接数万人，然后突然停办。',
    insight=True, note='What引导的主语从句是四六级和考研阅读中的高频句式，尤其是What在从句中充当主语成分这一用法，在学术文章和新闻报道中非常常见。本句的结构（What从句+主句谓语+分词短语作状语）代表了一种典型的复杂句模式，掌握后可以迁移到大量类似句子的理解中。唯一不够极致典型的是blossominto这一搭配不如become、turninto等常见。',
    bold=['blossomed into', 'abruptly shutting down'],
    chunks=[
        dict(role='主语', text='What began as a small neighborhood gathering',
             note='what 引导主语从句（what 在从句中作主语）'),
        dict(role='谓语', text='blossomed into',
             note=''),
        dict(role='宾语', text='a massive cultural event,',
             note=''),
        dict(role='状语', text='welcoming tens of thousands of people each year over nearly two decades before abruptly shutting down.',
             note='现在分词短语作伴随状语；before abruptly shutting down 介词+动名词作时间'),
    ])

A['P2S1'] = dict(
    zh='Williams指出，不断上涨的制作成本和不断下降的参与者捐款是Silver Room街区派对无法继续举办的主要原因，这凸显了所有街头节日组织者目前面临的现实。',
    insight=False, note='',
    bold=['pointed to', 'declining attendee donations', 'highlighting'],
    chunks=[
        dict(role='主语', text='Williams',
             note=''),
        dict(role='谓语', text='pointed to',
             note=''),
        dict(role='宾语', text='rising production costs and declining attendee donations as primary reasons the Silver Room Block Party could not continue,',
             note='point to A as B 指出 A 是 B；(that) the Silver Room... could not continue 省略关系词的定语从句修饰 reasons'),
        dict(role='状语', text='highlighting a reality that all street festival organizers face right now.',
             note='现在分词作补充说明；that... 定语从句修饰 reality'),
    ])

A['P2S2'] = dict(
    zh='在芝加哥举办街头节日的成本已经飙升。',
    insight=False, note='',
    bold=['skyrocketed'],
    chunks=[
        dict(role='主语', text='The cost of producing a street festival in Chicago',
             note=''),
        dict(role='谓语', text='has skyrocketed.',
             note='现在完成时；skyrocket 飞涨'),
    ])

A['P2S3'] = dict(
    zh='安保、娱乐、便携式卫生间、保险甚至围栏和人员配备等基本费用都变得显著昂贵。',
    insight=False, note='',
    bold=['portable restrooms', 'staffing'],
    chunks=[
        dict(role='主语', text='Security, entertainment, portable restrooms, insurance and even basics such as fencing and staffing',
             note='多个并列名词；such as... 举例'),
        dict(role='谓语', text='have all become',
             note=''),
        dict(role='表语', text='significantly more expensive.',
             note='现在完成时系表'),
    ])
