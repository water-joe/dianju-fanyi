# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='接下来，研究人员将机器困在笼子里，让老鼠有机会通过按压杠杆释放它们。',
    insight=True, note='本句包含双宾语结构（gavetheratstheopportunity）和不定式后置定语（toreleasethem），这两者都是易错点；同时涉及并列谓语、地点状语、方式状语等多种成分，成分种类较为丰富，适合练习成分划分',
    bold=['trapped the robots', 'by pressing a lever'],
    chunks=[
        dict(role='状语', text='Next,',
             note=''),
        dict(role='主语', text='the researchers',
             note=''),
        dict(role='谓语', text='trapped the robots in cages and gave the rats the opportunity to release them',
             note='并列谓语；give sb. sth. 双宾语；to release... 不定式作后置定语'),
        dict(role='状语', text='by pressing a lever.',
             note='by + 动名词表方式'),
    ])

A['P4S2'] = dict(
    zh='在各18次试验中，真老鼠释放社交型机器的可能性平均比释放非社交型机器高52%。',
    insight=False, note='',
    bold=['trials', 'more likely'],
    chunks=[
        dict(role='状语', text='Across 18 trials each,',
             note=''),
        dict(role='主语', text='the living rats',
             note=''),
        dict(role='谓语', text='were 52 percent more likely on average to set the social robot free',
             note='be likely to do；set... free 释放'),
        dict(role='状语', text='than the asocial one.',
             note='than 比较状语'),
    ])

A['P4S3'] = dict(
    zh='Quinn说，这表明老鼠将社交型机器视为真正的社交生物。',
    insight=True, note='主句+宾语从句的结构在四六级和考研阅读中非常常见,perceive...as...也是高频考查的动词短语结构。末尾的引述标记says+人名是学术文本的典型表达方式。这个句式具有较高的迁移价值,掌握后可应用于大量类似句子。',
    bold=['perceived', 'genuine social being'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='suggests',
             note=''),
        dict(role='宾语从句', text='that the rats perceived the social robot as a genuine social being,',
             note='perceive A as B 把 A 视为 B'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Quinn.',
             note='引述分句（says 前置倒装）'),
    ])

A['P4S4'] = dict(
    zh='老鼠可能与社交型机器建立了更深的联系，因为它表现出了诸如共同探索和玩耍等行为。',
    insight=True, note='“主句＋because引导的原因状语从句”是很常见、可迁移性很强的句式。再加上主句里的情态动词结构，也很符合考试阅读中常见的判断与解释表达。',
    bold=['bonded', 'communal exploring'],
    chunks=[
        dict(role='主语', text='The rats',
             note=''),
        dict(role='谓语', text='may have bonded more with the social robot',
             note='may have done 情态+完成时；bond with 与…建立情感联系'),
        dict(role='状语从句', text='because it displayed behaviors like communal exploring and playing.',
             note='because 引导原因状语从句；like... 举例'),
    ])

A['P4S5'] = dict(
    zh='她说，这可能导致老鼠更好地记住之前曾释放过它，并希望当自己被困时机器能够回报这份恩惠。',
    insight=True, note='本句成分丰富且层次分明：主句包含情态动词谓语、动名词复合结构作宾语、并列动名词、完成式动名词、不定式复合结构；从句包含时间状语从句的识别。涵盖多种非谓语动词形式、并列结构、复杂宾语以及从句嵌套，是训练成分划分和层次分析的优质材料。',
    bold=['return the favour', 'get trapped'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='could lead to',
             note=''),
        dict(role='宾语', text='the rats better remembering having freed it earlier, and wanting the robot to return the favour when they get trapped,',
             note='two 并列动名词短语；better remembering having freed 完成式动名词；want sth. to do 复合结构；when 引导时间状语从句'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P5S1'] = dict(
    zh='Quinn说:"研究表明，老鼠会参与多种形式的互惠帮助和合作，包括所谓的直接互惠，即一只老鼠会帮助曾经帮助过自己的另一只老鼠。"',
    insight=True, note='句中覆盖主语、谓语、宾语、表语、宾语从句、定语从句（两层嵌套）、状语、主语补语等多种成分，并且包含融合型关系代词（what）、关系副词（where）、关系代词（that）三种从句引导词的典型用法，适合全面练习成分划分。',
    bold=['reciprocal help', 'direct reciprocity'],
    chunks=[
        dict(role='宾语', text='"Rats have been shown to engage in multiple forms of reciprocal help and cooperation,',
             note='直接引语；have been shown to do 被动结构'),
        dict(role='宾语', text='including what is referred to as direct reciprocity',
             note='what 引导宾语从句作介词宾语'),
        dict(role='定语从句', text='where a rat will help another rat that has previously helped them,"',
             note='where 引导定语从句修饰 reciprocity；that... 定语从句修饰 rat'),
        dict(role='谓语', text='says Quinn.',
             note='倒装引述分句'),
    ])
