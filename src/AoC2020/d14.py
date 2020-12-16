def apply_mask(val, mask):
    bval = list('{0:036b}'.format(val))
    for ind in range(len(mask)):
        if mask[ind] != 'X':
            bval[ind] = mask[ind]
    return int("".join(bval), 2)


# task 1
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d14.txt") as f:
    content = f.readlines()
    res = dict()
    for line in content:
        if line.startswith('mask'):
            mask = line[line.index('=') + 2:].strip()
        else:
            ind = int(line[line.index('[') + 1: line.index(']')])
            val = int(line[line.index('=') + 2:])
            res[ind] = apply_mask(val, mask)
    s = 0
    for v in res.values():
        s += v
    print(s)


# task 2

def apply_mask_2(val, mask):
    bval = list('{0:036b}'.format(val))
    for ind in range(len(mask)):
        if mask[ind] != 'X':
            bval[ind] = int(mask[ind]) | int(bval[ind])
        else:
            bval[ind] = 'X'
    return "".join([str(x) for x in bval])


def get_possible_addresses(mask):
    res = set()
    if 'X' not in mask:
        return set(mask)
    ind = mask.rindex('X')


class command:
    index = ''
    value = 0

    def __init__(self, index, value):
        self.index = index
        self.value = value


def clashes(new_ind, old_ind):
    for i in range(len(old_ind)):
        if (new_ind[i] != 'X' and old_ind[i] != 'X' or new_ind == 'X') and not new_ind[i] == old_ind[i]:
            return False  # there's at least 1 digit different
    return True


def maskit(new_ind, old_ind):
    upd_old = list(old_ind)
    for i in range(len(old_ind)):
        if not new_ind[i] == 'X' and old_ind[i] == 'X':
            upd_old[i] = str(int(not (bool(int(new_ind[i])))))

    return "".join(upd_old)


def calc_inds(cache):
    res = set()
    for v in cache:
        if 'X' in v:
            mod0 = v[:v.index('X')] + '0' + v[v.index('X') + 1:]
            mod1 = v[:v.index('X')] + '1' + v[v.index('X') + 1:]
            subcache = set()
            subcache.add(mod0)
            subcache.add(mod1)
            res.update(calc_inds(subcache))
        else:
            res.add(v)
    return res


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d14.txt") as f:
    content = f.readlines()
    res = dict()
    l = list()
    for line in content:
        if line.startswith('mask'):
            mask = line[line.index('=') + 2:].strip()
        else:
            ind = int(line[line.index('[') + 1: line.index(']')])
            val = int(line[line.index('=') + 2:])
            funny_ind = apply_mask_2(ind, mask)
            l.append(funny_ind)
            res[funny_ind] = val

    s = 0
    applied = set()

    for ind in reversed(l):
        cache = set()
        cache.add(ind)
        possible = calc_inds(cache)
        # print(ind, possible)
        cnt = 0
        for i in possible:
            if i not in applied:
                cnt += 1
                applied.add(i)
        s += cnt * res[ind]
    print(s)
    import math
    # for ind, val in res.items():
    #     # options = math.pow(2, ind.count('X'))
    #     # s += options * val
    # print(s)

# 29579448737 low
# 1865645579756 low
# 2867723735362 low
# 2900994392308