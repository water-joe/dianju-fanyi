# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 1 —— 逐句成分划分与重点词释义。

口径（与用户确认过，见 CLAUDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
  3. 状语插在谓词中间时整体作一个谓语块（如 are now falling）
"""

A = {}

A['P2S6'] = dict(
    zh='在2012年前夕，每周参加体育运动的成年人数量确实增加了近200万，但总人口增长更快。',
    insight=True, note='并列复合句结构在四六级和考研阅读中高频出现,尤其是"先肯定再but转折"的论证模式非常典型。第一主句中"主语包含介词短语和分词定语"以及"状语补充说明数据"的结构,也是学术和新闻类文本的常见句式。掌握本句的分析方法可迁移到大量类似真题句。',
    bold=['did rise', 'in the run-up to', 'growing'],
    chunks=[
        dict(role='主语', text='The number of adults doing weekly sport',
             note='of adults... 为介词短语作后置定语；doing weekly sport 为现在分词短语修饰 adults'),
        dict(role='谓语', text='did rise',
             note='did 为强调助动词，加强肯定语气'),
        dict(role='状语', text='by nearly 2 million in the run-up to 2012',
             note='by... 表增幅；in the run-up to 2012 表时间'),
        dict(role='连接词', text='but',
             note='转折连词，引出第二个并列分句'),
        dict(role='主语', text='the general population',
             note=''),
        dict(role='谓语', text='was growing',
             note=''),
        dict(role='状语', text='faster',
             note='比较状语'),
    ])

A['P2S7'] = dict(
    zh='更糟的是，现在这些数字正在加速下降。',
    insight=False, note='',
    bold=['accelerating', 'falling'],
    chunks=[
        dict(role='状语', text='Worse',
             note='评注性状语：更糟的是'),
        dict(role='主语', text='the numbers',
             note='指上文的参与人数'),
        dict(role='谓语', text='are now falling',
             note='时间状语 now 插在助动词与实义动词之间，整体作为一个谓语块'),
        dict(role='状语', text='at an accelerating rate',
             note='介词短语作方式状语'),
    ])

A['P2S8'] = dict(
    zh='反对派声称每周至少参加两小时体育运动的小学生几乎减半。',
    insight=False, note='',
    bold=['opposition', 'at least', 'halved'],
    chunks=[
        dict(role='主语', text='The opposition',
             note=''),
        dict(role='谓语', text='claims',
             note='引述动词，后接省略 that 的宾语从句'),
        dict(role='宾语从句', text='primary school pupils doing at least two hours of sport a week have nearly halved',
             note='省略了 that 的宾语从句；从句主语 pupils 带动名词短语 doing at least two hours of sport a week 作后置定语；have nearly halved 为从句谓语，nearly 为程度状语'),
    ])

A['P2S9'] = dict(
    zh='成人和儿童的肥胖率都上升了。',
    insight=False, note='',
    bold=['obesity', 'risen'],
    chunks=[
        dict(role='主语', text='Obesity',
             note=''),
        dict(role='谓语', text='has risen',
             note='现在完成时，表已经发生的变化'),
        dict(role='状语', text='among adults and children',
             note='among... 表范围'),
    ])

A['P2S10'] = dict(
    zh='关于伦敦2012年为何未能「激励一代人」的官方反思仍在继续。',
    insight=False, note='',
    bold=['retrospections', 'failed to'],
    chunks=[
        dict(role='主语', text='Official retrospections',
             note='官方的反思'),
        dict(role='谓语', text='continue',
             note=''),
        dict(role='状语', text='as to',
             note='固定搭配 as to 引出说明的内容'),
        dict(role='宾语从句', text='why London 2012 failed to "inspire a generation."',
             note='why 引导的从句作 as to 的宾语；fail to do 意为「未能做某事」'),
    ])

A['P2S11'] = dict(
    zh='Parkrun 的成功提供了答案。',
    insight=False, note='',
    bold=['success', 'offers'],
    chunks=[
        dict(role='主语', text='The success of Parkrun',
             note='of Parkrun 为介词短语作后置定语'),
        dict(role='谓语', text='offers',
             note=''),
        dict(role='宾语', text='answers',
             note=''),
    ])

A['P3S1'] = dict(
    zh='Parkrun 不是一场比赛而是计时赛：你唯一的竞争对手是时钟。',
    insight=True, note='主系表结构和并列主句都是考试常见句式,not...but结构也是高频考点,但本句整体过于简单,缺少真题中常见的从句嵌套或复杂修饰,作为代表性句式的迁移价值中等偏下',
    bold=['time trial', 'competitor'],
    chunks=[
        dict(role='主语', text='Parkun',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='not a race but a time trial',
             note='not...but... 并列两个表语；time trial 意为「计时赛」'),
        dict(role='主语', text='Your only competitor',
             note='冒号后第二个并列分句的主语'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='the clock',
             note=''),
    ])

A['P3S2'] = dict(
    zh='其理念欢迎任何人。',
    insight=False, note='',
    bold=['ethos', 'welcomes'],
    chunks=[
        dict(role='主语', text='The ethos',
             note='理念、精神气质'),
        dict(role='谓语', text='welcomes',
             note=''),
        dict(role='宾语', text='anybody',
             note=''),
    ])

A['P3S3'] = dict(
    zh='当气喘吁吁的初次参加者在掌声中冲过终点线时的欢乐，与顶尖人才闪耀时的欢乐一样多。',
    insight=True, note='本句涵盖了There be句型中主语后置、as...as比较结构、分词短语作后置定语、介词短语作定语等多种成分类型，且主语结构较长容易误判，适合训练学生识别存在句主语、区分谓语与非谓语、划分修饰成分归属等易错点。',
    bold=['puffed-out', 'top talent'],
    chunks=[
        dict(role='谓语', text='There is',
             note='存在句：there 为引导词，is 为谓语'),
        dict(role='主语', text='as much joy over a puffed-out first-timer being clapped over the line',
             note='存在句的真正主语；over... 为介词短语作定语修饰 joy；being clapped over the line 为动名词的被动式，修饰 first-timer'),
        dict(role='状语从句', text='as there is about top talent shining',
             note='as...as 比较结构中的比较状语从句，第二个 as 引导从句，从句里同样存在主语后置与 about... 作定语'),
    ])

A['P3S4'] = dict(
    zh='相比之下，奥运申办者想让更多人参加体育运动并培养更多精英运动员。',
    insight=True, note='简单句中使用并列不定式作宾语以及插入状语的结构在四六级和考研阅读中较为常见，具有一定代表性。这类句式在实际考试中频繁出现，掌握后可迁移到类似结构的句子理解中。',
    bold=['bidders', 'by contrast', 'elite athletes'],
    chunks=[
        dict(role='主语', text='The Olympic bidders',
             note=''),
        dict(role='插入语', text='by contrast',
             note='插入语，表对比'),
        dict(role='谓语', text='wanted',
             note=''),
        dict(role='宾语', text='to get more people doing sport',
             note='不定式作宾语；doing sport 为现在分词作宾语补足语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='宾语', text='to produce more elite athletes',
             note='与上一个不定式并列，共同作 wanted 的宾语'),
    ])

A['P3S5'] = dict(
    zh='这一双重目标混淆了：强调成功而非参与对新人来说令人生畏。',
    insight=False, note='',
    bold=['dual', 'mixed up', 'intimidating'],
    chunks=[
        dict(role='主语', text='The dual aim',
             note=''),
        dict(role='谓语', text='was mixed up',
             note='被动语态；mix up 意为「混淆」'),
        dict(role='主语', text='The stress on success over taking part',
             note='冒号后第二个分句的主语；on success over taking part 为介词短语作后置定语'),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='intimidating',
             note=''),
        dict(role='状语', text='for newcomers',
             note=''),
    ])
