import re
import load_input
content = load_input.load(2019, 18).split('\n')

lmap = {}
entx, enty = None, None
keys = {}
doors = {}
for y in range(0, len(content)):
    lmap[y] = {}
    for x in range(0, len(content[y])):
        symbol = content[y][x]
        lmap[y][x] = symbol
        if symbol == '@':
            entx = x
            enty = y
        elif re.match("[A-Z]", symbol):
            doors[symbol] = [x, y]
        elif re.match("[a-z]", symbol):
            keys[symbol] = [x, y]


