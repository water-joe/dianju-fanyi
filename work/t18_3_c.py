# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S7'] = dict(
    zh='这些服务的用户不是他们的客户。',
    insight=False, note='',
    bold=['customers'],
    chunks=[
        dict(role='主语', text='The users of their services',
             note=''),
        dict(role='谓语', text='are not',
             note=''),
        dict(role='表语', text='their customers.',
             note=''),
    ])

A['P3S8'] = dict(
    zh='客户应该是那些向他们购买广告的人——而Facebook和Google这两个虚拟巨头主导着数字广告，使所有其他媒体和娱乐公司处于劣势。',
    insight=False, note='',
    bold=['dominate', 'to the disadvantage of'],
    chunks=[
        dict(role='主语', text='That',
             note=''),
        dict(role='谓语', text='would be',
             note=''),
        dict(role='表语', text='the people who buy advertising from them –',
             note='who... 定语从句修饰 people'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='Facebook and Google, the two virtual giants,',
             note=''),
        dict(role='谓语', text='dominate',
             note=''),
        dict(role='宾语', text='digital advertising',
             note=''),
        dict(role='状语', text='to the disadvantage of all other media and entertainment companies.',
             note='to the disadvantage of 使…处于劣势'),
    ])

A['P4S1'] = dict(
    zh='他们销售的产品是数据，而我们这些用户为了数字巨头的利益将我们的生活转化为数据。',
    insight=False, note='',
    bold=['convert', 'for the benefit of'],
    chunks=[
        dict(role='主语', text="The product they're selling",
             note="(that) they're selling 省略关系词的定语从句"),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='data,',
             note=''),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='we, the users,',
             note=''),
        dict(role='谓语', text='convert',
             note=''),
        dict(role='宾语', text='our lives',
             note=''),
        dict(role='状语', text='to data for the benefit of the digital giants.',
             note='convert A to B；for the benefit of 为…的利益'),
    ])

A['P4S2'] = dict(
    zh='正如一些蚂蚁饲养蚜虫以获取它们进食时产生的蜜露，Google也饲养我们以获取我们数字生活产生的数据。',
    insight=True, note='涵盖主谓宾、目的状语、后置定语、定语从句(含关系代词省略和作宾语两种情况)、时间状语从句等多种成分;"Justas...so..."并列结构和三层嵌套关系是易错点;适合训练成分识别和修饰关系判断',
    bold=['farm the bugs', 'honeydew', 'yield'],
    chunks=[
        dict(role='状语从句', text='Just as some ants farm the bugs called aphids for the honeydew they produce when they feed,',
             note='just as 引导方式状语从句；called aphids 过去分词作后置定语；(that) they produce 省略关系词的定语从句；when they feed 时间状语从句'),
        dict(role='状语', text='so',
             note=''),
        dict(role='主语', text='Google',
             note=''),
        dict(role='谓语', text='farms',
             note=''),
        dict(role='宾语', text='us',
             note=''),
        dict(role='状语', text='for the data that our digital lives yield.',
             note='that... 定语从句修饰 data；yield 产生'),
    ])

A['P4S3'] = dict(
    zh='蚂蚁让捕食性昆虫远离蚜虫觅食的地方；Gmail让垃圾邮件发送者远离我们的收件箱。',
    insight=False, note='',
    bold=['predatory insects', 'spammers'],
    chunks=[
        dict(role='主语', text='Ants',
             note=''),
        dict(role='谓语', text='keep predatory insects away from',
             note=''),
        dict(role='宾语', text='where their aphids feed;',
             note='where 引导宾语从句作介词宾语'),
        dict(role='主语', text='Gmail',
             note=''),
        dict(role='谓语', text='keeps',
             note=''),
        dict(role='宾语', text='the spammers',
             note=''),
        dict(role='宾语补足语', text='out of our inboxes.',
             note='keep sb. out of 使…远离'),
    ])

A['P4S4'] = dict(
    zh='即使双方都受益，这感觉也不像是一种人性化或民主的关系。',
    insight=True, note='主句的"主+系动词+表语（介词短语）"结构较为常见，让步状语从句（"evenif"）也是四六级和考研阅读中的典型结构。但整体句式偏简单，缺少定语从句、名词性从句等更高频的复杂句式，代表性中等。',
    bold=['democratic relationship', 'even if'],
    chunks=[
        dict(role='主语', text='It',
             note=''),
        dict(role='谓语', text="doesn't feel like",
             note=''),
        dict(role='宾语', text='a human or democratic relationship,',
             note=''),
        dict(role='状语从句', text='even if both sides benefit.',
             note='even if 引导让步状语从句'),
    ])
