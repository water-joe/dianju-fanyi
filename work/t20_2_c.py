# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='认为高CEO薪酬主要是剥削他人的普遍观点并不能很好地解释历史。',
    insight=False, note='',
    bold=['ripping people off'],
    chunks=[
        dict(role='主语', text='The common idea that high CEO pay is mainly about ripping people off',
             note='that 引导同位语从句说明 idea'),
        dict(role='谓语', text="doesn't explain",
             note=''),
        dict(role='宾语', text='history very well.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='从大多数衡量标准来看，自20世纪70年代以来，公司治理已经变得更加严格和规范。',
    insight=False, note='',
    bold=['corporate governance', 'rigorous'],
    chunks=[
        dict(role='状语', text='By most measures,',
             note=''),
        dict(role='主语', text='corporate governance',
             note=''),
        dict(role='谓语', text='has become',
             note=''),
        dict(role='表语', text='a lot tighter and more rigorous',
             note=''),
        dict(role='状语', text='since the 1970s.',
             note=''),
    ])

A['P4S3'] = dict(
    zh='然而正是在这个治理更加严格的时期，CEO薪酬一直处于高位并持续上涨。',
    insight=True, note='强调句型"Itis...that..."是四六级和考研阅读中的高频句式，用于突出特定成分以形成对比或强调。本句的结构非常典型，掌握后可直接迁移到大量类似句子的分析中。',
    bold=['principally'],
    chunks=[
        dict(role='连接词', text='Yet',
             note=''),
        dict(role='强调句', text='it is principally during this period of stronger governance that CEO pay has been high and rising.',
             note='it is... that... 强调句型，强调时间状语'),
    ])

A['P4S4'] = dict(
    zh='这表明招募顶尖候选人来担任日益艰难的工作符合更广泛的公司利益。',
    insight=True, note='本句的结构(主句+宾语从句,宾语从句内使用形式主语it加不定式作真正主语)是考试阅读中的高频句式。形式主语结构和宾语从句省略that都是四六级和考研真题中反复出现的典型语法现象,掌握后可大量复用。',
    bold=['corporate interest', 'tough jobs'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text='suggests',
             note=''),
        dict(role='宾语从句', text='it is in the broader corporate interest to recruit top candidates for increasingly tough jobs.',
             note="it 形式主语；真正主语为 to recruit...；in one's interest 符合…利益"),
    ])

A['P5S1'] = dict(
    zh='此外，最高的CEO薪酬支付给外部候选人，而不是内部亲信人选，这是高CEO薪酬并非以牺牲公司其他部分为代价进行掠夺的另一个迹象。',
    insight=True, note='本句成分丰富且层次清晰:主句包含被动语态谓语、主语、两个并列状语("tooutsidecandidates"和"nottothecozyinsiderpicks")以及同位语;同位语从句内部有系表结构和较长的介词短语作定语;训练价值在于:被动语态中状语的识别(易与宾语混淆)、同位语从句的辨认(易与定语从句混淆)、系表结构中表语范围的划定(介词短语是否属于表语);这些都是学生常见的易错点',
    bold=['cozy insider picks', 'depredation', 'at the expense of'],
    chunks=[
        dict(role='状语', text='Furthermore,',
             note=''),
        dict(role='主语', text='the highest CEO salaries',
             note=''),
        dict(role='谓语', text='are paid to outside candidates, not to the cozy insider picks,',
             note='被动语态；两个并列状语（肯定/否定对照）'),
        dict(role='同位语', text='another sign that high CEO pay is not some kind of depredation at the expense of the rest of the company.',
             note='another sign 为同位语；that... 同位语从句作补充说明；at the expense of 以…为代价'),
    ])

A['P5S2'] = dict(
    zh='而且当公司将CEO薪酬与股价等指标挂钩时，股市会做出积极反应，这表明这些做法不仅为CEO，也为公司建立了企业价值。',
    insight=False, note='',
    bold=['tie CEO pay to', 'build up'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='the stock market',
             note=''),
        dict(role='谓语', text='reacts positively',
             note=''),
        dict(role='状语从句', text='when companies tie CEO pay to, say, stock prices,',
             note='when 引导时间状语从句；tie A to B 把 A 与 B 挂钩；say 为插入语'),
        dict(role='同位语', text='a sign that those practices build up corporate value not just for the CEO.',
             note='a sign 作同位语；that... 同位语从句'),
    ])
