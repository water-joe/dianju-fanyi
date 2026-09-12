# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='如今，普遍存在的立即上大学的社会压力，加上快速发展的世界中日益增高的期望，常常导致学生完全忽视间隔年的可能性。',
    insight=True, note='长主语+简单谓语+宾语及宾补的结构在四六级和考研阅读中极为常见,尤其是主语部分通过介词短语和不定式扩展来表达复杂概念的写法,是学术文本的典型句式,掌握后可迁移到大量同类句子。',
    bold=['in conjunction with', 'overlook the possibility'],
    chunks=[
        dict(role='状语', text='Today,',
             note=''),
        dict(role='主语', text='widespread social pressure to immediately go to college in conjunction with increasingly high expectations in a fast-moving world',
             note='to go... 不定式作后置定语；in conjunction with 连同（并列结构）'),
        dict(role='状语', text='often',
             note=''),
        dict(role='谓语', text='causes',
             note=''),
        dict(role='宾语', text='students',
             note=''),
        dict(role='宾语补足语', text='to completely overlook the possibility of taking a gap year.',
             note='cause sb. to do 宾补；of taking... 动名词作介词宾语'),
    ])

A['P1S2'] = dict(
    zh='毕竟，如果你认识的每个人都在秋季上大学，那么推迟一年似乎很愚蠢，不是吗？',
    insight=True, note='"if条件从句+主句"结构、形式主语"it"搭配不定式、定语从句省略关系代词，都是四六级和考研真题中的高频句式。本句句式组合典型，学生掌握后可大量迁移到类似结构的句子中。',
    bold=['After all', 'stay back a year'],
    chunks=[
        dict(role='状语', text='After all,',
             note=''),
        dict(role='状语从句', text='if everyone you know is going to college in the fall,',
             note='if 条件状语从句；(whom) you know 省略关系词的定语从句'),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text='seems silly',
             note=''),
        dict(role='真正主语', text='to stay back a year,',
             note=''),
        dict(role='附加问句', text="doesn't it?",
             note='反义疑问句'),
    ])

A['P1S3'] = dict(
    zh='而且在上了12年学之后，花一年时间做一些非学术性的事情感觉并不自然。',
    insight=True, note='本句在主干识别上有一定难度(形式主语需要判断),成分丰富且涵盖多个训练价值高的考点(形式主语、定语从句、不定式短语、现在分词),结构典型(形式主语+定语从句都是常考句式),而时态简单不构成额外负担。综合来看,这是一个适合优先用于句子结构训练的材料,能让学习者在适度挑战中掌握可迁移的分析方法。',
    bold=['feel natural', "isn't academic"],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='状语', text='after going to school for 12 years,',
             note='after + 动名词作时间状语'),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text="doesn't feel natural",
             note=''),
        dict(role='真正主语', text="to spend a year doing something that isn't academic.",
             note='不定式作真正主语；that... 定语从句修饰 something'),
    ])

A['P2S1'] = dict(
    zh='但尽管这可能是事实，却不足以成为谴责间隔年的充分理由。',
    insight=True, note='“让步状语从句+主句评价”是考试阅读和写作里都很常见的句型，像"while...,..."这种转折推进也很典型。掌握这种识别顺序，迁移价值较高。',
    bold=['condemn', 'good enough reason'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语从句', text='while this may be true,',
             note='while 引导让步状语从句'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text="'s not",
             note=''),
        dict(role='表语', text='a good enough reason to condemn gap years.',
             note='to condemn... 不定式作后置定语'),
    ])

A['P2S2'] = dict(
    zh='人们总是不断担心在社会延续的"冲向终点线的竞赛"中落后于其他所有人，无论那是通向研究生院、医学院还是一份高薪职业。',
    insight=True, note='本句涵盖了therebe存在句、动名词作介词宾语、过去分词作后置定语、同位语从句、虚拟语气等多个考点，成分种类较为丰富。同位语从句的识别和虚拟语气的判断都是常见易错点，具有较好的训练价值。',
    bold=['falling behind', 'lucrative'],
    chunks=[
        dict(role='谓语', text="There's always",
             note=''),
        dict(role='主语', text='a constant fear of falling behind everyone else on the socially perpetuated "race to the finish line,"',
             note='of falling behind... 动名词短语作后置定语；perpetuated 过去分词作定语'),
        dict(role='状语从句', text='whether that be toward graduate school, medical school or a lucrative career.',
             note='whether 让步状语从句（虚拟语气 be）'),
    ])
