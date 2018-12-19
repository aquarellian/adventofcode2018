
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
    for line in content:
        coord = substr_between(line, 'position=<', '>').split(',')
        x = int(coord[0])
        y = int(coord[1])
        velocity = substr_between(line, 'velocity=<', '>').split(',')
        dx = int(velocity[0])
        dy = int(velocity[1])
        data[(x, y)] = [dx, dy]
    #     minx = x if minx is None or minx > x else minx
    #     maxx = x if maxx is None or maxx < x else maxx
    #     miny = y if miny is None or miny > y else miny
    #     maxy = y if maxy is None or maxy < y else maxy
    #
    # print('miny=' + str(miny))
    # print('maxy=' + str(maxy))

    keep_going = True
    sec = 10880


    while keep_going and sec<10900:
        minx = None
        miny = None
        maxx = None
        maxy = None
        updated = []
        for coord, vel in data.items():
            x=coord[0]
            y=coord[1]
            dx = vel[0]
            dy = vel[1]
            newx = x+sec*dx
            newy = y+sec*dy
            updated.append([newx, newy])
            minx = newx if minx is None or minx > newx else minx
            maxx = newx if maxx is None or maxx < newx else maxx
            miny = newy if miny is None or miny > newy else miny
            maxy = newy if maxy is None or maxy < newy else maxy
        # print(updated)

        print('after ' + str(sec) + ' sec')
        print('minx='+str(minx) + 'maxx='+str(maxx))
        print('miny='+str(miny) + 'maxy='+str(maxy))
        filename = '../resources/task20.out.'+str(sec)+'.txt'
        # print_out = input('print out?') != 'n'
        print_out = maxy < 5000 or maxx<5000

        done = False
        if print_out:
            done = True
        if print_out:
            with open(filename, 'w') as r:
                for y in range(miny, maxy+1):
                    printlane=''
                    for x in range(minx, maxx+1):
                        printlane += ( '#' if [x,y] in updated else '.')
                    # print('y=' + str(y) + ' ' +str(len(printlane)))
                    r.write(printlane + '\n')
                    # print(printlane)
                r.close()
        # keep_going = input('continue?') != 'n'
        keep_going = True
        sec +=1
        # if not print_out and done:
        #     keep_going = False








