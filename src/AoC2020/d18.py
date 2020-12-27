def calc(s):
    s = addition(s)
    v = None
    oper = None
    for a in s.split(" "):
        if a == '+' or a == '*':
            oper = a
        elif v is None:
            v = int(a)
        else:
            if oper == '+':
                v += int(a)
            elif oper == '*':
                v *= int(a)
            else:
                print('unexpected')
    return v

def addition(s):
    while '+' in s:
        ind = s.index('+')
        first = int(s[:ind-1].split(' ')[-1])
        second = int(s[ind+2:].split(' ')[0])
        v = first + second
        first_i = s[:ind-1].rindex(str(first))
        last_i = ind + 2 + len(str(second))
        s = s[:first_i] + str(v) + s[last_i:]
    return s


def braces(s):
    while ")" in s:
        rind = s.index(")")
        ind = s[:rind].rindex("(")
        v = calc(s[ind + 1: rind])
        s = s[:ind] + str(v) + s[rind + 1:]
    return calc(s)


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d18.txt") as f:
    content = f.readlines()
    s = 0
    for line in content:
        s += braces(line)
    print(s)
