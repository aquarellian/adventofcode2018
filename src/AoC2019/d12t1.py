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
        if not (moons[i].x == ethalons[i].x and moons[i].vx == ethalons[i].vx
                and moons[i].y == ethalons[i].y and moons[i].vy == ethalons[i].vy
                and moons[i].z == ethalons[i].z and moons[i].vz == ethalons[i].vz):
            return False
    return True

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
moons = []
ind = 0
for line in content:
    if line != '':
        lines = line[1:-1].split(', ')
        x = int(lines[0].split('=')[1])
        y = int(lines[1].split('=')[1])
        z = int(lines[2].split('=')[1])
        moons.append(Moon(x, y, z))


total_energy = 0
for ind in range(0, 1000):
    ind+=1

    for i in range(0, len(moons)):
        moon1 = moons[i]
        for j in range(i+1, len(moons)):
            moon2 = moons[j]
            vx, vy, vz = get_velocity(moon1, moon2)
            moon1.vx += vx
            moon1.vy += vy
            moon1.vz += vz
            moon2.vx -= vx
            moon2.vy -= vy
            moon2.vz -= vz
    for moon in moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz
        if ind == 1000:
            px = abs(moon.x) + abs(moon.y) + abs(moon.z)
            kx = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
            total_energy += (kx*px)
print(total_energy)