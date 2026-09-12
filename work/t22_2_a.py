# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 2 —— P1 至 P3 的逐句成分划分与重点词释义。
口径：嵌套成分合并为一块（子结构写进 note）；引述分句各标各的主谓语。"""

A = {}

A['P1S1'] = dict(
    zh='越来越多的美国人选择工作到退休之后很久，这一日益增长的趋势可能颠覆旧的劳动力模式。',
    insight=True,
    note='本句展示了主句加限制性定语从句的常见结构，同位语加定语从句的组合在考试阅读中频繁出现。不定式作宾语和关系代词引导定语从句都是四六级和考研的高频考点，结构典型性较高。',
    bold=['opting', 'well into retirement', 'upend', 'workforce model'],
    chunks=[
        dict(role='主语', text='More Americans'),
        dict(role='谓语', text='are opting'),
        dict(role='状语', text='to work well into retirement',
             note='不定式作状语，well into retirement 为时间补语'),
        dict(role='同位语', text='a growing trend that threatens to upend the old workforce model',
             note='补充说明主句；that 引导定语从句修饰 trend'),
    ])

A['P2S1'] = dict(
    zh='根据 Harris Poll 为 TD Ameritrade 做的一项调查，年满 40 岁的美国人中，有三分之一已经或计划在退休后找一份工作，为更长的寿命做准备。',
    insight=False, note='',
    bold=['at least 40', 'plan to', 'prepare for', 'a longer life'],
    chunks=[
        dict(role='主语', text='One in three Americans who are at least 40'),
        dict(role='谓语', text='have or plan to have'),
        dict(role='宾语', text='a job in retirement'),
        dict(role='状语', text='to prepare for a longer life'),
        dict(role='状语', text='according to a survey conducted by Harris Poll for TD Ameritrade',
             note='according to... 作状语；conducted by... 为过去分词短语修饰 survey'),
    ])

A['P2S2'] = dict(
    zh='更令人惊讶的是，调查显示，超过半数的"不退休者"——那些计划在退休后工作或退休后重返岗位的人——表示即使有足够的钱安顿下来，他们也会在晚年继续受雇，',
    insight=True,
    note='涵盖了倒装结构、长主语从句、同位语、定语从句、省略 that 的宾语从句、虚拟让步状语从句以及插入式说明语。是极佳的综合成分拆解练习句。',
    bold=['Even more surprising', 'unretirees', 'settle down', 'the survey showed'],
    chunks=[
        dict(role='表语', text='Even more surprising', note='表语前置，主句为倒装'),
        dict(role='谓语', text='is', note='系动词，与前置表语构成倒装'),
        dict(role='主语', text='that more than half of "unretirees"—those who plan to work in retirement or went back to work after retiring—said they would be employed in their later years even if they had enough money to settle down',
             note='that 引导主语从句；其中 those who... 为同位语解释 unretirees，said 后省略 that 的宾语从句含 even if 虚拟让步从句'),
        dict(role='插入语', text='the survey showed'),
    ])

A['P3S1'] = dict(
    zh='经济需求并非"不退休"趋势的唯一原因。',
    insight=True,
    note='主系表加状语的简单句在真题中较为常见，具有一定代表性；但本句用词较为口语化（"culprit"、"unretirement"等新造词），且结构过于简单，迁移价值低于包含从句或复杂修饰的典型句式。',
    bold=['culprit', 'unretirement'],
    chunks=[
        dict(role='主语', text='Financial needs'),
        dict(role='谓语', text="aren't", note='are not 缩略'),
        dict(role='表语', text='the only culprit'),
        dict(role='状语', text='for the "unretirement" trend', note='原因状语'),
    ])

A['P3S2'] = dict(
    zh='根据该研究，其他原因包括个人成就感，如保持精神健康、防止无聊或避免抑郁。',
    insight=True,
    note='主谓宾加插入语、宾语后跟同位语解释的结构在四六级和考研阅读中高频出现，"such as"引导同位语列举也是标准考点句式。掌握本句的分析方法可直接迁移到大量真题句子中。',
    bold=['according to the study', 'personal fulfillment', 'such as', 'avoiding depression'],
    chunks=[
        dict(role='主语', text='Other reasons'),
        dict(role='插入语', text='according to the study'),
        dict(role='谓语', text='include'),
        dict(role='宾语', text='personal fulfillment such as staying mentally fit, preventing boredom or avoiding depression',
             note='such as... 为同位语，列举 fulfillment 的具体内容'),
    ])

A['P3S3'] = dict(
    zh='约 72% 的"不退休者"受访者表示，他们会在退休后重返工作以保持精神健康，而 59% 的人说这与维持生计有关。',
    insight=True,
    note='并列主句+宾语从句是四六级和考研阅读中的高频句式；间接引语中的时态呼应（主句过去时、从句过去将来时）以及"while"引导的对比并列结构都是典型考点；被动语态"would be tied to"的使用也符合学术和调查报告文体的常见模式。',
    bold=['respondents', 'once retired', 'keep mentally fit', 'tied to', 'making ends meet'],
    chunks=[
        dict(role='主语', text='About 72% of "unretiree" respondents'),
        dict(role='谓语', text='said', note='引述动词'),
        dict(role='宾语', text='that they would return to work once retired to keep mentally fit',
             note='said 后省略 that 的宾语从句；once retired 为省略的时间状语从句'),
        dict(role='连接词', text='while'),
        dict(role='主语', text='59%'),
        dict(role='谓语', text='said'),
        dict(role='宾语', text='it would be tied to making ends meet',
             note='it 指代 return to work；be tied to 被动语态'),
    ])
