# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S1'] = dict(
    zh='在其他弱点之中，当城市被迫独自应对污浊空气时必须采用的措施在政治上具有争议性，因此容易受到攻击。',
    insight=True, note='本句成分丰富且具有典型易错点：主句包含主系表结构和并列表语；定语从句中关系词省略（作宾语）；状语从句中主语和be动词省略；还涉及宾语补足语"totackle"的识别。这些都是学习者容易混淆的成分，适合作为划分练习的优质材料。',
    bold=['vulnerable', 'tackle'],
    chunks=[
        dict(role='状语', text='Among other weaknesses,',
             note=''),
        dict(role='主语', text='the measures cities must employ when left to tackle dirty air on their own',
             note='(that) cities must employ 省略关系词的定语从句；when (they are) left to... 省略主语和 be 的状语从句'),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='politically controversial, and therefore vulnerable.',
             note='两个并列表语'),
    ])

A['P3S2'] = dict(
    zh='这是因为这些措施不可避免地将清洁空气的成本转嫁到个人驾驶者身上——他们必须支付费用或购买更好的车辆——而不是转嫁到汽车制造商身上，而制造商的作弊行为才是我们有毒污染的真正原因。',
    insight=True, note='本句包含多个四六级和考研常见结构:主系表+表语从句、ratherthan对比、非限制性定语从句用破折号隔开、whose引导的限制性定语从句、put...onto短语。这些结构在议论文和说明文中频繁出现,尤其ratherthan对比和whose定语从句是高频考点。句式典型,掌握后可迁移到大量类似长难句。',
    bold=['inevitably', 'rather than', 'toxic pollution'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text="'s",
             note=''),
        dict(role='状语从句', text='because they inevitably put the costs of cleaning the air on to individual drivers—who must pay fees or buy better vehicles—rather than on to the car manufacturers whose cheating is the real cause of our toxic pollution.',
             note='because 引导原因状语从句；破折号内为非限制性定语从句；rather than 对比；whose... 定语从句修饰 manufacturers'),
    ])

A['P3S3'] = dict(
    zh='不难想象伦敦也会发生类似的逆转。',
    insight=False, note='',
    bold=['reversal'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text="'s not hard",
             note=''),
        dict(role='真正主语', text='to imagine a similar reversal happening in London.',
             note='不定式短语作真正主语；happening... 现在分词作宾补'),
    ])

A['P3S4'] = dict(
    zh='新的超低排放区(Ulez)很可能成为明年市长选举的一个重大议题。',
    insight=False, note='',
    bold=['ultra-low emission zone', 'mayoral election'],
    chunks=[
        dict(role='主语', text='The new ultra-low emission zone (Ulez)',
             note=''),
        dict(role='谓语', text='is likely to be',
             note=''),
        dict(role='表语', text="a big issue in next year's mayoral election.",
             note=''),
    ])

A['P3S5'] = dict(
    zh='如果Sadiq Khan获胜并按照他的计划在2021年将其扩展到北环路和南环路，这必将引发数量多得多的驾车者的强烈反对，因为届时他们将受到影响。',
    insight=True, note='条件状语从句+主句+定语从句的组合是四六级和考研阅读中的高频句式。条件从句内嵌套方式从句的结构也很常见。整句体现了新闻报道或学术文章中典型的复杂句式：先交代条件，再陈述结果，最后补充受影响对象的细节。这种结构的掌握对理解大多数英文长难句都有帮助。',
    bold=['spark intense opposition', 'motorists'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='状语从句', text='if Sadiq Khan wins and extends it to the North and South Circular roads in 2021 as he intends,',
             note='if 引导条件状语从句；as he intends 方式状语从句'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='is sure to spark',
             note=''),
        dict(role='宾语', text='intense opposition from the far larger number of motorists who will then be affected.',
             note='who... 定语从句修饰 motorists'),
    ])

A['P4S1'] = dict(
    zh='这并不是说像伦敦的Ulez这样的措施毫无用处。',
    insight=False, note='',
    bold=['useless'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text="'s not",
             note=''),
        dict(role='表语从句', text="that measures such as London's Ulez are useless.",
             note='that 引导表语从句'),
    ])

A['P4S2'] = dict(
    zh='恰恰相反。',
    insight=False, note='',
    bold=['Far from it'],
    chunks=[
        dict(role='表语', text='Far from it.',
             note='省略句，意为「远非如此」'),
    ])

A['P4S3'] = dict(
    zh='地方官员正在使用他们可用的手段，在面对严重威胁时保护居民的健康。',
    insight=True, note='主句+限制性定语从句+目的状语+介词短语状语的组合是四六级和考研阅读中常见的句式。定语从句修饰宾语、不定式表目的均为高频考点，学习后可迁移至大量类似句子。',
    bold=['levers', 'safeguard', 'in the face of'],
    chunks=[
        dict(role='主语', text='Local officials',
             note=''),
        dict(role='谓语', text='are using',
             note=''),
        dict(role='宾语', text='the levers that are available to them',
             note='that... 定语从句修饰 levers'),
        dict(role='状语', text="to safeguard residents' health in the face of a serious threat.",
             note='不定式作目的状语；in the face of 面对'),
    ])
