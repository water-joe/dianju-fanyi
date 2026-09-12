# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S1'] = dict(
    zh='California计划到2020年每年处理35000英亩森林，到2030年处理60000英亩——资金来自该州排放许可证拍卖的收益。',
    insight=False, note='',
    bold=['treat', 'proceeds of'],
    chunks=[
        dict(role='主语', text='California',
             note=''),
        dict(role='谓语', text='plans to treat',
             note=''),
        dict(role='宾语', text='35,000 acres of forest a year by 2020, and 60,000 by 2030 –',
             note=''),
        dict(role='状语', text="financed from the proceeds of the state's emissions-permit auctions.",
             note='过去分词短语作后置/补充说明；proceeds 收益'),
    ])

A['P5S2'] = dict(
    zh='这只是可以受益的总面积中的一小部分，总计约50万英亩，因此优先处理火灾或干旱风险最大的地区至关重要。',
    insight=True, note='包含因果并列结构、限制性定语从句、形式主语等常考句式。特别是so引出的因果并列和itisvitaltodo的形式主语结构在考试中频繁出现，具有较高的代表性和迁移价值。',
    bold=['acreage', 'prioritize'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text="'s only a small share of the total acreage",
             note=''),
        dict(role='定语从句', text='that could benefit,',
             note='that... 定语从句修饰 acreage'),
        dict(role='同位语', text='about half a million acres in all,',
             note='补充说明总面积'),
        dict(role='状语从句', text='so it will be vital to prioritize areas at greatest risk of fire or drought.',
             note='so 引导结果状语从句；it 形式主语；to prioritize... 真正主语'),
    ])

A['P6S1'] = dict(
    zh='该战略还旨在确保从森林中移除的木质材料中的碳以实木木材的形式固定下来，或作为生物燃料在原本使用化石燃料的车辆中燃烧。',
    insight=True, note='本句成分丰富且包含多个训练价值高的点:主句包含不定式作宾语、宾语从句整体作宾语;宾语从句内有并列谓语(且第二个谓语承前省略is)、过去分词作后置定语"removedfromtheforests"、多个不同类型的状语(方式状语intheformof、asbiofuel,地点状语invehicles);定语从句中关系代词that作主语。这些成分覆盖了从句、非谓语、并列、修饰关系等多个易错点,是优质的划分练习句。',
    bold=['locked away', 'solid lumber', 'biofuel'],
    chunks=[
        dict(role='主语', text='The strategy',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='aims to ensure',
             note=''),
        dict(role='宾语从句', text='that carbon in woody material removed from the forests is locked away in the form of solid lumber or burned as biofuel in vehicles that would otherwise run on fossil fuels.',
             note='that 引导宾语从句；removed from... 过去分词作后置定语；is locked away... or (is) burned... 并列被动谓语；that... 定语从句修饰 vehicles'),
    ])

A['P6S2'] = dict(
    zh='关于运输生物燃料的新研究已经在进行中。',
    insight=False, note='',
    bold=['under way'],
    chunks=[
        dict(role='主语', text='New research on transportation biofuels',
             note=''),
        dict(role='谓语', text='is already under way.',
             note='under way 在进行中'),
    ])

A['P7S1'] = dict(
    zh='州政府非常习惯于管理森林，但传统上它们关注的是野生动物、流域和娱乐机会。',
    insight=True, note='两个主句通过转折连词"but"并列是四六级和考研阅读中的常见句式,且第二分句的现在完成时"havefocusedon"结构在真题中频繁出现,具有较好的代表性和复用价值,适合作为并列句和完成时的入门练习句',
    bold=['accustomed to', 'watersheds', 'recreation'],
    chunks=[
        dict(role='主语', text='State governments',
             note=''),
        dict(role='谓语', text='are well accustomed to managing forests,',
             note='be accustomed to doing 习惯于做'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='状语', text='traditionally',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text="'ve focused on",
             note=''),
        dict(role='宾语', text='wildlife, watersheds and opportunities for recreation.',
             note='现在完成时；focus on 关注'),
    ])

A['P7S2'] = dict(
    zh='直到最近，它们才开始认识到森林在储存碳方面必须发挥的重要作用。',
    insight=True, note='本句涵盖倒装结构中的主谓宾识别、时间状语前置、省略关系词的定语从句、动名词短语作介词宾语、介词短语作地点状语等多种成分类型，且定语从句中省略的关系词在从句内充当宾语，是典型的易错点。适合作为成分划分的综合练习材料。',
    bold=['Only recently', 'vital part'],
    chunks=[
        dict(role='状语', text='Only recently',
             note=''),
        dict(role='谓语', text='have',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='come to see',
             note=''),
        dict(role='宾语', text='the vital part forests will have to play in storing carbon.',
             note='only 置首引起部分倒装；the vital part (that) forests will have to play 省略关系词的定语从句；in storing... 动名词作介词宾语'),
    ])

A['P7S3'] = dict(
    zh='California的计划预计将于明年由州长最终确定，应该作为一个典范。',
    insight=False, note='',
    bold=['finalized', 'serve as a model'],
    chunks=[
        dict(role='主语', text="California's plan, which is expected to be finalized by the governor next year,",
             note='which 引导非限制性定语从句；be expected to do'),
        dict(role='谓语', text='should serve as',
             note=''),
        dict(role='宾语', text='a model.',
             note='serve as 作为'),
    ])
