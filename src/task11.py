with open("../resources/task11.txt") as f:
    content = f.readlines()
    coord = []
    xs = []
    ys = []
    for line in content:
        strs = line.split(',')
        x = int(strs[0].strip())
        y = int(strs[1].strip())
        coord.append([x,y])
        xs.append(x)
        ys.append(y)
    field = {}
    dist_field = {}
    for i in range(min(xs), max(xs)+1):
        if field.get(i, None) is None:
            field[i] = {}
        for j in range(min(ys), max(ys)+1):
            if (i in xs) and (j in ys) and ([i, j] in coord):
                field[i][j] = coord.index([i, j]) + 1
                ci = coord.index([i,j])
                dx = abs(xs[ci] - i)
                dy = abs(ys[ci] - j)
                dist = dx + dy
                dist_field[(i,j)] = dist_field.get((i,j), 0) + dist
            else:
                id = None
                min_dist = None
                collapsed = False
                for ci in range(0, len(coord)):
                    dx = abs(xs[ci] - i)
                    dy = abs(ys[ci] - j)
                    dist = dx + dy
                    dist_field[(i,j)] = dist_field.get((i,j), 0) + dist
                    if (min_dist is None) or (dist < min_dist):
                        min_dist = dist
                        id = ci+1
                        collapsed = False
                    elif dist == min_dist:
                        collapsed = True
                field[i][j] = ('.' if collapsed else id)

    print("task 11")
    themax = 0
    import numpy
    count = list(map(int, numpy.zeros(len(coord)).tolist()))
    on_border_list = set()
    for i, arr in field.items():
        for j, val in arr.items():
            if val != '.':
                on_border = (val in field[min(xs)].values()) or \
                            (val in field[max(xs)].values()) or \
                            (val in [field[x][min(ys)] for x in range(min(xs), max(xs)+1)]) or \
                            (val in [field[x][max(ys)] for x in range(min(xs), max(xs)+1)])
                if (not on_border) and (val != '.'):
                    count[val-1] += 1
                elif on_border:
                    on_border_list.add(val)
    print(count)
    print(max(count))

    print("task 12")
    print(dist_field.values())
    print(on_border_list)
    maybe = [x for x in dist_field.values() if x < 10000]
    print(maybe)
    reversed_dictionary = dict(map(reversed, dist_field.items()))
    aset = set()
    for value in maybe:
        x, y = reversed_dictionary.get(value)
        val = field[x][y]
        if val != '.' and val not in on_border_list and count[val-1] != 0:
            aset.add(count[val-1])
            # print(count[val-1])
            # break
    print(aset)

    # min_total_dist = min(dist_field.values())

    # print(min_total_dist)
    # for key, value in dist_field.items():
    #     # print(value)
    #     if value == min_total_dist:
    #         print(key)
    #         x, y = key
    #         print(x,y)
    #         val = field[x][y]
    #         print(val)
    #         print(count[val-1])




