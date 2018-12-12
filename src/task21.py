def fuel_level(x, y, serial):
    rack_id = x + 10
    pow_l = rack_id * (rack_id * y + serial)
    hundreds = int(pow_l / 100) % 10
    return hundreds - 5


def grid_val(grid, x,y,z):
    if len(grid[x][y]) == 0:
        return sum([grid[x+i][y+j] for i, j in itertools.product(range(0, z+1), range(0, z+1))])
    else:
        maxkey = max([key for key in grid[x][y].keys() if key <= z])
        seq = [grid[x+i][y+j][1] for i, j in itertools.product(range(maxkey+1, z+1), range(maxkey+1, z+1))]

        return grid[x][y][maxkey] + (sum(seq) if len(seq) > 0 else 0)


serial = 18  # test
# serial = 42  # test
# serial = 7403 # res
grid = {}
max_pow = 0
max_data = [0, 0, 0]
for x in range(1, 301):
    if grid.get(x, None) is None:
        grid[x] = {}
    for y in range(1, 301):
        if grid[x].get(y, None) is None:
            grid[x][y] = {}
        grid[x][y][1] = fuel_level(x, y, serial)
        if grid[x][y][1] > max_pow:
            max_pow = grid[x][y][1]
            max_data = [x, y, 1]



import itertools
for x in range(1, 301):
    for y in range(1, 301):
        # z = 3
        for z in range(2, 301 - max(x, y)):
        # for z in range(3, 3):
            grid[x][y][z] = grid_val(grid, x,y,z)
            # test = fuel_level(x, y, serial) + fuel_level(x + 1, y, serial) + fuel_level(x + 2, y, serial) + \
            #        fuel_level(x, y + 1, serial) + fuel_level(x + 1, y + 1, serial) + fuel_level(x + 2, y + 1, serial) + \
            #        fuel_level(x, y + 2, serial) + fuel_level(x + 1, y + 2, serial) + fuel_level(x + 2, y + 2, serial)
            # if z == 3 and test != grid[x][y][z]:
            #     print('discrepancy!')
            #     print(test)
            #     print(grid[x][y][z])

            if grid[x][y][z] > max_pow:
                max_pow = grid[x][y][z]
                max_data = [x, y, z]

print(grid[90][269][16])

print(max_pow)
print(max_data)

