def calculate_filed(id, field, friends, enemies, players):
    for p in players:
        data = players[p]
        x = data[0]
        y = data [1]
        field[y][x] = 10000000
    targets = {}
    for e, coord in enemies.items():
        if

    data = players[id]
    x = data[0]
    y = data[1]
    filled = False
    field[y][x] = 0
    while not filled:
        for i in range(0, len(field)):
            for j in range(0, len(field[i])):
                if x - j >= 0 and y - i >=0:
                    field[y-i][x-j] =


    for enemy in enemies:
        data = players[friend]
        ex = data[0]
        ey = data[1]




with open("../resources/task29.txt") as f:
    content = f.readlines()
    players = {}
    ehp = {}
    ghp = {}
    id = 0
    field = []
    for y, line in enumerate(content):
        field.append([])
        for x in range(0, len(line)):
            if line[x] == 'E' or line[x] == 'G':
                players[id] = [x,y, line[x]]
                if line[x] == 'E':
                    ehp[id] = 200
                else:
                    ghp[id] = 200
                id +=1
                field[y][x] = -1
            elif line[x] == '#':
                field[y][x] = 10000000
            elif line[x] == '.':
                field[y][x] = -1

    game_over = False
    while not game_over:
        sorted_all = list(p for p in players.keys() if ehp.get(p, 0) > 0 or ghp.get(p, 0) > 0)
        sorted(sorted_all, key=lambda p: (players[p][0], players[p][1]))
        for id in sorted_all:
            my_field = calculate_filed()
            closest_enemy = find_closest_enemy()
            if combat:
                enemy = chose_enemy();
                fight()
            else:
                move_towards_enemy()

