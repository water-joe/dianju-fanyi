# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 4 —— P1 至 P2 的逐句成分划分与重点词释义。
口径：嵌套成分合并为一块（子结构写进 note）；引述分句各标各的主谓语。"""

A = {}

A['P1S1'] = dict(
    zh='尽管伦理课程在世界各地很常见，但科学家们不确定这些课程是否真的能改变行为；无论哪种方向的证据都很薄弱，依赖于人为设计的实验室测试或有时不可靠的自我报告。',
    insight=True,
    note='本句结构高度典型。分号连接并列句、让步状语从句前置、宾语从句嵌套、分词短语作状语，这些都是四六级和考研阅读中的高频句式。并列复合句加从句嵌套的组合是学术文本的标准配置，掌握本句结构后可直接迁移到大量真题句子。',
    bold=['Although', 'ethics classes', 'unsure', 'behavior', 'contrived', 'self-reports'],
    chunks=[
        dict(role='状语从句', text='Although ethics classes are common around the world',
             note='让步状语从句'),
        dict(role='主语', text='scientists'),
        dict(role='谓语', text='are unsure'),
        dict(role='宾语', text='if their lessons can actually change behavior',
             note='if 引导宾语从句（是否）'),
        dict(role='连接词', text=';'),
        dict(role='主语', text='evidence either way'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='weak'),
        dict(role='状语', text='relying on contrived laboratory tests or sometimes unreliable self-reports',
             note='现在分词短语作状语，说明证据薄弱的原因'),
    ])

A['P1S2'] = dict(
    zh='但发表在《认知》期刊上的一项新研究发现，至少在一种真实世界的情况下，一堂伦理课可能产生了持久的影响。',
    insight=True,
    note='"主句+that 宾语从句"是四六级和考研阅读中高频出现的句式。主语带后置定语、从句中插入状语也是真题常见特征。情态动词加完成式的用法在学术性文本中经常用于表达推测，具有较高的复用价值。掌握此句型可迁移到大量同类句子的理解中。',
    bold=['published in Cognition', 'found', 'real-world', 'lasting effects'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='a new study published in Cognition',
             note='published in Cognition 为过去分词短语作后置定语'),
        dict(role='谓语', text='found'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='状语', text='in at least one real-world situation'),
        dict(role='主语', text='a single ethics lesson'),
        dict(role='谓语', text='may have had', note='情态动词+现在完成时，表推测'),
        dict(role='宾语', text='lasting effects'),
    ])

A['P2S1'] = dict(
    zh='研究人员调查了一堂课对吃肉行为的影响。',
    insight=False, note='',
    bold=['investigated', 'impact', 'eating meat'],
    chunks=[
        dict(role='主语', text='The researchers'),
        dict(role='谓语', text='investigated'),
        dict(role='宾语', text="one class session's impact on eating meat"),
    ])

A['P2S2'] = dict(
    zh='根据该研究的共同作者、加州大学河滨分校哲学家 Eric Schwitzgebel 的说法，他们选择这一特定行为有三个原因：学生对该话题的态度是可变且不稳定的，行为易于测量，且伦理学文献大体认同少吃肉是好的，因为它减少了环境危害和动物痛苦。',
    insight=False, note='',
    bold=['for three reasons', 'co-author', 'philosopher', 'variable', 'easily measurable', 'ethics literature', 'environmental harm', 'animal suffering'],
    chunks=[
        dict(role='主语', text='They'),
        dict(role='谓语', text='chose'),
        dict(role='宾语', text='this particular behavior'),
        dict(role='状语', text='for three reasons'),
        dict(role='插入语', text='according to study co-author Eric Schwitzgebel, a philosopher at the University of California, Riverside',
             note='according to... 作插入语；a philosopher... 为同位语'),
        dict(role='同位语', text=': students\' attitudes on the topic are variable and unstable, behavior is easily measurable, and ethics literature largely agrees that eating less meat is good because it reduces environmental harm and animal suffering',
             note='冒号后解释 three reasons；内含并列句与 that 宾语从句、because 原因状语从句'),
    ])

A['P2S3'] = dict(
    zh='在四个大型哲学课堂中，一半学生阅读了一篇关于工厂化养殖肉类伦理的文章，自愿观看了一个 11 分钟的相关视频，并参加了 50 分钟的讨论。',
    insight=False, note='',
    bold=['read an article', 'optionally', 'joined', 'discussion'],
    chunks=[
        dict(role='主语', text='Half of the students in four large philosophy classes'),
        dict(role='谓语', text='read an article on the ethics of factory-farmed meat'),
        dict(role='连接词', text=', optionally'),
        dict(role='谓语', text='watched an 11-minute video on the topic'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='joined a 50-minute discussion'),
    ])

A['P2S4'] = dict(
    zh='另一半则专注于慈善捐赠。',
    insight=False, note='',
    bold=['focused on', 'charitable giving'],
    chunks=[
        dict(role='主语', text='The other half'),
        dict(role='谓语', text='focused on'),
        dict(role='宾语', text='charitable giving instead'),
    ])

A['P2S5'] = dict(
    zh='然后，在学生不知情的情况下，研究人员研究了他们那个学期的匿名餐卡购买记录——近 500 名学生的近 14000 张收据。',
    insight=True,
    note='简单句中嵌入插入语和破折号补充说明是考试阅读中常见的句式，能训练学生在干扰信息中提取主干的能力。这种结构在四六级和考研真题中有一定代表性，掌握后可迁移到类似长句的分析，具有中等偏上的典型性。',
    bold=['unknown to the students', 'anonymized', 'meal-card purchases', 'receipts'],
    chunks=[
        dict(role='状语', text='Then'),
        dict(role='插入语', text='unknown to the students'),
        dict(role='主语', text='the researchers'),
        dict(role='谓语', text='studied'),
        dict(role='宾语', text='their anonymized meal-card purchases for that semester—nearly 14,000 receipts for almost 500 students',
             note='meal-card purchases 后接 for that semester 定语；破折号后 nearly 14,000 receipts... 补充说明'),
    ])
