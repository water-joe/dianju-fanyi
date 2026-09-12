# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='在她的新书《齿轮与怪兽：经济学是什么，以及它应该是什么》中，剑桥大学经济学家Diane Coyle认为，数字经济需要关于进步的新思维方式。',
    insight=False, note='',
    bold=['In her new book', 'an economist at', 'argues that'],
    chunks=[
        dict(role='状语', text='In her new book Cogs and Monsters: What Economics Is, and What It Should Be,',
             note='介词短语作状语；书名后 What Economics Is... 为书名副标题'),
        dict(role='主语', text='Diane Coyle',
             note=''),
        dict(role='同位语', text='an economist at Cambridge University',
             note='说明 Diane Coyle 身份'),
        dict(role='谓语', text='argues',
             note='引述动词'),
        dict(role='宾语从句', text='that the digital economy requires new ways of thinking about progress',
             note='that 引导宾语从句；of thinking about progress 介词短语作后置定语'),
    ])

A['P1S2'] = dict(
    zh='"无论我们所说的经济增长、事物变得更好是什么意思，收益都必须比近期更加均匀地分享。"她写道。',
    insight=True, note='本句覆盖主语、谓语、宾语、宾语从句、让步状语从句、方式状语、时间状语、比较状语等多种成分，且包含谓语省略、被动语态、情态助动词等易错点。引号内的长句作为宾语从句，对划分直接引语与间接成分有训练价值，适合作为综合练习句。',
    bold=['Whatever we mean', 'the gains', 'more evenly shared'],
    chunks=[
        dict(role='宾语', text='"Whatever we mean by the economy growing, by things getting better, the gains will have to be more evenly shared than in the recent past,"',
             note='直接引语作 writes 的宾语；Whatever 引导让步状语从句；主句 the gains will have to be shared 为被动语态；than in the recent past 比较状语'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='writes',
             note='引述动词（主句谓语）'),
    ])

A['P1S3'] = dict(
    zh='"一个由科技百万富翁或亿万富翁和零工工人组成的经济体，其中等收入工作被自动化削弱，将无法在政治上持续。"',
    insight=False, note='',
    bold=['gig workers', 'undercut by automation', 'politically sustainable'],
    chunks=[
        dict(role='主语', text='An economy of tech millionaires or billionaires and gig workers,',
             note='of... 介词短语作后置定语'),
        dict(role='状语', text='with middle-income jobs undercut by automation,',
             note='with 复合结构作伴随状语；undercut by automation 过去分词表被动'),
        dict(role='谓语', text='will not be',
             note=''),
        dict(role='表语', text='politically sustainable',
             note='sustainable 可持续的'),
    ])

A['P2S1'] = dict(
    zh='Coyle说，提高生活水平和让更多人增加繁荣将需要更多地使用数字技术来提高包括医疗保健和建筑在内的各个部门的生产力。',
    insight=True, note='覆盖倒装引述句、省略引导词的宾语从句、并列动名词短语作主语、不定式作目的状语等多种成分类型。倒装结构和省略that是学生常见的易错点,练习此句可提高识别主句主干和从句边界的能力,训练收益较高。',
    bold=['Improving living standards', 'boost productivity', 'says Coyle'],
    chunks=[
        dict(role='主语', text='Improving living standards and increasing prosperity for more people',
             note='两个并列动名词短语作主语'),
        dict(role='谓语', text='will require greater use of digital technologies to boost productivity in various sectors, including health care and construction,',
             note='to boost... 不定式作目的状语；including... 介词短语举例'),
        dict(role='谓语', text='says',
             note='引述动词（倒装引述分句：says 前置）'),
        dict(role='主语', text='Coyle.',
             note='引述分句的主语（says 前置倒装）'),
    ])

A['P2S2'] = dict(
    zh='但如果人们看不到好处——如果他们只是看到好工作被摧毁，就不能期望他们接受这些变化。',
    insight=True, note='本句成分丰富且具有典型训练价值：主句包含情态动词、被动语态、不定式宾语，适合练习复杂谓语的识别；两个条件状语从句考查从句识别能力；第二个从句的宾语补足语"goodjobsbeingdestroyed"是易错点，学习者容易误判为独立从句；整体覆盖主、谓、宾、条件状语等多种成分，且含有多个值得练习的语法难点。',
    bold=["can't be expected to", 'if they', 'being destroyed'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='people',
             note=''),
        dict(role='谓语', text="can't be expected to embrace the changes",
             note='be expected to do 被期望做；被动语态'),
        dict(role='状语从句', text="if they're not seeing the benefits",
             note='if 引导条件状语从句'),
        dict(role='状语从句', text="if they're just seeing good jobs being destroyed",
             note='破折号后第二个 if 条件从句；good jobs being destroyed 为 see 的宾语+宾语补足语（现在分词被动式）'),
    ])

A['P3S1'] = dict(
    zh='在最近的一次采访中，Coyle说她担心科技的不平等问题可能成为部署人工智能的障碍。',
    insight=False, note='',
    bold=['In a recent interview', 'roadblock', 'deploying AI'],
    chunks=[
        dict(role='状语', text='In a recent interview,',
             note='介词短语作状语'),
        dict(role='主语', text='Coyle',
             note=''),
        dict(role='谓语', text='said',
             note='后接省略 that 的宾语从句'),
        dict(role='宾语从句', text="she fears that tech's inequality problem could be a roadblock to deploying AI",
             note='从句内 fears 后又接 that 宾语从句；to deploying AI 动名词作 roadblock 的定语'),
    ])
