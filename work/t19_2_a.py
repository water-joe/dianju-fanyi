# -*- coding: utf-8 -*-
"""2019 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='森林为我们提供荫凉、宁静，以及应对气候变化斗争中较为艰巨的挑战之一。',
    insight=False, note='',
    bold=['shade', 'the fight against'],
    chunks=[
        dict(role='主语', text='Forests',
             note=''),
        dict(role='谓语', text='give',
             note=''),
        dict(role='间接宾语', text='us',
             note=''),
        dict(role='直接宾语', text='shade, quiet and one of the harder challenges in the fight against climate change.',
             note='give sb. sth. 双宾语'),
    ])

A['P1S2'] = dict(
    zh='尽管我们人类指望森林吸收我们产生的大量二氧化碳，但我们正在威胁它们这样做的能力。',
    insight=True, note='让步状语从句+主句的结构在考试阅读中高频出现，"countonsbtodosth"句型也是常考固定搭配。省略关系代词的定语从句是真题中反复出现的考点。本句的结构模式具有较强的代表性和可复用性，掌握后可应用于大量类似句子。',
    bold=['count on', 'soak up', 'carbon dioxide'],
    chunks=[
        dict(role='状语从句', text='Even as we humans count on forests to soak up a good share of the carbon dioxide we produce,',
             note='even as 引导时间状语从句；count on sb. to do 指望某人做；(that) we produce 省略关系词的定语从句'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='are threatening',
             note=''),
        dict(role='宾语', text='their ability to do so.',
             note='to do so 不定式作后置定语'),
    ])

A['P1S3'] = dict(
    zh='我们正在加速的气候变化有朝一日可能使我们面临排放多于吸收碳的森林。',
    insight=True, note='本句覆盖了主语（含定语从句修饰）、谓语（情态动词结构）、宾语、宾语补足语（介词短语）、时间状语、多个层级的定语从句、比较状语从句，以及承前省略的宾语。成分种类丰富，且定语从句的多层嵌套、宾语补足语的识别、比较结构中的省略都是学生容易混淆的点，训练价值较高。',
    bold=['hastening', 'emit', 'absorb'],
    chunks=[
        dict(role='主语', text='The climate change we are hastening',
             note='(that) we are hastening 省略关系词的定语从句'),
        dict(role='谓语', text='could one day leave',
             note=''),
        dict(role='宾语', text='us',
             note=''),
        dict(role='宾语补足语', text='with forests that emit more carbon than they absorb.',
             note='leave sb. with 使…带有；that... 定语从句修饰 forests；than they absorb 比较'),
    ])

A['P2S1'] = dict(
    zh='值得庆幸的是，有一个办法可以摆脱这个困境——但这涉及达成一种微妙的平衡。',
    insight=False, note='',
    bold=['a way out of', 'striking a subtle balance'],
    chunks=[
        dict(role='状语', text='Thankfully,',
             note=''),
        dict(role='谓语', text='there is',
             note=''),
        dict(role='主语', text='a way out of this trap –',
             note='there be 句型真正主语'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='谓语', text='involves striking a subtle balance.',
             note='strike a balance 取得平衡'),
    ])

A['P2S2'] = dict(
    zh='帮助森林在未来长期作为有价值的"碳汇"繁荣发展，可能需要降低它们现在吸收碳的能力。',
    insight=False, note='',
    bold=['flourish', 'carbon sinks'],
    chunks=[
        dict(role='主语', text='Helping forests flourish as valuable "carbon sinks" long into the future',
             note='动名词短语作主语；flourish 繁荣'),
        dict(role='谓语', text='may require',
             note=''),
        dict(role='宾语', text='reducing their capacity to absorb carbon now.',
             note='动名词作宾语；to absorb... 不定式作后置定语'),
    ])

A['P2S3'] = dict(
    zh='California正在引领这一努力，就像它在许多气候工作中所做的那样，正在摸索具体细节。',
    insight=True, note='非限制性定语从句插在主句中间,且用"as"引导进行类比说明,是四六级和考研阅读中常见的句式。掌握这种插入结构和"as"从句的用法,可以应用于大量类似长难句的理解。',
    bold=['leading the way', 'figuring out the details'],
    chunks=[
        dict(role='主语', text='California',
             note=''),
        dict(role='谓语', text='is leading the way,',
             note=''),
        dict(role='非限制性定语从句', text='as it does on so many climate efforts,',
             note='as 引导非限制性定语从句（插入）'),
        dict(role='状语', text='in figuring out the details.',
             note='in + 动名词表方面'),
    ])

A['P3S1'] = dict(
    zh='该州提出的森林碳计划旨在加倍努力疏伐部分森林中的幼树并清理灌木丛。',
    insight=False, note='',
    bold=['aims to double', 'thin out', 'brush'],
    chunks=[
        dict(role='主语', text="The state's proposed Forest Carbon Plan",
             note=''),
        dict(role='谓语', text='aims to double efforts',
             note=''),
        dict(role='状语', text='to thin out young trees and clear brush in parts of the forest.',
             note='两个并列不定式作后置定语；thin out 疏伐'),
    ])
