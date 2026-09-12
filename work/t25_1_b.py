# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='而新的小费技术甚至可能自动添加小费。',
    insight=False, note='',
    bold=['automatically add tips'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='new tipping technology',
             note=''),
        dict(role='谓语', text='may even automatically add tips.',
             note='even 插在情态动词后'),
    ])

A['P4S1'] = dict(
    zh='数字支付设备的普及使向顾客索要小费变得更加容易。',
    insight=True, note='makeit+形容词+todo结构在四六级和考研阅读中频繁出现，且本句将该结构置于现在完成时中，兼具时态和句型的典型性，掌握后可迁移到大量类似表达',
    bold=['prevalence', 'made it easier'],
    chunks=[
        dict(role='主语', text='The prevalence of digital payment devices',
             note=''),
        dict(role='谓语', text='has made it easier to ask customers for a tip.',
             note='make it + adj. + to do 结构：it 形式宾语，to ask... 真正宾语'),
    ])

A['P4S2'] = dict(
    zh='这有助于解释为什么小费要求正在渗透到新的服务类型中。',
    insight=False, note='',
    bold=['creeping into'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text='helps explain why tip requests are creeping into new kinds of services.',
             note='help (to) do；why 引导宾语从句；creep into 渗透'),
    ])

A['P4S3'] = dict(
    zh='顾客现在经常看到建议的默认选项菜单——通常远高于其消费金额的20%。',
    insight=False, note='',
    bold=['routinely', 'default options'],
    chunks=[
        dict(role='主语', text='Customers',
             note=''),
        dict(role='状语', text='now routinely',
             note=''),
        dict(role='谓语', text='see',
             note=''),
        dict(role='宾语', text='menus of suggested default options—often well above 20% of what they owe.',
             note='破折号后为补充说明；of what they owe 宾语从句作介词宾语'),
    ])

A['P4S4'] = dict(
    zh='小费金额已从1950年代的10%或更低上升到2000年左右的15%，再到如今的20%或更高。',
    insight=False, note='',
    bold=['risen from', 'or higher'],
    chunks=[
        dict(role='主语', text='The amounts',
             note=''),
        dict(role='谓语', text='have risen from 10% or less in the 1950s to 15% around the year 2000 to 20% or higher today.',
             note='rise from A to B (to C) 递进结构'),
    ])

A['P4S5'] = dict(
    zh='这种增长有时被称为小费通胀——即对越来越高的小费金额的预期。',
    insight=False, note='',
    bold=['tipflation', 'expectation'],
    chunks=[
        dict(role='主语', text='This increase',
             note=''),
        dict(role='谓语', text='is sometimes called',
             note='被动语态'),
        dict(role='主语补足语', text='tipflation—the expectation of ever-higher tip amounts.',
             note='call A B 的被动式：主语补足语；破折号后为同位解释'),
    ])

A['P5S1'] = dict(
    zh='对于传统上依赖小费的服务行业员工，如餐厅员工，小费一直是重要的收入来源，这些行业的最低小费工资可低至每小时2.13美元。',
    insight=True, note='主句采用主系表结构配长表语，从句为where引导的非限制性定语从句，都是四六级和考研真题中高频出现的句式。特别是非限制性定语从句对名词的补充说明用法，以及长表语中多层修饰的处理，具有较强的代表性和复用价值。',
    bold=['a vital source of income', 'tipped minimum wage', 'as low as'],
    chunks=[
        dict(role='主语', text='Tipping',
             note=''),
        dict(role='谓语', text='has always been',
             note='always 插在助动词后'),
        dict(role='表语', text='a vital source of income for workers in historically tipped services, like restaurants,',
             note='for/in/like 多层介词短语作后置定语'),
        dict(role='定语从句', text='where the tipped minimum wage can be as low as US$2.13 an hour.',
             note='where 引导定语从句修饰 restaurants'),
    ])
