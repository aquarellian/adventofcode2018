MAX_DIST = 10000
# MAX_DIST = 32
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
    # dist_field = {}
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    count = 0
    for i in range(minx, maxx+1):
        for j in range(miny, maxy+1):
            totaldist = 0
            for ci in range(0, len(coord)):
                dx = abs(xs[ci] - i)
                dy = abs(ys[ci] - j)
                dist = dx + dy
                totaldist += dist
            if totaldist < MAX_DIST:
                count += 1
    print(count)







