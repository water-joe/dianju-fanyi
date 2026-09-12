# -*- coding: utf-8 -*-
"""2018 考研英语二 Text 4 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P1S1'] = dict(
    zh='为了对抗将忙碌视为优点的陷阱，《深度工作:在分心世界中专注成功的法则》一书的作者Cal Newport建议培养"深度工作"的习惯——即不受干扰地专注的能力。',
    insight=True, note='本句成分较为丰富：包含主语、谓语、宾语、两处同位语（主语同位语和宾语内部同位语）、目的状语，覆盖了多种常见成分类型。特别是同位语的识别（通过逗号和破折号引出）和动名词宾语的判定（buildingahabit），都是学习者易混淆的考点，具有较高的训练价值',
    bold=['putting a premium on', 'recommends', 'without distraction'],
    chunks=[
        dict(role='状语', text='To combat the trap of putting a premium on being busy,',
             note='不定式作目的状语；put a premium on 重视'),
        dict(role='主语', text='Cal Newport,',
             note=''),
        dict(role='同位语', text='author of Deep Work: Rules for Focused Success in a Distracted World,',
             note=''),
        dict(role='谓语', text='recommends',
             note=''),
        dict(role='宾语', text='building a habit of "deep work" –',
             note=''),
        dict(role='同位语', text='the ability to focus without distraction.',
             note='对 deep work 的同位解释；to focus... 不定式作后置定语'),
    ])

A['P2S1'] = dict(
    zh='掌握深度工作艺术有多种方法——无论是专门用于特定任务的长时间静修、养成日常习惯，还是采取"新闻工作者式"的方法在一天中抓住深度工作的时刻。',
    insight=True, note='本句覆盖存现句主语识别、系动词谓语、同位语列举、介词短语后置定语、时间状语从句等多种成分。同位语部分包含三个并列的名词性结构，有动名词和名词短语的混合，适合练习并列成分的划分。状语从句中情态动词后的省略也是实用考点。成分种类丰富，训练价值较高。',
    bold=['a number of approaches', 'lengthy retreats', 'seizing moments'],
    chunks=[
        dict(role='谓语', text='There are',
             note=''),
        dict(role='主语', text='a number of approaches to mastering the art of deep work –',
             note='to mastering... 动名词作介词宾语'),
        dict(role='同位语', text='be it lengthy retreats dedicated to a specific task; developing a daily ritual; or taking a "journalistic" approach to seizing moments of deep work when you can throughout the day.',
             note='破折号后三个并列名词结构作同位举例；be it... 让步倒装（=whether it be...）；when you can 时间状语从句（省略 do it）'),
    ])

A['P2S2'] = dict(
    zh='无论采用哪种方法，关键是确定你的专注时长并坚持下去。',
    insight=True, note='句式具有一定典型性。让步状语从句(尤其是以"Whichever/Whatever/Whoever"引导并有所省略的形式)在考试阅读中时有出现,主句的"thekeyistodo..."也是常见的表达关键要点的句式。不定式作表语和并列不定式也是高频结构。虽然不是最复杂的典型难句,但作为中等难度的常见句式,有一定的学习迁移价值。',
    bold=['stick to it'],
    chunks=[
        dict(role='状语从句', text='Whichever approach,',
             note='whichever 引导让步状语从句（省略 it is）'),
        dict(role='主语', text='the key',
             note=''),
        dict(role='谓语', text='is',
             note=''),
        dict(role='表语', text='to determine your length of focus time and stick to it.',
             note='两个并列不定式作表语'),
    ])

A['P3S1'] = dict(
    zh='Newport还建议采用"深度日程安排"来对抗持续的干扰，在更短的时间内完成更多工作。',
    insight=True, note='主谓宾+不定式作目的状语是四六级和考研阅读中的常见句式，具有一定代表性。recommend作为常考词汇，其后接名词宾语+不定式状语的结构也较为典型。但本句过于简洁，缺少从句或复杂修饰成分，未能充分体现真题中常见的长难句特征，因此典型性中等。',
    bold=['deep scheduling', 'interruptions', 'get more done'],
    chunks=[
        dict(role='主语', text='Newport',
             note=''),
        dict(role='状语', text='also',
             note=''),
        dict(role='谓语', text='recommends',
             note=''),
        dict(role='宾语', text='"deep scheduling"',
             note=''),
        dict(role='状语', text='to combat constant interruptions and get more done in less time.',
             note='两个并列不定式作目的状语'),
    ])

A['P3S2'] = dict(
    zh='"在任何给定时刻，我都应该为未来大约一个月安排好深度工作。',
    insight=True, note='句中的结构非常典型：情态动词should+have、一般现在时表达习惯、比较状语从句like、条件状语once、以及引述动词writes的用法，都是四六级和考研真题中的常见句式。尤其是比较状语从句中的省略结构和条件状语的前置，都是高频考点。掌握本句的结构分析方法，可以直接迁移到大量类似句子中。',
    bold=['At any given point', 'scheduled'],
    chunks=[
        dict(role='状语', text='"At any given point,',
             note=''),
        dict(role='主语', text='I',
             note=''),
        dict(role='谓语', text='should have deep work scheduled',
             note=''),
        dict(role='状语', text='for roughly the next month.',
             note='have sth. done 使…被完成（scheduled 过去分词作宾补）'),
    ])

A['P3S3'] = dict(
    zh='"一旦列入日程，我就会像对待医生预约或重要会议一样保护这段时间"，他写道。',
    insight=False, note='',
    bold=['Once on the calendar', 'protect this time'],
    chunks=[
        dict(role='状语从句', text='Once on the calendar,',
             note='once 引导时间状语从句（省略 it is）'),
        dict(role='主语', text='I',
             note=''),
        dict(role='谓语', text='protect this time',
             note=''),
        dict(role='状语从句', text='like I would a doctor\'s appointment or important meeting",',
             note='like 引导比较状语从句（would 后省略 protect）'),
        dict(role='主语', text='he',
             note=''),
        dict(role='谓语', text='writes.',
             note=''),
    ])
