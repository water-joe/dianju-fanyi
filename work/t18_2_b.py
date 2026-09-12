# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S3'] = dict(
    zh='在世界其他地区引领潮流的同时，尤其是中国和欧洲，美国也正在经历显著的转变。',
    insight=True, note='"While从句+主句"的结构在四六级和考研阅读中较为常见，属于标准的状语从句前置句式。现在进行时表达当前趋势的用法也是典型表达。插入语用法虽不算最高频，但也属于正式书面语的常规手法。整体结构具有较好的代表性和可迁移性。',
    bold=['takes the lead', 'remarkable shift'],
    chunks=[
        dict(role='状语从句', text='While the rest of the world takes the lead,',
             note='while 引导时间状语从句；take the lead 带头'),
        dict(role='插入语', text='notably China and Europe,',
             note='举例插入语'),
        dict(role='主语', text='the United States',
             note=''),
        dict(role='谓语', text='is also seeing',
             note=''),
        dict(role='宾语', text='a remarkable shift.',
             note='现在进行时'),
    ])

A['P3S4'] = dict(
    zh='据美国能源信息署报道，今年3月，风能和太阳能首次占美国发电量的10%以上。',
    insight=True, note='「陈述事实加倒装引述来源」是英语新闻报道的高频句式,在四六级和考研阅读中经常出现。并列主语、短语动词、定语后置都是典型结构。掌握后可以迁移到大量类似新闻句子,代表性较强。',
    bold=['for the first time', 'generated'],
    chunks=[
        dict(role='状语', text='In March,',
             note=''),
        dict(role='插入语', text='for the first time,',
             note=''),
        dict(role='主语', text='wind and solar power',
             note=''),
        dict(role='谓语', text='accounted for',
             note=''),
        dict(role='宾语', text='more than 10 percent of the power generated in the US,',
             note=''),
        dict(role='谓语', text='reported',
             note='倒装引述（reported 前置）'),
        dict(role='主语', text='the US Energy Information Administration.',
             note=''),
    ])

A['P4S1'] = dict(
    zh='Trump总统强调化石燃料——尤其是煤炭——是经济增长的途径。',
    insight=False, note='',
    bold=['underlined', 'the path to'],
    chunks=[
        dict(role='主语', text='President Trump',
             note=''),
        dict(role='谓语', text='has underlined',
             note=''),
        dict(role='宾语', text='fossil fuels – especially coal –',
             note=''),
        dict(role='宾语补足语', text='as the path to economic growth.',
             note='underline A as B 强调 A 是 B'),
    ])

A['P4S2'] = dict(
    zh='在最近于Iowa的一次演讲中，他将风能斥为不可靠的能源来源。',
    insight=False, note='',
    bold=['dismissed', 'unreliable'],
    chunks=[
        dict(role='状语', text='In a recent speech in Iowa,',
             note=''),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='dismissed',
             note=''),
        dict(role='宾语', text='wind power',
             note=''),
        dict(role='宾语补足语', text='as an unreliable energy source.',
             note='dismiss A as B 把 A 贬为 B'),
    ])

A['P4S3'] = dict(
    zh='但这一信息在Iowa并未得到许多人的认同，在那里风力涡轮机遍布田野，提供该州36%的发电量——并且Microsoft等科技巨头正被清洁能源为其数据中心供电的可能性所吸引。',
    insight=True, note='非限制性定语从句修饰地点名词、where引导从句、被动语态、并列谓语等都是四六级和考研阅读中的高频句式。本句结构清晰且典型，学习后可直接迁移到大量真题句子的分析中。',
    bold=['did not play well', 'dot the fields', 'tech giants'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='that message',
             note=''),
        dict(role='谓语', text='did not play well with many in Iowa,',
             note='play well with 得到…认同'),
        dict(role='定语从句', text="where wind turbines dot the fields and provide 36 percent of the state's electricity generation –",
             note='where 引导非限制性定语从句；并列谓语 dot... and provide...'),
        dict(role='定语从句', text='and where tech giants like Microsoft are being attracted by the availability of clean energy to power their data centers.',
             note='第二个并列 where 定语从句；are being attracted 现在进行时被动'),
    ])

A['P5S1'] = dict(
    zh='"当风不吹或太阳不照耀时会发生什么？"这个问题为怀疑者提供了快速反驳。',
    insight=False, note='',
    bold=['put-down for skeptics'],
    chunks=[
        dict(role='主语', text='The question "what happens when the wind doesn\'t blow or the sun doesn\'t shine?"',
             note='引号内为同位语从句'),
        dict(role='谓语', text='has provided',
             note=''),
        dict(role='宾语', text='a quick put-down for skeptics.',
             note='put-down 贬低的话；skeptic 怀疑者'),
    ])
