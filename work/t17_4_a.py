# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='火灾生态学与管理专家Max Moritz教授表示，尽管野火发生频率的增加常被视为西部各州的问题，但由于其对联邦税收的影响，这是一个全国性的关切。',
    insight=True, note='“句首让步背景+主句判断+原因补充+句尾信息来源”是较常见的书面表达方式。掌握这种读法后，处理新闻、说明文和学术表达都很有迁移价值。',
    bold=['viewed as', 'frequency of wildfires', 'federal tax dollars'],
    chunks=[
        dict(role='状语', text='Though often viewed as a problem for western states,',
             note='though (it is) often viewed... 省略主谓的让步状语'),
        dict(role='主语', text='the growing frequency of wildfires',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a national concern',
             note=''),
        dict(role='状语', text='because of its impact on federal tax dollars,',
             note=''),
        dict(role='谓语', text='says',
             note='引述动词'),
        dict(role='主语', text='Professor Max Moritz,',
             note=''),
        dict(role='同位语', text='a specialist in fire ecology and management.',
             note='说明 Moritz 身份'),
    ])

A['P2S1'] = dict(
    zh='2015年，美国林务局首次将其55亿美元年度预算的一半以上用于灭火，这一比例几乎是20年前的两倍。',
    insight=False, note='',
    bold=['annual budget', 'nearly double'],
    chunks=[
        dict(role='状语', text='In 2015,',
             note=''),
        dict(role='主语', text='the US Forest Service',
             note=''),
        dict(role='状语', text='for the first time',
             note=''),
        dict(role='谓语', text='spent more than half of its $5.5 billion annual budget fighting fires',
             note='spend... doing 花费…做'),
        dict(role='同位语', text='– nearly double the percentage it spent on such efforts 20 years ago.',
             note='同位补充；(that) it spent... 省略关系词的定语从句'),
    ])

A['P2S2'] = dict(
    zh='实际上，如今用于该机构其他工作的联邦资金减少了，这些工作包括森林保护、流域和文化资源管理以及基础设施维护，这些都影响着全体美国人的生活。',
    insight=False, note='',
    bold=['In effect', 'watershed', 'upkeep'],
    chunks=[
        dict(role='状语', text='In effect,',
             note=''),
        dict(role='主语', text='fewer federal funds',
             note=''),
        dict(role='状语', text='today',
             note=''),
        dict(role='谓语', text="are going towards the agency's other work",
             note=''),
        dict(role='同位语', text='– such as forest conservation, watershed and cultural resources management, and infrastructure upkeep –',
             note='such as 举例'),
        dict(role='定语从句', text='that affect the lives of all Americans.',
             note='that 引导定语从句修饰 work'),
    ])

A['P3S1'] = dict(
    zh='另一个全国性的关切是，来自其他机构的公共资金是否正流向火灾高发地区的建设。',
    insight=True, note='主句+表语从句的结构在四六级和考研阅读中高频出现,whether引导名词性从句是常考句式,且主系表框架+名词性从句的组合具有很强的迁移性,学习者掌握后可应用于大量类似句型',
    bold=['fire-prone districts', 'public funds'],
    chunks=[
        dict(role='主语', text='Another nationwide concern',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语从句', text='whether public funds from other agencies are going into construction in fire-prone districts.',
             note='whether 引导表语从句；现在进行时'),
    ])

A['P3S2'] = dict(
    zh='正如Moritz所说，联邦资金有多少次在建造可能毁于野火的房屋？',
    insight=False, note='',
    bold=['puts it', 'lost to a wildfire'],
    chunks=[
        dict(role='状语', text='As Moritz puts it,',
             note='as 引导方式状语从句；put it 表述'),
        dict(role='状语', text='how often',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='主语', text='federal dollars',
             note=''),
        dict(role='补语', text='building homes that are likely to be lost to a wildfire?',
             note='现在分词作主语补足语；that... 定语从句修饰 homes'),
    ])

A['P4S1'] = dict(
    zh='他说:"从公共支出的角度来看，这对整个国家来说已经是一个巨大的问题。"',
    insight=False, note='',
    bold=['public expenditure perspective'],
    chunks=[
        dict(role='宾语', text='"It\'s already a huge problem from a public expenditure perspective for the whole country,"',
             note='直接引语作 says 的宾语；from... perspective 从…角度来看'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='"我们需要用放大镜来审视这个问题。',
    insight=True, note='第一句展示了不定式作宾语的用法,第二句包含疑问句结构、状语插入(instead)、双层不定式(toredirect...toconcentrate),成分种类较丰富。但缺少定语从句、宾补等常考易错点,训练价值中等',
    bold=['magnifying glass'],
    chunks=[
        dict(role='主语', text='"We',
             note=''),
        dict(role='谓语', text='need to take',
             note=''),
        dict(role='宾语', text='a magnifying glass to that.',
             note='need to do；take... to 把…对准'),
    ])
