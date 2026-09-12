# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='在更短时间内完成更多工作的另一种方法是重新思考如何安排一天的优先事项——特别是我们如何制定待办事项清单。',
    insight=False, note='',
    bold=['rethink', 'prioritise', 'to-do lists'],
    chunks=[
        dict(role='主语', text='Another approach to getting more done in less time',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='to rethink how you prioritise your day – in particular how we craft our to-do lists.',
             note='不定式作表语；两个 how 引导宾语从句'),
    ])

A['P4S2'] = dict(
    zh='《混乱:无序的力量如何改变我们的生活》一书的作者Tim Harford指出了20世纪80年代初的一项研究，该研究将本科生分为两组:一些人被建议制定月度目标和学习活动；另一些人被要求更详细地规划活动和目标，逐日进行。',
    insight=True, note='句子覆盖主语、谓语、宾语、同位语、定语从句、结果状语等多种成分，定语从句中关系代词作主语是常见考点，冒号后并列被动结构可练习宾语从句和被动语态识别，成分种类较丰富',
    bold=['points to', 'undergraduates', 'day by day'],
    chunks=[
        dict(role='主语', text='Tim Harford,',
             note=''),
        dict(role='同位语', text='author of Messy: The Power of Disorder to Transform Our Lives,',
             note=''),
        dict(role='谓语', text='points to',
             note=''),
        dict(role='宾语', text='a study in the early 1980s that divided undergraduates into two groups:',
             note='that... 定语从句修饰 study；divide A into B'),
        dict(role='宾语从句', text='some were advised to set out monthly goals and study activities; others were told to plan activities and goals in much more detail, day by day.',
             note='冒号后两组并列分句（被动语态）；day by day 逐日'),
    ])

A['P5S1'] = dict(
    zh='虽然研究人员认为结构良好的每日计划在执行任务时最有效，但他们错了:详细的每日计划削弱了学生的积极性。',
    insight=False, note='',
    bold=['assumed', 'the execution of tasks', 'demotivated'],
    chunks=[
        dict(role='状语从句', text='While the researchers assumed that the well-structured daily plans would be most effective when it came to the execution of tasks,',
             note='while 引导让步状语从句；assumed that 宾语从句；when it came to 时间状语从句'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='were wrong:',
             note=''),
        dict(role='主语', text='the detailed daily plans',
             note=''),
        dict(role='谓语', text='demotivated students.',
             note='冒号后解释说明；demotivate 使失去动力'),
    ])

A['P5S2'] = dict(
    zh='Harford认为，不可避免的干扰常常使每日待办事项清单失效，而在这样的清单中为即兴发挥留出空间可以获得最佳结果。',
    insight=True, note='arguethat引导宾语从句是学术写作和考试中的高频句式，while引导对比状语从句也是常见结构，动名词短语作主语在四六级和考研阅读中反复出现，整体句式具有很强的代表性和迁移价值。',
    bold=['render', 'improvisation', 'reap the best results'],
    chunks=[
        dict(role='主语', text='Harford',
             note=''),
        dict(role='谓语', text='argues',
             note=''),
        dict(role='宾语从句', text='that inevitable distractions often render the daily to-do list ineffective,',
             note='render A adj. 使 A 变得…'),
        dict(role='连接词', text='while',
             note=''),
        dict(role='主语', text='leaving room for improvisation in such a list',
             note=''),
        dict(role='谓语', text='can reap the best results.',
             note='动名词短语作主语；reap 收获'),
    ])

A['P6S1'] = dict(
    zh='为了充分利用我们的专注力和精力，我们还需要拥抱休息时间，或者如Newport所建议的，"变得懒惰"。',
    insight=True, note='本句覆盖了主谓宾、目的状语、插入的状语从句、宾语引语等多种成分，结构较为丰富。特别是"needtoembrace"这种谓语与不定式搭配、以及插入从句的识别，对学生有一定练习价值。但句中无定语从句、复杂修饰语或易混淆的多重嵌套，难度适中，作为成分划分练习句有一定收益',
    bold=['make the most of', 'embrace downtime'],
    chunks=[
        dict(role='状语', text='In order to make the most of our focus and energy,',
             note='in order to 引导目的状语'),
        dict(role='主语', text='we',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='need to embrace downtime,',
             note=''),
        dict(role='状语从句', text='or as Newport suggests, "be lazy".',
             note='or 引出同位性说明；as 引导方式状语从句'),
    ])
