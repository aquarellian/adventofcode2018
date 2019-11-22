depth = 11394
target = [7, 701]
# depth = 510
# target = [10, 10]

NEITHER = 'neither'
GEAR = 'climbing gear'
TORCH = 'torch'

map = {}
equipment = {TORCH, GEAR, NEITHER}


def eroLevel(x, y):
    if x < len(map[y]):
        return map[y][x]
    if x == target[0] and y == target[1]:
        map[y][x] = 0
    elif x == 0:
        if y == 0:
            map[y][x] = 0
        else:
            map[y][x] = (48271 * y + depth) % 20183
    elif y == 0:
        map[y][x] = (16807 * x + depth) % 20183
    else:
        map[y][x] = (eroLevel(x - 1, y) * eroLevel(x, y - 1) + depth) % 20183
    return map[y][x]


def usable_tools(region):
    region = region % 3
    if region == 0:  # '.':  # rocky
        return {GEAR, TORCH}
    elif region == 2:  # '|':  # narrow
        return {TORCH, NEITHER}
    elif region == 1:  # '=':  # wet
        return {GEAR, NEITHER}


def can_use_gear(gear, region):
    return gear in usable_tools(region)


def get_min_dist(tool, dist_map, i, j):
    return min(dist_map[i][j][NEITHER][tool], dist_map[i][j][GEAR][tool], dist_map[i][j][TORCH][tool])


REALLY_BIG_NUMBER = 10000000000


def get_distance(map, dist_map, tool, i, j, i1, j1):
    common_tools = usable_tools(map[i1][j1]) & usable_tools(map[i][j])
    min_v = dist_map[i][j].get(tool, REALLY_BIG_NUMBER)
    for t in common_tools:
        offset = 1 if t == tool else 8
        min_v = min(min_v, dist_map[i1][j1].get(t, REALLY_BIG_NUMBER) + offset)
    return min_v


risk = 0
# offtop = max(target[0], target[1]) // 2
offtop = 50
for i in range(0, target[1] + offtop):
    map[i] = {}
    strng = ''
    for j in range(0, target[0] + offtop):
        # print(i,j)
        lvl = eroLevel(j, i) % 3
        risk += lvl
        strng += '.' if lvl == 0 else '|' if lvl == 2 else '='
    print(strng)
print(risk)
# 5645 too high
# 5637 ok

dist_map = {}
for i in range(0, len(map)):
    dist_map[i] = {}
    for j in range(0, len(map[i])):
        dist_map[i][j] = {}

tool = TORCH
dist_map[0][0][TORCH] = 0
dist_map[0][0][GEAR] = 7
changed = True
while changed:
    changed = False
    for i in range(0, len(dist_map)):
        for j in range(0, len(dist_map[i])):
            region = map[i][j]
            for tool in usable_tools(region):
                if i > 0:
                    dist = get_distance(map, dist_map, tool, i, j, i - 1, j)
                    current_dist = dist_map[i][j].get(tool, REALLY_BIG_NUMBER)
                    changed |= current_dist > dist
                    dist_map[i][j][tool] = min(dist, current_dist)
                if j > 0:
                    dist = get_distance(map, dist_map, tool, i, j, i, j - 1)
                    current_dist = dist_map[i][j].get(tool, REALLY_BIG_NUMBER)
                    changed |= current_dist > dist
                    dist_map[i][j][tool] = min(dist, current_dist)
                if i < (len(dist_map) - 1):
                    dist = get_distance(map, dist_map, tool, i, j, i + 1, j)
                    current_dist = dist_map[i][j].get(tool, REALLY_BIG_NUMBER)
                    changed |= current_dist > dist
                    dist_map[i][j][tool] = min(dist, current_dist)

                if j < (len(dist_map[i]) - 1):
                    dist = get_distance(map, dist_map, tool, i, j, i, j + 1)
                    current_dist = dist_map[i][j].get(tool, REALLY_BIG_NUMBER)
                    changed |= current_dist > dist
                    dist_map[i][j][tool] = min(dist, current_dist)
                # if i == 0 and j == 3:
                #     print(i, j, tool, dist_map[i][j][tool])
    # print(changed)
for i in range(0, len(dist_map)):
    string = ''
    for j in range(0, len(dist_map[i])):
        string += str(min([dist_map[i][j].get(tool, REALLY_BIG_NUMBER) for tool in equipment])) + ' '
    print(string)

target_map = dist_map[target[1]][target[0]]
print([target_map.get(tool, REALLY_BIG_NUMBER) for tool in equipment])
print(min(target_map.get(TORCH, REALLY_BIG_NUMBER), target_map.get(GEAR, REALLY_BIG_NUMBER) + 7))

# 1020 too high
# min 708 with no eq changes
# 969 ok
