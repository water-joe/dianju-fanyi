# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S5'] = dict(
    zh='它还将监测进展的工作交给西部鱼类和野生动物机构协会(WAFWA)，这是一个州级机构联盟。',
    insight=False, note='',
    bold=['coalition', 'monitoring progress'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='gives',
             note=''),
        dict(role='间接宾语', text='the Western Association of Fish and Wildlife Agencies (WAFWA), a coalition of state agencies,',
             note='a coalition... 为同位语；give sb. sth. 双宾语'),
        dict(role='直接宾语', text='the job of monitoring progress.',
             note='of monitoring... 动名词作后置定语'),
    ])

A['P3S6'] = dict(
    zh='总体而言，其理念是让"各州在管理该物种方面保持主导地位"，Ashe说。',
    insight=True, note='引述结构（某人said+引号内容）和不定式作表语说明抽象名词的内容，都是四六级和考研阅读中的高频句式，典型性较强，掌握后可广泛迁移。',
    bold=["remain in the driver's seat"],
    chunks=[
        dict(role='状语', text='Overall,',
             note=''),
        dict(role='主语', text='the idea',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='to let "states remain in the driver\'s seat for managing the species,"',
             note="不定式作表语；let sb. do 宾补；in the driver's seat 处于主导地位"),
        dict(role='谓语', text='Ashe',
             note=''),
        dict(role='主语', text='said.',
             note='引述分句（Ashe said）'),
    ])

A['P4S1'] = dict(
    zh='并非所有人都认同这种双赢的说辞。',
    insight=True, note='简单句的主谓宾结构是最基础句型，但否定主语"Noteveryone"的表达在考试阅读中较为常见，适合作为否定范围理解的入门例句；整体句式虽简单但具有一定实用性。',
    bold=['buys the win-win rhetoric'],
    chunks=[
        dict(role='主语', text='Not everyone',
             note=''),
        dict(role='谓语', text='buys',
             note=''),
        dict(role='宾语', text='the win-win rhetoric.',
             note='buy 此处意为「相信、接受」；rhetoric 说辞'),
    ])

A['P4S2'] = dict(
    zh='一些国会议员正试图阻止该计划，至少有十几个行业团体、四个州和三个环保组织正在联邦法院对其提出质疑。',
    insight=False, note='',
    bold=['block the plan', 'challenging'],
    chunks=[
        dict(role='主语', text='Some Congress members',
             note=''),
        dict(role='谓语', text='are trying to block the plan,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='at least a dozen industry groups, four states, and three environmental groups',
             note=''),
        dict(role='谓语', text='are challenging',
             note=''),
        dict(role='宾语', text='it in federal court.',
             note='现在进行时；challenge 质疑'),
    ])

A['P4S3'] = dict(
    zh='不出所料，行业团体和各州普遍认为该计划走得太远；环保人士则说它做得还不够。',
    insight=False, note='',
    bold=['goes too far', "doesn't go far enough"],
    chunks=[
        dict(role='状语', text='Not surprisingly,',
             note=''),
        dict(role='主语', text='industry groups and states',
             note=''),
        dict(role='状语', text='generally',
             note=''),
        dict(role='谓语', text='argue',
             note=''),
        dict(role='宾语从句', text='it goes too far;',
             note='省略 that 的宾语从句'),
        dict(role='主语', text='environmentalists',
             note=''),
        dict(role='谓语', text='say',
             note=''),
        dict(role='宾语从句', text="it doesn't go far enough.",
             note='省略 that 的宾语从句'),
    ])

A['P4S4'] = dict(
    zh='生物学家Jay Lininger说:"联邦政府正将管理这种鸟的责任交给那些正在将它推向灭绝的行业。"',
    insight=False, note='',
    bold=['giving responsibility for', 'extinction'],
    chunks=[
        dict(role='宾语', text='"The federal government is giving responsibility for managing the bird to the same industries that are pushing it to extinction,"',
             note='直接引语作 says 的宾语；give sth. to sb.；that... 定语从句修饰 industries；push... to extinction 推向灭绝'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='biologist Jay Lininger.',
             note=''),
    ])
