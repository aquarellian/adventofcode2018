import opcode
# import load_input

with open("../../resources/AoC2019/d15.txt") as f:
    content = f.readlines()[0].split(',')


def update_map(x, y, _map, value):
    if y not in _map.keys():
        _map[y] = {}
    if x in _map[y].keys():
        print('warning: overwriting', x, y, _map[y][x], value)
    _map[y][x] = value


def print_field(field, dx, dy, dir):
    for y in range(min(field.keys(), max(field.keys())+1)):
        line = ''
        if y in field.keys():
            for x in range(min(field[y].keys(), max(field[y].keys())+1)):
                if y ==dy and x == dx:
                    line += '^' if dir == 1 else '>' if dir == 4 else 'v' if dir ==2 else '<'
                else:
                    line += field[y].get(x, '?')
        else:
            if y == dy:
                line += '?'*dx + ('^' if dir == 1 else '>' if dir == 4 else 'v' if dir ==2 else '<')
            else:
                line + '?' * (max(field.keys) - min(field.keys() + 1))
        print(line)


# content = load_input.load(2019, 15).split(',')
amp = opcode.Amplifier(content)
res = None
dir = 1
_map = {}
x = 0
y = 0
_map[y] = {}
_map[y][x] = ' '

i = 10
while i > 0:
    i-=1
    _x = x
    _y = x
    if res is None or res == 1:
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
    if dir == 1:
        _y += 1
    elif dir == 4:
        _x += 1
    elif dir == 2:
        _y -= 1
    elif dir == 3:
        _x -=1
    res = amp.apply(dir)
    if res == 0:
        update_map(_x, _y, _map, '#')
    elif res == 2:
        update_map(_x, _y, _map, '&')
        x = _x
        y = _y
        #break
    else:
        update_map(_x, _y, _map, ' ')
        x = _x
        y = _y
    print(_x,  _y)
    print_field(_map, x, y, dir)


