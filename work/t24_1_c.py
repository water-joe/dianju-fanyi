# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S1'] = dict(
    zh='少数城市在人工智能发明和商业化方面的主导地位意味着地理上的财富差距将继续飙升。',
    insight=False, note='',
    bold=['dominance', 'commercialization', 'soar'],
    chunks=[
        dict(role='主语', text='The dominance of a few cities in the invention and commercialization of AI',
             note='of/in 多层介词短语作后置定语'),
        dict(role='谓语', text='means',
             note='后接 that 宾语从句'),
        dict(role='宾语从句', text='that geographical disparities in wealth will continue to soar',
             note='continue to do 继续做；soar 飙升'),
    ])

A['P6S2'] = dict(
    zh='这不仅会助长政治和社会动荡，而且正如Coyle所说，它可能阻碍区域经济增长所需的各种人工智能技术。',
    insight=True, note='本句的"notonly...but(also)"并列结构、倒装句式、插入语从句都是四六级和考研真题中的高频句式。特别是"notonly"引起的倒装,以及插入语打断主句谓语,是考试中反复出现的典型结构。掌握本句的分析方法,可直接迁移到大量同类考题,代表性极强。',
    bold=['Not only', 'foster', 'hold back'],
    chunks=[
        dict(role='状语', text='Not only',
             note='否定词前置引起部分倒装'),
        dict(role='谓语', text='will this foster political and social unrest,',
             note='Not only 后倒装：will 提至主语 this 前'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='could,',
             note='情态动词（被插入语隔开）'),
        dict(role='插入语', text='as Coyle suggests,',
             note='方式/引述插入语'),
        dict(role='谓语', text='hold back the sorts of AI technologies needed for regional economies to grow',
             note='hold back 阻碍；needed for... 过去分词短语作后置定语'),
    ])

A['P7S1'] = dict(
    zh='解决方案的一部分可能在于以某种方式放松大型科技公司对定义人工智能议程的控制。',
    insight=False, note='',
    bold=['lie in', 'loosening', 'stranglehold'],
    chunks=[
        dict(role='主语', text='Part of the solution',
             note=''),
        dict(role='谓语', text='could lie in somehow loosening the stranglehold that Big Tech has on defining the AI agenda',
             note='lie in 在于；loosening... 动名词作宾语；that... 定语从句修饰 stranglehold'),
    ])

A['P7S2'] = dict(
    zh='这可能需要增加联邦资金，用于独立于科技巨头的研究。',
    insight=True, note="简单句的主谓宾结构配合后置定语修饰，是四六级和考研阅读中常见的句式。宾语中'名词+介词短语+形容词短语'的多层修饰模式在学术类文本中频繁出现，掌握后可迁移到类似长难句的理解中。但因无从句，句式复杂度未达到典型长难句水平，代表性中等偏上。",
    bold=['increased federal funding', 'independent of', 'tech giants'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text='will likely take',
             note=''),
        dict(role='宾语', text='increased federal funding for research independent of the tech giants',
             note='for research 介词短语作定语；independent of... 形容词短语作后置定语修饰 research'),
    ])

A['P8S1'] = dict(
    zh='一个更直接的应对措施是拓宽我们的数字想象力，构想不是简单地取代工作而是在国家不同地区最关心的部门(如医疗保健、教育和制造业)扩大机会的人工智能技术。',
    insight=False, note='',
    bold=['more immediate response', 'broaden', 'expand opportunities'],
    chunks=[
        dict(role='主语', text='A more immediate response',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text="to broaden our digital imaginations to conceive of AI technologies that don't simply replace jobs but expand opportunities in the sectors that different parts of the country care most about, like health care, education, and manufacturing",
             note="不定式作表语；that don't... but expand... 定语从句修饰 technologies；that... care most about 定语从句修饰 sectors；like... 举例"),
    ])
