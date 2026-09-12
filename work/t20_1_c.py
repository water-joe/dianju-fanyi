# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S1'] = dict(
    zh='考虑到机器的简约设计，老鼠愿意与社交型机器交朋友令人惊讶。',
    insight=False, note='',
    bold=['readiness', 'given its minimal design'],
    chunks=[
        dict(role='主语', text='The readiness of the rats to befriend the social robot',
             note='to befriend... 不定式作后置定语'),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='surprising',
             note=''),
        dict(role='状语', text='given its minimal design.',
             note='given 介词「考虑到」'),
    ])

A['P6S2'] = dict(
    zh='这个机器与普通老鼠大小相同，但看起来像一个装在轮子上的简单塑料盒。',
    insight=True, note='本句覆盖了主语、并列谓语、表语、宾语、比较状语等多种成分,且并列谓语一个是系表结构一个是主谓宾结构,可练习区分表语与宾语。比较结构"thesame...as"中存在谓语省略现象,可训练学生补全省略成分的能力,具有一定训练价值',
    bold=['the same size as', 'resembled'],
    chunks=[
        dict(role='主语', text='The robot',
             note=''),
        dict(role='谓语', text='was the same size as a regular rat',
             note='the same... as... 比较结构（as a regular rat (is) 省略谓语）'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='谓语', text='resembled',
             note=''),
        dict(role='宾语', text='a simple plastic box on wheels.',
             note=''),
    ])

A['P6S3'] = dict(
    zh='"我们原本以为必须给它安装一个能动的头和尾巴、面部特征，并在它身上喷洒气味使其闻起来像真老鼠，但这些都不必要。"澳大利亚昆士兰大学的Janet Wiles说，她参与了这项研究。',
    insight=True, note='覆盖了主语、谓语、宾语从句、双宾语结构、并列谓语、直接和间接宾语、目的状语、地点状语、表语、非限制性定语从句等多种成分；特别是双宾语结构和并列谓语的组合，以及关系代词在从句中充当主语的情况，都是常见易错点，训练价值高。',
    bold=['assumed', 'scent', 'helped with the research'],
    chunks=[
        dict(role='宾语', text='"We\'d assumed we\'d have to give it a moving head and tail, facial features, and put a scent on it to make it smell like a real rat, but that wasn\'t necessary,"',
             note='直接引语作 says 的宾语；内嵌两个省略 that 的宾语从句；give it... 双宾语；to make... 不定式作目的'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Janet Wiles at the University of Queensland in Australia,',
             note=''),
        dict(role='定语从句', text='who helped with the research.',
             note='who 引导非限制性定语从句'),
    ])

A['P7S1'] = dict(
    zh='这一发现显示了老鼠对社交线索的敏感程度，即使这些线索来自基本的机器。',
    insight=False, note='',
    bold=['how sensitive', 'social cues'],
    chunks=[
        dict(role='主语', text='The finding',
             note=''),
        dict(role='谓语', text='shows',
             note=''),
        dict(role='宾语从句', text='how sensitive rats are to social cues,',
             note='how 引导宾语从句'),
        dict(role='状语从句', text='even when they come from basic robots.',
             note='even when 引导让步状语从句'),
    ])

A['P7S2'] = dict(
    zh='同样，儿童往往会把机器当作同类对待，即使它们只展示简单的社交信号。',
    insight=True, note='本句是"主句+方式状语从句+让步状语从句"的典型组合,这种"核心论断+方式说明+条件强调"的句式在四六级和考研阅读中高频出现。"asif"虚拟比较和"evenwhen"让步结构都是考点常客。掌握本句的拆解方法可直接迁移到大量同类句式,代表性较强。',
    bold=['tend to treat', 'fellow beings'],
    chunks=[
        dict(role='状语', text='Similarly,',
             note=''),
        dict(role='主语', text='children',
             note=''),
        dict(role='谓语', text='tend to treat robots',
             note=''),
        dict(role='状语从句', text='as if they are fellow beings,',
             note='as if 引导方式状语从句（虚拟比较）'),
        dict(role='状语从句', text='even when they display only simple social signals.',
             note='even when 引导让步状语从句'),
    ])

A['P7S3'] = dict(
    zh='Wiles说:"我们人类似乎对机器着迷，事实证明其他动物也是如此。"',
    insight=True, note='并列句+主语从句的组合在四六级和考研阅读中频繁出现，itturnsout后接从句是典型的形式主语结构。句式具有较强代表性，掌握后可迁移到大量类似句子。',
    bold=['fascinated by', 'it turns out'],
    chunks=[
        dict(role='主语', text='"We humans',
             note=''),
        dict(role='谓语', text='seem to be fascinated by robots,',
             note='seem to do；be fascinated by 对…着迷'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='turns out',
             note=''),
        dict(role='主语从句', text='other animals are too,"',
             note='it turns out (that) ... 形式主语句型；too 代替 fascinated'),
        dict(role='谓语', text='says Wiles.',
             note='倒装引述分句'),
    ])
