import re
import load_input
content = load_input.load(2019, 20).split('\n')[:-1]

def print_map(_map):
    for y in range(0, len(_map.keys())):
        line = ''
        for x in range(0, len(_map[y].keys())):
            if re.match("[A-Z]", _map[y][x]):
                line += _map[y][x]
            else:
                line += _map[y][x]*2
        print(line)

_map = {}
portals = {}
aax, aay, zzx, zzy = None, None, None, None
for y in range(0, len(content)):
    line = content[y]
    _map[y] = {}
    for x in range(0, len(line)):
        ch = line[x]
        if ch in ["#", ' ']:
            _map[y][x] = '#'
        elif ch == '.':
            _map[y][x] = '.'
        elif re.match("[A-Z]", ch):
            print(x, y, len(content) - 1)
            if 0 < y < (len(content) - 1) and re.match("[A-Z]", content[y - 1][x]) and content[y + 1][x] == '.':
                name = content[y - 1][x] + content[y][x]
                _map[y][x] = name
                portals[name] = portals.get(name, [])
                portals[name].append([x, y])
            elif 0 < y < (len(content) - 1) and re.match("[A-Z]", content[y + 1][x]) and content[y - 1][x] == '.':
                name = content[y][x] + content[y + 1][x]
                _map[y][x] = name
                portals[name] = portals.get(name, [])
                portals[name].append([x, y])
            elif 0 < x < (len(content[y]) - 1) and re.match("[A-Z]", content[y][x + 1]) and content[y][x - 1] == '.':
                name = content[y][x] + content[y][x + 1]
                _map[y][x] = name
                portals[name] = portals.get(name, [])
                portals[name].append([x, y])
            elif 0 < x < (len(content[y]) - 1) and re.match("[A-Z]", content[y][x - 1]) and content[y][x + 1] == '.':
                name = content[y][x - 1] + content[y][x]
                _map[y][x] = name
                portals[name] = portals.get(name, [])
                portals[name].append([x, y])
            else:
                _map[y][x] = '#'
            if _map[y][x] == 'AA':
                aax = x
                aay = y
            elif _map[y][x] == 'ZZ':
                zzx = x
                zzy = y
# print(_map)
# print_map(_map)

def percolate(x, y, v, _map, percolation, dots):
    if _map[y].get(x, '?') not in ['#', '?']:
        percolation[y][x] = min(percolation[y][x], v)
        if percolation[y][x] == v:
            dots.append([x,y])

def print_field(field):
    with open('test20.txt', 'w') as r:
        for y in range(0, len(field)):
            line = ''
            for x in range(0, len(field[y].keys())):
                if field[y][x] == 10000000000:
                    line += '##'
                elif field[y][x] == 100000:
                    line += '??'
                else:
                    if field[y][x] < 10:
                        line += '0' + str(field[y][x])
                    else:
                        line += str(field[y][x])
            r.write(line + '\n')

percolation = {}
for y in range(0, len(_map.keys())):
    percolation[y] = {}
    for x in range(0, len(_map[y].keys())):
        v = _map[y].get(x, '?')
        if v in ['#', '?']:
            percolation[y][x] = 10000000000
        elif v == '.' or re.match('[A-Z]', v):
            percolation[y][x] = 100000

percolation[aay][aax] = 0
dots = [[aax, aay]]
while percolation[zzy][zzx] == 100000:
    new_dots = []
    for d in list(dots):
        x = d[0]
        y = d[1]
        v = percolation[y][x]
        if _map[y].get(x, '?') not in ['#', '?']:
            percolate(x+1, y, v+1, _map, percolation, new_dots)
            percolate(x-1, y, v1, _map, percolation, new_dots)
            percolate(x, y-1, v+1, _map, percolation, new_dots)
            percolate(x, y+1, v+1, _map, percolation, new_dots)
            if re.match('[A-Z][A-Z]', _map[y][x]):
                portal_info = portals[_map[y][x]]
                if len(portal_info) > 1:
                    if portal_info[0][0] == x and portal_info[0][1] == y:
                        px, py = portal_info[1][0], portal_info[1][1]
                        vp = percolation[py][px]
                        print('teleporting from ', x, y, ' to ', px, py)
                        percolate(px,py, vp+1, _map, percolation, new_dots)
                    else:
                        px, py = portal_info[0][0], portal_info[0][1]
                        vp = percolation[py][px]
                        print('teleporting from ', x, y, ' to ', px, py)
                        percolate(px,py, vp+1, _map, percolation, new_dots)
        print_field(percolation)
    if len(new_dots) == 0:
        print('dead end')
        break
    # if percolation[zzy][zzx] != 100000:
    #     break
    dots = new_dots
print(percolation[zzy][zzx])



