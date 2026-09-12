# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='"我们谈论的是颠覆。"她说。',
    insight=False, note='',
    bold=['disruption'],
    chunks=[
        dict(role='宾语', text='"We\'re talking about disruption,"',
             note='直接引语作 says 的宾语'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='says',
             note=''),
    ])

A['P3S3'] = dict(
    zh='"这些是变革性技术，改变了我们每天度过时间的方式，改变了成功的商业模式。"',
    insight=False, note='',
    bold=['transformative technologies', 'business models'],
    chunks=[
        dict(role='主语', text='These',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='transformative technologies that change the ways we spend our time every day, that change business models that succeed',
             note='两个 that 定语从句并列修饰 technologies；we spend our time every day 省略关系词的定语从句修饰 ways；that succeed 修饰 business models'),
    ])

A['P3S4'] = dict(
    zh='她补充说，要做出这样的"巨大变化"，你需要社会认同。',
    insight=True, note='简单句+不定式目的状语的组合在四六级和考研阅读中较为常见,具有一定代表性,但因无从句结构,典型性不如复合句。',
    bold=['tremendous changes', 'she adds', 'social buy-in'],
    chunks=[
        dict(role='状语', text='To make such "tremendous changes,"',
             note='不定式作目的状语'),
        dict(role='插入语', text='she adds,',
             note='引述插入语'),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text='need',
             note=''),
        dict(role='宾语', text='social buy-in',
             note='buy-in 认同、支持'),
    ])

A['P4S1'] = dict(
    zh='Coyle说，相反，随着收益被认为流向少数繁荣城市的精英，许多人的怨恨正在酝酿。',
    insight=True, note='句子包含插入语、主动进行时谓语、被动语态谓语、主语补语、原因状语从句等多种成分，可以练习识别插入语对主干的干扰、被动结构中的补语识别、状语从句的定位，成分种类较丰富',
    bold=['Instead', 'resentment is simmering', 'perceived to'],
    chunks=[
        dict(role='插入语', text='Instead, says Coyle,',
             note='引述插入语（says Coyle 倒装）'),
        dict(role='主语', text='resentment',
             note=''),
        dict(role='谓语', text='is simmering',
             note='现在进行时，simmer 酝酿、积蓄'),
        dict(role='状语', text='among many',
             note='介词短语作状语'),
        dict(role='状语从句', text='as the benefits are perceived to go to elites in a handful of prosperous cities',
             note='as 引导原因/时间状语从句；are perceived to... 被动结构；in a handful of... 介词短语修饰 elites'),
    ])

A['P5S1'] = dict(
    zh='根据Brookings Institution的数据，到2019年，包括旧金山、圣何塞、波士顿和西雅图在内的八个美国城市的简短名单拥有大约38%的科技工作岗位。',
    insight=True, note='典型的真题句式:主语带定语从句修饰、句首介词短语作状语、核心陈述事实性数据,这种结构在四六级和考研阅读中极为常见,尤其是学术报告、统计数据类文本;掌握后可直接迁移到大量同类句子',
    bold=['According to', 'roughly 38%', 'tech jobs'],
    chunks=[
        dict(role='状语', text='According to the Brookings Institution,',
             note='介词短语作状语，表信息来源'),
        dict(role='主语', text='a short list of eight American cities that included San Francisco, San Jose, Boston, and Seattle',
             note='that included... 定语从句修饰 cities'),
        dict(role='谓语', text='had',
             note=''),
        dict(role='宾语', text='roughly 38% of all tech jobs',
             note=''),
        dict(role='状语', text='by 2019',
             note='时间状语'),
    ])

A['P5S2'] = dict(
    zh='新的人工智能技术尤其集中:Brookings的Mark Muro和Sifan Liu估计，仅15个城市就占据了美国三分之二的人工智能资产和能力。',
    insight=True, note='本句包含两个并列主句加一个宾语从句的组合,是四六级和考研阅读中常见的句式。通过冒号连接主句进行解释说明,以及"estimatethat"引导宾语从句的结构,都是学术和新闻文本的典型用法,掌握后可迁移到大量类似句子,具有较高的代表性。',
    bold=['particularly concentrated', 'estimate', 'account for'],
    chunks=[
        dict(role='主语', text='New AI technologies',
             note=''),
        dict(role='谓语', text='are particularly concentrated',
             note='被动/表语结构'),
        dict(role='主语', text="Brookings's Mark Muro and Sifan Liu",
             note=''),
        dict(role='谓语', text='estimate',
             note='后接 that 宾语从句'),
        dict(role='宾语从句', text='that just 15 cities account for two-thirds of the AI assets and capabilities in the United States',
             note='account for 占据'),
    ])
