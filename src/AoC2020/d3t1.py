class slope:
    x = 0
    y = 0
    cnt = 0
    dx = 0
    dy = 0

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def check(self, ch):
        if ch == '#':
            self.cnt += 1
        self.x = self.x + self.dx
        self.y = self.y + self.dy

def testSlope(slope1):
    while slope1.y < len(content):
        slope1.check(content[slope1.y][slope1.x % len(content[slope1.y])])
    return slope1.cnt


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d3.txt") as f:
    content = f.read().split('\n')
    res = testSlope(slope(1, 1)) * \
    testSlope(slope(3, 1)) * \
    testSlope(slope(5, 1)) * \
    testSlope(slope(7, 1)) * \
    testSlope(slope(1, 2))
    print(res)
    # while slope1.y < len(content):
    #     slope1.check(content[slope1.y][slope1.x % len(content[slope1.y])])
    # print(slope1.cnt)

