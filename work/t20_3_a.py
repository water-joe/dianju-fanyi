# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='去年11月，马德里因推出针对污染最严重车辆的雄心勃勃的限制措施而被誉为公共健康的灯塔。',
    insight=False, note='',
    bold=['hailed as', 'rolled out', 'ambitious restrictions'],
    chunks=[
        dict(role='主语', text='Madrid',
             note=''),
        dict(role='谓语', text='was hailed as a public health beacon',
             note='被动语态 + as 主语补足语'),
        dict(role='状语', text='last November',
             note=''),
        dict(role='状语从句', text='when it rolled out ambitious restrictions on the most polluting cars.',
             note='when 引导时间状语从句；roll out 推出'),
    ])

A['P1S2'] = dict(
    zh='七个月和一个选举日之后，新的保守派市议会暂停了清洁空气区的执法，这是该措施可能终止的第一步。',
    insight=False, note='',
    bold=['suspended', 'demise'],
    chunks=[
        dict(role='状语', text='Seven months and one election day later,',
             note=''),
        dict(role='主语', text='a new conservative city council',
             note=''),
        dict(role='谓语', text='suspended',
             note=''),
        dict(role='宾语', text='enforcement of the clean air zone,',
             note=''),
        dict(role='同位语', text='a first step toward its possible demise.',
             note='对前面整件事的同位补充；demise 终止、消亡'),
    ])

A['P1S3'] = dict(
    zh='尽管该区域在改善空气质量方面取得了成功，市长José Luis Martinez-Almeida仍将反对该区域作为其竞选活动的核心内容。',
    insight=False, note='',
    bold=['centrepiece', 'opposition to'],
    chunks=[
        dict(role='主语', text='Mayor José Luis Martinez-Almeida',
             note=''),
        dict(role='谓语', text='made',
             note=''),
        dict(role='宾语', text='opposition to the zone',
             note=''),
        dict(role='宾语补足语', text='a centrepiece of his election campaign,',
             note='make A B：把 A 作为 B'),
        dict(role='状语', text='despite its success in improving air quality.',
             note='despite 介词短语作让步状语'),
    ])

A['P1S4'] = dict(
    zh='现在，一名法官推翻了该市停止征收罚款的决定，下令恢复罚款。',
    insight=False, note='',
    bold=['overruled', 'levying fines'],
    chunks=[
        dict(role='主语', text='A judge',
             note=''),
        dict(role='谓语', text='has now overruled',
             note=''),
        dict(role='宾语', text="the city's decision to stop levying fines,",
             note='to stop... 不定式作后置定语；levy fines 征收罚款'),
        dict(role='状语', text='ordering them reinstated.',
             note='现在分词作伴随状语；reinstated 过去分词作宾补'),
    ])

A['P1S5'] = dict(
    zh='但随着法律纠纷的到来，该区域的未来充其量看起来并不确定。',
    insight=True, note='主系表结构加介词短语状语是四六级和考研阅读中高频出现的句式。"with+复合结构"作状语、系动词表示状态判断（"looksuncertain"）、程度副词修饰表语（"atbest"）都是典型用法，掌握后可迁移到大量类似句子。虽然本句本身不复杂，但其结构模式具有较强代表性。',
    bold=['at best'],
    chunks=[
        dict(role='状语', text='But with legal battles ahead,',
             note='with 复合结构作伴随状语'),
        dict(role='主语', text="the zone's future",
             note=''),
        dict(role='谓语', text='looks',
             note='系动词，表状态判断'),
        dict(role='表语', text='uncertain at best.',
             note='at best 充其量'),
    ])

A['P2S1'] = dict(
    zh='马德里在清洁空气问题上的反复提醒人们，欧洲各地(英国也深陷其中)针对空气污染所做努力的零散的、逐个城市推进的方式存在局限性。',
    insight=False, note='',
    bold=['pointed reminder', 'patchwork', 'characterises'],
    chunks=[
        dict(role='主语', text="Madrid's back and forth on clean air",
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a pointed reminder of the limits to the patchwork, city- by-city approach',
             note='of/to 多层介词短语作后置定语'),
        dict(role='定语从句', text='that characterises efforts on air pollution across Europe,',
             note='that 引导定语从句修饰 approach'),
        dict(role='状语', text='Britain very much included.',
             note='独立结构作补充说明'),
    ])
