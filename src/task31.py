def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[c]


def bani(reg, a, b, c):
    reg[c] = reg[a] & c


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[c]


def bori(reg, a, b, c):
    reg[c] = reg[a] | c


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
    reg[c] = 1 if a == b else 0


def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


with open("../resources/task31.test.txt") as f:
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
    sample2oper = {}
    count = 0
    for entry in data:
        cmd = entry['command']
        before = entry['before']
        after = entry['after']

        if cmd[0] not in num2opers:
            num2opers[cmd[0]] = set()
        # possible_ops = []
        # # is arg 1 register?
        # aCanBeReg = (0<= cmd[1] <=3)
        # bCanBeReg = (0<= cmd[2] <=3)
        #
        # aMatches = before[1] == cmd[1]
        # bMatches = before[2] == cmd[2]
        #
        # aCanBeReg &= aMatches
        # bCanBeReg &= bMatches
        #
        # if aCanBeReg:
        #     possible_ops += raops
        #     if bCanBeReg:
        #         possible_ops += rbops
        #         possible_ops += rops
        # elif bCanBeReg:
        #     possible_ops += rbops


        print(entry)
        operCount = 0
        opers = set()

        for oper in operations:
            # res = [before[0], before[1], before[2], before[3]]
            oper(before, cmd[1], cmd[2], cmd[3])
            # if oper in rops:
            #     oper(res, before[1], before[2], cmd[3])
            # elif oper in raops:
            #     oper(res, before[1], cmd[2], cmd[3])
            # elif oper in rbops:
            #     oper(res, cmd[1], before[2], cmd[3])

            if before == after:
                num2opers[cmd[0]].add(oper)
                opers.add(oper)
                operCount+=1
        print(opers)
        if operCount>=3:
            count +=1
    print(count)

    #192 too low
    #13,14 wrong
    #648 wrong 637??656???

