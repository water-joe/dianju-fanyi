# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='互联网也许只是改变了我们记忆的内容，而非我们的记忆能力，Columbia University心理学教授Betsy Sparrow如此认为。',
    insight=False, note='',
    bold=['capacity to do so'],
    chunks=[
        dict(role='主语', text='The Internet',
             note=''),
        dict(role='谓语', text='may be changing',
             note=''),
        dict(role='宾语', text='merely what we remember, not our capacity to do so,',
             note='what 引导宾语从句；not... but 否定对照'),
        dict(role='谓语', text='suggests',
             note='引述动词'),
        dict(role='主语', text='Columbia University psychology professor Betsy Sparrow.',
             note='引述分句主语（suggests 前置倒装）'),
    ])

A['P1S2'] = dict(
    zh='2011年，Sparrow主持了一项研究，参与者被要求在计算机中记录40条小知识(例如"鸵鸟的眼睛比它的大脑还大")。',
    insight=False, note='',
    bold=['led a study', 'factoids'],
    chunks=[
        dict(role='状语', text='In 2011,',
             note=''),
        dict(role='主语', text='Sparrow',
             note=''),
        dict(role='谓语', text='led',
             note=''),
        dict(role='宾语', text='a study in which participants were asked to record 40 factoids in a computer',
             note='in which 引导定语从句修饰 study；be asked to do 被动'),
        dict(role='同位语', text='("an ostrich\'s eye is bigger than its brain," for example).',
             note='括号内举例'),
    ])

A['P1S3'] = dict(
    zh='一半参与者被告知这些信息将被删除，而另一半被告知信息会被保存。',
    insight=True, note='并列主句+宾语从句的组合在四六级和考研阅读中非常常见，尤其是描述对比实验或调查结果的学术文本中。while连接对比并列句也是高频句式。掌握这种结构后，可以迁移到大量类似句子的分析中，典型性较高。',
    bold=['erased'],
    chunks=[
        dict(role='主语', text='Half of the participants',
             note=''),
        dict(role='谓语', text='were told',
             note=''),
        dict(role='宾语从句', text='the information would be erased,',
             note='省略 that 的宾语从句'),
        dict(role='状语从句', text='while the other half were told it would be saved.',
             note='while 引导对比状语从句；be told (that)... 省略 that'),
    ])

A['P1S4'] = dict(
    zh='结果如何？',
    insight=False, note='',
    bold=['Guess what'],
    chunks=[
        dict(role='谓语', text='Guess',
             note=''),
        dict(role='宾语', text='what?',
             note='设问句，引出下文'),
    ])

A['P1S5'] = dict(
    zh='后一组在随后被测试时完全没有努力回忆这些信息，因为他们知道可以在电脑上找到它们。',
    insight=False, note='',
    bold=['made no effort to recall'],
    chunks=[
        dict(role='主语', text='The latter group',
             note=''),
        dict(role='谓语', text='made no effort to recall the information',
             note='make no effort to do 没有费力做'),
        dict(role='状语从句', text='when quizzed on it later,',
             note='when (they were) quizzed 省略主谓'),
        dict(role='状语从句', text='because they knew they could find it on their computers.',
             note='because 原因状语从句；knew 后省略 that 的宾语从句'),
    ])

A['P1S6'] = dict(
    zh='在同一研究中，另一组被要求同时记住信息和存储信息的文件夹。',
    insight=True, note='被动语态加不定式宾补的结构（"beaskedtodo"）以及省略关系代词的定语从句（"thefoldersitwasstoredin"），都是四六级和考研阅读中的高频句式，具有较强的代表性和迁移价值。',
    bold=['folders'],
    chunks=[
        dict(role='状语', text='In the same study,',
             note=''),
        dict(role='主语', text='a group',
             note=''),
        dict(role='谓语', text='was asked to remember both the information and the folders it was stored in.',
             note='be asked to do 被动；both... and... 并列；(that) it was stored in 省略关系词的定语从句'),
    ])

A['P1S7'] = dict(
    zh='他们没有记住信息，但记住了如何找到文件夹。',
    insight=False, note='',
    bold=['how to find'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text="didn't remember",
             note=''),
        dict(role='宾语', text='the information,',
             note=''),
        dict(role='连接词', text='but',
             note=''),
        dict(role='谓语', text='they remembered how to find the folders.',
             note='疑问词+不定式作宾语'),
    ])

A['P1S8'] = dict(
    zh='换句话说，Sparrow表示，人类记忆并非在退化，而是"在适应新的通信技术"。',
    insight=True, note='引述动词加宾语从句是四六级和考研阅读中的高频句式,且not...but并列否定转折结构也常出现,句式典型且实用性强,掌握后可迁移至大量类似表达。',
    bold=['deteriorating', 'adapting to'],
    chunks=[
        dict(role='状语', text='In other words,',
             note=''),
        dict(role='主语', text='human memory',
             note=''),
        dict(role='谓语', text='is not deteriorating but "adapting to new communications technology,"',
             note='not... but... 否定转折并列'),
        dict(role='主语', text='Sparrow',
             note=''),
        dict(role='谓语', text='says.',
             note=''),
    ])

A['P2S1'] = dict(
    zh='从非常实际的角度来说，互联网正在成为我们记忆的外部硬盘，这一过程被称为"认知卸载"。',
    insight=False, note='',
    bold=['external hard drive', 'cognitive offloading'],
    chunks=[
        dict(role='状语', text='In a very practical way,',
             note=''),
        dict(role='主语', text='the Internet',
             note=''),
        dict(role='谓语', text='is becoming',
             note=''),
        dict(role='表语', text='an external hard drive for our memories,',
             note=''),
        dict(role='同位语', text='a process known as "cognitive offloading."',
             note='a process 为同位语；known as... 过去分词作后置定语'),
    ])

A['P2S2'] = dict(
    zh='传统上，这一角色由数据库、图书馆和其他人来承担。',
    insight=False, note='',
    bold=['fulfilled by'],
    chunks=[
        dict(role='状语', text='Traditionally,',
             note=''),
        dict(role='主语', text='this role',
             note=''),
        dict(role='谓语', text='was fulfilled by data banks, libraries, and other humans.',
             note='被动语态 + by 施动者'),
    ])

A['P2S3'] = dict(
    zh='例如，你的父亲可能永远记不住生日，因为你的母亲会记得。',
    insight=True, note='这是一个典型的主从复合句：主句+原因状语从句，符合四六级和考研中常见的句式。情态动词加否定副词的谓语结构以及从句中的承前省略也是考试中经常出现的考点。虽然句子整体不算复杂，但结构具有较高的代表性，掌握后可以迁移到类似的因果复合句中。',
    bold=['may never', 'does'],
    chunks=[
        dict(role='主语', text='Your father',
             note=''),
        dict(role='谓语', text='may never remember',
             note=''),
        dict(role='宾语', text='birthdays',
             note=''),
        dict(role='状语从句', text='because your mother does,',
             note='because 原因状语从句；does 承前省略 remember'),
        dict(role='状语', text='for instance.',
             note=''),
    ])

A['P2S4'] = dict(
    zh='一些人担心这对社会产生破坏性影响，但Sparrow看到了积极的一面。',
    insight=True, note='句子结构是典型的"主句+宾语从句+转折并列主句"模式,这种"观点陈述+转折对比"的句式在四六级和考研阅读中频繁出现,学习迁移价值高',
    bold=['destructive effect', 'upside'],
    chunks=[
        dict(role='主语', text='Some',
             note=''),
        dict(role='谓语', text='worry',
             note=''),
        dict(role='宾语从句', text='that this is having a destructive effect on society,',
             note='that 引导宾语从句；现在进行时'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='Sparrow',
             note=''),
        dict(role='谓语', text='sees',
             note=''),
        dict(role='宾语', text='an upside.',
             note='upside 积极的一面'),
    ])

A['P2S5'] = dict(
    zh='她认为，这一趋势也许会改变我们的学习方式，从关注个别事实和记忆转向强调更具概念性的思维——这是互联网上无法获得的东西。',
    insight=False, note='',
    bold=['approach to learning', 'conceptual thinking'],
    chunks=[
        dict(role='状语', text='Perhaps,',
             note=''),
        dict(role='插入语', text='she suggests,',
             note=''),
        dict(role='主语', text='the trend',
             note=''),
        dict(role='谓语', text='will change',
             note=''),
        dict(role='宾语', text='our approach to learning from a focus on individual facts and memorization to an emphasis on more conceptual thinking—something that is not available on the Internet.',
             note='from... to... 对比；破折号后 something 为同位语；that... 定语从句修饰 something'),
    ])
