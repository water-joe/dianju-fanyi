# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P5S2'] = dict(
    zh='小费蔓延和小费通胀现在进一步补充了许多低薪服务业员工的收入。',
    insight=False, note='',
    bold=['supplementing', 'low-wage service workers'],
    chunks=[
        dict(role='主语', text='Tip creep and tipflation',
             note=''),
        dict(role='谓语', text='are now further supplementing the income of many low-wage service workers.',
             note='now 插在助动词后；现在进行时；supplement 补充'),
    ])

A['P6S1'] = dict(
    zh='值得注意的是，小费主要惠及其中一些员工，如服务员，但不惠及其他员工，如厨师和洗碗工。',
    insight=True, note='本句展示了"主语+谓语+并列宾语"的基本句型,以及"some...butnotothers"的对比并列结构和"suchas"的举例用法,这些都是四六级和考研阅读中高频出现的典型结构;掌握后可迁移到大量同类句式,具有较高代表性。',
    bold=['Notably', 'primarily benefits', 'waiters'],
    chunks=[
        dict(role='状语', text='Notably,',
             note='评注性状语'),
        dict(role='主语', text='tipping',
             note=''),
        dict(role='状语', text='primarily',
             note=''),
        dict(role='谓语', text='benefits',
             note=''),
        dict(role='宾语', text='some of these workers, such as waiters, but not others, such as cooks and dishwashers.',
             note='some... but not others 对比并列；两个 such as 举例'),
    ])

A['P6S2'] = dict(
    zh='为确保所有员工获得公平工资，一些餐厅禁止收小费并提高了价格，但这种取消小费服务的运动基本上已经失败。',
    insight=False, note='',
    bold=['banned tipping', 'fizzled out'],
    chunks=[
        dict(role='状语', text='To ensure that all employees were paid fair wages,',
             note='不定式作目的状语；ensure 后接宾语从句（被动）'),
        dict(role='主语', text='some restaurants',
             note=''),
        dict(role='谓语', text='banned tipping and increased prices,',
             note='并列谓语'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='this movement toward no-tipping services',
             note=''),
        dict(role='谓语', text='has largely fizzled out.',
             note='largely 插在助动词后；fizzle out （运动等）不了了之'),
    ])

A['P7S1'] = dict(
    zh='因此，为了在不提高价格的情况下增加员工工资，越来越多的雇主屈服于小费蔓延和小费通胀的诱惑。',
    insight=True, note='本句涉及主语、谓语、宾语、目的状语四种核心成分，且目的状语前置容易与主语混淆，宾语中包含后置定语修饰，对初学者有一定辨识训练价值。但成分种类不算丰富（无表语、补语、同位语等），坑点密集度中等。',
    bold=['succumbing to', 'temptations'],
    chunks=[
        dict(role='状语', text='So, to increase employee wages without raising prices,',
             note='不定式作目的状语（前置）；without raising 动名词作介词宾语'),
        dict(role='主语', text='more employers',
             note=''),
        dict(role='谓语', text='are succumbing to the temptations of tip creep and tipflation.',
             note='succumb to 屈服于；现在进行时'),
    ])

A['P7S2'] = dict(
    zh='然而，许多顾客感到沮丧，因为他们觉得自己被要求支付过高的小费，而且频率过高。',
    insight=True, note='主句加because原因状语从句是四六级和考研阅读中的高频结构。宾语从句省略that引导词，也是常见现象。现在进行时被动语态arebeingasked是考试中常考的时态语态组合。整体句式具有很强的代表性和可迁移性。',
    bold=['frustrated', 'too high of a tip, too often'],
    chunks=[
        dict(role='状语', text='However,',
             note='转折'),
        dict(role='主语', text='many customers',
             note=''),
        dict(role='谓语', text='are frustrated',
             note=''),
        dict(role='状语从句', text='because they feel they are being asked for too high of a tip, too often.',
             note='because 引导原因状语从句；feel 后省略 that 的宾语从句；are being asked 现在进行时被动'),
    ])

A['P7S3'] = dict(
    zh='而且，正如我们的研究所强调的，小费现在似乎更具强制性、更缺乏慷慨性，并且往往与服务质量完全脱节。',
    insight=True, note='状语从句插入主句是四六级和考研阅读中的高频句式,系表结构加不定式表语也很常见。掌握这种插入结构的识别方法可以迁移到大量类似句子,具有较好的典型性。',
    bold=['coercive', 'dissociated from'],
    chunks=[
        dict(role='连接词', text='And,',
             note='并列'),
        dict(role='插入语', text='as our research emphasizes,',
             note='as 引导的非限制性定语从句作插入语'),
        dict(role='主语', text='tipping',
             note=''),
        dict(role='状语', text='now',
             note=''),
        dict(role='谓语', text='seems to be more coercive, less generous and often completely dissociated from service quality.',
             note='seem + adj.；三个并列表语'),
    ])
