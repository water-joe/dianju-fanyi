# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S4'] = dict(
    zh='与此同时，节日入口处的捐款却大幅下降。',
    insight=False, note='',
    bold=['dropped dramatically'],
    chunks=[
        dict(role='状语', text='At the same time,',
             note=''),
        dict(role='主语', text='donations at festival gates',
             note=''),
        dict(role='谓语', text='have dropped dramatically.',
             note='现在完成时'),
    ])

A['P3S1'] = dict(
    zh='芝加哥的夏季节日不仅仅是娱乐活动，它们是经济引擎，直接惠及所在社区和整个芝加哥市。',
    insight=True, note='分号连接并列主句、定语从句修饰表语、关系代词省略等结构都是四六级和考研真题中的常见句式。学生掌握本句后可将方法迁移到大量类似句子，具有较高的典型性和复用价值。',
    bold=['economic engines', 'as a whole'],
    chunks=[
        dict(role='主语', text="Chicago's summer festivals",
             note=''),
        dict(role='谓语', text='are about more than just entertainment;',
             note='more than just 不仅仅是'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text="economic engines that directly benefit the neighborhoods they're in and the city of Chicago as a whole.",
             note="that... 定语从句修饰 engines；(that) they're in 省略关系词的定语从句修饰 neighborhoods"),
    ])

A['P3S2'] = dict(
    zh='街头节日为本地商业带来客流量，培育使我们城市与众不同的文化活力。',
    insight=False, note='',
    bold=['drive foot traffic', 'cultural vibrancy'],
    chunks=[
        dict(role='主语', text='Street festivals',
             note=''),
        dict(role='谓语', text='drive foot traffic to local businesses and foster the kind of cultural vibrancy',
             note='并列谓语 drive... and foster...'),
        dict(role='定语从句', text='that makes our city special.',
             note='that 引导定语从句修饰 vibrancy'),
    ])

A['P4S1'] = dict(
    zh='我们经常听到人们问为什么我们在入口处请求捐款，尤其是当芝加哥爵士音乐节等该市最大型节日不要求捐款时。',
    insight=False, note='',
    bold=['solicit donations'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='状语', text='often',
             note=''),
        dict(role='谓语', text='hear people ask why we solicit donations at our entry points,',
             note='hear sb. do 宾补结构；why 引导宾语从句'),
        dict(role='状语从句', text="especially when the city's largest festivals like the Chicago Jazz Festival do not request donations.",
             note='when 引导时间/背景状语从句；like... 举例'),
    ])

A['P4S2'] = dict(
    zh='事实是，与那些由市政府制作的大型音乐节不同，你们社区的街头节日没有得到市政拨款，依靠赞助、摊位费和入口捐款的组合来支付成本。',
    insight=False, note='',
    bold=['no city funding', 'sponsorships', 'vendor fees'],
    chunks=[
        dict(role='主语', text='The fact',
             note=''),
        dict(role='谓语', text='is,',
             note='后接表语从句'),
        dict(role='表语从句', text='unlike those large, city-produced music festivals, your neighborhood street festivals receive no city funding and rely on a combination of sponsorships, vendor fees and gate donations to cover their costs.',
             note='unlike... 介词短语作对比状语；并列谓语 receive... and rely on...；to cover... 不定式作目的'),
    ])

A['P5S1'] = dict(
    zh='Wicker Park音乐节长期以来一直是芝加哥最受期待的夏季节日之一，在整个周末吸引超过7万名参与者，呈现现场独立音乐、本地艺术、小型商业摊位，以及最重要的社区联结。',
    insight=False, note='',
    bold=['most anticipated', 'drawing upward of', 'vendors'],
    chunks=[
        dict(role='主语', text='Wicker Park Fest',
             note=''),
        dict(role='谓语', text="has long been one of Chicago's most anticipated summer festivals,",
             note='现在完成时系表'),
        dict(role='状语', text='drawing upward of 70,000 attendees for a full weekend of live indie music, local art, small business vendors and, most importantly, community connection.',
             note='现在分词作伴随状语；upward of 超过'),
    ])
