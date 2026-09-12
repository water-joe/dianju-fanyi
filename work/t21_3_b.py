# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 3 — 逐句成分划分与重点词释义。
口径（与用户确认过，见 CLAUDE.md / BUILD_GUIDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""

# key = 句子 id ; zh 取自 raw 段落 zh 按句切分；bold/chunk.text 必须是 en 的连续子串
A = {}

A['P2S1'] = dict(
    zh=u'然而，这两款应用后来都被废弃了，微软表示已经在自己的产品中使用了它们的最佳功能。',
    insight=True,
    note=u'主句+after引导的时间状语从句+嵌套宾语从句是四六级和考研阅读中的高频句式。时间状语从句和宾语从句的组合、that省略、过去完成时表达时间先后等都是真题常见考点。句子长度和复杂度也符合真题典型水平,学习后可大量复用到其他句子的理解中。',
    bold=['scrapped', 'after', 'said'],
    chunks=[
        dict(role='状语', text='Both apps, however,', note='however 为插入性状语'),
        dict(role='谓语', text='were later scrapped', note='被动语态，scrapped 废弃'),
        dict(role='状语从句', text='after Microsoft said it had used their best features in its own products',
             note='after 引导时间状语从句；said 后省略 that 的宾语从句；had used 过去完成时表先后'),
    ])

A['P2S2'] = dict(
    zh=u'它们的工程师团队留了下来，使它们成为最大型公司为满足对技术人才的巨大需求而采用的众多"收购即招聘"案例中的两个。',
    insight=False, note='',
    bold=['stayed on', 'making them', 'acqui-hires'],
    chunks=[
        dict(role='主语', text='Their teams of engineers'),
        dict(role='谓语', text='stayed on'),
        dict(role='状语', text='making them two of the many "acqui-hires" that the biggest companies have used to feed their great hunger for tech talent',
             note='现在分词短语作结果状语；that... 定语从句修饰 acqui-hires；to feed... 不定式表目的'),
    ])

A['P3S1'] = dict(
    zh=u'在微软的批评者看来，Wunderlist和Sunrise的命运是大型科技公司无情吞噬任何挡在其道路上的创新公司的例证。',
    insight=False, note='',
    bold=["To Microsoft's critics", 'remorseless', 'chew up'],
    chunks=[
        dict(role='状语', text="To Microsoft's critics", note='介词短语作状语，表"在…看来"'),
        dict(role='主语', text='the fates of Wunderlist and Sunrise'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='examples of a remorseless drive by Big Tech to chew up any innovative companies that lie in their path',
             note='of... 介词短语与后置定语；that lie in their path 定语从句修饰 companies'),
    ])

A['P3S2'] = dict(
    zh=u'"他们买下幼苗然后关闭它们，"旧金山SwitchVentures的合伙人Paul Arnold抱怨道，终结了那些有朝一日可能成为竞争对手的企业。',
    insight=True,
    note=u'本句涵盖倒装结构、直接引语作宾语从句、并列谓语、同位语、分词短语作状语、限制性定语从句等多种成分，成分种类丰富。尤其倒装结构和分词短语嵌套定语从句是学生易混淆的点，适合作为划分成分的综合练习。',
    bold=['complained', 'a partner at', 'putting an end to'],
    chunks=[
        dict(role='宾语', text='"They bought the seedlings and closed them down,"',
             note='直接引语作 complained 的宾语'),
        dict(role='谓语', text='complained', note='主句谓语（引述动词）'),
        dict(role='主语', text='Paul Arnold', note='主句主语'),
        dict(role='同位语', text='a partner at San Francisco-based Switch Ventures', note='说明 Paul Arnold 身份'),
        dict(role='状语', text='putting an end to businesses that might one day turn into competitors',
             note='现在分词短语作结果状语；that... 定语从句修饰 businesses'),
    ])

A['P3S3'] = dict(
    zh=u'微软拒绝置评。',
    insight=False, note='',
    bold=['declined to comment'],
    chunks=[
        dict(role='主语', text='Microsoft'),
        dict(role='谓语', text='declined to comment', note='decline to do 拒绝做'),
    ])

A['P4S1'] = dict(
    zh=u'与其他初创企业投资者一样，Arnold先生自己的业务往往依赖于将初创企业出售给更大的科技公司，尽管他承认对结果心情复杂:"我认为如果我戴上自私的帽子，这些事情对我有利。但它们对美国经济有利吗？我不知道。"',
    insight=True,
    note=u'本句涵盖了主语、谓语、宾语、表语、状语（包括让步、条件、方式等多种类型）、宾语从句等多种成分，且存在动名词短语作宾语、形容词短语作表语、介词短语作状语等常见结构。尤其是宾语从句嵌套条件从句的结构，以及并列主句的划分，都是值得练习的典型成分识别点。',
    bold=['depends on', 'selling', 'mixed feelings'],
    chunks=[
        dict(role='状语', text='Like other start-up investors', note='介词短语作比较状语'),
        dict(role='主语', text="Mr. Arnold's own business"),
        dict(role='谓语', text='often depends on', note='depend on 取决于/依赖'),
        dict(role='宾语', text='selling start-ups to larger tech companies',
             note='动名词短语 selling... 作宾语'),
        dict(role='状语从句', text='though he admits to mixed feelings about the result',
             note='though 引导让步状语从句'),
        dict(role='宾语', text=': "I think these things are good for me, if I put my selfish hat on.',
             note='冒号后直接引语作 admits to 的宾语；内嵌 if 条件状语从句'),
    ])
