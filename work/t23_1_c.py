# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S1'] = dict(
    zh='去年，另一份关于禁止人造草坪的请愿书征集到三万个签名，政府对此回应称"没有禁止使用人造草的计划"。',
    insight=True, note='本句覆盖了主句的主谓宾结构、长状语、宾语从句、非限制性定语从句、插入语等多种成分类型，且状语和从句嵌套位置容易混淆，能有效训练学生区分主干与修饰成分、识别从句归属的能力，训练价值较高。',
    bold=['In response to', 'artificial grass'],
    chunks=[
        dict(role='状语', text='In response to another petition last year about banning fake lawns,',
             note='介词短语作状语；about banning... 动名词作介词宾语'),
        dict(role='定语从句', text='which gathered 30,000 signatures,',
             note='which 引导非限制性定语从句'),
        dict(role='主语', text='the government',
             note=''),
        dict(role='谓语', text='responded',
             note=''),
        dict(role='宾语从句', text='that it has "no plans to ban the use of artificial grass".',
             note='that 引导宾语从句'),
    ])

A['P6S1'] = dict(
    zh='政府补充道:"我们更倾向于帮助个人和组织做出正确选择，而非就此类事项立法。',
    insight=True, note='本句呈现典型的学术或政策性文本特征:多个并列主句、转折副词However、情态动词表达义务和建议、复杂名词短语加后置定语、while引导的让步从句。这些都是四六级和考研阅读中的高频结构,掌握后可迁移到大量类似语境。引述结构"Itadded:"也常见于新闻报道和政策解读类文章。结构代表性强。',
    bold=['legislating on', 'make the right choice'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='added:',
             note=''),
        dict(role='宾语', text='"We prefer to help people and organisations make the right choice rather than legislating on such matters.',
             note='直接引语；prefer to do... rather than (doing)... 对比结构；make the right choice 为宾补'),
    ])

A['P6S2'] = dict(
    zh='然而，人造草的使用必须遵守现行的法律和政策保障措施，以保护生物多样性并确保可持续排水，同时诸如强化的生物多样性义务等措施应有助于鼓励公共机构考虑可持续的替代方案。"',
    insight=False, note='',
    bold=['comply with', 'safeguards', 'sustainable alternatives'],
    chunks=[
        dict(role='连接词', text='However,',
             note=''),
        dict(role='主语', text='the use of artificial grass',
             note=''),
        dict(role='谓语', text='must comply with the legal and policy safeguards in place',
             note='comply with 遵守；in place 后置定语'),
        dict(role='状语', text='to protect biodiversity and ensure sustainable drainage,',
             note='不定式作目的状语'),
        dict(role='状语从句', text='while measures such as the strengthened biodiversity duty should serve to encourage public authorities to consider sustainable alternatives."',
             note='while 引导让步/对比状语从句；serve to do 有助于；encourage sb. to do 宾补'),
    ])
