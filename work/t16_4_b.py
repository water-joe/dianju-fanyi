# -*- coding: utf-8 -*-
"""2016 考研英语二 Text 4 —— 逐句成分划分（中段：P4–P6S2）。

口径见 BUILD_GUIDE.md / CLAUDE.md：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""
A = {}

A['P4S1'] = dict(
    zh='从职业到社区再到家庭，这些对比表明，在严重的大衰退之后，那些刚开始人生旅程的人正在确定优先事项和期望，这些将日益扩散到美国生活的几乎所有方面，从消费偏好到住房模式再到政治。',
    insight=True, note='本句结构高度典型:主句+that引导的宾语从句+嵌套的that引导的限制性定语从句,是四六级和考研阅读中的高频句式。suggest后接宾语从句、名词后接定语从句进一步说明,这种层层展开的论述方式在学术文本和新闻报道中极为常见。掌握本句结构后,可以直接迁移到大量类似句式的理解和分析中,代表性很强。',
    bold=['suggest', 'in the aftermath of', 'searing', 'virtually'],
    chunks=[
        dict(role='状语', text='From career to community and family',
             note='介词短语作范围状语'),
        dict(role='主语', text='these contrasts',
             note=''),
        dict(role='谓语', text='suggest',
             note='引述/论证动词，后接宾语从句'),
        dict(role='连接词', text='that',
             note='引导宾语从句'),
        dict(role='状语', text='in the aftermath of the searing Great Recession',
             note='宾语从句中的时间状语；Great Recession 指 2008 年大衰退'),
        dict(role='主语', text='those just starting out in life',
             note='宾语从句的主语；just starting out in life 为现在分词短语作后置定语'),
        dict(role='谓语', text='are defining',
             note=''),
        dict(role='宾语', text='priorities and expectations that will increasingly spread through virtually all aspects of American life, from consumer preferences to housing patterns to politics',
             note='that 引导定语从句修饰 priorities and expectations；from consumer preferences to housing patterns to politics 列举说明 aspects'),
    ])

A['P5S1'] = dict(
    zh='年轻人和老年人在一个关键点上达成一致:两个群体中的压倒性多数都表示，他们认为今天的年轻人开始人生比早期几代人更加困难。',
    insight=True, note='这句结构层次丰富但不过分偏怪，时态也有清楚的对照关系，适合作为“结构+时态”综合训练材料。对想提升长句拆解能力的学习者来说，投入练习的回报很高。',
    bold=['converge on', 'Overwhelming majorities', 'get started in life', 'earlier generations'],
    chunks=[
        dict(role='主语', text='Young and old',
             note=''),
        dict(role='谓语', text='converge',
             note='converge on = 在…上达成一致'),
        dict(role='状语', text='on one key point',
             note='介词短语作状语'),
        dict(role='主语', text='Overwhelming majorities of both groups',
             note='冒号后为同位语从句，解释 one key point 的内容'),
        dict(role='谓语', text='said',
             note='引述动词'),
        dict(role='主语', text='they',
             note='believe 的主语'),
        dict(role='谓语', text='believe',
             note=''),
        dict(role='主语', text='it',
             note='形式主语，真正的主语是后面的不定式 for young people today to get started in life'),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='harder',
             note=''),
        dict(role='状语', text='for young people today to get started in life',
             note='不定式复合结构；for young people today 为 to get started 的逻辑主语'),
        dict(role='状语从句', text='than it was for earlier generations',
             note='than 引导比较状语从句，it 指代前面的不定式结构'),
    ])

A['P5S2'] = dict(
    zh='尽管年轻人对今天起步者的前景比他们的长辈稍微乐观一些，但两个群体中的绝大多数都认为那些"刚开始人生"的人在实现诸如获得一份薪酬优厚的工作、组建家庭、管理债务和找到负担得起的住房等标志性成就方面，比早期几代人面临更艰难的攀登。',
    insight=True, note='本句的结构非常典型："While"引导的让步状语从句+主句+省略"that"的宾语从句，这是四六级和考研阅读中常见的复合句模式。比较结构"tougher...than"和"such...as"列举也是高频考点。掌握本句的分析方法可以直接迁移到大量真题句子。',
    bold=['optimistic', 'tougher climb', 'signpost achievements', 'affordable housing'],
    chunks=[
        dict(role='状语从句', text='While younger people are somewhat more optimistic than their elders about the prospects for those starting out today',
             note='While 引导让步状语从句；比较结构 more optimistic than their elders；those starting out today 中 starting out 为现在分词短语作后置定语'),
        dict(role='主语', text='big majorities in both groups',
             note='主句主语'),
        dict(role='谓语', text='believe',
             note=''),
        dict(role='主语', text='those "just getting started in life"',
             note='宾语从句的主语（believe 后省略 that）；引号内为后置修饰'),
        dict(role='谓语', text='face',
             note=''),
        dict(role='宾语', text='a tougher climb than earlier generations in reaching such signpost achievements as securing a good-paying job, starting a family, managing debt, and finding affordable housing',
             note='than earlier generations 为比较对象；in reaching... 为方式/范围状语；such...as... 列举四项标志性成就'),
    ])

A['P6S1'] = dict(
    zh='PeteSchneider认为今天的攀登更加艰难。',
    insight=False, note='',
    bold=['considers', 'the climb', 'tougher'],
    chunks=[
        dict(role='主语', text='Pete Schneider',
             note=''),
        dict(role='谓语', text='considers',
             note=''),
        dict(role='宾语', text='the climb',
             note=''),
        dict(role='补语', text='tougher',
             note='宾语补足语，补充说明 the climb'),
        dict(role='状语', text='today',
             note=''),
    ])

A['P6S2'] = dict(
    zh='Schneider是来自芝加哥郊区的一名27岁汽车技师，他说自己大学毕业后很难找到工作。',
    insight=True, note='"主语(含同位语)+says+宾语从句"是新闻报道和学术写作中的高频句式,同位语补充人物背景信息也是典型用法。宾语从句省略that的现象在口语和书面语中都很常见。掌握这种结构后可以迁移到大量类似的引述句和报道句中,具有较强的代表性。',
    bold=['auto technician', 'struggled', 'graduating from college'],
    chunks=[
        dict(role='主语', text='Schneider',
             note=''),
        dict(role='同位语', text='a 27-year-old auto technician from the Chicago suburbs',
             note='补充说明 Schneider 的身份；from the Chicago suburbs 为介词短语作后置定语'),
        dict(role='谓语', text='says',
             note='引述动词'),
        dict(role='主语', text='he',
             note='宾语从句的主语（says 后省略 that）'),
        dict(role='谓语', text='struggled',
             note=''),
        dict(role='状语', text='to find a job',
             note='不定式作目的状语'),
        dict(role='状语', text='after graduating from college',
             note='介词短语作时间状语'),
    ])
