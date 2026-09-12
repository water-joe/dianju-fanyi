# -*- coding: utf-8 -*-
"""2023 Text 4 —— P3 至 P5 的成分划分。口径见 t23_4_a.py 头注释。"""
A = {}

A['P3S1'] = dict(
    zh='研究人员对 200 多名 11 岁到 28 岁的儿童和年轻成人的"亲社会"特质与叛逆特质进行了研究。',
    insight=True,
    note='study A in B 结构（研究 A 在 B 群体中），后面 ranging from...to... 是现在分词短语'
         '作后置定语修饰 children and young adults，给出年龄跨度。'
         '难点是 study 在这里是动词「研究」，不是常见的名词「学习」。',
    bold=['studied', 'traits', 'ranging from'],
    chunks=[
        dict(role='主语', text='The researchers'),
        dict(role='谓语', text='studied'),
        dict(role='宾语', text='"prosocial" and rebellious traits'),
        dict(role='状语', text='in more than 200 children and young adults'),
        dict(role='定语', text='ranging from 11 to 28 years old',
             note='现在分词短语作后置定语，修饰 children and young adults'),
    ])

A['P3S2'] = dict(
    zh='参与者填写了问卷，内容是关于他们做利他、积极的事情（比如牺牲自己的利益去帮助朋友）'
       '或叛逆、消极的事情（比如喝醉或在外逗留到很晚）的频率。',
    insight=True,
    note='句子主干是 fill out questionnaires about + 宾语从句（how often...）。'
         '真正的难点是两个 like 引出的举例结构：'
         'like sacrificing... or rebellious...，以及第二个 like getting drunk or staying out late。'
         '两个 like 属于不同层级：第一个与 altruistic and positive 对应，'
         '第二个与 rebellious and negative 对应。',
    bold=['filled out', 'questionnaires', 'altruistic', 'sacrificing'],
    chunks=[
        dict(role='主语', text='The participants'),
        dict(role='谓语', text='filled out'),
        dict(role='宾语', text='questionnaires'),
        dict(role='定语', text='about how often they did things',
             note='介词短语作后置定语，内含 how often 宾语从句'),
        dict(role='定语从句', text='that were altruistic and positive, like sacrificing their own interests to help a friend, or rebellious and negative, like getting drunk or staying out late',
             note='修饰 things；两个 like 分别举例说明两类行为'),
    ])

A['P4S1'] = dict(
    zh='其他研究表明，叛逆行为会随着你进入青少年时期而增加，然后随着年龄增长而逐渐消失。',
    insight=False, note='',
    bold=['rebellious', 'fades away'],
    chunks=[
        dict(role='主语', text='Other studies'),
        dict(role='谓语', text='have shown', note='现在完成时'),
        dict(role='连接词', text='that'),
        dict(role='主语', text='rebellious behavior', note='宾语从句的主语'),
        dict(role='谓语', text='increases'),
        dict(role='状语从句', text='as you become a teenager', note='时间状语从句'),
        dict(role='连接词', text='and then'),
        dict(role='谓语', text='fades away', note='与 increases 并列'),
        dict(role='状语从句', text='as you grow older'),
    ])

A['P4S2'] = dict(
    zh='但这项新研究显示，有趣的是，同样的模式也适用于亲社会行为。',
    insight=False, note='',
    bold=['the same pattern', 'holds for'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='the new study'),
        dict(role='谓语', text='shows'),
        dict(role='连接词', text='that'),
        dict(role='插入语', text='interestingly'),
        dict(role='主语', text='the same pattern', note='宾语从句的主语'),
        dict(role='谓语', text='holds'),
        dict(role='状语', text='for prosocial behavior',
             note='hold for = 适用于'),
    ])

A['P4S3'] = dict(
    zh='青少年比更年幼的儿童或成年人更有可能报告说，他们会做诸如无私地帮助朋友之类的事情。',
    insight=False, note='',
    bold=['more likely', 'report', 'unselfishly'],
    chunks=[
        dict(role='主语', text='Teenagers'),
        dict(role='谓语', text='were more likely'),
        dict(role='状语', text='than younger children or adults',
             note='比较对象'),
        dict(role='状语', text='to report', note='不定式作状语，说明在哪方面 more likely'),
        dict(role='连接词', text='that'),
        dict(role='主语', text='they', note='宾语从句的主语'),
        dict(role='谓语', text='did'),
        dict(role='宾语', text='things like unselfishly helping a friend'),
    ])

A['P5S1'] = dict(
    zh='最重要的是，亲社会性与叛逆性之间存在正相关关系。',
    insight=False, note='',
    bold=['Most significantly', 'positive correlation'],
    chunks=[
        dict(role='状语', text='Most significantly',
             note='评注性状语，修饰全句'),
        dict(role='形式主语', text='there'),
        dict(role='谓语', text='was', note='there be 存在句'),
        dict(role='主语', text='a positive correlation'),
        dict(role='定语', text='between prosociality and rebelliousness'),
    ])

A['P5S2'] = dict(
    zh='越叛逆的青少年，也越有可能去帮助他人。',
    insight=True,
    note='"the + 比较级 ..., the + 比较级 ..." 结构在主语内部再套一个定语从句'
         '（who were more rebellious），是本句的双重难点。'
         '主句其实是 the more rebellious... the more likely...，'
         '但前半部分被改写成了 the teenagers who were more rebellious。',
    bold=['rebellious', 'more likely'],
    chunks=[
        dict(role='主语', text='The teenagers who were more rebellious',
             note='内含定语从句 who were more rebellious；此处相当于 the more rebellious teenagers'),
        dict(role='谓语', text='were'),
        dict(role='表语', text='also more likely'),
        dict(role='状语', text='to help others'),
    ])

A['P5S3'] = dict(
    zh='青春期好的一面和坏的一面似乎是共同发展的。',
    insight=True,
    note='seem to do 结构中 to develop together 是不定式作表语（或视为复合谓语的一部分）。'
         'together 是副词作方式状语，位置在句末，容易被忽略其修饰关系。'
         '本句虽短，但 seem + 不定式的识别是四六级常见考点。',
    bold=['develop together'],
    chunks=[
        dict(role='主语', text='The good and bad sides of adolescence'),
        dict(role='谓语', text='seem'),
        dict(role='表语', text='to develop', note='不定式作表语'),
        dict(role='状语', text='together', note='方式状语'),
    ])
