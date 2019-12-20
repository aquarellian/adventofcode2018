class Ingredient:
    name = ''
    count = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count

def parse_ing(st):
    count, name = st.strip().split(' ')
    return Ingredient(name, int(count))

import math
def desintegrate(name, count, book, stash={}):
    # print('desintegrating', count, name)
    if stash.get(name, 0) > 0:
        if stash[name] >= count:
            stash[name] = stash[name] - count
            # print('unstashed', count, name)
            return 0, stash
        else:
            count -= stash[name]
            # print('unstashed', stash[name], name)
            stash[name] = 0

    if 'ORE' == name:
        return count, stash

    reaction = book[name]
    reaction_outcome = book[name][0].count
    reactions_count = 1 if reaction_outcome > count else int(math.ceil(float(count) / reaction_outcome))
    reactions_leftover = reactions_count * reaction_outcome - count
    # print('need', count, 'by', reactions_count,'reactions producing', reaction_outcome, 'each, leftover=', reactions_leftover)
    ore = 0
    while reactions_count > 0:
        for i in range(1, len(reaction)):
            ing = reaction[i].name
            cnt = reaction[i].count
            o, s = desintegrate(ing, cnt, book, stash)
            ore += o
        reactions_count-=1
    # print('stashing', reactions_leftover, name)
    if reactions_leftover >= 0:
        stash[name] = stash.get(name, 0) + reactions_leftover
    # else:

    return ore, stash


import load_input
book = {}
content = load_input.load(2019, 14).split('\n')

# content = '10 ORE => 10 A\n1 ORE => 1 B\n7 A, 1 B => 1 C\n7 A, 1 C => 1 D\n7 A, 1 D => 1 E\n7 A, 1 E => 1 FUEL\n'.split('\n')
# content='157 ORE => 5 NZVS\n165 ORE => 6 DCFZ\n44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n179 ORE => 7 PSHF\n177 ORE => 5 HKGWZ\n7 DCFZ, 7 PSHF => 2 XJWVT\n165 ORE => 2 GPVTF\n3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT\n'.split('\n')
for line in content:
    if line != '':
        react2res = line.split('=>')
        res = parse_ing(react2res[1])
        book[res.name] = [res]

        for ing in react2res[0].split(','):
            _ing = parse_ing(ing)
            book[res.name].append(_ing)

fuel = book['FUEL']
if fuel[0].count != 1:
    print('want more fuel!')

ore,stash  = desintegrate('FUEL', 1, book)
print(ore)
# ore,stash  = desintegrate('FUEL', 1, book, {})
# print(ore)
rcnt = (float(ore) / float(1))
# 783895

def is_stash_empty(stash):
    for k, v in stash.items():
        if v != 0:
            return False
    return True

# 1275681 low
# 1275681
# 1275683 low
# 1277654 wrong
# 1276192
# 1280549wrong
# 1897500
# 1897528

# 1891295 ->
# 1891547
# 1893300 wrong
# 1894516 !!
 # 1894518
#  1894707
# 1895622
# 1895730 wrong
# 1896163 wrong


# count100, stash = desintegrate('FUEL', 100, book)

# print('1:', ore, '100:', count100)
opt = 527380.7259259259
ocnt = 540
print(ore, 1, rcnt)

# for cnt in range(500, 550):
#     ore, stash = desintegrate('FUEL', cnt, book, {})
#     rcnt = (float(ore) / float(cnt))
#     if rcnt < opt:
#         print(ore, cnt, rcnt)
#         opt = rcnt
#         ocnt = cnt
# print('optimal:', ocnt, opt)


stash = {}
count = 0
remains = 1000000000000
while remains > (1000000000000 % ocnt) + ocnt:
     ore, stash = desintegrate('FUEL', ocnt, book, stash)
     remains -= ore
     count += ocnt

# count = ocnt * (1000000000000 // ore)
# remains = 1000000000000 % ore
# print(count)
while remains > 0:
    o, stash = desintegrate('FUEL', 1, book, stash)
    remains -= o
    count += 1
    print(count, remains)
print(count-1)

#1000000000025


# count -=20000# print(count)
# remains = 1000000000000 - ore*count
# while remains > 0:
#     if count > 1280549:
#         print(count, remains)
#     o, stash = desintegrate('FUEL', 1, book, stash)
#     remains -= o
#     count += 1
#
# print(count-1)

