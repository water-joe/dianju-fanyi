# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S1'] = dict(
    zh='竞争法似乎是解决这些权力失衡的唯一途径。',
    insight=True, note='"主语+系表结构+不定式定语"是考研和四六级阅读中的高频句式，尤其"appears/seemstobe"结构和不定式作后置定语都是常考点，典型性较强，掌握后可大量迁移。',
    bold=['imbalances of power'],
    chunks=[
        dict(role='主语', text='Competition law',
             note=''),
        dict(role='谓语', text='appears to be',
             note=''),
        dict(role='表语', text='the only way to address these imbalances of power.',
             note='appear to be；to address... 不定式作后置定语'),
    ])

A['P3S2'] = dict(
    zh='但它很笨拙。',
    insight=False, note='',
    bold=['clumsy'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='clumsy.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='首先，与数字经济内部的变化速度相比，它非常缓慢。',
    insight=True, note='主系表加状语修饰是常见结构，"comparedto"引出的比较状语在说明文中较常出现，但整体结构较简单，代表性中等。',
    bold=['compared to', 'the pace of change'],
    chunks=[
        dict(role='状语', text='For one thing,',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='very slow',
             note=''),
        dict(role='状语', text='compared to the pace of change within the digital economy.',
             note='compared to 过去分词短语作比较状语'),
    ])

A['P3S4'] = dict(
    zh='当一个问题得到解决和补救时，它可能已经在市场上消失，被新的权力滥用所取代。',
    insight=True, note='本句的"时间状语从句+主句"结构是考试中的常见句式,"Bythetime"引导时间状语从句也是高频考点。主句中"mayhave+过去分词"表推测的用法,以及被动语态的现在完成时,都是四六级和考研阅读中经常出现的语法点。掌握本句的结构和时态用法,可以迁移到许多类似句子的理解中,典型性较高。',
    bold=['remedied', 'vanished', 'abuses of power'],
    chunks=[
        dict(role='状语从句', text='By the time a problem has been addressed and remedied',
             note='by the time 引导时间状语从句；现在完成时被动'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='may have vanished',
             note=''),
        dict(role='状语', text='in the marketplace,',
             note=''),
        dict(role='状语', text='to be replaced by new abuses of power.',
             note='不定式作结果状语；be replaced 被动'),
    ])

A['P3S5'] = dict(
    zh='但还有一个更深层次的概念问题。',
    insight=False, note='',
    bold=['conceptual problem'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='谓语', text='there is',
             note=''),
        dict(role='主语', text='a deeper conceptual problem, too.',
             note='there be 句型真正主语'),
    ])

A['P3S6'] = dict(
    zh='目前解释的竞争法处理的是消费者的财务劣势，而当这些服务的用户不为它们付费时，这一点并不明显。',
    insight=False, note='',
    bold=['as presently interpreted', 'financial disadvantage'],
    chunks=[
        dict(role='主语', text='Competition law as presently interpreted',
             note=''),
        dict(role='谓语', text='deals with',
             note=''),
        dict(role='宾语', text='financial disadvantage to consumers',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='this',
             note=''),
        dict(role='谓语', text='is not obvious',
             note=''),
        dict(role='状语从句', text="when the users of these services don't pay for them.",
             note='when 引导时间状语从句'),
    ])
