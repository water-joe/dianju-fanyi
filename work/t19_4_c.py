# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S3'] = dict(
    zh='还有基于激励的方式使更好的环境选择变得更容易，例如确保回收至少与垃圾处理一样容易。',
    insight=False, note='',
    bold=['incentive-based', 'trash disposal'],
    chunks=[
        dict(role='谓语', text='There are also',
             note=''),
        dict(role='主语', text='incentive-based ways of making better environmental choices easier,',
             note='there be 句型真正主语；make A easier 宾补'),
        dict(role='同位语', text='such as ensuring recycling is at least as easy as trash disposal.',
             note='such as 举例；ensuring 后接省略 that 的宾语从句；as... as... 比较'),
    ])

A['P7S1'] = dict(
    zh='DeSombre并不是说人们应该停止关心环境。',
    insight=True, note='say后接省略that的宾语从句是四六级和考研阅读中的高频结构,且从句内情态动词+动词原形的搭配也很常见。掌握后可广泛迁移到其他say/think/believe等动词的句式。',
    bold=["isn't saying", 'caring about'],
    chunks=[
        dict(role='主语', text='DeSombre',
             note=''),
        dict(role='谓语', text="isn't saying",
             note=''),
        dict(role='宾语从句', text='people should stop caring about the environment.',
             note='省略 that 的宾语从句；stop doing 停止做'),
    ])

A['P7S2'] = dict(
    zh='她说，只是个人行动太慢了，不能成为改变广泛行为的唯一甚至主要方法。',
    insight=True, note='这句时态不难，能把注意力集中到主干识别和成分划分上，训练收益较高。对需要突破长句读法的学习者来说，属于值得优先练的结构型材料。',
    bold=['too slow', 'widespread behavior'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text="'s just that",
             note=''),
        dict(role='表语从句', text='individual actions are too slow,',
             note='that 引导表语从句；too... to... 结构'),
        dict(role='插入语', text='she says,',
             note=''),
        dict(role='状语', text='for that to be the only, or even primary, approach to changing widespread behavior.',
             note='for... to be... 不定式复合结构表结果；approach to doing'),
    ])

A['P8S1'] = dict(
    zh='所有这些都不是要否定个人。',
    insight=False, note='',
    bold=['writing off'],
    chunks=[
        dict(role='主语', text='None of this',
             note=''),
        dict(role='谓语', text='is about',
             note=''),
        dict(role='宾语', text='writing off the individual.',
             note='write off 否定、一笔勾销'),
    ])

A['P8S2'] = dict(
    zh='这只是关乎正确看待事物。',
    insight=False, note='',
    bold=['putting things into perspective'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text="'s just about",
             note=''),
        dict(role='宾语', text='putting things into perspective.',
             note='put... into perspective 正确看待'),
    ])

A['P8S3'] = dict(
    zh='我们没有时间等待。',
    insight=False, note='',
    bold=["don't have time to wait"],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text="don't have time",
             note=''),
        dict(role='状语', text='to wait.',
             note='不定式作后置定语'),
    ])

A['P8S4'] = dict(
    zh='我们需要塑造集体行动(并约束污染企业)的进步政策，以及推动变革的积极公民。',
    insight=True, note='主句+限制性定语从句+介词短语状语是四六级和考研阅读中高频出现的句式组合；定语从句修饰宾语、关系代词在从句中作主语、从句内并列谓语、分词作后置定语等都是考试常考结构；整体句式具有较强的代表性和可迁移性，掌握后能应对大量类似句子。',
    bold=['progressive policies', 'rein in', 'engaged citizens'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text='need',
             note=''),
        dict(role='宾语', text='progressive policies that shape collective action (and rein in polluting businesses), alongside engaged citizens pushing for change.',
             note='that... 定语从句修饰 policies（括号内为并列谓语）；alongside... 介词短语作伴随状语；pushing for... 现在分词作后置定语'),
    ])
