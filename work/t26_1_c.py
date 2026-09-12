# -*- coding: utf-8 -*-
"""2026 考研英语二 Text 1 — 逐句成分划分（repr 转义生成）。"""
A = {}

A['P6S1'] = dict(
    zh='自2010年以来关闭的图书馆数量存在争议。',
    insight=False, note='',
    bold=['disputed'],
    chunks=[
        dict(role='主语', text='The number of libraries that have closed since 2010',
             note='that have closed... 定语从句修饰 libraries'),
        dict(role='谓语', text='is disputed.',
             note='被动'),
    ])

A['P6S2'] = dict(
    zh='英国特许公共财政与会计协会的年度调查显示全英国有近800家；艺术委员会保存的官方统计数据记录英格兰有230家。',
    insight=True, note='分号连接两个并列主句的结构在四六级和考研阅读中较为常见,是典型的并列复合句式。两个分句内部都有介词短语或分词短语作定语修饰主语,也是真题中常见的修饰模式。掌握这种句式后,可以迁移到大量类似结构的句子。',
    bold=['annual survey', 'official statistics'],
    chunks=[
        dict(role='主语', text='An annual survey by the Chartered Institute of Public Finance and Accountancy',
             note=''),
        dict(role='谓语', text='puts it at nearly 800 across the UK;',
             note='put... at 估计为…；it 指关闭数量'),
        dict(role='主语', text='official statistics held by the Arts Council',
             note=''),
        dict(role='谓语', text='record',
             note=''),
        dict(role='宾语', text='230 in England.',
             note=''),
    ])

A['P6S3'] = dict(
    zh='当然，这230家图书馆已经太多了。',
    insight=True, note='覆盖主语、谓语、表语三个核心成分，表语为数量短语加程度修饰结构略有训练价值，但成分单一，无定语从句、状语从句等复杂修饰，整体练习收益有限',
    bold=['of course', 'too many'],
    chunks=[
        dict(role='插入语', text='It is, of course, 230 libraries too many.',
             note='too many 后置修饰，意为「多出 230 家、太多了」'),
    ])

A['P6S4'] = dict(
    zh='因此，如果我们要为子孙后代保护图书馆，就必须提高人们对图书馆及其工作的认识。',
    insight=True, note='"if条件从句+主句（情态动词must）"是四六级和考研真题中高频句式，用于表达假设和必要性；定语从句省略关系代词也是常考结构；句式具有较强代表性，掌握后可大量复用',
    bold=['future generations', 'raise awareness of'],
    chunks=[
        dict(role='状语从句', text='So if we are to protect our libraries for future generations,',
             note='be to do 表计划/义务'),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='must raise awareness of them and the work they do.',
             note='the work (that) they do 省略关系词的定语从句'),
    ])

A['P7S1'] = dict(
    zh='该审查报告建议开展一项全国性的品牌宣传活动，以增强图书馆的实体存在感，重新推行一项计划使会员能够在全国任何图书馆使用其借书证，以及为儿童提供自动会员资格。',
    insight=True, note='本句采用"主语+谓语+并列宾语"结构，宾语部分通过并列连词连接多个名词短语，每个短语内部嵌套不定式或介词短语作修饰，这种结构在学术写作和正式文体中非常常见，是考试中高频出现的典型句式，掌握后可大量复用。',
    bold=['branding campaign', 'physical presence', 'automatic memberships'],
    chunks=[
        dict(role='主语', text='The review',
             note=''),
        dict(role='谓语', text='recommends',
             note=''),
        dict(role='宾语', text='a national branding campaign to give libraries a stronger physical presence,',
             note='不定式作后置定语'),
        dict(role='宾语', text='the reintroduction of a scheme to enable members to use their card in any library in the country,',
             note='to enable sb. to do 不定式作后置定语'),
        dict(role='连接词', text='and',
             note=''),
        dict(role='宾语', text='automatic memberships for children.',
             note='三个并列宾语'),
    ])

A['P7S2'] = dict(
    zh='如果我们不使用它们，最终就会失去它们。',
    insight=False, note='',
    bold=['end up losing'],
    chunks=[
        dict(role='状语从句', text="If we don't use them,",
             note=''),
        dict(role='主语', text='we',
             note=''),
        dict(role='谓语', text='will end up losing them.',
             note='end up doing 以…告终'),
    ])

A['P7S3'] = dict(
    zh='对于那些有一段时间没去过图书馆的人来说，他们可能会对所发现的情况感到惊讶。',
    insight=False, note='',
    bold=['for some time'],
    chunks=[
        dict(role='状语', text="And for those who haven't been to a library for some time,",
             note='who... 定语从句修饰 those'),
        dict(role='主语', text='they',
             note=''),
        dict(role='谓语', text='may be surprised by what they find.',
             note='what they find 宾语从句作介词宾语'),
    ])
