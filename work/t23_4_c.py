# -*- coding: utf-8 -*-
"""2023 Text 4 —— P6 至 P7 的成分划分。口径见 t23_4_a.py 头注释。"""
A = {}

A['P6S1'] = dict(
    zh='在这些看似矛盾的发展背后，是否存在某种共同因素？',
    insight=False, note='',
    bold=['common factor', 'underlies', 'contradictory'],
    chunks=[
        # 疑问式 there be：原文是 "Is there"，故顺序为 Is → there
        dict(role='谓语', text='Is', note='存在句的谓语'),
        dict(role='形式主语', text='there', note='there be 存在句'),
        dict(role='主语', text='some common factor'),
        dict(role='定语从句', text='that underlies these apparently contradictory developments',
             note='修饰 factor；underlie = 构成…的基础'),
    ])

A['P6S2'] = dict(
    zh='一种观点是，青少年的行为与研究人员所说的"奖赏敏感性"有关。',
    insight=False, note='',
    bold=['is related to', 'reward sensitivity'],
    chunks=[
        dict(role='主语', text='One idea'),
        dict(role='谓语', text='is'),
        dict(role='连接词', text='that', note='引导表语从句'),
        dict(role='主语', text='teenage behavior', note='表语从句的主语'),
        dict(role='谓语', text='is related'),
        dict(role='状语', text='to what researchers call "reward sensitivity."',
             note='what 引导的宾语从句作 to 的宾语'),
    ])

A['P6S3'] = dict(
    zh='做决定总是需要平衡奖赏与风险、收益与成本。',
    insight=False, note='',
    bold=['involves', 'balancing', 'benefits and costs'],
    chunks=[
        dict(role='主语', text='Decision-making', note='动名词作主语'),
        dict(role='状语', text='always'),
        dict(role='谓语', text='involves'),
        dict(role='宾语', text='balancing rewards and risks, benefits and costs',
             note='动名词短语作宾语；rewards and risks 与 benefits and costs 为并列结构'),
    ])

A['P6S4'] = dict(
    zh='"奖赏敏感性"衡量的是需要多大的奖赏才能超过风险。',
    insight=True,
    note='it takes ... to do 是固定句式（需要…才能做…），'
         '此处以 how much reward 提前构成宾语从句：'
         'measures how much reward it takes to outweigh risk。'
         '难点在于 it takes 的 it 是形式主语，真正的主语是后面的 to outweigh risk，'
         '而 how much reward 是 takes 的宾语。',
    bold=['measures', 'outweigh'],
    chunks=[
        dict(role='主语', text='"Reward sensitivity"'),
        dict(role='谓语', text='measures'),
        dict(role='连接词', text='how', note='引导宾语从句'),
        dict(role='宾语', text='much reward', note='从句中 takes 的宾语'),
        dict(role='形式主语', text='it', note='指代后文 to outweigh risk'),
        dict(role='谓语', text='takes', note='宾语从句的谓语'),
        dict(role='主语', text='to outweigh risk', note='真主语，不定式短语'),
    ])

A['P7S1'] = dict(
    zh='青少年对社会性奖赏尤其敏感——赢得比赛、给新朋友留下深刻印象、让那个男孩注意到你。',
    insight=True,
    note='破折号后是三个并列的动名词短语，作 social rewards 的同位语，'
         '具体解释哪些算「社会性奖赏」。'
         '识别同位语（而非状语或定语）是本句关键：它们与 rewards 是同一件事的不同说法。',
    bold=['particularly sensitive', 'social rewards', 'impressing'],
    chunks=[
        dict(role='主语', text='Teenagers'),
        dict(role='谓语', text='are'),
        dict(role='表语', text='particularly sensitive'),
        dict(role='状语', text='to social rewards'),
        dict(role='同位语', text='winning the game, impressing a new friend, getting that boy to notice you',
             note='三个动名词短语并列，解释 social rewards 的具体内容'),
    ])

A['P7S2'] = dict(
    zh='奖赏敏感性，如同亲社会行为和冒险行为一样，似乎在青春期上升，然后随着我们年龄增长而再次下降。',
    insight=False, note='',
    bold=['go up', 'risk-taking'],
    chunks=[
        dict(role='主语', text='Reward sensitivity'),
        dict(role='插入语', text='like prosocial behavior and risk-taking',
             note='插入的比较成分，主语与谓语被其隔开'),
        dict(role='谓语', text='seems'),
        dict(role='表语', text='to go up', note='不定式作表语'),
        dict(role='状语', text='in adolescence'),
        dict(role='连接词', text='and then'),
        dict(role='表语', text='down again', note='承前省略 to go'),
        dict(role='状语从句', text='as we age'),
    ])

A['P7S3'] = dict(
    zh='不知为何，当你到了 30 岁，在那个聚会上发生令人兴奋的新鲜事的可能性，'
       '似乎已经抵不过从沙发上爬起来的那点力气了。',
    insight=False, note='',
    bold=['Somehow', 'outweigh', 'the effort of'],
    chunks=[
        dict(role='状语', text='Somehow', note='评注性状语'),
        dict(role='状语从句', text='when you hit 30', note='时间状语从句'),
        dict(role='主语', text='the chance', note='主句主语'),
        dict(role='定语从句', text='that something exciting and new will happen at that party',
             note='修饰 chance；that 在从句中不作成分'),
        dict(role='谓语', text='just doesn' + "'" + 't seem'),
        dict(role='表语', text='to outweigh'),
        dict(role='宾语', text='the effort of getting up off the couch',
             note='outweigh = 比…更重要、超过'),
    ])
