# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='由于过多关注儿童使用屏幕的问题，家长很容易忘记自己对屏幕的使用。',
    insight=True, note='"Itis+形容词+forsb+todo"是四六级和考研阅读中的高频句式，且句首介词短语作状语的用法也很常见。本句结构具有较强的代表性，掌握后可迁移到大量类似句子的理解中。',
    bold=['With so much focus on', 'forget about'],
    chunks=[
        dict(role='状语', text="With so much focus on children's use of screens,",
             note='with 复合结构作原因/背景状语'),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text="'s easy for parents",
             note=''),
        dict(role='真正主语', text='to forget about their own screen use.',
             note='不定式复合结构作真正主语'),
    ])

A['P1S2'] = dict(
    zh='Jenny Radesky在她关于数字化游戏的研究中说:"科技的设计就是要真正吸引你，数字产品的存在是为了促进最大程度的参与。',
    insight=True, note='句中涵盖引述结构、被动语态、makeit+形容词+todo的形式宾语结构、并列谓语（makesandleads）、目的状语（不定式）、地点状语等多种成分，且makeithardtodo是常见易错点。引述结构中插入地点状语的用法也值得练习，成分种类丰富且具有实用性。',
    bold=['suck you in', 'maximal engagement'],
    chunks=[
        dict(role='宾语', text='"Tech is designed to really suck you in,"',
             note='直接引语作 says 的宾语；be designed to do 被动'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Jenny Radesky in her study of digital play,',
             note=''),
        dict(role='宾语', text='"and digital products are there to promote maximal engagement.',
             note='be there to do 旨在做；promote 促进'),
    ])

A['P1S3'] = dict(
    zh='这使人难以脱离，并导致大量渗透到家庭日常生活中。"',
    insight=False, note='',
    bold=['disengage', 'bleed-over'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='makes it hard to disengage, and leads to a lot of bleed-over',
             note='make it + adj. + to do 形式宾语；并列谓语'),
        dict(role='状语', text='into the family routine."',
             note='bleed-over into 渗入'),
    ])

A['P2S1'] = dict(
    zh='Radesky研究了用餐时使用手机和平板电脑的情况，她让母子配对进行食物测试练习。',
    insight=False, note='',
    bold=['tablets', 'food-testing exercise'],
    chunks=[
        dict(role='主语', text='Radesky',
             note=''),
        dict(role='谓语', text='has studied the use of mobile phones and tablets at mealtimes',
             note='现在完成时'),
        dict(role='状语', text='by giving mother-child pairs a food-testing exercise.',
             note='by + 动名词表方式；give sb. sth. 双宾语'),
    ])

A['P2S2'] = dict(
    zh='她发现，在练习过程中使用设备的母亲与孩子进行的语言互动减少了百分之二十，非语言互动减少了百分之三十九。',
    insight=False, note='',
    bold=['verbal', 'nonverbal interactions'],
    chunks=[
        dict(role='主语', text='She',
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语从句', text='that mothers who used devices during the exercise started 20 per cent fewer verbal and 39 per cent fewer nonverbal interactions with their children.',
             note='that 引导宾语从句；who... 定语从句修饰 mothers'),
    ])
