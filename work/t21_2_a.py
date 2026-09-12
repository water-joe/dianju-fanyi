# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 2 —— P1 至 P3 的逐句成分划分与重点词释义。
口径：嵌套成分合并为一块（子结构写进 note）；引述分句各标各的主谓语。"""

A = {}

A['P1S1'] = dict(
    zh='据预测，到 2050 年全球人口将接近 100 亿，且有预测称某些地区农业产量需近乎翻番才能跟上，粮食安全正日益登上头条。',
    insight=False, note='',
    bold=['global population', 'predicted to hit', 'keep pace', 'food security', 'making headlines'],
    chunks=[
        dict(role='状语', text='With the global population predicted to hit close to 10 billion by 2050, and forecasts that agricultural production in some regions will need to nearly double to keep pace',
             note='with 复合结构作原因状语；predicted to hit 过去分词；that 引导同位语从句说明 forecasts'),
        dict(role='主语', text='food security'),
        dict(role='谓语', text='is increasingly making', note='现在进行时'),
        dict(role='宾语', text='headlines'),
    ])

A['P1S2'] = dict(
    zh='在英国，最近它也成了一个大话题，原因相当特别：脱欧。',
    insight=False, note='',
    bold=['talking point', 'particular reason', 'Brexit'],
    chunks=[
        dict(role='状语', text='In the UK'),
        dict(role='主语', text='it'),
        dict(role='谓语', text='has become'),
        dict(role='宾语', text='a big talking point recently too'),
        dict(role='状语', text='for a rather particular reason: Brexit',
             note='for...reason 原因状语；冒号后 Brexit 解释 reason'),
    ])

A['P2S1'] = dict(
    zh='一些人将脱欧视为扭转英国近期进口食品趋势的一个机会。',
    insight=False, note='',
    bold=['seen by some', 'reverse', 'importing food'],
    chunks=[
        dict(role='主语', text='Brexit'),
        dict(role='谓语', text='is seen', note='被动语态'),
        dict(role='主语补足语', text='by some as an opportunity to reverse a recent trend towards the UK importing food',
             note='as 短语作主语补足语；to reverse 不定式；towards... 介词短语修饰 trend，其中 the UK importing food 为动名词复合结构'),
    ])

A['P2S2'] = dict(
    zh='该国只生产其消费食物的约 60%，低于 20 世纪 80 年代末的近四分之三。',
    insight=False, note='',
    bold=['produces', 'down from', 'in the late 1980s'],
    chunks=[
        dict(role='主语', text='The country'),
        dict(role='谓语', text='produces'),
        dict(role='宾语', text='only about 60 per cent of the food it eats',
             note='it eats 为省略 that 的定语从句修饰 food'),
        dict(role='状语', text='down from almost three-quarters in the late 1980s',
             note='down from... 比较状语'),
    ])

A['P2S3'] = dict(
    zh='有观点认为，回归自给自足将提振农业、政治主权乃至国民健康。',
    insight=False, note='',
    bold=['self-sufficiency', 'the argument goes', 'boost', 'political sovereignty'],
    chunks=[
        dict(role='主语', text='A move back to self-sufficiency'),
        dict(role='插入语', text='the argument goes'),
        dict(role='谓语', text='would boost'),
        dict(role='宾语', text='the farming industry, political sovereignty and even the nation\'s health',
             note='并列宾语'),
    ])

A['P2S4'] = dict(
    zh='听起来不错——但这一愿景可行吗？',
    insight=False, note='',
    bold=['Sounds great', 'feasible', 'vision'],
    chunks=[
        dict(role='谓语', text='Sounds great', note='省略主语 it 的祈使/描述句'),
        dict(role='连接词', text='—but'),
        dict(role='状语', text='how'),
        dict(role='谓语', text='feasible is', note='疑问句倒装：表语 feasible 前置'),
        dict(role='主语', text='this vision'),
    ])

A['P3S1'] = dict(
    zh='根据利兹大学一份关于英国粮食生产的报告，英国 85% 的国土面积与肉类和乳制品生产相关。',
    insight=True,
    note='本句的"主语+be+过去分词+with"被动结构，以及句首"According to"引出信息来源的状语用法，都是四六级和考研阅读中的高频句式。学术报告、新闻报道常用被动语态陈述客观事实，"According to"也是引述来源的典型表达。掌握本句结构后，学习者可直接迁移到大量同类真题句中，代表性较强。',
    bold=['According to a report', 'total land area', 'associated with', 'meat and dairy'],
    chunks=[
        dict(role='状语', text='According to a report on UK food production from the University of Leeds, UK',
             note='according to... 信息来源状语'),
        dict(role='主语', text='85 per cent of the country\'s total land area'),
        dict(role='谓语', text='is associated', note='被动语态'),
        dict(role='状语', text='with meat and dairy production', note='be associated with 与…相关'),
    ])

A['P3S2'] = dict(
    zh='这供应了消费量的 80%，因此即使把全国都铺满畜牧场，我们也无法满足全部肉类和乳制品需求。',
    insight=True,
    note='本句成分丰富：包含动名词短语作主语、宾语从句、复合宾语（宾语加宾补）、被动语态谓语等多种结构。第二个主句的宾补结构 allow us to cover 是典型的易错点，动名词短语作主语也是常考点，适合作为划分成分的练习句。',
    bold=['supplies', 'consumed', 'livestock farms', "allow us to cover"],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text='supplies'),
        dict(role='宾语', text='80 per cent of what is consumed',
             note='what 引导宾语从句作 of 的宾语，what is consumed 被动'),
        dict(role='连接词', text='so'),
        dict(role='状语', text='even covering the whole country in livestock farms',
             note='even 强调；covering... 动名词短语作状语'),
        dict(role='主语', text='wouldn\'t allow'),
        dict(role='宾语', text='us'),
        dict(role='宾语补足语', text='to cover all our meat and dairy needs',
             note='allow + 宾语 + to do 复合宾语'),
    ])
