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
    closest_enemy = None
    closest_enemy_x = None
    closest_enemy_y = None

    for enemy, location in target_locations.items():
        for coord in location:
            target_x = coord[0]
            target_y = coord[1]
            if closest_enemy is None \
                    or player_field[closest_enemy_y][closest_enemy_x] > player_field[target_y][target_x] \
                    or player_field[closest_enemy_y][closest_enemy_x] == player_field[target_y][target_x] and (
                    enemy.y < closest_enemy.y or enemy.y == closest_enemy.y and enemy.x < closest_enemy.x):
                closest_enemy = enemy
                closest_enemy_x = target_x
                closest_enemy_y = target_y
    return closest_enemy


def find_victim(player, players):
    enemies = [p for p in players if p.type != player.type]
    enemy_to_attack = None
    for enemy in enemies:
        if abs(enemy.x - player.x) + abs(enemy.y - player.y) == 1:
            if enemy_to_attack is None or enemy_to_attack.hp > enemy.hp or (
                    enemy.y < enemy_to_attack.y or enemy.x < enemy_to_attack.x):
                enemy_to_attack = enemy
    return enemy_to_attack


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

def find_coord_to_move_on(player, target, player_field):
    if target is None:
        return None, None

    paths = find_closest_path({}, player.x, player.y, target.x, target.y, player_field)
    newx = None
    newy = None

    for cfrom, cto in paths.items():
        if [player.x, player.y] in cto:
            if (newx is None and newy is None) or newy > cfrom[1] or newy == cfrom[1] and newx > cfrom[0]:
                newx = cfrom[0]
                newy = cfrom[1]
    return newx, newy


def make_move(player, players, field):
    victim = find_victim(player, players)
    if victim is not None:
        victim.hp -= 3
    else:
        player_field = calculate_field(player, players, field)
        target_locations = get_target_locations(player, players, field)
        closest_enemy = choose_target(player_field, target_locations)
        newx, newy = find_coord_to_move_on(player, closest_enemy, player_field)
        if newx is not None and newy is not None:
            player.x = newx
            player.y = newy


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
    for p in players:
        upd_field[p.y][p.x] = p.type

    for y in range(0, len(upd_field)):
        line = ''
        for x in range(0, len(upd_field[y])):
            line += '#' if upd_field[y][x] == 10000000 else '.' if upd_field[y][x] == -1 else upd_field[y][x]
        print(line)

with open("../resources/task29.test.txt") as f:
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
        round +=1
        sorted_players = list(p for p in players if p.hp > 0)
        sorted_players =sorted(sorted_players, key=lambda p: p.x)
        sorted_players =sorted(sorted_players, key=lambda p: p.y)
        for p in sorted_players:
            if len([pl for pl in sorted_players if pl.type != p.type]) == 0:
                break
            make_move(p, sorted_players, field)
            print_out(sorted_players, field)
        over, score = game_over(sorted_players)
        print(round)

    print(round)
    print(score)

