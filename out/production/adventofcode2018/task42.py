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


def emulate_elf(ip, reg0):
    reg = [reg0, 0, 0, 0, 0, 0]
    values = []
    count = 0
    oper = reg[ip]
    while True:
        if count == 1846:
            print(count, reg[1])
        if reg[ip] == 0:
            # seti 123 0 1
            reg[1] = 123
        elif reg[ip] == 1:
            # bani 1 456 1
            reg[1] &= 456
        elif reg[ip] == 2:
            # eqri 1 72 1
            reg[1] = (1 if reg[1] == 72 else 0)
        elif reg[ip] == 3:
            # addr 1 4 4
            reg[4] = reg[1] + reg[4]
        elif reg[ip] == 4:
            # seti 0 0 4
            reg[4] = 0
        elif reg[ip] == 5:
            # seti 0 6 1
            reg[1] = 0
        elif reg[ip] == 6:
            # bori 1 65536 3
            reg[3] = reg[1] | 65536
        elif reg[ip] == 7:
            # seti 6780005 8 1
            reg[1] = 6780005
        elif reg[ip] == 8:
            # bani 3 255 2
            reg[2] = reg[3] & 255
        elif reg[ip] == 9:
            # addr 1 2 1
            reg[1] = reg[1] + reg[2]
        elif reg[ip] == 10 or reg[ip] == 12:
            # bani 1 16777215 1
            reg[1] = reg[1] & 16777215
        elif reg[ip] == 11:
            # muli 1 65899 1
            reg[1] *= 65899
        # elif reg[ip] == 12:
        #     # bani 1 16777215 1
        #     reg[1] &= 16777215
        elif reg[ip] == 13:
            # gtir 256 3 2
            reg[2] = (1 if 256 > reg[3] else 0)
        elif reg[ip] == 14:
            # addr 2 4 4
            reg[4] += reg[2]
        elif reg[ip] == 15:
            # addi 4 1 4
            reg[4] += 1
        elif reg[ip] == 16:
            # seti 27 5 4
            reg[4] = 27
        elif reg[ip] == 17:
            # seti 0 5 2
            reg[2] = 0
        elif reg[ip] == 18:
            # addi 2 1 5
            reg[5] = reg[2] + 1
        elif reg[ip] == 19:
            # muli 5 256 5
            reg[5] &= 256
        elif reg[ip] == 20:
            # gtrr 5 3 5
            reg[5] = (1 if reg[5] > reg[3] else 0)
        elif reg[ip] == 21:
            # addr 5 4 4
            reg[4] = reg[5] + reg[4]
        elif reg[ip] == 22:
            # addi 4 1 4
            reg[4] += 1
        elif reg[ip] == 23:
            # seti 25 4 4
            reg[4] = 25
        elif reg[ip] == 24:
            # addi 2 1 2
            reg[2] += 1
        elif reg[ip] == 25:
            # seti 17 7 4
            reg[4] = 17
        elif reg[ip] == 26:
            # setr 2 1 3
            reg[3] = reg[2]
        elif reg[ip] == 27:
            # seti 7 3 4
            reg[4] = 7
        elif reg[ip] == 28:

            if reg[1] not in values:
                values.append(reg[1])
                print(count, reg[1])
            else:
                return values[-1]

            # eqrr 1 0 2
            reg[2] = (1 if reg[0] == reg[1] else 0)
        elif reg[ip] == 29:
            # addr 2 4 4
            reg[4] = reg[2] + reg[4]
        elif reg[ip] == 30:
            # seti 5 4 4
            reg[4] = 5

        reg[ip] += 1
        count += 1
        # print(oper, ' res ', reg)
        print(count)


        # if count == 30:
        #     break



def sublist(lst1, lst2):
    ls1 = [element for element in lst1 if element in lst2]
    ls2 = [element for element in lst2 if element in lst1]
    return ls1 == ls2


def start_over(ip, data, reg0):
    reg = [reg0, 0, 0, 0, 0, 0]
    ind = 0
    commands = []
    pattern = []
    values = []
    count = 0
    while True:
        # if ind  in commands:
        #     if ind in pattern:
        #         if sublist(pattern, commands):
        #             print('found pattern: ', pattern)
        #             return
        #
        #     else:
        #         pattern.append(ind)
        # else:
        #     commands.append(ind)

        oper = data[ind][0]

        if oper == eqrr:
            if reg[1] not in values:
                values.append(reg[1])
                print(count, reg[1])
            else:
                return values[-1]
        oper(reg, data[ind][1], data[ind][2], data[ind][3])
        reg[ip] = reg[ip] + 1
        print(data[ind], ' res ', reg)
        ind = reg[ip]
        count += 1
        if count == 60:
            break

    # start_over(ip, data, reg0 + 1)


with open("../resources/task41.txt") as f:
    content = f.readlines()
    ind = 0
    data = []
    ip = None
    import sys

    thismodule = sys.modules[__name__]

    for line in content:
        if '#ip ' in line:
            ip = int(substr_between(line, '#ip ', None).strip())
        else:
            cmd = substr_between(line, None, ' ')
            params = list(map(int, substr_between(line, ' ', None).strip().split()))

            data.append([getattr(thismodule, cmd)] + params)

    # reg0 = 2525738
    reg0 = 1000
    try:
        # while True:c
        start_over(ip, data, reg0)
        # emulate_elf(ip, reg0)
        reg0 += 1
    except IndexError:
        print(reg0)

        # 38424 too low
        # 10661894 too low
        # 2513594 too low
