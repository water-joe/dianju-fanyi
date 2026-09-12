# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S6'] = dict(
    zh='现在超过一半。',
    insight=False, note='',
    bold=['more than half'],
    chunks=[
        dict(role='状语', text='Now',
             note=''),
        dict(role='主语', text='more than half',
             note=''),
        dict(role='谓语', text='are.',
             note='承前省略 over the age of 35'),
    ])

A['P3S7'] = dict(
    zh='而且采摘农作物对年长的身体来说很艰难。',
    insight=False, note='',
    bold=['picking crops is hard on'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='picking crops',
             note='动名词短语作主语'),
        dict(role='谓语', text='is hard',
             note=''),
        dict(role='状语', text='on older bodies.',
             note='be hard on 对…很艰难'),
    ])

A['P3S8'] = dict(
    zh='对于这种劳动力短缺，一个经常被辩论的解决方案仍然像一直以来那样不切实际:本土美国工人不会回到农场。',
    insight=False, note='',
    bold=['oft- debated', 'implausible'],
    chunks=[
        dict(role='主语', text='One oft- debated cure for this labor shortage',
             note=''),
        dict(role='谓语', text='remains',
             note=''),
        dict(role='表语', text="as implausible as it's been all along:",
             note=''),
        dict(role='同位语从句', text="Native U.S. workers won't be returning to the farm.",
             note='冒号后为同位语从句，说明 cure 的内容'),
    ])

A['P4S1'] = dict(
    zh='机械化也不是答案——至少目前还不是。',
    insight=False, note='',
    bold=['Mechanization', 'not yet'],
    chunks=[
        dict(role='主语', text='Mechanization',
             note=''),
        dict(role='谓语', text="isn't",
             note=''),
        dict(role='表语', text='the answer, either – not yet, at least.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='玉米、棉花、水稻、大豆和小麦的生产已经基本实现机械化，但许多高价值、劳动密集型作物，如草莓，需要劳动力。',
    insight=False, note='',
    bold=['labor-intensive', 'strawberries'],
    chunks=[
        dict(role='主语', text='Production of corn, cotton, rice, soybeans, and wheat',
             note=''),
        dict(role='谓语', text='has been largely mechanized,',
             note='现在完成时被动'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='many high-value, labor-intensive crops, such as strawberries,',
             note=''),
        dict(role='谓语', text='need',
             note=''),
        dict(role='宾语', text='labor.',
             note=''),
    ])

A['P4S3'] = dict(
    zh='即使是奶牛场，机器人只完成一小部分挤奶工作，离自动化还有很长的路要走。',
    insight=True, note='句子结构在四六级和考研阅读中具有较高代表性：主句中插入非限制性定语从句、末尾附加时间状语从句的组合模式常见；"havealongwaytogo"是常考的习惯表达；"before"引导的时间状语从句用一般现在时代替将来时的"主将从现"原则也是常考语法点。掌握本句结构后可迁移到大量类似句式。',
    bold=['dairy farms', 'a long way to go', 'automated'],
    chunks=[
        dict(role='状语', text='Even',
             note=''),
        dict(role='主语', text='dairy farms,',
             note=''),
        dict(role='定语从句', text='where robots do a small share of milking,',
             note='where 引导非限制性定语从句（插入）'),
        dict(role='谓语', text='have a long way to go',
             note=''),
        dict(role='状语从句', text="before they're automated.",
             note='before 引导时间状语从句；主将从现'),
    ])

A['P5S1'] = dict(
    zh='因此，农场越来越依赖使用H-2A签证的临时客工来填补劳动力缺口。',
    insight=True, note='本句是典型的"主语+系动词+表语"结构，系动词grow表示状态变化，表语中包含形容词加介词短语以及分词定语和不定式状语，这种层层修饰的表语结构在四六级和考研阅读中非常常见。句首的结果状语"Asaresult"也是真题中高频的衔接表达。掌握本句的分析方法可以迁移到大量类似的"主系表+修饰成分"句型中。',
    bold=['reliant on', 'guest workers', 'fill the gaps'],
    chunks=[
        dict(role='状语', text='As a result,',
             note=''),
        dict(role='主语', text='farms',
             note=''),
        dict(role='谓语', text='have grown increasingly reliant on',
             note=''),
        dict(role='宾语', text='temporary guest workers using the H-2A visa to fill the gaps in the workforce.',
             note='using... 现在分词作后置定语；to fill... 不定式作目的状语'),
    ])

A['P5S2'] = dict(
    zh='大约从2012年开始，签证申请急剧上升；从2011年到2016年，签证发放数量增加了一倍多。',
    insight=True, note='分号连接两个主句、句首放时间范围、名词后接分词作后置修饰，这些都属于常见书面说明文结构。掌握这种读法后，处理数据描述类句子很有迁移性。',
    bold=['rose sharply', 'more than doubled'],
    chunks=[
        dict(role='状语', text='Starting around 2012,',
             note=''),
        dict(role='主语', text='requests for the visas',
             note=''),
        dict(role='谓语', text='rose sharply;',
             note=''),
        dict(role='状语', text='from 2011 to 2016',
             note=''),
        dict(role='主语', text='the number of visas issued',
             note=''),
        dict(role='谓语', text='more than doubled.',
             note='issued 过去分词作后置定语；double v. 翻倍'),
    ])

A['P6S1'] = dict(
    zh='H-2A签证没有数量上限，不像用于非农业工作的H-2B签证，后者每年限制在66000个。',
    insight=False, note='',
    bold=['numerical cap', 'limited to'],
    chunks=[
        dict(role='主语', text='The H-2A visa',
             note=''),
        dict(role='谓语', text='has',
             note=''),
        dict(role='宾语', text='no numerical cap,',
             note=''),
        dict(role='状语', text='unlike the H-2B visa for nonagricultural work,',
             note='unlike 介词短语作对比状语'),
        dict(role='定语从句', text='which is limited to 66,000 a year.',
             note='which 引导非限制性定语从句；be limited to 限于'),
    ])
