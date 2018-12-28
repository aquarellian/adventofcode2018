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


with open("../resources/task37.txt") as f:
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

    # TSK1
    # reg = [0,0,0,0,0,0]
    # ind = 0
    # try:
    #     while True:
    #         oper = data[ind][0]
    #         oper(reg, data[ind][1], data[ind][2], data[ind][3])
    #         reg[ip]=reg[ip]+1
    #         ind = reg[ip]
    # except IndexError:
    #     print(reg[0]) #2280


    reg = [1,0,0,0,0,0]
    ind = 0
    firstCycleByPassed = False
    secondCycleBypassed = False
    count = 0
    try:
        while True:
            oper = data[ind][0]
            oper(reg, data[ind][1], data[ind][2], data[ind][3])
            reg[ip]=reg[ip]+1
            print(data[ind], reg)
            ind = reg[ip]

            if reg[2]==9 and reg[3]==10551288 and not firstCycleByPassed:
                skipIter = 10551288 - reg[1]
                print('skipping ', skipIter, ' cycles')
                reg[1] = 10551288
                count += (skipIter*9)
                firstCycleByPassed = True
            elif reg[1] == 10551289 and reg[2] == 13 and reg[3] == 10551288 and firstCycleByPassed:
                skipIter = 10551289 - reg[4]
                print('skipping ', skipIter, ' cycles')
                reg[4] = 10551289
                count += skipIter
                secondCycleBypassed = True
            else:
                count +=1

    except IndexError:
        print(reg[0])
    # 10551289 too low


