# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 2 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P3S3'] = dict(
    zh='还有一个知识差距需要解决——受访者中有40%不确定谁保留AI生成内容的所有权。',
    insight=True, note='结构具有高度典型性。破折号连接并列主句进行解释说明,存在句表达客观事实,定语从句修饰名词,宾语从句作介词宾语,都是四六级和考研真题中频繁出现的标准句式。掌握本句结构后可直接迁移到大量类似题目',
    bold=['knowledge gap', 'ownership'],
    chunks=[
        dict(role='谓语', text="There's also a knowledge gap",
             note=''),
        dict(role='定语从句', text='that needs to be addressed —',
             note=''),
        dict(role='主语', text='40% of individuals surveyed',
             note='surveyed 过去分词作后置定语'),
        dict(role='谓语', text='are unsure about who retains ownership over the content produced by AI.',
             note='unsure about 后接 who 引导的宾语从句；produced by AI 过去分词作后置定语'),
    ])

A['P3S4'] = dict(
    zh='通过灌输AI使用的最佳实践并制定随技术发展而演变的政策，企业可以积极改变AI格局。',
    insight=False, note='',
    bold=['instilling', 'evolve with', 'AI landscape'],
    chunks=[
        dict(role='状语', text='By instilling best practices in AI engagement and creating policies that evolve with the technology,',
             note='by + 两个并列动名词；that evolve... 定语从句修饰 policies'),
        dict(role='主语', text='businesses',
             note=''),
        dict(role='谓语', text='can positively shift the AI landscape.',
             note=''),
    ])

A['P4S1'] = dict(
    zh='鉴于AI简化我们职业生活、处理行政事务并提升工作体验的潜力，我们有责任谨慎使用它，使其在不损害我们隐私的情况下为我们提供支持。',
    insight=True, note='"Itis+表语+todo"的形式主语结构和"so(that)+从句"表示目的或结果是四六级和考研中的高频句式。with引导的伴随状语也较常见。整体结构具有较强的代表性，掌握后可应用于多种场景。',
    bold=["it's up to us", 'compromising our privacy'],
    chunks=[
        dict(role='状语', text="With AI's potential to simplify our professional lives, do the admin and enhance the work experience,",
             note='with 复合结构；to simplify..., (to) do... and (to) enhance... 并列不定式作 potential 的后置定语'),
        dict(role='表语', text="it's up to us to navigate its usage cautiously",
             note='it 形式主语；up to sb. 由某人负责；to navigate... 真正主语'),
        dict(role='状语从句', text='so it supports us without compromising our privacy.',
             note='so (that) 引导目的状语从句；without compromising 介词+动名词'),
    ])

A['P4S2'] = dict(
    zh='没有必要退避进步，只要我们具备确保AI保持友好的知识和工具。',
    insight=True, note='本句为典型的主从复合句结构，包含条件状语从句和宾语从句的嵌套，符合四六级和考研阅读中常见的论证句式；"aslongas"引导条件从句、"makesure"后接宾语从句、被动语态"beequippedwith"等均为高频结构，代表性强，学习后可大量复用。',
    bold=['back away from', 'as long as', 'equipped with'],
    chunks=[
        dict(role='主语', text="There's no need to back away from progress,",
             note=''),
        dict(role='状语从句', text="as long as we're equipped with the knowledge and tools to make sure AI remains a friend.",
             note='as long as 引导条件状语从句；be equipped with 装备有；make sure 后省略 that 的宾语从句'),
    ])

A['P4S3'] = dict(
    zh='而这正是挑战所在。',
    insight=False, note='',
    bold=['the challenge lies'],
    chunks=[
        dict(role='连接词', text='And',
             note=''),
        dict(role='主语', text='this',
             note=''),
        dict(role='谓语', text='is where the challenge lies.',
             note='where 引导表语从句'),
    ])

A['P4S4'] = dict(
    zh='市场上有如此多的产品，用巨额的广告和营销预算进行推广，很容易成为受害者。',
    insight=False, note='',
    bold=['advertising and marketing budgets', 'fall victim'],
    chunks=[
        dict(role='谓语', text='There are so many products out there,',
             note=''),
        dict(role='状语', text='being promoted with huge advertising and marketing budgets,',
             note='现在分词被动式作后置修饰'),
        dict(role='状语从句', text="that it's easy to fall victim.",
             note='so... that... 结果状语从句；it 形式主语'),
    ])

A['P4S5'] = dict(
    zh='但通过在我们的企业中建立数字责任文化，我们可以创造一个AI能够在不泄露秘密的情况下帮助我们的未来。',
    insight=False, note='',
    bold=['digital responsibility', 'spilling the beans'],
    chunks=[
        dict(role='状语', text='But by building a culture of digital responsibility within our businesses,',
             note='by + 动名词'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='can create',
             note=''),
        dict(role='宾语', text='a future where AI can help us without spilling the beans.',
             note='where 引导定语从句修饰 future；spill the beans 泄密（习语）'),
    ])
