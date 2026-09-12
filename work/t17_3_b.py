# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S3'] = dict(
    zh='但尽管存在普遍的误解，间隔年并不会阻碍学业追求的成功——事实上，它可能会增强成功。',
    insight=True, note='破折号连接并列分句、用"infact"强化递进观点的写法在学术和考试文章中常见,是典型的论证句式。否定结构加递进强化的逻辑组合也是议论文的经典模式,学习后可迁移到阅读和写作中。',
    bold=['misconceptions', 'hinder', 'enhances'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语', text='despite common misconceptions,',
             note=''),
        dict(role='主语', text='a gap year',
             note=''),
        dict(role='谓语', text='does not hinder',
             note=''),
        dict(role='宾语', text='the success of academic pursuits –',
             note=''),
        dict(role='插入语', text='in fact, it probably enhances it.',
             note='破折号后为递进说明；it 指 gap year'),
    ])

A['P3S1'] = dict(
    zh='来自美国和澳大利亚的研究表明，经历间隔年的学生通常比没有经历间隔年的学生为大学做了更好的准备，并且在大学中表现更好。',
    insight=False, note='',
    bold=['better prepared for', 'perform better'],
    chunks=[
        dict(role='主语', text='Studies from the United States and Australia',
             note=''),
        dict(role='谓语', text='show',
             note=''),
        dict(role='宾语从句', text='that students who take a gap year are generally better prepared for and perform better in college than those who do not.',
             note='that 引导宾语从句；who take... 定语从句修饰 students；than those who do not 比较结构'),
    ])

A['P3S2'] = dict(
    zh='间隔年不是把学生拉回来，而是通过让他们为独立、新责任和环境变化做好准备来推动他们前进——这些都是大一新生往往最难应对的事情。',
    insight=True, note='句子成分丰富：主句包含对比状语、主语、谓语、宾语、方向状语、方式状语和同位语；定语从句包含关系代词作宾语的结构。特别是"Ratherthan"引导的对比状语、"by"引导的方式状语、破折号引出的同位语，以及关系代词在从句中充当介词宾语，都是值得练习的典型成分和易错点。',
    bold=['pushes them ahead', 'struggle with'],
    chunks=[
        dict(role='状语', text='Rather than pulling students back,',
             note='rather than + 动名词表对比'),
        dict(role='主语', text='a gap year',
             note=''),
        dict(role='谓语', text='pushes',
             note=''),
        dict(role='宾语', text='them',
             note=''),
        dict(role='状语', text='ahead',
             note=''),
        dict(role='状语', text='by preparing them for independence, new responsibilities and environmental changes –',
             note='by + 动名词表方式；prepare sb. for 使…为…做好准备'),
        dict(role='同位语', text='all things that first-year students often struggle with the most.',
             note='all things 作同位语；that... 定语从句（介词 with 的宾语为关系代词）'),
    ])

A['P3S3'] = dict(
    zh='间隔年经历可以减轻适应大学和被投入全新环境时的冲击，使人更容易专注于学业和活动，而不是适应过程中的失误。',
    insight=True, note="本句结构高度典型:主句+状语从句+分词短语状语的组合是四六级和考研阅读中的高频句式,'whenitcomesto'固定搭配和现在分词作结果状语也是常考点,掌握后可广泛迁移到类似长难句的分析。",
    bold=['lessen the blow', 'acclimation blunders'],
    chunks=[
        dict(role='主语', text='Gap year experiences',
             note=''),
        dict(role='谓语', text='can lessen the blow',
             note=''),
        dict(role='状语从句', text='when it comes to adjusting to college and being thrown into a brand new environment,',
             note='when it comes to + 动名词；being thrown into 动名词被动式'),
        dict(role='状语', text='making it easier to focus on academics and activities rather than acclimation blunders.',
             note='现在分词作结果状语；it 形式宾语；rather than 对比'),
    ])

A['P4S1'] = dict(
    zh='如果你不相信用一年时间探索兴趣的内在价值，那么请考虑它对未来学业选择的财务影响。',
    insight=True, note='条件状语从句加主句的结构在四六级和考研真题中非常常见，且本句的"if...then..."搭配是典型的条件关系表达方式。祈使句在建议类语境中也较为高频。掌握本句结构后可迁移到大量类似句式。',
    bold=['inherent value', 'financial impact'],
    chunks=[
        dict(role='状语从句', text="If you're not convinced of the inherent value in taking a year off to explore interests,",
             note='if 条件状语从句；be convinced of 相信；in taking... 动名词作介词宾语'),
        dict(role='连接词', text='then',
             note=''),
        dict(role='谓语', text='consider',
             note=''),
        dict(role='宾语', text='its financial impact on future academic choices.',
             note='祈使句；its 指 a gap year'),
    ])
