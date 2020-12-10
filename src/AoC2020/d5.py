def calc(minv, maxv, up):
    middle = (maxv - minv + 1) / 2
    return (minv + middle, maxv) if up else (minv, minv + middle - 1)

arr = [[None for x in range(8)] for y in range(128)]

with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d5.txt") as f:
    lines = f.readlines()

    # lines = ('FBFBBFFRLR', 'FBBBBFFRLR')
    maxres = 0
    for line in lines:
        minx = 0
        maxx = 7
        miny = 0
        maxy = 127
        for i in range(0,10):
            ch = line[i]
            if ch == 'F':
                (miny, maxy) = calc(miny, maxy, False)
                # print(miny, maxy, minx, maxx, minx * miny)
            elif ch == 'B':
                (miny, maxy) = calc(miny, maxy, True)
                # print(miny, maxy, minx, maxx, minx * miny)
            elif ch == 'R':
                (minx, maxx) = calc(minx, maxx, True)
                # print(miny, maxy, minx, maxx, minx * miny)
            elif ch == 'L':
                (minx, maxx) = calc(minx, maxx, False)
                # print(miny, maxy, minx, maxx, minx * miny)
            else:
                print(miny, maxy, minx, maxx, minx * miny)
        res = minx + miny*8
        arr[int(miny)][int(minx)] = res
        if maxres < res:
            maxres = res
        print(miny, maxy, minx, maxx, res, maxres)
    print (maxres)
    for i in range(1, len(arr) -1):
        print(arr[i])
        # for j in range(1, len(arr[i]) - 1):
        #     if arr[i-1][j] is not None and \
        #             arr[i+1][j] is not None and \
        #             arr[i][j-1] is not None and \
        #             arr[i][j+1] is not None:
        #          print(j, i, arr[i][j])
