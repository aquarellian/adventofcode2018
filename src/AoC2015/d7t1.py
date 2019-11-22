import load_input
content = load_input.load(2015, 7)

# content = [
#     '123 -> x',
#     '456 -> y',
#     'x AND y -> d',
#     'x OR y -> e',
#     'x LSHIFT 2 -> f',
#     'y RSHIFT 2 -> g',
#     'NOT x -> h',
#     'NOT y -> i'
# ]

import re
def get_param(res, s):
    return int(s) if re.compile(r'^[-+]?([1-9]\d*|0)$').match(s) else get_signal(res, s)


def get_signal(res, dest):
    if ' ' not in res[dest]:
        return get_param(res, res[dest])
    else:
        s = res[dest].split(' ')
        if len(s) == 2:
            a = int(get_param(res, s[1]))
            res[dest] = str(0b1111111111111111 - a)
            return res[dest]
        elif len(s) == 3:
            a = int(get_param(res, s[0]))
            b = int(get_param(res, s[2]))
            if s[1] == 'AND':
                res[dest] = str(a & b)
            elif s[1] == 'OR':
                res[dest] = str(a | b)
            elif s[1] == 'RSHIFT':
                res[dest] = str(a >> b)
            elif s[1] == 'LSHIFT':
                res[dest] = str(a << b)
            return res[dest]
        else:
            print('Parsing Error')

res = {}
for line in content.split('\n'):
    if '->' in line:
        s = line.split('->')
        dest = s[1].strip()
        res[dest] = s[0].strip()

print(get_signal(res, 'a'))
# print(get_signal(res, 'x'))
# print(get_signal(res, 'y'))
# print(get_signal(res, 'd'))
# print(get_signal(res, 'e'))
# print(get_signal(res, 'f'))
# print(get_signal(res, 'g'))
# print(get_signal(res, 'h'))
# print(get_signal(res, 'i'))
#



