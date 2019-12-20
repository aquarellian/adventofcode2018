def fuel_level(x, y, serial):
    rack_id = x + 10
    pow_l = rack_id * (rack_id * y + serial)
    hundreds = int(pow_l / 100) % 10
    return hundreds - 5


# print(fuel_level(3,5,8))
# print(fuel_level(122,79,57))
# print(fuel_level(217,196,39))
# print(fuel_level(101,153,71))

# serial = 18  # test ok
# serial = 42  # test ok
serial = 7403
pow2coord = {}
for x in range(1, 299):
    for y in range(1, 299):
        power = fuel_level(x, y, serial) + fuel_level(x + 1, y, serial) + fuel_level(x + 2, y, serial) + \
                fuel_level(x, y + 1, serial) + fuel_level(x + 1, y + 1, serial) + fuel_level(x + 2, y + 1, serial) + \
                fuel_level(x, y + 2, serial) + fuel_level(x + 1, y + 2, serial) + fuel_level(x + 2, y + 2, serial)
        pow2coord[power] = [x, y]

max_pow = max(pow2coord.keys())
print(max_pow)
res = pow2coord[max_pow]
print(res)

