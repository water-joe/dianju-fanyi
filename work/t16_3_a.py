# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='如今每个人都太忙了，这已是陈词滥调。',
    insight=False, note='',
    bold=['cliché'],
    chunks=[
        dict(role='主语从句', text="That everyone's too busy these days",
             note='that 引导主语从句'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a cliché.',
             note=''),
    ])

A['P1S2'] = dict(
    zh='但有一种抱怨尤其令人哀伤:永远没有时间阅读。',
    insight=False, note='',
    bold=['mournfully', 'never any time to read'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='one specific complaint',
             note=''),
        dict(role='谓语', text='is made',
             note=''),
        dict(role='状语', text='especially mournfully:',
             note=''),
        dict(role='同位语从句', text="There's never any time to read.",
             note='冒号后为同位语从句'),
    ])

A['P2S1'] = dict(
    zh='让这个问题更棘手的是，通常的时间管理技巧似乎并不够用。',
    insight=True, note='"What"引导主语从句+系动词+"that"引导表语从句，这是考研和四六级阅读中的高频句式，用于表达「某事物就是某情况」的逻辑。掌握这种结构后，可以迁移到大量类似句子的分析，实用性强。',
    bold=['thornier', 'time-management techniques'],
    chunks=[
        dict(role='主语从句', text='What makes the problem thornier',
             note='what 引导主语从句'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语从句', text="that the usual time-management techniques don't seem sufficient.",
             note='that 引导表语从句'),
    ])

A['P2S2'] = dict(
    zh='网上充斥着提供腾出时间阅读建议的文章:"放弃看电视"或"随时随地带本书"。',
    insight=True, note='本句展现的"主语+befullof+名词+现在分词定语"结构在四六级和考研阅读中较为常见，尤其是现在分词短语作后置定语修饰名词的用法（如articlesofferingtips,studentsstudyingabroad）是高频句式。掌握后可迁移到大量同类句子的分析中。',
    bold=['tips on making time to read', 'at all times'],
    chunks=[
        dict(role='主语', text='The web',
             note=''),
        dict(role='谓语', text="'s full of",
             note=''),
        dict(role='宾语', text='articles offering tips on making time to read:',
             note='offering... 现在分词作后置定语'),
        dict(role='同位语', text='"Give up TV" or "Carry a book with you at all times."',
             note='冒号后为 tips 的具体内容'),
    ])

A['P2S3'] = dict(
    zh='坐下来阅读时，与工作相关的思绪飞轮依然转个不停——要么就是你疲惫不堪，一本有挑战性的书是你最不需要的东西。',
    insight=False, note='',
    bold=['the flywheel of work-related thoughts', 'the last thing you need'],
    chunks=[
        dict(role='状语', text='Sit down to read',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='the flywheel of work-related thoughts',
             note=''),
        dict(role='谓语', text='keeps spinning –',
             note=''),
        dict(role='状语从句', text="or else you're so exhausted that a challenging book's the last thing you need.",
             note='so... that... 结果状语从句；the last thing sb. needs 最不需要的'),
    ])

A['P2S4'] = dict(
    zh='小说家兼评论家Tim Parks写道，现代人的思维"压倒性地倾向于交流……问题不仅仅在于一个人被打断；而在于一个人实际上倾向于被打断"。深度阅读不仅需要时间，还需要一种特殊的时间，这种时间无法仅仅通过提高效率来获得。',
    insight=True, note="包含了'so...that'、'thelastthingsomeoneneeds'以及祈使句并列等多个真题高频句式，极具代表性。",
    bold=['overwhelmingly inclined', 'inclined to interruption', "can't be obtained merely"],
    chunks=[
        dict(role='主语', text='The modern mind,',
             note=''),
        dict(role='插入语', text='Tim Parks, a novelist and critic, writes,',
             note='插入的引述结构；a novelist and critic 为同位语'),
        dict(role='宾语', text='"is overwhelmingly inclined toward communication… It is not simply that one is interrupted; it is that one is actually inclined to interruption."',
             note='直接引语作 writes 的宾语；并列表语从句'),
        dict(role='主语', text='Deep reading',
             note=''),
        dict(role='谓语', text='requires',
             note=''),
        dict(role='宾语', text="not just time, but a special kind of time which can't be obtained merely by becoming more efficient.",
             note='not just... but... 并列；which... 定语从句修饰 time；by becoming 动名词作方式状语'),
    ])
