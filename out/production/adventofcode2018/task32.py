def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(reg, a, b, c):
    reg[c] = reg[a] & b


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(reg, a, b, c):
    reg[c] = reg[a] | b


def setr(reg, a, b, c):
    reg[c] = reg[a]


def seti(reg, a, b, c):
    reg[c] = a


def gtir(reg, a, b, c):
    reg[c] = (1 if a > reg[b] else 0)


def gtri(reg, a, b, c):
    reg[c] = (1 if reg[a] > b else 0)


def gtrr(reg, a, b, c):
    reg[c] = (1 if reg[a] > reg[b] else 0)


def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


with open("../resources/task31.txt") as f:
    content = f.readlines()
    ind = 0
    data = []
    entry = {}
    prog = []

    for line in content:

        if "Before:" in line:
            strs = substr_between(line, '[', ']').split(',')
            entry['before'] = [int(strs[0]), int(strs[1]), int(strs[2]), int(strs[3])]
        elif "After: " in line:
            strs = substr_between(line, '[', ']').split(',')
            entry['after'] = [int(strs[0]), int(strs[1]), int(strs[2]), int(strs[3])]
            # if entry not in data:
            data.append(entry)
            entry = {}
        elif line[0].isdigit():
            if entry.get('before', None) is not None:
                strs = line.strip().split(' ')
                entry['command'] = [int(strs[0]), int(strs[1]), int(strs[2]), int(strs[3])]
            else:
                prog.append(map(int, line.split()))

    rops = [addr, mulr, banr, borr, setr, gtrr, eqrr]
    raops = [addi, muli, bani, bori, seti, gtri, eqri]
    rbops = [gtir, eqir]
    operations = rops + raops + rbops
    num2opers = {}
    oper2nums = {}
    sample2oper = {}
    count = 0
    for entry in data:
        cmd = entry['command']
        before = entry['before']
        after = entry['after']

        if cmd[0] not in num2opers:
            num2opers[cmd[0]] = set()

        operCount = 0

        for oper in operations:
            if oper not in oper2nums:
                oper2nums[oper] = set()
            res = [before[0], before[1], before[2], before[3]]
            oper(res, cmd[1], cmd[2], cmd[3])

            if res == after:
                num2opers[cmd[0]].add(oper)
                oper2nums[oper].add(cmd[0])

    # part 2

    res = {}
    while len(res) < 16:
        for n,o in res.items():
            if n in num2opers:
                del num2opers[n]
            if o in oper2nums:
                del oper2nums[o]
        for num, opers in num2opers.items():
            if len(opers) == 1:
                oper = list(opers)[0]
                res[num] = oper
            for o in res.values():
                if o in opers:
                    opers.remove(o)

        for oper, nums in oper2nums.items():
            if len(nums) == 1:
                num = list(nums)[0]
                res[num] = oper

            for n in res.keys():
                if n in nums:
                    nums.remove(n)
        # print(res)
    print(res)

    # print(prog)
    reg = [0,0,0,0]
    for line in prog:
        oper = line[0]
        a = line[1]
        b = line[2]
        c = line[3]
        res[oper](reg, a, b, c)

    print(reg)
    # 677 too high



