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


def sublist(lst1, lst2):
    ls1 = [element for element in lst1 if element in lst2]
    ls2 = [element for element in lst2 if element in lst1]
    return ls1 == ls2

def start_over(ip, data, reg0):
    reg = [reg0,0,0,0,0,0]
    ind = 0
    commands = []
    pattern = []
    while True:
        if [ind] + reg  in commands:
            if ind in pattern:
                if sublist(pattern, commands):
                    return
            else:
                pattern.append([ind] + reg)
        else:
            commands.append(ind)

        oper = data[ind][0]
        oper(reg, data[ind][1], data[ind][2], data[ind][3])
        reg[ip]=reg[ip]+1
        ind = reg[ip]
        print(data[ind], ' res ', reg)
    # print('found pattern: ', pattern)
    # start_over(ip, data, reg0 + 1)

with open("../resources/task41.txt") as f:
    content = f.readlines()
    ind = 0
    data = []
    ip = None
    import sys

    thismodule = sys.modules[__name__]

    for line in content:
        if '#ip 'in line:
            ip = int(substr_between(line, '#ip ', None).strip())
        else:
            cmd = substr_between(line, None, ' ')
            params = list(map(int,substr_between(line, ' ', None).strip().split()))

            data.append([getattr(thismodule, cmd)] + params)

    reg0 = 0
    try:
        while True:
            start_over(ip, data, reg0)
            reg0 += 1
    except IndexError:
        print(reg0)
