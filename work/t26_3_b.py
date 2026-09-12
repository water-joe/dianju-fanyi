# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='Ferrovie dello Stato Italiane是一家公共控股集团，拥有列车运营商Trenitalia和国家铁路网络RFI，该集团表示其运营的所有高速列车中有百分之二十三在2023年出现晚点。',
    insight=True, note='本句结构高度典型:主句+宾语从句是四六级和考研阅读的常见句式,主语带同位语(含定语从句)和宾语从句主语中嵌套定语从句(尤其是省略关系代词的定语从句)都是真题高频考点,掌握本句的拆解方法可直接迁移到大量类似长难句的分析。',
    bold=['publicly controlled', 'train operator'],
    chunks=[
        dict(role='主语', text='Ferrovie dello Stato Italiane,',
             note=''),
        dict(role='同位语', text='the publicly controlled group that owns train operator Trenitalia and the national train network RFI,',
             note='同位语内含 that 定语从句'),
        dict(role='谓语', text='said',
             note=''),
        dict(role='宾语从句', text='23 percent of all high-speed trains it operated were late in 2023.',
             note='(that/which) it operated 省略关系词的定语从句修饰 trains'),
    ])

A['P4S1'] = dict(
    zh='Ferrovie表示，意大利陈旧基础设施的巨大改善在一定程度上解释了中断的原因。',
    insight=False, note='',
    bold=['obsolete infrastructure', 'partly'],
    chunks=[
        dict(role='主语', text="The huge improvements in Italy's obsolete infrastructure",
             note='in... 介词短语作后置定语'),
        dict(role='状语', text='partly',
             note=''),
        dict(role='谓语', text='explained',
             note=''),
        dict(role='宾语', text='the disruption,',
             note=''),
        dict(role='主语', text='said',
             note='倒装引述分句谓语'),
        dict(role='宾语', text='Ferrovie.',
             note='倒装引述分句主语'),
    ])

A['P4S2'] = dict(
    zh='网络运营商RFI是欧洲复苏基金的最大单一受益方，计划到2026年投资240亿欧元。',
    insight=False, note='',
    bold=['recovery fund', 'beneficiary', 'planned investments'],
    chunks=[
        dict(role='主语', text='RFI, the network operator,',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='the single largest European recovery fund beneficiary with planned investments of €24bn by 2026.',
             note='with... 介词短语作后置定语'),
    ])

A['P4S3'] = dict(
    zh='Ferrovie将在未来10年内对基础设施投资总计1240亿欧元。',
    insight=False, note='',
    bold=['a total of'],
    chunks=[
        dict(role='主语', text='Ferrovie',
             note=''),
        dict(role='谓语', text='will invest a total of €124bn in infrastructure over the next 10 years.',
             note='invest... in... 投资于'),
    ])

A['P5S1'] = dict(
    zh='但运力不足是另一个问题。',
    insight=False, note='',
    bold=['lack of capacity'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='lack of capacity',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='another problem.',
             note=''),
    ])

A['P5S2'] = dict(
    zh='交通经济学家Andrea Giuricin表示，计划中的投资将带来改善，但期间的中断是不可避免的。',
    insight=True, note='该句型属于新闻报道和学术写作中的常见结构：引述权威人士观点（主句）加上其具体论述内容（宾语从句），宾语从句内部用but转折说明问题的两面性。这种结构在四六级和考研阅读中频繁出现，掌握后可复用于理解大量类似表达。',
    bold=['Transport economist', 'in the meantime', 'inevitable'],
    chunks=[
        dict(role='主语', text='Transport economist Andrea Giuricin',
             note=''),
        dict(role='谓语', text='said',
             note='后接并列宾语从句'),
        dict(role='宾语从句', text='the planned investments would bring improvements but disruptions in the meantime were inevitable.',
             note='从句内 but 连接两个并列分句；planned 过去分词作定语'),
    ])
