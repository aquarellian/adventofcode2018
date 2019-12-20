class Player:
    def __init__(self, x, y, type):
        self.hp = 200
        self.x = x
        self.y = y
        self.type = type

from copy import deepcopy


def get_target_locations(player, players, field):
    enemies = [p for p in players if p.type != player.type]
    locations = {}
    for p in enemies:
        locations[p] = []
        x = p.x
        y = p.y
        # enemy detected
        if field[y][x + 1] != 10000000:
            locations[p].append([x + 1, y])
        if field[y][x - 1] != 10000000:
            locations[p].append([x - 1, y])
        if field[y + 1][x] != 10000000:
            locations[p].append([x, y + 1])
        if field[y - 1][x] != 10000000:
            locations[p].append([x, y - 1])
    return locations


def calculate_field(player, players, field):

    my_field = deepcopy(field)
    my_field[player.y][player.x] = 0
    # we can't step on each other
    for p in players:
        if p != player:
            my_field[p.y][p.x] = 10000000

    something_changed = True
    while something_changed:
        something_changed = False
        for y in range(0, len(my_field)):
            for x in range(0, len(my_field[y])):
                current = my_field[y][x]
                if current != 10000000:
                    options = []
                    if my_field[y][x + 1] != -1:
                        options.append(my_field[y][x + 1])
                    if my_field[y][x - 1] != -1:
                        options.append(my_field[y][x - 1])
                    if my_field[y + 1][x] != -1:
                        options.append(my_field[y + 1][x])
                    if my_field[y - 1][x] != -1:
                        options.append(my_field[y - 1][x])
                    if len(options)> 0:
                        suggested = min(options) + 1
                        if current == -1 or current > suggested:
                            something_changed = True
                            my_field[y][x] = suggested
    return my_field


def choose_target(player_field, target_locations):
    reachable_locations = {}
    for enemy, locations in target_locations.items():
        for location in locations:
            dist = player_field[location[1]][location[0]]
            if reachable_locations.get(dist, None) is None:
                reachable_locations[dist] = []
            reachable_locations[dist].append(location)

    min_dist = min(reachable_locations.keys())
    if min_dist < 10000000:
        options = reachable_locations[min_dist]
        options = sorted(options, key=lambda p: p[0]) # sort by x
        options = sorted(options, key=lambda p: p[1]) # sort by y

        return options[0][0], options[0][1]
    else:
        return None, None


def find_victim(player, players):
    enemies = [p for p in players if p.type != player.type]
    options = []
    for enemy in enemies:
        if abs(enemy.x - player.x) + abs(enemy.y - player.y) == 1 and enemy.hp > 0:
            options.append(enemy)

    if len(options) > 0:
        options = sorted(options, key=lambda p: p.x)
        options = sorted(options, key=lambda p: p.y)
        options = sorted(options, key=lambda p: p.hp)
        return options[0]


def discover_nearby(x, y, player_field):
    min_val = min(player_field[y][x - 1], player_field[y][x + 1], player_field[y - 1][x], player_field[y + 1][x])
    paths = []
    if min_val < player_field[y][x]:
        if player_field[y][x - 1] == min_val:
            paths.append([x - 1, y])
        if player_field[y][x + 1] == min_val:
            paths.append([x + 1, y])
        if player_field[y - 1][x] == min_val:
            paths.append([x, y - 1])
        if player_field[y + 1][x] == min_val:
            paths.append([x, y + 1])
    return paths


def find_closest_path(paths, x_from, y_from, x_to, y_to, player_field):
    if x_to != x_from or y_to != y_from:
        paths[(x_to, y_to)] = discover_nearby(x_to, y_to, player_field)
        for coords in paths[(x_to, y_to)]:
            _x_to = coords[0]
            _y_to = coords[1]
            find_closest_path(paths, x_from, y_from, _x_to, _y_to, player_field)
    return paths

def find_coord_to_move_on(player, target_x, target_y, player_field):
    if target_x is None or target_y is None:
        return None, None

    paths = find_closest_path({}, player.x, player.y, target_x, target_y, player_field)
    newx = None
    newy = None

    options = []
    for cfrom, cto in paths.items():
        if [player.x, player.y] in cto:
            options.append(cfrom)

    if len(options) > 0:
        options = sorted(options, key=lambda p: p[0])
        options = sorted(options, key=lambda p: p[1])
        newx = options[0][0]
        newy = options[0][1]

    return newx, newy


def make_move(player, players, field):
    victim = find_victim(player, players)
    if victim is not None:
        victim.hp -= 3
    else:
        player_field = calculate_field(player, players, field)
        target_locations = get_target_locations(player, players, field)
        target_x, target_y = choose_target(player_field, target_locations)
        newx, newy = find_coord_to_move_on(player, target_x, target_y, player_field)
        if newx is not None and newy is not None:
            player.x = newx
            player.y = newy
            victim = find_victim(player, players)
            if victim is not None:
                victim.hp -= 3


def game_over(players):
    ehp = 0
    ghp = 0
    for p in players:
        if p.hp > 0:
            if p.type == 'E':
                ehp += p.hp
            else:
                ghp += p.hp
    over = (ehp == 0) or (ghp == 0)
    score = ehp + ghp
    return over, score

def print_out(players, field):
    upd_field = deepcopy(field)
    hp_out = {}
    for p in players:
        if p.hp > 0:
            upd_field[p.y][p.x] = p.type
            hp_out[p.y] = ' ' + hp_out.get(p.y, '') + p.type + ' ' + str(p.hp) + ' '

    for y in range(0, len(upd_field)):
        line = ''
        for x in range(0, len(upd_field[y])):
            line += '#' if upd_field[y][x] == 10000000 else '.' if upd_field[y][x] == -1 else upd_field[y][x]
        line += hp_out.get(y, '')
        print(line)

with open("../resources/task29.txt") as f:
    content = f.readlines()
    players = []
    id = 0
    field = []
    for y, line in enumerate(content):
        field.append([])
        for x in range(0, len(line)):
            if line[x] == 'E' or line[x] == 'G':
                player = Player(x, y, line[x])
                players.append(player)
                id += 1
                field[y].append(-1)
            elif line[x] == '#':
                field[y].append(10000000)
            elif line[x] == '.':
                field[y].append(-1)


    over, score = game_over(players)
    round = 0
    while not over:
        sorted_players = list(p for p in players if p.hp > 0)
        sorted_players =sorted(sorted_players, key=lambda p: p.x)
        sorted_players =sorted(sorted_players, key=lambda p: p.y)
        print_out(sorted_players, field)
        for ind, p in enumerate(sorted_players):
            if p.hp > 0:
                updated_players = [s for s in sorted_players if s.hp > 0]
                over, score = game_over(updated_players)
                if over:
                    # at least 1 left - current, it havent't moved yet! -> not full round
                    round -=1 # why ?
                    break
                else:
                    make_move(p, updated_players, field)
            if over:
                break
        round +=1
        print(round)
    print_out(sorted_players, field)

    print(round)
    print(score)
    print(round*score)

    # 239057 too high

