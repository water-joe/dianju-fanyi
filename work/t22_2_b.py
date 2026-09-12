# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 2 —— P4 至 P5 的成分划分。口径见 t22_2_a.py 头注释。"""

A = {}

A['P4S1'] = dict(
    zh='"退休的概念正在演变，"TD Ameritrade 退休业务高级经理 Christine Russell 说。',
    insight=False, note='',
    bold=['evolving', 'senior manager'],
    chunks=[
        dict(role='主语', text='"The concept of retirement is evolving,"', note='直接引语，含主语与谓语'),
        dict(role='谓语', text='said', note='引述动词'),
        dict(role='主语', text='Christine Russell, senior manager of retirement at TD Ameritrade',
             note='引述主语；senior manager... 为同位语'),
    ])

A['P4S2'] = dict(
    zh='"这不仅仅关乎财务。', insight=False, note='',
    bold=['finances'],
    chunks=[
        dict(role='主语', text='"It\'s'),
        dict(role='状语', text='not just about finances.', note='介词短语作表语'),
    ])

A['P4S3'] = dict(
    zh='工作的价值也在驱使人们在退休后继续工作。"',
    insight=False, note='',
    bold=['driving', 'past retirement'],
    chunks=[
        dict(role='主语', text='The value of work'),
        dict(role='谓语', text='is also driving'),
        dict(role='宾语', text='folks'),
        dict(role='状语', text='to continue working past retirement."',
             note='不定式作宾语补足语'),
    ])

A['P5S1'] = dict(
    zh='退休模式改变的一个原因是：美国人的寿命更长了。',
    insight=False, note='',
    bold=['patterns', 'living longer'],
    chunks=[
        dict(role='主语', text='One reason for the change in retirement patterns'),
        dict(role='同位语', text=': Americans are living longer.', note='冒号后解释 reason 的内容'),
    ])

A['P5S2'] = dict(
    zh='根据美国人口普查局的数据，2018 年 65 岁及以上人口占总人口的 16%，比上年增长了 32%。',
    insight=True,
    note='主系表结构加介词短语修饰是英语中的高频基础句式，在数据报告、说明文等文体中极为常见，具有较强的代表性和实用性。',
    bold=['The share of the population', 'up 32%', 'the prior year'],
    chunks=[
        dict(role='主语', text='The share of the population 65 and older'),
        dict(role='谓语', text='was'),
        dict(role='表语', text='16% in 2018, up 32% from the prior year',
             note='up 32%... 为补充说明的状语短语'),
        dict(role='状语', text='according to the U.S.', note='according to... 作依据状语'),
    ])

A['P5S3'] = dict(
    zh='Census Bureau.',
    insight=False, note='',
    bold=['Census Bureau'],
    chunks=[
        dict(role='主语', text='Census Bureau.', note='原始切句把 U.S. Census Bureau 拆成两句，此处仅余碎片'),
    ])

A['P5S4'] = dict(
    zh='这也比 2010 年增长了 30.2%。',
    insight=True,
    note='主系表结构是常见基础句式，但本句使用 up 作表语较为口语化，不如 be+形容词/名词典型，代表性中等。',
    bold=['That', 'up 30.2%', 'since 2010'],
    chunks=[
        dict(role='主语', text="That's", note='That is 缩略'),
        dict(role='表语', text='also up 30.2% since 2010', note='up 作表语，since 2010 为时间状语'),
    ])

A['P5S5'] = dict(
    zh='老年美国人也是美国劳动力中增长最快的群体，而婴儿潮一代预计会比前几代人更长寿。',
    insight=False, note='',
    bold=['fastest-growing', 'segment', 'boomers', 'previous generations'],
    chunks=[
        dict(role='主语', text='Older Americans'),
        dict(role='谓语', text='are also'),
        dict(role='表语', text='the fastest-growing segment of the US workforce'),
        dict(role='连接词', text='and'),
        dict(role='主语', text='boomers'),
        dict(role='谓语', text='are expected', note='被动语态'),
        dict(role='状语', text='to live longer than previous generations',
             note='不定式作主语补足语'),
    ])

A['P5S6'] = dict(
    zh='过去三十年里，退休年龄人口在劳动力中的比例翻了一番。',
    insight=False, note='',
    bold=['has doubled', 'over the past three decades'],
    chunks=[
        dict(role='主语', text='The percentage of retirement-age people in the labor force'),
        dict(role='谓语', text='has doubled'),
        dict(role='状语', text='over the past three decades'),
    ])

A['P5S7'] = dict(
    zh='据资产管理公司 United Income 的数据，2 月份约有 20% 的 65 岁及以上人口在劳动力队伍中，高于 1985 年 1 月 10% 的历史最低水平。',
    insight=False, note='',
    bold=['in the workforce', 'all-time low'],
    chunks=[
        dict(role='主语', text='About 20% of people 65 and older'),
        dict(role='谓语', text='were'),
        dict(role='表语', text='in the workforce in February'),
        dict(role='状语', text='up from an all-time low of 10% in January 1985',
             note='up from... 比较状语'),
        dict(role='状语', text='according to money manager United Income', note='依据状语'),
    ])
