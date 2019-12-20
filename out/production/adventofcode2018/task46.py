def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


def distance(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def count_reachable(x, y, z, id2data):
    count = 0
    for v in id2data.values():
        is_reachable = distance(x, y, z, v[0], v[1], v[2]) < v[3]
        if is_reachable:
            count += 1
    return count


def update_data(max_reachable, max_r_distance, rx, ry, rz, x, y, z, id2data):
    new_reachable = count_reachable(x, y, z, id2data)
    # if no improvement - no change
    if new_reachable < max_reachable:
        return max_reachable, max_r_distance, rx, ry, rz, False

    new_dist = distance(x, y, z, 0, 0, 0)
    # if improvement - new values
    if new_reachable > max_reachable:
        print('Improved!!!!')
        print(new_reachable, x, y, z, new_dist)
        return new_reachable, new_dist, x, y, z, True

    # if same res - shortest dist to x
    if new_dist < max_r_distance:
        print('Moved!!!!')
        print(new_reachable, x, y, z, new_dist)
        return new_reachable, new_dist, x, y, z, True
    else:
        return max_reachable, max_r_distance, rx, ry, rz, True


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

    bot = None
    max_reachable = 0
    dist_to_0 = 0
    for id, value in id2data.items():
        bot_reachable = count_reachable(value[0], value[1], value[2], id2data)
        if bot_reachable > max_reachable:
            max_reachable = bot_reachable
            dist_to_0 = distance(value[0], value[1], value[2], 0, 0, 0)
            bot = id
        elif bot_reachable == max_reachable:
            bot_dist_to_0 = distance(value[0], value[1], value[2], 0, 0, 0)
            if bot_dist_to_0 < dist_to_0:
                max_reachable = bot_reachable
                dist_to_0 = distance(value[0], value[1], value[2], 0, 0, 0)
                bot = id

    avgx = id2data[bot][0]
    avgy = id2data[bot][1]
    avgz = id2data[bot][2]

    rx = avgx
    ry = avgy
    rz = avgz
    print(max_reachable, rx, ry, rz)

    diff = 0
    no_improvement = 0
    no_improvement_left = 0
    no_improvement_right = 0
    no_improvement_up = 0
    no_improvement_down = 0
    no_improvement_forward = 0
    no_improvement_backward = 0

    # while True:
    #     diff += 1
    #     for i in range(avgy - diff, avgy + diff + 1):
    #         for j in range(avgx - diff, avgx + diff + 1):
    #             max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
    #                                                                           i, avgz - diff, id2data)
    #             max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
    #                                                                           i, avgz + diff, id2data)
    #             if not improved1 and not improved2:
    #                 no_improvement += 1
    #                 print(no_improvement)
    #         for k in range(avgz - diff, avgz + diff + 1):
    #             max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz,
    #                                                                           avgx - diff, i, k, id2data)
    #             max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz,
    #                                                                           avgx + diff, i, k, id2data)
    #             if not improved1 and not improved2:
    #                 no_improvement += 1
    #                 print(no_improvement)
    #     for j in range(avgx - diff, avgx + diff + 1):
    #         for k in range(avgz - diff, avgz + diff + 1):
    #             max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
    #                                                                           avgy - diff, k, id2data)
    #             max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
    #                                                                           avgy + diff, k, id2data)
    #             if not improved1 and not improved2:
    #                 no_improvement += 1
    #
    #     if no_improvement > 100:
    #         break
    # print(max_reachable, rx, ry, rz, distance(rx, ry, rz, 0, 0, 0))

    # 108382997 too high
    # 87578931 too high
    # 87523010 too high

    count = 815
    rx = 28167693
    ry = 22045886
    rz = 37309441
    dist = 87523020
    while True:
        new_count = count_reachable(rx - 1, ry-1, rz-1, id2data)
        new_dist = distance(rx - 1, ry-1, rz-1, 0,0,0)
        if new_count >= count and new_dist < dist:
            dist = new_dist
            count = new_count
            rx = rx - diff
            ry = ry - diff
            rz = rz - diff
            print(count, rx, ry, rz, new_dist)
        else:
            break


    avgx = rx
    avgy = ry
    avgz = rz
    diff = 0

    while True:
        diff += 1
        for i in range(avgy - diff, avgy + diff + 1):
            for j in range(avgx - diff, avgx + diff + 1):
                max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
                                                                              i, avgz - diff, id2data)
                max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
                                                                              i, avgz + diff, id2data)
                if not improved1 and not improved2:
                    no_improvement += 1
                    print(no_improvement)
            for k in range(avgz - diff, avgz + diff + 1):
                max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz,
                                                                              avgx - diff, i, k, id2data)
                max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz,
                                                                              avgx + diff, i, k, id2data)
                if not improved1 and not improved2:
                    no_improvement += 1
                    print(no_improvement)
        for j in range(avgx - diff, avgx + diff + 1):
            for k in range(avgz - diff, avgz + diff + 1):
                max_reachable, dist_to_0, rx, ry, rz, improved1 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
                                                                              avgy - diff, k, id2data)
                max_reachable, dist_to_0, rx, ry, rz, improved2 = update_data(max_reachable, dist_to_0, rx, ry, rz, j,
                                                                              avgy + diff, k, id2data)
                if not improved1 and not improved2:
                    no_improvement += 1

        if no_improvement > 100:
            break
    print(max_reachable, rx, ry, rz, distance(rx, ry, rz, 0, 0, 0))




