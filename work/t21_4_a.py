# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 4 — 逐句成分划分（自动生成，勿手改引号）。"""
A = {}

A['P1S1'] = dict(
    zh='我们相当擅长基于第一印象来判断他人，这种薄片体验范围从瞥见一张照片到五分钟的互动，而深思熟虑不仅可能是多余的，还可能是干扰性的。',
    insight=True, note='并列复合句是四六级和考研阅读中的常见句式,且本句第一个主句包含的"主系表+介词短语+同位语+分词定语"组合,以及第二个主句的"情态动词+notonly...but..."表语结构,都是考试中频繁出现的典型句式。掌握本句的分析方法可迁移到大量类似结构的句子。',
    bold=['based on first impressions', 'thin slices', 'extraneous'],
    chunks=[
        dict(role='主语', text='We',
             note='第一个主句主语'),
        dict(role='谓语', text="'re fairly good at judging people based on first impressions",
             note='be good at doing 擅长；based on... 过去分词短语作状语'),
        dict(role='同位语', text='thin slices of experience ranging from a glimpse of a photo to five-minute interaction',
             note='说明 first impressions；ranging from... 现在分词短语作后置定语'),
        dict(role='连接词', text='and',
             note='连接第二个主句'),
        dict(role='主语', text='deliberation',
             note='第二个主句主语'),
        dict(role='谓语', text='can be not only extraneous but intrusive',
             note='not only... but 连接并列表语'),
    ])

A['P1S2'] = dict(
    zh='在一项关于她称之为"薄片切割"能力的研究中，已故心理学家Nalini Ambady要求参与者观看教授们的10秒无声视频片段，并对教师的整体有效性进行评分。',
    insight=False, note='',
    bold=['In one study of', 'the late psychologist', 'asked participants to'],
    chunks=[
        dict(role='状语', text='In one study of the ability she called "thin slicing,"',
             note='介词短语作状语；she called "thin slicing" 省略 that 的定语从句修饰 ability'),
        dict(role='主语', text='the late psychologist Nalini Ambady',
             note='late 已故的'),
        dict(role='谓语', text='asked',
             note='后接宾语+宾语补足语'),
        dict(role='宾语', text='participants',
             note=''),
        dict(role='宾语补足语', text="to watch silent 10-second video clips of professors and to rate the instructor's overall effectiveness",
             note='两个并列不定式作宾补'),
    ])

A['P1S3'] = dict(
    zh='他们的评分与学生的学期末评分高度相关。',
    insight=False, note='',
    bold=['correlated strongly with', 'end-of-semester'],
    chunks=[
        dict(role='主语', text='Their ratings',
             note=''),
        dict(role='谓语', text="correlated strongly with students' end-of-semester ratings",
             note='correlate with 与…相关'),
    ])

A['P1S4'] = dict(
    zh='另一组参与者在观看视频片段时必须从1000倒数，每次减9，占用他们有意识的工作记忆。',
    insight=False, note='',
    bold=['count backward from', 'by nines', 'occupying'],
    chunks=[
        dict(role='主语', text='Another set of participants',
             note=''),
        dict(role='谓语', text='had to count backward from 1,000 by nines as they watched the clips',
             note='had to 不得不；as 引导时间状语从句'),
        dict(role='状语', text='occupying their conscious working memory',
             note='现在分词短语作结果/伴随状语'),
    ])

A['P1S5'] = dict(
    zh='他们的评分同样准确，证明了社会处理过程的直觉性质。',
    insight=False, note='',
    bold=['just as accurate', 'demonstrating', 'intuitive nature'],
    chunks=[
        dict(role='主语', text='Their ratings',
             note=''),
        dict(role='谓语', text='were just as accurate',
             note='系表结构'),
        dict(role='状语', text='demonstrating the intuitive nature of the social processing',
             note='现在分词短语作结果状语'),
    ])
