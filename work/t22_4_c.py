# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 4 —— P5 的成分划分。口径见 t22_4_a.py 头注释。"""

A = {}

A['P5S1'] = dict(
    zh='Schwitzgebel 怀疑最大的影响来自社会影响——主持讨论的同学或助教可能分享了他们自己的素食主义，表明这是可实现的或更常见的。',
    insight=False, note='',
    bold=['suspects', 'social influence', 'classmates', 'teaching assistants', 'vegetarianism'],
    chunks=[
        dict(role='主语', text='Schwitzgebel'),
        dict(role='谓语', text='suspects'),
        dict(role='宾语', text='the greatest impact came from social influence—classmates or teaching assistants leading the discussions may have shared their own vegetarianism, showing it as achievable or more common',
             note='suspects 后省略 that 的宾语从句；破折号后 classmates or... 为同位语解释 social influence'),
    ])

A['P5S2'] = dict(
    zh='其次，视频可能产生了情感影响。',
    insight=True,
    note='情态动词加完成式（may have done）是四六级和考研阅读中常见的表推测结构，具有一定代表性，但本句整体结构过于简单，缺少从句或复杂修饰，典型性中等。',
    bold=['Second', 'emotional impact'],
    chunks=[
        dict(role='状语', text='Second'),
        dict(role='主语', text='the video'),
        dict(role='谓语', text='may have had', note='情态动词+完成时，表推测'),
        dict(role='宾语', text='an emotional impact'),
    ])

A['P5S3'] = dict(
    zh='他认为，理性论证的激励作用最小——尽管他的共同作者们说理性可能发挥更大的作用。',
    insight=True,
    note='本句覆盖了主系表倒装结构、插入语、让步状语从句、宾语从句、情态动词谓语等多种成分和结构类型，且主句的倒装和插入语是常见易错点，需要还原语序才能准确划分成分。宾语从句省略了引导词 that，也是需要识别的考点，训练价值较高。',
    bold=['Least rousing', 'rational argument', 'co-authors', 'play a bigger role'],
    chunks=[
        dict(role='表语', text='Least rousing', note='表语前置，主句为倒装'),
        dict(role='插入语', text='he thinks'),
        dict(role='谓语', text='was', note='系动词，与前置表语构成倒装'),
        dict(role='主语', text='rational argument'),
        dict(role='状语从句', text='although his co-authors say reason might play a bigger role',
             note='让步状语从句；say 后省略 that 的宾语从句'),
    ])

A['P5S4'] = dict(
    zh='现在研究人员正在探究教学风格、助教的饮食习惯和学生观看视频的具体效果。',
    insight=False, note='',
    bold=['probing', 'specific effects', 'teaching style', 'video exposure'],
    chunks=[
        dict(role='状语', text='Now'),
        dict(role='主语', text='the researchers'),
        dict(role='谓语', text='are probing'),
        dict(role='宾语', text='the specific effects of teaching style, teaching assistants\' eating habits and students\' video exposure',
             note='effects 后接 of 介词短语，内含三个并列名词'),
    ])

A['P5S5'] = dict(
    zh='与此同时，曾预测不会有效果的 Schwitzgebel 将要食言了。',
    insight=True,
    note='非限制性定语从句插入主句内部是四六级和考研阅读中的高频句式，用破折号或逗号分隔修饰成分的写法非常典型；将来进行时与过去完成时的时态对比在叙述语境中也常见；整体句式具有较强的代表性，掌握后可以应用于理解大量类似结构的句子。',
    bold=['Meanwhile', 'had predicted', 'eating his words'],
    chunks=[
        dict(role='状语', text='Meanwhile'),
        dict(role='主语', text='Schwitzgebel—who had predicted no effect',
             note='主语含破折号分隔的非限制性定语从句（who had predicted no effect）'),
        dict(role='谓语', text='will be eating', note='将来进行时'),
        dict(role='宾语', text='his words', note='eat one\'s words 固定搭配：收回前言、食言'),
    ])
