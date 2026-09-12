# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 1 —— P3 至 P4 的成分划分。口径见 t22_1_a.py 头注释。"""

A = {}

A['P3S1'] = dict(
    zh='"我对我们的进展感到兴奋，"为丹佛的 Nest Fresh Eggs 收获鸡蛋的 Brown 说，他正在增加更多吸引蚯蚓和蟋蟀供鸡食用的覆盖作物。',
    insight=True,
    note='直接引语+倒装主句+非限制性定语从句+限制性定语从句嵌套，是四六级和考研阅读中极为常见的复杂句式；关系代词 who/that 的用法、非限从的逗号分隔、从句嵌套层级都是高频考点，掌握后可大量复用。',
    bold=['excited about', 'harvests', 'cover crops', 'draw worms and crickets'],
    chunks=[
        dict(role='主语', text='"I\'m excited about our progress,"', note='直接引语整体含主语 I 与谓语 am excited'),
        dict(role='谓语', text='says', note='引述动词'),
        dict(role='主语', text='Brown', note='引述主语'),
        dict(role='定语从句', text='who harvests eggs for Denver-based Nest Fresh Eggs and is adding more cover crops that draw worms and crickets for the chickens to eat',
             note='非限制性定语从句修饰 Brown；其中 that draw... 为限制性定语从句修饰 cover crops'),
    ])

A['P3S2'] = dict(
    zh='然后，鸡的粪便为田地施肥。',
    insight=False, note='',
    bold=['waste', 'fertilizes'],
    chunks=[
        dict(role='主语', text="The birds' waste"),
        dict(role='状语', text='then'),
        dict(role='谓语', text='fertilizes'),
        dict(role='宾语', text='fields'),
    ])

A['P3S3'] = dict(
    zh='这些改进"让我们的母鸡能觅食更高质量的天然饲料，这对土地、母鸡以及我们供应给客户的鸡蛋都有好处。"',
    insight=True,
    note='使役动词 allow + 宾语 + 不定式补足语，以及双层限制性定语从句嵌套，均为四六级和考研阅读中的高频句式。该句型既体现了复杂修饰关系，又保持了主干清晰，是真题长难句的典型代表。掌握此结构后可迁移到大量同类句子的分析，实用性强。',
    bold=['allow', 'forage', 'higher-quality', 'supply to'],
    chunks=[
        dict(role='主语', text='Such improvements'),
        dict(role='谓语', text='"allow'),
        dict(role='宾语', text='our hens'),
        dict(role='宾语补足语', text='to forage for higher-quality natural feed that will be good for the land, the hens, and the eggs that we supply to our customers."',
             note='不定式短语作宾语补足语；that will be good... 修饰 feed，其中又嵌套 that we supply... 修饰 eggs'),
    ])

A['P4S1'] = dict(
    zh='鸡蛋行业的推动，是对来自再生农场的动物产品能否成为下一个高端产品的一次重大考验。',
    insight=True,
    note='主句采用主系表结构，表语后接介词加从句的形式，这是四六级和考研阅读中常见的句式；宾语从句由"whether"引导表示疑问内容，也是典型的名词性从句用法；整体结构具有较高的代表性和迁移价值。',
    bold=['push', 'premium offering'],
    chunks=[
        dict(role='主语', text="The egg industry's push"),
        dict(role='谓语', text='is'),
        dict(role='表语', text='the first major test of whether animal products from regenerative farms can become the next premium offering',
             note='of whether... 介词短语作后置定语；whether 引导宾语从句作 of 的宾语'),
    ])

A['P4S2'] = dict(
    zh='在短短十多年里，有机鸡蛋从被视为天然食品商店里的小众产品，发展到了在沃尔玛销售。',
    insight=False, note='',
    bold=['barely', 'niche product', 'natural foods stores'],
    chunks=[
        dict(role='状语', text='In barely more than a decade'),
        dict(role='主语', text='organic eggs'),
        dict(role='谓语', text='went'),
        dict(role='状语', text='from being dismissed as a niche product in natural foods stores to being sold at Walmart',
             note='go from...to... 结构；being dismissed / being sold 为动名词被动式'),
    ])

A['P4S3'] = dict(
    zh='最近，关于益生菌和植物基肉类也曾有过类似的质疑，但两者都已爆发式增长，成为超市的主要品类。',
    insight=False, note='',
    bold=['probiotics', 'plant-based', 'exploded into'],
    chunks=[
        dict(role='状语', text='More recently'),
        dict(role='形式主语', text='there'),
        dict(role='谓语', text='were'),
        dict(role='主语', text='similar doubts about probiotics and plant-based meats'),
        dict(role='连接词', text='but'),
        dict(role='主语', text='both'),
        dict(role='谓语', text='have exploded into'),
        dict(role='宾语', text='major supermarket categories'),
    ])

A['P4S4'] = dict(
    zh='如果可持续鸡蛋的推广取得成功，它可能为再生牛肉、西兰花及更多产品打开闸门。',
    insight=False, note='',
    bold=['rollout', 'open the floodgates'],
    chunks=[
        dict(role='状语从句', text='If the sustainable-egg rollout is successful',
             note='条件状语从句'),
        dict(role='主语', text='it'),
        dict(role='谓语', text='could open'),
        dict(role='宾语', text='the floodgates'),
        dict(role='状语', text='for regenerative beef, broccoli, and beyond'),
    ])
