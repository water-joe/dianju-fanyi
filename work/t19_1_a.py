# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='与所谓的悲伤、恐惧和愤怒等基本情绪不同，内疚出现得稍晚一些，与儿童对社会和道德规范的理解不断增强相伴而生。',
    insight=False, note='',
    bold=['Unlike', 'emerges', 'moral norms'],
    chunks=[
        dict(role='状语', text='Unlike so-called basic emotions such as sadness, fear, and anger,',
             note='unlike 介词短语作对比状语'),
        dict(role='主语', text='guilt',
             note=''),
        dict(role='谓语', text='emerges',
             note=''),
        dict(role='状语', text='a little later,',
             note=''),
        dict(role='状语', text="in conjunction with a child's growing grasp of social and moral norms.",
             note='in conjunction with 与…相伴'),
    ])

A['P1S2'] = dict(
    zh='孩子们并非生来就知道如何说"对不起"；相反，他们随着时间推移逐渐了解到这样的表述能够安抚父母和朋友——以及他们自己的良心。',
    insight=True, note='本句成分较为丰富,包含主语、谓语、宾语、宾语从句、伴随状语、时间状语等多种成分,且涉及两个并列主句的划分。第一个主句中"knowinghowtosay"的伴随状语容易被误判为谓语,第二个主句中时间状语"overtime"插在谓语和宾语之间,都是值得练习的易错点。此外,两个宾语从句的识别和划分也有助于巩固从句概念',
    bold=["aren't born knowing", 'appease', 'consciences'],
    chunks=[
        dict(role='主语', text='Children',
             note=''),
        dict(role='谓语', text="aren't born knowing",
             note=''),
        dict(role='宾语', text='how to say "I\'m sorry";',
             note='疑问词+不定式作宾语'),
        dict(role='状语', text='rather,',
             note=''),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='learn',
             note=''),
        dict(role='状语', text='over time',
             note=''),
        dict(role='宾语从句', text='that such statements appease parents and friends – and their own consciences.',
             note='that 引导宾语从句；appease 安抚'),
    ])

A['P1S3'] = dict(
    zh='这就是为什么研究人员普遍认为，适量的所谓道德内疚是一件好事。',
    insight=False, note='',
    bold=['regard', 'in the right amount'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='is why',
             note='why 引导表语从句'),
        dict(role='表语从句', text='researchers generally regard so-called moral guilt, in the right amount, to be a good thing.',
             note='regard A to be B 认为 A 是 B；in the right amount 插入语'),
    ])

A['P2S1'] = dict(
    zh='当然，在大众想象中，内疚仍然名声不佳。',
    insight=False, note='',
    bold=['gets a bad rap'],
    chunks=[
        dict(role='状语', text='In the popular imagination, of course,',
             note='of course 插入语'),
        dict(role='主语', text='guilt',
             note=''),
        dict(role='状语', text='still',
             note=''),
        dict(role='谓语', text='gets',
             note=''),
        dict(role='宾语', text='a bad rap.',
             note='get a bad rap 名声不好'),
    ])

A['P2S2'] = dict(
    zh='它令人深感不适——就像穿着一件装满石头的沉重外套。',
    insight=False, note='',
    bold=['the emotional equivalent of', 'weighted with'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text='is deeply uncomfortable –',
             note=''),
        dict(role='表语', text="it's the emotional equivalent of wearing a jacket weighted with stones.",
             note='be the equivalent of 相当于；weighted with 过去分词作后置定语'),
    ])

A['P2S3'] = dict(
    zh='然而这种理解已经过时了。',
    insight=True, note='主系表结构是基础句型，但本句过于简短、无修饰成分，作为考试真题句式的代表性较弱，难以迁移到复杂语境。',
    bold=['outdated'],
    chunks=[
        dict(role='连接词', text='Yet',
             note=''),
        dict(role='主语', text='this understanding',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='outdated.',
             note=''),
    ])

A['P2S4'] = dict(
    zh='"人们对内疚是什么以及内疚能发挥什么作用进行了某种复兴或重新思考，"弗吉尼亚大学的心理学研究员Amrisha Vaish说道，并补充说这种复兴是更广泛认识的一部分，即情绪不是二元的——在某种情境下可能有利的情感在另一种情境下可能有害。',
    insight=True, note='涵盖了倒装、同位语短语、非谓语动词作状语、多种从句及破折号用法，是练习成分分析的极佳素材。',
    bold=['revival', 'binary', 'advantageous'],
    chunks=[
        dict(role='主语', text='"There has been',
             note=''),
        dict(role='主语', text='a kind of revival or a rethinking about what guilt is and what role guilt can serve,"',
             note='there be 句型真正主语；两个 what 引导宾语从句'),
        dict(role='谓语', text='says',
             note='引述动词（前置倒装）'),
        dict(role='主语', text='Amrisha Vaish,',
             note=''),
        dict(role='同位语', text='a psychology researcher at the University of Virginia,',
             note=''),
        dict(role='状语', text="adding that this revival is part of a larger recognition that emotions aren't binary – feelings that may be advantageous in one context may be harmful in another.",
             note='现在分词作伴随状语；that... 宾语从句内又嵌套 that... 同位语从句；破折号后为说明'),
    ])

A['P2S5'] = dict(
    zh='例如，嫉妒和愤怒可能是进化出来提醒我们注意重要的不平等现象的。',
    insight=True, note='情态动词加完成式的结构在四六级和考研阅读中频繁出现，目的状语不定式也是常考句式，本句作为此类结构的代表性较强，学习后可迁移到大量类似句子。',
    bold=['evolved', 'alert us to'],
    chunks=[
        dict(role='主语', text='Jealousy and anger,',
             note=''),
        dict(role='插入语', text='for example,',
             note=''),
        dict(role='谓语', text='may have evolved',
             note=''),
        dict(role='状语', text='to alert us to important inequalities.',
             note='不定式作目的状语；alert sb. to 提醒某人注意'),
    ])
