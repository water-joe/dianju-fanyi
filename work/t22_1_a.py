# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 1 —— P1 至 P2 的逐句成分划分与重点词释义。
口径见 CLAUDE.md：嵌套成分合并为一块（子结构写进 note）；
引述分句各标各的主谓语，不整体收进「引述分句」块。"""

A = {}

A['P1S1'] = dict(
    zh='在最近一个阳光明媚的日子里，13000 只鸡在德州 Shiner 镇 Larry Brown 那片 40 英亩的多风土地上漫步。',
    insight=False, note='',
    bold=['On a recent sunny day', 'roam over', 'windswept'],
    chunks=[
        dict(role='状语', text='On a recent sunny day', note='时间状语'),
        dict(role='主语', text='13,000 chickens'),
        dict(role='谓语', text='roam over', note='不及物动词短语'),
        dict(role='宾语', text="Larry Brown's 40 windswept acres in Shiner, Texas",
             note='in Shiner, Texas 为地点介词短语作后置定语'),
    ])

A['P1S2'] = dict(
    zh='一些鸡在停放着的汽车阴影下休息。',
    insight=True,
    note='本句是「主语+不及物动词+地点状语」的基本句型，在真题和日常阅读中较为常见，具有一定代表性。同时，过去分词作前置定语（"a parked car"）也是高频考点。不过由于句子过于简短且无从句，缺乏更复杂的典型句式特征（如定语从句、状语从句等），典型性相对一般。',
    bold=['rest', 'in the shade of', 'parked'],
    chunks=[
        dict(role='主语', text='Some'),
        dict(role='谓语', text='rest'),
        dict(role='状语', text='in the shade of a parked car',
             note='地点状语；a parked car 中 parked 为过去分词作前置定语'),
    ])

A['P1S3'] = dict(
    zh='另一些鸡和牛一起喝水。',
    insight=False, note='',
    bold=['drink water', 'with the cows'],
    chunks=[
        dict(role='主语', text='Others'),
        dict(role='谓语', text='drink water'),
        dict(role='状语', text='with the cows', note='伴随状语'),
    ])

A['P1S4'] = dict(
    zh='这一切看似随意，但其实是经过设计的，是这个价值 61 亿美元的美国鸡蛋产业押注的下一个大趋势的一部分：气候友好型鸡蛋。',
    insight=False, note='',
    bold=['random', 'by design', 'bets', 'climate- friendly'],
    chunks=[
        dict(role='主语', text='This all'),
        dict(role='谓语', text='seems', note='系动词'),
        dict(role='表语', text='random'),
        dict(role='连接词', text='but'),
        dict(role='主语', text="it's", note='it is 缩略'),
        dict(role='状语', text='by design', note='介词短语作表语，意为"经过设计的"'),
        dict(role='同位语', text='part of what the $6.1 billion U.S. egg industry bets will be its next big thing: climate- friendly eggs',
             note='解释说明 design；内含 what 从句作 of 的宾语，该从句本身嵌套 bets 的宾语从句'),
    ])

A['P2S1'] = dict(
    zh='这些鸡蛋目前正在货架上首次亮相，售价高达每打 8 美元，它们仍然标有有机和动物友好的标签，但它们也来自生活在使用再生农业的农场上的鸡群——这种特殊技术能培育可捕获温室气体的肥沃土壤。这类鸡蛋可作为帮助对抗气候变化的产品来营销。',
    insight=False, note='',
    bold=['making their debut', 'labeled', 'regenerative agriculture', 'trap greenhouse gases'],
    chunks=[
        dict(role='主语', text='These eggs'),
        dict(role='定语从句', text='which are making their debut now on shelves for as much as $8 a dozen',
             note='非限制性定语从句，修饰 eggs'),
        dict(role='谓语', text='are still labeled', note='被动语态谓语'),
        dict(role='宾语', text='organic and animal-friendly',
             note='主语补足语（被动语态后保留原宾语补足语）'),
        dict(role='连接词', text='but'),
        dict(role='主语', text='they', note='回指 These eggs'),
        dict(role='谓语', text="'re also from", note='are also from 缩略'),
        dict(role='宾语', text='birds that live on farms using regenerative agriculture—special techniques to cultivate rich soils that can trap greenhouse gases',
             note='birds 后接 that 定语从句；using regenerative agriculture 为现在分词短语作后置定语修饰 farms；破折号后 special techniques... 解释说明 regenerative agriculture'),
    ])

A['P2S2'] = dict(
    zh='这类鸡蛋可以作为帮助对抗气候变化的产品来营销。',
    insight=False, note='',
    bold=['marketed as', 'fight climate change'],
    chunks=[
        dict(role='定语', text='Such eggs'),
        dict(role='谓语', text='could be marketed', note='被动语态，情态动词+be+过分'),
        dict(role='状语', text='as helping to fight climate change',
             note='as 介词短语作方式/身份状语，helping to... 为动名词短语'),
    ])
