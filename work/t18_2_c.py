# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S2'] = dict(
    zh='但电池储能容量的提升使其全天候保持电力流动的能力更有可能实现。',
    insight=False, note='',
    bold=['storage capacity', 'around the clock'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='a boost in the storage capacity of batteries',
             note=''),
        dict(role='谓语', text='is making their ability to keep power flowing around the clock more likely.',
             note='make A (more likely) 宾补结构；to keep... 不定式作后置定语；around the clock 全天候'),
    ])

A['P6S1'] = dict(
    zh='这一进步部分是由汽车制造商推动的，他们在电池驱动的电动汽车上下了大赌注。',
    insight=True, note='本句结构在四六级和考研阅读中较为常见：被动语态陈述事实+非限制性定语从句补充说明，是典型的学术或新闻语体句式。掌握后可迁移到类似长句的理解和翻译中。',
    bold=['placing big bets', 'electric vehicles'],
    chunks=[
        dict(role='主语', text='The advance',
             note=''),
        dict(role='谓语', text='is driven',
             note=''),
        dict(role='状语', text='in part by vehicle manufacturers,',
             note='被动语态 + by 施动者；in part 部分地'),
        dict(role='定语从句', text='who are placing big bets on battery- powered electric vehicles.',
             note='who 引导非限制性定语从句；place bets on 押注于'),
    ])

A['P6S2'] = dict(
    zh='尽管电动汽车目前在道路上仍然罕见，但这一巨额投资可能在未来几年迅速改变这一局面。',
    insight=False, note='',
    bold=['a rarity', 'change the picture'],
    chunks=[
        dict(role='状语从句', text='Although electric cars are still a rarity on roads now,',
             note='although 引导让步状语从句；a rarity 罕见之物'),
        dict(role='主语', text='this massive investment',
             note=''),
        dict(role='谓语', text='could change the picture',
             note=''),
        dict(role='状语', text='rapidly in coming years.',
             note=''),
    ])

A['P7S1'] = dict(
    zh='尽管还有很长的路要走，但可再生能源的趋势线正在飙升。',
    insight=False, note='',
    bold=['trend lines', 'spiking'],
    chunks=[
        dict(role='状语从句', text="While there's a long way to go,",
             note='while 引导让步状语从句'),
        dict(role='主语', text='the trend lines for renewables',
             note=''),
        dict(role='谓语', text='are spiking.',
             note='现在进行时；spike 飙升'),
    ])

A['P7S2'] = dict(
    zh='能源来源的变化速度似乎正在加快——也许正好及时产生减缓气候变化的有意义影响。',
    insight=False, note='',
    bold=['speeding up', 'meaningful effect'],
    chunks=[
        dict(role='主语', text='The pace of change in energy sources',
             note=''),
        dict(role='谓语', text='appears to be speeding up –',
             note='appear to do；speed up 加快'),
        dict(role='状语', text='perhaps just in time to have a meaningful effect in slowing climate change.',
             note='in time to do 及时做；in slowing... 动名词作介词宾语'),
    ])

A['P7S3'] = dict(
    zh='在全球思想转变之际，华盛顿在促进替代能源方面做什么或不做什么可能变得越来越无关紧要。',
    insight=True, note='本句包含主语从句充当主语、情态动词谓语、宾语、时间状语等多种成分,且主语从句内部还含有并列谓语和目的状语,成分种类较丰富。主语从句整体作主语是一个典型易错点,适合训练成分识别能力。',
    bold=['alternative energy', 'may mean less and less'],
    chunks=[
        dict(role='主语从句', text="What Washington does – or doesn't do – to promote alternative energy",
             note='what 引导主语从句；to promote... 不定式作目的状语'),
        dict(role='谓语', text='may mean',
             note=''),
        dict(role='宾语', text='less and less',
             note=''),
        dict(role='状语', text='at a time of a global shift in thought.',
             note=''),
    ])
