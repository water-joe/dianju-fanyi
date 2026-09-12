# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 4 —— 逐句成分划分（后段：P4S2–P5）。口径见 t24_4_a.py 头注释。"""
A = {}

A['P4S2'] = dict(
    zh='虽然联邦贸易委员会正在尽其所能确保应用程序信守对消费者关于处理其敏感健康信息的承诺，但这些健康应用程序进入市场的速度表明这是一个多么巨大的挑战。',
    insight=True,
    note='本句成分种类丰富，包含被定语从句分隔的主语、多个层级的宾语从句、目的状语、方式状语、表语等多种成分，且有主干被从句分隔、表语前置等易错点，非常适合作为划分句子成分的练习材料。',
    bold=['While', 'keeping their promises', 'demonstrates'],
    chunks=[
        dict(role='状语从句', text='While the FTC is doing what it can to ensure apps are keeping their promises to consumers around the handling of their sensitive health information',
             note='While 引导让步状语从句；what it can 宾语从句作 doing 的宾语；to ensure 目的状语；apps are keeping... 为省略 that 的宾语从句'),
        dict(role='主语', text='the rate at which these health apps are hitting the market',
             note='at which... 定语从句修饰 rate'),
        dict(role='谓语', text='demonstrates'),
        dict(role='宾语从句', text='just how immense of a challenge this is',
             note='how 引导宾语从句，作表语'),
    ])

A['P5S1'] = dict(
    zh='至于联邦立法的前景，评论人士认为短期内似乎不太可能出台全面的联邦隐私立法。',
    insight=True,
    note='主句+that引导的宾语从句是四六级和考研阅读中的高频句式，句首介词短语作状语也很常见。本句结构具有较强的代表性，掌握后可迁移到大量类似句子。',
    bold=['As to the prospects', 'commentators', 'in the short term'],
    chunks=[
        dict(role='状语', text='As to the prospects for federal legislation',
             note='介词短语作状语，as to 关于'),
        dict(role='主语', text='commentators'),
        dict(role='谓语', text='suggest'),
        dict(role='宾语从句', text='that comprehensive federal privacy legislation seems unlikely in the short term',
             note='that 引导宾语从句；in the short term 时间状语'),
    ])

A['P5S2'] = dict(
    zh='各州已开始实施自己的解决方案，以加强对消费者生成的健康数据的保护。',
    insight=False, note='',
    bold=['implementing', 'shore up', 'consumer-generated'],
    chunks=[
        dict(role='主语', text='States'),
        dict(role='谓语', text='have begun implementing',
             note='现在完成时；begin doing 开始做'),
        dict(role='宾语', text='their own solutions'),
        dict(role='状语', text='to shore up protections for consumer-generated health data',
             note='不定式作目的状语；for... 介词短语修饰 protections'),
    ])

A['P5S3'] = dict(
    zh='加利福尼亚州一直处于州隐私努力的前沿，制定了2018年《加利福尼亚州消费者隐私法》。',
    insight=False, note='',
    bold=['at the forefront of', 'with the California Consumer Privacy Act'],
    chunks=[
        dict(role='主语', text='California'),
        dict(role='谓语', text='has been'),
        dict(role='表语', text='at the forefront of state privacy efforts',
             note='at the forefront of 处于…的前沿'),
        dict(role='状语', text='with the California Consumer Privacy Act of 2018',
             note='with 复合结构作伴随状语'),
    ])

A['P5S4'] = dict(
    zh='弗吉尼亚州、科罗拉多州和犹他州最近也通过了州消费者数据隐私立法。',
    insight=False, note='',
    bold=['recently passed', 'state consumer data privacy legislation'],
    chunks=[
        dict(role='主语', text='Virginia, Colorado and Utah'),
        dict(role='状语', text='also recently', note='also 与 recently 修饰谓语'),
        dict(role='谓语', text='passed'),
        dict(role='宾语', text='state consumer data privacy legislation'),
    ])
