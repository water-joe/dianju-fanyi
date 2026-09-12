# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S6'] = dict(
    zh='"我个人从未认为记忆事物有多大的智力价值，"Sparrow说，并补充说我们并未失去记忆的能力。',
    insight=True, note='直接引语加引述动词是四六级和考研阅读中常见的句式，用于引述观点或研究结果。伴随状语adding补充信息也是学术文本的典型结构。现在完成时否定句在真题中频繁出现。整体结构具有较高的代表性和可迁移性。',
    bold=['intellectual value', 'adding that'],
    chunks=[
        dict(role='宾语', text='"I personally have never seen all that much intellectual value in memorizing things,"',
             note='直接引语作 says 的宾语；have never seen 现在完成时否定'),
        dict(role='主语', text='Sparrow',
             note=''),
        dict(role='谓语', text='says,',
             note=''),
        dict(role='状语', text="adding that we haven't lost our ability to do it.",
             note='现在分词作伴随状语；adding that 后接宾语从句'),
    ])

A['P3S1'] = dict(
    zh='还有其他专家表示，现在就理解互联网如何影响我们的大脑还为时过早。',
    insight=True, note='双层宾语从句嵌套、形式主语it配合不定式、too...to结构均为四六级和考研阅读中的高频句式,本句同时呈现这些典型结构,学习迁移价值高',
    bold=['too soon to'],
    chunks=[
        dict(role='主语', text='Still other experts',
             note=''),
        dict(role='谓语', text='say',
             note=''),
        dict(role='宾语从句', text="it's too soon to understand how the Internet affects our brains.",
             note='省略 that 的宾语从句；it 形式主语；too... to 结构；how 引导宾语从句'),
    ])

A['P3S2'] = dict(
    zh='心理学家Christopher Chabris和Daniel J. Simons写道，例如，没有实验证据表明互联网会干扰我们的专注能力。',
    insight=True, note='句中涵盖倒装结构的主谓宾识别、therebe句型、现在分词短语作后置定语、宾语从句、插入语等多种成分,且倒装和嵌套制造了典型易错点,作为划分成分的练习句收益高',
    bold=['experimental evidence', 'interferes with'],
    chunks=[
        dict(role='谓语', text='There is',
             note=''),
        dict(role='主语', text='no experimental evidence showing',
             note=''),
        dict(role='宾语从句', text='that it interferes with our ability to focus,',
             note='showing 现在分词后接 that 宾语从句'),
        dict(role='插入语', text='for instance,',
             note=''),
        dict(role='谓语', text='wrote',
             note='引述动词（前置倒装）'),
        dict(role='主语', text='psychologists Christopher Chabris and Daniel J.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='Simons。（接上句：Daniel J. Simons）',
    insight=False, note='',
    bold=['Simons'],
    chunks=[
        dict(role='主语', text='Simons.',
             note='上句 Daniel J. 的姓氏，被引文与 PDF 分句隔断'),
    ])

A['P3S4'] = dict(
    zh='而且在2008年一项涉及University of California, Los Angeles的Semel Institute for Neuroscience and Human Behavior的24名参与者的研究中，浏览网页比阅读更能锻炼大脑。',
    insight=False, note='',
    bold=['surfing the web', 'computer-savvy'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='surfing the web',
             note=''),
        dict(role='谓语', text='exercised the brain more than reading did',
             note='more than reading did 比较结构，did 代 exercised'),
        dict(role='状语', text='among computer-savvy older adults',
             note=''),
        dict(role='状语', text='in a 2008 study involving 24 participants at the Semel Institute for Neuroscience and Human Behavior at the University of California, Los Angeles.',
             note='involving... 现在分词作后置定语'),
    ])
