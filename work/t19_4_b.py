# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh="当围绕我们的环境和我们对环境的责任的讨论仍然集中在购物袋和吸管上时，我们忽略了权力平衡，这种平衡意味着作为'消费者'，我们必须可持续地购物，而不是作为'公民'追究我们的政府和行业的责任，推动真正的系统性变革。",
    insight=True, note='本句成分丰富且层次分明，涵盖主语、谓语、宾语、表语、定语从句、宾语从句、状语从句、方式状语、目的状语、宾语补足语等多种成分，且出现"hold...toaccount"等固定搭配、情态动词结构、并列动词省略、定语从句嵌套宾语从句等易错点，作为划分练习句收益很高。',
    bold=['centered on', 'hold our governments and industries to account', 'systemic change'],
    chunks=[
        dict(role='状语从句', text='While the conversation around our environment and our responsibility toward it remains centered on shopping bags and straws,',
             note='while 引导让步状语从句；be centered on 集中于'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text="'re ignoring",
             note=''),
        dict(role='宾语', text='the balance of power',
             note=''),
        dict(role='定语从句', text='that implies that as "consumers" we must shop sustainably, rather than as "citizens" hold our governments and industries to account to push for real systemic change.',
             note='第一个 that 定语从句修饰 balance；that... implies 后接宾语从句；hold sb. to account 追究责任；to push for... 目的状语'),
    ])

A['P5S1'] = dict(
    zh='重要的是要承认，环境并不是每个人的优先事项——甚至不是大多数人的优先事项。',
    insight=False, note='',
    bold=['acknowledge', 'priority'],
    chunks=[
        dict(role='主语', text='It',
             note='形式主语'),
        dict(role='谓语', text="'s important",
             note=''),
        dict(role='真正主语', text="to acknowledge that the environment isn't everyone's priority – or even most people's.",
             note='不定式作真正主语；that 引导宾语从句'),
    ])

A['P5S2'] = dict(
    zh='我们不应该期望它是。',
    insight=False, note='',
    bold=['expect it to be'],
    chunks=[
        dict(role='主语', text='We',
             note=''),
        dict(role='谓语', text="shouldn't expect",
             note=''),
        dict(role='宾语', text='it',
             note=''),
        dict(role='宾语补足语', text='to be.',
             note='it 指 environment 是 priority；承前省略'),
    ])

A['P5S3'] = dict(
    zh='在她的最新著作《为什么好人做坏的环境事》中，Wellesley College教授Elizabeth R. DeSombre认为，集体改变大量人群行为的最佳方式是让改变成为结构性的。',
    insight=False, note='',
    bold=['latest book', 'Wellesley College professor'],
    chunks=[
        dict(role='状语', text='In her latest book, Why Good People Do Bad Environmental Things,',
             note=''),
        dict(role='主语', text='Wellesley College professor Elizabeth R.',
             note=''),
    ])

A['P5S4'] = dict(
    zh='DeSombre认为，集体改变大量人群行为的最佳方式是让改变成为结构性的。',
    insight=False, note='',
    bold=['collectively', 'structural'],
    chunks=[
        dict(role='主语', text='DeSombre',
             note=''),
        dict(role='谓语', text='argues',
             note=''),
        dict(role='宾语从句', text='that the best way to collectively change the behavior of large numbers of people is for the change to be structural.',
             note='that 引导宾语从句；to change... 不定式作后置定语；for... to be... 不定式复合结构作表语'),
    ])

A['P6S1'] = dict(
    zh='这可能意味着实施政策，如塑料税，为环境问题行为增加成本，或者完全禁止一次性塑料。',
    insight=False, note='',
    bold=['implementing policy', 'altogether'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='might mean',
             note=''),
        dict(role='宾语', text='implementing policy such as a plastic tax that adds a cost to environmentally problematic action, or banning single-use plastics altogether.',
             note='两个并列动名词作宾语；that... 定语从句修饰 tax；altogether 完全地'),
    ])

A['P6S2'] = dict(
    zh='印度刚刚宣布将"在2022年之前消除该国所有一次性塑料"。',
    insight=False, note='',
    bold=['eliminate'],
    chunks=[
        dict(role='主语', text='India',
             note=''),
        dict(role='谓语', text='has just announced',
             note=''),
        dict(role='宾语从句', text='it will "eliminate all single-use plastic in the country by 2022."',
             note='省略 that 的宾语从句'),
    ])
