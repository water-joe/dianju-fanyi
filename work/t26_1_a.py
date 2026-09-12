# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='问人们关于公共图书馆的看法，某种印象便会浮现在脑海中:尘封的、过时的，那种你小时候喜欢的地方，但就像英国的海滨小镇一样，你现在还会去那里吗？',
    insight=False, note='',
    bold=['springs to mind', 'old-fashioned', 'seaside town'],
    chunks=[
        dict(role='状语', text='Ask people about public libraries',
             note='祈使句作条件含义（=If you ask...）'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='a certain image',
             note=''),
        dict(role='谓语', text='springs to mind:',
             note=''),
        dict(role='同位语', text='dusty, old-fashioned, the sort of place you enjoyed as a child but, rather like a British seaside town, would you go there now?',
             note='对 image 的展开说明；you enjoyed... 省略关系词的定语从句'),
    ])

A['P1S2'] = dict(
    zh='而且不管怎样——它们不是都在关闭吗？',
    insight=True, note='一般疑问句在日常和考试中较常见，现在进行时否定疑问形式具有一定代表性，适合巩固疑问句倒装和时态辨识。但作为简单句，缺乏从句、复杂修饰等高频考点，典型性中等。',
    bold=["aren't they all closing"],
    chunks=[
        dict(role='状语', text='And anyway —',
             note='「而且不管怎样」'),
        dict(role='谓语', text="aren't",
             note='否定疑问倒装：are not 提前'),
        dict(role='主语', text='they all',
             note=''),
        dict(role='表语', text='closing?',
             note='现在进行时'),
    ])

A['P2S1'] = dict(
    zh='现实情况截然不同，正如我在文化部委托我对英格兰公共图书馆进行独立审查时所发现的那样，该审查于昨日发布。',
    insight=True, note='本句结构在考研和四六级真题中高度典型：主句+非限制性定语从句（"as"引导）+嵌套状语从句（"when"引导）+非谓语后置定语，这一层层展开的复合结构是学术和新闻语体的常见句式，掌握后可大量迁移至阅读理解和长难句分析。',
    bold=['startlingly', 'commissioned me to', 'independent review'],
    chunks=[
        dict(role='主语', text='The reality',
             note=''),
        dict(role='谓语', text='is startlingly different,',
             note=''),
        dict(role='定语从句', text='as I discovered when the culture department commissioned me to conduct an independent review of English public libraries, published yesterday.',
             note='as 引导非限制性定语从句（指代整个主句）；内嵌 when 状语从句；commission sb. to do；published yesterday 过去分词作后置定语'),
    ])

A['P2S2'] = dict(
    zh='当我走访全国各地的图书馆时，我惊讶地了解到图书馆的数量(2892家)是麦当劳分店数量的两倍多。',
    insight=True, note='“As...,Iwas+adj+todo+that-clause”是真题中描述个人见闻和客观事实的极其典型的复合句式。',
    bold=['up and down the country', 'more than twice the number of'],
    chunks=[
        dict(role='状语从句', text='As I visited libraries up and down the country,',
             note='as 引导时间状语从句'),
        dict(role='主语', text='I',
             note=''),
        dict(role='谓语', text='was surprised to learn',
             note='be surprised to do'),
        dict(role='宾语从句', text="there are more than twice the number of libraries (2,892) as there are branches of McDonald's.",
             note='more than twice as many... as 结构的变体（twice the number... as）'),
    ])

A['P3S1'] = dict(
    zh='走进其中任何一家，你都会发现一片繁忙的景象。',
    insight=False, note='',
    bold=['a hive of activity'],
    chunks=[
        dict(role='状语', text='Enter any one of them',
             note='祈使句作条件含义'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text='will find',
             note=''),
        dict(role='宾语', text='a hive of activity.',
             note='a hive of 一片（忙碌的）…'),
    ])

A['P3S2'] = dict(
    zh='虽然书籍现在是、而且应该永远是任何图书馆的核心，但图书馆还提供众多其他服务:就业咨询、语言课程或数字访问和支持。',
    insight=False, note='',
    bold=['a multitude of'],
    chunks=[
        dict(role='状语从句', text='While books are, and should always be, at the heart of any library,',
             note='while 引导让步状语从句；并列谓语 are... and should always be...'),
        dict(role='主语', text='a multitude of other services',
             note=''),
        dict(role='谓语', text='are offered:',
             note='被动语态'),
        dict(role='同位语', text='employment advice, language classes or digital access and support.',
             note='对 services 的举例说明'),
    ])

A['P4S1'] = dict(
    zh='有些图书馆设有商业和知识产权中心，可以帮助企业主和创业者。',
    insight=True, note='therebe存在句加非限制性定语从句是四六级和考研阅读中的常见句式,用于引出话题并补充说明。这种结构在说明文和议论文中频繁出现,掌握后可应用于大量类似句子的理解和写作,具有较高的迁移价值。',
    bold=['intellectual property', 'entrepreneurs'],
    chunks=[
        dict(role='谓语', text='There are',
             note=''),
        dict(role='主语', text='libraries with business and intellectual property centres,',
             note=''),
        dict(role='定语从句', text='which can help business owners and entrepreneurs.',
             note='which 引导非限制性定语从句'),
    ])
