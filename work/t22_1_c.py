# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 1 —— P5 至 P6 的成分划分。口径见 t22_1_a.py 头注释。"""

A = {}

A['P5S1'] = dict(
    zh='宾州州立大学 Brandywine 分校的农业经济学副教授 Julie Stanton 说，再生产品可能难以销售，因为这个概念很难快速定义。',
    insight=False, note='',
    bold=['hard sell', 'tough to define'],
    chunks=[
        dict(role='主语', text='Regenerative products'),
        dict(role='谓语', text='could be'),
        dict(role='表语', text='a hard sell'),
        dict(role='状语从句', text='because the concept is tough to define quickly',
             note='原因状语从句'),
        dict(role='谓语', text='says', note='引述动词，主语在后'),
        dict(role='主语', text='Julie Stanton, associate professor of agricultural economics at Pennsylvania State University Brandywine',
             note='引述主语；associate professor... 为同位语'),
    ])

A['P5S2'] = dict(
    zh='这种农业方式对食品本身的改善也极少，甚至没有（尽管一些生产商声称他们的鸡蛋含有更多蛋白质）。',
    insight=True,
    note='主句+让步状语从句（though）+从句内嵌套宾语从句是四六级和考研阅读中的常见结构。插入语、后置定语、省略 that 的宾语从句都是高频句式特征，学习后可广泛迁移到同类真题句。',
    bold=['minimal', 'improvement', 'though'],
    chunks=[
        dict(role='定语', text='Such farming'),
        dict(role='状语', text='also'),
        dict(role='谓语', text='brings'),
        dict(role='宾语', text='minimal, if any, improvement to the food products',
             note='minimal, if any, 为插入语；to the food products 为状语'),
        dict(role='状语从句', text='(though some producers say their eggs have more protein)',
             note='让步状语从句；say 后省略 that 的宾语从句'),
    ])

A['P6S1'] = dict(
    zh='该行业押注：那些愿意为自由放养、非转基因和牧场饲养等优质属性支付更多费用的消费者，将会接受可持续性。',
    insight=True,
    note='"主句+that 引导的宾语从句"以及"现在分词短语作后置定语"都是四六级和考研阅读中的高频句式，掌握后可以复用到大量类似句子的理解中，具有较强的代表性。',
    bold=['betting', 'premium attributes', 'free-range', 'embrace sustainability'],
    chunks=[
        dict(role='主语', text='The industry'),
        dict(role='谓语', text='is betting', note='现在进行时谓语'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='主语', text='the same consumers paying more for premium attributes such as free-range, non-GMO, and pasture-raised eggs',
             note='宾语从句主语；paying more... 为现在分词短语作后置定语修饰 consumers'),
        dict(role='谓语', text='will embrace'),
        dict(role='宾语', text='sustainability'),
    ])

A['P6S2'] = dict(
    zh='调查显示，年轻一代更关注气候变化，而植物基肉类的一些成功可以归因于购物者希望表达他们保护环境的愿望。',
    insight=False, note='',
    bold=['Surveys show', 'concerned about', 'chalked up to'],
    chunks=[
        dict(role='主语', text='Surveys'),
        dict(role='谓语', text='show', note='引述动词'),
        dict(role='连接词', text='that', note='引导宾语从句'),
        dict(role='主语', text='younger generations'),
        dict(role='谓语', text='are more concerned about', note='宾语从句谓语'),
        dict(role='宾语', text='climate change'),
        dict(role='连接词', text='and'),
        dict(role='主语', text='some of the success of plant-based meat'),
        dict(role='谓语', text='can be chalked up to'),
        dict(role='宾语', text='shoppers wanting to signal their desire to protect the environment',
             note='wanting to... 为现在分词短语作后置定语修饰 shoppers'),
    ])

A['P6S3'] = dict(
    zh='Egg Innovations 的总裁 John Brunnquell 说，年轻人"真的很关心地球"。',
    insight=False, note='',
    bold=['president'],
    chunks=[
        dict(role='主语', text='Young adults'),
        dict(role='谓语', text='"really care about the planet,"', note='引语谓语'),
        dict(role='谓语', text='says', note='引述动词'),
        dict(role='主语', text='John Brunnquell, president of Egg Innovations',
             note='引述主语；president of... 为同位语'),
    ])

A['P6S4'] = dict(
    zh='"他们正在彻底改变食物链，其影响甚至超出了我认为他们自己所理解的程度。"',
    insight=False, note='',
    bold=['altering', 'food chain', 'beyond'],
    chunks=[
        dict(role='主语', text='"They'),
        dict(role='谓语', text='are absolutely altering'),
        dict(role='宾语', text='the food chain'),
        dict(role='状语', text='beyond what I think even they understand what they\'re doing."',
             note='beyond 介词短语作状语；what... 引导宾语从句作 beyond 的宾语，其中嵌套 I think 的插入与 what they\'re doing 从句'),
    ])
