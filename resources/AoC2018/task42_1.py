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

def start_over(ip, data, reg0):
    reg = [reg0, 0, 0, 0, 0, 0]
    ind = 0
    commands = []
    pattern = []
    values = []
    count = 0
    while True:
        oper = data[ind][0]

        if oper == eqrr:
            if reg[1] not in values:
                values.append(reg[1])
                print(count, reg[1])
            else:
                return values[-1]
        oper(reg, data[ind][1], data[ind][2], data[ind][3])
        reg[ip] = reg[ip] + 1
        ind = reg[ip]
        count += 1


data=[[seti, 123, 0, 1],
      [bani, 1, 456, 1],
      [eqri, 1, 72, 1],
      [addr, 1, 4, 4],
      [seti, 0, 0, 4],
      [seti, 0, 6, 1],
      [bori, 1, 65536, 3],
      [seti, 6780005, 8, 1],
      [bani, 3, 255, 2],
      [addr, 1, 2, 1],
      [bani, 1, 16777215, 1],
      [muli, 1, 65899, 1],
      [bani, 1, 16777215, 1],
      [gtir, 256, 3, 2],
      [addr, 2, 4, 4],
      [addi, 4, 1, 4],
      [seti, 27, 5, 4],
      [seti, 0, 5, 2],
      [addi, 2, 1, 5],
      [muli, 5, 256, 5],
      [gtrr, 5, 3, 5],
      [addr, 5, 4, 4],
      [addi, 4, 1, 4],
      [seti, 25, 4, 4],
      [addi, 2, 1, 2],
      [seti, 17, 7, 4],
      [setr, 2, 1, 3],
      [seti, 7, 3, 4],
      [eqrr, 1, 0, 2],
      [addr, 2, 4, 4],
      [seti, 5, 4, 4]
      ]

reg0 = 1000
ip=4
try:
    start_over(ip, data, reg0)
except IndexError:
    print(reg0)

