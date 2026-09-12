# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S1'] = dict(
    zh='这必须从如何最大化国民健康这一问题开始，而不是"修复"NHS。',
    insight=True, note='本句包含主语、情态动词谓语、方式状语、嵌入的宾语从句,从句内部又有主谓宾结构和方式状语,成分丰富;"ratherthan"对比结构和间接疑问从句的处理是常见易错点,训练价值较高',
    bold=['maximise', 'rather than'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='must begin with the question of how we maximise the health of the nation,',
             note='how 引导宾语从句作介词宾语'),
        dict(role='状语', text='rather than "fix" the NHS.',
             note='rather than 而非'),
    ])

A['P5S2'] = dict(
    zh='例如，据估计，医疗服务仅占健康结果的约20%。',
    insight=True, note='"Itisestimatedthat..."是学术写作、四六级阅读中极高频出现的句式，极具迁移价值。',
    bold=['It is estimated', 'accounts for'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text='is estimated,',
             note=''),
        dict(role='插入语', text='for example,',
             note='插入举例'),
        dict(role='主语从句', text='that healthcare accounts for only about 20% of health outcomes.',
             note='that 从句为真正主语；account for 占比'),
    ])

A['P5S3'] = dict(
    zh='更重要的是我们生活、工作和社交的场所——然而政府并没有明确的跨部门战略来改善这些健康的社会决定因素。',
    insight=True, note='本句包含倒装结构、Therebe句型、并列定语从句、主语从句省略、关系副词省略等多种成分划分的重点和易错点，既覆盖了主系表和存在句两种基本句型，又涉及修饰成分的识别和省略成分的还原，是很好的综合练习句。',
    bold=['socialise', 'cross- government strategy', 'social determinants'],
    chunks=[
        dict(role='表语', text='Much more important',
             note='前置表语（倒装）'),
        dict(role='谓语', text='are',
             note=''),
        dict(role='主语', text='the places we live, work and socialise—',
             note='(where) we live... 省略关系副词的定语从句'),
        dict(role='连接词', text='yet',
             note=''),
        dict(role='谓语', text='there is',
             note=''),
        dict(role='主语', text='no clear cross- government strategy for improving these social determinants of health.',
             note='there be 句型真正主语'),
    ])

A['P5S4'] = dict(
    zh='更糟糕的是，当像国家肥胖战略这样的政策被废弃时，纳税人就要承担治疗由此导致的疾病(如糖尿病)的沉重代价。',
    insight=False, note='',
    bold=['scrapped', 'price tag', 'diabetes'],
    chunks=[
        dict(role='状语', text='Worse,',
             note='评注性状语'),
        dict(role='状语从句', text='when policies like the national obesity strategy are scrapped,',
             note='when 引导时间状语从句（被动）'),
        dict(role='主语', text='taxpayers',
             note=''),
        dict(role='谓语', text='are left with the heavy price tag of treating the illnesses, like diabetes, that result.',
             note='be left with 承担/留下；that result 定语从句修饰 illnesses'),
    ])

A['P6S1'] = dict(
    zh='Reform希望探讨权力和资源应该如何在我们的卫生系统中分配。',
    insight=False, note='',
    bold=['distributed'],
    chunks=[
        dict(role='主语', text='Reform',
             note=''),
        dict(role='谓语', text='wants to ask',
             note=''),
        dict(role='宾语从句', text='how power and resources should be distributed in our health system.',
             note='how 引导宾语从句（被动语态）'),
    ])

A['P6S2'] = dict(
    zh='哪些卫生职能应该保留在中央，哪些应该交给地方领导者——他们通常负责创造健康的服务，并且对其人群的需求有更好的了解？',
    insight=True, note='两个并列的特殊疑问句，一个主动一个被动，是考试中常见的对比性并列结构。定语从句修饰名词、介词短语作定语、情态动词的被动形式，这些都是四六级和考研阅读中的高频句式。句子整体结构具有很强的代表性，掌握后可迁移到大量类似长难句的分析中。',
    bold=['health functions', 'local leaders'],
    chunks=[
        dict(role='主语', text='What health functions',
             note=''),
        dict(role='谓语', text='should remain at the centre,',
             note='remain 系动词用法'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='what',
             note=''),
        dict(role='谓语', text='should be given to local leaders,',
             note='情态动词被动式'),
        dict(role='定语从句', text='often responsible for services that create health, and with a much better understanding of the needs of their populations?',
             note='形容词短语作后置定语修饰 leaders；that create health 定语从句修饰 services'),
    ])
