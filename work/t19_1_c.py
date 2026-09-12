# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S5'] = dict(
    zh='反之亦然:高同情心可以替代低内疚感。',
    insight=False, note='',
    bold=['vice versa', 'substitute for'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='插入语', text='vice versa:',
             note=''),
        dict(role='主语', text='High sympathy',
             note=''),
        dict(role='谓语', text='can substitute for',
             note=''),
        dict(role='宾语', text='low guilt.',
             note=''),
    ])

A['P5S1'] = dict(
    zh='例如，在2014年的一项研究中，Malti观察了244名儿童。',
    insight=True, note='简单句在各类考试中常见，句首状语+主谓宾的结构也是典型的叙述句式，但过于简单，缺少考试中更常考的从句、非谓语等复杂结构，代表性有限。',
    bold=['looked at'],
    chunks=[
        dict(role='状语', text='In a 2014 study, for example,',
             note=''),
        dict(role='主语', text='Malti',
             note=''),
        dict(role='谓语', text='looked at',
             note=''),
        dict(role='宾语', text='244 children.',
             note=''),
    ])

A['P5S2'] = dict(
    zh='利用看护者评估和儿童的自我观察，她评定了每个孩子的整体同情心水平以及他或她在道德过失后感受负面情绪的倾向。',
    insight=False, note='',
    bold=['caregiver assessments', 'transgressions'],
    chunks=[
        dict(role='状语', text="Using caregiver assessments and the children's self-observations,",
             note='现在分词短语作方式状语'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='rated',
             note=''),
        dict(role='宾语', text="each child's overall sympathy level and his or her tendency to feel negative emotions after moral transgressions.",
             note='to feel... 不定式作后置定语；transgression 过失'),
    ])

A['P5S3'] = dict(
    zh='然后孩子们得到了巧克力硬币，并有机会与一个匿名儿童分享。',
    insight=True, note='并列谓语结构（尤其含省略）和被动语态都是四六级、考研阅读中的高频句式。本句展示了典型的"主语+be+过去分词+宾语"被动结构，以及"and"连接并列谓语时的省略规则，具有较强的代表性和迁移价值。',
    bold=['handed', 'anonymous'],
    chunks=[
        dict(role='状语', text='Then',
             note=''),
        dict(role='主语', text='the kids',
             note=''),
        dict(role='谓语', text='were handed',
             note=''),
        dict(role='宾语', text='chocolate coins,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='given a chance to share them with an anonymous child.',
             note='and 后省略 were；to share... 不定式作后置定语'),
    ])

A['P5S4'] = dict(
    zh='对于同情心较低的孩子，他们分享多少似乎取决于他们有多倾向于感到内疚。',
    insight=True, note='本句涵盖主语从句、宾语从句、介词短语状语、系表结构、不定式状语等多种成分类型,且主语从句和宾语从句由疑问词"how"引导,需区分引导词在从句内外的双重身份(引导整个从句+充当从句内部成分),是练习名词性从句成分划分的优质例句',
    bold=['appeared to', 'inclined they were to'],
    chunks=[
        dict(role='状语', text='For the low-sympathy kids,',
             note=''),
        dict(role='主语从句', text='how much they shared',
             note='how 引导主语从句'),
        dict(role='谓语', text='appeared to turn on',
             note=''),
        dict(role='宾语从句', text='how inclined they were to feel guilty.',
             note='how 引导宾语从句；be inclined to do 倾向于'),
    ])

A['P5S5'] = dict(
    zh='容易感到内疚的孩子分享得更多，尽管他们并没有神奇地对另一个孩子的匮乏变得更有同情心。',
    insight=True, note='让步状语从句(eventhough引导)是四六级和考研阅读中的高频句式,常用于表达对比或转折逻辑。过去完成时在从句中的使用也符合真题中常见的时态对比模式。该句结构清晰且逻辑关系典型,学生掌握后可直接迁移到大量类似句式中,代表性较强。',
    bold=['guilt-prone', 'deprivation'],
    chunks=[
        dict(role='主语', text='The guilt-prone ones',
             note=''),
        dict(role='谓语', text='shared',
             note=''),
        dict(role='状语', text='more,',
             note=''),
        dict(role='状语从句', text="even though they hadn't magically become more sympathetic to the other child's deprivation.",
             note='even though 引导让步状语从句；过去完成时；deprivation 匮乏'),
    ])

A['P6S1'] = dict(
    zh='"这是个好消息，"Malti说。',
    insight=False, note='',
    bold=['good news'],
    chunks=[
        dict(role='宾语', text='"That\'s good news,"',
             note='直接引语作 says 的宾语'),
        dict(role='主语', text='Malti',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P6S2'] = dict(
    zh='"我们可以表现出亲社会行为，因为我们造成了伤害并感到后悔。"',
    insight=False, note='',
    bold=['prosocial', 'regret'],
    chunks=[
        dict(role='主语', text='"We',
             note=''),
        dict(role='谓语', text='can be',
             note=''),
        dict(role='表语', text='prosocial',
             note=''),
        dict(role='状语从句', text='because we caused harm and we feel regret."',
             note='because 引导原因状语从句；并列谓语'),
    ])
