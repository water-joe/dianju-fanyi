# -*- coding: utf-8 -*-
"""2025 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='国民健康服务体系(NHS)建立之初颇具远见：提供高质量、及时的医疗服务以满足其所服务人群的主要需求。',
    insight=False, note='',
    bold=['visionary', 'high-quality, timely care'],
    chunks=[
        dict(role='状语从句', text='When it was established,',
             note='when 引导时间状语从句（被动）'),
        dict(role='主语', text='the National Health Service (NHS)',
             note=''),
        dict(role='谓语', text='was',
             note=''),
        dict(role='表语', text='visionary:',
             note=''),
        dict(role='状语', text='offering high-quality, timely care to meet the dominant needs of the population it served.',
             note='现在分词短语作补充说明；to meet... 不定式作目的状语；(that/which) it served 省略关系词的定语从句'),
    ])

A['P1S2'] = dict(
    zh='近75年过去了，英国面临着截然不同的健康挑战，这一模式显然已经过时。',
    insight=True, note='本句时态不难，但结构上包含常见且高频的训练点，尤其适合练习主干定位、形式主语识别和背景状语剥离。对于结构训练来说，投入产出比较高。',
    bold=['out of date', 'Nearly 75 years on'],
    chunks=[
        dict(role='状语', text='Nearly 75 years on,',
             note='时间状语'),
        dict(role='状语', text='with the UK facing very different health challenges,',
             note='with 复合结构作背景状语'),
        dict(role='谓语', text='it is clear',
             note='it 形式主语；that 从句为真正主语'),
        dict(role='主语从句', text='that model is out of date.',
             note='that model 指上文 NHS 模式'),
    ])

A['P2S1'] = dict(
    zh='从预期寿命到癌症和婴儿死亡率，我们都落后于许多同类国家。',
    insight=False, note='',
    bold=['life expectancy', 'infant mortality', 'lagging behind'],
    chunks=[
        dict(role='状语', text='From life expectancy to cancer and infant mortality rates,',
             note='介词短语作范围状语'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='are lagging behind many of our peers.',
             note='现在进行时；lag behind 落后于'),
    ])

A['P2S2'] = dict(
    zh='超过680万人在候诊名单上，医疗服务对那些无力选择支付私人治疗费用的人来说越来越难以获得；提供医疗服务的成本也日益挤压其他公共服务的投资。',
    insight=False, note='',
    bold=['waitlists', 'inaccessible', 'squeezing out'],
    chunks=[
        dict(role='状语', text='With more than 6.8 million on waitlists,',
             note='with 复合结构'),
        dict(role='主语', text='healthcare',
             note=''),
        dict(role='谓语', text='is becoming increasingly inaccessible for those who cannot opt to pay for private treatment;',
             note='who... 定语从句修饰 those；opt to do 选择做'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='主语', text='the cost of providing healthcare',
             note=''),
        dict(role='谓语', text='is increasingly squeezing out investment in other public services.',
             note='squeeze out 挤占；现在进行时'),
    ])

A['P2S3'] = dict(
    zh='随着医疗需求持续增长，本已接近崩溃边缘的医疗队伍所面临的压力只会变得更加严峻。',
    insight=True, note='状语从句前置+主句+非限制性定语从句插入是四六级和考研阅读中的高频句式组合。这种结构在学术类文本和新闻报道中反复出现，掌握后可大量复用于同类长难句的解析。',
    bold=['breaking point', 'acute'],
    chunks=[
        dict(role='状语从句', text='As demand for healthcare continues to grow,',
             note='as 引导时间状语从句'),
        dict(role='主语', text='pressures on the workforce—which is already near breaking point—',
             note='破折号内为非限制性定语从句修饰 workforce'),
        dict(role='谓语', text='will only become more acute.',
             note='only 强调'),
    ])

A['P3S1'] = dict(
    zh='解决健康和护理危机的许多答案都已被反复讨论。',
    insight=False, note='',
    bold=['well rehearsed'],
    chunks=[
        dict(role='主语', text='Many of the answers to the crisis in health and care',
             note=''),
        dict(role='谓语', text='are well rehearsed.',
             note='被动；rehearsed 此处指「反复说过、老生常谈」'),
    ])
