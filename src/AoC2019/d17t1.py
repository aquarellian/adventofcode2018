import load_input
import opcode
content = load_input.load(2019, 17).split(',')
_map = {}
ind = 0
line = ''
amp = opcode.Amplifier(content)
while not amp.halted:

    v = amp.apply(None)

    if v == 35:
        line += '#'
    elif v == 46:
        line += '.'
    elif v == 10:
        _map[ind] = line
        line = ''
        ind += 1
    else:
        print('unknown symbol')

res = 0
for i in range(max(_map.keys()) + 1):
    line = _map[i]
    for j in range(len(line)):
        if line[j] == '#' and 0 < j < len(line) - 1 and 0 < i < max(_map.keys()) and line[j-1] == '#' and line[j+1] == '#' and  _map[i-1][j] == '#' and _map[i+1][j]== '#':
            res += i*j
print(res)


