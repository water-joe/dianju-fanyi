# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='近年来，高温行动计划(HAPs)在印度迅速普及。',
    insight=False, note='',
    bold=['proliferating'],
    chunks=[
        dict(role='主语', text='Heat action plans, or HAPs,',
             note='or HAPs 为同位说明'),
        dict(role='谓语', text='have been proliferating',
             note='现在完成进行时；proliferate 激增'),
        dict(role='状语', text='in India in the past few years.',
             note=''),
    ])

A['P1S2'] = dict(
    zh='一般来说，高温行动计划明确规定了官员应何时以及如何发布高温警报并提醒医院和其他机构。',
    insight=True, note='宾语从句由疑问词引导、短语动词作谓语、从句内并列谓语结构,都是四六级和考研阅读中的常见句式,尤其是间接疑问句作宾语的结构出现频率高,学习后可广泛迁移到其他类似句子。',
    bold=['spells out', 'issue heat warnings'],
    chunks=[
        dict(role='状语', text='In general,',
             note='总起状语'),
        dict(role='主语', text='an HAP',
             note=''),
        dict(role='谓语', text='spells out',
             note='spell out 明确说明'),
        dict(role='宾语从句', text='when and how officials should issue heat warnings and alert hospitals and other institutions.',
             note='when and how 引导宾语从句；从句内并列谓语 issue... and alert...'),
    ])

A['P1S3'] = dict(
    zh='例如，那格浦尔的计划要求医院在夏季预留"降温病房"用于治疗中暑患者，并建议建筑商在酷热天气让建筑工人停工休息。',
    insight=True, note='“主语加并列谓语，后接较长补足结构”是说明文和新闻写作里很常见的句式。掌握这种句子后，处理同类的政策、计划、建议类表达会很有迁移性。',
    bold=['calls for', 'set aside', 'heatstroke'],
    chunks=[
        dict(role='主语', text="Nagpur's plan, for instance,",
             note='for instance 插入语'),
        dict(role='谓语', text='calls for hospitals to set aside "cold wards" in the summer for treating heatstroke patients,',
             note='call for sb. to do 要求某人做；for treating... 介词短语作目的'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='advises builders to give construction laborers a break from work on very hot days.',
             note='advise sb. to do 建议某人做；give sb. sth. 双宾结构'),
    ])

A['P2S1'] = dict(
    zh='但根据政策研究中心的一份报告，现有高温行动计划的实施情况参差不齐。',
    insight=False, note='',
    bold=['implementation', 'uneven'],
    chunks=[
        dict(role='主语', text='But implementation of existing HAPs',
             note=''),
        dict(role='谓语', text='has been',
             note='系动词（现在完成时）'),
        dict(role='表语', text='uneven,',
             note=''),
        dict(role='状语', text='according to a report from the Centre for Policy Research.',
             note='信息来源状语'),
    ])

A['P2S2'] = dict(
    zh='报告发现，许多计划缺乏充足的资金。',
    insight=False, note='',
    bold=['adequate funding'],
    chunks=[
        dict(role='主语', text='Many',
             note=''),
        dict(role='谓语', text='lack',
             note=''),
        dict(role='宾语', text='adequate funding,',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='found.',
             note='倒装引述分句'),
    ])

A['P2S3'] = dict(
    zh='而且它们的触发阈值往往没有根据当地气候进行定制。',
    insight=False, note='',
    bold=['triggering thresholds', 'customized to'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='their triggering thresholds',
             note=''),
        dict(role='状语', text='often',
             note=''),
        dict(role='谓语', text='are not customized to the local climate.',
             note='be customized to 按…定制（被动）'),
    ])

A['P2S4'] = dict(
    zh='在某些地区，仅白天的高温就可以作为发布警报的充分触发条件。',
    insight=False, note='',
    bold=['adequate trigger'],
    chunks=[
        dict(role='状语', text='In some areas,',
             note=''),
        dict(role='主语', text='high daytime temperatures alone',
             note='alone 后置修饰，意为「仅…就」'),
        dict(role='谓语', text='might serve as an adequate trigger for alerts.',
             note='serve as 充当、作为'),
    ])
