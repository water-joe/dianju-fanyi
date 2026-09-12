# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P7S1'] = dict(
    zh='公园以极少的预算完成所有这些工作。',
    insight=False, note='',
    bold=['on a shoestring'],
    chunks=[
        dict(role='主语', text='The parks',
             note=''),
        dict(role='谓语', text='do all this',
             note=''),
        dict(role='状语', text='on a shoestring.',
             note='on a shoestring 以极少的钱'),
    ])

A['P7S2'] = dict(
    zh='国会每年只拨款30亿美元给国家公园系统——这一数额自2001年以来一直持平（按通胀调整后的美元计算），除了2009年的一次性增加。',
    insight=False, note='',
    bold=['allocates', 'flat since'],
    chunks=[
        dict(role='主语', text='Congress',
             note=''),
        dict(role='谓语', text='allocates only $3 billion a year to the national park system—',
             note='allocate A to B 把 A 拨给 B'),
        dict(role='同位语', text='an amount that has been flat since 2001 (in inflation-adjusted dollars) with the exception of a onetime boost in 2009.',
             note='an amount 为同位语；that... 定语从句修饰 amount；with the exception of 除…之外'),
    ])

A['P7S3'] = dict(
    zh='与此同时，年游客数量自1980年以来增长了50%以上，现在达到每年3.3亿游客。',
    insight=True, note='并列主句结构在四六级和考研阅读中非常常见,尤其是描述数据变化的句子经常使用"数量+完成时增长+and+现在时当前状态"这种模式。掌握这种句式后,可以迁移到大量统计类、说明类文本的理解中。句首插入语和主语省略也是典型的书面语特征,学习价值较高。',
    bold=['annual visitors', 'stands at'],
    chunks=[
        dict(role='状语', text='Meanwhile,',
             note=''),
        dict(role='主语', text='the number of annual visitors',
             note=''),
        dict(role='谓语', text='has increased by more than 50% since 1980,',
             note='现在完成时；increase by 增长了…'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='now stands at 330 million visitors per year.',
             note='stand at 达到（某数值）'),
    ])
