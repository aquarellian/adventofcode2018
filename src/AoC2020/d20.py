class Tile:
    id = None
    tile = None
    up = None
    down = None
    left = None
    right = None

    def __init__(self, id, tile):
        self.id = id
        self.tile = tile

    def borders(self):
        up = [x for x in self.tile[0]]
        down = [x for x in self.tile[-1]]
        left = []
        right = []
        for i in range(len(self.tile)):
            left.append(self.tile[i][0])
            right.append(self.tile[i][-1])
        return up, down, left, right

    def match(self, tile):
        up, down, left, right = self.borders()
        other = [x for x in tile.borders()]

        # reversed_other = []
        #
        # reversed_other.append([x for x in [reversed(y) for y in other]])
        # reversed_other = [x.reverse() for x in other]
        other += [x[::-1] for x in other]
        if up in other:
            self.up = tile.id
        elif down in other:
            self.down = tile.id
        elif left in other:
            self.left = tile.id
        elif right in other:
            self.right = tile.id

    def is_corner(self):
        return int(self.up is None) + int(self.down is None) + int(self.left is None) + int(self.right is None) == 2


def fill_matrix(matrix, tile, posx, posy):



with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d20.txt") as f:
    content = f.readlines()
    map = dict()
    arr = []

    id = None
    for line in content:
        if line.strip() == "":
            continue
        if line.startswith('Tile'):
            if not id is None:
                map[id] = Tile(id, arr)
            id = int(line.strip()[5:-1])
            arr = []
        else:
            row = list(line.strip())
            arr.append(row)
    map[id] = Tile(id, arr)

    for i in map.keys():
        for j in map.keys():
            if i != j:
                map[i].match(map[j])
    v = 1

    corner = None
    for i in map.keys():
        if map[i].is_corner():
            v *= i
        if map[i].up is None and map[i].left is None:
            corner = i
    print(v)

    lng = 3 * 8
    # lng = 12 * 8 # res
    matrix = [['' for x in range(lng)] for y in range(lng)]
    new_tiles = [corner]
    while len(new_tiles) > 0:
        matrix[i]
        matrix[0]



