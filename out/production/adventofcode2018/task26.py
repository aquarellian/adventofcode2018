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
    # print('cart ', str(cart), ' ', str([x,y]), ' turned ', dir, ' to ', new_symb, ' onto ', track[y][x])
    return new_symb


def make_move(carts, cartid, track):
    symb = carts[cartid][2]
    x = carts[cartid][0]
    y = carts[cartid][1]
    if symb == '>':
        if track[y][x + 1] == '-':
            return x + 1, y, symb
        elif track[y][x + 1] == '/':
            return x+1, y, '^'
        elif track[y][x + 1] == '\\':
            return x+1, y, 'v'
        elif track[y][x + 1] == '+':
            symb = make_turn(carts, cartid)
            return x + 1, y, symb
        else:

            print_out(track, carts, -1)
            print(track[y][x + 1])
            print(carts[cartid])
            print('ERROR1')
    elif symb == '<':
        if track[y][x - 1] == '-':
            return x - 1, y, symb
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
    elif symb == '^':
        if track[y - 1][x] == '|':
            return x, y - 1, symb
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
    elif symb == 'v':
        if track[y + 1][x] == '|':
            return x, y + 1, symb
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


def is_cart_there(carts, x, y):
    for crt, val in carts.items():
        if val[0] == x and val[1] == y:
            return True
    return False


def is_hor_road(track, x, y):
    if y == 0 or y == len(track)-1:
        return True
    elif track[y][x] in ['>', '<']:
        return track[y-1][x] not in ['|', '+'] and track[y+1][x] not in ['|', '+']
    i = 0
    while x - i > 0 and (is_cart_there(carts, x-i, y) or track[y][x-i] == '+'):
        i += 1
    road_on_left = ((x + i) >= 0) and track[y][x - i] == '-'
    i = 0
    while x + i < len(track[y]) and (is_cart_there(carts, x+i, y) or track[y][x+i] == '+'):
        i += 1
    road_on_right = ((x + i) < len(track[y])) and track[y][x + i] == '-'
    return road_on_left and road_on_right


def is_ver_road(track, x, y):
    if x == 0 or x == len(track[y])-1:
        return True
    elif track[y][x] in ['^', 'v']:
        return track[y][x-1] not in ['-', '+'] and track[y][x+1] not in ['|', '+']
    i = 0
    while y - i >= 0 and (is_cart_there(carts, x, y-i) or track[y-i][x] == '+'):
        i += 1
    road_on_left = (y - i >= 0) and track[y - i][x] == '-'
    i = 0
    while y + i < len(track) and (is_cart_there(carts, x, y+i) or track[y+i][x] == '+'):
        i += 1
    road_on_right = (y + i < len(track)) and track[y][x + i] == '|'
    return road_on_left and road_on_right


def print_out(track, carts, i):
    with open("../resources/task26." + str(i) + ".txt", 'w') as f:
        for y in range(0, len(track)):
            strng = ''
            for x in range(0, len(track[y])):
                rd = track[y][x]
                for cart, val in carts.items():
                    cx = val[0]
                    cy = val[1]
                    if cx == x and cy == y:
                        rd = val[2]
                strng += rd
            f.write(strng + '\n')


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
            if track[y][x] in ['v', '^', '<', '>']:
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
    ind = 1
    print_out(track, {}, -2)
    print_out(track, carts, 0)

    print(len(sorted_carts))
    additional = True
    while len(sorted_carts) > 1:
        # sorted_carts = sorted(sorted_carts, key=operator.itemgetter(1, 2))
        sorted_carts = sorted(sorted_carts, key=lambda x: (carts[x][0], carts[x][1]))
        # sorted_carts = sorted(sorted_carts, key=lambda cart: carts[cart][0])
        # sorted_carts = sorted(sorted_carts, key=lambda cart: carts[cart][1])
        crashed = set()
        for cart in sorted_carts:
            if cart in crashed:
                continue
            x, y, dir = make_move(carts, cart, track)
            # print('cart ', str(cart), ' moved from ', carts[cart], ' to ', str([x,y,dir]), ' onto ', track[y][x])

            carts[cart] = [x, y, dir]

            for crt in sorted_carts:
                if crt != cart and carts[crt][0] == carts[cart][0] and carts[crt][1] == carts[cart][1] \
                        and crt not in crashed and cart not in crashed:
                    print('Crashed ', crt, carts[crt], cart, carts[cart])
                    crashed.add(crt)
                    crashed.add(cart)
        if len(crashed) > 0:
            print('Crashed ', crashed)
            for c in crashed:
                sorted_carts.remove(c)
                del carts[c]
                # carts.remove(c)
            print(sorted_carts)

        if ind > 17710:
            print_out(track, carts, ind)

        ind+=1
    # print(sorted_carts)
    print(ind)
    print_out(track, carts, ind)
    print(carts[sorted_carts[0]])

# 135, 83 wrong
# 135, 82 wrong
# 135, 84 wrong



