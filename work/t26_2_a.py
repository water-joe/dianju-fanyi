# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='根据我们的研究，英国约有五分之一的员工像朋友一样与AI交谈，在个人和职业问题上寻求指导。',
    insight=True, note='"主语+谓语+状语"配分词短语作状语的结构，在四六级和考研阅读中高频出现；句首介词短语引出信息来源、句末分词短语补充伴随动作或目的，是学术和新闻语体的典型句式，掌握后可广泛迁移。',
    bold=['one in five', 'looking for guidance'],
    chunks=[
        dict(role='状语', text='According to our research,',
             note='信息来源状语'),
        dict(role='主语', text='around one in five workers in the UK',
             note=''),
        dict(role='谓语', text='talk to AI like a friend,',
             note=''),
        dict(role='状语', text='looking for guidance on personal and professional problems.',
             note='现在分词短语作伴随状语'),
    ])

A['P1S2'] = dict(
    zh='我们的数据显示，以这种方式与AI互动可以让我们感到被倾听，减少孤独感。',
    insight=False, note='',
    bold=['engaging with', 'feeling heard', 'isolated'],
    chunks=[
        dict(role='主语', text='Our data',
             note=''),
        dict(role='谓语', text='shows',
             note='后接 that 宾语从句'),
        dict(role='宾语从句', text='that engaging with AI like this can leave us feeling heard and less isolated.',
             note='动名词短语作从句主语；leave us feeling... 宾补结构'),
    ])

A['P1S3'] = dict(
    zh='但是，随着这种新建立的联系，我们中的许多人分享了敏感的、有时是高度机密的信息，尽管超过三分之一的人没有意识到AI平台可能并不擅长保守我们的秘密……秘密。',
    insight=True, note='本句在成分丰富度、结构典型性和实用性方面得分较高，适合作为让步状语从句和从句嵌套的练习材料。主干识别有一定挑战但不至于过难，时态语态相对基础，整体平衡了难度和训练价值，推荐作为中等偏上难度的结构分析练习句。',
    bold=['newfound', 'confidential information', 'keeping our secrets'],
    chunks=[
        dict(role='连接词', text='But,',
             note=''),
        dict(role='状语', text='with this newfound connection,',
             note='with 复合结构作伴随状语'),
        dict(role='主语', text='many of us',
             note=''),
        dict(role='谓语', text='share',
             note=''),
        dict(role='宾语', text='sensitive, sometimes highly confidential information,',
             note=''),
        dict(role='状语从句', text="even though over a third of people don't realise that AI platforms may not be very good at keeping our secrets…secret.",
             note='even though 引导让步状语从句；that 引导 realise 的宾语从句'),
    ])

A['P2S1'] = dict(
    zh='对企业而言，这种影响令人担忧。',
    insight=False, note='',
    bold=['implications'],
    chunks=[
        dict(role='状语', text='For businesses,',
             note=''),
        dict(role='主语', text='the implications',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='worrying.',
             note=''),
    ])

A['P2S2'] = dict(
    zh='以Microsoft Copilot为例。',
    insight=False, note='',
    bold=['for example'],
    chunks=[
        dict(role='谓语', text='Consider Microsoft Copilot, for example.',
             note='祈使句（=Let us consider...）'),
    ])

A['P2S3'] = dict(
    zh='它使Microsoft获得对任何用户输入或输出数据的广泛权利——以其认为合适的任何方式使用这些数据的权利；它甚至可以与第三方分享这些数据。',
    insight=True, note='本句涵盖了双宾语结构（"gainsMicrosoftbroadrights"）、定语（介词短语、不定式短语、定语从句）、同位语、状语等多种成分，且定语从句省略引导词、破折号引出同位语等都是易错点。此外，"itseesfit"中"fit"作补语、"canshare"中"even"的位置等细节也值得练习。成分种类较丰富，适合作为综合练习句。',
    bold=['broad rights', 'sees fit', 'third parties'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='gains',
             note='双宾结构：gains Microsoft broad rights'),
        dict(role='间接宾语', text='Microsoft',
             note=''),
        dict(role='直接宾语', text='broad rights to the data inputted or outputted by any user',
             note='inputted or outputted... 过去分词短语作后置定语'),
        dict(role='同位语', text='— rights to use this data in any way it sees fit;',
             note='破折号引出同位语；(that) it sees fit 省略关系词的定语从句修饰 way'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='can even share it with third parties.',
             note='even 插在情态动词后'),
    ])

A['P2S4'] = dict(
    zh='这意味着任何敏感的商业信息都可能暴露给全世界。',
    insight=True, note='"主句+that宾语从句"是四六级和考研阅读中的高频句式，且从句内含情态+被动结构也是常考点，典型性较高，掌握后可广泛复用。',
    bold=['potentially be exposed'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='means',
             note=''),
        dict(role='宾语从句', text='that any sensitive business information could potentially be exposed to the world.',
             note='情态+被动结构'),
    ])
