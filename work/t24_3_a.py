# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='让不安全的老年驾驶员远离道路的最大挑战之一是说服他们是时候交出钥匙了。',
    insight=True, note='主系表结构配合动名词作表语是四六级和考研阅读中的常见句式,宾语从句和不定式后置定语也是高频考点。句中"Oneofthebiggestchallengesisdoingsomething"这类表达在议论文中出现频率较高,具有较强的迁移价值。掌握本句结构后可应用于大量类似语境。',
    bold=['One of the biggest challenges', 'convincing them that', 'turn over the keys'],
    chunks=[
        dict(role='主语', text='One of the biggest challenges in keeping unsafe aging drivers off the road',
             note='in keeping... 动名词短语作后置定语；keep... off 使…远离'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text="convincing them that it's time to turn over the keys",
             note='动名词短语作表语；that 引导宾语从句；to turn over... 不定式作后置定语'),
    ])

A['P1S2'] = dict(
    zh='"当有人停止——或被迫停止——驾驶时，"这完全改变了生活"，前风险管理人员Anne M. Menke说。',
    insight=False, note='',
    bold=['life-changer', 'forced to stop', 'former risk manager'],
    chunks=[
        dict(role='宾语', text='"It\'s a complete life-changer"',
             note='直接引语（主句）'),
        dict(role='状语从句', text='when someone stops—or is forced to stop—driving,',
             note='when 引导时间状语从句；or is forced to stop 并列（插入破折号）'),
        dict(role='谓语', text='said',
             note='引述动词'),
        dict(role='同位语', text='former risk manager Anne M.',
             note='Anne M. 为引述分句主语；former risk manager 为其同位语（与 P1S3 的 Menke. 合为姓名）'),
    ])

A['P1S3'] = dict(
    zh='Menke。（接上句：前风险管理人员 Anne M. Menke）',
    insight=False, note='',
    bold=['Menke'],
    chunks=[
        dict(role='同位语', text='Menke.',
             note='上句 Anne M. 的姓氏，中间被引语隔断（PDF 分句所致）'),
    ])

A['P2S1'] = dict(
    zh='"美国医学会建议医生，\'在有明确证据表明存在严重驾驶障碍，对患者和公共安全构成重大威胁，且医生建议停止驾驶特权而被忽视的情况下，通知机动车辆管理部门是可取且合乎道德的。\'"Menke写道。',
    insight=True, note='覆盖丰富：双宾语结构（advisesphysiciansthat）、形式主语（it...tonotify）、直接引语作宾语、长状语前置、并列定语从句、被动语态、不定式作后置定语等多种成分和句式；特别是形式主语和双宾语是常见易错点，适合反复练习划分。',
    bold=['advises physicians that', 'substantial driving impairment', 'it is desirable and ethical to'],
    chunks=[
        dict(role='宾语', text='"The American Medical Association advises physicians that \'in situations where clear evidence of substantial driving impairment implies a strong threat to patient and public safety, and where the physician\'s advice to discontinue driving privileges is ignored, it is desirable and ethical to notify the Department of Motor Vehicles,\'"',
             note='直接引语作 wrote 的宾语；内层：advises sb. that 双宾语结构；where... and where... 两个并列定语从句修饰 situations；it 形式主语，真正主语为 to notify...'),
        dict(role='主语', text='Menke',
             note=''),
        dict(role='谓语', text='wrote.',
             note=''),
    ])
