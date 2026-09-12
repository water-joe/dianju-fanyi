# -*- coding: utf-8 -*-
"""2022 考研英语二 Text 3 —— P1 至 P2 的逐句成分划分与重点词释义。
口径：嵌套成分合并为一块（子结构写进 note）；引述分句各标各的主谓语。"""

A = {}

A['P1S1'] = dict(
    zh='我们在个人生活和职业生涯中都遇到过它们。',
    insight=False, note='',
    bold=['encountered', 'personal', 'professional lives'],
    chunks=[
        dict(role='主语', text='We'),
        dict(role='谓语', text='have all encountered'),
        dict(role='宾语', text='them'),
        dict(role='状语', text='in both our personal and professional lives'),
    ])

A['P1S2'] = dict(
    zh='想想那些让你感到被欺骗或沮丧的会员资格或订阅服务，它们注册过程无缝顺畅，但后来却很难取消。',
    insight=False, note='',
    bold=['Think about', 'tricked', 'frustrated', 'seamless', 'sign-up process', 'cancel'],
    chunks=[
        dict(role='谓语', text='Think about', note='祈使句谓语'),
        dict(role='宾语', text='the times you felt tricked or frustrated by a membership or subscription that had a seamless sign-up process but was later difficult to cancel',
             note='the times 后接 that/省略关系代词的定语从句；其中 that 引导的从句修饰 membership or subscription'),
    ])

A['P1S3'] = dict(
    zh='本应简单透明的事情，可能被有意或无意地复杂化，从而损害消费者的选择权。',
    insight=False, note='',
    bold=['transparent', 'complicated', 'impair', 'consumer choice'],
    chunks=[
        dict(role='主语', text='Something that should be simple and transparent'),
        dict(role='谓语', text='can be complicated'),
        dict(role='状语', text='intentionally or unintentionally'),
        dict(role='状语', text='in ways that impair consumer choice',
             note='in ways 方式状语；that 引导定语从句修饰 ways'),
    ])

A['P1S4'] = dict(
    zh='这些就是暗黑模式的例子。',
    insight=False, note='',
    bold=['examples', 'dark patterns'],
    chunks=[
        dict(role='主语', text='These'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='examples of dark patterns'),
    ])

A['P2S1'] = dict(
    zh='2010 年由用户体验专家 Harry Brignull 首次提出，"暗黑模式"是一个概括性术语，指操纵用户界面以影响用户决策能力的做法。',
    insight=False, note='',
    bold=['First coined', 'catch-all term', 'manipulate', 'decision-making', 'users'],
    chunks=[
        dict(role='状语', text='First coined in 2010 by user experience expert Harry Brignull',
             note='过去分词短语作状语，相当于 After it was coined...'),
        dict(role='主语', text='"dark patterns"'),
        dict(role='谓语', text='is'),
        dict(role='表语', text='a catch-all term for practices that manipulate user interfaces to influence the decision-making ability of users',
             note='that 引导定语从句修饰 practices；to influence... 为不定式作目的状语'),
    ])

A['P2S2'] = dict(
    zh='Brignull 识别出 12 种常见的暗黑模式类型，从误导和隐藏成本到"蟑螂旅馆"——一种用户体验起初简单直观，但当用户试图退出时却变得困难的做法。',
    insight=True,
    note='非限制性定语从句补充说明特定名词，从句内部包含并列结构和状语从句嵌套，这种层层修饰的句式在四六级和考研阅读中极为常见，掌握后可直接迁移到大量真题长难句。',
    bold=['identifies', 'common dark patterns', 'ranging from', 'hidden costs', 'roach motel'],
    chunks=[
        dict(role='主语', text='Brignull'),
        dict(role='谓语', text='identifies'),
        dict(role='宾语', text='12 types of common dark patterns'),
        dict(role='定语', text='ranging from misdirection and hidden costs to "roach motel", where a user experience seems easy and intuitive at the start, but turns difficult when the user tries to get out',
             note='现在分词短语作后置定语；其中 where 引导非限制性定语从句修饰 roach motel，从句内含 but 并列与 when 时间状语从句'),
    ])
