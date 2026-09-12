# -*- coding: utf-8 -*-
"""2023 考研英语二 Text 3 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P4S1'] = dict(
    zh='心理学教授Benjamin Storm指出:"我们日益依赖互联网可能会带来一些代价，但我必须认为总体而言收益将超过这些代价。',
    insight=True, note='涵盖主谓宾、Therebe句型、宾语从句、后置定语、状语等多种成分,且包含引语后置、情态动词作谓语、begoingto结构等易错点。特别是最外层主句的宾语(整段引语)和引语内的宾语从句,层次分明,适合训练成分识别能力。',
    bold=['associated with', 'outweigh'],
    chunks=[
        dict(role='宾语', text='"There may be costs associated with our increased reliance on the Internet, but I\'d have to imagine that overall the benefits are going to outweigh those costs,"',
             note='直接引语作 observes 的宾语；there be 句型；associated with... 过去分词作后置定语；imagine that 宾语从句；be going to do'),
        dict(role='谓语', text='observes',
             note='引述动词'),
        dict(role='主语', text='psychology professor Benjamin Storm.',
             note=''),
    ])

A['P4S2'] = dict(
    zh='"记忆似乎确实在发生变化，但它是在向好的方向变化吗？',
    insight=False, note='',
    bold=['for the better'],
    chunks=[
        dict(role='主语', text='"It',
             note=''),
        dict(role='谓语', text='seems pretty clear that memory is changing,',
             note='it seems clear that 形式主语句型'),
        dict(role='连接词', text='but',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='主语', text='it',
             note=''),
        dict(role='状语', text='changing for the better?',
             note='for the better 向好的方向'),
    ])

A['P4S3'] = dict(
    zh='目前，我们还不知道。"',
    insight=False, note='',
    bold=['At this point'],
    chunks=[
        dict(role='状语', text='At this point,',
             note=''),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='don\'t know."',
             note=''),
    ])
