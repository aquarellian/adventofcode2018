MAX_DIST = 10000
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
    minx = min(xs) if min(xs) < MAX_DIST else min(xs) - MAX_DIST
    maxx = max(xs) + MAX_DIST
    miny = min(ys) if min(ys) < MAX_DIST else min(ys) - MAX_DIST
    maxy = max(ys) + MAX_DIST
    count = 0
    for i in range(minx, maxx+1):
        for j in range(miny, maxy+1):
            totaldist = 0
            for ci in range(0, len(coord)):
                dx = abs(xs[ci] - i)
                dy = abs(ys[ci] - j)
                dist = dx + dy
                totaldist += dist
                # dist_field[(i,j)] = dist_field.get((i,j), 0) + dist
            # if dist_field[i,j] < MAX_DIST:
            if totaldist < MAX_DIST:
                count += 1

    # maybe = [x for x in dist_field.values() if x < MAX_DIST]
    # print(len(maybe))

#     coords_by_dist = {}
#
#     dist2count = {}
#     maybeset = set(maybe)
#     for value in maybeset:
#         dist2count[value] = maybe.count(value)
#         coords_by_dist[value] = []
#         for key1, val1 in dist_field.items():
#             if val1 == value:
#                 coords_by_dist[value].append(key1)
#
#
#     for dist, coords in coords_by_dist.items():
#
#         groups = to_groups()
#         for group in groups:
#
#     print(dist2count)
#
# def to_groups(val, field):





