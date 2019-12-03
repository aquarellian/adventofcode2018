def pipe(cmds):
    x = 0
    y = 0
    lines = []
    for cmd in cmds:
        dir = cmd[0]
        lng = int(cmd[1:])
        x1 = x
        y1 = y
        if dir == 'R':
            x1 = x + lng
        elif dir == 'L':
            x1 = x - lng
        elif dir == 'U':
            y1 = y + lng
        elif dir == 'D':
            y1 = y - lng
        else:
            print('ERROR Direction unknown ', dir)
        lines.append([x, y, x1, y1])
        x = x1
        y = y1
    return lines

def cross(line1, line2):
    x11 = line1[0]
    y11 = line1[1]
    x12 = line1[2]
    y12 = line1[3]
    x21 = line2[0]
    y21 = line2[1]
    x22 = line2[2]
    y22 = line2[3]
    crossx = min(x11, x12) <= x21 <= max(x11, x12) or \
             min(x11, x12) <= x22 <= max(x11, x12) or \
             min(x21, x22) <= x11 <= max(x21, x22) or \
             min(x21, x22) <= x12 <= max(x21, x22)
    crossy = min(y11, y12) <= y21 <= max(y11, y12) or \
             min(y11, y12) <= y22 <= max(y11, y12) or \
             min(y21, y22) <= y11 <= max(y21, y22) or \
             min(y21, y22) <= y12 <= max(y21, y22)
    if crossx and crossy:
        interx = [x11, x12, x21, x22]
        interx.remove(min(interx))
        interx.remove(max(interx))

        intery = [y11, y12, y21, y22]
        intery.remove(min(intery))
        intery.remove(max(intery))

        return min(interx), min(intery)
    else:
        return None, None

import load_input
# content = load_input.load(2019, 3)
# content = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
# content = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
content = 'R8,U5,L5,D3\nU7,R6,D4,L4'
linelist = []
for v in content.split('\n'):
    print(v)
    linelist.append(pipe(v.split(',')))
steps = 0
print(linelist)
if len(linelist) == 2:
    line1 = linelist[0]
    print(line1)
    line2 = linelist[1]
    print(line2)
    for a in line1:
        for b in line2:
            interx, intery = cross(a, b)
            if interx is not None and intery is not None and (steps == 0 or a[4] + b[4] < steps):
                steps = a[4] + b[4]

print(steps)


#545 low