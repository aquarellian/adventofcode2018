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
                # second part started
                break
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
            num2opers[cmd[0]] = []

        operCount = 0
        opers = set()

        for oper in operations:
            if oper not in oper2nums:
                oper2nums[oper] = []
            res = [before[0], before[1], before[2], before[3]]
            oper(res, cmd[1], cmd[2], cmd[3])

            if res == after:
                num2opers[cmd[0]].append(oper)
                oper2nums[oper].append(cmd[0])
                opers.add(oper)
                operCount+=1
        if operCount>=3:
            count +=1
    print(count)
    # part 2
    # print(num2opers)
    num2oper = {}
    opers = set()

    # from collections import Counter
    # for key, value in num2opers.items():
    # # print(key, max(value,key=value.count))
    #     op2count = Counter(value)
    #     print()



    # while len(num2opers) > 0:
    #     for key, value in num2opers.items():
    #         if value in operations:
    #             num2opers[key].remove(value)
    #         if len(value) == 1:
    #             print(value)
    #             num2oper[key] = value[0]
    #             opers.add(value[0])
    #             print(opers)


    for key, value in num2opers.items():

        from collections import Counter
        # print(key, max(value,key=value.count))
        op2count = Counter(value)
        print(key, Counter(value))
    for key, value in oper2nums.items():

        from collections import Counter
        # print(key, max(value,key=value.count))
        op2count = Counter(value)
        print(key, Counter(value))

    #192 too low
    #13,14 wrong
    #648 wrong 637??656 wrong???
    # 610 wrong
    # 594 wrong
    # 621 wrong
    #636
