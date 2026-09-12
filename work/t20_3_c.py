# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S4'] = dict(
    zh='这些区域确实在一定程度上改善了空气质量，科学告诉我们这意味着真正的健康益处。',
    insight=False, note='',
    bold=['deliver', 'health benefits'],
    chunks=[
        dict(role='主语', text='The zones',
             note=''),
        dict(role='谓语', text='do deliver',
             note='do 强调'),
        dict(role='宾语', text='some improvements to air quality,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='the science',
             note=''),
        dict(role='谓语', text='tells',
             note=''),
        dict(role='宾语', text='us',
             note=''),
        dict(role='宾语从句', text='that means real health benefits.',
             note='省略 that 的宾语从句'),
    ])

A['P5S1'] = dict(
    zh='但市长和市议员对于这个远大于任何一个城市或城镇的问题所能做的十分有限。',
    insight=False, note='',
    bold=['do so much', 'far bigger than'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='mayors and councilors',
             note=''),
        dict(role='谓语', text='can only do so much',
             note=''),
        dict(role='状语', text='about a problem that is far bigger than any one city or town.',
             note='that... 定语从句修饰 problem'),
    ])

A['P5S2'] = dict(
    zh='他们之所以采取行动，是因为国家政府——英国和欧洲其他国家——未能做到这一点。',
    insight=True, note='主句+原因状语从句的结构在四六级和考研真题中非常常见，"because"引导原因状语是典型句式。破折号同位语的用法也是书面语中的常见现象。本句结构具有较高的代表性和迁移价值。',
    bold=['have failed to'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='are acting',
             note=''),
        dict(role='状语从句', text="because national governments—Britain's and others across Europe—have failed to do so.",
             note='because 引导原因状语从句；破折号内为同位语；fail to do 未能做'),
    ])

A['P6S1'] = dict(
    zh='将高污染车辆限制在特定区域之外——市中心、"学校街道"，甚至单独的道路——是对缺乏更大努力来适当执行现有法规并要求汽车公司使其车辆符合规定的一种回应。',
    insight=False, note='',
    bold=['into compliance', 'enforce existing regulations'],
    chunks=[
        dict(role='主语', text='Restrictions that keep highly polluting cars out of certain areas—city centres, "school streets", even individual roads—',
             note='that... 定语从句修饰 Restrictions；破折号内为 areas 的同位举例'),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='a response to the absence of a larger effort to properly enforce existing regulations and require auto companies to bring their vehicles into compliance.',
             note='to properly enforce... and require... 并列不定式作 effort 的后置定语；bring... into compliance 使…合规'),
    ])

A['P6S2'] = dict(
    zh='威尔士引入了特殊的低速限制以减少污染。',
    insight=False, note='',
    bold=['low speed limits', 'minimise'],
    chunks=[
        dict(role='主语', text='Wales',
             note=''),
        dict(role='谓语', text='has introduced',
             note=''),
        dict(role='宾语', text='special low speed limits',
             note=''),
        dict(role='状语', text='to minimise pollution.',
             note='不定式作目的状语'),
    ])

A['P6S3'] = dict(
    zh='我们正在做一切事情，却没有坚持要求制造商清理他们的汽车。',
    insight=True, note='句中涉及复杂宾语结构（everythingbutinsist...）、宾语从句、虚拟语气、省略to的不定式等多个知识点,成分划分覆盖主谓宾、从句内部主谓宾,且but的介词用法是易错点,训练价值较高。',
    bold=['insist', 'clean up'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text="'re doing",
             note=''),
        dict(role='宾语', text='everything',
             note=''),
        dict(role='介词短语', text='but insist that manufacturers clean up their cars.',
             note='but 此处为介词「除…之外」；insist that 后接宾语从句（(should) clean）'),
    ])
