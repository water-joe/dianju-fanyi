# -*- coding: utf-8 -*-
"""2020 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='CEO薪酬确实上涨了——顶级CEO的薪酬平均可能是普通员工的300倍，而且自20世纪70年代中期以来，根据不同的估算，美国大型上市公司CEO的薪酬已经上涨了约500%。',
    insight=True, note='形式主语+主语从句结构（Itistruethat...）和现在完成时搭配since时间状语是四六级和考研常考句式；并列主句结构也频繁出现在真题中；句式具有较强的代表性和可迁移性，掌握后可应用于大量类似句子。',
    bold=['It is true that', 'publicly traded', 'by varying estimates'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text='is true',
             note=''),
        dict(role='主语从句', text='that CEO pay has gone up—',
             note='that 引导主语从句；现在完成时'),
        dict(role='主语', text='top ones',
             note=''),
        dict(role='谓语', text='may make 300 times the pay of typical workers on average,',
             note='倍数表达：300 times the pay'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='状语', text='since the mid-1970s,',
             note=''),
        dict(role='主语', text='CEO pay for large publicly traded American corporations',
             note=''),
        dict(role='状语', text='has, by varying estimates, gone up by about 500%.',
             note='by varying estimates 插入性状语；by about 500% 幅度状语'),
    ])

A['P1S2'] = dict(
    zh='如今美国顶级公司的典型CEO年薪约为1890万美元。',
    insight=False, note='',
    bold=['typical CEO'],
    chunks=[
        dict(role='主语', text='The typical CEO of a top American corporation',
             note=''),
        dict(role='状语', text='now',
             note=''),
        dict(role='谓语', text='makes',
             note=''),
        dict(role='宾语', text='about $18.9 million a year.',
             note=''),
    ])

A['P2S1'] = dict(
    zh='理解CEO薪酬增长的最佳模型是，在顶级公司的商业机会快速增长的世界中，CEO人才是有限的。',
    insight=True, note='主系表结构配合限制性定语从句是四六级和考研真题中的高频句式。表语中使用that指代、介词短语层层修饰以及定语从句限定先行词的手法，都是学术文章和说明文的典型特征。掌握此类句式可迁移至大量同类真题句子。',
    bold=['The best model for understanding', 'that of limited CEO talent'],
    chunks=[
        dict(role='主语', text='The best model for understanding the growth of CEO pay',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='that of limited CEO talent in a world',
             note='that 指代 model'),
        dict(role='定语从句', text='where business opportunities for the top firms are growing rapidly.',
             note='where 引导定语从句修饰 world'),
    ])

A['P2S2'] = dict(
    zh='美国收入最高的1%群体的努力一直是全球经济中更具活力的要素之一。',
    insight=False, note='',
    bold=['highest-earning', 'dynamic elements'],
    chunks=[
        dict(role='主语', text="The efforts of America's highest-earning 1%",
             note=''),
        dict(role='谓语', text='have been',
             note=''),
        dict(role='表语', text='one of the more dynamic elements of the global economy.',
             note='one of the + 最高级 结构'),
    ])

A['P2S3'] = dict(
    zh='尽管这样说不受欢迎，但他们薪酬大幅上涨的一个原因是，相对于美国经济中的许多其他劳动者，CEO确实提升了他们的能力。',
    insight=True, note='转折并列句+定语从句（省略关系词）+表语从句的组合是四六级和考研阅读中的高频句式。主系表结构配合that引导的表语从句（reasonisthat）尤其常见。本句结构具有很强的代表性，掌握后可迁移到大量类似长难句。',
    bold=['upped their game', 'relative to'],
    chunks=[
        dict(role='主语', text="It's not popular to say,",
             note=''),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='one reason their pay has gone up so much',
             note='(why) their pay has gone up 省略关系副词的定语从句'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语从句', text='that CEOs really have upped their game relative to many other workers in the U.S. economy.',
             note="that 引导表语从句；up one's game 提升水平；relative to 相对于"),
    ])

A['P3S1'] = dict(
    zh='如今的CEO，至少对于美国大公司而言，必须具备比单纯"经营公司"多得多的技能。',
    insight=False, note='',
    bold=['at least for', 'simply being able to'],
    chunks=[
        dict(role='主语', text="Today's CEO, at least for major American firms,",
             note=''),
        dict(role='谓语', text='must have many more skills',
             note=''),
        dict(role='状语', text='than simply being able to "run the company."',
             note='than 比较状语；being able to... 动名词短语'),
    ])
