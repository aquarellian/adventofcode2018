def make_turn(carts, cart):
    data = carts[cart]
    x = data[0]
    y = data[1]
    dir = data[2]
    new_symb = ''
    if turns[cart] == -1:
        if dir == '>':
            new_symb = '^'
        elif dir == '<':
            new_symb = 'v'
        elif dir == '^':
            new_symb = '<'
        elif dir == 'v':
            new_symb = '>'
    elif turns[cart] == 0:
        new_symb = dir
    elif turns[cart] == 1:
        if dir == '>':
            new_symb = 'v'
        elif dir == '<':
            new_symb = '^'
        elif dir == '^':
            new_symb = '>'
        elif dir == 'v':
            new_symb = '<'

    turns[cart] = (turns[cart] + 1 if turns[cart] < 1 else -1)
    print('cart ' + str(cart) + ' turned ' + dir + ' to ' + new_symb)
    return new_symb


def make_move(carts, cartid, track):
    cart = carts[cartid][2]
    x = carts[cartid][0]
    y = carts[cartid][1]
    if cart == '>':
        if track[y][x + 1] == '-':
            return x + 1, y, cart
        elif track[y][x + 1] == '/':
            return x+1, y, '^'
        elif track[y][x + 1] == '\\':
            return x+1, y, 'v'
        elif track[y][x + 1] == '+':
            symb = make_turn(carts, cartid)
            return x + 1, y, symb
        else:

            print_out(track, carts)
            print(track[y][x + 1])
            print(carts[cartid])
            print('ERROR1')
    elif cart == '<':
        if track[y][x - 1] == '-':
            return x - 1, y, cart
        elif track[y][x - 1] == '/':
            return x-1, y, 'v'
        elif track[y][x - 1] == '\\':
            return x-1, y, '^'
        elif track[y][x - 1] == '+':
            symb = make_turn(carts, cartid)
            return x - 1, y, symb
        else:
            print(track[y][x - 1])
            print('ERROR2')
    elif cart == '^':
        if track[y - 1][x] == '|':
            return x, y - 1, cart
        elif track[y - 1][x] == '/':
            return x, y-1, '>'
        elif track[y - 1][x] == '\\':
            return x, y-1, '<'
        elif track[y - 1][x] == '+':
            symb = make_turn(carts, cartid)
            return x, y-1, symb
        else:
            print(track[y-1][x])
            print('ERROR3')
    elif cart == 'v':
        if track[y + 1][x] == '|':
            return x, y + 1, cart
        elif track[y + 1][x] == '/':
            return x, y+1, '<'
        elif track[y + 1][x] == '\\':
            return x, y+1, '>'
        elif track[y + 1][x] == '+':
            symb = make_turn(carts, cartid)
            return x, y+1, symb
        else:
            print(track[y+1][x])
            print('ERROR4')


def is_cart(symbol):
    return symbol in ['>', '<', '^', 'v']


def is_hor_road(track, x, y):
    i = 0
    while x - i > 0 and is_cart(track[y][x - i]):
        i += 1
    road_on_left = ((x + i) >= 0) and track[y][x - i] == '-'
    i = 0
    while x + i < len(track[y]) and is_cart(track[y][x + i]):
        i += 1
    road_on_right = ((x + i) < len(track[y])) and track[y][x + i] == '-'
    return road_on_left and road_on_right


def is_ver_road(track, x, y):
    i = 0
    while y - i >= 0 and is_cart(track[y - i][x]):
        i += 1
    road_on_left = (y - i >= 0) and track[y - i][x] == '-'
    i = 0
    while y + i < len(track) and is_cart(track[y + i][x]):
        i += 1
    road_on_right = (y + i < len(track)) and track[y][x + i] == '|'
    return road_on_left and road_on_right

def print_out(track, carts):
    import copy
    new_track = copy.deepcopy(track)
    for cart, val in carts.items():
        x = val[0]
        y = val[1]
        dir = val[2]
        new_track[y][x] = dir
    for y in range(0, len(new_track)):
        str = ''
        for x in range(0, len(new_track[y])):
            str += new_track[y][x]
        print(str)


with open("../resources/task25.txt") as f:
    content = f.readlines()
    carts = {}
    sorted_carts = []
    turns = {}
    cartid = 0
    track = []
    for y, line in enumerate(content):
        track.append([])
        for x in range(0, len(line.replace('\n', ''))):
            track[y].append(line[x])
            if is_cart(track[y][x]):
                carts[cartid] = [x, y, track[y][x]]
                turns[cartid] = -1
                cartid += 1
    sorted_carts = list(carts.keys())

    for cart in sorted_carts:
        coord = carts[cart]
        x = coord[0]
        y = coord[1]
        if is_hor_road(track, x, y):
            if is_ver_road(track, x, y):
                track[y][x] = '+'
            else:
                track[y][x] = '-'
        else:
            track[y][x] = '|'

    crashed = False
    while not crashed:
        sorted(sorted_carts, key=lambda cart: carts[cart][1])
        sorted(sorted_carts, key=lambda cart: carts[cart][0])
        for cart in sorted_carts:
            # print(track)
            # print(carts)
            # print(carts[cart])
            x, y, dir = make_move(carts, cart, track)
            for crt, val in carts.items():
                if val[0] == x and val[1] == y and crt != cart:
                    crashed = True
                    print([x, y])
                    break
                carts[cart] = [x, y, dir]
            if crashed:
                break
        print_out(track, carts)





