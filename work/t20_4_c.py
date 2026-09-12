# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S2'] = dict(
    zh='与此同时，在2019年对乔治亚大学学生的一项调查中，就业办公室发现未来雇主最令人向往的特质是能够提供稳定的就业机会(其次是职业发展和培训，然后是鼓舞人心的目标)。',
    insight=True, note='主句+宾语从句（省略that）的结构在四六级和考研阅读中非常常见，特别是find/show/suggest/indicate等动词后接宾语从句的句式是典型的学术写作和新闻报道句式。句首介词短语状语也是高频结构，掌握后可大量复用到类似句子的分析中。',
    bold=['desirable trait', 'secure employment'],
    chunks=[
        dict(role='状语', text='In a 2019 survey of University of Georgia students, meanwhile,',
             note=''),
        dict(role='主语', text='the career office',
             note=''),
        dict(role='谓语', text='found',
             note=''),
        dict(role='宾语从句', text='the most desirable trait in a future employer was the ability to offer secure employment (followed by professional development and training, and then inspiring purpose).',
             note='省略 that 的宾语从句；to offer... 不定式作后置定语；括号内为 followed by 过去分词短语作补充'),
    ])

A['P3S3'] = dict(
    zh='工作保障或稳定性是第二重要的职业目标(工作与生活的平衡排名第一)，其次是致力于某项事业的使命感或为更大利益服务的良好感觉。',
    insight=True, note='本句涵盖主语(并列名词短语)、系动词、表语(名词短语)、插入语(括号内完整主系表)、过去分词短语作状语等成分,结构较丰富。过去分词短语followedby的状语用法以及括号插入语的识别,对基础较弱的学习者有一定练习价值,但整体难度不高,缺少易错的复杂修饰或多重嵌套。',
    bold=['job security', 'dedicated to a cause', 'the greater good'],
    chunks=[
        dict(role='主语', text='Job security or stability',
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='the second most important career goal',
             note=''),
        dict(role='插入语', text='(work-life balance was number one),',
             note='括号内为插入语，补充另一项数据'),
        dict(role='状语', text='followed by a sense of being dedicated to a cause or to feel good about serving the greater good.',
             note='followed by 过去分词短语作补充；being dedicated to... 动名词作介词宾语'),
    ])

A['P4S1'] = dict(
    zh='这与上一代人相比是一个巨大的变化。',
    insight=False, note='',
    bold=['a big change from'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text="'s",
             note=''),
        dict(role='表语', text='a big change from the previous generation.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='"千禧一代希望生活更加灵活，"英国品牌管理公司YouthSight的副主任Tanya Michelsen指出，该公司定期对英国青年进行60天调查，其研究结果同样适用于美国青年。',
    insight=False, note='',
    bold=['Associate Director', 'conducts regular'],
    chunks=[
        dict(role='宾语', text='"Millennials wanted more flexibility in their lives,"',
             note='直接引语作 notes 的宾语'),
        dict(role='谓语', text='notes',
             note='引述动词'),
        dict(role='主语', text='Tanya Michelsen,',
             note='引述分句主语'),
        dict(role='同位语', text='Associate Director of YouthSight, a UK-based brand manager that conducts regular 60-day surveys of British youth,',
             note='同位语；a UK-based brand manager 又作 YouthSight 的同位语；that... 定语从句修饰 manager'),
        dict(role='状语', text='in findings that might just as well apply to American youth.',
             note='that... 定语从句修饰 findings'),
    ])

A['P4S3'] = dict(
    zh='"Z世代正在寻求更多的确定性和稳定性，因为零工经济的兴起。',
    insight=True, note='三个独立主句线性排列、用代词承接的写法,在真题中较常见,便于学生练习代词回指和句间逻辑;第一句的现在进行时+原因状语、第二句的"havetroubledoing"句型,都是考试常考结构;但整体句式偏简单,缺少复杂从句或特殊结构,典型性中等。',
    bold=['certainty and stability', 'gig economy'],
    chunks=[
        dict(role='主语', text='"Generation Zs',
             note=''),
        dict(role='谓语', text='are looking for',
             note=''),
        dict(role='宾语', text='more certainty and stability,',
             note=''),
        dict(role='状语', text='because of the rise of the gig economy.',
             note='because of 介词短语作原因状语'),
    ])

A['P4S4'] = dict(
    zh='他们难以看到财务前景，而且相当规避风险。"',
    insight=False, note='',
    bold=['risk averse'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='have trouble seeing a financial future',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='they are quite risk averse."',
             note='have trouble doing 做…有困难；risk averse 规避风险'),
    ])
