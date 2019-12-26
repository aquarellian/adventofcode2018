import opcode
import load_input
content = load_input.load(2019, 19).split(',')
amp = opcode.Amplifier(content)
_map = {}

colsum = 0
dx = 0
dy = 0
xmax = 970
ymax = 998
# for y in range(dy, ymax):
#     # if y < 50:
#     #     continue
#     _map[y] = {}
#     linesum = 0
#     for x in range(dx, xmax):
#         amp.apply(x)
#         res = amp.apply(y)
#         linesum += res
#         _map[y][x] = res
#         amp = opcode.Amplifier(content)
# sum = 0
# with open('test19.txt', 'w') as r:
#     for y in range(0, max(_map.keys())):
#         line = ''
#         if y not in _map.keys():
#             line += '0' * max(_map.keys())
#             continue
#         for x in range(0, max(_map[y].keys())):
#             if x not in _map[y].keys():
#                 line += '0'
#                 continue
#             sum +=  _map[y][x]
#             line += str(_map[y][x])
#         # print(line)
#         r.write(line + '\n')
# print(sum)
# l100 ='1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
# print(len(l100))
#      high 8710898
# 5710899 wrong
res = 8710899
sq = 100
l100 = '1'* sq
with open('test19.txt') as r:
    content = r.readlines()
    for y in range(len(content)-1, 0, -1):
        line = content[y]
        # print(line, y)
        # y = content.index(line)
        # line = content[y]
        if l100 in line:
            # print('100 -> ', y)
            _x = line.index(l100)
            if content[y - (sq-1)][_x] == '1' and content[y - (sq - 1)][_x + (sq-1)] == '1':
                val = 10000 * (_x + dx) + (y - (sq-1)) + dy
                ndest = val / 10000 + val % 10000
                dest = res / 10000 + res % 10000
                if ndest < dest:
                    res = val
                    print(val)
            else:
                while l100 in line[_x+1:]:
                    _x = _x + 1 + line[_x+1:].index(l100)
                    if content[y - (sq-1)][_x] == '1' and content[y - (sq-1)][_x + (sq-1)] == '1':
                        val = 10000 * (_x + dx) + (y - (sq-1)) + dy
                        ndest = val / 10000 + val % 10000
                        dest = res / 10000 + res % 10000
                        if ndest < dest:
                            res = val
                            print(val)
        # print(y)
print(res)

