import load_input
# content = load_input.load(2019, 3).split('\n')
content='R8,U5,L5,D3\nU7,R6,D4,L4'.split('\n')
map = {}
x = 0
y = 0
li = 0
for line in content:
    count = 0
    for command in line.split(','):
        if len(command) > 1:
            dir = command[0]
            ln = int(command[1])

            x1 = x
            y1 = y
            if dir == 'U':
                y1 = y+int(ln)
            elif dir == 'D':
                y1 = y-int(ln)
            elif dir == 'L':
                x1 = x-int(ln)
            elif dir == 'R':
                x1 = x+int(ln)
            stepx = x1-1 if x > x1 else 1
            stepy = y1-1 if y > y1 else 1
            print(x, y, '->', x1, y1, command, stepx, range(x + stepx, x1 + stepx, stepx), stepy, range(y + stepy, y1 + stepy, stepy))
            for _x in range(x, x1 + stepx, stepx):
                for _y in range(y, y1 + stepy, stepy):
                    print(_x, _y)
                    if map.get(_x) is None:
                        map[_x] = {}
                    if map[_x].get(_y) is None:
                        map[_x][_y] = {}
                    if map[_x][_y].get(li, None) is None:
                        count += 1
                        map[_x][_y][li] = count
            x = x1
            y = y1

_min = 10000000
print(map)
for x in map.keys():
    for y in map[x].keys():
        print(x, y, map[x][y].get(0, None))
        print(x, y, map[x][y].get(1, None))
        if map[x][y].get(0, None) is not None and map[x][y].get(1, None) is not None:
            v = map[x][y][0] + map[x][y][1]
            _min = min(_min, v)
print(_min)