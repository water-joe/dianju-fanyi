# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S2'] = dict(
    zh='是的，学士学位能打开更多大门。',
    insight=False, note='',
    bold=['opens more doors'],
    chunks=[
        dict(role='插入语', text='Yes,',
             note=''),
        dict(role='主语', text="a bachelor's degree",
             note=''),
        dict(role='谓语', text='opens',
             note=''),
        dict(role='宾语', text='more doors.',
             note=''),
    ])

A['P6S3'] = dict(
    zh='但即使现在，全国54%的工作是中等技能工作，如建筑业和高技能制造业。',
    insight=False, note='',
    bold=['middle-skill jobs', 'high-skill manufacturing'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语', text='even now,',
             note=''),
        dict(role='主语', text='54 percent of the jobs in the country',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='middle-skill jobs, such as construction and high-skill manufacturing.',
             note=''),
    ])

A['P6S4'] = dict(
    zh='但只有44%的工人接受了充分培训。',
    insight=False, note='',
    bold=['adequately trained'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语', text='only',
             note=''),
        dict(role='主语', text='44 percent of workers',
             note=''),
        dict(role='谓语', text='are adequately trained.',
             note='被动语态；adequately 充分地'),
    ])

A['P7S1'] = dict(
    zh='换句话说，在工人阶级已让这个国家在政治上发生剧变的时刻，他们对曾经定义美国的机会正在消失感到沮丧，一个显而易见的解决方案正摆在我们面前。',
    insight=True, note='本句结构高度典型:主句+多层状语修饰+定语从句嵌套+宾语从句嵌套,是四六级和考研阅读中常见的复杂句式。时间状语内嵌定语从句、分词短语作状语带宾语从句、宾语从句内再嵌套定语从句,这些都是真题高频结构。掌握本句的分析方法可直接复用到大量同类句子',
    bold=['vanishing', 'staring us in the face'],
    chunks=[
        dict(role='状语', text='In other words,',
             note=''),
        dict(role='状语', text='at a time when the working class has turned the country on its political head, frustrated that the opportunity that once defined America is vanishing,',
             note='when... 定语从句修饰 time；frustrated that... 过去分词短语表状态；that... 宾语从句内又含 that... 定语从句修饰 opportunity'),
        dict(role='主语', text='one obvious solution',
             note=''),
        dict(role='谓语', text='is staring us in the face.',
             note='stare sb. in the face 摆在眼前'),
    ])

A['P7S2'] = dict(
    zh='工人阶级岗位存在缺口，但最需要这些工作的工人却不具备胜任能力。',
    insight=True, note='but连接的转折并列句+限制性定语从句是四六级和考研阅读的高频句式，存在句和被动语态也是常考结构。本句结构具有很强的代表性，掌握后可迁移到大量类似长句。',
    bold=['a gap in', 'equipped to'],
    chunks=[
        dict(role='谓语', text='There is',
             note=''),
        dict(role='主语', text='a gap in working-class jobs,',
             note=''),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='the workers who need those jobs most',
             note=''),
        dict(role='谓语', text="aren't equipped to do them.",
             note='be equipped to do 有能力做；who... 定语从句修饰 workers'),
    ])

A['P7S3'] = dict(
    zh='Koziatek的Manchester School of Technology High School正试图填补这一缺口。',
    insight=False, note='',
    bold=['fill that gap'],
    chunks=[
        dict(role='主语', text="Koziatek's Manchester School of Technology High School",
             note=''),
        dict(role='谓语', text='is trying to fill',
             note=''),
        dict(role='宾语', text='that gap.',
             note=''),
    ])

A['P8S1'] = dict(
    zh='Koziatek的学校是一记警钟。',
    insight=False, note='',
    bold=['wake-up call'],
    chunks=[
        dict(role='主语', text="Koziatek's school",
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a wake-up call.',
             note=''),
    ])

A['P8S2'] = dict(
    zh='当教育变成一刀切时，它就有可能忽视一个国家天赋的多样性。',
    insight=True, note='"When从句+主句"的条件或时间状语结构在考试中非常常见，是阅读理解和写作中的高频句式。主句中"riskdoing"的搭配也是典型用法。这种结构具有较强的代表性和迁移价值。',
    bold=['one-size-fits-all', 'diversity of gifts'],
    chunks=[
        dict(role='状语从句', text='When education becomes one-size-fits-all,',
             note='when 引导时间状语从句'),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='risks overlooking',
             note=''),
        dict(role='宾语', text="a nation's diversity of gifts.",
             note='risk doing 有…的风险；overlook 忽视'),
    ])
