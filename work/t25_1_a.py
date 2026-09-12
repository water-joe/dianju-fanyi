# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='美国顾客历来会给那些他们认为主要靠小费谋生的人支付小费，比如收入低于最低工资的餐厅服务员。',
    insight=True, note='本句涵盖主谓宾、时间状语、同位语、嵌套定语从句(省略关系代词)、嵌套宾语从句(省略that)等多种成分,尤其是双重省略引导词的从句结构和suchas同位语,是成分划分的高频易错点,练习价值高',
    bold=['historically tipped', 'restaurant servers', 'minimum wage'],
    chunks=[
        dict(role='主语', text='U.S. customers',
             note=''),
        dict(role='谓语', text='historically tipped',
             note=''),
        dict(role='宾语', text='people they assumed were earning most of their income via tips,',
             note='(whom/that) they assumed were earning... 双重省略：省略关系词的定语从句内又嵌套省略 that 的宾语从句'),
        dict(role='同位语', text='such as restaurant servers earning less than the minimum wage.',
             note='举例同位语；earning... 现在分词短语作后置定语'),
    ])

A['P1S2'] = dict(
    zh='2010年代初，各类商家开始使用iPad和其他数字支付系统处理交易。',
    insight=False, note='',
    bold=['a wide range of', 'processing purchases', 'digital payment systems'],
    chunks=[
        dict(role='状语', text='In the early 2010s,',
             note='时间状语'),
        dict(role='主语', text='a wide range of businesses',
             note=''),
        dict(role='谓语', text='started processing purchases with iPads and other digital payment systems.',
             note='start doing 开始做；with... 介词短语作方式状语'),
    ])

A['P1S3'] = dict(
    zh='这些系统经常提示顾客为以前不需要支付小费的服务支付小费。',
    insight=False, note='',
    bold=['prompted customers to'],
    chunks=[
        dict(role='主语', text='These systems',
             note=''),
        dict(role='状语', text='often',
             note=''),
        dict(role='谓语', text='prompted customers to tip for services that were not previously tipped.',
             note='prompt sb. to do 提示某人做；that... 定语从句修饰 services'),
    ])

A['P2S1'] = dict(
    zh='如今的小费要求往往与过去决定何时以及如何支付小费的薪资和服务规范脱节。',
    insight=True, note='覆盖主谓宾、被动结构、多个状语(频率、否定、方向)、定语从句、宾语从句等多种成分，且存在易错点：介词短语作状语、关系代词在从句中作主语、宾语从句嵌套。成分丰富且有练习价值。',
    bold=['not connected to', 'salary and service norms', 'when and how people tip'],
    chunks=[
        dict(role='主语', text="Today's tip requests",
             note=''),
        dict(role='谓语', text='are often not connected to',
             note='often 插在助动词后；be connected to 与…相关联'),
        dict(role='宾语', text='the salary and service norms that used to determine when and how people tip.',
             note='that used to... 定语从句修饰 norms；when and how people tip 宾语从句作 determine 的宾语'),
    ])

A['P2S2'] = dict(
    zh='过去顾客几乎总是在接受服务后支付小费，比如在用完餐后、理完发后或披萨送达后。',
    insight=False, note='',
    bold=['nearly always', 'receiving a service', 'haircut'],
    chunks=[
        dict(role='主语', text='Customers in the past',
             note=''),
        dict(role='状语', text='nearly always',
             note=''),
        dict(role='谓语', text='paid tips after receiving a service,',
             note='after receiving... 动名词短语作时间状语'),
        dict(role='同位语', text='such as at the conclusion of a restaurant meal, after getting a haircut or once a pizza was delivered.',
             note='三个并列时间状语举例'),
    ])

A['P2S3'] = dict(
    zh='这种时机可以奖励高质量的服务，并激励员工提供优质服务。',
    insight=False, note='',
    bold=['reward', 'incentive'],
    chunks=[
        dict(role='主语', text='That timing',
             note=''),
        dict(role='谓语', text='could reward high-quality service and give workers an incentive to provide it.',
             note='并列谓语 reward... and give...；to provide it 不定式作 incentive 的后置定语'),
    ])

A['P3S1'] = dict(
    zh='事先要求支付小费的情况正变得越来越普遍。',
    insight=False, note='',
    bold=['more common', 'beforehand'],
    chunks=[
        dict(role='主语', text="It's becoming more common for tips to be requested beforehand.",
             note='it 形式主语；真正主语为 for tips to be requested... 不定式复合结构'),
    ])
