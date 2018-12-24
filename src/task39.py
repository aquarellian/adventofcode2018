# line = '^ENWWW(NEEE|SSE(EE|N))$'
# line='^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
line = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'

minx = 0
miny = 0
maxx = 0
maxy = 0

with open("../resources/task39.txt") as f:
    line = f.readline()


def update_boundaries(x1, x2, y1, y2):
    global maxx
    global maxy
    global minx
    global miny
    minx = min(minx, x1, x2)
    maxx = max(maxx, x1, x2)
    miny = min(miny, y1, y2)
    maxy = max(maxy, y1, y2)


ROOM = '.'
WALL = '#'
HOR_DOOR = '-'
VER_DOOR = '|'
the_map = {}
x = 0
y = 0
the_map[x, y] = ROOM
return_points = []
rooms = {0: (0, 0)}
coord_to_rooms = {(0, 0): 0}
roomid = 1
max_doors = 10
for ind in range(1, len(line) - 1):
    if line[ind] == 'E':
        max_doors += 1
        the_map[x + 1, y] = VER_DOOR
        the_map[x + 2, y] = ROOM
        the_map[x + 1, y - 1] = WALL
        the_map[x + 1, y + 1] = WALL
        update_boundaries(x, x + 2, y - 1, y + 1)
        if (x + 2, y) not in coord_to_rooms:
            rooms[roomid] = (x + 2, y)
            coord_to_rooms[x + 2, y] = roomid
            roomid += 1
        x = x + 2
    elif line[ind] == 'W':
        max_doors += 1
        the_map[x - 1, y] = VER_DOOR
        the_map[x - 2, y] = ROOM
        the_map[x - 1, y - 1] = WALL
        the_map[x - 1, y + 1] = WALL
        update_boundaries(x, x - 2, y - 1, y + 1)
        if (x - 2, y) not in coord_to_rooms:
            rooms[roomid] = (x - 2, y)
            coord_to_rooms[x - 2, y] = roomid
            roomid += 1
        x = x - 2
    elif line[ind] == 'N':
        max_doors += 1
        the_map[x, y - 1] = HOR_DOOR
        the_map[x, y - 2] = ROOM
        the_map[x - 1, y - 1] = WALL
        the_map[x + 1, y - 1] = WALL
        update_boundaries(x - 1, x + 1, y, y - 2)
        if (x, y - 2) not in coord_to_rooms:
            rooms[roomid] = (x, y - 2)
            coord_to_rooms[x, y - 2] = roomid
            roomid += 1
        y = y - 2
    elif line[ind] == 'S':
        max_doors += 1
        the_map[x, y + 1] = HOR_DOOR
        the_map[x, y + 2] = ROOM
        the_map[x - 1, y + 1] = WALL
        the_map[x + 1, y + 1] = WALL
        update_boundaries(x - 1, x + 1, y, y + 2)
        if (x, y + 2) not in coord_to_rooms:
            rooms[roomid] = (x, y + 2)
            coord_to_rooms[x, y + 2] = roomid
            roomid += 1
        y = y + 2
    elif line[ind] == '(':
        return_points.append([x, y])
    elif line[ind] == ')':
        del return_points[-1]
    elif line[ind] == '|':
        coord = return_points[-1]
        x = coord[0]
        y = coord[1]

for y in range(miny, maxy + 1):
    line = ''
    for x in range(minx, maxx + 1):
        # print(x,y)
        if the_map.get((x, y), None) is None:
            the_map[x, y] = '#'
        line += the_map[x, y]
    print(line)

# print(the_map)
sorted_rooms = sorted(list(coord_to_rooms.values()))
print(len(sorted_rooms))
lengths = {0: 0}
keep_lurking = True
while keep_lurking:
    keep_lurking = False
    for roomid in sorted_rooms:
        l = lengths.get(roomid, None)
        if l is not None:
            x, y = rooms[roomid]
            # find all neighbors
            if the_map[x + 1, y] == '|':
                other_room = coord_to_rooms[x + 2, y]
                if lengths.get(other_room, max_doors) > l + 1:
                    lengths[other_room] = l + 1
                    keep_lurking = True
            if the_map[x - 1, y] == '|':
                other_room = coord_to_rooms[x - 2, y]
                if lengths.get(other_room, max_doors) > l + 1:
                    lengths[other_room] = l + 1
                    keep_lurking = True
            if the_map[x, y - 1] == '-':
                other_room = coord_to_rooms[x, y - 2]
                if lengths.get(other_room, max_doors) > l + 1:
                    lengths[other_room] = l + 1
                    keep_lurking = True
            if the_map[x, y + 1] == '-':
                other_room = coord_to_rooms[x, y + 2]
                if lengths.get(other_room, max_doors) > l + 1:
                    lengths[other_room] = l + 1
                    keep_lurking = True

#task1
print(max(lengths.values()))

#task2
over1000 = [x for x in lengths.values() if x >= 1000]
print(len(over1000))
#8520
