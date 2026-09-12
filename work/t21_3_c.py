# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 3 — 逐句成分划分与重点词释义。
口径（与用户确认过，见 CLAUDE.md / BUILD_GUIDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""

# key = 句子 id ; zh 取自 raw 段落 zh 按句切分；bold/chunk.text 必须是 en 的连续子串
A = {}

A['P4S2'] = dict(
    zh=u'但这些事情对美国经济有利吗？',
    insight=False, note='',
    bold=['good for'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='谓语', text='are they good for', note='疑问句语序，主语 they'),
        dict(role='宾语', text='the American economy'),
    ])

A['P4S3'] = dict(
    zh=u'我不知道。',
    insight=False, note='',
    bold=["I don't know"],
    chunks=[
        dict(role='主语', text='I'),
        dict(role='谓语', text="don't know"),
    ])

A['P5S1'] = dict(
    zh=u'美国联邦贸易委员会表示它想找到这个问题的答案。',
    insight=False, note='',
    bold=['The US Federal Trade Commission', 'find the answer'],
    chunks=[
        dict(role='主语', text='The US Federal Trade Commission'),
        dict(role='谓语', text='says', note='后接省略 that 的宾语从句'),
        dict(role='宾语从句', text='it wants to find the answer to that question',
             note='that question 指前文的 result 之争'),
    ])

A['P5S2'] = dict(
    zh=u'本周，它要求五家最有价值的美国科技公司提供关于它们在过去十年中进行的众多小型收购的信息。',
    insight=False, note='',
    bold=['asked', 'for information about', 'over the past decade'],
    chunks=[
        dict(role='状语', text='This week', note='时间状语'),
        dict(role='主语', text='it'),
        dict(role='谓语', text='asked'),
        dict(role='宾语', text='the five most valuable US tech companies'),
        dict(role='状语', text='for information about their many small acquisitions over the past decade',
             note='for information 作对象状语；about... 介词短语修饰 information'),
    ])

A['P5S3'] = dict(
    zh=u'尽管目前只是一个研究项目，但这一要求引发了监管机构涉足迄今为止超出其管辖范围的早期科技市场的可能性。',
    insight=True,
    note=u'成分丰富：主句包含主谓宾和让步状语，宾语由介词短语扩展且内含动名词结构，从句中有主系表和时间状语；覆盖了定语从句中关系代词充当主语、介词短语作表语、动名词作介词宾语等多个知识点，适合综合练习',
    bold=['Although only a research project', 'raised the prospect', 'beyond their reach'],
    chunks=[
        dict(role='状语', text='Although only a research project at this stage',
             note='省略主语和 be 的让步状语从句（=Although it is only...）'),
        dict(role='主语', text='the request'),
        dict(role='谓语', text='has raised', note='现在完成时'),
        dict(role='宾语', text='the prospect of regulators wading into early-stage tech markets that until now have been beyond their reach',
             note='of... 介词短语作后置定语；wading into... 动名词短语；that... 定语从句修饰 markets'),
    ])

A['P6S1'] = dict(
    zh=u'考虑到它们总计超过5.5万亿美元的市值，仔细审查这些小型交易——其中许多远不如Wunderlist和Sunrise那样知名——似乎无关紧要。',
    insight=True,
    note=u'本句成分丰富且具有典型易错点:动名词作主语、分词独立结构作状语、破折号同位语插入、系表结构,覆盖多种常考成分类型,且主干被修饰语分隔是常见难点,适合作为成分划分练习',
    bold=['Given', 'rifling through', 'beside the point'],
    chunks=[
        dict(role='状语', text='Given their combined market value of more than $5.5 trillion',
             note='Given 引导的分词独立结构作状语，表"考虑到"'),
        dict(role='主语', text='rifling through such small deals— many of them much less prominent than Wunderlist and Sunrise—',
             note='动名词短语作主语；破折号内为同位语补充说明 deals'),
        dict(role='谓语', text='might seem', note='系动词'),
        dict(role='表语', text='beside the point', note='介词短语作表语，意为"无关紧要"'),
    ])

A['P6S2'] = dict(
    zh=u'在过去五年中，五大科技公司平均每年仅在10亿美元以下的收购上花费34亿美元——与它们庞大的财务储备以及去年在美国投资的超过1300亿美元风险资本相比不过是沧海一粟。',
    insight=False, note='',
    bold=['Between them', 'an average of', 'a drop in the ocean'],
    chunks=[
        dict(role='状语', text='Between them', note='介词短语，表"合计/在它们之间"'),
        dict(role='主语', text='the five biggest tech companies'),
        dict(role='谓语', text='have spent'),
        dict(role='宾语', text='an average of only $3.4 billion a year on sub-$1 billion acquisitions over the past five years',
             note='on... 状语表花费对象；over... 时间状语'),
        dict(role='同位语', text='—a drop in the ocean compared with their massive financial reserves, and the more than $130 billion of venture capital that was invested in the US last year',
             note='破折号后名词短语作同位语；compared with... 过去分词作后置定语；that... 定语从句修饰 capital'),
    ])

A['P7S1'] = dict(
    zh=u'然而，批评者称，大公司利用此类交易在最具威胁性的潜在竞争对手的业务有机会获得发展势头之前将其收购，在某些情况下作为"买了就关"策略的一部分，干脆将它们关闭。',
    insight=True,
    note=u'"say"后省略"that"引导宾语从句、宾语从句内嵌套时间状语从句、不定式作目的状语，这些都是四六级和考研阅读中的高频句式。掌握这类结构后，学生可以迁移到大量类似长句的分析中，典型性很高。',
    bold=['critics say', 'buy', 'gain momentum'],
    chunks=[
        dict(role='主语', text='critics'),
        dict(role='谓语', text='say', note='后接省略 that 的宾语从句'),
        dict(role='宾语从句', text='the big companies use such deals to buy their most threatening potential competitors before their businesses have a chance to gain momentum, in some cases as part of a "buy and kill" tactic to simply close them down',
             note='从句内含 before 时间状语从句；to buy... 不定式表目的；in some cases... 为状语性插入；to simply close them down 不定式作目的状语'),
    ])
