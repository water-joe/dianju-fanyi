# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S4'] = dict(
    zh='Radesky说:"父母不必时刻都极度专注，但需要有一个平衡，父母需要对孩子的语言或非语言情感需求表达做出回应和敏感。"',
    insight=False, note='',
    bold=['exquisitely present', 'responsive and sensitive'],
    chunks=[
        dict(role='宾语', text='"Parents don\'t have to be exquisitely present at all times, but there needs to be a balance and parents need to be responsive and sensitive to a child\'s verbal or nonverbal expressions of an emotional need,"',
             note='直接引语作 says 的宾语；多个并列分句'),
        dict(role='谓语', text='says',
             note=''),
        dict(role='主语', text='Radesky.',
             note=''),
    ])

A['P4S1'] = dict(
    zh='另一方面，Tronick本人担心对孩子使用屏幕的忧虑源于一种"压迫性的意识形态，要求父母应该始终与孩子互动":"这基于一种有些理想化的、非常白人的、非常中上阶层的意识形态，认为如果你没有让孩子接触三万个单词，你就是在忽视他们。"',
    insight=True, note='本句包含了几乎所有典型语法点：多种从句、双宾语、不定式作定语、并列结构、从句作主语等，是极佳的综合练习素材。',
    bold=['oppressive ideology', 'neglecting them'],
    chunks=[
        dict(role='状语', text='On the other hand,',
             note=''),
        dict(role='主语', text='Tronick himself',
             note=''),
        dict(role='谓语', text='is concerned',
             note=''),
        dict(role='宾语从句', text='that the worries about kids\' use of screens are born out of an "oppressive ideology that demands that parents should always be interacting" with their children:',
             note='that 引导宾语从句；that demands that... 定语从句内含宾语从句'),
        dict(role='宾语', text='"It\'s based on a somewhat fantasised, very white, very upper-middle-class ideology that says if you\'re failing to expose your child to 30,000 words you are neglecting them."',
             note='直接引语；that... 定语从句修饰 ideology；if 引导条件从句'),
    ])

A['P4S2'] = dict(
    zh='Tronick认为，仅仅因为孩子没有从屏幕中学习并不意味着它没有价值——特别是如果它能让父母有时间洗澡、做家务或只是从孩子那里休息一下。',
    insight=True, note='句子覆盖主语、谓语、宾语、状语以及插入语的识别，成分种类较为丰富。插入语的识别是一个值得练习的点，状语部分"outofusing..."结构较长且包含并列成分，有助于训练学生识别复杂状语的能力。但整体难度适中，缺少定语从句、宾语从句等更复杂的成分。',
    bold=['just because', 'have a break from'],
    chunks=[
        dict(role='主语', text='Tronick',
             note=''),
        dict(role='谓语', text='believes',
             note=''),
        dict(role='宾语从句', text="that just because a child isn't learning from the screen doesn't mean there's no value to it –",
             note="just because 引导主语从句；doesn't mean (that)... 宾语从句"),
        dict(role='状语', text='particularly if it gives parents time to have a shower, do housework or simply have a break from their child.',
             note='if 引导条件状语从句；三个并列不定式作后置定语'),
    ])

A['P4S3'] = dict(
    zh='他说，父母可以通过使用设备与朋友交谈或完成一些工作而获得很多好处。',
    insight=True, note='本句覆盖主谓宾补结构、情态动词谓语、使役动词用法、非限制性定语从句等多种成分和结构。宾语补足语"feelhappier"和"bemoreavailable..."是常见易错点,值得练习区分补足语与独立谓语。成分种类较丰富,训练价值较高。',
    bold=['get a lot out of', 'out of the way'],
    chunks=[
        dict(role='主语', text='Parents,',
             note=''),
        dict(role='插入语', text='he says,',
             note=''),
        dict(role='谓语', text='can get a lot out of',
             note=''),
        dict(role='宾语', text='using their devices to speak to a friend or get some work out of the way.',
             note='get a lot out of 从…中获益；out of the way 处理掉'),
    ])

A['P4S4'] = dict(
    zh='这可以让他们感到更快乐，从而让他们在其余时间更能陪伴孩子。',
    insight=False, note='',
    bold=['available to'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text='can make',
             note=''),
        dict(role='宾语', text='them',
             note=''),
        dict(role='宾语补足语', text='feel happier,',
             note='make sb. do 宾补'),
        dict(role='定语从句', text='which lets them be more available to their child the rest of the time.',
             note='which 引导非限制性定语从句；let sb. do 宾补；available to 能陪伴'),
    ])
