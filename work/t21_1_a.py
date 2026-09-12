# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 1 —— P1 至 P2 的逐句成分划分与重点词释义。
口径：嵌套成分合并为一块（子结构写进 note）；引述分句各标各的主谓语。"""

A = {}

A['P1S1'] = dict(
    zh='"再培训"听起来像是一个流行词，但如果我们计划拥有一个不让大量潜在劳动者掉队的未来，它实际上是一项必需。',
    insight=False, note='',
    bold=['Reskilling', 'buzzword', 'requirement', 'would-be', 'left behind'],
    chunks=[
        dict(role='主语', text='"Reskilling"'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='something that sounds like a buzzword but is actually a requirement if we plan to have a future where a lot of would-be workers do not get left behind',
             note='that 引导定语从句修饰 something；其中 but 连接并列谓语 sounds / is，if 引导条件状语从句内含 where 定语从句'),
    ])

A['P1S2'] = dict(
    zh='我们知道，我们正在进入一个需求岗位将快速变化的时期，而留存的岗位其要求也会随之变化。',
    insight=True,
    note='全句覆盖主语、谓语、宾语、状语、定语等多种成分，且包含宾语从句充当宾语、定语从句修饰名词、状语从句修饰动作、介词短语作后置定语等多种典型结构。特别是状语从句中的倒装和承前省略、宾语从句省略引导词 that、关系代词 that 在从句中充当主语等，都是常见易错点，训练价值较高。',
    bold=['moving into', 'in demand', 'rapidly', 'as will'],
    chunks=[
        dict(role='主语', text='We'),
        dict(role='谓语', text='know', note='引述动词'),
        dict(role='宾语', text='we are moving into a period where the jobs in demand will change rapidly, as will the requirements of the jobs that remain',
             note='省略 that 的宾语从句；where 定语从句修饰 period；as will... 为倒装省略结构，that remain 定语从句修饰 jobs'),
    ])

A['P1S3'] = dict(
    zh='世界经济论坛的研究发现，到 2022 年，岗位角色中平均 42% 的"核心技能"将发生变化。',
    insight=False, note='',
    bold=['Research by the World Economic Forum', 'finds', 'on average', 'core skills'],
    chunks=[
        dict(role='主语', text='Research by the World Economic Forum'),
        dict(role='谓语', text='finds'),
        dict(role='宾语', text='that on average 42 per cent of the "core skills" within job roles will change by 2022',
             note='that 引导宾语从句；within job roles 介词短语作后置定语'),
    ])

A['P1S4'] = dict(
    zh='那是一条非常短的时间线。',
    insight=False, note='',
    bold=['timeline'],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='a very short timeline'),
    ])

A['P2S1'] = dict(
    zh='谁应该为再培训买单是一个棘手的问题。',
    insight=False, note='',
    bold=['thorny'],
    chunks=[
        dict(role='主语', text='The question of who should pay for reskilling'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='a thorny one', note='one 指代 question'),
    ])

A['P2S2'] = dict(
    zh='对单个公司而言，诱惑总是解雇技能不再被需要的员工，并用那些具备所需技能的人取而代之。',
    insight=True,
    note='主系表结构加并列不定式作表语，搭配两个限制性定语从句形成对比，是四六级和考研阅读中常见的句式，对比结构和定语从句的嵌套使用具有很强的代表性和迁移性。',
    bold=['For individual companies', 'temptation', 'let go of', 'no longer in demand', 'replace'],
    chunks=[
        dict(role='状语', text='For individual companies'),
        dict(role='主语', text='the temptation'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='always to let go of workers whose skills are no longer in demand and replace them with those whose skills are',
             note='并列不定式 to let go of... and replace... 作表语；whose 引导两个对比定语从句'),
    ])

A['P2S3'] = dict(
    zh='但情况并非总是如此。',
    insight=False, note='',
    bold=['That does not always happen'],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text="does not always happen"),
    ])

A['P2S4'] = dict(
    zh='AT&T 常被视为决定实施大规模再培训计划、而非采取"解雇再招聘"策略的公司的黄金标准。',
    insight=True,
    note='"主句+限制性定语从句修饰宾语"是四六级和考研阅读中的高频句式，被动语态搭配"be given as"以及定语从句中的不定式宾语也是常见考点。本句结构具有较强的代表性和迁移价值。',
    bold=['gold standard', 'massive', 'rather than', 'fire-and-hire'],
    chunks=[
        dict(role='主语', text='AT&T'),
        dict(role='谓语', text='is often given', note='被动语态'),
        dict(role='主语补足语', text='as the gold standard of a company who decided to do a massive reskilling program rather than go with a fire-and-hire strategy',
             note='as 短语作主语补足语；who 引导定语从句修饰 company，内含 rather than 对比的不定式'),
    ])

A['P2S5'] = dict(
    zh='包括亚马逊和迪士尼在内的其他公司也承诺制定自己的计划。',
    insight=True,
    note='主谓宾结构是英语最常见的基本句型，过去完成时在真题叙述中也常出现。主语带后置定语、不定式作宾语都是典型用法，学习后可迁移到同类句子。但因过于基础，代表性中等。',
    bold=['Other companies including', 'pledged', 'create their own plans'],
    chunks=[
        dict(role='主语', text='Other companies including Amazon and Disney'),
        dict(role='谓语', text='had also pledged', note='过去完成时'),
        dict(role='宾语', text='to create their own plans', note='不定式作宾语'),
    ])

A['P2S6'] = dict(
    zh='然而，当技能错配出现在更广泛的经济中时，焦点通常转向政府来处理。',
    insight=False, note='',
    bold=['skills mismatch', 'broader economy', 'turns to'],
    chunks=[
        dict(role='状语从句', text='When the skills mismatch is in the broader economy though',
             note='when 引导时间状语从句，though 为插入的转折副词'),
        dict(role='主语', text='the focus'),
        dict(role='谓语', text='usually turns'),
        dict(role='状语', text='to government to handle', note='to government 状语；to handle 不定式作目的/修饰'),
    ])

A['P2S7'] = dict(
    zh='加拿大和其他地方的努力可以说充其量迟缓，并给我们带来这样一种局面：我们经常听到雇主恳求招工，即便是在失业率很高的时期和地区。',
    insight=True,
    note='主句包含并列谓语、系表结构、双宾语结构，第一个定语从句包含频率状语、介词宾语及宾语补足语，第二个定语从句包含系表结构，成分种类丰富。关系副词 where 在两个从句中既作连接词又作地点状语，易与关系代词混淆。并列谓语和双宾语结构都是学生容易混淆的点，练习价值较高。',
    bold=['Efforts', 'arguably', 'languid', 'begging for', 'unemployment'],
    chunks=[
        dict(role='主语', text='Efforts in Canada and elsewhere'),
        dict(role='谓语', text='have been arguably languid at best'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='have given'),
        dict(role='间接宾语', text='us'),
        dict(role='直接宾语', text='a situation where we frequently hear of employers begging for workers, even at times and in regions where unemployment is high',
             note='双宾语 us / a situation；where 定语从句修饰 situation，内含 even at... where... 嵌套地点从句'),
    ])
