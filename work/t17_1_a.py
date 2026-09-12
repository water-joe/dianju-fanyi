# -*- coding: utf-8 -*-
"""2017 考研英语二 Text 1 —— 逐句成分划分与重点词释义。

口径（与用户确认过，见 CLAUDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
  3. 状语插在谓词中间时整体作一个谓语块（如 are now falling）
"""

A = {}

A['P1S1'] = dict(
    zh='每周六上午9点，超过5万名跑步者出发在当地公园跑5公里。',
    insight=True, note='句中包含主语、谓语、时间状语（两处）、目的状语，成分种类较丰富；时间状语的并列呈现、目的状语不定式的识别，对基础学习者有一定训练价值，但不涉及宾语、表语、定语从句等更多元的成分。',
    bold=['set off', 'more than', 'local park'],
    chunks=[
        dict(role='状语', text='Every Saturday morning',
             note='时间状语'),
        dict(role='状语', text='at 9 am',
             note='时间状语，与上一个是并列的两处时间'),
        dict(role='主语', text='more than 50,000 runners',
             note=''),
        dict(role='谓语', text='set off',
             note='固定搭配：出发、动身'),
        dict(role='状语', text='to run 5km around their local park',
             note='不定式作目的状语；其中 around their local park 为地点状语'),
    ])

A['P1S2'] = dict(
    zh='Parkrun 现象始于十几个朋友，如今已在英国催生了400场活动，国外还有更多。',
    insight=False, note='',
    bold=['phenomenon', 'inspired', 'a dozen'],
    chunks=[
        dict(role='主语', text='The Parkrun phenomenon',
             note=''),
        dict(role='谓语', text='began',
             note=''),
        dict(role='状语', text='with a dozen friends',
             note='介词短语作状语，说明起始规模'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='has inspired',
             note='现在完成时，与 began 并列'),
        dict(role='宾语', text='400 events in the UK and more abroad',
             note='in the UK 为介词短语作后置定语；more abroad 后省略了 events'),
    ])

A['P1S3'] = dict(
    zh='活动免费，由数千名志愿者提供服务。',
    insight=False, note='',
    bold=['staffed', 'volunteers'],
    chunks=[
        dict(role='主语', text='Events',
             note=''),
        dict(role='谓语', text='are',
             note=''),
        dict(role='表语', text='free',
             note=''),
        dict(role='定语', text='staffed by thousands of volunteers',
             note='过去分词短语作后置定语（兼补充说明），修饰 Events；by... 说明施动者'),
    ])

A['P1S4'] = dict(
    zh='跑步者从4岁儿童到祖父母辈不等；他们的成绩从 Andrew Baddeley 创造的13分48秒世界纪录到1小时不等。',
    insight=False, note='',
    bold=['range from', 'world record'],
    chunks=[
        dict(role='主语', text='Runners',
             note=''),
        dict(role='谓语', text='range',
             note=''),
        dict(role='状语', text='from four years old to grandparents',
             note='from...to... 表范围，作状语'),
        dict(role='主语', text='their times',
             note='分号后的第二个并列分句的主语'),
        dict(role='谓语', text='range',
             note=''),
        dict(role='状语', text="from Andrew Baddeley's world record 13 minutes 48 seconds up to an hour",
             note='from...up to... 表范围；world record 与具体成绩为同位关系'),
    ])

A['P2S1'] = dict(
    zh='Parkrun 在伦敦奥运会「遗产」失败的地方取得了成功。',
    insight=True, note='主句+状语从句的结构是四六级和考研真题中的常见句式，具有一定代表性。where 引导抽象状语从句的用法也时有出现，掌握后可迁移到类似句型。但本句结构相对简单，没有多层嵌套或复杂修饰，典型性中等。',
    bold=['is succeeding', 'legacy'],
    chunks=[
        dict(role='主语', text='Parkrun',
             note=''),
        dict(role='谓语', text='is succeeding',
             note='现在进行时表持续的成功'),
        dict(role='状语从句', text='where London\'s Olympic "legacy" is failing',
             note='where 引导状语从句，此处表对比：在……的方面／而……'),
    ])

A['P2S2'] = dict(
    zh='十年前的周一，第30届奥林匹克运动会宣布将在伦敦举办。',
    insight=False, note='',
    bold=['was announced', 'Olympiad'],
    chunks=[
        dict(role='状语', text='Ten years ago on Monday',
             note='时间状语'),
        dict(role='形式主语', text='it',
             note='形式主语，真正主语是后面的 that 从句'),
        dict(role='谓语', text='was announced',
             note='被动语态'),
        dict(role='主语从句', text='that the Games of the 30th Olympiad would be in London',
             note='that 引导主语从句；从句内部为主语 the Games of the 30th Olympiad + 谓语 would be + 表语 in London'),
    ])

A['P2S3'] = dict(
    zh='规划文件承诺，奥运会的伟大遗产将是撬动一个热爱运动的国家离开沙发。',
    insight=False, note='',
    bold=['pledged', 'lever', 'couches'],
    chunks=[
        dict(role='主语', text='Planning documents',
             note=''),
        dict(role='谓语', text='pledged',
             note='引述动词：承诺'),
        dict(role='连接词', text='that',
             note='引导宾语从句'),
        dict(role='主语', text='the great legacy of the Games',
             note='宾语从句的主语；of the Games 为介词短语作后置定语'),
        dict(role='谓语', text='would be',
             note=''),
        dict(role='表语', text='to lever a nation of sport lovers away from their couches',
             note='不定式作表语；lever...away from... 意为「把……撬离……」；of sport lovers 修饰 nation'),
    ])

A['P2S4'] = dict(
    zh='人口将更健康，产生更多赢家。',
    insight=False, note='',
    bold=['population', 'produce'],
    chunks=[
        dict(role='主语', text='The population',
             note=''),
        dict(role='谓语', text='would be',
             note=''),
        dict(role='表语', text='fitter, healthier',
             note='and 连接的两个并列表语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='谓语', text='produce',
             note=''),
        dict(role='宾语', text='more winners',
             note=''),
    ])

A['P2S5'] = dict(
    zh='但这并未发生。',
    insight=False, note='',
    bold=['happened'],
    chunks=[
        dict(role='主语', text='It',
             note='指代上文承诺的种种结果'),
        dict(role='谓语', text='has not happened',
             note='否定副词 not 插在助动词与实义动词之间，整体作为一个谓语块'),
    ])
