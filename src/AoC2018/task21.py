def fuel_level(x, y, serial):
    rack_id = x + 10
    pow_l = rack_id * (rack_id * y + serial)
    hundreds = int(pow_l / 100) % 10
    return hundreds - 5


# def grid_val(grid, x,y,z):
#     if len(grid[x][y]) == 0:
#         print('ERROR')
#         return sum([grid[x+i][y+j] for i, j in itertools.product(range(0, z+1), range(0, z+1))])
#     else:
#         maxkey = max([key for key in grid[x][y].keys() if key <= z])
#         sum = grid[x][y][maxkey]
#         for i in range(1, z - maxkey + 1):
#             for j in range(1, z - maxkey + 1):
#                 sum += grid[x+i][y+j][1]
#         # seq = [grid[x+i][y+j][1] for i, j in itertools.product(range(1, z - maxkey + 1), range(1, z - maxkey + 1))]
#         return sum #grid[x][y][maxkey] + (sum(seq) if len(seq) > 0 else 0)

# border = 301
border = 301
# serial = 18  # test ok
# serial = 42  # test ok
serial = 7403 # res
grid = {}
max_pow = 0
max_data = [0, 0, 0]
for x in range(1, border):
    if grid.get(x, None) is None:
        grid[x] = {}
    for y in range(1, border):
        if grid[x].get(y, None) is None:
            grid[x][y] = {}
        grid[x][y][1] = fuel_level(x, y, serial)
        if grid[x][y][1] > max_pow:
            max_pow = grid[x][y][1]
            max_data = [x, y, 1]

for x in range(1, border):
    for y in range(1, border):
        for z in range(2, border - max(x, y) + 1):
            val = grid[x][y][z-1]
            for i in range(y, y+z-1):
                val += grid[x+z-1][i][1]
            for i in range(x, x+z-1):
                val += grid[i][y+z-1][1]
            val += grid[x+z-1][y+z-1][1]

            grid[x][y][z] = val
            # grid[x][y][z] = grid_val(grid, x, y, z)
            if grid[x][y][z] > max_pow:
                max_pow = grid[x][y][z]
                max_data = [x, y, z]


print(max_pow)
print(max_data)

