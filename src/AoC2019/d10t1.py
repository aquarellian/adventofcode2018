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
    for b in list(a.accessible):
        if b.accessible is None:
            b.accessible = set(asteroids)
            b.accessible.remove(b)
        if a.x != b.x:
            k, d = lin(a.x, b.x, a.y, b.y)
            for _x in range(min(a.x, b.x), max(a.x, b.x)+1):
                y = k * _x + d
                _y = int(y)
                if _y == y and content[int(_y)][_x] == '#' and b in a.accessible and not (_y == b.y and _x == b.x) and not (_y == a.y and _x == a.x):
                    # found something in between - removing b from available to a and vice versa
                    a.accessible.remove(b)
                    b.accessible.remove(a)
        else:
            _x = a.x
            for _y in range(min(a.y, b.y), max(a.y, b.y)+1):
                if content[int(_y)][_x] == '#' and b in a.accessible and not (_y == b.y and _x == b.x)  and not (_y == a.y and _x == a.x):
                    # found something in between - removing b from available to a and vice versa
                    a.accessible.remove(b)
                    if a in b.accessible
                    b.accessible.remove(a)

    if amax is None or len(a.accessible) > len(amax.accessible):
        amax = a
print(len(amax.accessible))
print(amax.x, amax.y)
# for a in asteroids:
#     if len(a.accessible) == 280:
#         # print(a.x, a.y)
#         print(a.x, a.y, len(a.accessible))
#447 too high
#288 too high
# 280 ok










