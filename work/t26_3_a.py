# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='自2008年罗马与米兰之间的高速铁路网络开通以来，火车已成为意大利本地人和游客在全国各地出行的首选方式。',
    insight=False, note='',
    bold=['preferred means of travel', 'locals and tourists alike'],
    chunks=[
        dict(role='状语', text='Since the 2008 launch of the high-speed rail network between Rome and Milan,',
             note='since + 名词短语作时间状语'),
        dict(role='主语', text='trains',
             note=''),
        dict(role='谓语', text='have become',
             note=''),
        dict(role='表语', text='the preferred means of travel across Italy for locals and tourists alike.',
             note='for... and... alike 介词短语作状语性修饰'),
    ])

A['P1S2'] = dict(
    zh='快速列车可以在三小时内完成两座城市之间500公里的行程。',
    insight=False, note='',
    bold=['cover'],
    chunks=[
        dict(role='主语', text='Fast trains',
             note=''),
        dict(role='谓语', text='can cover the 500km between the two cities in three hours.',
             note='cover 此处指「行驶完（一段距离）」'),
    ])

A['P1S3'] = dict(
    zh='该铁路网还连接那不勒斯、博洛尼亚、佛罗伦萨和都灵。',
    insight=False, note='',
    bold=['connects'],
    chunks=[
        dict(role='主语', text='The network',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='connects Naples, Bologna, Florence and Turin.',
             note=''),
    ])

A['P1S4'] = dict(
    zh='在许多情况下，它是在旅行时间和成本方面的最佳选择——对休闲旅客和商务旅客而言都是。',
    insight=True, note='主系表结构配合多个修饰成分是考试中常见的句式，尤其是后置定语和插入语的使用较为典型，具有一定的迁移价值，但句式本身不算复杂或高频难点。',
    bold=['the best option', 'leisure and business travellers'],
    chunks=[
        dict(role='状语', text='In many cases,',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='the best option',
             note=''),
        dict(role='插入语', text='— in terms of travel time and cost —',
             note='插入语'),
        dict(role='状语', text='for both leisure and business travellers.',
             note='both... and... 并列'),
    ])

A['P2S1'] = dict(
    zh='这就是为什么最近由大量维护工程造成的严重延误使铁路行业在大多数人外出度假的时期陷入混乱，这对一个旅游业占GDP百分之十的国家的商业活动至关重要。',
    insight=True, note='"Thisiswhy"引出表语从句说明原因、现在完成时表示过去对现在的影响、"which"引导非限制性定语从句补充说明、"where"引导定语从句修饰地点名词，这些都是四六级和考研阅读中的高频句式，掌握后可大量迁移',
    bold=['maintenance works', 'into chaos', 'accounts for'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='is why',
             note='why 引导表语从句'),
        dict(role='表语从句', text='the recent severe delays caused by numerous maintenance works have thrown the rail industry into chaos at a time when most people head on holiday,',
             note='caused by... 过去分词作后置定语；throw... into chaos 使…陷入混乱；when... 定语从句修饰 time'),
        dict(role='定语从句', text='which matters for business in a country where tourism accounts for 10 percent of GDP.',
             note='which 引导非限制性定语从句（指代前面整件事）；where... 定语从句修饰 country；account for 占比'),
    ])

A['P3S1'] = dict(
    zh='中断变得越来越频繁，列车延误现在已成为意大利媒体报道的固定内容。',
    insight=True, note='主系表结构加状语是四六级和考研阅读中的高频句式，with复合结构也是常考语法点。本句结构简洁但完整，能代表真题中常见的陈述加补充信息的表达模式，学习后可迁移到大量类似句子。',
    bold=['Disruptions', 'a fixture in'],
    chunks=[
        dict(role='主语', text='Disruptions',
             note=''),
        dict(role='谓语', text='have become',
             note=''),
        dict(role='表语', text='increasingly frequent',
             note=''),
        dict(role='状语', text='with train delays now a fixture in Italian media coverage.',
             note='with 复合结构（名词+名词短语作补充）'),
    ])
