# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 4 —— 逐句成分划分（后半：P6S3–P6S6）。

口径见 BUILD_GUIDE.md / CLAUDE.md：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""
A = {}

A['P6S3'] = dict(
    zh='即使现在有了稳定的工作，他说:"我无法独自负担每月的抵押贷款，所以我不得不把房间租给别人来实现这一点。"',
    insight=True, note='句子覆盖了主语、谓语、宾语、宾语补足语、状语等多种成分,且包含不定式作宾语、不定式作目的状语、介词短语作状语等典型结构。宾语从句内的并列结构和目的状语的嵌套也是常见易错点,非常适合作为成分划分练习句。',
    bold=["can't afford", 'monthly mortgage payments', 'rent rooms out', 'on my own'],
    chunks=[
        dict(role='状语从句', text='Even now that he is working steadily',
             note='now that 引导原因状语从句，even 加强语气'),
        dict(role='主语', text='he',
             note='主句主语'),
        dict(role='谓语', text='said',
             note='引述动词'),
        dict(role='主语', text='I',
             note='引语中第一个分句的主语'),
        dict(role='谓语', text="can't afford",
             note='情态动词 + 动词原形'),
        dict(role='宾语', text='to pay my monthly mortgage payments',
             note='不定式短语作宾语'),
        dict(role='状语', text='on my own',
             note='方式状语'),
        dict(role='连接词', text='so',
             note='并列连词，引出结果分句'),
        dict(role='主语', text='I',
             note='引语中第二个分句的主语'),
        dict(role='谓语', text='have to rent',
             note=''),
        dict(role='宾语', text='rooms',
             note=''),
        dict(role='状语', text='out to people to make that happen',
             note='out to people 为对象状语；to make that happen 为目的状语'),
    ])

A['P6S4'] = dict(
    zh='回首往事，他惊讶于他的父母能够为子女提供舒适的生活，尽管在他年幼时父母双方都没有完成大学学业。',
    insight=True, note='本句在主干识别、嵌套层级、时态难度、成分训练价值和结构典型性五个维度上均处于中等偏上水平，尤其在嵌套复杂度和成分训练价值上较为突出。作为句子结构与时态训练材料，它能够覆盖多个重要知识点且具有较好的迁移性，推荐作为中高难度练习句优先学习。',
    bold=['Looking back', 'struck', 'comfortable life', 'completed college'],
    chunks=[
        dict(role='状语', text='Looking back',
             note='现在分词短语作时间状语'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='struck',
             note='过去分词作表语；be struck that... 表示「对…感到震惊」'),
        dict(role='连接词', text='that',
             note='引导名词性从句，说明 struck 的内容'),
        dict(role='主语', text='his parents',
             note='从句主语'),
        dict(role='谓语', text='could provide',
             note=''),
        dict(role='宾语', text='a comfortable life',
             note=''),
        dict(role='状语', text='for their children',
             note=''),
        dict(role='状语从句', text='even though neither had completed college when he was young',
             note='even though 引导让步状语从句；内含 when 引导的时间状语从句'),
    ])

A['P6S5'] = dict(
    zh='"我仍然是在一个中上层阶级家庭中长大的，父母都没有大学学位，"Schneider说。',
    insight=False, note='',
    bold=['grew up', 'middle-class', 'college degrees'],
    chunks=[
        dict(role='主语', text='I',
             note='引语中的主语'),
        dict(role='谓语', text='still grew up',
             note=''),
        dict(role='状语', text='in an upper middle-class home',
             note='介词短语作地点状语'),
        dict(role='定语', text="with parents who didn't have college degrees",
             note="介词短语作后置定语修饰 home；内含定语从句 who didn't have college degrees 修饰 parents"),
        dict(role='主语', text='Schneider',
             note='引述分句的主语'),
        dict(role='谓语', text='said',
             note='引述分句的谓语'),
    ])

A['P6S6'] = dict(
    zh='"我认为人们不再有能力做到这一点了。"',
    insight=True, note='"主句+宾语从句"且宾语从句省略that是四六级和考研阅读中的高频句式,尤其think/believe/hope等动词后省略引导词非常常见。本句结构简洁但典型,掌握后可迁移到大量类似句子,具有较高的学习复用价值。',
    bold=["don't think", 'capable of', 'anymore'],
    chunks=[
        dict(role='主语', text='I',
             note=''),
        dict(role='谓语', text="don't think",
             note='否定转移：形式上否定 think，语义上否定从句'),
        dict(role='主语', text='people',
             note='宾语从句的主语（think 后省略 that）'),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='capable of that anymore',
             note='be capable of 表示「有能力做…」'),
    ])
