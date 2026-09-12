# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 1 —— 逐句成分划分与重点词释义。

口径（与用户确认过，见 CLAUDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
  3. 状语插在谓词中间时整体作一个谓语块（如 are now falling）
"""

A = {}

A['P4S1'] = dict(
    zh='事实上，政府参与规划社区体育协会这样一个根本上属于「草根」的概念，确实有些荒谬。',
    insight=True, note='本句的结构在四六级和考研阅读中非常典型。therebe句型+复杂主语（带多层后置定语）是学术类和议论文中的高频句式，用于引出一个抽象概念或现象并展开描述。掌握这种句式后，学习者可以迁移到大量类似的长难句分析中，实用性很强。',
    bold=['absurd', 'getting involved in', 'grassroots'],
    chunks=[
        dict(role='状语', text='Indeed',
             note='评注性状语：的确、事实上'),
        dict(role='谓语', text='there is',
             note='存在句：there 为引导词，is 为谓语'),
        dict(role='主语', text='something a little absurd in the state getting involved in the planning of such a fundamentally "grassroots" concept as community sports associations',
             note='存在句的真正主语；a little absurd 为后置修饰语；in the state getting involved... 为介词短语说明「荒谬」体现在何处，getting involved 为动名词；such...as... 引出同位说明'),
    ])

A['P4S2'] = dict(
    zh='如果政府有作用，它真正应该做的是参与提供公共产品——确保有运动场地的空间和铺设网球场和无挡板篮球场的资金，并鼓励学校提供所有这些活动。',
    insight=False, note='',
    bold=['common goods', 'pave', 'provision'],
    chunks=[
        dict(role='状语从句', text='If there is a role for government',
             note='if 引导条件状语从句，从句内部同样是 there be 结构'),
        dict(role='主语', text='it',
             note='指代 government'),
        dict(role='谓语', text='should really be getting involved',
             note='really 为插入状语；be getting involved 为进行时的系表结构'),
        dict(role='状语', text='in providing common goods',
             note='in doing 表示「在……方面」；common goods 意为公共产品'),
        dict(role='定语', text='making sure there is space for playing fields and the money to pave tennis and netball courts',
             note='现在分词短语，对「提供公共产品」作补充说明；making sure 后接省略 that 的宾语从句，其中 space 与 the money 并列'),
        dict(role='定语', text='and encouraging the provision of all these activities in schools',
             note='与上一个分词短语并列，and 连接两个现在分词'),
    ])

A['P4S3'] = dict(
    zh='但历届政府却主持出售绿地，挤压地方当局的资金，减少对教育中体育的关注。',
    insight=False, note='',
    bold=['successive', 'presided over', 'squeezing'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='successive governments',
             note='历届政府'),
        dict(role='谓语', text='have presided over',
             note='preside over 意为「主持、掌管」，此处含失职的意味'),
        dict(role='宾语', text='selling green spaces, squeezing money from local authorities and declining attention on sport in education',
             note='三个并列的动名词短语作介词 over 的宾语，是本句的难点：名词化结构被用来罗列政府的作为'),
    ])

A['P4S4'] = dict(
    zh='未来的政府需要做更多工作来提供体育繁荣的条件，而不是空洞的、冠冕堂皇的战略。',
    insight=True, note='本句使用「InsteadofA,BneedtodoCtoachieveD」的对比建议结构，这种「对比+行动呼吁」的句式在四六级和考研阅读中较为常见，尤其在议论文和评论类文章中频繁出现，具有较强的代表性。',
    bold=['Instead of', 'worthy', 'thrive'],
    chunks=[
        dict(role='状语', text='Instead of wordy, worthy strategies',
             note='介词短语作状语，表对比/否定；wordy 与 worthy 为并列定语'),
        dict(role='主语', text='future governments',
             note=''),
        dict(role='谓语', text='need',
             note=''),
        dict(role='宾语', text='to do more',
             note='不定式作宾语'),
        dict(role='状语', text='to provide the conditions for sport to thrive',
             note='不定式作目的状语；for sport to thrive 为不定式的复合结构'),
    ])

A['P4S5'] = dict(
    zh='或者至少不要让情况变得更糟。',
    insight=False, note='',
    bold=['at least', 'worse'],
    chunks=[
        dict(role='连接词', text='Or',
             note='承上文的另一种（更低的）要求'),
        dict(role='状语', text='at least',
             note='固定短语：至少'),
        dict(role='状语', text='not',
             note='否定状语，与后面的动词构成否定祈使'),
        dict(role='谓语', text='make',
             note=''),
        dict(role='宾语', text='them',
             note='指代上文提到的各种条件'),
        dict(role='宾语补足语', text='worse',
             note='形容词作宾语补足语'),
    ])
