# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 2 —— P6 至 P8 的成分划分。口径见 t22_2_a.py 头注释。"""

A = {}

A['P6S1'] = dict(
    zh='TD Ameritrade 的研究显示，由于寿命延长，美国人也在增加储蓄以保护他们的养老金，该研究调查了 2000 名 40 至 79 岁的成年人。',
    insight=False, note='',
    bold=['Because of', 'boosting', 'preserve', 'nest eggs', 'surveyed'],
    chunks=[
        dict(role='状语', text='Because of longer life spans'),
        dict(role='主语', text='Americans'),
        dict(role='谓语', text='are also boosting'),
        dict(role='宾语', text='their savings'),
        dict(role='状语', text='to preserve their nest eggs',
             note='不定式作目的状语'),
        dict(role='主语', text='the TD Ameritrade study'),
        dict(role='谓语', text='showed', note='引述动词，主语 the TD Ameritrade study 在前'),
        dict(role='定语从句', text='which surveyed 2000 adults between 40 and 79',
             note='非限制性定语从句修饰 study'),
    ])

A['P6S2'] = dict(
    zh='根据调查，十分之六的"不退休者"正在增加储蓄以应对更长的寿命。',
    insight=False, note='',
    bold=['Six in 10', 'in anticipation of'],
    chunks=[
        dict(role='主语', text='Six in 10 "unretirees"'),
        dict(role='谓语', text='are increasing'),
        dict(role='宾语', text='their savings'),
        dict(role='状语', text='in anticipation of a longer life'),
        dict(role='状语', text='according to the survey', note='依据状语'),
    ])

A['P6S3'] = dict(
    zh='该公司表示，他们这样做的最流行方式包括减少总体开支、购买人寿保险或最大化对退休账户的缴款。',
    insight=False, note='',
    bold=['Among the most popular ways', 'reducing', 'securing', 'maximizing', 'retirement accounts'],
    chunks=[
        dict(role='状语', text='Among the most popular ways they are doing this'),
        dict(role='插入语', text='the company said'),
        dict(role='谓语', text='is', note='倒装：表语前置'),
        dict(role='表语', text='by reducing their overall expenses, securing life insurance or maximizing their contributions to retirement accounts',
             note='by + 并列动名词短语作表语'),
    ])

A['P7S1'] = dict(
    zh='位于巴尔的摩的财务规划公司 Facet Wealth 的联合创始人 Brent Weiss 说，不幸的是，许多选择在退休后工作的人准备这样做，是因为他们担心晚年无法维持生计。',
    insight=True,
    note='本句涵盖主语（含定语从句修饰）、谓语、宾语（不定式）、状语（句首副词、原因状语从句、时间状语）等多种成分；定语从句中关系代词"who"在从句内作主语，是学生常错的考点；主句宾语"to do so"中的"so"指代较为隐晦，需理解上下文；成分种类较丰富，适合练习修饰成分的识别与剥离。',
    bold=['Unfortunately', 'opting to work', 'making ends meet', 'later years'],
    chunks=[
        dict(role='状语', text='Unfortunately'),
        dict(role='主语', text='many people who are opting to work in retirement',
             note='主语含 who 引导的定语从句'),
        dict(role='谓语', text='are preparing'),
        dict(role='状语', text='to do so', note='不定式作状语，so 指代 work in retirement'),
        dict(role='状语从句', text='because they are worried about making ends meet in their later years',
             note='原因状语从句'),
        dict(role='谓语', text='said', note='引述动词，主语在后'),
        dict(role='主语', text='Brent Weiss, a co-founder at Baltimore-based financial-planning firm Facet Wealth',
             note='引述主语；a co-founder... 为同位语'),
    ])

A['P7S2'] = dict(
    zh='他建议即将退休的人应该与财务顾问交谈，以设定长期财务目标。',
    insight=True,
    note='"主句+that 引导的宾语从句"是四六级和考研阅读中的高频句式，从句内含情态动词、介词短语和不定式作状语，贴近真题常见结构，典型性较强，掌握后可大量复用。',
    bold=['suggested', 'preretirees', 'financial adviser', 'long-term'],
    chunks=[
        dict(role='主语', text='He'),
        dict(role='谓语', text='suggested'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='主语', text='preretirees'),
        dict(role='谓语', text='should speak', note='情态动词谓语'),
        dict(role='状语', text='with a financial adviser'),
        dict(role='状语', text='to set long-term financial goals',
             note='不定式作目的状语'),
    ])

A['P8S1'] = dict(
    zh='"人生中最具挑战性的时刻是结婚、组建家庭以及最终退休，"Weiss 说。',
    insight=False, note='',
    bold=['challenging', 'getting married', 'starting a family'],
    chunks=[
        dict(role='主语', text='"The most challenging moments in life'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='getting married, starting a family and ultimately retiring,"',
             note='三个动名词短语并列作表语'),
        dict(role='谓语', text='Weiss said', note='引述'),
    ])

A['P8S2'] = dict(
    zh='"这不仅仅是一个财务决定，而是情感上的决定。',
    insight=False, note='',
    bold=['an emotional one'],
    chunks=[
        dict(role='主语', text='"It'),
        dict(role='谓语', text="'s"),
        dict(role='表语', text='not just a financial decision, but an emotional one.',
             note='not...but... 连接两个并列表语'),
    ])

A['P8S3'] = dict(
    zh='许多人认为他们无法退休。"',
    insight=False, note='',
    bold=['believe', "can't retire"],
    chunks=[
        dict(role='主语', text='Many people'),
        dict(role='谓语', text='believe'),
        dict(role='宾语', text='they can\'t retire."', note='省略 that 的宾语从句'),
    ])
