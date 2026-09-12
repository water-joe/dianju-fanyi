# -*- coding: utf-8 -*-
"""2024 考研英语二 Text 3 — 逐句成分划分 part2（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='有一件事似乎确实有效，那就是要求驾驶员亲自到场更新驾照。',
    insight=True, note='主系表结构配合限制性定语从句修饰主语，是四六级和考研阅读中的常见句式。动名词短语作表语、定语从句紧跟先行词的布局都是典型考点。掌握本句结构后，学生可将方法迁移到大量类似句子，实用性较强。',
    bold=['does seem to work', 'requiring drivers to', 'license renewal'],
    chunks=[
        dict(role='主语', text='One thing that does seem to work',
             note='that does seem to work 定语从句修饰 thing；does 强调'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='requiring drivers to report in person for license renewal.',
             note='动名词短语作表语；require sb. to do 宾补结构；in person 亲自'),
    ])

A['P4S2'] = dict(
    zh='一项研究显示，强制性亲自更新与85岁或以上驾驶员涉及的致命车祸减少31%相关。',
    insight=True, note='被动语态+介词短语作宾语+分词作后置定语+句末状语，这是四六级和考研阅读中高频出现的学术陈述句式。结构典型，掌握后可大量迁移到类似科研报道或论文摘要的句子中。',
    bold=['Mandatory in-person renewal', 'associated with', 'fatal crashes'],
    chunks=[
        dict(role='主语', text='Mandatory in-person renewal',
             note=''),
        dict(role='谓语', text='was associated with',
             note='be associated with 与…相关；被动语态'),
        dict(role='宾语', text='a 31 percent reduction in fatal crashes involving drivers 85 or older,',
             note='involving... 现在分词短语作后置定语修饰 crashes'),
        dict(role='状语', text='according to one study.',
             note='句末状语，表信息来源'),
    ])

A['P4S3'] = dict(
    zh='通过视力测试也使这些驾驶员的致命车祸出现了类似的下降，尽管将两者结合起来似乎没有什么益处。',
    insight=True, note='although引导的让步状语从句是四六级和考研中的高频句式，动名词短语作主语也是常考结构。therebe变体结构虽不如标准therebe常见，但仍属典型考点。整体句式在真题中有较高的代表性，掌握后可迁移到大量类似句子的分析中。',
    bold=['Passing vision tests', 'a similar decline', 'no benefit from'],
    chunks=[
        dict(role='主语', text='Passing vision tests',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='produced',
             note=''),
        dict(role='宾语', text='a similar decline in fatal crashes for those drivers,',
             note=''),
        dict(role='状语从句', text='although there appeared to be no benefit from combining the two.',
             note='although 引导让步状语从句；there appeared to be there be 变体；combining 动名词作介词宾语'),
    ])

A['P5S1'] = dict(
    zh='许多老年驾驶员不去看眼科医生或负担不起。',
    insight=False, note='',
    bold=['eye doctors', "can't afford to"],
    chunks=[
        dict(role='主语', text='Many older drivers',
             note=''),
        dict(role='谓语', text="don't see eye doctors or can't afford to.",
             note='两个并列谓语；afford to 后省略 see eye doctors'),
    ])

A['P5S2'] = dict(
    zh='初级保健提供者手头工作繁重，可能无法跟进那些因无法转头或记不住要去哪里而驾驶困难的患者，或者那些身高变矮却没有充分调整座椅设置以便轻松够到汽车踏板的患者。',
    insight=True, note='本句包含限制性定语从句修饰先行词、原因状语从句解释原因、宾语从句充当动词宾语，这些都是四六级和考研真题中高频出现的句式；三层嵌套结构虽然复杂，但正是长难句的典型代表，掌握后可迁移到大量真题阅读理解和翻译题目中',
    bold=['have their hands full', 'follow through with', 'have trouble driving'],
    chunks=[
        dict(role='主语', text='Primary care providers',
             note=''),
        dict(role='谓语', text='have their hands full and may not be able to follow through with patients',
             note="have one's hands full 忙得不可开交；follow through with 跟进、落实"),
        dict(role='定语从句', text="who have trouble driving because they can't turn their heads or remember where they are going—or have gotten shorter and haven't changed their seat settings sufficiently to reach car pedals easily.",
             note='who... 定语从句修饰 patients；because 引导原因状语从句；where they are going 宾语从句；to reach... 不定式作目的状语'),
    ])

A['P6S1'] = dict(
    zh='Dugan说，只要路上还有其他汽车，自动驾驶汽车就无法解决车祸问题。',
    insight=True, note='条件状语从句+主句的结构是考试中非常常见的句式，特别是"aslongas"引导的条件句在四六级和考研阅读中频繁出现。引述结构"said+人名"也是新闻和学术文本的典型标记。掌握这种句式后可以迁移到大量类似句子的理解。',
    bold=['As long as', 'self-driving cars', 'crashes'],
    chunks=[
        dict(role='状语从句', text='As long as there are other cars on the roads,',
             note='as long as 引导条件状语从句；there be 句型'),
        dict(role='主语', text='self-driving cars',
             note=''),
        dict(role='谓语', text="won't solve",
             note=''),
        dict(role='宾语', text='the problems of crashes,',
             note=''),
        dict(role='谓语', text='said',
             note='倒装引述分句'),
        dict(role='主语', text='Dugan.',
             note=''),
    ])

A['P6S2'] = dict(
    zh='她说，避免所有那些人类驾驶员造成的危险需要太多算法。',
    insight=False, note='',
    bold=['posed by', 'algorithms'],
    chunks=[
        dict(role='主语', text='Avoiding dangers posed by all those human drivers',
             note='动名词短语作主语；posed by... 过去分词短语作后置定语'),
        dict(role='谓语', text='would require',
             note=''),
        dict(role='宾语', text='too many algorithms,',
             note=''),
        dict(role='主语', text='she',
             note=''),
        dict(role='谓语', text='said.',
             note=''),
    ])

A['P6S3'] = dict(
    zh='但Dugan说，我们需要做更多工作来提高安全性。',
    insight=False, note='',
    bold=['improve safety'],
    chunks=[
        dict(role='连接词', text='But',
             note=''),
        dict(role='主语', text='we',
             note='宾语从句主语'),
        dict(role='谓语', text='need to do more to improve safety,',
             note='to improve... 不定式作目的状语'),
        dict(role='主语', text='said Dugan.',
             note='倒装引述分句'),
    ])

A['P6S4'] = dict(
    zh='"如果我们要活到100岁，我们需要90岁的人能够舒适驾驶的汽车。"',
    insight=False, note='',
    bold=['100-year lives', 'comfortably'],
    chunks=[
        dict(role='状语从句', text='"If we\'re going to have 100-year lives,',
             note='if 引导条件状语从句；be going to 打算、将要'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='need',
             note=''),
        dict(role='宾语', text='cars that a 90-year-old can drive comfortably."',
             note='that... 定语从句修饰 cars'),
    ])
