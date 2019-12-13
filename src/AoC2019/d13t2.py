def parse_game(res):
    tiles = {}
    x = 0
    y = 0
    for ind, val in enumerate(res):
        rem = ind % 3
        if rem == 0:
            x = val
        elif rem == 1:
            y = val
        elif rem == 2:
            tile = ' ' if val == 0 else '#' if val == 1 else '*' if val == 2 else '_' if val == 3 else 'O' if val == 4 else 'WTF'
            tiles[y] = tiles.get(y, {})
            tiles[y][x] = tile
            x = None
            y = None
    return tiles


def print_field(field):
    for y in field.keys():
        line = ''
        for x in field[y].keys():
            line += field[y][x]
        print(line)


def update_field(field, upd):
    ball_x, base_x = None, None
    score = 0
    for ind, val in enumerate(upd):
        rem = ind % 3
        if rem == 0:
            x = val
        elif rem == 1:
            y = val
        elif rem == 2:
            if x == -1 and y == 0:
                score = val
            else:
                tile = ' ' if val == 0 else '#' if val == 1 else '*' if val == 2 else '_' if val == 3 else 'O' if val == 4 else 'WTF'
                if val == 4:
                    ball_x = x
                elif val == 3:
                    base_x = x
                field[y] = field.get(y, {})
                field[y][x] = tile
            x = None
            y = None
    if ball_x is None or base_x is None or ball_x == base_x:
        return 0, score
    elif ball_x > base_x:
        return 1, score
    elif ball_x < base_x:
        return -1, score


import opcode
import load_input


content = load_input.load(2019, 13).split(',')
amp = opcode.Amplifier(content)
res = amp.apply(None)
field = parse_game(res)

content[0] = 2
amp = opcode.Amplifier(content)
signal = 0
score = 0
while not amp.halted:
    upd = amp.apply(signal)
    if len(upd) == 0:
        break
    signal, score = update_field(field, upd)
    print_field(field)
print(score)


