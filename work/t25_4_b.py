# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='一个专门讨论这一现象的Reddit网页拥有近5万名成员，展示了当地欲望路径的图片，这些路径上装饰着指示行人遵守指定人行道的标志，凸显了这些人造小径固有的叛逆性质。',
    insight=True, note='本句时态不难，但结构拆解价值很高，尤其适合训练如何从长修饰中抓住真正主干。对句子结构学习而言，值得优先练习。',
    bold=['devoted to', 'adhere to designated walkways', 'inherent in'],
    chunks=[
        dict(role='主语', text='A Reddit webpage devoted to the phenomenon, boasting nearly 50,000 members,',
             note='devoted to... 过去分词短语作后置定语；boasting... 现在分词短语作补充'),
        dict(role='谓语', text='showcases',
             note=''),
        dict(role='宾语', text='images of local desire paths adorned with signs instructing pedestrians to adhere to designated walkways,',
             note='adorned with... 过去分词短语作后置定语；instructing... 现在分词修饰 signs'),
        dict(role='状语', text='underscoring the rebellious nature inherent in these human-made tracks.',
             note='现在分词作补充说明；inherent in... 形容词短语作后置定语'),
    ])

A['P3S3'] = dict(
    zh='这种冲突凸显了公共空间有机的、用户驱动的演变与对视觉上精心策划和控制的城市环境的渴望之间的持续斗争。',
    insight=True, note='本句包含主语、谓语、宾语、前置定语、后置定语（介词短语），成分种类中等丰富。后置定语内部存在"betweenAandB"并列结构，A和B各自又含多层修饰（"organic,user-drivenevolutionofpublicspaces"和"desireforavisuallycuratedandcontrolledurbanenvironment"），适合练习识别复杂名词短语内部的修饰层次，有一定训练价值。',
    bold=['clash', 'user-driven', 'visually curated'],
    chunks=[
        dict(role='主语', text='This clash',
             note=''),
        dict(role='谓语', text='highlights',
             note=''),
        dict(role='宾语', text='an ongoing struggle between the organic, user-driven evolution of public spaces and the desire for a visually curated and controlled urban environment.',
             note='between A and B 并列结构；两个名词短语各自带多层修饰'),
    ])

A['P4S1'] = dict(
    zh='Wickquasgeck小径是历史欲望路径的一个例子，由美洲原住民创建，用于穿越曼哈顿的森林并在定居点之间快速移动。',
    insight=True, note='主系表结构加后置定语是常见句式，后置定语由过去分词引导也较为典型，在阅读理解中频繁出现。但整体难度偏低，缺少考试中常见的从句嵌套或复杂修饰，代表性中等。',
    bold=['Native Americans', 'settlements'],
    chunks=[
        dict(role='主语', text='The Wickquasgeck Trail',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='an example of a historical desire path,',
             note=''),
        dict(role='状语', text='created by Native Americans to cross the forests of Manhattan and move between settlements quickly.',
             note='过去分词短语作后置定语；to cross... and (to) move... 并列不定式作目的'),
    ])

A['P4S2'] = dict(
    zh='当荷兰殖民者到达时，这条小径被拓宽并建成横跨该岛的主要贸易道路之一，当时被称为de Heere Straat，即绅士街。',
    insight=True, note='本句结构不至于过难，但包含插入从句、被动并列谓语和句尾补充说明，训练收益高而挫败感不强。作为结构与时态练习材料，值得优先学习。',
    bold=['Dutch colonists', 'trade roads'],
    chunks=[
        dict(role='主语', text='This trail,',
             note=''),
        dict(role='状语从句', text='when Dutch colonists arrived,',
             note='when 引导时间状语从句（插入主语后）'),
        dict(role='谓语', text='was widened and made into one of the main trade roads across the island,',
             note='被动并列谓语；make... into 把…建成'),
        dict(role='主语补足语', text="known at the time as de Heere Straat, or Gentlemen's Street.",
             note="known as 被称为；or Gentlemen's Street 同位解释"),
    ])

A['P4S3'] = dict(
    zh='在英国控制纽约后，这条街被重新命名为Broadway。',
    insight=False, note='',
    bold=['renamed'],
    chunks=[
        dict(role='状语', text='Following the British assumption of control in New York,',
             note='following 介词「在…之后」'),
        dict(role='主语', text='the street',
             note=''),
        dict(role='谓语', text='was renamed Broadway.',
             note='被动；Broadway 为主语补足语'),
    ])
