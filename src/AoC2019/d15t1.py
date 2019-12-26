import opcode
import load_input

# with open("../../resources/AoC2019/d15.txt") as f:
#     content = f.readlines()[0].split(',')


def update_map(x, y, _map, value):
    if y not in _map.keys():
        _map[y] = {}
    if x in _map[y].keys():
        print('warning: overwriting', x, y, _map[y][x], value)
    _map[y][x] = value


def percolate(x, y, v, _map, percolation, dots):
    if _map[y].get(x, '?') not in ['#', '?']:
        percolation[y][x] = min(percolation[y][x], v)
        if percolation[y][x] == v:
            dots.append([x,y])

def print_field(field, dx, dy, dir):
    for y in range(50, -51, -1):
        line = ''
        if y in field.keys():
            for x in range(-25, 26):
                if y ==dy and x == dx:
                    line += '^' if dir == 1 else '>' if dir == 4 else 'v' if dir ==2 else '<'
                else:
                    line += field[y].get(x, '?')
        else:
            if y == dy:
                line += '?'*dx + ('^' if dir == 1 else '>' if dir == 4 else 'v' if dir ==2 else '<')
            else:
                line + '?' * 10 #(max(field.keys()) - min(field.keys() + 1))
        print(line)


content = load_input.load(2019, 15).split(',')
amp = opcode.Amplifier(content)
res = None
dir = 1
_map = {}
x = 0
y = 0
_map[y] = {}
_map[y][x] = ' '

i = 10000
minx = 0
maxx = 0
miny = 0
maxy = 0
ax = 0
ay = 0
while i > 0:
    i-=1
    _x = x
    _y = y
    if res is None: #or res == 1:
        dir = dir
    elif res == 0:
        if dir == 1:
            dir = 4
        elif dir == 4:
            dir = 2
        elif dir == 2:
            dir = 3
        elif dir == 3:
            dir = 1
    elif res == 1:
        if dir == 1:
            dir = 3
        elif dir == 3:
            dir = 2
        elif dir == 2:
            dir = 4
        elif dir == 4:
            dir = 1
    if dir == 1:
        _y += 1
    elif dir == 4:
        _x += 1
    elif dir == 2:
        _y -= 1
    elif dir == 3:
        _x -=1
    res = amp.apply(dir)
    # print(_x, _y, dir, res)
    if res == 0:
        update_map(_x, _y, _map, '#')
    elif res == 2:
        update_map(_x, _y, _map, '&')
        x = _x
        y = _y
        ax = _x
        ay = _y
        #break
    else:
        update_map(_x, _y, _map, ' ')
        x = _x
        y = _y
    if _x > maxx:
        maxx = _x
    if _x < minx:
        minx = _x
    if _y < miny:
        miny = _y
    if _y > maxy:
        maxy = _y
    # print(_x,  _y)
    # print_field(_map, x, y, dir)

def print_perc(perc, _map):
    res = True
    fmax = 0
    for y in range(min(perc.keys()), max(perc.keys()) + 1):
        line = ''
        for x in range(min(perc[y].keys()), max(perc[y].keys()) + 1):
            if _map[y].get(x, '?') in ['#', '?']:
                line += ' # '
            elif perc[y][x] == 100000:
                line += ' ? '
                res = False
            else:
                line += str(perc [y][x])
                if perc [y][x] > fmax:
                    fmax= perc [y][x]
        print(line)
    print()
    return res, fmax

percolation = {}
for y in range(miny, maxy):
    percolation[y] = {}
    for x in range(minx, maxx):
        if _map[y].get(x, '?') in ['#', '?']:
            percolation[y][x] = 10000000000
        elif _map[y].get(x, '?') in [' ', '&']:
            percolation[y][x] = 100000

# percolation[0][0] = 0
# dots = [[0,0]]
# filled = False
# fmax = 0
# while not filled:
#     new_dots = []
#     for d in list(dots):
#         x = d[0]
#         y = d[1]
#         v = percolation[y][x]
#         if _map[y].get(x, '?') not in ['#', '?']:
#             percolate(x+1, y, v+1, _map, percolation, new_dots)
#             percolate(x-1, y, v+1, _map, percolation, new_dots)
#             percolate(x, y-1, v+1, _map, percolation, new_dots)
#             percolate(x, y+1, v+1, _map, percolation, new_dots)
#     filled, fmax = print_perc(percolation, _map)
#     if len(new_dots) == 0:
#         print('dead end')
#         break
#     dots = new_dots
# print(percolation[ay][ax])


# percolation = {}
#
# for y in range(miny, maxy):
#     percolation[y] = {}
#     for x in range(minx, maxx):
#         if _map[y].get(x, '?') in ['#', '?']:
#             percolation[y][x] = 10000000000
#         elif _map[y].get(x, '?') in [' ', '&']:
#             percolation[y][x] = 100000

percolation[ay][ax] = 0
dots = [[ax, ay]]
filled = False
fmax = 0
while not filled:
    new_dots = []
    for d in list(dots):
        x = d[0]
        y = d[1]
        v = percolation[y][x]
        if _map[y].get(x, '?') not in ['#', '?']:
            percolate(x+1, y, v+1, _map, percolation, new_dots)
            percolate(x-1, y, v+1, _map, percolation, new_dots)
            percolate(x, y-1, v+1, _map, percolation, new_dots)
            percolate(x, y+1, v+1, _map, percolation, new_dots)
    filled, fmax = print_perc(percolation, _map)
    if len(new_dots) == 0:
        print('dead end')
        break
    dots = new_dots
print(fmax)

