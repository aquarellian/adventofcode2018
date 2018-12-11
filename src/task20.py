
def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


with open("../resources/task20.test.txt") as f:
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
        data[(x, y)] = [dx, dy]
        print(str(x) + ' ' + str(y) + ' ' + str(dx) + ' ' + str(dy))
        minx = x if minx is None or minx > x else minx
        maxx = x if maxx is None or maxx < x else maxx
        miny = y if miny is None or miny > y else miny
        maxy = y if maxy is None or maxy < y else maxy

    print('miny=' + str(miny))
    print('maxy=' + str(maxy))

    keep_going = True
    sec = 0
    deltax = abs(minx) if minx < 0 else -minx
    deltay = abs(miny) if miny < 0 else -miny


    while keep_going:
        updated = []
        for coord, vel in data.items():
            print(coord)
            print(vel)
            x=coord[0]
            y=coord[1]
            dx = vel[0]
            dy = vel[1]
            newx = x+sec*dx
            newy = y+sec*dy
            updated.append([newx, newy])
        print(updated)

        print('after ' + str(sec) + ' sec')
        for y in range(miny, maxy+1):
            printlane=''
            for x in range(minx, maxx+1):
                printlane += ( '#' if [x,y] in updated else '.')

            print(printlane)

        keep_going = input('continue?') != 'n'

        sec +=1








