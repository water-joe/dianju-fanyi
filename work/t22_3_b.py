# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 3 —— P3 至 P4 的成分划分。口径见 t22_3_a.py 头注释。"""

A = {}

A['P3S1'] = dict(
    zh='在 2019 年一项对 53000 个产品页面和 11000 个网站的研究中，研究人员发现约十分之一采用了这些设计做法。',
    insight=False, note='',
    bold=['In a 2019 study', 'researchers', 'employs'],
    chunks=[
        dict(role='状语', text='In a 2019 study of 53,000 product pages and 11,000 websites'),
        dict(role='主语', text='researchers'),
        dict(role='谓语', text='found'),
        dict(role='宾语', text='that about one in 10 employs these design practices',
             note='省略 that 的宾语从句；one in 10 主语，employs 谓语'),
    ])

A['P3S2'] = dict(
    zh='尽管广泛流行，暗黑模式的概念仍未被充分理解。',
    insight=True,
    note='让步状语从句搭配被动语态主句是四六级和考研阅读中的高频句式，尤其是"Though/Although"引导的让步从句。从句省略主语和系动词的用法也很常见。这种转折对比结构在学术写作和议论文中频繁出现，掌握后可应用于大量类似句子。',
    bold=['Though widely prevalent', 'concept', 'well understood'],
    chunks=[
        dict(role='状语从句', text='Though widely prevalent',
             note='让步状语从句省略主语和系动词（= Though it is widely prevalent）'),
        dict(role='主语', text='the concept of dark patterns'),
        dict(role='谓语', text='is still not well understood', note='被动语态主句'),
    ])

A['P3S3'] = dict(
    zh='企业和非营利组织领导者应该意识到暗黑模式，并努力避免它们所产生的灰色地带。',
    insight=True,
    note='情态动词加并列谓语"should...and(should)..."以及紧贴名词的限制性定语从句都是四六级和考研阅读中的高频句式，这类结构在学术和正式文体中反复出现，掌握后可直接迁移至大量类似句子的理解，典型性较强。',
    bold=['Business and nonprofit leaders', 'aware of', 'avoid', 'gray areas', 'engender'],
    chunks=[
        dict(role='主语', text='Business and nonprofit leaders'),
        dict(role='谓语', text='should be aware of dark patterns and try to avoid the gray areas they engender',
             note='情态动词 should + 并列谓语（be aware of / try to avoid）；they engender 为省略 that 的定语从句修饰 gray areas'),
    ])

A['P4S1'] = dict(
    zh='道德的、具有说服力的设计与暗黑模式之间的界限在哪里？',
    insight=False, note='',
    bold=['ethical', 'persuasive', 'the line between'],
    chunks=[
        dict(role='谓语', text='is', note='系动词，主语后置构成疑问倒装'),
        dict(role='主语', text='the line between ethical, persuasive design and dark patterns',
             note='between...and... 连接两个并列成分'),
    ])

A['P4S2'] = dict(
    zh='企业应该与 IT、合规、风险和法律团队展开对话，审查其隐私政策，并将负责公司用户界面的客户/用户体验设计师和编码人员，以及负责注册、结账篮、定价和促销的营销人员和广告商纳入讨论。',
    insight=True,
    note='本句在主干识别、成分划分和结构典型性方面表现出较高的训练价值，虽然嵌套层次不深、时态语态相对简单，但句子长度适中、成分丰富、结构典型，非常适合作为"句子结构+时态"的综合训练材料，能帮助目标读者在实战中提升分析复杂并列和修饰结构的能力。综合前五维评估，本句值得优先纳入训练库。',
    bold=['engage in conversations', 'compliance', 'privacy policy', 'experience designers', 'marketers'],
    chunks=[
        dict(role='主语', text='Businesses'),
        dict(role='谓语', text='should engage in conversations with IT, compliance, risk, and legal teams'),
        dict(role='状语', text='to review their privacy policy',
             note='不定式作目的状语'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='include', note='与 engage 并列的谓语'),
        dict(role='状语', text='in the discussion',
             note='include 的状语，宾语后置（因带长修饰）'),
        dict(role='宾语', text='the customer/user experience designers and coders responsible for the company\'s user interface, as well as the marketers and advertisers responsible for sign-ups, checkout baskets, pricing, and promotions',
             note='include 的真正宾语；responsible for... 为形容词短语作后置定语，分两组'),
    ])

A['P4S3'] = dict(
    zh='这些团队中的任何一个或全部都可能在创造或避免"数字欺骗"中发挥作用。',
    insight=True,
    note='情态动词 can 加动词原形的结构、后置定语修饰宾语的模式，都是四六级和考研真题中频繁出现的常见句式，具有一定的代表性和迁移价值，但因句子整体过于简单，无复杂嵌套或特殊结构，典型性略打折扣。',
    bold=['Any or all', 'play a role', 'digital deception'],
    chunks=[
        dict(role='主语', text='Any or all these teams'),
        dict(role='谓语', text='can play'),
        dict(role='宾语', text='a role'),
        dict(role='状语', text='in creating or avoiding "digital deception."',
             note='in... 介词短语作状语'),
    ])
