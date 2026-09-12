# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='我们需要在减少和分流医疗服务需求方面做得更好，而不是仅仅对其进行管理。',
    insight=True, note='"主语+needtobe+形容词+介词短语"的主系表结构在四六级和考研阅读中较为常见，属于表达观点或建议的典型句式。"ratherthan"引导的对比结构也是常考的逻辑连接手段。掌握本句结构后，学生可以迁移到类似的"begoodat/beskilledin"等表达以及对比论证句式。不过，本句缺少从句嵌套和复杂修饰，代表性略逊于包含多层从句的长难句，因此典型性评为中等偏上。',
    bold=['reducing and diverting demand', 'rather than'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text='need to be much better at reducing and diverting demand on health services,',
             note='be good at doing；at 的宾语为两个并列动名词'),
        dict(role='状语', text='rather than simply managing it.',
             note='rather than 而非；managing 动名词'),
    ])

A['P3S3'] = dict(
    zh='需要在社区和基层医疗方面投入更多资金，以减少我们对医院的依赖。',
    insight=True, note='"needtobe+过去分词"的被动结构在四六级和考研阅读中频繁出现，不定式作目的状语也是高频句式。本句结构清晰且实用性强，学会后可迁移至大量类似表达。',
    bold=['primary care', 'reliance on'],
    chunks=[
        dict(role='主语', text='Much more',
             note=''),
        dict(role='谓语', text='needs to be invested in communities and primary care',
             note='need to be done 被动结构'),
        dict(role='状语', text='to reduce our reliance on hospitals.',
             note='不定式作目的状语'),
    ])

A['P3S4'] = dict(
    zh='社会护理的能力需要更大，以支持日益增长的长期病患者数量。',
    insight=True, note='"主语+needstobe+形容词+目的状语"是议论文和说明文中常见的论证句式，用于陈述必要性并说明原因；后置定语和分词短语修饰名词也是考试高频结构，具有较强的迁移性。',
    bold=['social care', 'capacity', 'long-term conditions'],
    chunks=[
        dict(role='主语', text='And capacity in social care',
             note=''),
        dict(role='谓语', text='needs to be greater,',
             note=''),
        dict(role='状语', text='to support the growing number of people living with long-term conditions.',
             note='不定式作目的状语；living with... 现在分词短语作后置定语'),
    ])

A['P4S1'] = dict(
    zh='然而，尽管经历了二十年的战略规划和多次重大卫生改革，我们在任何这些目标上都未能取得实质性进展。',
    insight=True, note='"尽管...但是..."的让步转折结构在四六级和考研阅读中高频出现，现在完成时表达持续未变的状态也是常考句式，本句结构具有较强的代表性和可迁移性。',
    bold=['Yet despite', 'meaningful progress'],
    chunks=[
        dict(role='状语', text='Yet despite two decades of strategies and a number of major health reforms,',
             note='despite 介词短语作让步状语'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='have failed to make meaningful progress on any of these aims.',
             note='fail to do 未能做；现在完成时'),
    ])

A['P4S2'] = dict(
    zh='这就是为什么Reform智库在十位前卫生大臣的支持下启动了一项名为"重新构想健康"的新工作计划。',
    insight=True, note='主系表结构后接表语从句是考试中的常见句式，尤其是why引导的表语从句在解释原因类文本中频繁出现。本句结构具有较高的代表性，掌握后可迁移到同类句型。',
    bold=['think tank', 'launching', 'entitled'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text='is why',
             note='why 引导表语从句'),
        dict(role='表语从句', text='the Reform think tank is launching a new programme of work entitled "Reimagining health", supported by ten former health ministers.',
             note='entitled... 过去分词短语作后置定语；supported by... 过去分词短语作补充'),
    ])

A['P4S3'] = dict(
    zh='我们共同呼吁就英国健康的未来进行更加开放和诚实的对话，并"紧急反思"我们所保留的以医院为中心的模式。',
    insight=True, note='主句使用现在进行时陈述当前行为，宾语带介词短语后置定语和定语从句修饰，这是四六级和考研阅读中较为常见的句式。定语从句省略关系代词的现象也较典型。但句子整体语义偏向特定话题（医疗政策讨论），结构本身虽典型但不算高频核心句式，迁移价值中等偏上。',
    bold=['calling for', 'urgent rethink', 'hospital-centric'],
    chunks=[
        dict(role='状语', text='Together,',
             note=''),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='are calling for',
             note=''),
        dict(role='宾语', text='a much more open and honest conversation about the future of health in the UK, and an "urgent rethink" of the hospital-centric model we retain.',
             note='两个并列宾语；(that/which) we retain 省略关系词的定语从句'),
    ])
