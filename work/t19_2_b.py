# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='这暂时降低了碳承载能力。',
    insight=False, note='',
    bold=['temporarily', 'carbon-carrying capacity'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='状语', text='temporarily',
             note=''),
        dict(role='谓语', text='lowers',
             note=''),
        dict(role='宾语', text='carbon-carrying capacity.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='但剩余的树木获得了更多可用水分，因此它们生长并茁壮成长，恢复了森林从空气中吸收碳的能力。',
    insight=True, note='因果关系的并列句是考试常见句式,"so"连接主句的结构具有一定典型性,且现在分词作结果状语也是常考点,但整体结构相对简单,不如含有从句的复杂句更具代表性。',
    bold=['moisture', 'restoring'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='the remaining trees',
             note=''),
        dict(role='谓语', text='draw',
             note=''),
        dict(role='宾语', text='a greater share of the available moisture,',
             note=''),
        dict(role='状语从句', text='so they grow and thrive,',
             note='so 引导结果状语从句；并列谓语 grow... and thrive'),
        dict(role='状语', text="restoring the forest's capacity to pull carbon from the air.",
             note='现在分词作结果状语；to pull... 不定式作后置定语'),
    ])

A['P3S4'] = dict(
    zh='健康的树木也更能抵御昆虫侵害。',
    insight=False, note='',
    bold=['fend off'],
    chunks=[
        dict(role='主语', text='Healthy trees',
             note=''),
        dict(role='谓语', text='are also better able to fend off insects.',
             note='be able to do；fend off 抵御'),
    ])

A['P3S5'] = dict(
    zh='地貌变得不那么容易燃烧。',
    insight=False, note='',
    bold=['rendered', 'burnable'],
    chunks=[
        dict(role='主语', text='The landscape',
             note=''),
        dict(role='谓语', text='is rendered',
             note=''),
        dict(role='宾语', text='less easily burnable.',
             note='被动语态；render 使成为'),
    ])

A['P3S6'] = dict(
    zh='即使发生火灾，被烧毁的树木也更少。',
    insight=True, note='被动语态和介词短语作状语是四六级和考研中的高频句式，结构简单但实用性强，学习者掌握后可迁移到大量类似句子，具有一定典型性。',
    bold=['in the event of'],
    chunks=[
        dict(role='状语', text='Even in the event of a fire,',
             note='in the event of 万一发生…'),
        dict(role='主语', text='fewer trees',
             note=''),
        dict(role='谓语', text='are consumed.',
             note='被动语态；consume 烧毁'),
    ])

A['P4S1'] = dict(
    zh='这种规划的必要性日益紧迫。',
    insight=False, note='',
    bold=['increasingly urgent'],
    chunks=[
        dict(role='主语', text='The need for such planning',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='increasingly urgent.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='自2010年以来，干旱和昆虫已在California造成超过1亿棵树木死亡，其中大部分仅在2016年，而野火已烧毁数十万英亩土地。',
    insight=False, note='',
    bold=['drought', 'acres'],
    chunks=[
        dict(role='状语', text='Already, since 2010,',
             note=''),
        dict(role='主语', text='drought and insects',
             note=''),
        dict(role='谓语', text='have killed',
             note=''),
        dict(role='宾语', text='over 100 million trees in California, most of them in 2016 alone,',
             note='most of them in 2016 alone 为独立主格/补充说明'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='wildfires',
             note=''),
        dict(role='谓语', text='have burned',
             note=''),
        dict(role='宾语', text='hundreds of thousands of acres.',
             note=''),
    ])
