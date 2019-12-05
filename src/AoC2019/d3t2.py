import load_input
content = load_input.load(2019, 3).split('\n')
# content='R8,U5,L5,D3\nU7,R6,D4,L4'.split('\n')
# content='R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'.split('\n')
# content='R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split('\n')
map = {}
li = 0
for line in content:
    count = 1
    print(line)
    x = 0
    y = 0
    map[x] = {y:{0:0, 1:0}}
    for command in line.split(','):
        if len(command) > 1:
            dir = command[0]
            ln = int(command[1:])

            x1 = x
            y1 = y
            stepx=0
            stepy=0
            if dir == 'U':
                y1 = y+int(ln)
                stepy=1
                stepx=1
            elif dir == 'D':
                y1 = y-int(ln)
                stepy=-1
                stepx=1
            elif dir == 'L':
                x1 = x - int(ln)
                stepx=-1
                stepy=1
            elif dir == 'R':
                x1 = x+int(ln)
                stepx=1
                stepy=1
            # stepx = x1-1 if x > x1 else 1
            # stepy = y1-1 if y > y1 else 1
            # print(x, y, '->', x1, y1, command, stepx, range(x + stepx, x1 + stepx, stepx), stepy, range(y + stepy, y1 + stepy, stepy))
            for _x in range(x, x1 + stepx, stepx):
                for _y in range(y, y1 + stepy, stepy):
                    if _x == x and _y == y:
                        continue
                    # print(_x, _y)
                    if map.get(_x) is None:
                        map[_x] = {}
                    if map[_x].get(_y) is None:
                        map[_x][_y] = {}
                    if map[_x][_y].get(li, None) is None:
                        map[_x][_y][li] = count
                    count += 1
                    # print(_x, _y, li, count)
                    # if _x == 3 and _y == 3:
                    #     print('3:3', li, map[_x][_y][li])
                    # elif _x == 6 and _y == 5:
                    #     print('6:5', li, map[_x][_y][li])
            x = x1
            y = y1
    li+=1

_min = 10000000
mapstr1 = ''
mapstr2 = ''
for x in map.keys():
    for y in map[x].keys():
        # print(x, y, map[x][y].get(0, None))
        # print(x, y, map[x][y].get(1, None))
        if not (x== 0 and y == 0) and map[x][y].get(0, None) is not None and map[x][y].get(1, None) is not None:
            print(x, y, map[x][y][0], map[x][y][1], map[x][y][0] + map[x][y][1])
            v = map[x][y][0] + map[x][y][1]
            _min = min(_min, v)
print(_min)

# for x in range(0, 10):
#     for y in range(0, 10):
#         if map.get(x) is not None and map[x].get(y) is not None:
#             mapstr1 += str(map[x][y].get(0, 'X'))
#             mapstr2 += str(map[x][y].get(1, 'X'))
#         else:
#             mapstr1+='X'
#             mapstr2+='X'
#     mapstr1+='\n'
#     mapstr2+='\n'

# print(mapstr1)
# print(mapstr2)


# 37 wrong
# 4157 wrong
# 4163 wrong