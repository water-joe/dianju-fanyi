# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 4 —— 逐句成分划分（前半：P1–P3）。

口径见 BUILD_GUIDE.md / CLAUDE.md：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""
A = {}

A['P1S1'] = dict(
    zh='最新民意调查发现，在经济和人口结构发生剧烈变化的背景下，美国年轻一代正在绘制一幅通往成功的21世纪新路线图。',
    insight=False, note='',
    bold=['Against a backdrop of', 'drastic', 'road map'],
    chunks=[
        dict(role='状语', text='Against a backdrop of drastic changes in economy and population structure',
             note='介词短语作背景状语；of drastic changes... 为介词短语作后置定语修饰 backdrop'),
        dict(role='主语', text='younger Americans',
             note=''),
        dict(role='谓语', text='are drawing',
             note='现在进行时'),
        dict(role='宾语', text='a new 21st-century road map to success',
             note='road map to success 意为「通往成功的路线图」；to success 为介词短语作后置定语'),
        dict(role='主语', text='the latest poll',
             note='引述分句的主语，后置'),
        dict(role='谓语', text='has found',
             note='引述分句的谓语'),
    ])

A['P2S1'] = dict(
    zh='跨越代际界线，美国人继续珍视许多相同的传统成功人生里程碑，包括结婚、生育子女、拥有住房以及在六十多岁退休。',
    insight=False, note='',
    bold=['prize', 'milestones', 'including'],
    chunks=[
        dict(role='状语', text='Across generational lines',
             note='介词短语作范围状语'),
        dict(role='主语', text='Americans',
             note=''),
        dict(role='谓语', text='continue',
             note='后接不定式 to prize'),
        dict(role='宾语', text='to prize many of the same traditional milestones of a successful life',
             note='不定式短语作宾语；of a successful life 为介词短语作后置定语修饰 milestones'),
        dict(role='同位语', text='including getting married, having children, owning a home, and retiring in their sixties',
             note='including 引导的四个并列动名词短语，对 milestones 举例说明'),
    ])

A['P2S2'] = dict(
    zh='但是，尽管年轻人和老年人在充实人生的终点线是什么这一问题上基本达成一致，他们却为实现这一目标提供了截然不同的路径。',
    insight=False, note='',
    bold=['agree on', 'strikingly', 'fulfilling'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语从句', text='while young and old mostly agree on what constitutes the finish line of a fulfilling life',
             note='while 引导让步状语从句；what 引导宾语从句作介词 on 的宾语'),
        dict(role='主语', text='they',
             note='主句主语'),
        dict(role='谓语', text='offer',
             note=''),
        dict(role='宾语', text='strikingly different paths for reaching it',
             note='for reaching it 为介词短语作后置定语修饰 paths；it 指代 a fulfilling life'),
    ])

A['P3S1'] = dict(
    zh='调查发现，仍处于人生起步阶段的年轻人比老年人更有可能将工作中的个人满足感放在优先位置，相信他们通过定期更换工作最能推进职业发展，偏好拥有更多公共服务和更快生活节奏的社区，认同夫妻应在经济上有保障后再结婚或生育子女，并坚持认为父母双方都外出工作最有利于子女成长。',
    insight=False, note='',
    bold=['prioritize', 'advance', 'financially secure', 'maintain'],
    chunks=[
        dict(role='主语', text='Young people who are still getting started in life',
             note='内含定语从句 who are still getting started in life 修饰 people'),
        dict(role='谓语', text='were',
             note=''),
        dict(role='表语', text='more likely than older adults',
             note='比较结构，than older adults 为比较对象'),
        dict(role='补语', text='to prioritize personal fulfillment in their work',
             note='不定式短语作补足语，与 more likely 构成 be likely to do'),
        dict(role='补语', text='to believe they will advance their careers most by regularly changing jobs',
             note='并列不定式；believe 后为省略 that 的宾语从句，by regularly changing jobs 为方式状语'),
        dict(role='补语', text='to favor communities with more public services and a faster pace of life',
             note='with... 为介词短语作后置定语修饰 communities'),
        dict(role='补语', text='to agree that couples should be financially secure before getting married or having children',
             note='that 引导宾语从句；before getting married or having children 为时间状语'),
        dict(role='补语', text='and to maintain that children are best served by two parents working outside the home',
             note='与前面四个不定式并列；that 引导宾语从句，working outside the home 为现在分词短语作后置定语'),
        dict(role='主语', text='the survey',
             note='引述分句的主语，后置'),
        dict(role='谓语', text='found',
             note='引述分句的谓语'),
    ])
