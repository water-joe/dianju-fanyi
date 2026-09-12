# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S1'] = dict(
    zh='英国皇家园艺学会的这一决定正值活动人士试图提高人们对人造草所造成问题的认识之际。',
    insight=True, note='as引导的时间或原因状语从句、嵌套定语从句、不定式作宾语都是四六级和考研真题中的高频结构，句式代表性强，学习后可迁移到大量类似句子。',
    bold=['comes as', 'raise awareness of'],
    chunks=[
        dict(role='主语', text="The RHS's decision",
             note=''),
        dict(role='谓语', text='comes',
             note=''),
        dict(role='状语从句', text='as campaigners try to raise awareness of the problems fake grass causes.',
             note='as 引导时间状语从句；to raise... 不定式作 try 的宾语；(that) fake grass causes 省略关系词的定语从句'),
    ])

A['P3S2'] = dict(
    zh='一个声称要"揭穿"人造草"漂绿行为"的Twitter账号已经拥有超过两万名关注者。',
    insight=True, note='非限制性定语从句插入主语和谓语之间的结构,在四六级和考研真题中属于常见句式。这种结构既考查学生识别从句边界的能力,又考查跳过修饰定位主干的能力,是阅读理解和翻译题中的典型难点。掌握这种句式后,可以应对大量类似的插入结构和定语从句题目,迁移价值较高',
    bold=['greenwash', 'followers'],
    chunks=[
        dict(role='主语', text='A Twitter account,',
             note=''),
        dict(role='定语从句', text='which claims to "cut through the greenwash" of artificial grass,',
             note='which 引导非限制性定语从句插入主谓之间'),
        dict(role='状语', text='already',
             note=''),
        dict(role='谓语', text='has more than 20,000 followers.',
             note=''),
    ])

A['P3S3'] = dict(
    zh='该账号正试图鼓励人们签署两份请愿书，一份呼吁禁止销售塑料草坪，另一份呼吁对此类草坪征收"生态破坏"税。',
    insight=True, note='本句覆盖主语、谓语、宾语、宾语补足语、同位语等多种成分，尤其是双同位语并列结构和不定式作宾补，适合练习成分划分。但句中无定语从句、状语从句等易错高频结构，训练价值中等偏上。',
    bold=['petitions', 'ecological damage'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='is trying to encourage people to sign two petitions,',
             note='encourage sb. to do 宾补结构'),
        dict(role='同位语', text='one calling for a ban on the sale of plastic grass',
             note='one 指代一份请愿书；calling for... 现在分词作后置定语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='同位语', text='another calling for an "ecological damage" tax on such lawns.',
             note='another 与 one 并列；calling for... 后置定语'),
    ])

A['P3S4'] = dict(
    zh='这两份请愿书已分别征集到7276和11282个签名。',
    insight=False, note='',
    bold=['signatures'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='have gathered',
             note=''),
        dict(role='宾语', text='7,276 and 11,282 signatures.',
             note=''),
    ])

A['P4S1'] = dict(
    zh='然而，人造草的支持者指出，天然草坪也会产生环境影响，因为需要修剪，因此通常会消耗电力或汽油。',
    insight=True, note='主句+that宾语从句+非限制性定语从句的三层嵌套结构在四六级和考研阅读中极为常见，pointoutthat、thereis存在句、逗号which引导补充说明均为高频句式，掌握后可大量迁移至同类长难句分析。',
    bold=['point out', 'consume electricity'],
    chunks=[
        dict(role='状语', text='However,',
             note=''),
        dict(role='主语', text='supporters of fake grass',
             note=''),
        dict(role='谓语', text='point out',
             note=''),
        dict(role='宾语从句', text='that there is also an environmental impact with natural lawns,',
             note='that 引导宾语从句；there be 句型'),
        dict(role='定语从句', text='which need mowing and therefore usually consume electricity or petrol.',
             note='which 引导非限制性定语从句修饰 lawns'),
    ])

A['P4S2'] = dict(
    zh='该行业还指出，真草需要大量的水、除草剂或其他处理，而铺设人造草的人往往会更多地使用他们的花园。',
    insight=True, note='点明观点加宾语从句并列的结构是四六级和考研阅读中的高频句式,尤其在议论文和说明文中常见。定语从句嵌套在宾语从句中也是典型的复杂句特征,掌握后可迁移到大量同类句式',
    bold=['considerable amounts of', 'lay fake grass'],
    chunks=[
        dict(role='主语', text='The industry',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='points out',
             note=''),
        dict(role='宾语从句', text='that real grass requires considerable amounts of water, weed killer or other treatments',
             note='第一个 that 宾语从句'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='宾语从句', text='that people who lay fake grass tend to use their garden more.',
             note='第二个并列 that 宾语从句；who... 定语从句修饰 people'),
    ])

A['P4S3'] = dict(
    zh='该行业还声称，铺设人造草的人平均会花费500英镑购买树木或灌木来装点花园，这为昆虫提供了栖息地。',
    insight=True, note='本句时态不难，但结构拆解价值高，尤其适合训练“先抓主干，再识别从句层级”的基本功。对结构阅读能力提升很有代表性，因此值得优先练习。',
    bold=['shrubs', 'habitat for insects'],
    chunks=[
        dict(role='主语', text='The industry',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='claims',
             note=''),
        dict(role='宾语从句', text='that people who lay fake grass spend an average of £500 on trees or shrubs for their garden,',
             note='that 宾语从句；who... 定语从句修饰 people'),
        dict(role='定语从句', text='which provides habitat for insects.',
             note='which 引导非限制性定语从句'),
    ])
