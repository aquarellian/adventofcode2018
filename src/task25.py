def do_turn(x,y):

    for key, value in carts.items():
        if value == [x,y]:
            cartid = key
            turn = turns[cartid]
            turns[cartid] = (turn + 1 if turn < 1 else -1)

            if turn == -1:
                if track[y][x] == '>':
                    new_symb = '^'
                elif track[y][x] == '<':
                    new_symb = 'v'
                elif track[y][x] == '^':
                    new_symb = '<'
                elif track[y][x] == 'v':
                    new_symb = '>'
            elif turn == 0:
                new_symb = track[y][x]
            elif turn == 1:
                if track[y][x] == '>':
                    new_symb = 'v'
                elif track[y][x] == '<':
                    new_symb = '^'
                elif track[y][x] == '^':
                    new_symb = '>'
                elif track[y][x] == 'v':
                    new_symb = '<'




def do_move():


def is_cart(track, x, y):
    return track[y][x] in ['>', '<', '^', 'v']

def is_hor_road(track, x, y):
    i = 0
    while x-i >= 0 and is_cart(track, x-i, y):
        i+=1
    road_on_left = track[y][x-i] == '-'
    i = 0
    while x+i <= len(track[y]) and is_cart(track, x+i, y):
        i+=1
    road_on_right = track[y][x+i] == '-'
    return road_on_left and road_on_right

def is_ver_road(track, x, y):
    i = 0
    while y-i >= 0 and is_cart(track, x, y-i):
        i+=1
    road_on_left = track[y-i][x] == '-'
    i = 0
    while y+i <= len(track) and is_cart(track, x, y+1):
        i+=1
    road_on_right = track[y][x+i] == '|'
    return road_on_left and road_on_right


with open("../resources/task23.txt") as f:
    content = f.readlines()
    carts = {}
    turns = {}
    cartid = 0
    track = {}
    for y, line in enumerate(track):
        for x in range(0, len(line)):
            if track.get(x, None) is None:
                track[x] = {}
            track[x][y] = line[x]

    for x in track.keys():
        for y in track[x].keys():
             if is_cart(track, x, y):
                carts[cartid] = [x,y]
                turns[cartid] = -1
                if is_hor_road(track, x, y):
                    if is_ver_road(track, x,y):
                        line.[x] = '+'
                    else :
                        line[x] = ''
                # now we replace cart with corresponding track
                if track[y-1][x] == '|' and track[y+1][x] == '|':
                    if track[y][x-1] == track[y][x-1]
                        line[x] =
    for y, line in enumerate(track):
        for x in range(0, len(line)):
            if '+' == line[x]:
                do_turn()



