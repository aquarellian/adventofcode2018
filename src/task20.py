
def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


with open("../resources/task20.txt") as f:
    content = f.readlines()
    data = {}
    minx = None
    miny = None
    maxx = None
    maxy = None
    for line in content:
        coord = substr_between(line, 'position=<', '>').split(',')
        x = int(coord[0])
        y = int(coord[1])
        velocity = substr_between(line, 'velocity=<', '>').split(',')
        dx = int(velocity[0])
        dy = int(velocity[1])
        data[x, y] = [dx, dy]
        print(str(x) + ' ' + str(y) + ' ' + str(dx) + ' ' + str(dy))
        minx = x if minx is None or minx > x else minx
        maxx = x if maxx is None or maxx < x else maxx
        miny = y if miny is None or miny > y else miny
        maxy = y if maxy is None or maxy < y else maxy

    print('miny=' + str(miny))
    print('maxy=' + str(maxy))

    keep_going = True
    import copy
    data_before = copy.copy(data)
    data_after = {}
    sec = 0
    deltax = abs(minx) if minx < 0 else -minx
    deltay = abs(miny) if miny < 0 else -miny


    while keep_going:
        print('after ' + str(sec) + ' sec')
        import cv2
        import numpy as np
        img = np.zeros((maxx-minx, maxy-miny, 2), np.uint8)

        # array = np.zeros([maxx-minx, maxy-miny, 3], dtype=np.uint8)
        # with open('../resources/task20.out.txt', 'w', newline='') as r:
        for y in range(miny, maxy+1):
            printlane=''
            for x in range(minx, maxx+1):
                vel = data_before.get((x, y), None)
                if vel is not None:
                    printlane += '#'
                    dx = vel[0]
                    dy = vel[1]
                    newx = x+dx
                    newy = y+dy
                    data_after[newx, newy] = vel

                    img.itemset((x+deltax, y+deltay, 2), 255)
                else:
                    printlane += '.'

        # r.write(printlane + '\n')

            # print(printlane)
        from PIL import Image
        # img = Image.fromarray(array)
        img.save('../resources/task20.out.png')

        keep_going = input('continue?') != 'n'

        data_before = copy.copy(data_after)
        data_after = {}
        sec +=1








