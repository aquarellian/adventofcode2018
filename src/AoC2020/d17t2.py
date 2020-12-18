def to_bool(ch):
    return True if ch == '#' else False


def get_int(map, x, y, z, w):
    if not w in map or not z in map[w] or not y in map[w][z] or not x in map[w][z][y]:
        return 0
    return int(map[w][z][y][x])


def get_bool(map, x, y, z, w):
    if not w in map or not z in map[w] or not y in map[w][z] or not x in map[w][z][y]:
        return False
    return map[w][z][y][x]


def print_map(map):
    res = 0
    for keyw, mapz in map.items():
        for keyz, mapy in mapz.items():
            for keyy, mapx in mapy.items():
                line = ''
                for keyx, v in mapx.items():
                    line += '#' if v else "."
                    res += int(v)
                print(line)
            print(keyz, keyw)
    print(res)


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d17.txt") as f:
    content = f.readlines()
    map = dict()
    map[0] = dict()
    map[0][0] = dict()
    # for y in range(-1, 2):
    for y in range(-4, 4):
        map[0][0][y] = dict()
        # for x in range(-1, 2):
        for x in range(-4, 4):
            # s = content[y + 1][x + 1]
            s = content[y + 4][x + 4]
            map[0][0][y][x] = to_bool(s)

    i = 0
    maxy = 4
    maxx = 4
    maxz = 0
    maxw = 0
    print_map(map)
    while i < 6:
        i += 1
        new_map = dict()
        for w in range(-maxw - i, maxw + i + 1):
            new_map[w] = dict()
            for z in range(-maxz - i, maxz + i + 1):
                new_map[w][z] = dict()
                for y in range(-maxy - i, maxy + i + 1):
                    new_map[w][z][y] = dict()
                    for x in range(-maxx - i, maxx + i + 1):
                        v = get_int(map, x - 1, y, z, w) + \
                            get_int(map, x - 1, y, z - 1, w) + get_int(map, x - 1, y, z + 1, w) + \
                            get_int(map, x - 1, y - 1, z, w) + get_int(map, x - 1, y + 1, z, w) + \
                            get_int(map, x - 1, y - 1, z - 1, w) + get_int(map, x - 1, y - 1, z + 1, w) + \
                            get_int(map, x - 1, y + 1, z - 1, w) + get_int(map, x - 1, y + 1, z + 1, w) + \
                            get_int(map, x + 1, y, z, w) + \
                            get_int(map, x + 1, y, z - 1, w) + get_int(map, x + 1, y, z + 1, w) + \
                            get_int(map, x + 1, y - 1, z, w) + get_int(map, x + 1, y + 1, z, w) + \
                            get_int(map, x + 1, y - 1, z - 1, w) + get_int(map, x + 1, y - 1, z + 1, w) + \
                            get_int(map, x + 1, y + 1, z - 1, w) + get_int(map, x + 1, y + 1, z + 1, w) + \
                            get_int(map, x, y, z - 1, w) + get_int(map, x, y, z + 1, w) + \
                            get_int(map, x, y - 1, z, w) + get_int(map, x, y + 1, z, w) + \
                            get_int(map, x, y - 1, z - 1, w) + get_int(map, x, y - 1, z + 1, w) + \
                            get_int(map, x, y + 1, z - 1, w) + get_int(map, x, y + 1, z + 1, w) + \
 \
                            get_int(map, x - 1, y, z, w - 1) + \
                            get_int(map, x - 1, y, z - 1, w - 1) + get_int(map, x - 1, y, z + 1, w - 1) + \
                            get_int(map, x - 1, y - 1, z, w - 1) + get_int(map, x - 1, y + 1, z, w - 1) + \
                            get_int(map, x - 1, y - 1, z - 1, w - 1) + get_int(map, x - 1, y - 1, z + 1, w - 1) + \
                            get_int(map, x - 1, y + 1, z - 1, w - 1) + get_int(map, x - 1, y + 1, z + 1, w - 1) + \
                            get_int(map, x + 1, y, z, w - 1) + \
                            get_int(map, x + 1, y, z - 1, w - 1) + get_int(map, x + 1, y, z + 1, w - 1) + \
                            get_int(map, x + 1, y - 1, z, w - 1) + get_int(map, x + 1, y + 1, z, w - 1) + \
                            get_int(map, x + 1, y - 1, z - 1, w - 1) + get_int(map, x + 1, y - 1, z + 1, w - 1) + \
                            get_int(map, x + 1, y + 1, z - 1, w - 1) + get_int(map, x + 1, y + 1, z + 1, w - 1) + \
                            get_int(map, x, y, z - 1, w - 1) + get_int(map, x, y, z + 1, w - 1) + \
                            get_int(map, x, y - 1, z, w - 1) + get_int(map, x, y + 1, z, w - 1) + \
                            get_int(map, x, y - 1, z - 1, w - 1) + get_int(map, x, y - 1, z + 1, w - 1) + \
                            get_int(map, x, y + 1, z - 1, w - 1) + get_int(map, x, y + 1, z + 1, w - 1) + \
 \
                            get_int(map, x - 1, y, z, w + 1) + \
                            get_int(map, x - 1, y, z - 1, w + 1) + get_int(map, x - 1, y, z + 1, w + 1) + \
                            get_int(map, x - 1, y - 1, z, w + 1) + get_int(map, x - 1, y + 1, z, w + 1) + \
                            get_int(map, x - 1, y - 1, z - 1, w + 1) + get_int(map, x - 1, y - 1, z + 1, w + 1) + \
                            get_int(map, x - 1, y + 1, z - 1, w + 1) + get_int(map, x - 1, y + 1, z + 1, w + 1) + \
                            get_int(map, x + 1, y, z, w + 1) + \
                            get_int(map, x + 1, y, z - 1, w + 1) + get_int(map, x + 1, y, z + 1, w + 1) + \
                            get_int(map, x + 1, y - 1, z, w + 1) + get_int(map, x + 1, y + 1, z, w + 1) + \
                            get_int(map, x + 1, y - 1, z - 1, w + 1) + get_int(map, x + 1, y - 1, z + 1, w + 1) + \
                            get_int(map, x + 1, y + 1, z - 1, w + 1) + get_int(map, x + 1, y + 1, z + 1, w + 1) + \
                            get_int(map, x, y, z - 1, w + 1) + get_int(map, x, y, z + 1, w + 1) + \
                            get_int(map, x, y - 1, z, w + 1) + get_int(map, x, y + 1, z, w + 1) + \
                            get_int(map, x, y - 1, z - 1, w + 1) + get_int(map, x, y - 1, z + 1, w + 1) + \
                            get_int(map, x, y + 1, z - 1, w + 1) + get_int(map, x, y + 1, z + 1, w + 1) + \
 \
                            get_int(map, x, y, z, w + 1) + get_int(map, x, y, z, w - 1)
                        if get_bool(map, x, y, z, w):
                            new_map[w][z][y][x] = (v == 2 or v == 3)
                        else:
                            new_map[w][z][y][x] = v == 3
        # maxx += 1
        # maxy += 1
        # maxz += 1
        map = new_map
        print_map(map)
# 328 low
