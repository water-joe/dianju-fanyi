# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S5'] = dict(
    zh='但在其他地方，夜间温度或湿度可能与白天高温一样，都是风险的重要衡量指标。',
    insight=True, note='主系表结构配合比较状语从句是四六级和考研阅读中的常见句式，"as...as"比较结构及其省略用法是高频考点。并列主语和前置状语也是典型特征。句式简洁但代表性强，掌握后可迁移到大量类似比较句和主系表句的分析。',
    bold=['humidity', 'gauge of risk'],
    chunks=[
        dict(role='状语', text='But in other places,',
             note=''),
        dict(role='主语', text='nighttime temperatures or humidity',
             note=''),
        dict(role='谓语', text='might be',
             note=''),
        dict(role='表语', text='as important a gauge of risk as daytime highs.',
             note='as important a... as... 比较结构（as 修饰重要程度）'),
    ])

A['P3S1'] = dict(
    zh='研究人员表示，孟买四月份的中暑死亡事件凸显了制定更细致和本地化预警的必要性。',
    insight=False, note='',
    bold=['heatstroke deaths', 'nuanced and localized'],
    chunks=[
        dict(role='主语', text="Mumbai's April heatstroke deaths",
             note=''),
        dict(role='谓语', text='highlighted',
             note=''),
        dict(role='宾语', text='the need for more nuanced and localized warnings,',
             note=''),
        dict(role='主语', text='researchers',
             note='倒装引述分句主语'),
        dict(role='谓语', text='say.',
             note=''),
    ])

A['P3S2'] = dict(
    zh='当天约36°C的最高气温比国家气象部门为沿海城市设定的热浪警报阈值低1°C。',
    insight=False, note='',
    bold=['shy of', 'threshold', 'meteorological'],
    chunks=[
        dict(role='主语', text="That day's high temperature of roughly 36°C",
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='1°C shy of the heat wave alert threshold for coastal cities set by national meteorological authorities.',
             note='shy of 差…不到；set by... 过去分词短语作后置定语'),
    ])

A['P3S3'] = dict(
    zh='但高温的影响因湿度而被放大——这是高温警报系统中经常被忽视的因素——以及上午晚些时候户外仪式缺乏遮阴。',
    insight=False, note='',
    bold=['amplified', 'neglected factor', 'shade'],
    chunks=[
        dict(role='主语', text='the effects of the heat',
             note=''),
        dict(role='谓语', text='were amplified by humidity—an often neglected factor in heat alert systems—',
             note='被动语态；破折号内为 humidity 的同位语（内含过去分词 neglected 作定语）'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='状语', text='the lack of shade at the late-morning outdoor ceremony.',
             note='与 by humidity 并列的施动成分'),
    ])

A['P4S1'] = dict(
    zh='为了帮助改进高温行动计划，城市规划师Rajashree Kotharkar的团队正在制定一个示范计划，概述最佳实践并可根据当地条件进行调整。',
    insight=True, note='本句体现了四六级和考研真题中的典型结构:主句包含定语从句修饰宾语,从句内使用并列谓语和情态被动结构。这种嵌套修饰和情态表达在学术文本和考试中极为常见,掌握后可广泛应用',
    bold=['urban planner', 'model plan', 'best practices'],
    chunks=[
        dict(role='状语', text='To help improve HAPs,',
             note='不定式作目的状语'),
        dict(role='主语', text="urban planner Rajashree Kotharkar's team",
             note=''),
        dict(role='谓语', text='is working on a model plan',
             note='work on 从事于'),
        dict(role='定语从句', text='that outlines best practices and could be adapted to local conditions.',
             note='that 引导定语从句；并列谓语 outlines... and could be adapted...（情态被动）'),
    ])

A['P4S2'] = dict(
    zh='她说，除其他事项外，所有城市都应该绘制脆弱性地图，以帮助将应对措施集中在风险最高的人群上。',
    insight=False, note='',
    bold=['vulnerability map', 'most at risk'],
    chunks=[
        dict(role='状语', text='Among other things,',
             note='插语「除其他事项外」'),
        dict(role='插入语', text='she says,',
             note='引述插入语'),
        dict(role='主语', text='all cities',
             note=''),
        dict(role='谓语', text='should create a vulnerability map',
             note=''),
        dict(role='状语', text='to help focus responses on the populations most at risk.',
             note='不定式作目的状语；most at risk 后置定语修饰 populations'),
    ])

A['P5S1'] = dict(
    zh='Kotharkar说，这种地图绘制不需要很复杂。',
    insight=False, note='',
    bold=['mapping'],
    chunks=[
        dict(role='主语', text='Such mapping',
             note=''),
        dict(role='谓语', text="doesn't need to be complex,",
             note=''),
        dict(role='主语', text='Kotharkar',
             note='倒装引述分句主语'),
        dict(role='谓语', text='says.',
             note=''),
    ])
