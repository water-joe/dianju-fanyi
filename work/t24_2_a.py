# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='Confor警告称，由于未能种植树木以生产木材，英国正面临未来的建筑危机。',
    insight=False, note='',
    bold=['construction crisis', 'because of', 'has warned'],
    chunks=[
        dict(role='主语', text='The UK',
             note=''),
        dict(role='谓语', text='is facing',
             note='现在进行时'),
        dict(role='宾语', text='a future construction crisis',
             note=''),
        dict(role='状语', text='because of a failure to plant trees to produce wood,',
             note='because of 介词短语作原因状语；to plant... 不定式作后置定语修饰 failure'),
        dict(role='主语', text='Confor',
             note='引述分句主语'),
        dict(role='谓语', text='has warned.',
             note='现在完成时引述动词'),
    ])

A['P1S2'] = dict(
    zh='这家林业和木材贸易机构呼吁采取紧急行动，减少国家对木材进口的依赖，并为子孙后代提供稳定的木材供应。',
    insight=True, note='本句展现了"主语+现在完成时谓语+宾语+不定式后置定语"这一常见句式，在四六级和考研阅读中频繁出现（尤其是新闻、报告类文本）。短语动词"callfor"、不定式作定语、and连接的并列不定式，都是高频考点。句式规整、实用性强，具有较高的迁移价值。',
    bold=['trade body', 'has called for', 'urgent action'],
    chunks=[
        dict(role='主语', text='The forestry and wood trade body',
             note=''),
        dict(role='谓语', text='has called for',
             note='call for 呼吁；现在完成时'),
        dict(role='宾语', text='urgent action',
             note=''),
        dict(role='定语', text="to reduce the country's reliance on timber imports and provide a stable supply of wood for future generations.",
             note='两个并列不定式（to reduce... and (to) provide...）作后置定语修饰 action'),
    ])

A['P1S3'] = dict(
    zh='目前英国木材需求中仅有20%来自国内生产，而英国仍然是世界上第二大木材净进口国。',
    insight=True, note='while引导的对比状语从句是考试常见句式，主句中的百分数主语和定语修饰也具有一定代表性。整体结构在说明文、议论文中较为典型，掌握后可迁移到类似表达中。',
    bold=['Currently', 'home-grown', 'net importer'],
    chunks=[
        dict(role='状语', text='Currently',
             note='时间状语'),
        dict(role='主语', text="only 20 percent of the UK's wood requirement",
             note='百分数+of 短语作主语'),
        dict(role='谓语', text='is home-grown',
             note='系表；home-grown 本国种植的'),
        dict(role='状语从句', text='while it remains the second- largest net importer of timber in the world.',
             note='while 引导对比状语从句；remain 系动词'),
    ])

A['P2S1'] = dict(
    zh='在英国政府为土地所有者提供更多种树激励措施之际，该贸易机构表示这些措施力度不够，未能宣传种植树木以增加木材供应的好处。',
    insight=False, note='',
    bold=['Coming at a time of', 'go far enough', 'fail to promote'],
    chunks=[
        dict(role='状语', text='Coming at a time of fresh incentives from the UK government for landowners to grow more trees,',
             note='现在分词短语作时间状语；to grow more trees 不定式作 incentives 的定语'),
        dict(role='主语', text='the trade body',
             note=''),
        dict(role='谓语', text='says',
             note='后接并列宾语从句（省略 that）'),
        dict(role='宾语从句', text="these don't go far enough and fail to promote the benefits of planting them to boost timber supplies.",
             note="并列谓语 don't go... and fail to...；to boost... 不定式作目的状语"),
    ])

A['P2S2'] = dict(
    zh='"我们现在不仅面临碳危机，而且由于未能种植树木以生产木材，我们还将面临未来的建筑危机。"Confor首席执行官Stuart Goodall说。',
    insight=True, note='直接引语结构、Notonly...butalso并列递进、becauseof原因状语,都是四六级和考研阅读中的高频句式。倒装结构也是常考语法点。本句结构具有很强的代表性,掌握后可以迁移到大量类似句子的理解和分析中。',
    bold=['Not only', 'carbon crisis', 'chief executive of'],
    chunks=[
        dict(role='宾语', text='"Not only are we facing a carbon crisis now, but we will also be facing a future construction crisis because of a failure to plant trees to produce wood,"',
             note='直接引语作 said 的宾语；Not only 前置引起部分倒装（are 提前）；because of 原因状语'),
        dict(role='谓语', text='said',
             note='引述动词'),
        dict(role='主语', text='Stuart Goodall',
             note='引述分句主语'),
        dict(role='同位语', text='chief executive of Confor.',
             note='说明 Stuart Goodall 职务'),
    ])
