def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]

def parse_range(line):
    coords = line.strip().split('..')
    return range(int(coords[0]), int(coords[len(coords)-1]) + 1)

def is_water(symbol):
    return symbol in ['+', '|', '~']

def is_still(symbol):
    return symbol == '~'

def is_spring(x, y):
    return x == 500 and y == 0

def print_out(clay_map, minx, maxx, miny, maxy):
    for y in range(miny, maxy+1):
        line = ''
        i = y - miny
        for x in range(minx, maxx+1):
            j = x - minx
            line += clay_map[i][j]
        print(line)

with open("../resources/task33.txt") as f:
    content = f.readlines()
    clay = []
    spring = [500, 0]
    # make sure to enclose spring
    maxx = spring[0]
    minx = spring[0]
    maxy = spring[1]
    miny = spring[1]
    for line in content:
        coords = line.strip().split(',')
        x_range = None
        y_range = None
        for coord in coords:
            if 'x=' in coord:
                x_range = parse_range(substr_between(coord, 'x=', None))
            elif 'y=' in coord:
                y_range = parse_range(substr_between(coord, 'y=', None))
        for y in y_range:
            for x in x_range:
                clay.append([x, y])
                maxx = max(x, maxx)
                minx = min(x, minx)
            maxy = max(y, maxy)
            miny = min(y, miny)

    clay_map = []
    for y in range(miny, maxy+1):
        clay_map.append([])
        i = y - miny
        for x in range(minx, maxx+1):
            j = x - minx
            if x == spring[0] and y == spring[1]:
                symbol = '+'
            elif [x, y] in clay:
                symbol = '#'
            else:
                symbol = '.'
            clay_map[i].append(symbol)



    pic_changed = True
    iteration = 0
    min_water_y = 0
    max_water_y = 0
    min_water_x = 500
    max_water_x = 500
    while pic_changed:
        iteration +=1
        pic_changed = False
        for y in range(miny, maxy+1):
            i = y - miny
            for x in range(minx, maxx+1):
                j = x - minx
                symbol = clay_map[i][j]
                if is_water(symbol):
                    if symbol == '~':
                        continue
                    elif symbol == '+' or symbol == '|':
                        # go down?
                        if i < len(clay_map) - 1:
                            symbol_below = clay_map[i+1][j]
                            if symbol_below == '.':
                                clay_map[i+1][j] = '|'
                                pic_changed = True
                            elif symbol_below == '#' or symbol_below == '~': # no way down
                                # go sides
                                no_way_left = False
                                no_way_right = False
                                if j > 0:
                                    # go left
                                    symbol_left = clay_map[i][j-1]
                                    if symbol_left == '#' or symbol_left == '~':
                                        no_way_left = True
                                    elif symbol_left == '|':
                                        k = j - 1
                                        while k >= 0 and clay_map[i][k] == '|':
                                            k = k-1
                                        if k >= 0 and (clay_map[i][k] == '#' or clay_map[i][k] == '~'):
                                            no_way_left = True
                                    elif symbol_left == '.':
                                        clay_map[i][j-1] = '|'
                                        pic_changed = True
                                if j < len(clay_map[i]) - 1:
                                    # go right
                                    symbol_right = clay_map[i][j+1]
                                    if symbol_right == '#' or symbol_right == '~':
                                        no_way_right = True
                                    elif symbol_right == '|':
                                        k = j + 1
                                        while k < len(clay_map[i]) and clay_map[i][k] == '|':
                                            k = k+1
                                        if k < len(clay_map[i]) and (clay_map[i][k] == '#' or clay_map[i][k] == '~'):
                                            no_way_right = True
                                    elif symbol_right == '.':
                                        clay_map[i][j+1] = '|'
                                        pic_changed = True
                                if no_way_left and no_way_right:
                                    clay_map[i][j] = '~'
                                    pic_changed = True
        # print_out(clay_map, minx, maxx, miny, maxy)
        # print()
        # print()
        if iteration % 100 == 0:
            print_out(clay_map, minx, maxx, miny, maxy)



    count = 0
    for y in range(miny, maxy+1):
        i = y - miny
        for x in range(minx, maxx+1):
            j = x - minx
            symbol = clay_map[i][j]
            if is_water(symbol):
                count +=1
    print(count-1) # not counting the spring













