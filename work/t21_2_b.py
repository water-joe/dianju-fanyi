# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 2 —— P4 至 P6 的成分划分。口径见 t21_2_a.py 头注释。"""

A = {}

A['P4S1'] = dict(
    zh='这些数字虽有许多保留，但依然严峻。',
    insight=False, note='',
    bold=['caveats', 'grave'],
    chunks=[
        dict(role='主语', text='There are many caveats to those figures',
             note='there be 存在句，caveats 为真正主语'),
        dict(role='连接词', text='but'),
        dict(role='主语', text='they'),
        dict(role='谓语', text='are still'),
        dict(role='表语', text='grave'),
    ])

A['P4S2'] = dict(
    zh='要更自给自足，英国需大幅减少动物性食品消费，并可能更集约化地耕作——意味着更少的绿地和更多的工厂式生产。',
    insight=True,
    note='本句涵盖主语、谓语、宾语、目的状语、结果状语等多种成分，宾语部分包含并列不定式（且第二个不定式省略"to"），破折号后现在分词短语作结果状语，成分种类丰富，且并列结构和状语识别是常见易错点，训练价值较高。',
    bold=['self- sufficient', 'drastically reduce', 'farm more intensively', 'factory-style'],
    chunks=[
        dict(role='状语', text='To become much more self- sufficient',
             note='不定式作目的状语，self- 与 sufficient 间有原提取空格'),
        dict(role='主语', text='the UK'),
        dict(role='谓语', text='would need'),
        dict(role='宾语', text='to drastically reduce its consumption of animal foods, and probably also farm more intensively—meaning fewer green fields and more factory-style production',
             note='并列不定式 to reduce... and (to) farm...；破折号后 meaning... 现在分词短语作结果状语'),
    ])

A['P5S1'] = dict(
    zh='但转向以植物为主的饮食也无济于事。',
    insight=False, note='',
    bold=['switching to', 'plant-based diet'],
    chunks=[
        dict(role='连接词', text='But'),
        dict(role='主语', text='switching to a mainly plant-based diet',
             note='动名词短语作主语'),
        dict(role='谓语', text="wouldn't help"),
    ])

A['P5S2'] = dict(
    zh='英国以畜牧业为主有个充分的理由：其大部分地形没有合适的土壤或气候来进行商业化作物种植。',
    insight=True,
    note='there be 句型、定语从句修饰抽象名词 reason、冒号引出同位语从句解释说明，这些都是四六级和考研阅读中的高频句式。被动语态在从句中的运用、不定式作后置定语也是典型考点，整体结构具有很强的代表性。',
    bold=['There is a good reason', 'dominated by', 'animal husbandry', 'on a commercial basis'],
    chunks=[
        dict(role='形式主语', text='There'),
        dict(role='谓语', text='is'),
        dict(role='主语', text='a good reason why the UK is dominated by animal husbandry',
             note='why 引导定语从句修饰 reason（抽象名词后定从）'),
        dict(role='同位语', text=': most of its terrain doesn\'t have the right soil or climate to grow crops on a commercial basis',
             note='冒号后解释 reason；to grow... 不定式作后置定语修饰 soil or climate'),
    ])

A['P5S3'] = dict(
    zh='仅 25% 的国土适合种作物，其中大部分已被耕地占据。',
    insight=True,
    note='非限制性定语从句补充说明主句内容、被动语态描述客观事实，这两种结构在四六级和考研阅读中高频出现；"介词+which"引导定语从句的形式是考试重点句式，学生掌握后可广泛迁移到同类句型的理解和翻译中。',
    bold=['suitable for', 'crop-growing', 'occupied', 'arable fields'],
    chunks=[
        dict(role='主语', text='Just 25 per cent of the country\'s land'),
        dict(role='谓语', text='is suitable'),
        dict(role='状语', text='for crop-growing'),
        dict(role='定语从句', text='most of which is already occupied by arable fields',
             note='介词 + which 非限制性定语从句，which 指代 land'),
    ])

A['P5S4'] = dict(
    zh='即使我们把所有适宜土地都改成果蔬田——这将牵涉占用所有自然保护区、把成千上万人迁离家园——我们也只能实现作物产量 30% 的增长。',
    insight=True,
    note='成分丰富且含多个训练价值点：主句的主谓宾、状语从句的主谓宾加方向状语、定语从句中关系代词作主语、并列动名词作宾语、多个后置定语。破折号插入的定语从句和状语从句前置都是常考易错点，适合反复练习划分。',
    bold=['Even if', 'converted', 'fruit and veg', 'nature reserves', 'boost'],
    chunks=[
        dict(role='状语从句', text='Even if we converted all the suitable land to fields of fruit and veg —which would involve taking out all the nature reserves and removing thousands of people from their homes—',
             note='even if 让步状语从句；破折号内 which 非限制性定语从句，内含 taking... and removing... 并列动名词'),
        dict(role='主语', text='we'),
        dict(role='谓语', text='would achieve'),
        dict(role='宾语', text='only a 30 per cent boost in crop production',
             note='in crop production 介词短语作后置定语'),
    ])

A['P6S1'] = dict(
    zh='目前英国消费的水果蔬菜仅 23% 为本土种植，因此即使采取最极端的措施，我们也只能满足 30% 的新鲜农产品需求。',
    insight=True,
    note='因果关系的并列句（"so"连接）是四六级和考研阅读中的高频句式，考生需熟练识别并列逻辑。第一句的主系表结构加长主语（百分比+of 短语+后置定语）也是常见模式，尤其在数据类文本中。第二句的情态动词表推测、状语插入主谓之间，也是典型用法。掌握本句结构后，考生可迁移至其他含数据陈述、因果推理的句子，实用性较高。',
    bold=['home-grown', 'extreme measures', 'fresh produce'],
    chunks=[
        dict(role='主语', text='Just 23 per cent of the fruit and vegetables consumed in the UK',
             note='consumed 过去分词作后置定语修饰 fruit and vegetables'),
        dict(role='谓语', text='are currently home-grown'),
        dict(role='连接词', text='so'),
        dict(role='状语', text='even with the most extreme measures'),
        dict(role='主语', text='we'),
        dict(role='谓语', text='could meet'),
        dict(role='宾语', text='only 30 per cent of our fresh produce needs',
             note='needs 此处为名词"需求"，非动词'),
    ])

A['P6S2'] = dict(
    zh='这还是在我们寻找空间去种谷物、糖料、种子和油料之前——这些作物提供了我们当前卡路里摄入的绝大部分。',
    insight=True,
    note='主句+时间状语从句+定语从句的三层嵌套结构，以及"provide sb with sth"双宾语搭配，都是四六级和考研阅读中高频出现的句式；掌握本句切分方法后可直接迁移到大量同类长难句。',
    bold=['look for the space', 'grains', 'provide us with', 'calorie intake'],
    chunks=[
        dict(role='主语', text='That'),
        dict(role='谓语', text='is'),
        dict(role='状语', text='before we look for the space to grow the grains, sugars, seeds and oils that provide us with the vast bulk of our current calorie intake',
             note='before 引导时间状语从句；to grow... 不定式作后置定语；that 定语从句修饰 grains...oils，provide us with 双宾语'),
    ])
