import load_input
content = load_input.load(2019, 10).split('\n')
total_count = 0
# content = '.#..#\n.....\n#####\n....#\n...##\n'.split('\n')
# content = '......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####\n'.split('\n')
# content= '#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##..\n..##....##\n......#...\n.####.###.\n'.split('\n')
# content='.#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#..\n'.split('\n')
# content='.#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##\n'.split('\n')



def nod(a,b):
    for i in range(abs(min(a,b)) + 1, 0, -1):
        print(a, b, i)
        if abs(a % i) == 0 and abs(b % i) == 0:
            if (a == -3 and b == -3):
                print('nod', i)
            return i
    return None


def lin(x1, x2, y1, y2):
    if x1 == x2:
        return None
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b


def unlink(a,b):
    if b in a.accessible:
        a.accessible.remove(b)
    if a in b.accessible:
        b.accessible.remove(a)


def same_point(_x, _y, a):
    return _x == a.x and _y == a.y


def found_other_asteroid(content, a, b, _x, _y):
    return content[int(_y)][_x] == '#' and not same_point(_x, _y, a) and not same_point(_x, _y, b)

# def clock_comparator(less_than):
#     def compare(x, y):
#         if less_than(x, y):
#             return -1
#         elif less_than(y, x):
#             return 1
#         else:
#             return 0
#     return compare
#
# sortedDict = sorted(subjects, cmp=make_comparator(cmpValue), reverse=True)

class Asteroid:
    x = 0
    y = 0
    accessible = None
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(slf.y) + ']'

asteroids = []


h = len(content) -1
w = len(content[0])
for i, c in enumerate(content):
    print(c)
    for j, s in enumerate(c):
        if s == '#':
            asteroids.append(Asteroid(j, i))
            # print(j, i)


print(len(asteroids))
# print(asteroids)
amax = None
for a in asteroids:
    a.accessible = set(asteroids)
    a.accessible.remove(a)
    # for b in list(a.accessible):
    for b in asteroids:
        if b.accessible is None:
            b.accessible = set(asteroids)
            b.accessible.remove(b)
        if a.x != b.x and a.y != b.y:
            k, d = lin(a.x, b.x, a.y, b.y)
            for _x in range(min(a.x, b.x), max(a.x, b.x)+1):
                y = k * _x + d
                _y = int(y)

                # if 0 < abs(_y - y) < 0.01 and found_other_asteroid(content, a, b, _x, _y):
                #     print(_y - y)
                if abs(_y - y) < 0.0454505 and found_other_asteroid(content, a, b, _x, _y):
                    unlink(a, b)
        elif a.x != b.x:
            _y = a.x
            for _x in range(min(a.x, b.x), max(a.x, b.x)+1):
                if found_other_asteroid(content, a, b, _x, _y):
                    unlink(a, b)
        else:
            _x = a.x
            for _y in range(min(a.y, b.y), max(a.y, b.y)+1):
                if found_other_asteroid(content, a, b, _x, _y):
                    unlink(a, b)

        # if a.x != b.x:
        #     if a.y == b.y:
        #         _y = a.x
        #         for _x in range(min(a.x, b.x), max(a.x, b.x)+1):
        #             if content[int(_y)][_x] == '#' and not same_point(_x, _y, a) and not same_point(_x, _y, b):
        #                 unlink(a, b)
        #     else:
        #         k, d = lin(a.x, b.x, a.y, b.y)
        #         for _x in range(min(a.x, b.x), max(a.x, b.x)+1):
        #             y = k * _x + d
        #             _y = int(y)
        #             if _y == y and content[int(_y)][_x] == '#'  and not same_point(_x, _y, a) and not same_point(_x, _y, b):
        #                 unlink(a, b)
        # else:
        #     _x = a.x
        #     for _y in range(min(a.y, b.y), max(a.y, b.y)+1):
        #         if content[int(_y)][_x] == '#' and not same_point(_x, _y, a) and not same_point(_x, _y, b):
        #             unlink(a, b)

    if amax is None or len(a.accessible) > len(amax.accessible):
        amax = a
print(len(amax.accessible))
print(amax.x, amax.y)

station = None
for a in asteroids:
    if len(a.accessible) == 280 or len(a.accessible) == 281:
        station = a
        # print(a.x, a.y)
        print(a.x, a.y, len(a.accessible))

right_up = [a for a in station.accessible if a.x >= station.x and a.y >= station.y]
right_down = [a for a in station.accessible if a.x >= station.x and a.y < station.y]
left_down = [a for a in station.accessible if a.x < station.x and a.y <= station.y]


print(len(right_up) + len(right_down)+ len(left_down))
left_up = [a for a in station.accessible if a.x < station.x and a.y > station.y]
print(len(left_up))

left_up = sorted(left_up, key = lambda a:(a.y, a.x))
# left_up = sorted(left_up, key=comparator)
# left_up.sort(comparator)
print(200 - len(right_up) - len(right_down) - len(left_down))
a200 = left_up[24]
print(a200.x * 100 + a200.y)
a200 = left_up[25]
print(a200.x * 100 + a200.y)
a200 = left_up[26]
print(a200.x * 100 + a200.y)

res = []
for a200 in left_up:
    if a200.x * 100 + a200.y < 1116:
        res.append(a200.x * 100 + a200.y)
print(sorted(res))



#447 too high
#288 too high
# 280 ok


#part2
#1516 too high
#1216 too high
#1116 too high
#1115 wrong










