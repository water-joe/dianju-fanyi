# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S2'] = dict(
    zh='"只需查看几个关键参数就可以创建一张有用的地图。"',
    insight=False, note='',
    bold=['key parameters'],
    chunks=[
        dict(role='主语', text='"A useful map',
             note=''),
        dict(role='谓语', text='can be created',
             note='情态被动'),
        dict(role='状语', text='by looking at even a few key parameters."',
             note='by + 动名词表方式'),
    ])

A['P5S3'] = dict(
    zh='例如，老年人口较多或非正式住所不能很好应对高温的社区可以获得特别警报或通过设立降温中心得到加强。',
    insight=True, note='本句主干识别有一定难度但不算极端,嵌套层级适中,时态语态涉及情态动词和主被动并列,成分丰富且包含常见易错点,结构在考试中高度典型。综合来看,这是一个难度适中、训练价值高、结构代表性强的优质练习句,值得优先用于结构和时态训练。',
    bold=['elderly population', 'informal dwellings', 'cooling centers'],
    chunks=[
        dict(role='状语', text='For example,',
             note=''),
        dict(role='主语', text='neighborhoods with a large elderly population or informal dwellings that cope poorly with heat',
             note='with... 介词短语作后置定语；that cope poorly... 定语从句修饰 dwellings'),
        dict(role='谓语', text='could get special warnings or be bolstered with cooling centers.',
             note='情态动词 + 主动被动并列谓语；bolster 增强'),
    ])

A['P5S4'] = dict(
    zh='那格浦尔项目已经创建了一张风险和脆弱性地图，这使Kotharkar能够告诉官员在今年夏季发生热浪时应关注哪些社区。',
    insight=True, note='非限制性定语从句补充说明、"enablesbtodo"结构、"疑问词+todo"作宾语从句,都是四六级和考研阅读中的高频句式,掌握后可大量复用于长难句分析',
    bold=['vulnerability map', 'in the event of', 'heat wave'],
    chunks=[
        dict(role='主语', text='The Nagpur project',
             note=''),
        dict(role='谓语', text='has already created',
             note=''),
        dict(role='宾语', text='a risk and vulnerability map,',
             note=''),
        dict(role='定语从句', text='which enabled Kotharkar to tell officials which neighborhoods to focus on in the event of a heat wave this summer.',
             note='which 引导非限制性定语从句；enable sb. to do；which neighborhoods to focus on 疑问词+不定式作宾语'),
    ])

A['P6S1'] = dict(
    zh='研究人员表示，高温行动计划不应仅包括短期应急响应，还应推荐可使社区更凉爽的中长期措施。',
    insight=False, note='',
    bold=['emergency responses', 'medium- to long-term measures'],
    chunks=[
        dict(role='谓语', text="HAPs shouldn't just include short-term emergency responses,",
             note=''),
        dict(role='主语', text='researchers',
             note='倒装引述分句主语'),
        dict(role='谓语', text='say,',
             note=''),
        dict(role='连接词', text='but',
             note=''),
        dict(role='谓语', text='also recommend medium- to long-term measures that could make communities cooler.',
             note='not just... but also... 并列谓语；that... 定语从句修饰 measures'),
    ])

A['P6S2'] = dict(
    zh='例如在那格浦尔，Kotharkar的团队已能够就在哪里种植树木以提供遮阴向市政官员提供建议。',
    insight=True, note='本句涵盖主语、谓语、宾语、地点状语、插入语和介词短语作状语，成分种类较为丰富；特别是"aboutwheretoplanttreestoprovideshade"这一多层嵌套的介词短语，可用于训练学生识别疑问词不定式结构和目的状语，具有一定练习价值。',
    bold=['advise', 'provide shade'],
    chunks=[
        dict(role='状语', text='In Nagpur, for example,',
             note=''),
        dict(role='主语', text="Kotharkar's team",
             note=''),
        dict(role='谓语', text='has been able to advise city officials about where to plant trees to provide shade.',
             note='about + 疑问词不定式短语作 advise 的补足成分；to provide shade 不定式作目的'),
    ])

A['P6S3'] = dict(
    zh='高温行动计划还可以指导房屋改造或修改建筑法规的工作。',
    insight=False, note='',
    bold=['retrofit', 'building regulations'],
    chunks=[
        dict(role='主语', text='HAPs',
             note=''),
        dict(role='谓语', text='could also guide efforts to retrofit homes or modify building regulations.',
             note='to retrofit... or (to) modify... 并列不定式作 efforts 的后置定语'),
    ])

A['P6S4'] = dict(
    zh='"在紧急情况下减少死亡是一个值得追求的目标，但这是最低目标。"气候研究员Chandni Singh说。',
    insight=False, note='',
    bold=['target'],
    chunks=[
        dict(role='主语', text='"Reducing deaths in an emergency',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='a good target to have, but it\'s the lowest target,"',
             note='to have 不定式作后置定语；but 连接并列分句'),
        dict(role='主语', text='says',
             note=''),
        dict(role='谓语', text='climate researcher Chandni Singh.',
             note='倒装引述（谓语 says 前置）'),
    ])
