# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='联邦政府为弥补我们国家公园长期资金缺口而提出的想法很容易被视为荒谬。',
    insight=True, note='本句使用的"Itis+形容词+todo"结构是四六级和考研英语中高频出现的典型句式，尤其在观点陈述和评价类文章中极为常见。形式主语后置是英语书面语中平衡句子结构、避免头重脚轻的标准用法，掌握此结构后可直接迁移到大量类似句型（如Itisimportanttodo、Itisnecessarytodo等）。因此本句具有很高的结构典型性和学习迁移价值。',
    bold=['dismiss as', 'chronic funding gap'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text="'s easy",
             note=''),
        dict(role='真正宾语', text="to dismiss as absurd the federal government's ideas for plugging the chronic funding gap of our national parks.",
             note='不定式作真正主语；dismiss A as B 把 A 视为 B；chronic 长期的'),
    ])

A['P1S2'] = dict(
    zh='真的有人认为允许亚马逊将货物送到你在约塞米蒂的帐篷里，或者让餐车在红杉国家公园的红杉树下排成行是个好主意吗？',
    insight=False, note='',
    bold=['line up'],
    chunks=[
        dict(role='谓语', text='Can anyone really think',
             note=''),
        dict(role='宾语从句', text="it's a good idea to allow Amazon deliveries to your tent in Yosemite or food trucks to line up under the redwood trees at Sequoia National Park?",
             note='省略 that 的宾语从句；it 形式主语；两个并列不定式复合结构（allow... to... 宾补）'),
    ])

A['P2S1'] = dict(
    zh='但政府在一件事上是对的：美国国家公园正处于危机之中。',
    insight=False, note='',
    bold=['in crisis'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='the government',
             note=''),
        dict(role='谓语', text='is right about one thing:',
             note=''),
        dict(role='同位语从句', text='U.S. national parks are in crisis.',
             note='冒号后为同位语从句，说明 one thing 的内容'),
    ])

A['P2S2'] = dict(
    zh='它们总共积压了超过120亿美元的维护费用。',
    insight=True, note='主谓宾加状语的简单句是英语基本句式，但本句过于简单、缺少从句或复杂修饰，不能代表四六级或考研真题中常见的长难句结构，典型性和迁移价值中等偏下。',
    bold=['maintenance backlog'],
    chunks=[
        dict(role='状语', text='Collectively,',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='have',
             note=''),
        dict(role='宾语', text='a maintenance backlog of more than $12 billion.',
             note='maintenance backlog 维护积压'),
    ])

A['P2S3'] = dict(
    zh='道路、小径、卫生间、游客中心和其他基础设施正在破败。',
    insight=False, note='',
    bold=['infrastructure', 'crumbling'],
    chunks=[
        dict(role='主语', text='Roads, trails, restrooms, visitor centers and other infrastructure',
             note=''),
        dict(role='谓语', text='are crumbling.',
             note='现在进行时；crumble 破败、崩塌'),
    ])

A['P3S1'] = dict(
    zh='但将露营地私有化和商业化并不是万能药。',
    insight=False, note='',
    bold=['privatizing', 'cure-all'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='privatizing and commercializing the campgrounds',
             note='两个并列动名词短语作主语'),
        dict(role='谓语', text='would not be',
             note=''),
        dict(role='表语', text='a cure-all.',
             note='cure-all 万能药'),
    ])

A['P3S2'] = dict(
    zh='露营地只占整体基础设施积压的很小一部分，而且公园内的企业平均只向国家公园管理局上交其收入的约5%。',
    insight=False, note='',
    bold=['a tiny portion', 'revenues'],
    chunks=[
        dict(role='主语', text='Campgrounds',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='a tiny portion of the overall infrastructure backlog,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='businesses in the parks',
             note=''),
        dict(role='谓语', text='hand over, on average, only about 5% of their revenues to the National Park Service.',
             note='hand over A to B 把 A 交给 B；on average 为插入语'),
    ])

A['P4S1'] = dict(
    zh='此外，私有化程度的提高肯定会削弱每年3亿游客来公园的一个主要原因：享受自然，从充斥日常生活的商业鼓噪中得到喘息。',
    insight=True, note='本句的结构是四六级和考研阅读中常见的典型句式：主句+定语从句修饰宾语+同位语解释内容+定语从句修饰同位语中的名词。这种多层修饰的长难句在真题中频繁出现，掌握后可以迁移到大量类似句子的分析中，代表性很强。',
    bold=['undercut', 'commercial drumbeat'],
    chunks=[
        dict(role='状语', text='Moreover,',
             note=''),
        dict(role='主语', text='increased privatization',
             note=''),
        dict(role='谓语', text='would certainly undercut',
             note=''),
        dict(role='宾语', text='one of the major reasons why 300 million visitors come to the parks each year:',
             note='why 引导定语从句修饰 reasons'),
        dict(role='同位语', text='to enjoy nature and get a break from the commercial drumbeat that overwhelms daily life.',
             note='不定式短语解释 reasons 的内容；that... 定语从句修饰 drumbeat'),
    ])
