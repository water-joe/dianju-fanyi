# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S5'] = dict(
    zh='雇主们注意到了这一点并采取了行动。',
    insight=False, note='',
    bold=['taking note'],
    chunks=[
        dict(role='主语', text='Employers',
             note=''),
        dict(role='谓语', text='are taking note and taking action.',
             note='并列现在进行时谓语；take note 注意到'),
    ])

A['P2S6'] = dict(
    zh='根据我们的研究，25%的雇主决定完全禁止AI或规范其在组织内的使用。',
    insight=False, note='',
    bold=['outright ban', 'regulate'],
    chunks=[
        dict(role='状语', text='According to our research,',
             note=''),
        dict(role='主语', text='25%',
             note=''),
        dict(role='谓语', text='have decided to either outright ban AI or regulate its use within their organisations.',
             note='either... or... 并列不定式'),
    ])

A['P2S7'] = dict(
    zh='但即使有这些政策，一些员工仍选择违反规定。',
    insight=False, note='',
    bold=['in place', 'break the rules'],
    chunks=[
        dict(role='状语', text='But even with these policies in place,',
             note='in place 后置修饰 policies（就位的）'),
        dict(role='主语', text='some employees',
             note=''),
        dict(role='谓语', text='choose to break the rules.',
             note=''),
    ])

A['P2S8'] = dict(
    zh='他们有自己的理由——约63%的员工报告称使用AI提高了他们的生产力，有些人甚至觉得AI比他们的人类同事提供更多帮助。',
    insight=True, note='本句的"主句+破折号+并列主句(各带宾语从句)"结构在四六级和考研阅读中非常常见,尤其是用破折号或冒号来补充解释前文的写法,以及多个并列主句通过and连接、各自带宾语从句展开的平行结构,都是典型的学术或新闻文体句式,学习价值较高',
    bold=['productivity', 'human colleagues'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='have their reasons —',
             note=''),
        dict(role='主语', text='around 63% of them',
             note=''),
        dict(role='谓语', text='report',
             note=''),
        dict(role='宾语从句', text='that using AI increases their productivity,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='some',
             note=''),
        dict(role='谓语', text='even feel',
             note=''),
        dict(role='宾语从句', text='AI offers more help than their human colleagues.',
             note='省略 that 的宾语从句；than 比较结构'),
    ])

A['P3S1'] = dict(
    zh='这种情况需要在利用AI提高生产力和冒机密数据泄露风险之间保持微妙的平衡。',
    insight=False, note='',
    bold=['delicate balance', 'leveraging', 'data exposure'],
    chunks=[
        dict(role='主语', text='The situation',
             note=''),
        dict(role='谓语', text='presents',
             note=''),
        dict(role='宾语', text='a delicate balance between leveraging AI for its productivity gains and risking confidential data exposure.',
             note='between A and B：两个并列动名词短语'),
    ])

A['P3S2'] = dict(
    zh='雇主需要像管理任何其他形式的数据共享或存储一样谨慎地管理AI工具。',
    insight=True, note='thesame...as比较结构在四六级和考研阅读中频繁出现,且本句将比较结构嵌入方式状语的用法也较为典型,学生掌握后可迁移到大量类似句式,具有较高的代表性和实用性',
    bold=['with the same level of care'],
    chunks=[
        dict(role='主语', text='Employers',
             note=''),
        dict(role='谓语', text='need to manage AI tools',
             note=''),
        dict(role='状语', text='with the same level of care as any other form of data sharing or storage.',
             note='the same... as... 比较结构'),
    ])
