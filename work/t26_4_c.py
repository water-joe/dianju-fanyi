# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S2'] = dict(
    zh='2024年，Wicker Park音乐节的参与人数创下纪录。',
    insight=False, note='',
    bold=['record-breaking attendance'],
    chunks=[
        dict(role='状语', text='In 2024,',
             note=''),
        dict(role='主语', text='Wicker Park Fest',
             note=''),
        dict(role='谓语', text='saw record-breaking attendance.',
             note='see 此处意为「经历、见证」'),
    ])

A['P5S3'] = dict(
    zh='尽管参与人数众多，入口捐款却降至我们历史上的最低点。',
    insight=True, note='主句+让步状语的结构在四六级和考研阅读中较为常见，"Despite"引导让步也是典型考点。但本句结构相对简单，未涉及从句或复杂修饰，作为句式代表性中等偏上。',
    bold=['the turnout', 'lowest point'],
    chunks=[
        dict(role='状语', text='Despite the turnout,',
             note=''),
        dict(role='主语', text='gate donations',
             note=''),
        dict(role='谓语', text='reached',
             note=''),
        dict(role='宾语', text='their lowest point in our history.',
             note=''),
    ])

A['P5S4'] = dict(
    zh='今年，我们被迫缩小节日的规模。',
    insight=False, note='',
    bold=['scale back', 'footprint'],
    chunks=[
        dict(role='状语', text='This year,',
             note=''),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text="'ve been forced to scale back the footprint of the fest.",
             note='be forced to do 被迫做；scale back 缩减'),
    ])

A['P5S5'] = dict(
    zh='我们取消了一个舞台，预订了更少的表演者，并进行了额外削减以降低成本，同时努力保持节日一如既往的活力，一如既往地支持本地艺术家和商业，并一如既往地忠于参与者所期待的Wicker Park独特精神和声誉。',
    insight=True, note="包含并列谓语、目的状语、复杂的伴随状语以及'as...as'比较从句，是练习划分长难句成分、识别多重并列关系的极佳素材。",
    bold=['eliminating', 'striving to keep', 'come to expect'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text='are eliminating a stage, booking fewer performers and making additional cuts to reduce our costs,',
             note='三个并列现在进行时谓语；to reduce... 不定式作目的状语'),
        dict(role='状语', text="all while striving to keep the festival as vibrant as ever, as supportive of local artists and businesses, and as true to Wicker Park's unique spirit and reputation as festgoers have come to expect.",
             note='all while + 动名词表伴随；三个 as...as 比较结构并列；as festgoers have come to expect 方式状语从句'),
    ])

A['P6S1'] = dict(
    zh='今年夏天，当你享受你最喜爱的社区街头节日时，我希望你会记得它们的存在源于社区支持。',
    insight=True, note='"主句+状语从句+宾语从句嵌套"是四六级和考研阅读中的高频句式，特别是hope/think/believe等动词后跟宾语从句、再嵌套一层that从句的结构非常典型，掌握后可大量迁移。',
    bold=['community support'],
    chunks=[
        dict(role='状语', text='This summer,',
             note=''),
        dict(role='状语从句', text='as you enjoy your favorite neighborhood street festival,',
             note='as 引导时间状语从句'),
        dict(role='主语', text='I',
             note=''),
        dict(role='谓语', text='hope',
             note=''),
        dict(role='宾语从句', text="you'll remember that they exist because of community support.",
             note='宾语从句内嵌套 that 从句；because of... 原因状语'),
    ])

A['P6S2'] = dict(
    zh='一个繁荣的夏季节日季不会偶然发生，它的实现需要我们所有人共同出力。',
    insight=False, note='',
    bold=['thriving', 'chip in'],
    chunks=[
        dict(role='主语', text='A thriving summer festival season',
             note=''),
        dict(role='谓语', text="doesn't happen by accident;",
             note='by accident 偶然（do 强调）'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='happens',
             note=''),
        dict(role='状语从句', text='when we all chip in.',
             note='when 引导时间/条件状语从句；chip in 共同出力'),
    ])
