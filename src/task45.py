def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


def distance(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


with open("../resources/task45.txt") as f:
    max_r = 0
    max_r_id = -1
    content = f.readlines()
    id = 0
    id2data = {}
    for line in content:
        coord = list(map(int, substr_between(line, 'pos=<', '>').split(',')))
        r = int(substr_between(line, 'r=', None).strip())
        id2data[id] = coord + [r]
        if r > max_r:
            max_r = r
            max_r_id = id
        id += 1

    reachable = 0
    x = id2data[max_r_id][0]
    y = id2data[max_r_id][1]
    z = id2data[max_r_id][2]
    r = id2data[max_r_id][3]

    minx = None
    miny = None
    minz = None
    maxx = None
    maxy = None
    maxz = None
    avgx = 0
    avgy = 0
    avgz = 0

    for id, value in id2data.items():
        x1 = value[0]
        y1 = value[1]
        z1 = value[2]
        r1 = value[3]
        avgx = avgx + x1
        avgy = avgy + y1
        avgz = avgz + z1
        minx = min(minx, x1) if minx is not None else x1
        maxx = max(maxx, x1) if maxx is not None else x1
        miny = min(miny, y1) if miny is not None else y1
        maxy = max(maxy, y1) if maxy is not None else y1
        minz = min(minz, z1) if minz is not None else z1
        maxz = max(maxz, z1) if maxz is not None else z1
        dist = distance(x, y, z, x1, y1, z1)
        if dist <= r:
            reachable += 1
    print(reachable)

    opt_x = 0
    opt_y = 0
    opt_z = 0
    bots = 0
    shrt_dist = None
    avgx = avgx // len(id2data.items())
    avgy = avgy // len(id2data.items())
    avgz = avgz // len(id2data.items())
    xdec = 0
    ydec = 0
    zdec = 0
    # for x in

    # for i in range(minx, maxx+1):
    #     for j in range(miny, maxy+1):
    #         for k in range(minz, maxz+1):
    #             reachable = 0
    #             for id, value in id2data.items():
    #                 x=value[0]
    #                 y=value[1]
    #                 z=value[2]
    #                 r=value[3]
    #                 dist = distance(x,y,z,i,j,k)
    #                 if dist <=r:
    #                     reachable+=1
    #             if reachable > bots or (reachable == bots and (shrt_dist is None or shrt_dist >abs(i)+abs(j)+abs(k))):
    #                 print(opt_x, opt_y, opt_z, bots)
    #                 bots = reachable
    #                 opt_x = i
    #                 opt_y = j
    #                 opt_z = k
    #                 shrt_dist = abs(i)+abs(j)+abs(k)
    # print(shrt_dist)

    # xdec = 0
    # for i in range(0, avgx):
    #     x1 = avgx + i
    #     x2 = avgx - i
    #     xreachable = 0
    #
    #
    #     ydec = 0
    #     for j in range(0, avgy):
    #         y1 = avgy + j
    #         y2 = avgy - j
    #         yreachable = 0
    #
    #
    #         zdec = 0
    #         for k in range(0, avgz):
    #             z1 = avgz + k
    #             z2 = avgz - k
    #
    #
    #             reachable = 0
    #
    #             for id, value in id2data.items():
    #                 x = value[0]
    #                 y = value[1]
    #                 z = value[2]
    #                 r = value[3]
    #                 if minx<=x1<=maxx and miny<=y1<=maxy and minz<=z1<=maxz:
    #                     dist = distance(x, y, z, x1, y1, z1)
    #                     if dist <= r:
    #                         reachable += 1
    #                         xreachable = max(xreachable, reachable)
    #                         yreachable = max(yreachable, reachable)
    #                     if reachable > bots or (
    #                             reachable == bots and (shrt_dist is None or shrt_dist > abs(x1) + abs(y1) + abs(z1))):
    #                         # print(opt_x, opt_y, opt_z, reachable)
    #                         bots = reachable
    #                         opt_x = x1
    #                         opt_y = y1
    #                         opt_z = z1
    #                         shrt_dist = abs(x1) + abs(y1) + abs(z1)
    #
    #                 if minx<=x2<=maxx and miny<=y2<=maxy and minz<=z2<=maxz:
    #                     dist = distance(x, y, z, x2, y2, z2)
    #
    #                     if dist <= r:
    #                         reachable += 1
    #                         xreachable = max(xreachable, reachable)
    #                         yreachable = max(yreachable, reachable)
    #                     if reachable > bots or (
    #                             reachable == bots and (shrt_dist is None or shrt_dist > abs(x2) + abs(y2) + abs(z2))):
    #                         # print(opt_x, opt_y, opt_z, reachable)
    #                         bots = reachable
    #                         opt_x = x2
    #                         opt_y = y2
    #                         opt_z = z2
    #                         shrt_dist = abs(x2) + abs(y2) + abs(z2)
    #             if reachable < bots:
    #                 zdec +=1
    #             if zdec > 10:
    #                 print('breakz')
    #                 break
    #         if yreachable < bots:
    #             ydec+=1
    #         if ydec > 10:
    #             print('breaky')
    #             break
    #     if xreachable < bots:
    #         xdec+=1
    #     if xdec > 10:
    #         print('breakx')
    #         break
    # print(shrt_dist)
