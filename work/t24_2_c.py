# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='虽然生产性树木种植可以为农村经济带来实际的经济效益，并有助于英国的净零排放战略，但政府支持的重点仍然集中在粮食生产以及仅为生物多样性而进行的野化和本土林地种植。',
    insight=False, note='',
    bold=['productive tree planting', 'deliver', 'net-zero strategy'],
    chunks=[
        dict(role='状语从句', text="While productive tree planting can deliver real financial benefits to rural economies and contribute to the UK's net-zero strategy,",
             note='while 引导让步状语从句；并列谓语 deliver... and contribute to...'),
        dict(role='主语', text='the focus of government support',
             note=''),
        dict(role='谓语', text='continues to be on food production and the rewilding and planting of native woodland solely for biodiversity.',
             note='continue to do 继续做'),
    ])

A['P4S2'] = dict(
    zh='Goodall补充说:"虽然粮食生产和生物多样性健康显然至关重要，但我们需要我们的土地也能提供建筑和制造所需的可靠木材供应，并为实现净零排放做出贡献。"',
    insight=True, note='本句结构高度典型：引述结构+宾语从句+让步状语从句+宾补不定式并列，是四六级和考研阅读中常见的复合句模式。While引导的让步从句前置、needsbtodo的宾补结构、并列不定式的并列连词省略（provide...andcontribute...）都是考试高频考点。掌握本句的分析方法可直接迁移到大量真题句式。',
    bold=['added', 'of critical importance', 'secure supplies'],
    chunks=[
        dict(role='主语', text='Goodall',
             note=''),
        dict(role='谓语', text='added:',
             note=''),
        dict(role='宾语', text='"While food production and biodiversity health are clearly of critical importance, we need our land to also provide secure supplies of wood for construction, manufacturing and contribute to net zero."',
             note='直接引语作宾语；While 引导让步状语从句；need our land to provide... 宾补结构；provide... and contribute... 并列不定式（省略 to）'),
    ])

A['P5S1'] = dict(
    zh='"虽然英国政府已表明其扩大植树的雄心，但在实际行动上却很少。',
    insight=True, note='"While"引导的让步或对比状语从句置于句首、主句使用therebe句型,这两种结构在四六级和考研阅读中频繁出现。本句句式典型,掌握后可迁移到大量类似句子,实用性强。',
    bold=['has stated', 'ambition', 'little action'],
    chunks=[
        dict(role='状语从句', text='"While the UK government has stated its ambition for more tree planting,',
             note='while 引导让步状语从句'),
        dict(role='主语', text='there',
             note=''),
        dict(role='谓语', text='has been',
             note='there be 句型（现在完成时）'),
        dict(role='主语', text='little action on the ground.',
             note='there be 句型的真正主语；on the ground 在实际行动上'),
    ])

A['P5S2'] = dict(
    zh='Confor现在呼吁为这些愿景注入更大的推动力，以确保我们有足够的木材来满足不断增长的需求。"',
    insight=True, note='主句+宾语从句的结构在四六级和考研阅读中非常常见，且本句中目的状语引导宾语从句的用法也是典型句式，学习后可迁移到大量类似句子。',
    bold=['calling for', 'impetus', 'meet increasing demand'],
    chunks=[
        dict(role='主语', text='Confor',
             note=''),
        dict(role='谓语', text='is now calling for',
             note='call for 呼吁；现在进行时'),
        dict(role='宾语', text='much greater impetus behind those aspirations',
             note=''),
        dict(role='状语', text='to ensure we have enough wood to meet increasing demand."',
             note='to ensure... 不定式作目的状语；（that）we have... 省略 that 的宾语从句'),
    ])
