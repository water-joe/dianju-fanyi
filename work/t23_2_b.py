# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S1'] = dict(
    zh='真正的问题是公园长期以来一直资金匮乏。',
    insight=False, note='',
    bold=['chronically starved of'],
    chunks=[
        dict(role='主语', text='The real problem',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语从句', text='that the parks have been chronically starved of funding.',
             note='that 引导表语从句；现在完成时；be starved of 缺乏'),
    ])

A['P5S2'] = dict(
    zh='一项针对700名美国纳税人的经济调查发现，人们愿意支付大量金钱以确保公园及其项目保持完整。',
    insight=True, note='宾语从句嵌套、情态动词表达意愿、不定式作目的状语、被动语态，这些都是四六级和考研阅读中的高频句式。尤其是"foundthat..."引导宾语从句以及"tomakesure(that)..."的目的表达，在真题中反复出现，学习者掌握后可大量复用。',
    bold=['taxpayers', 'kept intact'],
    chunks=[
        dict(role='主语', text='An economic survey of 700 U.S. taxpayers',
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语从句', text='that people would be willing to pay a significant amount of money to make sure the parks and their programs are kept intact.',
             note='that 引导宾语从句；be willing to do；to make sure... 不定式作目的状语；be kept intact 保持完整'),
    ])

A['P5S3'] = dict(
    zh='约81%的受访者表示，他们愿意在未来10年缴纳额外税款，以避免国家公园遭受任何削减。',
    insight=True, note='本句体现了考试中高频出现的"主句+宾语从句"结构，且宾语从句省略引导词that的用法也是真题常见模式。从句内的系表结构、时间状语和目的状语组合，符合真题中描述意愿或计划类句子的典型特征。整体句式在四六级和考研阅读中具有较高代表性，掌握后可迁移到大量类似长句的分析中。',
    bold=['respondents', 'additional taxes'],
    chunks=[
        dict(role='主语', text='Some 81% of respondents',
             note=''),
        dict(role='谓语', text='said',
             note=''),
        dict(role='宾语从句', text='they would be willing to pay additional taxes for the next 10 years to avoid any cuts to the national parks.',
             note='省略 that 的宾语从句；be willing to do；to avoid... 不定式作目的状语'),
    ])

A['P6S1'] = dict(
    zh='国家公园作为逃离之地和自然象征，为美国居民提供了巨大价值。',
    insight=True, note='涵盖主谓宾基本成分，外加两个状语（对象状语和方式状语）和一个后置定语，成分种类较丰富；方式状语采用both...and并列结构，有一定练习价值，但整体无明显易错点',
    bold=['U.S. residents', 'symbols of nature'],
    chunks=[
        dict(role='主语', text='The national parks',
             note=''),
        dict(role='谓语', text='provide',
             note=''),
        dict(role='宾语', text='great value',
             note=''),
        dict(role='状语', text='to U.S. residents',
             note=''),
        dict(role='状语', text='both as places to escape and as symbols of nature.',
             note='both... and... 并列方式状语'),
    ])

A['P6S2'] = dict(
    zh='除此之外，它们还通过广泛的教育项目、通过碳封存对气候产生的积极影响、对我们文化和艺术生活的贡献，当然还有旅游业，创造价值。',
    insight=True, note='"主谓宾+介词短语引导的并列状语"是四六级和考研阅读中的高频句式，尤其from引导的来源状语和并列列举在说明文、议论文中极为常见，掌握后可直接迁移至大量真题句型。',
    bold=['carbon sequestration', 'contribution to'],
    chunks=[
        dict(role='状语', text='On top of this,',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='produce',
             note=''),
        dict(role='宾语', text='value',
             note=''),
        dict(role='状语', text='from their extensive educational programs, their positive impact on the climate through carbon sequestration, their contribution to our cultural and artistic life, and of course through tourism.',
             note='from 后接四个并列名词短语作来源状语'),
    ])

A['P6S3'] = dict(
    zh='这些公园还帮助保持美国历史的鲜活，与全国数千个地方司法管辖区合作保护历史遗址，并让这些地方的故事生动起来。',
    insight=False, note='',
    bold=['jurisdictions', 'to life'],
    chunks=[
        dict(role='主语', text='The parks',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text="help keep America's past alive,",
             note='help do 帮助做；keep... alive 使…保持鲜活'),
        dict(role='状语', text='working with thousands of local jurisdictions around the country to protect historical sites and to bring the stories of these places to life.',
             note='现在分词作伴随状语；两个并列不定式作目的'),
    ])
