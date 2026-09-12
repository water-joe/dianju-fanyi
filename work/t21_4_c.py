# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 4 — 逐句成分划分（自动生成，勿手改引号）。"""
A = {}

A['P4S1'] = dict(
    zh='思考过多也会损害我们形成偏好的能力。',
    insight=False, note='',
    bold=['Thinking too much', 'harm', 'form preferences'],
    chunks=[
        dict(role='主语', text='Thinking too much',
             note='动名词短语作主语'),
        dict(role='谓语', text='can also harm',
             note='harm 损害'),
        dict(role='宾语', text='our ability to form preferences',
             note='to form... 不定式作后置定语修饰 ability'),
    ])

A['P4S2'] = dict(
    zh='当大学生不被要求分析他们的理由时，他们对草莓酱和大学课程的评分与专家意见更一致。',
    insight=False, note='',
    bold=['aligned better with', 'rationale'],
    chunks=[
        dict(role='主语', text="College students' ratings of strawberry jams and college courses",
             note=''),
        dict(role='谓语', text="aligned better with experts' opinions",
             note='align with 与…一致'),
        dict(role='状语从句', text="when the students weren't asked to analyze their rationale",
             note='when 引导时间状语从句'),
    ])

A['P4S3'] = dict(
    zh='当人们被要求关注自己的感受而非细节时，他们做出的购车决策既在客观上更好，也在个人层面上更令人满意，但只有在决策复杂时才如此——当他们有大量信息需要处理时。',
    insight=True, note='本句成分丰富且含多个训练点：主句包含主谓宾结构及多个状语从句；定语从句中有主系表结构及并列表语；时间状语从句涉及主语省略和宾语补足语；条件状语从句再现主系表结构。句中展示了定语从句修饰宾语、多个状语从句修饰主句、省略结构还原、不定式作定语等多种成分划分训练点，是较好的综合练习句。',
    bold=['made car-buying decisions', 'objectively better', 'only if the decision was complex'],
    chunks=[
        dict(role='主语', text='And people',
             note=''),
        dict(role='谓语', text='made car-buying decisions',
             note='make decisions 做决定'),
        dict(role='定语从句', text='that were both objectively better and more personally satisfying',
             note='修饰 decisions；both... and 并列表语'),
        dict(role='状语从句', text='when asked to focus on their feelings rather than on details',
             note='when 引导时间状语从句（省略 they were）'),
        dict(role='连接词', text='but',
             note='转折'),
        dict(role='状语', text='only if the decision was complex—when they had a lot of information to process',
             note='if 条件状语从句；破折号后 when 从句进一步说明 complex'),
    ])

A['P5S1'] = dict(
    zh='直觉的特殊力量只在特定情况下才会释放。',
    insight=False, note='',
    bold=['unleashed', 'in certain circumstances'],
    chunks=[
        dict(role='主语', text="Intuition's special powers",
             note=''),
        dict(role='谓语', text='are unleashed',
             note='被动语态，unleash 释放'),
        dict(role='状语', text='only in certain circumstances',
             note='介词短语作状语'),
    ])

A['P5S2'] = dict(
    zh='在一项研究中，参与者完成了八项任务，其中四项利用反思性思维(辨别规则、理解词汇)，四项利用直觉和创造力(生成新产品或修辞手法)。',
    insight=True, note='这是学术文本中非常典型的句式：主句陈述研究内容，后接定语从句对研究对象进行分类说明。这种"主句+并列定语从句"的结构在四六级和考研阅读理解中频繁出现，掌握后迁移价值高',
    bold=['completed a battery of', 'tapped reflective thinking', 'figures of speech'],
    chunks=[
        dict(role='状语', text='In one study,',
             note='介词短语作状语'),
        dict(role='主语', text='participants',
             note=''),
        dict(role='谓语', text='completed a battery of eight tasks',
             note='a battery of 一系列'),
        dict(role='定语从句', text='including four that tapped reflective thinking (discerning rules, comprehending vocabulary) and four that tapped intuition and creativity (generating new products or figures of speech)',
             note='including... 现在分词短语含两个 that 定语从句；括号内为分词短语举例'),
    ])

A['P5S3'] = dict(
    zh='然后他们评估自己使用直觉的程度("直觉感受"、"预感"、"我的内心")。',
    insight=True, note='本句的结构是典型的主句带限制性定语从句，且定语从句用了"介词+which"引导，这是四六级和考研阅读中常见的句式。过去完成时与一般过去时的配合也是常考的时态组合。句子没有特别罕见的结构或生僻用法，学生掌握后可以迁移到大量类似句子。具有较高的代表性和复用价值。',
    bold=['rated the degree', 'to which they had used'],
    chunks=[
        dict(role='状语', text='Then',
             note='时间状语'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='rated',
             note='rated 此处为动词"评估"'),
        dict(role='宾语', text='the degree to which they had used intuition ("gut feelings," "hunches," "my heart")',
             note='to which 引导定语从句修饰 degree（介词+which）；括号内为 intuition 的同位举例'),
    ])

A['P5S4'] = dict(
    zh='如预期的那样，使用直觉损害了他们在前四项任务上的表现，但帮助了他们完成其余任务。',
    insight=False, note='',
    bold=['Use of their gut', 'hurt their performance', 'on the rest'],
    chunks=[
        dict(role='主语', text='Use of their gut',
             note='gut 直觉'),
        dict(role='谓语', text='hurt their performance on the first four tasks',
             note='hurt 损害'),
        dict(role='插入语', text='as expected,',
             note='如预期'),
        dict(role='连接词', text='and',
             note='并列'),
        dict(role='谓语', text='helped them on the rest',
             note='help 帮助'),
    ])

A['P5S5'] = dict(
    zh='有时心灵比头脑更聪明。',
    insight=False, note='',
    bold=['the heart is smarter than'],
    chunks=[
        dict(role='状语', text='Sometimes',
             note='时间状语'),
        dict(role='主语', text='the heart',
             note='喻指情感/直觉'),
        dict(role='谓语', text='is smarter than the head',
             note='比较结构，head 喻指理智'),
    ])
