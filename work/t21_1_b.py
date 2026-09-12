# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 1 —— P3 至 P4 的成分划分。口径见 t21_1_a.py 头注释。"""

A = {}

A['P3S1'] = dict(
    zh='随着疫情到来，失业率的确非常高。',
    insight=True,
    note='主系表结构在英语中非常常见，介词短语作状语也是高频句式。虽然本句较短且简单，但这种结构在四六级和考研阅读中经常出现，具有一定的典型性和迁移价值。',
    bold=['With the pandemic', 'unemployment', 'indeed'],
    chunks=[
        dict(role='状语', text='With the pandemic'),
        dict(role='主语', text='unemployment'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='very high indeed', note='indeed 为强调副词'),
    ])

A['P3S2'] = dict(
    zh='2 月，加拿大和美国的失业率分别为 3.5% 和 5.5%，处于几代人未见的最低点，各地都出现了劳动力短缺。',
    insight=False, note='',
    bold=['at 3.5 per cent and 5.5 per cent', 'generational lows', 'worker shortages'],
    chunks=[
        dict(role='状语', text='In February, at 3.5 per cent and 5.5 per cent respectively'),
        dict(role='主语', text='unemployment rates in Canada and the United States'),
        dict(role='谓语', text='were'),
        dict(role='表语', text='at generational lows'),
        dict(role='连接词', text='and'),
        dict(role='主语', text='worker shortages'),
        dict(role='谓语', text='were'),
        dict(role='表语', text='everywhere'),
    ])

A['P3S3'] = dict(
    zh='到 5 月，这些比率已飙升至 13.3% 和 13.7%；尽管许多劳动力短缺已经消失，但并非全部如此。',
    insight=True,
    note='并列复合句加让步状语从句是四六级和考研阅读中的常见句式，过去完成时也是常考时态。"although" 引导让步从句、"and" 连接并列主句、代动词 "do" 避免重复，这些都是典型的书面语结构。本句结构具有较强的代表性，掌握后可以迁移到大量类似的复合句分析中，对提升阅读理解能力有实际帮助。',
    bold=['As of May', 'spiked up', 'although', 'disappeared'],
    chunks=[
        dict(role='状语', text='As of May'),
        dict(role='主语', text='those rates'),
        dict(role='谓语', text='had spiked up'),
        dict(role='状语', text='to 13.3 per cent and 13.7 per cent'),
        dict(role='连接词', text='and'),
        dict(role='状语从句', text='although many worker shortages had disappeared',
             note='although 引导让步状语从句，过去完成时'),
        dict(role='主语', text='not all'),
        dict(role='谓语', text='had done so', note='do so 替代 had disappeared，避免重复'),
    ])

A['P3S4'] = dict(
    zh='以医疗领域这个明显的例子来说，疫情意味着医生、护士和其他医务人员仍然存在明显的短缺。',
    insight=False, note='',
    bold=['In the medical field', 'obvious example', 'meant', 'personnel'],
    chunks=[
        dict(role='状语', text='In the medical field, to take an obvious example'),
        dict(role='主语', text='the pandemic'),
        dict(role='谓语', text='meant'),
        dict(role='宾语', text='that there were still clear shortages of doctors, nurses and other medical personnel',
             note='that 引导宾语从句'),
    ])

A['P4S1'] = dict(
    zh='当然，你不可能在几周内把一个失业的服务员培训成医生，无论由谁买单。',
    insight=True,
    note='句子成分丰富：形式主语、表语从句、并列谓语、宾语补足语、时间状语、让步状语，覆盖多种成分类型。特别是形式主语 "it" 和并列谓语 "can take... and train" 是易错点，适合作为划分练习句。',
    bold=['Of course', 'unemployed', 'train', 'no matter who'],
    chunks=[
        dict(role='状语', text='Of course'),
        dict(role='形式主语', text='it'),
        dict(role='谓语', text='is not like'),
        dict(role='表语', text='you can take an unemployed waiter and train him to be a doctor in a few weeks, no matter who pays for it',
             note='like 后接省略 that 的从句作表语；并列谓语 can take... and train；no matter who 让步状语从句'),
    ])

A['P4S2'] = dict(
    zh='但即使你无法弥合那种差距，也许你能弥合其他差距，而这样做将使所有相关者受益。',
    insight=True,
    note='本句涵盖主语、谓语、宾语、表语、状语从句等多种成分，且出现动名词短语作主语 "doing so"、介词短语作表语 "to the benefit of all concerned"、让步状语从句等较丰富的结构，适合练习成分识别和从句定位，具有较好的训练价值。',
    bold=['even if', 'close that gap', 'to the benefit of'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='状语从句', text='even if you cannot close that gap',
             note='even if 引导让步状语从句'),
        dict(role='主语', text='maybe you'),
        dict(role='谓语', text='can close'),
        dict(role='宾语', text='others'),
        dict(role='连接词', text='and'),
        dict(role='主语', text='doing so', note='动名词短语作主语'),
        dict(role='谓语', text='would be'),
        dict(role='表语', text='to the benefit of all concerned', note='介词短语作表语'),
    ])

A['P4S3'] = dict(
    zh='瑞典的情况似乎就是这样：当被迫让 90% 的机舱乘务员休假时，斯堪的纳维亚航空决定启动一个短期再培训项目，对下岗员工进行再培训以支援医院工作人员。',
    insight=True,
    note='全句涵盖了主谓宾、主系表、状语从句、定语从句、目的状语、宾语补足语等多种成分，且状语从句中的省略结构（"When forced..."）和定语从句中的关系代词作主语（"that reskilled..."）都是常见易错点。适合作为成分划分练习句，能训练多个知识点。',
    bold=['That seems to be', 'When forced to furlough', 'decided to start up', 'retraining program', 'laid-off'],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text='seems to be'),
        dict(role='表语', text='the case in Sweden'),
        dict(role='同位语', text=': When forced to furlough 90 per cent of their cabin staff, Scandinavian Airlines decided to start up a short retraining program that reskilled the laid-off workers to support hospital staff',
             note='冒号后解释 the case；when forced... 为省略的时间状语从句；that reskilled... 定语从句修饰 program，to support... 为目的状语'),
    ])

A['P4S4'] = dict(
    zh='这项努力是集体性的，还涉及其他公司以及一所瑞典的大学。',
    insight=False, note='',
    bold=['collective', 'involved'],
    chunks=[
        dict(role='主语', text='The effort'),
        dict(role='谓语', text='was'),
        dict(role='表语', text='a collective one'),
        dict(role='连接词', text='and'),
        dict(role='谓语', text='involved'),
        dict(role='宾语', text='other companies as well as a Swedish university'),
    ])
