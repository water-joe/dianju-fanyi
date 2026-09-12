# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P2S6'] = dict(
    zh='但Ashe和其他人辩称，"受威胁"标签赋予联邦政府灵活性，可以尝试新的、潜在冲突较少的保护方法。',
    insight=True, note='主句+并列修饰对象+嵌入定语从句的组合是四六级和考研阅读中的高频句式。"callfor+动名词"、非限定与限定定语从句的对比使用、百分比表达等均为真题常见结构,学习后可大量迁移',
    bold=['flexibility', 'confrontational'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='Ashe and others',
             note=''),
        dict(role='谓语', text='argued',
             note=''),
        dict(role='宾语从句', text='that the "threatened" tag gave the federal government flexibility to try out new, potentially less confrontational conservation approaches.',
             note='that 引导宾语从句；give sb. sth. 双宾语；to try out... 不定式作后置定语'),
    ])

A['P2S7'] = dict(
    zh='特别是，他们呼吁与西部各州政府建立更紧密的合作关系，这些州政府往往对联邦行动感到不安，并与控制着估计95%的草原松鸡栖息地的私人土地所有者合作。',
    insight=False, note='',
    bold=['forging closer collaborations', 'uneasy with', 'landowners'],
    chunks=[
        dict(role='状语', text='In particular,',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='called for forging closer collaborations with western state governments,',
             note='call for doing 呼吁做；forge 建立'),
        dict(role='定语从句', text='which are often uneasy with federal action,',
             note='which 引导非限制性定语从句修饰 governments'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='介词短语', text="with the private landowners who control an estimated 95% of the prairie chicken's habitat.",
             note='与前面 with 并列；who... 定语从句修饰 landowners'),
    ])

A['P3S1'] = dict(
    zh='例如，根据该计划，该机构表示不会起诉无意中杀死、伤害或干扰该鸟的土地所有者或企业，只要他们签署了恢复草原松鸡栖息地的全面管理计划。',
    insight=True, note='覆盖主谓宾、定语从句、宾语从句、条件状语从句、不定式作定语等多种成分,且定语从句的"that"在从句中作主语、宾语从句前置于主句谓语之后,都是常见易错点,练习价值高',
    bold=['prosecute', 'as long as', 'range-wide'],
    chunks=[
        dict(role='状语', text='Under the plan, for example,',
             note=''),
        dict(role='主语', text='the agency',
             note=''),
        dict(role='谓语', text='said',
             note=''),
        dict(role='宾语从句', text='it would not prosecute landowners or businesses that unintentionally kill, harm, or disturb the bird,',
             note='省略 that 的宾语从句；that... 定语从句修饰 businesses；三个并列动词'),
        dict(role='状语从句', text='as long as they had signed a range-wide management plan to restore prairie chicken habitat.',
             note='as long as 引导条件状语从句；to restore... 不定式作后置定语'),
    ])

A['P3S2'] = dict(
    zh='该计划由USFWS和各州协商制定，要求在其运营过程中破坏栖息地的个人和企业向一个基金支付费用，用每2英亩合适的栖息地替换被破坏的每1英亩。',
    insight=True, note='本句使用了requiresomebodytodo复合宾语结构和限制性定语从句修饰宾语的组合，这是四六级和考研真题中高频出现的句式。过去分词短语作状语也是常见考点。整体结构具有较高的代表性和复用价值。',
    bold=['requires', 'pay into a fund', 'habitat'],
    chunks=[
        dict(role='状语', text='Negotiated by USFWS and the states,',
             note='过去分词短语作状语'),
        dict(role='主语', text='the plan',
             note=''),
        dict(role='谓语', text='requires',
             note=''),
        dict(role='宾语', text='individuals and businesses that damage habitat as part of their operations',
             note='that... 定语从句修饰 businesses'),
        dict(role='宾语补足语', text='to pay into a fund to replace every acre destroyed with 2 new acres of suitable habitat.',
             note='require sb. to do 宾补；to replace... 目的状语；destroyed 过去分词作后置定语'),
    ])

A['P3S3'] = dict(
    zh='该基金还将用于补偿那些预留栖息地的土地所有者。',
    insight=True, note='被动语态加不定式目的状语的结构（beusedtodo）以及限制性定语从句修饰宾语的模式，都是四六级和考研阅读中的高频句式。掌握这类结构后可以迁移到大量类似句子，具有较强的代表性和实用性。',
    bold=['compensate', 'set aside'],
    chunks=[
        dict(role='主语', text='The fund',
             note=''),
        dict(role='谓语', text='will also be used to compensate',
             note=''),
        dict(role='宾语', text='landowners who set aside habitat.',
             note='被动语态 + 不定式作目的；who... 定语从句修饰 landowners；set aside 预留'),
    ])

A['P3S4'] = dict(
    zh='USFWS还设定了一个中期目标，即在未来10年内将草原松鸡种群恢复到年平均67000只。',
    insight=False, note='',
    bold=['interim goal', 'restoring'],
    chunks=[
        dict(role='主语', text='USFWS',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='set',
             note=''),
        dict(role='宾语', text='an interim goal of restoring prairie chicken populations to an annual average of 67,000 birds over the next 10 years.',
             note='of restoring... 动名词作后置定语；interim 中期的'),
    ])
