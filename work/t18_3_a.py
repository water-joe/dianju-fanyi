# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='数字经济巨头的力量和野心令人震惊——Amazon刚刚宣布以135亿美元收购高端食品连锁店Whole Foods，但两年前Facebook为收购WhatsApp消息服务支付了更高的价格，而WhatsApp根本没有任何实体产品。',
    insight=False, note='',
    bold=['upmarket grocery chain', 'acquire', 'physical product'],
    chunks=[
        dict(role='主语', text='The power and ambition of the giants of the digital economy',
             note=''),
        dict(role='谓语', text='are astonishing—',
             note=''),
        dict(role='主语', text='Amazon',
             note=''),
        dict(role='谓语', text='has just ＄ announced the purchase of the upmarket grocery chain Whole Foods for 13.5bn,',
             note='现在完成时；for 13.5bn 价格状语'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='状语', text='two years ago',
             note=''),
        dict(role='主语', text='Facebook',
             note=''),
        dict(role='谓语', text='paid even more than that to acquire the WhatsApp messaging service,',
             note='to acquire... 不定式作目的状语'),
        dict(role='定语从句', text="which doesn't have any physical product at all.",
             note='which 引导非限制性定语从句修饰 service'),
    ])

A['P1S2'] = dict(
    zh='WhatsApp提供给Facebook的是其用户友谊和社交生活的复杂而精细的网络。',
    insight=True, note='主语从句+系动词+表语的结构在四六级和考研阅读中非常常见,尤其是用"What"引导主语从句来强调内容。双宾语结构也是高频考点。本句结构具有很强的代表性,掌握后可大量复用于理解同类句式',
    bold=['intricate', 'friendships and social lives'],
    chunks=[
        dict(role='主语从句', text='What WhatsApp offered Facebook',
             note='what 引导主语从句；offer sb. sth. 双宾语'),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text="an intricate and finely detailed web of its users' friendships and social lives.",
             note=''),
    ])

A['P2S1'] = dict(
    zh='Facebook当时向欧盟委员会承诺不会将电话号码与Facebook身份关联，但交易完成后几乎立即违背了这一承诺。',
    insight=True, note='本句结构在四六级和考研阅读中非常典型:并列句+宾语从句+时间状语从句的组合是长难句的常见模式;双宾语结构(promisesbsth)和时间状语从句(assoonas)都是高频考点;掌握本句的分析方法可以迁移到大量真题句子',
    bold=['promised', 'link', 'broke the promise'],
    chunks=[
        dict(role='主语', text='Facebook',
             note=''),
        dict(role='谓语', text='promised',
             note=''),
        dict(role='间接宾语', text='the European commission',
             note=''),
        dict(role='状语', text='then',
             note=''),
        dict(role='宾语从句', text='that it would not link phone numbers to Facebook identities,',
             note='that 引导宾语从句；link A to B 把 A 与 B 关联'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='broke the promise',
             note=''),
        dict(role='状语从句', text='almost as soon as the deal went through.',
             note='as soon as 引导时间状语从句；go through 完成、通过'),
    ])

A['P2S2'] = dict(
    zh='即使不知道消息内容是什么，了解谁发送了消息以及发给了谁也极具揭示性，而且现在仍然如此。',
    insight=False, note='',
    bold=['enormously revealing'],
    chunks=[
        dict(role='状语', text='Even without knowing what was in the messages,',
             note='without + 动名词；what 引导宾语从句'),
        dict(role='主语', text='the knowledge of who sent them and to whom',
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='enormously revealing',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='still could be.',
             note='省略 revealing'),
    ])

A['P2S3'] = dict(
    zh='哪个政治记者、哪个党鞭不想知道Theresa May的敌人目前正在密谋的WhatsApp群组的构成？',
    insight=True, note='本句覆盖多种成分：并列主语、情态动词谓语、复杂宾语（含介词短语定语和定语从句）、定语从句内的主谓结构及地点状语、时间状语。定语从句中inwhich的用法是常见考点，宾语的多层修饰也值得练习。成分种类较丰富，适合作为综合练习句。',
    bold=['party whip', 'makeup', 'plotting'],
    chunks=[
        dict(role='主语', text='What political journalist, what party whip,',
             note=''),
        dict(role='谓语', text='would not want to know',
             note=''),
        dict(role='宾语', text="the makeup of the WhatsApp groups in which Theresa May's enemies are currently plotting?",
             note='in which 引导定语从句修饰 groups；现在进行时'),
    ])

A['P2S4'] = dict(
    zh='Whole Foods对Amazon的价值可能不在于它拥有的460家店铺，而在于哪些顾客购买了什么的记录。',
    insight=True, note='成分种类丰富且包含多个易错点：形式主语it与真正主语的区分，主语从句同时作表语的双重身份，notsomuch...but...并列结构中的表语识别，定语从句中省略关系代词和介词前置（ofwhich）的处理，间接疑问词what作宾语。这些都是考试高频考点，训练价值高。',
    bold=['not so much', 'the records of'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text='may be',
             note=''),
        dict(role='表语从句', text='that the value of Whole Foods to Amazon is not so much the 460 shops it owns, but the records of which customers have purchased what.',
             note='that 引导表语从句（从句本身为主系表）；(that) it owns 省略关系词的定语从句；not so much A but B；which customers have purchased what 为 of 的宾语从句'),
    ])
