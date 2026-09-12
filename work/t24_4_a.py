# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 4 —— 逐句成分划分与重点词释义（前半：P1–P2）。

口径（与用户确认过，见 CLAUDE.md / BUILD_GUIDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""

# key = 句子 id (段落 P1..P5 + 句序)
# zh        : 本句中文翻译（从 raw 段落 zh 按句切分，不自行翻译）
# insight   : 是否为 PDF「真题句逐层精讲」选中的句子
# note      : 精讲考点文字（取自 PDF insights）
# bold      : 重点单词/词组（须为 en 的子串）
# chunks    : 成分划分，按出现顺序；role 见 app.js 的 ROLE_COLORS
A = {}

A['P1S1'] = dict(
    zh='如果你查看手机上的应用程序，很可能至少有一个与健康相关的应用——而且可能有好几个。',
    insight=True,
    note='本句结构高度典型：If引导的条件状语从句+主句+省略that的宾语从句，这种组合在四六级和考研真题中频繁出现。chances are这一固定搭配及其后接从句的用法也是常考点。掌握本句结构可迁移到大量同类句式',
    bold=['chances are', 'related to'],
    chunks=[
        dict(role='状语从句', text='If you look at the apps on your phone',
             note='If 引导的条件状语从句'),
        dict(role='主语', text='chances'),
        dict(role='谓语', text="are", note='chances are 固定搭配「很可能」'),
        dict(role='宾语从句', text='you have at least one related to your health —and probably several',
             note='省略 that 的宾语从句；related to your health 为过去分词短语作后置定语修饰 one'),
    ])

A['P1S2'] = dict(
    zh='无论是心理健康应用、健身追踪器、联网健康设备还是其他什么，我们中的许多人都在利用这项技术以某种形式更好地追踪自己的健康状况。',
    insight=True,
    note='"Whether"引导让步状语从句置于句首、后接主句的结构在四六级和考研阅读中较为常见,且主句中不定式作目的状语、介词短语作方式状语也是典型用法。学生掌握本句的分析方法后,可以迁移到大量类似的让步状语从句和状语修饰结构上,具有较好的复用性。',
    bold=['Whether', 'taking advantage of', 'keep better track of'],
    chunks=[
        dict(role='状语从句', text='Whether it is a mental health app, a fitness tracker, a connected health device or something else',
             note='Whether 引导的让步状语从句'),
        dict(role='主语', text='many of us'),
        dict(role='谓语', text='are taking advantage of',
             note='take advantage of 利用'),
        dict(role='宾语', text='this technology'),
        dict(role='状语', text='to keep better track of our health',
             note='不定式作目的状语'),
        dict(role='状语', text='in some shape or form',
             note='介词短语作方式状语'),
    ])

A['P1S3'] = dict(
    zh='健康与护理应用审查组织最近的研究发现，市场上有35万个健康应用程序，其中仅2020年就推出了9万个。',
    insight=True,
    note='主句+宾语从句+非限制性定语从句的三层结构是学术文本和新闻报道的常见句式,特别是\'数据+of which+补充说明\'的模式在考试阅读中频繁出现。掌握后可迁移到大量类似真题句型,结构典型性高',
    bold=['Recent research', 'Organization for the Review of Care and Health Applications', 'available on the market'],
    chunks=[
        dict(role='主语', text='Recent research from the Organization for the Review of Care and Health Applications',
             note='from... 介词短语作后置定语修饰 research'),
        dict(role='谓语', text='found'),
        dict(role='宾语从句', text='that 350,000 health apps were available on the market',
             note='that 引导宾语从句'),
        dict(role='非限制性定语从句', text='90,000 of which launched in 2020 alone',
             note='which 指代 350,000 health apps；of which 表示「其中」'),
    ])

A['P2S1'] = dict(
    zh='虽然这些应用程序有很多好处，但我们输入的个人信息如何被收集、保护和在线共享并不总是清楚的。',
    insight=True,
    note='本句的 it is+形容词+how/whether 从句结构、被动语态并列、省略关系代词的定语从句、while引导的让步状语从句，都是四六级和考研阅读中的高频句式。掌握本句的拆解方法可以直接迁移到大量同类真题句，代表性很强。',
    bold=['While', 'it is not always clear', 'collected, safeguarded and shared'],
    chunks=[
        dict(role='状语从句', text='While these apps have a great deal to offer',
             note='While 引导的让步状语从句'),
        dict(role='形式主语', text='it'),
        dict(role='谓语', text='is not always clear',
             note='it is + 形容词 + 从句'),
        dict(role='主语从句', text='how the personal information we input is collected, safeguarded and shared online',
             note='how 引导主语从句；we input 为省略关系代词的定语从句修饰 information'),
    ])

A['P2S2'] = dict(
    zh='现有的健康隐私法律，如《健康保险携带和责任法案》，主要关注医院、诊所、门诊部和保险公司在线存储健康记录的方式。',
    insight=False, note='',
    bold=['Existing health privacy law', 'primarily focused on', 'the way'],
    chunks=[
        dict(role='主语', text='Existing health privacy law',
             note='existing 现有的'),
        dict(role='插入语', text='such as the Health Insurance Portability and Accountability Act',
             note='举例插入语'),
        dict(role='谓语', text='is primarily focused on',
             note='be focused on 关注于'),
        dict(role='宾语', text='the way hospitals, doctors\' offices, clinics and insurance companies store health records online',
             note='the way 后接定语从句（省略 in which）说明方式'),
    ])

A['P2S3'] = dict(
    zh='这些应用程序和健康数据追踪可穿戴设备收集的健康信息通常不会受到同样的法律保护。',
    insight=False, note='',
    bold=['health information', 'tracking wearables', 'legal protections'],
    chunks=[
        dict(role='主语', text='The health information these apps and health data tracking wearables are collecting',
             note='these apps ... are collecting 为省略关系代词的定语从句修饰 information'),
        dict(role='状语', text='typically', note='频度副词'),
        dict(role='谓语', text='does not receive'),
        dict(role='宾语', text='the same legal protections'),
    ])
