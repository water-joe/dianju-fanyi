# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S3'] = dict(
    zh='"我们有一个混合系统，没有备用运力，一旦线路上出现小问题，情况就会变得高度复杂。"他说。',
    insight=True, note='本句的结构非常典型：引述动词后接宾语从句，宾语从句内部用并列连词连接多个分句，其中一个分句又嵌套时间状语从句。这种引述加复合从句的句式在四六级和考研阅读中极为常见，掌握后可直接迁移到大量类似句子。结构代表性强，是值得重点练习的句式。',
    bold=['mixed system', 'spare capacity', 'hiccup'],
    chunks=[
        dict(role='宾语', text='"We have a mixed system, there is no spare capacity and as soon as there\'s a hiccup on the line, the situation becomes highly complex,"',
             note='直接引语；三个并列分句；as soon as 引导时间状语从句'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='said.',
             note=''),
    ])

A['P5S4'] = dict(
    zh='混合系统意味着高速列车在某些路线上或通过大城市时必须在普通轨道上行驶。',
    insight=True, note='"主语+谓语+宾语从句"是四六级和考研阅读中非常常见的句式,宾语从句中嵌套状语从句的结构也是典型的复杂句模式。掌握这种结构后可以大量复用到其他长难句的分析中,具有较高的典型性和迁移价值。',
    bold=['means that', 'regular tracks'],
    chunks=[
        dict(role='主语', text='A mixed system',
             note=''),
        dict(role='谓语', text='means',
             note=''),
        dict(role='宾语从句', text='that high-speed trains must travel on the regular tracks on certain routes or when passing through large cities.',
             note='or 连接 on certain routes 与 when passing... 两个并列状语'),
    ])

A['P5S5'] = dict(
    zh='如果出现拥堵或者例如一辆地方列车发生故障，整个高速铁路网都会受到影响。',
    insight=True, note='条件状语从句+主句的结构在四六级和考研中非常常见，被动语态和并列结构也是高频考点。本句的句式具有很强的代表性，掌握后可以迁移到大量类似句子的分析。',
    bold=['congestion', 'breaks down', 'is affected'],
    chunks=[
        dict(role='状语从句', text="If there's congestion or, for example, a local train breaks down,",
             note='if 引导条件状语从句；or 连接两个并列条件；for example 插入语'),
        dict(role='主语', text='the entire high-speed network',
             note=''),
        dict(role='谓语', text='is affected.',
             note=''),
    ])

A['P6S1'] = dict(
    zh='升级将带来的最重要变化之一是通过建设地下铁路连接线，在某些城市中心将高速线路与普通线路分离。',
    insight=True, note='本句体现了四六级和考研真题中常见的结构特点：主语较长且内嵌定语从句、关系代词省略、主系表结构、介词短语作多重修饰成分。这类结构在阅读理解和翻译题中频繁出现，掌握后可以应对大量同类型长难句。具有较高的典型性和迁移价值。',
    bold=['segregation', 'urban centres', 'underground rail links'],
    chunks=[
        dict(role='主语', text='One of the most important changes the upgrades will bring',
             note='(that) the upgrades will bring 省略关系词的定语从句'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='the segregation of the high-speed line from the regular one in certain urban centres through the construction of underground rail links.',
             note='segregation of A from B 把 A 与 B 分离；through... 介词短语作方式状语'),
    ])

A['P7S1'] = dict(
    zh='专家表示，改善还将来自RFI多年来一直在投资的高密度技术和卫星信号系统。',
    insight=True, note='句子主干识别有一定难度但不极端，嵌套层次适中，时态组合覆盖常考点，成分类型丰富且具有典型性；综合来看，该句作为结构和时态训练材料有较高收益，适合作为中等偏上难度的练习句优先推荐。',
    bold=['high-density technology', 'satellite signalling'],
    chunks=[
        dict(role='主语', text='Improvements',
             note=''),
        dict(role='谓语', text='will also come from',
             note=''),
        dict(role='宾语', text='the high-density technology and satellite signalling that RFI has been investing in for years,',
             note='that... 定语从句（现在完成进行时 has been investing）'),
        dict(role='主语', text='say experts.',
             note='倒装引述分句'),
    ])

A['P7S2'] = dict(
    zh='Giuricin认为，这将使在任何给定时间在同一线路上行驶的高速列车之间的距离得以缩短，这应该意味着运力和交通流畅性的显著提升。',
    insight=True, note='非限制性定语从句补充说明整句内容,是四六级和考研阅读中的高频句式;主句中"allowfor+名词短语(含多层修饰)"的结构也较为典型,学生掌握后可应用于大量科技、政策类文本的理解。',
    bold=['allow for', 'at any given time', 'traffic fluidity'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='will allow for a reduction of the distance between high- speed trains travelling on the same line at any given time,',
             note='allow for 允许；travelling... 现在分词短语作后置定语'),
        dict(role='定语从句', text='which should mean a significant increase in capacity and traffic fluidity,',
             note='which 引导非限制性定语从句'),
        dict(role='状语', text='according to Giuricin.',
             note='信息来源状语'),
    ])
