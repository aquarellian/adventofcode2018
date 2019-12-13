import opcode
import load_input
content = load_input.load(2019, 13).split(',')
amp = opcode.Amplifier(content)
res = amp.apply(None)
print(res)

tilesN = 0
tiles = {}
x = None
y = None
for ind, val in enumerate(res):
    rem = ind % 3
    if rem == 0:
        tiles[val] = tiles.get(val, {})
        x = val
    elif rem == 1:
        tiles[x][val] = tiles[x].get(val, {})
        y = val
    elif rem == 2:
        tile = ' ' if val == 0 else '#' if val == 1 else '*' if val == 2 else '_' if val == 3 else 'O' if val == 4 else 'WTF'
        if val == 2:
            tilesN += 1
        tiles[x][y] = tile
        x = None
        y = None

print(tilesN)

for y in range(0, max(tiles[0].keys()) + 1):
    line = ''
    for x in tiles.keys():
        line += tiles[x][y]
    print(line)
