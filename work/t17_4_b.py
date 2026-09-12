# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S3'] = dict(
    zh='比如，"等一下，这样可以吗？"',
    insight=False, note='',
    bold=['is this OK'],
    chunks=[
        dict(role='插入语', text='Like,',
             note=''),
        dict(role='主语', text="'Wait a minute,",
             note=''),
        dict(role='表语', text="is this OK?'",
             note='口语化的短句'),
    ])

A['P4S4'] = dict(
    zh='我们是否应该将这些资金重新引导，集中用于地形中危险性较低的部分？"',
    insight=False, note='',
    bold=['redirect', 'lower-hazard'],
    chunks=[
        dict(role='谓语', text='Do',
             note=''),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='want',
             note=''),
        dict(role='状语', text='instead',
             note=''),
        dict(role='宾语', text='to redirect those funds to concentrate on lower-hazard parts of the landscape?"',
             note='两个并列不定式作 want 的宾语'),
    ])

A['P5S1'] = dict(
    zh='研究人员表示，这种观点需要美国社会对火灾的看法发生相应的转变。',
    insight=True, note='主句包含情态动词加及物动词,宾语中嵌入限制性定语从句且关系副词省略,这是四六级和考研阅读中的高频句式。该结构在学术写作和新闻报道中常见,掌握后可迁移到大量类似句子。',
    bold=['corresponding shift', 'views fire'],
    chunks=[
        dict(role='主语', text='Such a view',
             note=''),
        dict(role='谓语', text='would require',
             note=''),
        dict(role='宾语', text='a corresponding shift in the way US society today views fire,',
             note='(in which) US society views fire 省略关系词的定语从句修饰 way'),
        dict(role='主语', text='researchers',
             note=''),
        dict(role='谓语', text='say.',
             note=''),
    ])

A['P6S1'] = dict(
    zh='首先，关于野火的讨论需要更具包容性。',
    insight=True, note='"主语+needtobe+形容词"是四六级和考研阅读中的常见句式，具有一定代表性；句首状语"Foronething"也是议论文常用的列举标记；但整体结构过于基础，缺少复杂句式特征',
    bold=['more inclusive'],
    chunks=[
        dict(role='状语', text='For one thing,',
             note='列举状语，引出第一条'),
        dict(role='主语', text='conversations about wildfires',
             note=''),
        dict(role='谓语', text='need to be',
             note=''),
        dict(role='表语', text='more inclusive.',
             note=''),
    ])

A['P6S2'] = dict(
    zh='过去十年，焦点一直集中在气候变化上，即温室气体导致的地球变暖如何造成恶化火灾的条件。',
    insight=True, note='主句包含时间状语、主系表结构、同位语从句（破折号引出）；how从句内有主语（动名词短语）、谓语（现在进行时）、宾语、后置定语（介词短语fromgreenhousegases）；定语从句涉及关系代词作主语、及物动词作谓语、名词作宾语；成分种类丰富，且破折号的同位语用法、动名词短语作主语、关系代词双重作用等都是易错点，训练价值较高。',
    bold=['the focus has been on', 'greenhouse gases', 'worsen'],
    chunks=[
        dict(role='状语', text='Over the past decade,',
             note=''),
        dict(role='主语', text='the focus',
             note=''),
        dict(role='谓语', text='has been on',
             note=''),
        dict(role='宾语', text='climate change –',
             note=''),
        dict(role='同位语从句', text='how the warming of the Earth from greenhouse gases is leading to conditions that worsen fires.',
             note='how 引导同位语从句说明 climate change；that... 定语从句修饰 conditions'),
    ])

A['P7S1'] = dict(
    zh='Moritz表示，虽然气候是一个关键因素，但不应以牺牲等式中的其他部分为代价。',
    insight=True, note='该句型非常典型：让步状语从句+主句引述+宾语从句的组合是学术文章和考试阅读中的高频结构。学会分析此类句子可直接迁移到大量真题中，具有很强的代表性和复用价值。',
    bold=['at the expense of', 'equation'],
    chunks=[
        dict(role='状语从句', text='While climate is a key element,',
             note='while 引导让步状语从句'),
        dict(role='插入语', text='Moritz says,',
             note='引述插入语'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text="shouldn't come",
             note=''),
        dict(role='状语', text='at the expense of the rest of the equation.',
             note='at the expense of 以…为代价'),
    ])

A['P8S1'] = dict(
    zh='他说:"人类系统和我们生活的地貌是相互关联的，这种相互作用是双向的。"',
    insight=False, note='',
    bold=['go both ways'],
    chunks=[
        dict(role='主语', text='"The human systems and the landscapes we live on',
             note=''),
        dict(role='谓语', text='are linked,',
             note='(that) we live on 省略关系词的定语从句'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='the interactions',
             note=''),
        dict(role='谓语', text='go both ways,"',
             note='go both ways 双向互动'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])
