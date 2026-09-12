# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S2'] = dict(
    zh='根据美国国家教育统计中心的数据，近80%的大学生最终至少换过一次专业。',
    insight=True, note='简单句中带有"endupdoing"这一高频短语动词结构，以及"Accordingto"引导的信息来源状语，都是四六级和考研阅读中常见的表达方式；数量主语"80percentof"的用法也较为典型；掌握本句结构后可迁移至大量类似表述，代表性较强。',
    bold=['end up changing', 'majors'],
    chunks=[
        dict(role='状语', text='According to the National Center for Education Statistics,',
             note=''),
        dict(role='主语', text='nearly 80 percent of college students',
             note=''),
        dict(role='谓语', text='end up changing',
             note=''),
        dict(role='宾语', text='their majors at least once.',
             note='end up doing 最终…；at least once 至少一次'),
    ])

A['P4S3'] = dict(
    zh='这并不令人惊讶，因为高中基础必修课程使学生对大学中等待他们的广阔学术可能性了解甚少。',
    insight=False, note='',
    bold=['mandatory', 'a poor understanding'],
    chunks=[
        dict(role='主语', text='This',
             note=''),
        dict(role='谓语', text="isn't",
             note=''),
        dict(role='表语', text='surprising,',
             note=''),
        dict(role='状语', text='considering the basic mandatory high school curriculum leaves students with a poor understanding of the vast academic possibilities that await them in college.',
             note='considering 现在分词作原因状语；leave sb. with 使…带有；that... 定语从句修饰 possibilities'),
    ])

A['P4S4'] = dict(
    zh='许多学生发现自己在大学申请中列出一个专业，但在上了大学课程后换到另一个专业。',
    insight=True, note='"find+宾语+doing"是四六级和考研阅读中的高频句型,并列宾语补足语结构也常见于描述对比或转折的语境,本句结构具有较强的代表性和迁移价值,掌握后可应用于大量同类句子。',
    bold=['listing one major', 'switching to another'],
    chunks=[
        dict(role='主语', text='Many students',
             note=''),
        dict(role='谓语', text='find',
             note=''),
        dict(role='宾语', text='themselves',
             note=''),
        dict(role='宾语补足语', text='listing one major on their college applications, but switching to another after taking college classes.',
             note='find sb. doing 宾补；两个并列现在分词（listing / switching）'),
    ])

A['P4S5'] = dict(
    zh='这不一定是坏事，但取决于学校，如果换专业太晚，补学分可能代价高昂。',
    insight=True, note='"but"连接的并列转折句和"itis+形容词+todo"句型都是四六级和考研阅读中的高频结构，尤其形式主语句型在学术文本中大量出现，掌握后迁移性强，具有较高典型性。',
    bold=['costly', 'credits'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text="'s not necessarily",
             note=''),
        dict(role='表语', text='a bad thing,',
             note=''),
        dict(role='连接词', text='but',
             note=''),
        dict(role='状语', text='depending on the school,',
             note='现在分词作条件状语'),
        dict(role='主语', text='it',
             note='形式主语'),
        dict(role='谓语', text='can be costly',
             note=''),
        dict(role='真正主语', text='to make up credits after switching too late in the game.',
             note='不定式作真正主语；make up credits 补学分'),
    ])

A['P4S6'] = dict(
    zh='例如在Boston College，如果你从其他院系转到护理学院，就必须额外完成一年学业。',
    insight=True, note='句子覆盖了主语、谓语、宾语、地点状语、插入语、条件状语从句等多种成分，且条件从句采用倒装形式，练习价值较高。特别是倒装条件从句的识别、虚拟语气的判断、情态动词结构的分析，都是容易出错且需要强化的知识点，适合作为综合练习句。',
    bold=['complete an extra year', 'nursing school'],
    chunks=[
        dict(role='状语', text='At Boston College,',
             note=''),
        dict(role='插入语', text='for example,',
             note=''),
        dict(role='主语', text='you',
             note=''),
        dict(role='谓语', text='would have to complete',
             note=''),
        dict(role='宾语', text='an extra year',
             note=''),
        dict(role='状语从句', text='were you to switch to the nursing school from another department.',
             note='倒装的条件状语从句（= if you were to switch...）；虚拟语气'),
    ])

A['P4S7'] = dict(
    zh='最初花一年间隔年来弄清楚这些事情，可以帮助防止压力并在以后节省金钱。',
    insight=True, note='本句涵盖动名词短语作主语、情态动词作谓语、宾语补足语（且为并列动词短语）、不定式短语作目的状语等多种成分，能够同时练习主语识别（区分动名词与进行时）、谓语定位（排除非谓语动词）、宾补与状语的区分，成分种类丰富且包含易错点（如help后接不带to的不定式），适合作为成分划分的综合练习。',
    bold=['figure things out', 'prevent stress'],
    chunks=[
        dict(role='主语', text='Taking a gap year to figure things out initially',
             note='动名词短语作主语；to figure... 不定式作目的状语'),
        dict(role='谓语', text='can help',
             note=''),
        dict(role='宾语补足语', text='prevent stress and save money later on.',
             note='help (to) do，两个并列省略 to 的不定式作宾补'),
    ])
