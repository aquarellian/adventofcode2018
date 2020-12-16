# task 1
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d12.txt") as f:
    content = f.readlines()
    x = 0
    y = 0
    dir = 'E'
    dirind = 1
    dirs = 'NESW'
    for line in content:
        cmd = line[0]
        num = int(line[1:len(line)])
        if cmd == 'F':
            cmd = dirs[dirind]
        if cmd == 'N':
            y -= num
        elif cmd == 'E':
            x += num
        elif cmd == 'W':
            x -= num
        elif cmd == 'S':
            y += num
        elif cmd == 'L':
            dirind = (dirind - int(num / 90)) % 4
        elif cmd == 'R':
            dirind = (dirind + int(num / 90)) % 4
    print(abs(x) + abs(y))

# task 2
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d12.txt") as f:
    content = f.readlines()
x = 0
y = 0
wx = 10
wy = -1
dirx = 1
diry = 0
dirs = 'NESW'
for line in content:
    cmd = line[0]
    num = int(line[1:len(line)])
    rotate = False
    if cmd == 'F':
        x += num * wx
        y += num * wy
    elif cmd == 'N':
        wy -= num
    elif cmd == 'E':
        wx += num
    elif cmd == 'W':
        wx -= num
    elif cmd == 'S':
        wy += num
    elif cmd == 'L' or cmd == 'R':
        if abs(num % 360) == 0:
            continue
        elif abs(num % 180) == 0:
            wx = -wx
            wy = -wy
        elif (num % 360 == 90 or num % 360 == -270) and cmd == 'R' or \
                (num % 360 == -90 or num % 360 == 270) and cmd == 'L':
            tmp = wy
            wy = wx
            wx = -tmp
        elif (num % 360 == 90 or num % 360 == -270) and cmd == 'L' or \
                (num % 360 == -90 or num % 360 == 270) and cmd == 'R':
            tmp = wy
            wy = -wx
            wx = tmp
        else:
            print('wtf?')

        if cmd == 'L':
            dirx = ((dirx - int(num / 90)) % 4) if cmd == 'L' else (dirx + int(num / 90)) % 4
            diry = ((diry - int(num / 90)) % 4) if cmd == 'L' else (diry + int(num / 90)) % 4

print(x, y)
print(abs(x) + abs(y))
