# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='老鼠和其他动物需要高度关注来自同类的社交信号，以便识别可以合作的朋友和需要避开的敌人。',
    insight=True, note='"主句+so引导的目的或结果状语从句"是四六级和考研阅读中的高频句式。主句用"needtobe+形容词"表达必要性，从句用"can+动词"表达能力或可能性，都是典型的表达方式。宾语后带不定式定语（"friendstocooperatewith"）也是常考结构。整句的句式组合具有很强的迁移价值，学生掌握后可以应用到大量类似句子的分析中。',
    bold=['attuned to', 'cooperate with'],
    chunks=[
        dict(role='主语', text='Rats and other animals',
             note=''),
        dict(role='谓语', text='need to be highly attuned to social signals from others',
             note='need to be + adj.；be attuned to 对…敏感'),
        dict(role='状语从句', text='so they can identify friends to cooperate with and enemies to avoid.',
             note='so 引导目的状语从句；两个不定式作后置定语'),
    ])

A['P1S2'] = dict(
    zh='为了弄清这是否延伸到非生命体，加州大学圣地亚哥分校的Laleh Quinn和她的同事们测试了老鼠是否能够检测到来自机器老鼠的社交信号。',
    insight=True, note='句首不定式表目的、主句后接宾语从句、宾语从句由whether或if引导,这些都是四六级和考研阅读中高频出现的句式。主语较长且含并列也是学术文本的常见特点。本句结构具有较强的代表性,掌握后可复用于理解大量类似句子。',
    bold=['extends to', 'non-living beings', 'whether'],
    chunks=[
        dict(role='状语', text='To find out if this extends to non-living beings,',
             note='不定式作目的状语；if 引导宾语从句作 find out 的宾语'),
        dict(role='主语', text='Laleh Quinn at the University of California, San Diego, and her colleagues',
             note=''),
        dict(role='谓语', text='tested',
             note=''),
        dict(role='宾语从句', text='whether rats can detect social signals from robotic rats.',
             note='whether 引导宾语从句'),
    ])

A['P2S1'] = dict(
    zh='他们让八只成年老鼠与两种类型的机器老鼠——一种社交型和一种非社交型——共同生活了四天。',
    insight=False, note='',
    bold=['housed', 'asocial'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='housed',
             note=''),
        dict(role='宾语', text='eight adult rats',
             note=''),
        dict(role='状语', text='with two types of robotic rat—one social and one asocial—for four days.',
             note='with... 介词短语作方式状语；破折号内为同位补充'),
    ])

A['P2S2'] = dict(
    zh='这些机器老鼠相当简约，像是一个带轮子可以四处移动、有彩色标记的加厚版电脑鼠标。',
    insight=False, note='',
    bold=['minimalist', 'resembling'],
    chunks=[
        dict(role='主语', text='The robot rats',
             note=''),
        dict(role='谓语', text='were quite minimalist,',
             note=''),
        dict(role='状语', text='resembling a chunkier version of a computer mouse with wheels to move around and colourful markings.',
             note='现在分词短语作补充说明；with... 介词短语作后置定语'),
    ])

A['P3S1'] = dict(
    zh='在实验期间，社交型机器老鼠跟随真老鼠四处走动，玩相同的玩具，并打开笼门让被困的老鼠逃出。',
    insight=False, note='',
    bold=['followed', 'trapped'],
    chunks=[
        dict(role='状语', text='During the experiment,',
             note=''),
        dict(role='主语', text='the social robot rat',
             note=''),
        dict(role='谓语', text='followed the living rats around, played with the same toys, and opened cage doors to let trapped rats escape.',
             note='三个并列谓语；to let... 不定式作目的状语；trapped 过去分词作前置定语'),
    ])

A['P3S2'] = dict(
    zh='与此同时，非社交型机器只是简单地前后和左右移动。',
    insight=True, note='包含主语、谓语、多个状语（时间状语、方式状语、方向状语）和并列结构，成分种类有一定覆盖，但结构过于简单，缺少易混淆的成分或特殊句式，练习价值有限。',
    bold=['Meanwhile', 'forwards and backwards'],
    chunks=[
        dict(role='状语', text='Meanwhile,',
             note=''),
        dict(role='主语', text='the asocial robot',
             note=''),
        dict(role='状语', text='simply',
             note=''),
        dict(role='谓语', text='moved forwards and backwards and side to side.',
             note='两个并列方向状语'),
    ])
