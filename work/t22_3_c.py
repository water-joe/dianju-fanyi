# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 3 —— P5 至 P6 的成分划分。口径见 t22_3_a.py 头注释。"""

A = {}

A['P5S1'] = dict(
    zh='立法者和监管机构正在缓慢开始解决暗黑模式周围的模糊性问题，最近主要在州一级。',
    insight=False, note='',
    bold=['Lawmakers', 'regulators', 'address', 'ambiguity'],
    chunks=[
        dict(role='主语', text='Lawmakers and regulators'),
        dict(role='谓语', text='are slowly starting to address'),
        dict(role='宾语', text='the ambiguity around dark patterns'),
        dict(role='状语', text='most recently at the state level'),
    ])

A['P5S2'] = dict(
    zh='3 月，加州总检察长宣布批准《加州消费者隐私法》(CCPA) 下的附加法规，这些法规"确保消费者在寻求行使其数据隐私权时不会感到困惑或被误导。',
    insight=True,
    note='典型的政经/法律类报道句式，大量使用复杂名词短语、嵌套从句和举例结构，在考研和六级长难句中非常普遍。',
    bold=['In March', 'the California Attorney General', 'announced', 'additional regulations'],
    chunks=[
        dict(role='状语', text='In March'),
        dict(role='主语', text='the California Attorney General'),
        dict(role='谓语', text='announced'),
        dict(role='宾语', text='the approval of additional regulations under the California Consumer Privacy Act (CCPA) that "ensure that consumers will not be confused or misled when seeking to exercise their data privacy rights',
             note='under... 介词短语作后置定语；that 引导定语从句修饰 regulations，从句内含第二个 that 宾语从句与 when 时间状语'),
    ])

A['P5S3'] = dict(
    zh='这些法规旨在禁止暗黑模式——这意味着禁止公司使用令人困惑的语言或不必要的步骤，例如强迫他们点击多个屏幕或听他们为何不该退出的理由。"',
    insight=False, note='',
    bold=['The regulations aim to', 'ban', 'confusing language', 'unnecessary steps'],
    chunks=[
        dict(role='主语', text='The regulations'),
        dict(role='谓语', text='aim to ban', note='aim to do 旨在做'),
        dict(role='宾语', text='dark patterns—this means prohibiting companies from using confusing language or unnecessary steps such as forcing them to click through multiple screens or listen to reasons why they shouldn\'t opt out."',
             note='破折号后 this means... 同位/解释；prohibiting... 为动名词短语；such as 举例'),
    ])

A['P6S1'] = dict(
    zh='随着更多州考虑颁布额外的法规，商业界需要更大的问责制。',
    insight=False, note='',
    bold=['As more states', 'promulgating', 'greater accountability'],
    chunks=[
        dict(role='状语从句', text='As more states consider promulgating additional regulations',
             note='as 引导时间/原因状语从句'),
        dict(role='主语', text='there'),
        dict(role='谓语', text='is'),
        dict(role='主语', text='a need for greater accountability from within the business community',
             note='there be 句型的主语（a need...）'),
    ])

A['P6S2'] = dict(
    zh='暗黑模式也可以在自律的基础上得到解决，但前提是组织不仅要对法律要求负责，还要对行业最佳实践和标准负责。',
    insight=True,
    note='本句结构在四六级和考研阅读中较为常见：主句包含情态动词和被动语态，从句使用条件状语引导，且从句内部包含并列状语。这种"主句陈述+条件限定"的句式是学术和议论文写作的典型模式，掌握后可广泛迁移到类似语境。',
    bold=['addressed', 'on a self- regulatory basis', 'hold themselves accountable', 'industry best practices'],
    chunks=[
        dict(role='主语', text='Dark patterns'),
        dict(role='谓语', text='also can be addressed', note='被动语态，情态动词+be+过分'),
        dict(role='状语', text='on a self- regulatory basis'),
        dict(role='连接词', text='but'),
        dict(role='状语从句', text='only if organizations hold themselves accountable, not just to legal requirements but also to industry best practices and standards',
             note='only if 条件状语从句；not just...but also... 并列状语'),
    ])
