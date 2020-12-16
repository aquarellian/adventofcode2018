import copy


def occupied(x, y, array):
    return 0 <= y < len(array) and 0 <= x < len(array[y]) and array[y][x] == '#'

def vacant(x, y, array):
    return 0 <= y < len(array) and 0 <= x < len(array[y]) and array[y][x] == 'L'


def dir_occupied(x, y, xtr, ytr, array):
    while 0 <= y < len(array) and 0 <= x < len(array[y]):
        x = xtr(x)
        y = ytr(y)
        if occupied(x, y, array):
            return True
        elif vacant(x, y, array):
            return False
    return False


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def nop(x):
    return x

def can_sit(x, y, array):
    if array[y][x] == '.' or array[y][x] == '#':
        return False
    return not (occupied(x - 1, y - 1, array) or occupied(x, y - 1, array) or occupied(x + 1, y - 1, array) or
                occupied(x - 1, y, array) or occupied(x + 1, y, array) or
                occupied(x - 1, y + 1, array) or occupied(x, y + 1, array) or occupied(x + 1, y + 1, array))



def can_sit2(x, y, array):
    if array[y][x] == '.' or array[y][x] == '#':
        return False
    return not (dir_occupied(x, y, dec, dec, array) or dir_occupied(x, y, nop, dec, array) or dir_occupied(x, y, inc,
                                                                                                           dec,
                                                                                                           array) or
                dir_occupied(x, y, dec, nop, array) or dir_occupied(x, y, inc, nop, array) or
                dir_occupied(x, y, dec, inc, array) or dir_occupied(x, y, nop, inc, array) or dir_occupied(x, y, inc,
                                                                                                           inc, array))


def should_leave(x, y, array):
    if array[y][x] == '.' or array[y][x] == 'L':
        return False
    return int(occupied(x - 1, y - 1, array)) + int(occupied(x, y - 1, array)) + int(occupied(x + 1, y - 1, array)) + \
           int(occupied(x - 1, y, array)) + int(occupied(x + 1, y, array)) + \
           int(occupied(x - 1, y + 1, array)) + int(occupied(x, y + 1, array)) + int(occupied(x + 1, y + 1, array)) > 3


def should_leave2(x, y, array):
    if array[y][x] == '.' or array[y][x] == 'L':
        return False
    return int(dir_occupied(x, y, dec, dec, array)) + int(dir_occupied(x, y, nop, dec, array)) + int(
        dir_occupied(x, y, inc, dec, array)) + \
           int(dir_occupied(x, y, dec, nop, array)) + int(dir_occupied(x, y, inc, nop, array)) + \
           int(dir_occupied(x, y, dec, inc, array)) + int(dir_occupied(x, y, nop, inc, array)) + int(
        dir_occupied(x, y, inc, inc, array)) > 4


def print_arr(array):
    for line in array:
        print("".join(line))


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d11.txt") as f:
    content = f.readlines()
    content = [list(line.strip()) for line in content]
    changed = True
    i = 0
    while changed:
        i+=1
        changed = False
        snapshot = copy.deepcopy(content)
        print(i)
        # print_arr(content)
        # print("\n")
        for y in range(len(snapshot)):
            for x in range(len(snapshot[y])):
                if can_sit2(x, y, snapshot):
                    content[y][x] = '#'
                    changed = True
                if should_leave2(x, y, snapshot):
                    content[y][x] = 'L'
                    changed = True
    # print_arr(content)
    # print()

    occupied_num = 0
    for y in range(len(content)):
        occupied_num += content[y].count('#')
    print(occupied_num)
