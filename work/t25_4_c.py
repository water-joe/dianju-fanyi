# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S4'] = dict(
    zh='值得注意的是，Broadway是纽约市少数几个违背应用于城市其他地区的网格系统的区域之一，在城市的部分地区斜穿而过。',
    insight=True, note='本句结构在考研和四六级阅读中较为常见：主句+限制性定语从句+分词短语伴随状语的组合，是典型的复杂句模式。句首插入语、不及物动词短语、后置定语等都是常考结构。掌握本句的分析方法可以迁移到大量类似长句，具有较高的典型性和复用价值。',
    bold=['defies', 'grid-based system', 'diagonal'],
    chunks=[
        dict(role='状语', text='Notably,',
             note='评注性状语'),
        dict(role='主语', text='Broadway',
             note=''),
        dict(role='谓语', text='stands out as one of the few areas in NYC',
             note='stand out as 突出为…'),
        dict(role='定语从句', text='that defies the grid-based system applied to the rest of the city,',
             note='that... 定语从句修饰 areas；applied to... 过去分词短语作后置定语'),
        dict(role='状语', text='cutting a diagonal across parts of the city.',
             note='现在分词短语作伴随状语'),
    ])

A['P5S1'] = dict(
    zh='在网络空间中，欲望路径激发了一种可能接近痴迷的迷恋，Reddit页面成为一个中心。',
    insight=True, note='“主句主干+名词后定语从句+句首介词状语+句尾补充结构”是阅读里很常见的组合。掌握这类句子后，处理同类长句的迁移价值很高。',
    bold=['sparked', 'fascination', 'hub'],
    chunks=[
        dict(role='状语', text='In online spaces,',
             note=''),
        dict(role='主语', text='desire paths',
             note=''),
        dict(role='谓语', text='have sparked',
             note=''),
        dict(role='宾语', text='a fascination that can approach obsession,',
             note='that... 定语从句修饰 fascination；approach 接近'),
        dict(role='独立主格', text='with the Reddit page serving as a hub.',
             note='with 复合结构作补充说明'),
    ])

A['P5S2'] = dict(
    zh='贡献者提供了各种各样的故事，从鲜为人知的新捷径到长期存在的替代路线。',
    insight=False, note='',
    bold=['a wide array of', 'little-known', 'alternate routes'],
    chunks=[
        dict(role='主语', text='Contributors',
             note=''),
        dict(role='谓语', text='offer',
             note=''),
        dict(role='宾语', text='a wide array of stories,',
             note=''),
        dict(role='状语', text='from little-known new shortcuts to long-established alternate routes.',
             note='from A to B 介词短语作范围状语'),
    ])

A['P6S1'] = dict(
    zh='动物欲望路径，如鸭子在结冰的池塘上开辟小径或狗在花园中开辟直接路线，突显了这些小径在人类和动物体验中的适应性。',
    insight=False, note='',
    bold=['forging', 'adaptability'],
    chunks=[
        dict(role='主语', text='Animal desire paths, such as ducks forging trails through frozen ponds or dogs carving direct routes in gardens,',
             note='such as... 举例插入；forging/carving 现在分词复合结构'),
        dict(role='谓语', text='highlight',
             note=''),
        dict(role='宾语', text='the adaptability of these trails in both human and animal experiences.',
             note='in both... 并列介词短语'),
    ])

A['P6S2'] = dict(
    zh='随着欲望路径在物理和虚拟景观中纵横交错，它们证明了集体坚持开辟非常规路线和拥抱共同选择精神的决心。',
    insight=True, note='"状语从句前置+主句"是四六级和考研阅读中的高频句式，"As"引导的状语从句尤其常见。主句中介词短语作状语修饰动词的结构也是典型搭配。学习者掌握本句结构后可迁移至大量类似长句。',
    bold=['criss-cross', 'unconventional routes', 'communal choice'],
    chunks=[
        dict(role='状语从句', text='As desire paths criss-cross through both physical and virtual landscapes,',
             note='as 引导时间状语从句；criss-cross 纵横交错'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='stand as a proof of the collective insistence on forging unconventional routes and embracing the spirit of communal choice.',
             note='stand as 作为…而存在；on 的宾语为两个并列动名词'),
    ])
