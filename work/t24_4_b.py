# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 4 —— 逐句成分划分（中段：P3–P4S1）。口径见 t24_4_a.py 头注释。"""
A = {}

A['P3S1'] = dict(
    zh='在没有额外保护措施的情况下，公司可能会以消费者未授权或未预料到的方式共享(并可能将其货币化)个人健康信息。',
    insight=True,
    note='句子成分丰富且包含多个练习点：句首介词短语状语、括号内并列谓语、名词短语作宾语、方式状语内嵌定语从句、定语从句省略关系词、从句中并列谓语省略助动词。特别是定语从句修饰抽象名词 way 且省略关系词这一结构，在真题中常见但学生容易忽略，作为划分成分练习句有较高训练价值。',
    bold=['Without additional protections', 'monetize', 'in a way'],
    chunks=[
        dict(role='状语', text='Without additional protections in place',
             note='介词短语作条件状语'),
        dict(role='主语', text='companies'),
        dict(role='谓语', text='may share (and potentially monetize)',
             note='括号内 and potentially monetize 与 share 并列'),
        dict(role='宾语', text='personal health information'),
        dict(role='状语', text='in a way consumers may not have authorized or anticipated',
             note='方式状语；consumers may not have authorized or anticipated 为省略关系词（that/in which）的定语从句修饰 way'),
    ])

A['P3S2'] = dict(
    zh='2021年，Flo Health面临联邦贸易委员会的调查。',
    insight=False, note='',
    bold=['In 2021', 'faced', 'Federal Trade Commission'],
    chunks=[
        dict(role='状语', text='In 2021', note='时间状语'),
        dict(role='主语', text='Flo Health'),
        dict(role='谓语', text='faced'),
        dict(role='宾语', text='a Federal Trade Commission (FTC) investigation',
             note='FTC 为 Federal Trade Commission 缩写'),
    ])

A['P3S3'] = dict(
    zh='联邦贸易委员会在一项投诉中指控"尽管有明确的隐私声明，该公司还是控制了用户的敏感生育数据并将其与第三方共享"。',
    insight=True,
    note='主句+that引导宾语从句的结构在四六级和考研真题中非常常见，尤其是新闻报道、学术陈述类文本。从句内部包含让步状语和并列谓语，也是典型的复杂句特征。掌握这类结构后可大量复用到类似句型。',
    bold=['The FTC', 'alleged', 'despite express privacy claims'],
    chunks=[
        dict(role='主语', text='The FTC'),
        dict(role='谓语', text='alleged'),
        dict(role='状语', text='in a complaint', note='介词短语作状语'),
        dict(role='宾语从句', text='that "despite express privacy claims, the company took control of users\' sensitive fertility data and shared it with third parties."',
             note='that 引导宾语从句；从句内 despite...claims 为让步状语，took control... and shared... 为并列谓语'),
    ])

A['P3S4'] = dict(
    zh='Flo Health与联邦贸易委员会通过一项同意令解决了此事，要求该公司在共享用户健康信息之前获得应用程序用户的明确肯定同意，并指示第三方删除他们已获得的数据。',
    insight=True,
    note='本句结构在四六级和考研真题中具有较高代表性。主句+定语从句（关系代词省略）是高频考点；现在分词作后置定语修饰名词、不定式作宾语补足语、并列不定式结构也是常考句式。过去完成时在定语从句中的使用典型地体现了时态的相对性。整体句式虽略长，但各部分都是标准语法结构的组合，掌握后可以在阅读理解和翻译题中大量复用。',
    bold=['settled the matter', 'requiring', 'express affirmative consent'],
    chunks=[
        dict(role='主语', text='Flo Health and the FTC'),
        dict(role='谓语', text='settled'),
        dict(role='宾语', text='the matter'),
        dict(role='状语', text='with a Consent Order',
             note='介词短语作方式状语'),
        dict(role='定语', text='requiring the company to get app users\' express affirmative consent before sharing their health information as well as to instruct the third parties to delete the data they had obtained',
             note='现在分词短语作后置定语修饰 Consent Order；内含并列不定式 to get ... as well as to instruct ...；they had obtained 为省略关系代词的定语从句修饰 data，过去完成时'),
    ])

A['P4S1'] = dict(
    zh='《联邦贸易委员会法》第5条授权联邦贸易委员会对不公平或欺骗性行为采取执法行动，这意味着联邦贸易委员会只能在公司的隐私做法具有误导性或造成不正当消费者损害之后采取行动。',
    insight=True,
    note='本句覆盖主语、谓语、宾语、宾语补足语、表语、时间状语、条件状语从句等多种成分，结构较为丰富。第一个主句的不定式宾补、第二个主句的情态动词谓语、条件从句内的并列谓语和系表结构，都是值得练习的考点。对于成分划分训练而言，本句具有较好的练习价值。',
    bold=['empowers', 'initiate enforcement action', 'meaning'],
    chunks=[
        dict(role='主语', text='Section 5 of the FTC Act',
             note='of the FTC Act 为介词短语作后置定语'),
        dict(role='谓语', text='empowers'),
        dict(role='宾语', text='the FTC'),
        dict(role='宾语补足语', text='to initiate enforcement action against unfair or deceptive acts',
             note='不定式作宾补；against... 介词短语修饰 action'),
        dict(role='定语', text='meaning the FTC can only act after the fact if a company\'s privacy practices are misleading or cause unjustified consumer harm',
             note='现在分词短语作结果/伴随定语；内含 if 条件状语从句，从句中 are misleading 与 cause...harm 为并列谓语'),
    ])
