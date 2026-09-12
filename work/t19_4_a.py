# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='Arnold Schwarzenegger、Dia Mirza和Adrian Grenier向你传递一个信息:战胜塑料很容易。',
    insight=False, note='',
    bold=['have a message for you', 'beat plastic'],
    chunks=[
        dict(role='主语', text='Arnold Schwarzenegger, Dia Mirza and Adrian Grenier',
             note=''),
        dict(role='谓语', text='have',
             note=''),
        dict(role='宾语', text='a message for you:',
             note=''),
        dict(role='同位语从句', text="It's easy to beat plastic.",
             note='冒号后为同位语从句；it 形式主语；to beat... 真正主语'),
    ])

A['P1S2'] = dict(
    zh='他们是为世界环境日拍摄新视频的一群名人中的一部分，该视频鼓励你这样的消费者，用可替代品取代你的一次性塑料必需品，如吸管和餐具，以应对塑料危机。',
    insight=False, note='',
    bold=['starring in', 'swap out', 'single-use plastic'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text="'re",
             note=''),
        dict(role='表语', text='part of a bunch of celebrities starring in a new video for World Environment Day –',
             note='starring in... 现在分词作后置定语'),
        dict(role='状语', text='encouraging you, the consumer, to swap out your single-use plastic staples like straws and cutlery to combat the plastics crisis.',
             note='现在分词作补充说明；the consumer 为同位语；encourage sb. to do 宾补；to combat... 不定式作目的状语'),
    ])

A['P2S1'] = dict(
    zh='为世界环境日整合的关键信息确实包括呼吁政府制定法律来遏制一次性塑料。',
    insight=True, note='本句结构高度典型:限制性定语从句修饰主语、强调助动词"do"加强语气、宾语后接"for+名词+todo"结构表达呼吁对象与内容,这些都是四六级和考研阅读中的高频句式。掌握本句的拆解方法,可直接迁移到大量同类结构的真题句子,代表性很强。',
    bold=['put together', 'enact legislation', 'curb'],
    chunks=[
        dict(role='主语', text='The key messages that have been put together for World Environment Day',
             note='that... 定语从句修饰 messages；put together 汇集'),
        dict(role='谓语', text='do include',
             note='do 强调'),
        dict(role='宾语', text='a call for governments to enact legislation to curb single-use plastics.',
             note='a call for sb. to do；两个不定式分别作后置定语与目的状语'),
    ])

A['P2S2'] = dict(
    zh='但总体信息是针对个人的。',
    insight=False, note='',
    bold=['overarching message', 'directed at'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='the overarching message',
             note=''),
        dict(role='谓语', text='is directed at',
             note=''),
        dict(role='宾语', text='individuals.',
             note='overarching 总体的；be directed at 针对'),
    ])

A['P3S1'] = dict(
    zh='然而，我对把这件事留给个人的担忧在于，我们对需要实现什么目标的认识有限。',
    insight=False, note='',
    bold=['leaving it up to', 'limited sense'],
    chunks=[
        dict(role='主语', text='My concern with leaving it up to the individual, however,',
             note='动名词作介词宾语；leave sth. up to sb. 把…留给某人'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='our limited sense of what needs to be achieved.',
             note='what 引导宾语从句作介词宾语'),
    ])

A['P3S2'] = dict(
    zh='例如，仅靠我们自己带购物袋去杂货店或戒掉塑料吸管，将取得很少成就，也只需要我们付出很少。',
    insight=False, note='',
    bold=['On their own', 'accomplish little', 'quitting'],
    chunks=[
        dict(role='状语', text='On their own,',
             note='独立地；靠自身'),
        dict(role='主语', text='taking our own bags to the grocery store or quitting plastic straws, for example,',
             note='两个并列动名词短语作主语'),
        dict(role='谓语', text='will accomplish little and require very little of us.',
             note='并列谓语'),
    ])

A['P3S3'] = dict(
    zh="它们甚至可能是有害的，满足了一种'我们已经尽力'的需求，却从未进展到更大、更大胆、更有效的行动——一种'道德许可'，它缓解了我们的担忧，阻止我们做更多事情和向掌权者要求更多。",
    insight=False, note='',
    bold=['detrimental', 'moral licensing', 'allays'],
    chunks=[
        dict(role='主语', text='They',
             note=''),
        dict(role='谓语', text='could even be',
             note=''),
        dict(role='表语', text='detrimental,',
             note=''),
        dict(role='状语', text='satisfying a need to have "done our bit" without ever progressing onto bigger, bolder, more effective actions –',
             note='现在分词作伴随状语；without + 动名词'),
        dict(role='同位语', text='a kind of "moral licensing" that allays our concerns and stops us doing more and asking more of those in charge.',
             note='对前面行为的同位解释；that... 定语从句；stop sb. doing 阻止'),
    ])
