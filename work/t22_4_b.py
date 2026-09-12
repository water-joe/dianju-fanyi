# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 4 —— P3 至 P4 的成分划分。口径见 t22_4_a.py 头注释。"""

A = {}

A['P3S1'] = dict(
    zh='Schwitzgebel 预测这一干预不会产生效果；他此前发现伦理学教授在一系列行为上与其他教授没有差异，包括投票率、献血和归还图书馆书籍。',
    insight=False, note='',
    bold=['predicted', 'intervention', 'previously', 'differ from', 'blood donation'],
    chunks=[
        dict(role='主语', text='Schwitzgebel'),
        dict(role='谓语', text='predicted'),
        dict(role='宾语', text='the intervention would have no effect',
             note='省略 that 的宾语从句'),
        dict(role='连接词', text=';'),
        dict(role='主语', text='he'),
        dict(role='谓语', text='had previously found'),
        dict(role='宾语', text='that ethics professors do not differ from other professors on a range of behaviors, including voting rates, blood donation and returning library books',
             note='that 引导宾语从句；including... 为介词短语举例'),
    ])

A['P3S2'] = dict(
    zh='但在讨论了肉类伦理的学生受试者中，含肉的餐食购买从 52% 下降到 45%——而且这一效果在研究持续的几周内保持稳定。',
    insight=True,
    note='定语从句修饰主语+并列主句的结构在四六级和考研阅读中高频出现，是典型的学术报道句式，掌握后可迁移到大量类似长句的理解。',
    bold=['among student subjects', 'discussed meat ethics', 'decreased', 'held steady'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='状语', text='among student subjects who discussed meat ethics',
             note='among... 作状语；who 引导定语从句修饰 subjects'),
        dict(role='主语', text='meal purchases containing meat'),
        dict(role='谓语', text='decreased'),
        dict(role='状语', text='from 52 to 45 percent'),
        dict(role='连接词', text='—and'),
        dict(role='主语', text='this effect'),
        dict(role='谓语', text='held steady'),
        dict(role='状语', text='for the study\'s duration of several weeks'),
    ])

A['P3S3'] = dict(
    zh='另一组的购买则保持在 52%。',
    insight=False, note='',
    bold=['remained', 'the other group'],
    chunks=[
        dict(role='主语', text='Purchases from the other group'),
        dict(role='谓语', text='remained'),
        dict(role='表语', text='at 52 percent'),
    ])

A['P4S1'] = dict(
    zh='"对于一个相当小的干预来说，这实际上是一个相当大的效果，"Schwitzgebel 说。',
    insight=False, note='',
    bold=['pretty large', 'pretty small', 'intervention'],
    chunks=[
        dict(role='主语', text='"That'),
        dict(role='谓语', text="'s"),
        dict(role='表语', text='actually a pretty large effect for a pretty small intervention,"',
             note='直接引语整体含主系表'),
        dict(role='谓语', text='Schwitzgebel says', note='引述'),
    ])

A['P4S2'] = dict(
    zh='未参与该研究的宾夕法尼亚大学心理学家 Nina Strohminger 说，她希望这个效果是真实的，但不能排除某些未知的混淆变量。',
    insight=True,
    note='本句的结构非常典型：主句+插入的非限定性定语从句+宾语从句，且宾语从句内部有并列谓语。这种 says 引导宾语从句、宾语从句内部带有转折并列的结构，在四六级和考研真题中极为常见，尤其是科技、学术类文章的引述句式。学生掌握这种结构后，能够快速识别和理解类似的复杂句，迁移性很强。',
    bold=['Psychologist', 'not involved', 'rule out', 'confounding variable'],
    chunks=[
        dict(role='主语', text='Psychologist Nina Strohminger at the University of Pennsylvania'),
        dict(role='定语从句', text='who was not involved in the study',
             note='非限制性定语从句修饰 Nina Strohminger'),
        dict(role='谓语', text='says', note='引述动词'),
        dict(role='宾语', text='she wants the effect to be real but cannot rule out some unknown confounding variable',
             note='says 后省略 that 的宾语从句；but 连接并列谓语 wants / cannot rule out'),
    ])

A['P4S3'] = dict(
    zh='她指出，如果是真实的，它可能会被另一个推动所逆转："来得容易，去得也快。"',
    insight=True,
    note='本句包含插入语、条件状语从句省略结构、情态动词系表结构、方式状语等多种成分，能够训练学习者识别省略、区分插入语与主干、判断状语类型等关键能力，训练价值较高。',
    bold=['if real', 'reversible', 'nudge', 'Easy come, easy go'],
    chunks=[
        dict(role='连接词', text='And'),
        dict(role='状语从句', text='if real', note='条件状语从句省略（= if it is real）'),
        dict(role='主语', text='she'),
        dict(role='谓语', text='notes', note='引述动词'),
        dict(role='主语', text='it'),
        dict(role='谓语', text='might be reversible'),
        dict(role='状语', text='by another nudge'),
        dict(role='同位语', text=': "Easy come, easy go."',
             note='冒号后解释说明 reversible（被逆转）'),
    ])
