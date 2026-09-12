# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='在我们城市空间中有序的人行道和公园之外，欲望路径是社区的非官方足迹，揭示了人类未言明的偏好、共同的捷径和集体的选择。',
    insight=False, note='',
    bold=['desire paths', 'unofficial footprints', 'unspoken preferences'],
    chunks=[
        dict(role='状语', text='Navigating beyond the organised pavements and parks of our urban spaces,',
             note='现在分词短语作状语'),
        dict(role='主语', text='desire paths',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='the unofficial footprints of a community,',
             note=''),
        dict(role='状语', text='revealing the unspoken preferences, shared shortcuts and collective choices of humans.',
             note='现在分词短语作补充说明；三个并列名词短语作 revealing 的宾语'),
    ])

A['P1S2'] = dict(
    zh='这些路径常常表现为穿过整洁绿地的踩踏泥土小径，这些集体违规的路线抄近路、横穿草坪、翻越小山，代表了人类(和动物)从A点到B点最有效移动的自然能力。',
    insight=True, note='本句包含并列谓语结构、前置和后置分词短语作状语、介词短语作后置定语等多种成分类型,覆盖面较广;句首和句末的分词短语容易被误判为独立分句或谓语,是练习区分谓语与非谓语、理解分词短语作状语的良好材料;同时并列谓语各自带宾语的结构也值得练习。',
    bold=['trodden dirt tracks', 'collective disobedience', 'cut corners'],
    chunks=[
        dict(role='状语', text='Often appearing as trodden dirt tracks through otherwise neat green spaces,',
             note='现在分词短语作状语；otherwise 否定 green spaces（「本该整洁的」）'),
        dict(role='主语', text='these routes of collective disobedience',
             note=''),
        dict(role='谓语', text='cut corners, bisect lawns and cross hills,',
             note='三个并列谓语'),
        dict(role='状语', text='representing the natural capability of people (and animals) to go from point A to point B most effectively.',
             note='现在分词短语作补充说明；to go... 不定式作 capability 的后置定语'),
    ])

A['P2S1'] = dict(
    zh='城市规划者将欲望路径解读为不仅仅是便捷的捷径；它们提供了关于规划与行为之间动态关系的宝贵见解。',
    insight=True, note='“分号连接两个完整陈述+一般现在时讲普遍事实”是较常见的说明文句式。第一个分句中的“动词+宾语+补足语”也属于常见、值得迁移的结构。',
    bold=['interpret', 'valuable insights', 'dynamics'],
    chunks=[
        dict(role='主语', text='Urban planners',
             note=''),
        dict(role='谓语', text='interpret desire paths as more than just convenient shortcuts;',
             note='interpret A as B 把 A 解读为 B'),
        dict(role='主语', text='they',
             note='分号后第二个分句主语'),
        dict(role='谓语', text='offer',
             note=''),
        dict(role='宾语', text='valuable insights into the dynamics between planning and behaviour.',
             note='insights into 关于…的见解'),
    ])

A['P2S2'] = dict(
    zh='俄亥俄州立大学允许其学生自由穿行校园中心的椭圆形草坪，然后铺设这些欲望路径，创建了学生已经建立的有效路线网络。',
    insight=True, note='主句包含并列谓语、宾语、宾语补足语、同位语、方式状语、时间状语、伴随状语等多种成分,成分种类丰富;定语从句省略关系代词,是常见易错点;不定式tonavigate和topave分别作宾语补足语和动词宾语,todo的多重用法值得练习。整体覆盖面广,训练价值较高。',
    bold=['the Oval', 'pave'],
    chunks=[
        dict(role='主语', text='Ohio State University',
             note=''),
        dict(role='谓语', text='allowed its students to navigate the Oval, a lawn in the centre of campus, freely,',
             note='allow sb. to do 宾补结构；a lawn... 同位语；freely 方式状语'),
        dict(role='连接词', text='then',
             note=''),
        dict(role='谓语', text='proceeded to pave the desire paths,',
             note='proceed to do 接着做'),
        dict(role='状语', text='creating a web of effective routes students had established.',
             note='现在分词作结果状语；(that) students had established 省略关系词的定语从句'),
    ])

A['P3S1'] = dict(
    zh='然而，其他规划者仍然不愿将欲望路径纳入正式规划，理由是对安全、环境影响，或主要是美观的担忧。',
    insight=True, note='本句时态不难，但结构上很适合练主干识别和非谓语辨认，训练收益较稳定。对于需要巩固“一个谓语配多个后置补充”的学习者，优先度较高。',
    bold=['reluctance', 'integrate', 'aesthetics'],
    chunks=[
        dict(role='状语', text='Yet,',
             note=''),
        dict(role='主语', text='reluctance persists among other planners to integrate desire paths into formal plans,',
             note='persist 持续存在；to integrate... 不定式作 reluctance 的后置定语'),
        dict(role='状语', text='citing concerns about safety, environmental impact, or primarily, aesthetics.',
             note='现在分词短语作原因状语'),
    ])
