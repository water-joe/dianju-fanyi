# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S3'] = dict(
    zh='"几十年来，我们没有承担起投资国内木材供应的责任，这使我们面临价格波动的风险，并在全球需求上升而我们自身供应下降之际争夺未来的木材供应。"',
    insight=False, note='',
    bold=['For decades', 'taken responsibility for', 'fluctuating prices'],
    chunks=[
        dict(role='状语', text='"For decades',
             note='时间状语（直接引语）'),
        dict(role='谓语', text='we have not taken responsibility for investing in our domestic wood supply,',
             note='take responsibility for 为…负责；investing... 动名词作介词宾语'),
        dict(role='状语', text='leaving us exposed to fluctuating prices and fighting for future supplies of wood as global demand rises and our own supplies fall."',
             note='现在分词短语作结果状语；leaving us exposed to... 宾补结构；as 引导时间状语从句'),
    ])

A['P3S1'] = dict(
    zh='Confor表示，英国拥有种植木材以建造低碳住宅的理想条件，并且在认证其森林可持续管理方面处于全球领先地位。',
    insight=False, note='',
    bold=['ideal conditions', 'low-carbon homes', 'sustainably managed'],
    chunks=[
        dict(role='主语', text='The UK',
             note='宾语从句主语（Confor says 后置）'),
        dict(role='谓语', text='has ideal conditions for growing wood to build low-carbon homes',
             note='to build... 不定式作目的状语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='is a global leader in certifying that its forests are sustainably managed,',
             note='certifying 动名词作介词宾语；that 引导宾语从句'),
        dict(role='主语', text='Confor',
             note='引述分句主语（后置）'),
        dict(role='谓语', text='says.',
             note='引述动词'),
    ])

A['P3S2'] = dict(
    zh='虽然约四分之三的苏格兰住宅使用苏格兰木材建造，但英格兰使用国产木材的比例仅约25%。',
    insight=False, note='',
    bold=['three quarters', 'built from', 'home-grown wood'],
    chunks=[
        dict(role='状语从句', text='While around three quarters of Scottish homes are built from Scottish timber,',
             note='while 引导让步/对比状语从句；are built from 被动语态'),
        dict(role='主语', text='the use of home-grown wood in England',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='only around 25 percent.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='英国当前处境的原因是复杂的，既包括对生产性林业的过时认知，也包括灰松鼠对树木的大量破坏。',
    insight=False, note='',
    bold=['complex', 'range from', 'outdated perceptions'],
    chunks=[
        dict(role='主语', text="The causes of the UK's current position",
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='complex',
             note=''),
        dict(role='状语', text='and range from outdated perceptions of productive forestry to the decimation of trees by grey squirrels.',
             note='range from... to... 从…到…不等'),
    ])

A['P3S4'] = dict(
    zh='这还涉及农民和其他土地所有者对投资长期种植项目的明显犹豫。',
    insight=True, note='本句的结构（主谓宾+介词短语后置定语+不定式后置定语）是四六级和考研阅读中的高频句式，尤其是不定式作后置定语修饰抽象名词（如hesitationtodo）是常考点。掌握后可大量复用到类似句子的分析中。',
    bold=['encompasses', 'significant hesitation', 'on behalf of'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='also encompasses',
             note=''),
        dict(role='宾语', text='significant hesitation on behalf of farmers and other landowners to invest in longer-term planting projects.',
             note='on behalf of... 介词短语作后置定语；to invest... 不定式作 hesitation 的后置定语'),
    ])
