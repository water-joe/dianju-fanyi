# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='在追求完美草坪的过程中，全国各地的房主正在走捷径——而为此付出代价的却是环境。',
    insight=True, note='本句包含主谓宾结构、主系表结构、强调句型、介词短语作状语、定语等多种成分，且强调句型是易错点，需要学生掌握"去掉框架验证完整性"的方法。成分丰富，训练价值较高。',
    bold=['In the quest for', 'taking a shortcut', 'paying the price'],
    chunks=[
        dict(role='状语', text='In the quest for the perfect lawn,',
             note=''),
        dict(role='主语', text='homeowners across the country',
             note=''),
        dict(role='谓语', text='are taking a shortcut—',
             note='现在进行时；take a shortcut 走捷径'),
        dict(role='强调句', text='and it is the environment that is paying the price.',
             note='it is... that... 强调句型，强调主语 the environment'),
    ])

A['P1S2'] = dict(
    zh='每年约有八百万平方米的塑料草坪被售出，但反对声音现已蔓延至最高园艺圈层。',
    insight=False, note='',
    bold=['square metres', 'opposition'],
    chunks=[
        dict(role='主语', text='About eight million square metres of plastic grass',
             note=''),
        dict(role='谓语', text='is sold each year',
             note='被动语态'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='opposition',
             note=''),
        dict(role='谓语', text='has now spread to the highest gardening circles.',
             note='现在完成时'),
    ])

A['P1S3'] = dict(
    zh='切尔西花展已从今年的活动中禁止人造草，宣称其不符合该展会的理念。',
    insight=True, note="本句包含主语、谓语、宾语、介词短语状语、分词短语状语等多种成分,成分种类较为丰富。分词短语declaringittobenotpartofitsethos作状语的用法值得练习,帮助学生识别非谓语动词在句中的作用。介词短语fromthisyear'sevent修饰谓语的位置和功能也有一定训练价值。",
    bold=['banned', 'ethos'],
    chunks=[
        dict(role='主语', text='The Chelsea Flower Show',
             note=''),
        dict(role='谓语', text='has banned',
             note=''),
        dict(role='宾语', text='fake grass',
             note=''),
        dict(role='状语', text="from this year's event,",
             note=''),
        dict(role='状语', text='declaring it to be not part of its ethos.',
             note='现在分词短语作伴随状语；declare A to be B 宾补结构'),
    ])

A['P1S4'] = dict(
    zh='主办这一伦敦西部年度展览的英国皇家园艺学会表示，之所以实施这一禁令，是因为塑料草坪对环境和生物多样性造成的破坏。',
    insight=True, note='主谓宾嵌套长状语和定语从句是典型的学术及新闻英语结构，对掌握长难句分析极具代表性。',
    bold=['Royal Horticultural Society', 'biodiversity'],
    chunks=[
        dict(role='主语', text='The Royal Horticultural Society (RHS), which runs the annual show in west London,',
             note=''),
        dict(role='谓语', text='says',
             note=''),
        dict(role='宾语从句', text='it has introduced the ban because of the damage plastic grass does to the environment and biodiversity.',
             note='省略 that 的宾语从句；because of + 名词短语作原因状语；(that) plastic grass does... 省略关系词的定语从句修饰 damage'),
    ])

A['P2S1'] = dict(
    zh='英国皇家园艺学会的Ed Home说:"我们去年发布了可持续发展战略，而人造草与我们在塑料问题上的理念和观点完全不符。',
    insight=True, note='引语作宾语从句、并列句、非限制性定语从句、动名词作宾语、介词短语作状语均为四六级和考研阅读常见句式;特别是引语内并列主句+定语从句嵌套的组合,在新闻报道和学术文献中高频出现,掌握后可大量迁移',
    bold=['sustainability strategy', 'in line with'],
    chunks=[
        dict(role='主语', text='Ed Home, of the RHS,',
             note=''),
        dict(role='谓语', text='said:',
             note=''),
        dict(role='宾语', text='"We launched our sustainability strategy last year and fake grass is just not in line with our ethos and views on plastic.',
             note='直接引语；并列主句；be in line with 与…一致'),
    ])

A['P2S2'] = dict(
    zh='我们建议使用真草，因为它具有环境效益，包括支持野生动物、缓解洪涝以及冷却环境。"',
    insight=False, note='',
    bold=['alleviating flooding', 'cooling the environment'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text='recommend using real grass',
             note='recommend doing 建议做；动名词作宾语'),
        dict(role='状语', text='because of its environmental benefits,',
             note='because of 介词短语作原因状语'),
        dict(role='定语从句', text='which include supporting wildlife, alleviating flooding and cooling the environment."',
             note='which 引导非限制性定语从句；三个并列动名词作 include 的宾语'),
    ])
