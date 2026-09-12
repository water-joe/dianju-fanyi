# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S1'] = dict(
    zh='事实上，"提高效率"本身就是问题的一部分。',
    insight=True, note='主系表结构是四六级和考研中的常见句式，动名词短语作主语也是常考点。句首插入语"Infact"的用法在阅读和写作中频繁出现。但本句结构过于简单，没有从句或复杂修饰，作为典型例句的代表性中等偏上。',
    bold=['becoming more efficient'],
    chunks=[
        dict(role='状语', text='In fact,',
             note=''),
        dict(role='主语', text='"becoming more efficient"',
             note='动名词短语作主语'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='part of the problem.',
             note=''),
    ])

A['P3S2'] = dict(
    zh='把时间视为需要最大化利用的资源，意味着你会工具性地对待它，仅仅根据某个时刻是否推进了某个目标的进展来判断它是否被妥善利用。',
    insight=False, note='',
    bold=['instrumentally', 'as well spent'],
    chunks=[
        dict(role='主语', text='Thinking of time as a resource to be maximised',
             note='动名词短语作主语；to be maximised 不定式作后置定语'),
        dict(role='谓语', text='means',
             note=''),
        dict(role='宾语从句', text='you approach it instrumentally, judging any given moment as well spent only in so far as it advances progress toward some goal.',
             note='省略 that 的宾语从句；judging... 现在分词作伴随状语；in so far as 只要、就…而言'),
    ])

A['P3S3'] = dict(
    zh='相比之下，沉浸式阅读依赖于愿意冒无效率、无目标甚至浪费时间的风险。',
    insight=True, note='"主语+dependon+动名词短语"是四六级和考研阅读中的高频句式，动名词作宾语、不定式作补语的嵌套结构也是常考考点。插入状语的使用符合学术语体特征，具有较强的迁移价值。',
    bold=['Immersive reading', 'goallessness'],
    chunks=[
        dict(role='主语', text='Immersive reading,',
             note=''),
        dict(role='插入语', text='by contrast,',
             note=''),
        dict(role='谓语', text='depends on',
             note=''),
        dict(role='宾语', text='being willing to risk inefficiency, goallessness, even time-wasting.',
             note='动名词作宾语；be willing to do；三个并列名词作 risk 的宾语'),
    ])

A['P3S4'] = dict(
    zh='试图把它作为待办事项清单中的一项塞进去，你只能做到目标导向的阅读——有时有用，但不是最令人满足的那种。',
    insight=False, note='',
    bold=['slot it in', 'goal-focused', 'fulfilling'],
    chunks=[
        dict(role='状语', text='Try to slot it in as a to-do list item',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text="'ll manage only goal-focused reading –",
             note=''),
        dict(role='同位语', text='useful, sometimes, but not the most fulfilling kind.',
             note='对 goal-focused reading 的补充说明'),
    ])

A['P3S5'] = dict(
    zh='Gary Eberle在其著作《神圣时间》中写道:"未来像空瓶子一样沿着一条无法停止且几乎无限的传送带向我们涌来"，"我们感到一种压力，要在这些不同大小的瓶子(天、小时、分钟)经过时填满它们，因为如果它们没被填满就过去了，我们就浪费了它们"。没有哪种心态比这更不利于让自己沉浸在一本书中。',
    insight=True, note='覆盖丰富的成分类型：直接引语作宾语、不定式短语作定语、时间状语从句、原因状语从句、条件状语从句、方式状语、动名词短语、代词指代关系，且包含倒装结构和嵌套从句的成分划分难点，适合综合训练',
    bold=['conveyor belt', 'mind-set', 'losing yourself in a book'],
    chunks=[
        dict(role='宾语', text='"The future comes at us like empty bottles along an unstoppable and nearly infinite conveyor belt,"',
             note='直接引语作 writes 的宾语'),
        dict(role='谓语', text='writes',
             note=''),
        dict(role='主语', text='Gary Eberle in his book Sacred Time,',
             note=''),
        dict(role='宾语', text='and "we feel a pressure to fill these different-sized bottles (days, hours, minutes) as they pass, for if they get by without being filled, we will have wasted them."',
             note='并列直接引语；to fill... 不定式作后置定语；as 时间状语从句；for if... 原因+条件从句'),
        dict(role='主语', text='No mind-set',
             note=''),
        dict(role='谓语', text='could be',
             note=''),
        dict(role='表语', text='worse for losing yourself in a book.',
             note='动名词复合结构作介词宾语'),
    ])

A['P4S1'] = dict(
    zh='那么什么方法有效呢？',
    insight=False, note='',
    bold=['what does work'],
    chunks=[
        dict(role='状语', text='So',
             note=''),
        dict(role='主语', text='what',
             note=''),
        dict(role='谓语', text='does work?',
             note='do 强调'),
    ])

A['P4S2'] = dict(
    zh='或许令人惊讶的是，安排固定的阅读时间。',
    insight=False, note='',
    bold=['scheduling regular times'],
    chunks=[
        dict(role='状语', text='Perhaps surprisingly,',
             note=''),
        dict(role='主语', text='scheduling regular times for reading.',
             note='动名词短语作主语（应答上句）'),
    ])
