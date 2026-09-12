# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='美国农民多年来一直抱怨劳动力短缺。',
    insight=False, note='',
    bold=['complaining of', 'labor shortages'],
    chunks=[
        dict(role='主语', text='American farmers',
             note=''),
        dict(role='谓语', text='have been complaining of',
             note=''),
        dict(role='宾语', text='labor shortages',
             note=''),
        dict(role='状语', text='for several years.',
             note='现在完成进行时；complain of 抱怨'),
    ])

A['P1S2'] = dict(
    zh='如果不对农业工人的移民规定进行全面改革，这些抱怨不太可能停止。',
    insight=False, note='',
    bold=['unlikely to stop', 'an overhaul of'],
    chunks=[
        dict(role='主语', text='The complaints',
             note=''),
        dict(role='谓语', text='are unlikely to stop',
             note=''),
        dict(role='状语', text='without an overhaul of immigration rules for farm workers.',
             note='without 引导条件状语；overhaul 全面改革'),
    ])

A['P2S1'] = dict(
    zh='国会一直阻挠为农业工人创建更简便签证的努力，这种签证将允许外国工人在美国停留更长时间并在该行业内更换工作。',
    insight=False, note='',
    bold=['obstructed', 'straightforward visa'],
    chunks=[
        dict(role='主语', text='Congress',
             note=''),
        dict(role='谓语', text='has obstructed',
             note=''),
        dict(role='宾语', text='efforts to create a more straightforward visa for agricultural workers',
             note='to create... 不定式作后置定语'),
        dict(role='定语从句', text='that would let foreign workers stay longer in the U.S. and change jobs within the industry.',
             note='that... 定语从句修饰 visa；let sb. do 宾补；并列不定式 stay... and change...'),
    ])

A['P2S2'] = dict(
    zh='如果这种情况不改变，美国企业、社区和消费者将成为输家。',
    insight=False, note='',
    bold=['will be the losers'],
    chunks=[
        dict(role='状语从句', text="If this doesn't change,",
             note='if 引导条件状语从句'),
        dict(role='主语', text='American businesses, communities, and consumers',
             note=''),
        dict(role='谓语', text='will be',
             note=''),
        dict(role='表语', text='the losers.',
             note=''),
    ])

A['P3S1'] = dict(
    zh='美国农场劳动力中大约有一半是无证移民。',
    insight=False, note='',
    bold=['undocumented immigrants'],
    chunks=[
        dict(role='状语', text='Perhaps',
             note=''),
        dict(role='主语', text='half of U.S. farm laborers',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='undocumented immigrants.',
             note=''),
    ])

A['P3S2'] = dict(
    zh='随着此类工人进入该国的人数减少，农业劳动力的特征正在发生变化。',
    insight=False, note='',
    bold=['characteristics', 'workforce'],
    chunks=[
        dict(role='状语从句', text='As fewer such workers enter the country,',
             note='as 引导时间状语从句'),
        dict(role='主语', text='the characteristics of the agricultural workforce',
             note=''),
        dict(role='谓语', text='are changing.',
             note='现在进行时'),
    ])

A['P3S3'] = dict(
    zh='今天的农场劳动者虽然仍以在墨西哥出生为主，但更可能是定居而非迁徙，更可能是已婚而非单身。',
    insight=False, note='',
    bold=['predominantly', 'settled rather than migrating'],
    chunks=[
        dict(role='主语', text="Today's farm laborers,",
             note=''),
        dict(role='插入语', text='while still predominantly born in Mexico,',
             note='while (they are) still... 省略主谓的插入语'),
        dict(role='谓语', text='are more likely to be settled rather than migrating and more likely to be married than single.',
             note='be likely to do；rather than / than 对比结构'),
    ])

A['P3S4'] = dict(
    zh='他们也在老龄化。',
    insight=False, note='',
    bold=['aging'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text="'re also aging.",
             note='现在进行时；age 变老'),
    ])

A['P3S5'] = dict(
    zh='在本世纪初，约三分之一的农作物工人年龄在35岁以上。',
    insight=False, note='',
    bold=['At the start of', 'crop workers'],
    chunks=[
        dict(role='状语', text='At the start of this century,',
             note=''),
        dict(role='主语', text='about one-third of crop workers',
             note=''),
        dict(role='谓语', text='were',
             note=''),
        dict(role='表语', text='over the age of 35.',
             note=''),
    ])
