# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S3'] = dict(
    zh='在另一次观察中，她看到手机成为家庭中紧张关系的来源。',
    insight=False, note='',
    bold=['a source of tension'],
    chunks=[
        dict(role='状语', text='During a separate observation,',
             note=''),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='saw',
             note=''),
        dict(role='宾语从句', text='that phones became a source of tension in the family.',
             note='that 引导宾语从句'),
    ])

A['P2S4'] = dict(
    zh='父母会查看电子邮件，而孩子们则会兴奋地争取他们的注意力。',
    insight=True, note='while引导时间状语从句对比两个并行动作，是四六级和考研阅读中常见的句式。过去将来进行时虽不如一般时态常见，但在叙述、描述场景的语境中有一定代表性。句子体现了典型的主从复合句结构和对比逻辑，掌握后可迁移到类似场景。',
    bold=['looking at their emails', 'bids for their attention'],
    chunks=[
        dict(role='主语', text='Parents',
             note=''),
        dict(role='谓语', text='would be looking at their emails',
             note=''),
        dict(role='状语从句', text='while the children would be making excited bids for their attention.',
             note='while 引导对比状语从句；过去将来进行时；make bids for 争取'),
    ])

A['P3S1'] = dict(
    zh='婴儿天生会看着父母的脸来试图理解他们的世界，如果这些脸是空白和无反应的——就像沉浸在设备中时经常出现的那样——这对孩子来说可能会非常令人不安。',
    insight=True, note='该句兼具结构复杂性和逻辑清晰性，是进阶学习者练习长难句分析、识别从句层级的必练曲目。',
    bold=['wired to', 'unresponsive', 'disconcerting'],
    chunks=[
        dict(role='主语', text='Infants',
             note=''),
        dict(role='谓语', text="are wired to look at parents' faces to try to understand their world,",
             note='be wired to do 天生倾向于；to try... 目的状语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='状语从句', text='if those faces are blank and unresponsive – as they often are when absorbed in a device –',
             note='if 条件状语从句；破折号内为 as 引导的方式状语从句'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='can be',
             note=''),
        dict(role='表语', text='extremely disconcerting for the children.',
             note='disconcerting 令人不安的'),
    ])

A['P3S2'] = dict(
    zh='Radesky引用了发展心理学家Ed Tronick在二十世纪七十年代设计的"静止面孔实验"。',
    insight=False, note='',
    bold=['cites', 'devised by'],
    chunks=[
        dict(role='主语', text='Radesky',
             note=''),
        dict(role='谓语', text='cites',
             note=''),
        dict(role='宾语', text='the "still face experiment" devised by developmental psychologist Ed Tronick in the 1970s.',
             note='devised by... 过去分词短语作后置定语'),
    ])

A['P3S3'] = dict(
    zh='在实验中，要求一位母亲先以正常方式与孩子互动，然后面无表情，不给孩子任何视觉社交反馈:随着孩子试图吸引母亲的注意力，她变得越来越焦虑。',
    insight=False, note='',
    bold=['blank expression', 'distressed'],
    chunks=[
        dict(role='状语', text='In it,',
             note=''),
        dict(role='主语', text='a mother',
             note=''),
        dict(role='谓语', text='is asked to interact with her child in a normal way',
             note='be asked to do 被动'),
        dict(role='状语', text='before putting on a blank expression and not giving them any visual social feedback:',
             note='before + 动名词'),
        dict(role='主语', text='The child',
             note=''),
        dict(role='谓语', text='becomes increasingly distressed',
             note=''),
        dict(role='状语从句', text="as she tries to capture her mother's attention.",
             note='as 引导时间状语从句'),
    ])
