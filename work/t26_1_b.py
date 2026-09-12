# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S2'] = dict(
    zh='许多图书馆有护士现场进行基本的健康检查，并与全科医生诊所建立联系。',
    insight=True, note='涵盖主谓宾基本结构、地点状语、不定式作后置定语、介词短语作状语等多种成分，成分种类较为丰富，适合作为划分基础成分的练习句，但缺少易错的复杂修饰或特殊结构。',
    bold=['on site', 'health checks'],
    chunks=[
        dict(role='主语', text='Many',
             note=''),
        dict(role='谓语', text='have',
             note=''),
        dict(role='宾语', text='nurses on site',
             note=''),
        dict(role='定语', text="to carry out basic health checks, with a link to the GP's surgery.",
             note='to carry out... 不定式作后置定语；with... 介词短语作补充'),
    ])

A['P4S3'] = dict(
    zh='有些图书馆年轻人可以免费借用符合国际足联标准的足球。',
    insight=False, note='',
    bold=['Fifa-standard', 'free'],
    chunks=[
        dict(role='谓语', text='There are',
             note=''),
        dict(role='主语', text='libraries where young people can borrow a Fifa-standard football free.',
             note='where 引导定语从句修饰 libraries'),
    ])

A['P5S1'] = dict(
    zh='作为这一切的回报，你不会被要求付出任何东西。',
    insight=False, note='',
    bold=['In return for', 'precisely nothing'],
    chunks=[
        dict(role='状语', text='In return for all of this,',
             note=''),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text="'ll be asked for precisely nothing.",
             note='被动语态'),
    ])

A['P5S2'] = dict(
    zh='不会有任何收费，你也永远不会被要求证明或解释自己；你只会受到欢迎，需要帮助时会得到帮助，不需要时也不会被打扰。',
    insight=True, note='涵盖存在句、被动语态、并列谓语、宾语补足语、条件状语从句、省略结构等多种成分和结构。尤其是并列被动谓语各自带不同补语、两个条件从句分别修饰不同谓语成分、以及第二个条件从句的省略形式,都是值得训练的常见易错点。',
    bold=['no charge', 'justify', 'welcomed in'],
    chunks=[
        dict(role='谓语', text='There will be no charge',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text='will never be asked to justify or explain yourself;',
             note='被动；to justify or explain 不定式作主语补足语'),
        dict(role='谓语', text='you will simply be welcomed in, offered help if you need it, and left alone if you do not.',
             note='三个并列被动谓语；if you need it / if you do not（省略 need help）两个条件从句'),
    ])

A['P5S3'] = dict(
    zh='没有其他机构，无论是公共的还是私人的，能做出同样的承诺。',
    insight=True, note='therebe句型加限制性定语从句是四六级和考研阅读中的高频结构,用于表达存在性陈述并对主语进行限定,句式典型且常见,掌握后可迁移到大量类似句子。',
    bold=['institution', 'public or private'],
    chunks=[
        dict(role='谓语', text='There is',
             note=''),
        dict(role='主语', text='no other institution, public or private,',
             note='public or private 形容词短语作插入性后置定语'),
        dict(role='定语从句', text='that can say the same.',
             note='that 引导限制性定语从句'),
    ])

A['P5S4'] = dict(
    zh='然而我们的图书馆仍然常常被忽视和低估。',
    insight=True, note='被动语态简单句在四六级和考研阅读中较为常见，Yetstill的转折衔接、often的频度修饰、并列过去分词结构都是典型用法，掌握后可迁移到其他类似句式。',
    bold=['overlooked and underappreciated'],
    chunks=[
        dict(role='状语', text='Yet still',
             note=''),
        dict(role='主语', text='our libraries',
             note=''),
        dict(role='谓语', text='are often overlooked and underappreciated.',
             note='often 插在助动词后；两个并列过去分词构成被动谓语'),
    ])

A['P5S5'] = dict(
    zh='访问量总体下降，许多图书馆由于地方当局持续面临财政压力而陷入困境。',
    insight=True, note='并列主句加状语从句的组合是四六级和考研阅读中高频出现的句式。"Thereis"存在句、现在进行时强调持续性、"as"引导原因从句，都是真题常见结构。句子长度和复杂度与真题中档句型相当，学习后可迁移到大量类似句子。',
    bold=['overall decline', 'financial pressure'],
    chunks=[
        dict(role='谓语', text='There is an overall decline in visits',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='many',
             note=''),
        dict(role='谓语', text='are struggling',
             note=''),
        dict(role='状语从句', text='as local authorities come under continued financial pressure.',
             note='as 引导原因状语从句'),
    ])
