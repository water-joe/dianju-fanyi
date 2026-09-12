# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P8S2'] = dict(
    zh='他指出，未能认识到这一点，会导致"对解决方案可能是什么产生过于简化的看法。',
    insight=False, note='',
    bold=['overly simplified'],
    chunks=[
        dict(role='主语', text='Failing to recognize that,',
             note='动名词短语作主语'),
        dict(role='插入语', text='he notes,',
             note='引述插入语'),
        dict(role='谓语', text='leads to',
             note=''),
        dict(role='宾语', text='"an overly simplified view of what the solutions might be.',
             note='what 引导宾语从句作介词宾语'),
    ])

A['P8S3'] = dict(
    zh='我们对问题的认知和对解决方案的认知变得非常有限。"',
    insight=False, note='',
    bold=['perception', 'becomes very limited'],
    chunks=[
        dict(role='主语', text='Our perception of the problem and of what the solution is',
             note=''),
        dict(role='谓语', text='becomes',
             note=''),
        dict(role='表语', text='very limited."',
             note=''),
    ])

A['P9S1'] = dict(
    zh='与此同时，Colorado大学的Balch教授表示，人们继续将火灾视为需要完全控制、仅在必要时才释放的事件。',
    insight=False, note='',
    bold=['wholly controlled', 'out of necessity'],
    chunks=[
        dict(role='状语', text='At the same time,',
             note=''),
        dict(role='主语', text='people',
             note=''),
        dict(role='谓语', text='continue to treat fire as an event that needs to be wholly controlled and unleashed only out of necessity,',
             note='treat A as B；that... 定语从句修饰 event；out of necessity 出于必要'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Professor Balch at the University of Colorado.',
             note='says 前置倒装'),
    ])

A['P9S2'] = dict(
    zh='但她说，承认火灾在人类生活中不可避免的存在，是制定使其尽可能安全的法律、政策和实践的关键态度。',
    insight=False, note='',
    bold=['inevitable presence', 'as safe as possible'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text="acknowledging fire's inevitable presence in human life",
             note='动名词短语作主语'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='an attitude crucial to developing the laws, policies, and practices that make it as safe as possible,',
             note='crucial to + 动名词；that... 定语从句修饰 practices；as... as possible'),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P10S1'] = dict(
    zh='Balch说:"我们已经将自己与火共生的状态割裂开来。',
    insight=False, note='',
    bold=['disconnected ourselves from'],
    chunks=[
        dict(role='主语', text='"We',
             note=''),
        dict(role='谓语', text="'ve disconnected ourselves from",
             note=''),
        dict(role='宾语', text='living with fire,"',
             note='动名词短语作介词宾语'),
        dict(role='主语', text='Balch',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P10S2'] = dict(
    zh='理解并努力梳理出当今人类与火灾的联系是什么，这一点非常重要。"',
    insight=False, note='',
    bold=['tease out'],
    chunks=[
        dict(role='主语', text='"It',
             note=''),
        dict(role='谓语', text='is really important',
             note=''),
        dict(role='真正主语', text='to understand and try and tease out what is the human connection with fire today."',
             note='不定式作真正主语；try and do；tease out 梳理出；what 引导宾语从句'),
    ])
