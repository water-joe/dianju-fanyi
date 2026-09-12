# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 4 — 逐句成分划分（自动生成，勿手改引号）。"""
A = {}

A['P2S1'] = dict(
    zh='关键的是，另一组被要求在给出评分之前花一分钟写下他们判断的理由。',
    insight=True, note='本句成分丰富，主句包含主语、谓语、宾语补足语、状语等多种成分，且宾语补足语内部嵌套不定式和分词结构，适合练习识别非谓语动词。状语从句虽然简单，但涉及动名词作谓语核心的特殊用法，以及省略主语的情况，是典型的易错点。句首的独立副词Critically也是状语成分的常见形式，整体训练价值较高。',
    bold=['Critically', 'spend a minute writing down', 'before giving'],
    chunks=[
        dict(role='状语', text='Critically,',
             note='评注性状语'),
        dict(role='主语', text='another group',
             note=''),
        dict(role='谓语', text='was asked to spend a minute writing down reasons for their judgment, before giving the rating',
             note='be asked to do 被要求做；writing down... 现在分词；before giving... 动名词短语作时间状语'),
    ])

A['P2S2'] = dict(
    zh='准确性急剧下降。',
    insight=False, note='',
    bold=['dropped dramatically'],
    chunks=[
        dict(role='主语', text='Accuracy',
             note=''),
        dict(role='谓语', text='dropped dramatically',
             note='dramatically 急剧地'),
    ])

A['P2S3'] = dict(
    zh='Ambady怀疑深思熟虑使他们专注于生动但具有误导性的线索，例如某些手势或话语，而不是让微妙信号的复杂相互作用形成整体印象。',
    insight=True, note='suspectthat引导的宾语从句结构在四六级和考研阅读中极为常见,从句内部的focuson搭配和ratherthan对比结构也是高频句式,掌握后可大量复用于理解类似的心理活动描写和对比论证句',
    bold=['suspected', 'focused them on', 'rather than'],
    chunks=[
        dict(role='主语', text='Ambady',
             note=''),
        dict(role='谓语', text='suspected',
             note='后接省略 that 的宾语从句'),
        dict(role='宾语从句', text='that deliberation focused them on vivid but misleading cues, such as certain gestures or utterances, rather than letting the complex interplay of subtle signals form a holistic impression',
             note='focus on 专注于；such as... 举例；rather than 而非'),
    ])

A['P2S4'] = dict(
    zh='当参与者观看15秒的两人配对视频片段并判断他们是陌生人、朋友还是约会对象时，她发现了类似的干扰。',
    insight=True, note='主句+时间状语从句+嵌套宾语从句的结构在学术文章和考试阅读中非常常见。whether引导的宾语从句、并列谓语、复杂名词短语修饰等都是四六级和考研的高频句式，掌握后可大量复用。',
    bold=['when participants watched', 'similar interference', 'whether they were'],
    chunks=[
        dict(role='主语', text='She',
             note='主句主语'),
        dict(role='谓语', text='found similar interference',
             note='主句谓语'),
        dict(role='状语从句', text='when participants watched 15-second clips of pairs of people and judged whether they were strangers, friends, or dating partners',
             note='when 引导时间状语从句；内含 and 并列谓语；whether 引导宾语从句作 judged 的宾语'),
    ])

A['P3S1'] = dict(
    zh='其他研究表明，当我们依靠直觉而非反思时，我们更善于从薄片中检测欺骗。',
    insight=True, note='主句+宾语从句+状语从句是四六级和考研真题中的高频句式，宾语从句省略"that"和"when"引导时间状语从句都是典型考点，学习迁移价值高。',
    bold=['Other research shows', 'detecting deception', 'instead of reflection'],
    chunks=[
        dict(role='主语', text='Other research',
             note=''),
        dict(role='谓语', text='shows',
             note='后接省略 that 的宾语从句'),
        dict(role='宾语从句', text="we're better at detecting deception from thin slices when we rely on intuition instead of reflection",
             note='when 引导时间状语从句；detecting... 动名词作 at 的宾语'),
    ])

A['P3S2'] = dict(
    zh='"这就像你在开手动挡车，"东北大学心理学家Judith Hall说，"如果你开始想得太多，你就记不住自己在做什么。"',
    insight=True, note='引语插入、条件从句前置以及"Itisasif..."的比喻句式在真题阅读中极其常见，具有很强的复用价值。',
    bold=["It's as if", 'driving a stick shift', "can't remember what"],
    chunks=[
        dict(role='宾语', text='"It\'s as if you\'re driving a stick shift,"',
             note='直接引语（比喻句）作 says 的宾语'),
        dict(role='谓语', text='says',
             note='引述动词（主句谓语）'),
        dict(role='主语', text='Judith Hall',
             note='主句主语'),
        dict(role='同位语', text='a psychologist at Northeastern University',
             note='说明 Judith Hall 身份'),
        dict(role='宾语', text='"and if you start thinking about it too much, you can\'t remember what you\'re doing.',
             note='直接引语续作 says 的宾语；if 条件从句 + what 宾语从句'),
    ])

A['P3S3'] = dict(
    zh='但如果你进入自动驾驶模式，你就没问题。',
    insight=False, note='',
    bold=['go on automatic pilot'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='状语从句', text='if you go on automatic pilot',
             note='if 引导条件状语从句'),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text="'re fine",
             note='系表'),
    ])

A['P3S4'] = dict(
    zh='我们的社会生活很大程度上就是这样。',
    insight=False, note='',
    bold=['Much of'],
    chunks=[
        dict(role='主语', text='Much of our social life',
             note=''),
        dict(role='谓语', text='is like that',
             note='系表，like that 像那样'),
    ])
