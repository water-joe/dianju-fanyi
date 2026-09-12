# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S2'] = dict(
    zh='"一些州要求医生报告，另一些州允许但不强制要求报告，而少数州认为报告属于违反保密义务。',
    insight=True, note='本句涵盖多种成分:宾语补足语(requirephysicianstoreport、considerareportabreach)、条件状语从句、方式状语、therebe句型的主语识别、并列谓语(allowbutdonotmandate),成分种类丰富,且宾补和并列谓语是常见易错点,作为划分成分练习句收益较高。',
    bold=['require physicians to report', 'mandate reports', 'a breach of confidentiality'],
    chunks=[
        dict(role='主语', text='"Some states',
             note=''),
        dict(role='谓语', text='require physicians to report,',
             note='require sb. to do 宾补结构'),
        dict(role='主语', text='others',
             note=''),
        dict(role='谓语', text='allow but do not mandate reports,',
             note='allow 与 do not mandate 并列谓语（but 转折）'),
        dict(role='主语', text='while a few',
             note=''),
        dict(role='谓语', text='consider',
             note=''),
        dict(role='宾语', text='a report',
             note=''),
        dict(role='宾语补足语', text='a breach of confidentiality.',
             note='consider A B「认为 A 是 B」结构'),
    ])

A['P2S3'] = dict(
    zh='"如果医生的行为不符合州法律关于报告和保密的规定，可能会承担责任和处罚。"她建议道。',
    insight=False, note='',
    bold=['liability and penalties', 'in accordance with', 'counseled'],
    chunks=[
        dict(role='主语', text='There',
             note=''),
        dict(role='谓语', text='could be',
             note=''),
        dict(role='主语', text='liability and penalties',
             note='there be 句型真正主语'),
        dict(role='状语从句', text='if a physician does not act in accordance with state laws on reporting and confidentiality,"',
             note='if 引导条件状语从句；in accordance with 依照'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='counseled.',
             note=''),
    ])

A['P3S1'] = dict(
    zh='老年学家Elizabeth Dugan说，保护老年驾驶员安全的部分问题在于，这些困难被不同专业、不同关注点的人员零散地处理，包括老年学家、公路管理官员、汽车工程师等。',
    insight=True, note='覆盖成分丰富：主谓宾、主系表、被动语态、方式状语、by引导的施动者状语、介词短语作定语、动名词短语、列举结构。表语从句和宾语从句的嵌套是易错点，倒装结构也值得练习。适合训练多层从句中成分的准确划分。',
    bold=['Part of the problem', 'addressed piecemeal', 'gerontologist'],
    chunks=[
        dict(role='主语', text='Part of the problem in keeping older drivers safe',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语从句', text='that the difficulties are addressed piecemeal by different professions with different focuses, including gerontologists, highway administration officials, automotive engineers and others,',
             note='that 引导表语从句；are addressed 被动语态；piecemeal 零散地；by... 施动者；including... 列举'),
        dict(role='谓语', text='said',
             note=''),
        dict(role='同位语', text='gerontologist Elizabeth Dugan.',
             note='引述分句倒装；gerontologist 为 Elizabeth Dugan 的同位语'),
    ])

A['P3S2'] = dict(
    zh='"没有一个国家老年驾驶员研究所。"她说。',
    insight=False, note='',
    bold=['National Institute'],
    chunks=[
        dict(role='主语', text='"There',
             note=''),
        dict(role='谓语', text="'s",
             note='there be 句型缩写'),
        dict(role='主语', text='not a National Institute of Older Driver Studies,"',
             note='真正主语'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='said.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='"我们需要更好的证据来说明是什么让驾驶员不安全"以及什么能有所帮助，Dugan说。',
    insight=False, note='',
    bold=['better evidence on', 'what makes drivers unsafe'],
    chunks=[
        dict(role='宾语', text='"We need better evidence on what makes drivers unsafe"',
             note=''),
        dict(role='连接词', text='and',
             note='连接两个 what 从句'),
        dict(role='宾语', text='what can help,',
             note=''),
        dict(role='主语', text='said Dugan.',
             note='倒装引述分句'),
    ])
