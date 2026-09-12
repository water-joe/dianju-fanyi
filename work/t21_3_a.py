# -*- coding: utf-8 -*-
"""2021 考研英语二 Text 3 — 逐句成分划分与重点词释义。
口径（与用户确认过，见 CLAUDE.md / BUILD_GUIDE.md）：
  1. 嵌套成分合并为一块，子结构写进 note
  2. 引述分句各标各的主谓语，不整体收进一个「引述分句」块
"""

# key = 句子 id ; zh 取自 raw 段落 zh 按句切分；bold/chunk.text 必须是 en 的连续子串
A = {}

A['P1S1'] = dict(
    zh=u'当微软在2015年收购任务管理应用Wunderlist和移动日历应用Sunrise时，它选中了两家在硅谷引起相当大关注的新兴公司。',
    insight=False, note='',
    bold=['When', 'bought', 'attracting considerable buzz'],
    chunks=[
        dict(role='状语从句', text='When Microsoft bought task management app Wunderlist and mobile calendar Sunrise in 2015',
             note='When 引导的时间状语从句'),
        dict(role='主语', text='it'),
        dict(role='谓语', text='picked'),
        dict(role='宾语', text='two newcomers that were attracting considerable buzz in Silicon Valley',
             note='that were attracting... 为定语从句修饰 newcomers'),
    ])

A['P1S2'] = dict(
    zh=u'微软自己的Office在"生产力"软件市场占据主导地位，但这些初创公司代表着一波专为智能手机世界从零开始设计的新技术浪潮。',
    insight=False, note='',
    bold=['dominates', 'represented', 'designed from the ground up'],
    chunks=[
        dict(role='主语', text="Microsoft's own Office"),
        dict(role='谓语', text='dominates', note='一般现在时，表常态'),
        dict(role='宾语', text='the market for "productivity" software'),
        dict(role='连接词', text='but'),
        dict(role='主语', text='the start-ups'),
        dict(role='谓语', text='represented'),
        dict(role='宾语', text='a new wave of technology designed from the ground up for the smartphone world',
             note='designed from the ground up... 为过去分词短语作后置定语修饰 technology'),
    ])
