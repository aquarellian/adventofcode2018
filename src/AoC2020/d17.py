def to_bool(ch):
    return True if ch == '#' else False


def get_int(map, x, y, z):
    if not z in map or not y in map[z] or not x in map[z][y]:
        return 0
    return int(map[z][y][x])


def get_bool(map, x, y, z):
    if not z in map or not y in map[z] or not x in map[z][y]:
        return False
    return map[z][y][x]


def print_map(map):
    res = 0
    for keyz, mapy in map.items():
        for keyy, mapx in mapy.items():
            line = ''
            for keyx, v in mapx.items():
                line += '#' if v else "."
                res += int(v)
            print(line)
        print(keyz)
    print(res)


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d17.txt") as f:
    content = f.readlines()
    map = dict()
    map[0] = dict()
    # for y in range(-1, 2):
    for y in range(-4, 4):
        map[0][y] = dict()
        # for x in range(-1, 2):
        for x in range(-4, 4):
            # s = content[y + 1][x + 1]
            s = content[y + 4][x + 4]
            map[0][y][x] = to_bool(s)

    i = 0
    maxy = 4
    maxx = 4
    maxz = 0
    print_map(map)
    while i < 6:
        i += 1
        new_map = dict()
        for z in range(-maxz - i, maxz + i + 1):
            new_map[z] = dict()
            for y in range(-maxy - i, maxy + i + 1):
                new_map[z][y] = dict()
                for x in range(-maxx - i, maxx + i + 1):
                    v = get_int(map, x - 1, y, z) + \
                        get_int(map, x - 1, y, z - 1) + get_int(map, x - 1, y, z + 1) + \
                        get_int(map, x - 1, y - 1, z) + get_int(map, x - 1, y + 1, z) + \
                        get_int(map, x - 1, y - 1, z - 1) + get_int(map, x - 1, y - 1, z + 1) + \
                        get_int(map, x - 1, y + 1, z - 1) + get_int(map, x - 1, y + 1, z + 1) + \
                        get_int(map, x + 1, y, z) + \
                        get_int(map, x + 1, y, z - 1) + get_int(map, x + 1, y, z + 1) + \
                        get_int(map, x + 1, y - 1, z) + get_int(map, x + 1, y + 1, z) + \
                        get_int(map, x + 1, y - 1, z - 1) + get_int(map, x + 1, y - 1, z + 1) + \
                        get_int(map, x + 1, y + 1, z - 1) + get_int(map, x + 1, y + 1, z + 1) + \
                        get_int(map, x, y, z - 1) + get_int(map, x, y, z + 1) + \
                        get_int(map, x, y - 1, z) + get_int(map, x, y + 1, z) + \
                        get_int(map, x, y - 1, z - 1) + get_int(map, x, y - 1, z + 1) + \
                        get_int(map, x, y + 1, z - 1) + get_int(map, x, y + 1, z + 1)
                    if get_bool(map, x, y, z):
                        new_map[z][y][x] = (v == 2 or v == 3)
                    else:
                        new_map[z][y][x] = v == 3
        # maxx += 1
        # maxy += 1
        # maxz += 1
        map = new_map
        print_map(map)
#328 low