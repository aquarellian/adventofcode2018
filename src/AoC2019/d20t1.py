import re
import load_input

# with open('../../resources/AoC2019/d20.txt') as r:
#     content = r.readlines()
content = load_input.load(2019, 20).split('\n')[:-1]
# print(content)
# content = [
#     '         A         ',
#     '         A         ',
#     '  #######.#########  ',
#     '  #######.........#  ',
#     '  #######.#######.#  ',
#     '  #######.#######.#  ',
#     '  #######.#######.#  ',
#     '  #####  B    ###.#  ',
#     'BC...##  C    ###.#  ',
#     '  ##.##       ###.#  ',
#     '  ##...DE  F  ###.#  ',
#     '  #####    G  ###.#  ',
#     '  #########.#####.#  ',
#     'DE..#######...###.#  ',
#     '  #.#########.###.#  ',
#     'FG..#########.....#  ',
#     '  ###########.#####  ',
#     '             Z       ',
#     '             Z       '
# ]

def percolate(x, y, v, _map, percolation, _dots, ignore):
    if not ignore and _map[y].get(x, '?') not in ['#', '?']:
        # changed = v != percolation[y][x]
        if v < percolation[y][x]:
            percolation[y][x] = v
            _dots.append([x, y])
        elif v - 1 != percolation[y][x]:
            _dots.append([x, y])
        # if changed:
        #     # something changed - recalculate surroundings
        #     skip = False
        #     for d in _dots:
        #         if d[0] == x and d[1] == y:
        #             skip = True
        #             break
        #     if not skip:
        #         _dots.append([x, y])

def print_field(field):
    with open('test20.txt', 'w') as r:
        for y in range(0, len(field)):
            line = ''
            for x in range(0, len(field[y].keys())):
                if field[y][x] == 10000000000:
                    line += '###'
                elif field[y][x] == 100000:
                    line += '???'
                else:
                    if field[y][x] < 10:
                        line += '00' + str(field[y][x])
                    elif field[y][x] < 100:
                        line += '0' + str(field[y][x])
                    else:
                        line += str(field[y][x])
            r.write(line + '\n')


def came_this_way(x1, y1, v1, x2, y2, v2):
    if v2 == v1 - 1:
        return (x1 == x2 and y1 == y2 -1) or (x1 == x2 and y1 == y2 + 1) or (x1 == x2 - 1 and y1 == y2)or (x1 == x2 + 1 and y1 == y2)
    return False


def is_portal(s):
    return re.match('[A-Z][A-Z]', s)

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
            elif 0 < x < (len(line) - 1) and re.match("[A-Z]", content[y][x + 1]) and content[y][x - 1] == '.':
                name = content[y][x] + content[y][x + 1]
                _map[y][x] = name
                portals[name] = portals.get(name, [])
                portals[name].append([x, y])
            elif 0 < x < (len(line) - 1) and re.match("[A-Z]", content[y][x - 1]) and content[y][x + 1] == '.':
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
print_map(_map)

percolation = {}
for y in range(0, len(_map.keys())):
    percolation[y] = {}
    for x in range(0, len(_map[y].keys())):
        v = _map[y].get(x, '?')
        if v in ['#', '?']:
            percolation[y][x] = 10000000000
        elif v == '.' or re.match('[A-Z]', v):
            percolation[y][x] = 100000

#646 too high
# 77 wrong
#634 wrong
percolation[aay][aax] = 0
dots = []
dots.append([aax, aay])
zz = percolation[zzy][zzx]
iter = 0
while True:
    new_dots = []
    # print(dots)
    for d in dots:
        x = d[0]
        y = d[1]
        v = percolation[y][x]
        if _map[y].get(x, '?') not in ['#', '?']:
            percolate(x+1, y, (v if is_portal(_map[y][x]) or is_portal(_map[y][x+1]) else v+1), _map, percolation, new_dots, came_this_way(x, y, percolation[y][x], x+1, y, percolation[y][x+1]))
            percolate(x-1, y, (v if is_portal(_map[y][x]) or is_portal(_map[y][x-1]) else v+1), _map, percolation, new_dots, came_this_way(x, y, percolation[y][x], x-1, y, percolation[y][x-1]))
            percolate(x, y-1, (v if is_portal(_map[y][x]) or is_portal(_map[y-1][x]) else v+1), _map, percolation, new_dots, came_this_way(x, y, percolation[y][x], x, y-1, percolation[y-1][x]))
            percolate(x, y+1, (v if is_portal(_map[y][x]) or is_portal(_map[y+1][x]) else v+1), _map, percolation, new_dots, came_this_way(x, y, percolation[y][x], x, y+1, percolation[y+1][x]))
            if re.match('[A-Z][A-Z]', _map[y][x]):
                portal_info = portals[_map[y][x]]
                if len(portal_info) > 1:
                    pi1 = portal_info[0]
                    pi2 = portal_info[1]
                    px, py = None, None
                    if pi1[0] == x and pi1[1] == y:
                        px, py = pi2[0], pi2[1]
                    elif pi2[0] == x and pi2[1] == y:
                        px, py = pi1[0], pi1[1]
                    if percolation[py][px] > v+1:
                        # print('teleporting from ', x, y, ' to ', px, py, 'from ', percolation[py][px], 'to', v+1)
                        percolate(px, py, v+1, _map, percolation, new_dots, False)
            # print(new_dots)
    dots = new_dots
    iter += 1
    if iter % 10 == 0:
        print_field(percolation)
    # print(dots)
    if percolation[zzy][zzx] != zz:
        zz = percolation[zzy][zzx]
        print(zz)
    if len(new_dots) == 0:
        print('dead end')
        break



print(percolation[zzy][zzx])



