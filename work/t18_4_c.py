# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P7S1'] = dict(
    zh='他认为:"闲散不仅仅是假期、放纵或恶习；它对大脑来说就像维生素D对身体一样不可或缺……[闲散]自相矛盾地是完成任何工作所必需的。"',
    insight=False, note='',
    bold=['indispensable', 'paradoxically'],
    chunks=[
        dict(role='主语', text='"Idleness',
             note=''),
        dict(role='谓语', text='is not just',
             note=''),
        dict(role='表语', text='a vacation, an indulgence or a vice;',
             note=''),
        dict(role='谓语', text='it is',
             note=''),
        dict(role='表语', text='as indispensable to the brain as vitamin D is to the body…[idleness] is, paradoxically, necessary to getting any work done,"',
             note='as... as... 比较结构；paradoxically 自相矛盾地'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='argues.',
             note=''),
    ])

A['P8S1'] = dict(
    zh='哈佛医学院精神病学助理教授Srini Pillay认为，休息时间与生产力之间这种违反直觉的联系可能源于我们大脑的运作方式。',
    insight=True, note='本句的结构在四六级和考研阅读中较为常见:主句+宾语从句+定语从句的组合是典型的学术陈述句式,同位语对人物身份的说明、宾语从句引导词的省略、定语从句修饰抽象名词(theway)等都是真题中高频出现的句式特征',
    bold=['counterintuitive', 'productivity', 'operate'],
    chunks=[
        dict(role='主语', text='Srini Pillay,',
             note=''),
        dict(role='同位语', text='an assistant professor of psychiatry at Harvard Medical School,',
             note=''),
        dict(role='谓语', text='believes',
             note=''),
        dict(role='宾语从句', text='this counterintuitive link between downtime and productivity may be due to the way our brains operate.',
             note='省略 that 的宾语从句；(in which) our brains operate 省略关系词的定语从句修饰 way'),
    ])

A['P8S2'] = dict(
    zh='当我们的大脑在专注和不专注于某项任务之间切换时，它们往往会更有效率。',
    insight=False, note='',
    bold=['switch between', 'more efficient'],
    chunks=[
        dict(role='状语从句', text='When our brains switch between being focused and unfocused on a task,',
             note='when 引导时间状语从句；between 后接两个并列动名词'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='tend to be',
             note=''),
        dict(role='表语', text='more efficient.',
             note='tend to be 往往…'),
    ])

A['P9S1'] = dict(
    zh='Pillay说:"人们没有意识到的是，为了完成这些任务，他们需要同时使用大脑中的专注和非专注回路。"',
    insight=False, note='',
    bold=['circuits', 'in order to complete'],
    chunks=[
        dict(role='主语从句', text='"What people don\'t realise is',
             note='what 引导主语从句'),
        dict(role='表语从句', text='that in order to complete these tasks they need to use both the focus and unfocus circuits in their brain,"',
             note='that 引导表语从句；in order to 目的状语；both... and... 并列'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Pillay.',
             note=''),
    ])
