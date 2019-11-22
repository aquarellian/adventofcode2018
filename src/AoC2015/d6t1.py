import load_input
content = load_input.load(2015, 6)
# content = 'turn on 0,0 through 5,5\nturn off 1,1 through 4,4\ntoggle 2,2 through 3,3'
import re

map = {}
count = 0
max = 999

for line in content.split('\n'):
    cmd = re.split('\W', line)
    if len(cmd) < 5:# EOF
        break
    v = None
    x1 = None
    x2 = None
    y1 = None
    y2 = None
    if cmd[0] == 'turn':
        x1 = int(cmd[2])
        y1 = int(cmd[3])
        x2 = int(cmd[5])
        y2 = int(cmd[6])
        if cmd[1] == 'on':
            v = 1
        elif cmd[1] == 'off':
            v = 0
        else:
            print('Error ', cmd[1])
            break
    elif cmd[0] == 'toggle':
        x1 = int(cmd[1])
        y1 = int(cmd[2])
        x2 = int(cmd[4])
        y2 = int(cmd[5])
        v = 2
    print(cmd)
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            # lightTurnsOn = (v == 1)
            # lightWasOn = map.get(x, {}).get(y, 0) == 1
            lightTurnsOn = (v != 0)
            lightWasOn = map.get(x, {}).get(y, 0) != 0
            if lightTurnsOn and not lightWasOn:
                count += 1
            elif not lightTurnsOn and lightWasOn:
                count -= 1
            map[x] = map.get(x, {})
            map[x][y] = v

print(count)

# for x in range(0,6):
#     line = ''
#     for y in range(0,6):
#         line += str(map[x][y]) + ' '
#     print(line)

# 8805256 too high
# 541749 -- no
# 271651 too low

