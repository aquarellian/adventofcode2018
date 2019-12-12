def get_vel(coord1, coord2):
    if coord1 == coord2:
        return 0
    elif coord1 > coord2:
        return -1
    else:
        return 1

def get_velocity(moon1, moon2):
    return get_vel(moon1.x, moon2.x), get_vel(moon1.y, moon2.y), get_vel(moon1.z, moon2.z)

def looped(moons, ethalons):
    for i in range(0, len(moons)):
        if not (moon_looped(moons[i], ethalons[i])):
            return False
    return True

def x_looped(moons, ethalons):
    return     moons[0].x == ethalons[0].x and moons[0].vx == ethalons[0].vx \
           and moons[1].x == ethalons[1].x and moons[1].vx == ethalons[1].vx \
           and moons[2].x == ethalons[2].x and moons[2].vx == ethalons[2].vx \
           and moons[3].x == ethalons[3].x and moons[3].vx == ethalons[3].vx

def y_looped(moons, ethalons):
    return moons[0].y == ethalons[0].y and moons[0].vy == ethalons[0].vy \
           and moons[1].y == ethalons[1].y and moons[1].vy == ethalons[1].vy \
           and moons[2].y == ethalons[2].y and moons[2].vy == ethalons[2].vy \
           and moons[3].y == ethalons[3].y and moons[3].vy == ethalons[3].vy

def z_looped(moons, ethalons):
    return moons[0].z == ethalons[0].z and moons[0].vz == ethalons[0].vz \
           and moons[1].z == ethalons[1].z and moons[1].vz == ethalons[1].vz \
           and moons[2].z == ethalons[2].z and moons[2].vz == ethalons[2].vz \
           and moons[3].z == ethalons[3].z and moons[3].vz == ethalons[3].vz


def moon_looped(moon, ethalon):
    return moon.x == ethalon.x and moon.vx == ethalon.vx \
     and moon.y == ethalon.y and moon.vy == ethalon.vy \
     and moon.z == ethalon.z and moon.vz == ethalon.vz

def get_energy(moon):
    px = abs(moon.x) + abs(moon.y) + abs(moon.z)
    kx = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
    return px*kx


def lcd(x1, x2, x3):
    for i in range(min(x1, x2, x3), 0, -1):
        if abs(x1 % i) == 0 and abs(x2 % i) == 0 and abs(x3 % i) == 0 :
            return i
    return 1

class Moon:
    x = 0
    y = 0
    z = 0

    vx = 0
    vy = 0
    vz = 0

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z


import load_input
content = load_input.load(2019, 12).split('\n')
# content = '<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>\n'.split('\n')
# content='<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>\n'.split('\n')
moons = []
ethalons = []


ind = 0
for line in content:
    if line != '':
        lines = line[1:-1].split(', ')
        x = int(lines[0].split('=')[1])
        y = int(lines[1].split('=')[1])
        z = int(lines[2].split('=')[1])
        moons.append(Moon(x, y, z))
        ethalons.append(Moon(x, y, z))


total_energy = 0
loopx = 0
loopy = 0
loopz = 0
while loopx == 0 or loopy == 0 or loopz == 0:
    ind+=1
    moon1 = moons[0]
    moon2 = moons[1]
    moon3 = moons[2]
    moon4 = moons[3]

    vx12, vy12, vz12 = get_velocity(moon1, moon2)
    vx13, vy13, vz13 = get_velocity(moon1, moon3)
    vx14, vy14, vz14 = get_velocity(moon1, moon4)
    vx23, vy23, vz23 = get_velocity(moon2, moon3)
    vx24, vy24, vz24 = get_velocity(moon2, moon4)
    vx34, vy34, vz34 = get_velocity(moon3, moon4)

    moon1.vx = moon1.vx + vx12 + vx13 + vx14
    moon1.vy = moon1.vy + vy12 + vy13 + vy14
    moon1.vz = moon1.vz + vz12 + vz13 + vz14
    moon1.x += moon1.vx
    moon1.y += moon1.vy
    moon1.z += moon1.vz

    moon2.vx = moon2.vx - vx12 + vx23 + vx24
    moon2.vy = moon2.vy - vy12 + vy23 + vy24
    moon2.vz = moon2.vz - vz12 + vz23 + vz24
    moon2.x += moon2.vx
    moon2.y += moon2.vy
    moon2.z += moon2.vz

    moon3.vx = moon3.vx - vx13 - vx23 + vx34
    moon3.vy = moon3.vy - vy13 - vy23 + vy34
    moon3.vz = moon3.vz - vz13 - vz23 + vz34
    moon3.x += moon3.vx
    moon3.y += moon3.vy
    moon3.z += moon3.vz

    moon4.vx = moon4.vx - vx14 - vx24 - vx34
    moon4.vy = moon4.vy - vy14 - vy24 - vy34
    moon4.vz = moon4.vz - vz14 - vz24 - vz34
    moon4.x += moon4.vx
    moon4.y += moon4.vy
    moon4.z += moon4.vz
    if loopx == 0 and x_looped(moons, ethalons):
        loopx = ind
    if loopy == 0 and y_looped(moons, ethalons):
        loopy = ind
    if loopz == 0 and z_looped(moons, ethalons):
        loopz = ind

    # print('moon1', moon1.x, moon1.y, moon1.z, moon1.vx, moon1.vy, moon1.vz)

    if ind % 1000000 == 0:
        print(ind, loopx, loopy, loopz)
    # if ind == 1000:
    #     print(get_energy(moon1) + get_energy(moon2) + get_energy(moon3) + get_energy(moon4) )
print(loopx, loopy, loopz)
print(loopx*loopy*loopz)
# 62141109744 low


att = None
for i in range(2, 2* max(loopx, loopy, loopz)+1):
    att = loopx*loopy*loopz / i
    if att == int(att) and (att % loopx == 0) and (att % loopy == 0) and (att % loopz == 0):
        print(int(att), i)

# print(loopy * loopz * 2)
# print(4686774924 % loopx, 4686774924 % loopy, 4686774924 % loopz)
# print(lcd(loopx, loopy, loopz))
# print(loopx*loopy*loopz // lcd(loopx, loopy, loopz))

# 841577049262992 high