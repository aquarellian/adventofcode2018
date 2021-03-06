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






