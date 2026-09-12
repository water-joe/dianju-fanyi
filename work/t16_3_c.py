# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S3'] = dict(
    zh='你可能会认为这会助长效率心态，但事实上，Eberle指出，这种仪式化行为帮助我们"走出时间的流动"进入"灵魂时间"。',
    insight=True, note='本句成分丰富且有多个训练点：宾语从句（省略that）、插入语识别、"helpsbdosth"结构中的宾语补足语、状语"infact"的定位。尤其是第二个主句，插入语和宾语从句的层层嵌套容易产生误判，适合作为成分划分的进阶练习。',
    bold=['fuel the efficiency mind-set', 'ritualistic behaviour'],
    chunks=[
        dict(role='主语', text='You',
             note=''),
        dict(role='谓语', text="'d think",
             note=''),
        dict(role='宾语从句', text='this might fuel the efficiency mind-set,',
             note='省略 that 的宾语从句'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='状语', text='in fact,',
             note=''),
        dict(role='插入语', text='Eberle notes,',
             note=''),
        dict(role='主语', text='such ritualistic behaviour',
             note=''),
        dict(role='谓语', text='helps',
             note=''),
        dict(role='宾语', text='us',
             note=''),
        dict(role='宾语补足语', text='"step outside time\'s flow" into "soul time."',
             note='help sb. do 宾补（省略 to）'),
        dict(role='主语', text='You',
             note=''),
        dict(role='谓语', text='could limit',
             note=''),
        dict(role='宾语', text='distractions',
             note=''),
        dict(role='状语', text='by reading only physical books, or on single-purpose e-readers.',
             note='by + 动名词表方式'),
    ])

A['P4S4'] = dict(
    zh='"随时随地带本书"实际上也能奏效——只要你足够频繁地翻阅，让阅读成为默认状态，你只是暂时从中浮出水面来处理事务，然后再沉回去。',
    insight=True, note='全句包含一个主句,主句后嵌套providing条件状语从句,该从句内部又嵌套sothat结果状语从句,sothat从句的表语后还带有fromwhich定语从句,形成三层嵌套加一个定语修饰的结构;providing从句与sothat从句之间、sothat从句与定语从句之间的归属关系需要仔细辨析,初学者容易混淆从属层级,需反复回读才能理清',
    bold=['providing you dip in', 'the default state', 'take care of business'],
    chunks=[
        dict(role='主语', text='"Carry a book with you at all times"',
             note=''),
        dict(role='谓语', text='can actually work, too –',
             note=''),
        dict(role='状语从句', text='providing you dip in often enough,',
             note='providing (that) 引导条件状语从句；dip in 翻阅'),
        dict(role='状语从句', text='so that reading becomes the default state from which you temporarily surface to take care of business, before dropping back down.',
             note='so that 引导结果状语从句；from which... 定语从句修饰 state；to take care... 目的状语'),
    ])

A['P4S5'] = dict(
    zh='在真正美好的一天，你不再觉得自己是在"腾出时间阅读"，而只是在阅读，并为其他一切事情腾出时间。',
    insight=True, note='本句覆盖了多种成分：主句有主语（"it"）、谓语（系动词"feels"）、时间状语（"Onareallygoodday"）、程度状语（"nolonger"）、表语（"asif"从句）；表语从句内部有主语（"you"）、三个并列谓语（含省略）、两个宾语（"timetoread"和"timeforeverythingelse"）、一个程度状语（"just"）；成分种类丰富，且包含系动词表语从句、并列省略、不定式作定语等多个值得练习的点。',
    bold=['as if', 'making time to read'],
    chunks=[
        dict(role='状语', text='On a really good day,',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='状语', text='no longer',
             note=''),
        dict(role='谓语', text='feels',
             note=''),
        dict(role='表语从句', text='as if you\'re "making time to read," but just reading, and making time for everything else.',
             note='as if 引导表语从句；三个并列动名词结构'),
    ])
