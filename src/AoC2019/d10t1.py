import load_input
# content = load_input.load(2019, 10).split('\n')
total_count = 0
content = '.#..#\n.....\n#####\n....#\n...##\n'.split('\n')

def nod(a,b):
    for i in range(min(a,b)+1, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return None


class Asteroid:
    x = 0
    y = 0
    accessible = set()
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(slf.y) + ']'

asteroids = []


h = len(content) -1
w = len(content[0])
for i, c in enumerate(content):
    for j, s in enumerate(c):
        if s == '#':
            asteroids.append(Asteroid(j, i))


print(len(asteroids))
# print(asteroids)
amax = None
for a in asteroids:
    a.accessible = set(asteroids)
    # a.accessible.remove(a)
    for b in asteroids:
        if a != b:
            dx = a.x - b.x
            dy = a.y - b.y
            _nod = nod(dx, dy)
            if _nod is not None:
                dx = dx // _nod
                dy = dy // _nod
            ax = a.x
            ay = a.y
            ok = False
            while 0 <= ax - dx < w and 0 <= ay - dy < h and not ok:
                ax = ax - dx
                ay = ay - dy
                if ax != a.x and ay != a.y and content[ay][ax] == '#':
                    if ax == b.x and ay == b.y:
                        ok = True
                        break # b accessible from a
                    else:
                        break
            ax = a.x
            ay = a.y
            while 0 <= ax + dx < w and 0 <= ay + dy < h and not ok:
                ax = ax + dx
                ay = ay + dy
                if ax != a.x and ay != a.y and content[ay][ax] == '#':
                    if ax == b.x and ay == b.y:
                        ok = True
                        break # b accessible from a
                    else:
                        break

            if not ok:
                a.accessible.remove(b)
    if amax is None or len(a.accessible) > len(amax.accessible):
        amax = a
print(len(amax.accessible))
print(amax.x, amax.y)
#447 too high











