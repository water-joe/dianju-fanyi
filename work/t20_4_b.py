# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S3'] = dict(
    zh='尽管毕业时正值过去50年来最好的经济形势，Z世代却清楚经济崩溃是什么样子。',
    insight=False, note='',
    bold=['economic train wreck'],
    chunks=[
        dict(role='状语', text='Despite graduating into the best economy in the past 50 years,',
             note='despite + 动名词作让步状语'),
        dict(role='主语', text='Gen Zs',
             note=''),
        dict(role='谓语', text='know',
             note=''),
        dict(role='宾语从句', text='what an economic train wreck looks like.',
             note='what 引导宾语从句'),
    ])

A['P2S4'] = dict(
    zh='2008年金融危机时他们正处于易受影响的孩童时期，当时他们的许多父母失去了工作或毕生积蓄，或两者皆失。',
    insight=True, note='主句+when引导的时间状语从句是四六级和考研阅读中常见的句式，用于交代事件发生的时间背景，具有较高的实用性和典型性，学习后可迁移到类似句型。',
    bold=['impressionable', 'life savings'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='were',
             note=''),
        dict(role='表语', text='impressionable kids',
             note=''),
        dict(role='状语', text='during the crash of 2008,',
             note=''),
        dict(role='状语从句', text='when many of their parents lost their jobs or their life savings or both.',
             note='when 引导非限制性定语从句/时间状语从句'),
    ])

A['P2S5'] = dict(
    zh='他们不想冒任何风险。',
    insight=True, note='"beinterestedin+动名词"是四六级和考研阅读中的常见搭配，具有一定代表性；但整体句式过于简单，缺少从句、复杂修饰或多重结构，作为真题典型句式的代表性一般，更接近基础例句而非考点句。',
    bold=['taking any chances'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text="aren't interested in",
             note=''),
        dict(role='宾语', text='taking any chances.',
             note='动名词作介词宾语'),
    ])

A['P2S6'] = dict(
    zh='蓬勃发展的经济似乎并未缓解这一代人潜在的焦虑紧迫感，尤其是对那些背负大学债务的人而言。',
    insight=False, note='',
    bold=['assuage', 'anxious urgency'],
    chunks=[
        dict(role='主语', text='The booming economy',
             note=''),
        dict(role='谓语', text='seems to have done little to assuage this underlying generational sense of anxious urgency,',
             note='seem to have done；do little to do 无助于'),
        dict(role='状语', text='especially for those who have college debt.',
             note='who... 定语从句修饰 those'),
    ])

A['P2S7'] = dict(
    zh='根据美国联邦储备委员会的数据，美国大学贷款余额目前已达创纪录的1.5万亿美元。',
    insight=False, note='',
    bold=['stand at', 'Federal Reserve'],
    chunks=[
        dict(role='主语', text='College loan balances in the U.S.',
             note=''),
        dict(role='状语', text='now',
             note=''),
        dict(role='谓语', text='stand at',
             note=''),
        dict(role='宾语', text='a record $1.5 trillion,',
             note=''),
        dict(role='状语', text='according to the Federal Reserve.',
             note=''),
    ])

A['P3S1'] = dict(
    zh='埃森哲的一项调查发现，今年88%的应届毕业生在选择专业时就考虑到了工作。',
    insight=False, note='',
    bold=['graduating seniors', 'with a job in mind'],
    chunks=[
        dict(role='主语', text='One survey from Accenture',
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语从句', text='that 88 percent of graduating seniors this year chose their major with a job in mind.',
             note='that 引导宾语从句；with a job in mind 心中有工作'),
    ])
