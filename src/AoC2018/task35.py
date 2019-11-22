def count_neighbors(amap, i, j, symbol):
    count = 0
    count += (amap[i-1][j-1] == symbol if i > 0 and j > 0 else 0)
    count += (amap[i-1][j] == symbol if i > 0 else 0)
    count += (amap[i-1][j+1] == symbol if i > 0 and j < len(amap[i])-1 else 0)
    count += (amap[i][j-1] == symbol if j > 0 else 0)
    count += (amap[i][j+1] == symbol if j < len(amap[i])-1 else 0)
    count += (amap[i+1][j-1] == symbol if i < len(amap)-1 and j > 0 else 0)
    count += (amap[i+1][j] == symbol if i < len(amap)-1 else 0)
    count += (amap[i+1][j+1] == symbol if i < len(amap)-1 and j < len(amap[i])-1 else 0)
    return count


def next_state(amap, i, j):
    if amap[i][j] == '.':
        return '|' if count_neighbors(amap, i, j, '|') >= 3 else '.'
    elif amap[i][j] == '|':
        return  '#' if count_neighbors(amap, i, j, '#') >= 3 else '|'
    elif amap[i][j] == '#':
        return '#' if count_neighbors(amap, i, j, '#') >= 1 and count_neighbors(amap, i, j, '|') >= 1 else '.'


def print_out(amap):
    for i in range(0, len(amap)):
        line = ''
        for j in range(0, len(amap[i])):
            line += amap[i][j]
        print(line)


with open("../resources/task35.txt") as f:
    content = f.readlines()
    the_map = []
    for i, line in enumerate(content):
        the_map.append([])
        for j in range(0, len(line.strip())):
            the_map[i].append(line[j])

    minute = 0
    # print_out(the_map)
    max_min = 10
    # max_min = 1000000000
    res = set()
    pattern = []
    duplicated = False
    duple_minute = 0
    while minute < max_min:
        wood = 0
        lumber = 0
        new_map = []
        minute +=1
        for i in range(0, len(the_map)):
            new_map.append([])
            for j in range(0, len(the_map[i])):
                new_symb = next_state(the_map, i, j)
                new_map[i].append(new_symb)
                if new_symb == '|':
                    wood += 1
                elif new_symb == '#':
                    lumber+=1
        the_map = new_map

        # print()
        # print_out(new_map)

        num = wood*lumber
        print(minute, num)








