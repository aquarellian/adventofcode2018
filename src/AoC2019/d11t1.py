BLACK = 0
WHITE = 1


def get_cur_color(_map, x, y):
    if _map.get(x) is None:
        _map[x] = {}
        _map[x][y] = BLACK
        return BLACK
    elif _map[x].get(y) is None:
        _map[x][y] = BLACK
        return BLACK
    else:
        return _map[x][y]

def print_map(_map):
    print(_map)
    minx = min(_map.keys())
    maxx = max(_map.keys())
    maxy = 0
    miny = 0
    for x in _map.keys():
        maxy = max(maxy, max(_map[x].keys()))
        miny = min(miny, min(_map[x].keys()))
    # dx = 0 - minx
    # dy = 0 - miny
    #
    # print(minx, maxx, dx)
    # print(miny, maxy, dy)
    for y in range(maxy, miny - 1, -1):
        s = ''
        for x in range(minx, maxx + 1):
            if _map.get(x) is None or _map[x].get(y) is None:
                s += ' '
            elif _map[x][y] == 0:
                s+= ' '
            elif _map[x][y] == 1:
                s += '#'
            else:
                s += str(_map[x][y])
        print(s)




import opcode
import load_input
content = load_input.load(2019, 11).split(',')
_map = {}
x = 0
y = 0
dir = '^'
_map[x] = {}
_map[x][y] = WHITE
amp = opcode.Amplifier(content)
# commands = [[1, 0], [0, 0], [1, 0], [1, 0], [0, 1], [1, 0], [1, 0]]
while not amp.halted:
# for command in commands:
    col = get_cur_color(_map, x, y)
    # print(x, y, col)

    cp_map = _map.copy()
    cp_map[x][y] = dir
    # print_map(cp_map)

    # print(col)
    res = amp.apply(col)
    # res = command
    if amp.halted:
        break
    newcol = res[0]
    newdir = res[1]
    # print(res)
    if newcol not in [0,1] or newdir not in [0,1]:
        print('ERROR dir=', newdir, ', color=', newcol)
    else:
        _map[x][y] = newcol
        if newdir == 0:
            # turn left
            if dir == '^':
                dir = '<'
                x = x - 1
            elif dir == '<':
                dir = 'V'
                y = y - 1
            elif dir == 'V':
                dir = '>'
                x = x + 1
            elif dir == '>':
                dir = '^'
                y = y + 1
        else:
            # turn right
            if dir == '^':
                dir = '>'
                x = x + 1
            elif dir == '>':
                dir = 'V'
                y = y - 1
            elif dir == 'V':
                dir = '<'
                x = x - 1
            elif dir == '<':
                dir = '^'
                y = y + 1
count = 0
for x in _map.keys():
    count += len(_map[x].keys())
print_map(_map)
# print(_map)
print(count)


